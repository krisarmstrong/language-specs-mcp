#!/usr/bin/env python3
"""Diagnose fetch connectivity and TLS verification issues."""

from __future__ import annotations

import os
import ssl
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_URLS = [
    "https://www.google.com",
    "https://eslint.org/docs/latest/rules/",
    "https://developer.mozilla.org/en-US/docs/Web/API",
]


def build_context() -> ssl.SSLContext | None:
    if os.getenv("FETCH_INSECURE") == "1":
        return ssl._create_unverified_context()
    cafile = os.getenv("SSL_CERT_FILE") or os.getenv("REQUESTS_CA_BUNDLE")
    if cafile:
        return ssl.create_default_context(cafile=cafile)
    return None


def diagnose(url: str, timeout: float = 15.0) -> None:
    context = build_context()
    request = Request(url, headers={"User-Agent": "specforge-mcp/diagnose"})
    start = time.monotonic()
    try:
        with urlopen(request, timeout=timeout, context=context) as response:
            elapsed = time.monotonic() - start
            status = getattr(response, "status", "unknown")
            content_type = response.headers.get("Content-Type", "unknown")
            sys.stdout.write(
                f"[ok] {url} status={status} type={content_type} time={elapsed:.2f}s\n"
            )
    except HTTPError as exc:
        elapsed = time.monotonic() - start
        sys.stdout.write(
            f"[http] {url} status={exc.code} reason={exc.reason} time={elapsed:.2f}s\n"
        )
    except (URLError, ssl.SSLError, OSError) as exc:
        elapsed = time.monotonic() - start
        message = str(exc)
        if "CERTIFICATE_VERIFY_FAILED" in message:
            message = (
                f"{message} (set SSL_CERT_FILE or REQUESTS_CA_BUNDLE, "
                "or FETCH_INSECURE=1 to bypass verification)"
            )
        sys.stdout.write(f"[fail] {url} error={message} time={elapsed:.2f}s\n")


def main() -> None:
    urls = sys.argv[1:] or DEFAULT_URLS
    for url in urls:
        diagnose(url)


if __name__ == "__main__":
    main()
