#!/usr/bin/env python3
"""Clean up URLs in sources.json files based on validation results.

This script:
1. Removes placeholder URLs (example.com, example.org, etc.)
2. Fixes malformed URLs (backticks, markdown artifacts)
3. Updates redirected URLs to their final destinations
4. Removes broken URLs that can't be fixed
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
SPECS_DIR = ROOT_DIR / "specs"
URL_STATUS_FILE = ROOT_DIR / "docs" / "site" / "url-status.json"

# Placeholder domains to remove
PLACEHOLDER_DOMAINS = {
    "example.com",
    "example.org",
    "example.net",
    "example.edu",
    "cdn-example.com",
    "idp.example",
    "api.example.com",
    "www.example.com",
    "test.example.com",
}

# URL patterns that indicate malformed URLs
MALFORMED_PATTERNS = [
    r"`$",  # Trailing backtick
    r"`",  # Any backtick
    r"\]\(https?://",  # Markdown link artifact
    r"\)$",  # Trailing parenthesis from markdown
]


def is_placeholder_url(url: str) -> bool:
    """Check if URL is a placeholder/example domain."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        return domain in PLACEHOLDER_DOMAINS or domain.endswith(".example.com")
    except Exception:
        return False


def is_malformed_url(url: str) -> bool:
    """Check if URL has malformed characters."""
    return any(re.search(pattern, url) for pattern in MALFORMED_PATTERNS)


def fix_malformed_url(url: str) -> str | None:
    """Attempt to fix a malformed URL. Returns None if unfixable."""
    fixed = url

    # Remove trailing backticks
    fixed = fixed.rstrip("`")

    # Remove markdown link artifacts
    if "](http" in fixed:
        # Extract just the first URL
        match = re.match(r"(https?://[^\]]+)", fixed)
        if match:
            fixed = match.group(1)

    # Remove trailing parenthesis
    fixed = fixed.rstrip(")")

    # Validate the fixed URL
    try:
        parsed = urlparse(fixed)
        if parsed.scheme in ("http", "https") and parsed.netloc:
            return fixed
    except Exception:
        pass

    return None


def load_url_status() -> dict:
    """Load the URL validation results."""
    if not URL_STATUS_FILE.exists():
        print(f"Error: {URL_STATUS_FILE} not found. Run validate-urls.py first.")
        sys.exit(1)
    return json.loads(URL_STATUS_FILE.read_text(encoding="utf-8"))


def build_redirect_map(status_data: dict) -> dict[str, str]:
    """Build a map of original URLs to their redirect destinations."""
    redirect_map = {}
    for result in status_data.get("allResults", []):
        if result.get("status") == "redirect" and result.get("redirectUrl"):
            original = result["url"]
            destination = result["redirectUrl"]
            # Only map if destination is different and valid
            if original != destination:
                redirect_map[original] = destination
    return redirect_map


def build_error_set(status_data: dict) -> set[str]:
    """Build a set of URLs that returned errors."""
    errors = set()
    for result in status_data.get("allResults", []):
        if result.get("status") == "error":
            errors.add(result["url"])
    return errors


def process_sources_file(
    sources_path: Path, redirect_map: dict[str, str], error_urls: set[str], dry_run: bool = False
) -> dict:
    """Process a single sources.json file and clean up URLs."""
    stats = {
        "placeholders_removed": 0,
        "malformed_fixed": 0,
        "malformed_removed": 0,
        "redirects_updated": 0,
        "errors_removed": 0,
        "total_urls_before": 0,
        "total_urls_after": 0,
    }

    data = json.loads(sources_path.read_text(encoding="utf-8"))
    modified = False

    for file_entry in data.get("files", []):
        urls = file_entry.get("urls", [])
        if not urls:
            continue

        stats["total_urls_before"] += len(urls)
        new_urls = []

        for url in urls:
            # Check placeholder
            if is_placeholder_url(url):
                stats["placeholders_removed"] += 1
                modified = True
                continue

            # Check malformed
            if is_malformed_url(url):
                fixed = fix_malformed_url(url)
                if fixed:
                    stats["malformed_fixed"] += 1
                    url = fixed
                    modified = True
                else:
                    stats["malformed_removed"] += 1
                    modified = True
                    continue

            # Check redirect
            if url in redirect_map:
                url = redirect_map[url]
                stats["redirects_updated"] += 1
                modified = True

            # Check error (after potential fixes)
            if url in error_urls:
                stats["errors_removed"] += 1
                modified = True
                continue

            new_urls.append(url)

        # Remove duplicates while preserving order
        seen = set()
        deduped = []
        for u in new_urls:
            if u not in seen:
                seen.add(u)
                deduped.append(u)

        file_entry["urls"] = deduped
        stats["total_urls_after"] += len(deduped)

    if modified and not dry_run:
        sources_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    return stats


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    # Load validation results
    print("Loading URL validation results...")
    status_data = load_url_status()

    redirect_map = build_redirect_map(status_data)
    error_urls = build_error_set(status_data)

    print(f"  Redirect mappings: {len(redirect_map)}")
    print(f"  Error URLs: {len(error_urls)}")
    print()

    # Process all sources.json files
    sources_files = list(SPECS_DIR.rglob("sources.json"))
    print(f"Processing {len(sources_files)} sources.json files...\n")

    total_stats = {
        "placeholders_removed": 0,
        "malformed_fixed": 0,
        "malformed_removed": 0,
        "redirects_updated": 0,
        "errors_removed": 0,
        "total_urls_before": 0,
        "total_urls_after": 0,
        "files_modified": 0,
    }

    for sources_path in sorted(sources_files):
        rel_path = sources_path.relative_to(SPECS_DIR)
        stats = process_sources_file(sources_path, redirect_map, error_urls, dry_run)

        # Aggregate stats
        for key in stats:
            if key in total_stats:
                total_stats[key] += stats[key]

        changes = (
            stats["placeholders_removed"]
            + stats["malformed_fixed"]
            + stats["malformed_removed"]
            + stats["redirects_updated"]
            + stats["errors_removed"]
        )

        if changes > 0:
            total_stats["files_modified"] += 1
            if verbose:
                print(f"  {rel_path}: {changes} changes")

    # Print summary
    print("\n=== Summary ===")
    print(f"Files modified: {total_stats['files_modified']}")
    print(f"URLs before: {total_stats['total_urls_before']}")
    print(f"URLs after: {total_stats['total_urls_after']}")
    print()
    print("Changes:")
    print(f"  Placeholders removed: {total_stats['placeholders_removed']}")
    print(f"  Malformed fixed: {total_stats['malformed_fixed']}")
    print(f"  Malformed removed: {total_stats['malformed_removed']}")
    print(f"  Redirects updated: {total_stats['redirects_updated']}")
    print(f"  Errors removed: {total_stats['errors_removed']}")

    if dry_run:
        print("\n(Dry run - no changes written)")
    else:
        print("\nChanges applied successfully.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
