#!/usr/bin/env python3
"""Shared helpers for fetch/maintenance scripts."""

from __future__ import annotations

import html
import logging
import os
import re
import shutil
import ssl
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
SPECS_DIR = ROOT_DIR / "specs"

FETCH_SCOPE = os.getenv("FETCH_SCOPE", "all")
USER_AGENT = os.getenv("FETCH_USER_AGENT", "specforge-mcp/1.0")

CURL_RETRY = int(os.getenv("CURL_RETRY", "3"))
CURL_RETRY_DELAY = float(os.getenv("CURL_RETRY_DELAY", "2"))
CURL_CONNECT_TIMEOUT = float(os.getenv("CURL_CONNECT_TIMEOUT", "10"))
CURL_MAX_TIME = float(os.getenv("CURL_MAX_TIME", "120"))

PANDOC_TIMEOUT = float(os.getenv("PANDOC_TIMEOUT", "30"))

LOG_LEVEL = os.getenv("SPECFORGE_LOG_LEVEL", os.getenv("LOG_LEVEL", "INFO")).upper()
LOG_FORMAT = os.getenv(
    "SPECFORGE_LOG_FORMAT",
    "%(asctime)s %(levelname)s %(message)s",
)
LOG_DATE_FORMAT = os.getenv("SPECFORGE_LOG_DATE_FORMAT", "%Y-%m-%dT%H:%M:%S%z")
_LOGGER_CONFIGURED = False


@dataclass(frozen=True)
class FetchError(Exception):
    url: str
    message: str

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.url}: {self.message}"


class _SimpleMarkdownParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._out: list[str] = []
        self._ignore_depth = 0
        self._in_pre = 0
        self._in_code = 0
        self._inline_code: list[str] = []
        self._link_href: str | None = None
        self._link_text: list[str] = []
        self._list_stack: list[tuple[str, int]] = []

    def _tail(self) -> str:
        return "".join(self._out[-3:])

    def _ensure_newline(self) -> None:
        if not self._out:
            return
        if not self._tail().endswith("\n"):
            self._out.append("\n")

    def _ensure_blank_line(self) -> None:
        if not self._out:
            return
        tail = self._tail()
        if tail.endswith("\n\n"):
            return
        if not tail.endswith("\n"):
            self._out.append("\n")
        self._out.append("\n")

    def _append(self, text: str) -> None:
        if text:
            self._out.append(text)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self._ignore_depth:
            if tag in ("script", "style", "noscript", "svg"):
                self._ignore_depth += 1
            return
        if tag in ("script", "style", "noscript", "svg"):
            self._ignore_depth += 1
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self._ensure_blank_line()
            self._append("#" * level + " ")
            return
        if tag == "p":
            self._ensure_blank_line()
            return
        if tag == "br":
            self._append("\n")
            return
        if tag in ("ul", "ol"):
            self._list_stack.append((tag, 1))
            self._ensure_blank_line()
            return
        if tag == "li":
            self._ensure_newline()
            indent = "  " * max(0, len(self._list_stack) - 1)
            if self._list_stack:
                kind, index = self._list_stack[-1]
                if kind == "ol":
                    bullet = f"{index}."
                    self._list_stack[-1] = (kind, index + 1)
                else:
                    bullet = "-"
            else:
                bullet = "-"
            self._append(f"{indent}{bullet} ")
            return
        if tag == "pre":
            self._ensure_blank_line()
            self._append("```\n")
            self._in_pre += 1
            return
        if tag == "code":
            if self._in_pre:
                self._in_code += 1
            else:
                self._in_code += 1
                self._inline_code = []
            return
        if tag == "a":
            href = dict(attrs).get("href") if attrs else None
            if href:
                self._link_href = href
                self._link_text = []
            return

    def handle_endtag(self, tag: str) -> None:
        if self._ignore_depth:
            if tag in ("script", "style", "noscript", "svg"):
                self._ignore_depth = max(0, self._ignore_depth - 1)
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._ensure_blank_line()
            return
        if tag == "p":
            self._ensure_blank_line()
            return
        if tag in ("ul", "ol"):
            if self._list_stack:
                self._list_stack.pop()
            self._ensure_blank_line()
            return
        if tag == "pre":
            if self._in_pre:
                self._in_pre -= 1
            self._ensure_newline()
            self._append("```\n")
            self._ensure_blank_line()
            return
        if tag == "code":
            if self._in_pre:
                self._in_code = max(0, self._in_code - 1)
                return
            if self._in_code:
                self._in_code -= 1
                text = "".join(self._inline_code).strip()
                if text:
                    self._append(f"`{text}`")
                self._inline_code = []
            return
        if tag == "a":
            if self._link_href is None:
                return
            text = "".join(self._link_text).strip()
            href = self._link_href
            if text:
                self._append(f"[{text}]({href})")
            else:
                self._append(href)
            self._link_href = None
            self._link_text = []

    def handle_data(self, data: str) -> None:
        if self._ignore_depth or not data:
            return
        if self._in_pre:
            self._append(data)
            return
        text = html.unescape(data)
        if self._link_href is not None:
            self._link_text.append(text)
            return
        if self._in_code:
            self._inline_code.append(text)
            return
        text = re.sub(r"\s+", " ", text)
        if text.strip():
            self._append(text)


