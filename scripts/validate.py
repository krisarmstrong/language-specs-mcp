#!/usr/bin/env python3
"""Validate specs freshness and stub files.

Consolidates validate-freshness and validate-stubs.
Note: validate-urls.py is kept separate (too complex).

Usage:
    python scripts/validate.py freshness   # Check spec freshness
    python scripts/validate.py stubs       # Check for stub files
    python scripts/validate.py all         # Run all validators

Environment:
    MAX_AGE_DAYS=90       Maximum age for freshness (default: 90)
    STUB_ALLOWLIST=path   Custom allowlist for stubs
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
SPECS_ROOT = ROOT_DIR / "specs"


# --- Freshness Command ---

def cmd_freshness() -> int:
    """Check spec freshness."""
    max_age_days = int(os.getenv("MAX_AGE_DAYS", "90"))
    max_age_seconds = max_age_days * 24 * 60 * 60
    now = datetime.now(timezone.utc)

    failures: list[str] = []
    languages = sorted([p for p in SPECS_ROOT.iterdir() if p.is_dir()])

    for lang_dir in languages:
        fetched_at_path = lang_dir / ".fetched-at"
        if not fetched_at_path.exists():
            failures.append(f"{lang_dir.name}: missing .fetched-at")
            continue

        trimmed = fetched_at_path.read_text(encoding="utf-8").strip()
        if not trimmed:
            failures.append(f"{lang_dir.name}: invalid .fetched-at (empty)")
            continue

        try:
            parsed = datetime.fromisoformat(trimmed.replace("Z", "+00:00"))
        except ValueError:
            failures.append(f"{lang_dir.name}: invalid .fetched-at ({trimmed})")
            continue

        age_seconds = (now - parsed).total_seconds()
        if age_seconds > max_age_seconds:
            failures.append(f"{lang_dir.name}: stale (.fetched-at {trimmed})")

    if failures:
        print(f"Freshness validation failed (>{max_age_days} days):")
        print("\n".join(f"  - {item}" for item in failures))
        return 1

    print(f"Freshness validation passed (<={max_age_days} days).")
    return 0


# --- Stubs Command ---

def is_stub_file(path: Path) -> bool:
    """Check if a file is a stub (1-2 lines starting with 'See:')."""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return False
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(lines) > 2:
        return False
    return any(line.startswith("See: ") for line in lines)


def load_allowlist() -> set[str]:
    """Load stub allowlist."""
    allowlist_path = Path(os.getenv("STUB_ALLOWLIST", ROOT_DIR / "tools" / "stubs-allowlist.txt"))
    if not allowlist_path.exists():
        return set()
    return {
        line.strip()
        for line in allowlist_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def cmd_stubs() -> int:
    """Check for stub files."""
    allowlist = load_allowlist()
    stubs: list[str] = []

    for file_path in SPECS_ROOT.rglob("*.md"):
        if is_stub_file(file_path):
            rel_path = file_path.relative_to(ROOT_DIR).as_posix()
            stubs.append(rel_path)

    unexpected = sorted([p for p in stubs if p not in allowlist])
    stale_allowlist = sorted([p for p in allowlist if p not in stubs])

    if unexpected:
        print("Stub validation failed (unexpected stub files detected):")
        for p in unexpected[:100]:
            print(f"  - {p}")
        if len(unexpected) > 100:
            print(f"  ... and {len(unexpected) - 100} more")
        return 1

    if stale_allowlist:
        print("Warning: allowlist entries no longer stubbed:")
        for p in stale_allowlist[:50]:
            print(f"  - {p}")
        if len(stale_allowlist) > 50:
            print(f"  ... and {len(stale_allowlist) - 50} more")

    print(f"Stub validation passed ({len(stubs)} stub files).")
    return 0


# --- All Command ---

def cmd_all() -> int:
    """Run all validators."""
    result = 0

    print("=== Freshness validation ===")
    result |= cmd_freshness()

    print("\n=== Stub validation ===")
    result |= cmd_stubs()

    return result


# --- Main ---

COMMANDS = {
    "freshness": cmd_freshness,
    "stubs": cmd_stubs,
    "all": cmd_all,
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Commands:")
        print("  freshness  Check spec freshness")
        print("  stubs      Check for stub files")
        print("  all        Run all validators")
        return 0

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(COMMANDS.keys())}")
        return 1

    return COMMANDS[cmd]()


if __name__ == "__main__":
    sys.exit(main())
