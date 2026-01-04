#!/usr/bin/env python3
"""Shared helpers for fetch/maintenance scripts."""

from __future__ import annotations

import os
import re
import ssl
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
SPECS_DIR = ROOT_DIR / "specs"

FETCH_SCOPE = os.getenv("FETCH_SCOPE", "all")
USER_AGENT = os.getenv("FETCH_USER_AGENT", "language-specs-mcp/1.0")

CURL_RETRY = int(os.getenv("CURL_RETRY", "3"))
CURL_RETRY_DELAY = float(os.getenv("CURL_RETRY_DELAY", "2"))
CURL_CONNECT_TIMEOUT = float(os.getenv("CURL_CONNECT_TIMEOUT", "10"))
CURL_MAX_TIME = float(os.getenv("CURL_MAX_TIME", "120"))

PANDOC_TIMEOUT = float(os.getenv("PANDOC_TIMEOUT", "30"))


@dataclass(frozen=True)
class FetchError(Exception):
    url: str
    message: str

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.url}: {self.message}"


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
    return Request(url, headers={"User-Agent": USER_AGENT})


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
    return match.group(0) if match else html


def html_to_markdown(html: str, output: Path) -> bool:
    ensure_dir(output.parent)
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


def log(message: str) -> None:
    sys.stdout.write(f"{message}\n")
    sys.stdout.flush()


def run_command(command: list[str], timeout: float | None = None) -> None:
    subprocess.run(command, check=True, timeout=timeout)


def join_lines(lines: Iterable[str]) -> str:
    return "\n".join(lines) + "\n"


def write_template(template_path: Path, output: Path) -> None:
    if not template_path.exists():
        return
    write_text(output, template_path.read_text(encoding="utf-8"))
