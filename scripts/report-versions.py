#!/usr/bin/env python3
"""Report tool versions and optionally latest upstream."""

from __future__ import annotations

import json
import os
from pathlib import Path

from _common import FetchError, get_latest_version, log

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"

CHECK_LATEST = os.getenv("CHECK_LATEST") == "1"


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    rows = []

    for tool in registry.get("tools", []):
        try:
            latest = get_latest_version(tool, check_enabled=CHECK_LATEST)
        except FetchError as exc:
            log(f"Latest version check failed for {tool.get('name')}: {exc}", level="warning")
            latest = None
        except OSError as exc:
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
            f"| {row['name']} | {row['version']} | {row['latest']} | {row.get('checkedAt', '-') or '-'} | {row['files']} | {row['sources']} |"
        )

    print("\n".join(lines))


if __name__ == "__main__":
    main()
