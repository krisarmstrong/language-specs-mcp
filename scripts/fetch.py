#!/usr/bin/env python3
"""Data-driven spec fetcher.

Reads URLs from sources.json files and fetches content.
This replaces the monolithic fetch.py with a simple, maintainable approach.

Usage:
    python scripts/fetch-v2.py                    # Fetch all languages
    python scripts/fetch-v2.py python typescript  # Fetch specific languages
    python scripts/fetch-v2.py --delta            # Only fetch stale specs
    python scripts/fetch-v2.py --dry-run          # Show what would be fetched
"""

from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from threading import Lock
from typing import Any

from _common import (
    SPECS_DIR,
    FetchError,
    fetch_url,
    html_to_markdown,
    log,
    write_fetched_at,
    write_text,
)

# Configuration
MAX_WORKERS = int(os.getenv("FETCH_WORKERS", "4"))
STALE_DAYS = int(os.getenv("FETCH_STALE_DAYS", "30"))
TIMEOUT_SECONDS = float(os.getenv("FETCH_TIMEOUT", "30"))

# Rate limiting
RATE_LIMIT_SECONDS = float(os.getenv("FETCH_RATE_LIMIT", "0.5"))
_rate_lock = Lock()
_last_request: dict[str, float] = {}


def rate_limit(domain: str) -> None:
    """Simple per-domain rate limiting."""
    with _rate_lock:
        now = time.monotonic()
        last = _last_request.get(domain, 0)
        wait = RATE_LIMIT_SECONDS - (now - last)
        if wait > 0:
            time.sleep(wait)
        _last_request[domain] = time.monotonic()


@dataclass
class FetchResult:
    """Result of fetching a single file."""

    path: str
    success: bool
    url: str | None = None
    error: str | None = None


@dataclass
class LanguageResult:
    """Result of fetching all files for a language."""

    language: str
    success: int = 0
    failed: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


def load_sources(language: str) -> dict[str, Any]:
    """Load sources.json for a language."""
    path = SPECS_DIR / language / "sources.json"
    if not path.exists():
        return {"language": language, "files": []}
    result: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return result


def is_stale(language: str) -> bool:
    """Check if a language's specs are stale."""
    fetched_at_path = SPECS_DIR / language / ".fetched-at"
    if not fetched_at_path.exists():
        return True

    try:
        content = fetched_at_path.read_text(encoding="utf-8").strip()
        fetched_time = datetime.fromisoformat(content)
        cutoff = datetime.now(UTC) - timedelta(days=STALE_DAYS)
        return fetched_time < cutoff
    except (ValueError, OSError):
        return True


def fetch_file(language: str, file_spec: dict[str, Any]) -> FetchResult:
    """Fetch a single file based on its sources.json entry."""
    path = file_spec.get("path", "")
    urls = file_spec.get("urls", [])

    if not path:
        return FetchResult(path="unknown", success=False, error="No path specified")

    if not urls:
        return FetchResult(path=path, success=True)  # No URLs = skip silently

    output_path = SPECS_DIR / language / path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Try each URL until one succeeds
    last_error = None
    for url in urls:
        try:
            # Rate limit by domain
            from urllib.parse import urlparse

            domain = urlparse(url).netloc
            rate_limit(domain)

            # Fetch content
            content = fetch_url(url)

            # Convert HTML to markdown if needed
            if url.endswith(".html") or "<html" in content.lower()[:500]:
                # Save as temp HTML, convert
                temp_html = output_path.with_suffix(".tmp.html")
                write_text(temp_html, content)
                success = html_to_markdown(content, output_path)
                temp_html.unlink(missing_ok=True)
                if not success:
                    # Fallback: save raw content
                    write_text(output_path, content)
            else:
                write_text(output_path, content)

            return FetchResult(path=path, success=True, url=url)

        except FetchError as e:
            last_error = str(e)
            continue
        except Exception as e:
            last_error = str(e)
            continue

    return FetchResult(path=path, success=False, url=urls[0] if urls else None, error=last_error)


