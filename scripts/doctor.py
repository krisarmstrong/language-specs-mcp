#!/usr/bin/env python3
"""Quick environment and data sanity checks."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
SPECS_DIR = ROOT_DIR / "specs"
TOOLS_JSON = ROOT_DIR / "tools" / "versions.json"
HEALTH_JSON = ROOT_DIR / "docs" / "site" / "health.json"
SEARCH_JSON = SPECS_DIR / "search.json"
ENV_FILE = ROOT_DIR / ".env"
CRON_MARKER = "# specforge-refresh"
LAUNCHD_LABEL = "com.specforge.refresh"


def parse_env_file() -> dict[str, str]:
    if not ENV_FILE.exists():
        return {}
    values: dict[str, str] = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def parse_iso(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def latest_fetched_at() -> datetime | None:
    latest = None
    for path in SPECS_DIR.rglob(".fetched-at"):
        parsed = parse_iso(path.read_text(encoding="utf-8").strip())
        if not parsed:
            continue
        if not latest or parsed > latest:
            latest = parsed
    return latest


def is_stub_file(path: Path) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return False
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(lines) > 2:
        return False
    return any(line.startswith("See: ") for line in lines)


def count_stubs() -> tuple[int, int]:
    total = 0
    important = 0
    for path in SPECS_DIR.rglob("*.md"):
        if not is_stub_file(path):
            continue
        total += 1
        if path.name in {"spec.md", "overview.md"}:
            important += 1
    return total, important


def check_launchd() -> tuple[bool, str]:
    plist = Path.home() / "Library" / "LaunchAgents" / f"{LAUNCHD_LABEL}.plist"
    if not plist.exists():
        return False, "Launchd plist not installed"
    try:
        result = subprocess.run(
            ["launchctl", "list", LAUNCHD_LABEL],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            return True, "Launchd agent loaded"
        return False, "Launchd plist installed but not loaded"
    except OSError:
        return False, "launchctl not available"


def check_cron() -> tuple[bool, str]:
    if not shutil.which("crontab"):
        return False, "crontab not available"
    result = subprocess.run(
        ["crontab", "-l"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if result.returncode != 0:
        return False, "crontab is empty"
    if CRON_MARKER in result.stdout:
        return True, "Cron entry installed"
    return False, "Cron entry not found"


def load_versions() -> tuple[str | None, list[str]]:
    if not TOOLS_JSON.exists():
        return None, ["tools/versions.json missing"]
    payload = json.loads(TOOLS_JSON.read_text(encoding="utf-8"))
    updated_at = payload.get("updatedAt")
    missing_checked = [
        entry["name"]
        for entry in payload.get("tools", [])
        if entry.get("latest") and not entry.get("checkedAt")
    ]
    return updated_at, missing_checked


def load_search_generated() -> str | None:
    if not SEARCH_JSON.exists():
        return None
    payload = json.loads(SEARCH_JSON.read_text(encoding="utf-8"))
    return payload.get("generatedAt")


def status_line(label: str, ok: bool, detail: str) -> str:
    return f"[{'OK' if ok else 'WARN'}] {label}: {detail}"


def main() -> int:
    env_values = parse_env_file()
    token_present = bool(os.getenv("GITHUB_TOKEN") or env_values.get("GITHUB_TOKEN"))
    print(status_line("GITHUB_TOKEN", token_present, "set" if token_present else "missing"))

    if sys.platform == "darwin":
        ok, detail = check_launchd()
        print(status_line("Scheduler", ok, detail))
    else:
        ok, detail = check_cron()
        print(status_line("Scheduler", ok, detail))

    latest = latest_fetched_at()
    if latest:
        age_days = (datetime.now(timezone.utc) - latest).days
        print(status_line("Last refresh", True, f"{latest.isoformat()} ({age_days} days ago)"))
    else:
        print(status_line("Last refresh", False, "no .fetched-at files"))

    updated_at, missing_checked = load_versions()
    if updated_at:
        detail = f"updatedAt {updated_at}"
        if missing_checked:
            detail += f" (missing checkedAt for {len(missing_checked)} tools)"
        print(status_line("Version registry", True, detail))
    else:
        print(status_line("Version registry", False, "tools/versions.json missing"))

    search_generated = load_search_generated()
    if search_generated:
        print(status_line("Search index", True, f"generatedAt {search_generated}"))
    else:
        print(status_line("Search index", False, "specs/search.json missing"))

    total_stubs, important_stubs = count_stubs()
    stub_detail = f"{total_stubs} stubs ({important_stubs} spec/overview)"
    print(status_line("Stub docs", total_stubs == 0, stub_detail))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
