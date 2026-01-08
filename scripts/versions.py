#!/usr/bin/env python3
"""Version management for tool registry.

Consolidates report-versions, update-versions, and validate-versions.

Usage:
    python scripts/versions.py report      # Show versions table
    python scripts/versions.py update      # Update from upstream
    python scripts/versions.py validate    # Validate against specs

Environment:
    CHECK_LATEST=1  Include upstream version checks (slower)
"""

from __future__ import annotations

import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from _common import FetchError, get_latest_version, log, normalize_version

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"

CHECK_LATEST = os.getenv("CHECK_LATEST") == "1"


def load_registry() -> dict:
    """Load the tool versions registry."""
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def save_registry(registry: dict) -> None:
    """Save the tool versions registry."""
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")


# --- Report Command ---


def cmd_report() -> int:
    """Show versions table."""
    registry = load_registry()
    rows = []

    for tool in registry.get("tools", []):
        try:
            latest = get_latest_version(tool, check_enabled=CHECK_LATEST)
        except (FetchError, OSError) as exc:
            log(f"Latest version check failed for {tool.get('name')}: {exc}", level="warning")
            latest = None
        rows.append(
            {
                "name": tool.get("name"),
                "version": tool.get("version"),
                "latest": latest or "-",
                "checkedAt": tool.get("checkedAt"),
                "files": len(tool.get("files", []) or []),
                "sources": len(tool.get("sources", []) or []),
            }
        )

    header = ["Tool", "Version", "Latest", "Checked", "Files", "Sources"]
    lines = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join('---' for _ in header)} |",
    ]
    for row in rows:
        lines.append(
            f"| {row['name']} | {row['version']} | {row['latest']} | "
            f"{row.get('checkedAt', '-') or '-'} | {row['files']} | {row['sources']} |"
        )

    print("\n".join(lines))
    return 0


# --- Update Command ---


def cmd_update() -> int:
    """Update tool versions from upstream."""
    registry = load_registry()
    updated = 0

    checked_at = datetime.now(UTC).isoformat()
    for tool in registry.get("tools", []):
        try:
            latest = get_latest_version(tool, check_enabled=True)
            if tool.get("latest"):
                tool["checkedAt"] = checked_at
            if latest:
                old_version = tool.get("version")
                tool["version"] = latest
                if old_version != latest:
                    log(f"{tool.get('name')}: {old_version} → {latest}")
                    updated += 1
        except (FetchError, OSError) as exc:
            log(f"Version check failed for {tool.get('name')}: {exc}", level="warning")

    registry["updatedAt"] = datetime.now(UTC).strftime("%Y-%m-%d")
    save_registry(registry)

    log(f"Updated {updated} tool versions")
    return 0


# --- Validate Command ---


def file_has_version_line(file_path: str, label: str, version: str) -> bool:
    """Check if file contains the expected version line."""
    full_path = ROOT_DIR / file_path
    content = full_path.read_text(encoding="utf-8")
    formatted_label = label[:1].upper() + label[1:]
    target = f"{formatted_label}: {version}"
    return target in content


def file_has_sources(file_path: str, sources: list[str]) -> bool:
    """Check if file contains expected source URLs."""
    if not sources:
        return True
    full_path = ROOT_DIR / file_path
    content = full_path.read_text(encoding="utf-8")
    return all(source in content for source in sources)


def cmd_validate() -> int:
    """Validate tool versions against spec files."""
    registry = load_registry()
    failures: list[str] = []
    warnings: list[str] = []

    for tool in registry.get("tools", []):
        if tool.get("latest") and tool.get("version") == "unknown":
            failures.append(f"{tool.get('name')}: version is unknown but has a latest source")

        files = tool.get("files", []) or []
        if not files:
            warnings.append(f"{tool.get('name')}: no file references to validate")
        else:
            label = tool.get("label") or "Version"
            for file in files:
                try:
                    if not file_has_version_line(file, label, tool.get("version", "")):
                        failures.append(
                            f"{tool.get('name')}: missing {label}: {tool.get('version')} in {file}"
                        )
                    if not file_has_sources(file, tool.get("sources", []) or []):
                        failures.append(f"{tool.get('name')}: missing source URL in {file}")
                except OSError:
                    failures.append(f"{tool.get('name')}: unable to read {file}")

        if CHECK_LATEST:
            try:
                latest = get_latest_version(tool, check_enabled=True)
                if latest and normalize_version(tool.get("version", "")) != latest:
                    failures.append(
                        f"{tool.get('name')}: registry {tool.get('version')} != latest {latest}"
                    )
            except (FetchError, OSError) as exc:
                log(f"Latest version check failed for {tool.get('name')}: {exc}", level="warning")
                failures.append(f"{tool.get('name')}: failed to check latest version")

    if warnings:
        print("Warnings:")
        print("\n".join(f"  - {item}" for item in warnings))
        print()

    if failures:
        print("Validation failed:")
        print("\n".join(f"  - {item}" for item in failures))
        return 1

    print("Version validation passed.")
    return 0


# --- Main ---

COMMANDS = {
    "report": cmd_report,
    "update": cmd_update,
    "validate": cmd_validate,
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Commands:")
        print("  report    Show versions table")
        print("  update    Update versions from upstream")
        print("  validate  Validate versions against specs")
        return 0

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(COMMANDS.keys())}")
        return 1

    return COMMANDS[cmd]()


if __name__ == "__main__":
    sys.exit(main())
