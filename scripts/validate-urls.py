#!/usr/bin/env python3
"""Validate all URLs in specs and detect redirects/failures.

This script:
1. Reads sources.json from each language directory
2. Validates each URL with HTTP HEAD requests
3. Detects permanent redirects (301) for URL updates
4. Outputs validation results to url-status.json
"""

from __future__ import annotations

import json
import os
import ssl
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import UTC, datetime
from threading import Lock
from typing import Any, Literal
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from _common import SPECS_DIR, log

ROOT_DIR = SPECS_DIR.parent
OUTPUT_FILE = ROOT_DIR / "docs" / "site" / "url-status.json"
MAX_WORKERS = int(os.getenv("URL_VALIDATE_WORKERS", "10"))
TIMEOUT = float(os.getenv("URL_VALIDATE_TIMEOUT", "15"))
USER_AGENT = os.getenv("FETCH_USER_AGENT", "specforge-mcp/1.0 (url-validator)")

# Per-domain rate limiting (seconds between requests to same domain)
RATE_LIMIT_DEFAULT = float(os.getenv("URL_RATE_LIMIT", "0.5"))
RATE_LIMIT_DOMAINS: dict[str, float] = {
    "github.com": 2.0,  # GitHub is aggressive with rate limiting
    "api.github.com": 2.0,
    "raw.githubusercontent.com": 1.0,
    "developer.mozilla.org": 0.3,
    "eslint.org": 0.5,
}


