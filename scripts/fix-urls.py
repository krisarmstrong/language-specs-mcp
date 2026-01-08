#!/usr/bin/env python3
"""Automatically fix URLs based on validation results.

This script:
1. Reads url-status.json for suggested fixes
2. Applies permanent redirect fixes to sources.json files
3. Logs changes and creates a summary report
"""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime

from _common import SPECS_DIR, log

ROOT_DIR = SPECS_DIR.parent
URL_STATUS_FILE = ROOT_DIR / "docs" / "site" / "url-status.json"
FIX_LOG_FILE = ROOT_DIR / "docs" / "site" / "url-fix-log.json"


def load_url_status() -> dict:
    """Load URL validation status."""
    if not URL_STATUS_FILE.exists():
        return {}
    try:
        return json.loads(URL_STATUS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def find_and_replace_url_in_sources(old_url: str, new_url: str) -> list[dict]:
    """Find all sources.json files containing old_url and replace with new_url."""
    changes = []

    for lang_dir in SPECS_DIR.iterdir():
        if not lang_dir.is_dir() or lang_dir.name.startswith("."):
            continue

        sources_file = lang_dir / "sources.json"
        if not sources_file.exists():
            continue

        try:
            content = sources_file.read_text(encoding="utf-8")
            if old_url not in content:
                continue

            # Parse and update
            data = json.loads(content)
            modified = False

            for file_entry in data.get("files", []):
                urls = file_entry.get("urls", [])
                if old_url in urls:
                    # Replace the URL
                    new_urls = [new_url if u == old_url else u for u in urls]
                    file_entry["urls"] = new_urls
                    modified = True
                    changes.append(
                        {
                            "language": lang_dir.name,
                            "file": file_entry.get("path", ""),
                            "oldUrl": old_url,
                            "newUrl": new_url,
                        }
                    )

            if modified:
                # Update timestamp
                data["generatedAt"] = datetime.now(UTC).isoformat()
                # Write back
                sources_file.write_text(
                    json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
                )
                log(f"Updated {sources_file}")

        except (json.JSONDecodeError, OSError) as exc:
            log(f"Warning: Could not process {sources_file}: {exc}", level="warning")

    return changes


def apply_auto_fixes(dry_run: bool = False) -> dict:
    """Apply all auto-fixable URL changes."""
    url_status = load_url_status()
    suggestions = url_status.get("suggestions", [])

    # Filter to auto-fixable suggestions
    auto_fixable = [
        s for s in suggestions if s.get("autoFixable") and s.get("type") == "permanent_redirect"
    ]

    if not auto_fixable:
        log("No auto-fixable URL changes found")
        return {"applied": 0, "changes": []}

    log(f"Found {len(auto_fixable)} auto-fixable URL changes")

    all_changes = []
    for fix in auto_fixable:
        old_url = fix.get("oldUrl")
        new_url = fix.get("newUrl")

        if not old_url or not new_url:
            continue

        if dry_run:
            log(f"[DRY RUN] Would replace: {old_url} -> {new_url}")
            all_changes.append(
                {
                    "oldUrl": old_url,
                    "newUrl": new_url,
                    "dryRun": True,
                }
            )
        else:
            log(f"Applying fix: {old_url} -> {new_url}")
            changes = find_and_replace_url_in_sources(old_url, new_url)
            all_changes.extend(changes)

    return {
        "applied": len(all_changes),
        "changes": all_changes,
        "dryRun": dry_run,
    }


def generate_manual_fix_report() -> list[dict]:
    """Generate a report of URLs that need manual fixing."""
    url_status = load_url_status()
    suggestions = url_status.get("suggestions", [])

    manual_fixes = [s for s in suggestions if not s.get("autoFixable")]

    if not manual_fixes:
        return []

    report = []
    for fix in manual_fixes:
        entry = {
            "type": fix.get("type"),
            "url": fix.get("url") or fix.get("oldUrl"),
            "error": fix.get("error"),
            "action": fix.get("action"),
        }
        if fix.get("searchHint"):
            entry["searchHint"] = fix.get("searchHint")
        if fix.get("newUrl"):
            entry["suggestedUrl"] = fix.get("newUrl")
        report.append(entry)

    return report


def main() -> int:
    """Main entry point."""
    dry_run = "--dry-run" in sys.argv
    report_only = "--report" in sys.argv

    if report_only:
        # Just generate report of manual fixes needed
        manual_fixes = generate_manual_fix_report()
        if manual_fixes:
            log(f"=== Manual Fixes Required ({len(manual_fixes)}) ===")
            for fix in manual_fixes:
                log(f"  [{fix['type']}] {fix['url']}")
                if fix.get("error"):
                    log(f"    Error: {fix['error']}")
                if fix.get("searchHint"):
                    log(f"    Hint: {fix['searchHint']}")
        else:
            log("No manual fixes required")
        return 0

    log("=== URL Fix Started ===")

    # Apply auto fixes
    result = apply_auto_fixes(dry_run=dry_run)

    if result["applied"] > 0:
        log(f"Applied {result['applied']} URL fixes")

        # Save fix log
        fix_log = {
            "generatedAt": datetime.now(UTC).isoformat(),
            "dryRun": dry_run,
            "totalChanges": result["applied"],
            "changes": result["changes"],
        }
        FIX_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        FIX_LOG_FILE.write_text(json.dumps(fix_log, indent=2), encoding="utf-8")
        log(f"Fix log written to {FIX_LOG_FILE}")
    else:
        log("No fixes applied")

    # Report manual fixes
    manual_fixes = generate_manual_fix_report()
    if manual_fixes:
        log(f"\n=== Manual Fixes Required ({len(manual_fixes)}) ===")
        for fix in manual_fixes[:10]:  # Show first 10
            log(f"  [{fix['type']}] {fix['url']}")

    log("=== URL Fix Complete ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