def fetch_language(language: str, dry_run: bool = False) -> LanguageResult:
    """Fetch all files for a language."""
    result = LanguageResult(language=language)
    sources = load_sources(language)
    files = sources.get("files", [])

    if not files:
        log(f"{language}: No sources.json or empty", level="warning")
        return result

    log(f"{language}: Processing {len(files)} files...")

    for file_spec in files:
        urls = file_spec.get("urls", [])
        path = file_spec.get("path", "unknown")

        if not urls:
            result.skipped += 1
            continue

        if dry_run:
            log(f"  [dry-run] Would fetch: {path} from {urls[0]}")
            result.success += 1
            continue

        fetch_result = fetch_file(language, file_spec)

        if fetch_result.success:
            result.success += 1
        else:
            result.failed += 1
            result.errors.append(f"{path}: {fetch_result.error}")

    # Write .fetched-at timestamp
    if not dry_run and result.success > 0:
        write_fetched_at(SPECS_DIR / language)

    status = "OK" if result.failed == 0 else f"{result.failed} failed"
    log(f"{language}: Done - {result.success} fetched, {result.skipped} skipped, {status}")

    return result


def get_languages() -> list[str]:
    """Get list of language directories."""
    return sorted(
        [
            d.name
            for d in SPECS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith("_") and (d / "sources.json").exists()
        ]
    )


def main() -> int:
    args = sys.argv[1:]

    # Show help
    if "-h" in args or "--help" in args:
        print(__doc__)
        print("Options:")
        print("  --dry-run    Show what would be fetched without fetching")
        print("  --delta      Only fetch stale specs (older than FETCH_STALE_DAYS)")
        print("  -h, --help   Show this help message")
        print()
        print("Environment:")
        print(f"  FETCH_WORKERS={MAX_WORKERS}     Number of parallel workers")
        print(f"  FETCH_STALE_DAYS={STALE_DAYS}   Days before spec is considered stale")
        print(f"  FETCH_TIMEOUT={TIMEOUT_SECONDS}      Request timeout in seconds")
        print(f"  FETCH_RATE_LIMIT={RATE_LIMIT_SECONDS}   Seconds between requests to same domain")
        return 0

    # Parse flags
    dry_run = "--dry-run" in args
    delta_mode = "--delta" in args
    args = [a for a in args if not a.startswith("-")]

    # Determine which languages to fetch
    languages = args or get_languages()

    # Filter to stale only in delta mode
    if delta_mode:
        stale = [lang for lang in languages if is_stale(lang)]
        if not stale:
            log("All specs are fresh. Nothing to fetch.")
            return 0
        log(f"Delta mode: {len(stale)}/{len(languages)} languages are stale")
        languages = stale

    if dry_run:
        log("=== DRY RUN MODE ===")

    log(f"Fetching {len(languages)} languages with {MAX_WORKERS} workers...")

    # Fetch languages in parallel
    all_results: list[LanguageResult] = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_language, lang, dry_run): lang for lang in languages}

        for future in as_completed(futures):
            lang = futures[future]
            try:
                result = future.result()
                all_results.append(result)
            except Exception as e:
                log(f"{lang}: Fatal error - {e}", level="error")
                all_results.append(LanguageResult(language=lang, errors=[str(e)]))

    # Summary
    total_success = sum(r.success for r in all_results)
    total_failed = sum(r.failed for r in all_results)
    total_skipped = sum(r.skipped for r in all_results)

    log("")
    log("=== Summary ===")
    log(f"Languages: {len(all_results)}")
    log(f"Files fetched: {total_success}")
    log(f"Files skipped: {total_skipped}")
    log(f"Files failed: {total_failed}")

    if total_failed > 0:
        log("")
        log("Errors:")
        for r in all_results:
            for err in r.errors[:3]:  # Limit errors shown
                log(f"  [{r.language}] {err}")

    return 1 if total_failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