def _simple_html_to_markdown(html_text: str) -> str:
    parser = _SimpleMarkdownParser()
    parser.feed(html_text)
    parser.close()
    content = "".join(parser._out)
    content = re.sub(r"\n{3,}", "\n\n", content).strip()
    return f"{content}\n" if content else ""


def _pandoc_available() -> bool:
    return shutil.which("pandoc") is not None


def _configure_logger() -> logging.Logger:
    global _LOGGER_CONFIGURED
    if not _LOGGER_CONFIGURED:
        logging.basicConfig(
            level=LOG_LEVEL,
            format=LOG_FORMAT,
            datefmt=LOG_DATE_FORMAT,
        )
        _LOGGER_CONFIGURED = True
    return logging.getLogger("specforge")


def fetch_section(section: str) -> bool:
    return FETCH_SCOPE == "all" or FETCH_SCOPE == section


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")


def write_stub(path: Path, title: str, url: str) -> None:
    write_text(path, f"# {title}\n\nSee: {url}\n")


def write_fetched_at(spec_dir: Path) -> None:
    write_text(spec_dir / ".fetched-at", f"{utc_now()}\n")


def stamp_versions() -> None:
    python_script = SCRIPT_DIR / "stamp-versions.py"
    node_script = SCRIPT_DIR / "stamp-versions.mjs"
    command = None
    if python_script.exists():
        command = [sys.executable, str(python_script)]
    elif node_script.exists():
        command = ["node", str(node_script)]
    if not command:
        return
    try:
        subprocess.run(
            command,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        return


def _request(url: str) -> Request:
    headers = {"User-Agent": USER_AGENT}
    token = os.getenv("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    return Request(url, headers=headers)


def _ssl_context() -> ssl.SSLContext | None:
    if os.getenv("FETCH_INSECURE") == "1":
        return ssl._create_unverified_context()
    cafile = os.getenv("SSL_CERT_FILE") or os.getenv("REQUESTS_CA_BUNDLE")
    if cafile:
        return ssl.create_default_context(cafile=cafile)
    try:
        import certifi
    except ImportError:
        return None
    return ssl.create_default_context(cafile=certifi.where())
    return None


def _format_fetch_error(exc: Exception) -> str:
    message = str(exc)
    if "CERTIFICATE_VERIFY_FAILED" in message:
        return (
            f"{message} (set SSL_CERT_FILE or REQUESTS_CA_BUNDLE to your CA bundle, "
            "or FETCH_INSECURE=1 to bypass verification)"
        )
    return message


def fetch_url(url: str) -> str:
    last_error: Exception | None = None
    context = _ssl_context()
    for attempt in range(CURL_RETRY + 1):
        try:
            timeout = CURL_MAX_TIME if CURL_MAX_TIME > 0 else CURL_CONNECT_TIMEOUT
            start = time.monotonic()
            with urlopen(_request(url), timeout=timeout, context=context) as response:
                data = response.read()
            elapsed = time.monotonic() - start
            if CURL_MAX_TIME > 0 and elapsed > CURL_MAX_TIME:
                raise TimeoutError(f"fetch exceeded {CURL_MAX_TIME}s")
            return data.decode("utf-8", errors="replace")
        except (OSError, URLError, TimeoutError, ssl.SSLError) as exc:
            last_error = exc
            if attempt >= CURL_RETRY:
                break
            time.sleep(CURL_RETRY_DELAY)
    raise FetchError(url, _format_fetch_error(last_error) if last_error else "unknown error")


def fetch_bytes(url: str) -> bytes:
    last_error: Exception | None = None
    context = _ssl_context()
    for attempt in range(CURL_RETRY + 1):
        try:
            timeout = CURL_MAX_TIME if CURL_MAX_TIME > 0 else CURL_CONNECT_TIMEOUT
            start = time.monotonic()
            with urlopen(_request(url), timeout=timeout, context=context) as response:
                data = response.read()
            elapsed = time.monotonic() - start
            if CURL_MAX_TIME > 0 and elapsed > CURL_MAX_TIME:
                raise TimeoutError(f"fetch exceeded {CURL_MAX_TIME}s")
            return data
        except (OSError, URLError, TimeoutError, ssl.SSLError) as exc:
            last_error = exc
            if attempt >= CURL_RETRY:
                break
            time.sleep(CURL_RETRY_DELAY)
    raise FetchError(url, _format_fetch_error(last_error) if last_error else "unknown error")


def extract_main(html: str) -> str:
    match = re.search(r"<main[^>]*>(.*?)</main>", html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(0)
    article = re.search(r"<article[^>]*>(.*?)</article>", html, re.IGNORECASE | re.DOTALL)
    return article.group(0) if article else html


def html_to_markdown(html: str, output: Path) -> bool:
    ensure_dir(output.parent)
    if _pandoc_available():
        try:
            subprocess.run(
                ["pandoc", "-f", "html", "-t", "markdown", "-o", str(output)],
                input=html.encode("utf-8"),
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=PANDOC_TIMEOUT,
            )
            return True
        except (OSError, subprocess.SubprocessError):
            pass
    markdown = _simple_html_to_markdown(html)
    if markdown:
        write_text(output, markdown)
        return True
    return False


def fetch_markdown(url: str, output: Path, title: str) -> None:
    try:
        html = fetch_url(url)
        main = extract_main(html)
        if html_to_markdown(main, output):
            return
    except FetchError:
        pass
    write_stub(output, title, url)


def fetch_markdown_or_html(
    url: str,
    output_md: Path,
    output_html: Path,
    title: str,
) -> None:
    try:
        html = fetch_url(url)
    except FetchError:
        write_stub(output_md, title, url)
        return
    main = extract_main(html)
    if html_to_markdown(main, output_md):
        return
    write_text(output_html, html)


def find_unique(html: str, pattern: str) -> list[str]:
    matches = re.findall(pattern, html)
    return sorted({m for m in matches if m})


def is_prerelease_version(version: str) -> bool:
    value = version.lower()
    if re.search(r"(?:^|[.-]|\d)a\d", value):
        return True
    if re.search(r"(?:^|[.-]|\d)b\d", value):
        return True
    if re.search(r"(?:^|[.-]|\d)rc\d", value):
        return True
    tokens = (
        "alpha",
        "beta",
        "preview",
        "pre",
        "nightly",
        "dev",
        "snapshot",
        "canary",
        "experimental",
        "prerelease",
    )
    return any(token in value for token in tokens)


def log(message: str, level: str = "info") -> None:
    logger = _configure_logger()
    normalized = level.lower()
    if normalized == "warning":
        logger.warning(message)
    elif normalized == "error":
        logger.error(message)
    else:
        logger.info(message)


def run_command(command: list[str], timeout: float | None = None) -> None:
    subprocess.run(command, check=True, timeout=timeout)


def join_lines(lines: Iterable[str]) -> str:
    return "\n".join(lines) + "\n"


def write_template(template_path: Path, output: Path) -> None:
    if not template_path.exists():
        return
    write_text(output, template_path.read_text(encoding="utf-8"))
