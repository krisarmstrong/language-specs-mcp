#!/usr/bin/env python3
"""Update tool versions registry from upstream sources."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from _common import FetchError, get_latest_version, log

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    checked_at = datetime.now(timezone.utc).isoformat()
    for tool in registry.get("tools", []):
        try:
            latest = get_latest_version(tool, check_enabled=True)
            if tool.get("latest"):
                tool["checkedAt"] = checked_at
            if latest:
                tool["version"] = latest
        except FetchError as exc:
            log(f"Version check failed for {tool.get('name')}: {exc}", level="warning")
        except OSError as exc:
            log(f"Version check failed for {tool.get('name')}: {exc}", level="warning")

    registry["updatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