class DomainRateLimiter:
    """Thread-safe per-domain rate limiter."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._last_request: dict[str, float] = {}

    def wait_for_domain(self, url: str) -> None:
        """Wait if necessary before making a request to this domain."""
        try:
            domain = urlparse(url).netloc.lower()
        except Exception:
            return

        delay = RATE_LIMIT_DOMAINS.get(domain, RATE_LIMIT_DEFAULT)
        if delay <= 0:
            return

        with self._lock:
            now = time.monotonic()
            last = self._last_request.get(domain, 0)
            wait_time = delay - (now - last)

            if wait_time > 0:
                time.sleep(wait_time)

            self._last_request[domain] = time.monotonic()


# Global rate limiter instance
_rate_limiter = DomainRateLimiter()


@dataclass
class URLResult:
    """Result of validating a single URL."""

    url: str
    status: Literal["ok", "redirect", "error", "timeout"]
    http_code: int | None = None
    redirect_url: str | None = None
    error_message: str | None = None
    response_time_ms: int | None = None
    checked_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    def to_dict(self) -> dict[str, str | int | None]:
        result: dict[str, str | int | None] = {
            "url": self.url,
            "status": self.status,
            "checkedAt": self.checked_at,
        }
        if self.http_code is not None:
            result["httpCode"] = self.http_code
        if self.redirect_url:
            result["redirectUrl"] = self.redirect_url
        if self.error_message:
            result["error"] = self.error_message
        if self.response_time_ms is not None:
            result["responseTimeMs"] = self.response_time_ms
        return result


def build_ssl_context() -> ssl.SSLContext | None:
    """Build SSL context with optional cert bundle."""
    if os.getenv("FETCH_INSECURE") == "1":
        return ssl._create_unverified_context()
    cafile = os.getenv("SSL_CERT_FILE") or os.getenv("REQUESTS_CA_BUNDLE")
    if cafile:
        return ssl.create_default_context(cafile=cafile)
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return None


def validate_url(url: str) -> URLResult:
    """Validate a single URL and return the result."""
    # Wait for rate limit before making request
    _rate_limiter.wait_for_domain(url)

    context = build_ssl_context()
    request = Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    start = time.monotonic()

    try:
        # Don't follow redirects automatically - we want to detect them
        with urlopen(request, timeout=TIMEOUT, context=context) as response:
            elapsed_ms = int((time.monotonic() - start) * 1000)
            status_code = getattr(response, "status", 200)

            # Check for redirect (urllib follows them, so we need to compare URLs)
            final_url = response.geturl()
            if final_url != url:
                return URLResult(
                    url=url,
                    status="redirect",
                    http_code=status_code,
                    redirect_url=final_url,
                    response_time_ms=elapsed_ms,
                )

            return URLResult(
                url=url,
                status="ok",
                http_code=status_code,
                response_time_ms=elapsed_ms,
            )

    except HTTPError as exc:
        elapsed_ms = int((time.monotonic() - start) * 1000)

        # 301/302/307/308 redirects
        if exc.code in (301, 302, 307, 308):
            redirect_url = exc.headers.get("Location")
            return URLResult(
                url=url,
                status="redirect",
                http_code=exc.code,
                redirect_url=redirect_url,
                response_time_ms=elapsed_ms,
            )

        # Client/server errors
        return URLResult(
            url=url,
            status="error",
            http_code=exc.code,
            error_message=f"HTTP {exc.code}: {exc.reason}",
            response_time_ms=elapsed_ms,
        )

    except (URLError, ssl.SSLError) as exc:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        message = str(exc)
        if hasattr(exc, "reason"):
            message = str(exc.reason)
        return URLResult(
            url=url,
            status="error",
            error_message=message,
            response_time_ms=elapsed_ms,
        )

    except TimeoutError:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return URLResult(
            url=url,
            status="timeout",
            error_message=f"Timeout after {TIMEOUT}s",
            response_time_ms=elapsed_ms,
        )

    except Exception as exc:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return URLResult(
            url=url,
            status="error",
            error_message=str(exc),
            response_time_ms=elapsed_ms,
        )


def collect_urls_from_sources() -> dict[str, set[str]]:
    """Collect all URLs from sources.json files, grouped by language."""
    urls_by_language: dict[str, set[str]] = {}

    for lang_dir in SPECS_DIR.iterdir():
        if not lang_dir.is_dir() or lang_dir.name.startswith("."):
            continue

        sources_file = lang_dir / "sources.json"
        if not sources_file.exists():
            continue

        try:
            data = json.loads(sources_file.read_text(encoding="utf-8"))
            urls = set()
            for file_entry in data.get("files", []):
                urls.update(file_entry.get("urls", []))
            if urls:
                urls_by_language[lang_dir.name] = urls
        except (json.JSONDecodeError, OSError) as exc:
            log(f"Warning: Could not read {sources_file}: {exc}", level="warning")

    return urls_by_language


def validate_all_urls(urls_by_language: dict[str, set[str]]) -> dict:
    """Validate all URLs in parallel and return results."""
    # Flatten to unique URLs while tracking which languages use them
    all_urls: dict[str, list[str]] = {}  # url -> list of languages
    for language, urls in urls_by_language.items():
        for url in urls:
            if url not in all_urls:
                all_urls[url] = []
            all_urls[url].append(language)

    log(f"Validating {len(all_urls)} unique URLs across {len(urls_by_language)} languages...")

    results: dict[str, URLResult] = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(validate_url, url): url for url in all_urls}

        completed = 0
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            completed += 1
            try:
                result = future.result()
                results[url] = result

                # Log issues
                if result.status == "error":
                    log(
                        f"[{completed}/{len(all_urls)}] ERROR: {url} - {result.error_message}",
                        level="error",
                    )
                elif result.status == "redirect":
                    log(
                        f"[{completed}/{len(all_urls)}] REDIRECT: {url} -> {result.redirect_url}",
                        level="warning",
                    )
                elif result.status == "timeout":
                    log(f"[{completed}/{len(all_urls)}] TIMEOUT: {url}", level="warning")
                # Only log every 10th success to reduce noise
                elif completed % 10 == 0:
                    log(f"[{completed}/{len(all_urls)}] Validated {completed} URLs...")

            except Exception as exc:
                results[url] = URLResult(
                    url=url,
                    status="error",
                    error_message=f"Validation failed: {exc}",
                )

    return {
        "results": results,
        "url_to_languages": all_urls,
    }


def build_summary(results: dict[str, URLResult], url_to_languages: dict[str, list[str]]) -> dict:
    """Build summary statistics and language-specific breakdowns."""
    summary = {
        "total": len(results),
        "ok": 0,
        "redirect": 0,
        "error": 0,
        "timeout": 0,
    }

    errors_by_language: dict[str, list[dict]] = {}
    redirects_by_language: dict[str, list[dict]] = {}

    for url, result in results.items():
        summary[result.status] += 1
        languages = url_to_languages.get(url, [])

        if result.status in {"error", "timeout"}:
            for lang in languages:
                if lang not in errors_by_language:
                    errors_by_language[lang] = []
                errors_by_language[lang].append(result.to_dict())

        elif result.status == "redirect":
            for lang in languages:
                if lang not in redirects_by_language:
                    redirects_by_language[lang] = []
                redirects_by_language[lang].append(result.to_dict())

    return {
        "summary": summary,
        "errorsByLanguage": errors_by_language,
        "redirectsByLanguage": redirects_by_language,
    }


def suggest_fixes(results: dict[str, URLResult]) -> list[dict[str, Any]]:
    """Generate suggested URL fixes for redirects and common issues."""
    suggestions: list[dict[str, Any]] = []

    for url, result in results.items():
        if result.status == "redirect" and result.redirect_url:
            # Permanent redirect - suggest update
            if result.http_code == 301:
                suggestions.append(
                    {
                        "type": "permanent_redirect",
                        "oldUrl": url,
                        "newUrl": result.redirect_url,
                        "action": "Update URL in sources",
                        "autoFixable": True,
                    }
                )
            else:
                suggestions.append(
                    {
                        "type": "temporary_redirect",
                        "oldUrl": url,
                        "newUrl": result.redirect_url,
                        "action": "Monitor - may be temporary",
                        "autoFixable": False,
                    }
                )

        elif result.status == "error":
            # Try to suggest alternatives
            suggestion = {
                "type": "broken_url",
                "url": url,
                "error": result.error_message,
                "action": "Manual review required",
                "autoFixable": False,
            }

            # Add search suggestions for common documentation sites
            if "docs.python.org" in url:
                suggestion["searchHint"] = "Try searching: site:docs.python.org <topic>"
            elif "developer.mozilla.org" in url:
                suggestion["searchHint"] = "Try searching: site:developer.mozilla.org <topic>"
            elif "github.com" in url:
                suggestion["searchHint"] = "Check if repository was renamed or moved"

            suggestions.append(suggestion)

    return suggestions


def main() -> int:
    """Main entry point."""
    log("=== URL Validation Started ===")

    # Collect URLs
    urls_by_language = collect_urls_from_sources()
    if not urls_by_language:
        log("No URLs found in sources.json files")
        return 0

    total_urls = sum(len(urls) for urls in urls_by_language.values())
    log(f"Found {total_urls} URLs across {len(urls_by_language)} languages")

    # Validate all URLs
    validation_data = validate_all_urls(urls_by_language)
    results = validation_data["results"]
    url_to_languages = validation_data["url_to_languages"]

    # Build summary and suggestions
    summary_data = build_summary(results, url_to_languages)
    suggestions = suggest_fixes(results)

    # Build output
    output = {
        "generatedAt": datetime.now(UTC).isoformat(),
        "summary": summary_data["summary"],
        "errorsByLanguage": summary_data["errorsByLanguage"],
        "redirectsByLanguage": summary_data["redirectsByLanguage"],
        "suggestions": suggestions,
        "allResults": [r.to_dict() for r in results.values()],
    }

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")

    # Log summary
    s = summary_data["summary"]
    log("=== URL Validation Complete ===")
    log(
        f"Total: {s['total']} | OK: {s['ok']} | Redirects: {s['redirect']} | Errors: {s['error']} | Timeouts: {s['timeout']}"
    )
    log(f"Results written to {OUTPUT_FILE}")

    if suggestions:
        log(f"Generated {len(suggestions)} fix suggestions")
        auto_fixable = sum(1 for s in suggestions if s.get("autoFixable"))
        if auto_fixable:
            log(f"  {auto_fixable} can be auto-fixed (permanent redirects)")

    # Return non-zero if there are errors
    return 1 if s["error"] > 0 or s["timeout"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
