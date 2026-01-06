#!/usr/bin/env python3
"""Detect stub markdown files and fail on new occurrences."""

from __future__ import annotations

import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SPECS_ROOT = ROOT_DIR / "specs"
ALLOWLIST_PATH = Path(
    os.getenv("STUB_ALLOWLIST", ROOT_DIR / "tools" / "stubs-allowlist.txt")
)


def is_stub_file(path: Path) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return False
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(lines) > 2:
        return False
    return any(line.startswith("See: ") for line in lines)


def load_allowlist() -> set[str]:
    if not ALLOWLIST_PATH.exists():
        return set()
    return {
        line.strip()
        for line in ALLOWLIST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def main() -> None:
    allowlist = load_allowlist()
    stubs = []
    for path in SPECS_ROOT.rglob("*.md"):
        if is_stub_file(path):
            rel_path = path.relative_to(ROOT_DIR).as_posix()
            stubs.append(rel_path)

    unexpected = sorted([path for path in stubs if path not in allowlist])
    stale_allowlist = sorted([path for path in allowlist if path not in stubs])

    if unexpected:
        details = "\n".join(f"- {path}" for path in unexpected[:100])
        raise SystemExit(
            "Stub validation failed (unexpected stub files detected):\n"
            f"{details}\n"
            f"(showing {min(len(unexpected), 100)} of {len(unexpected)})"
        )

    if stale_allowlist:
        print("Warning: allowlist entries no longer stubbed:")
        print("\n".join(f"- {path}" for path in stale_allowlist[:50]))
        print(f"(showing {min(len(stale_allowlist), 50)} of {len(stale_allowlist)})")

    print(f"Stub validation passed ({len(stubs)} stub files).")


if __name__ == "__main__":
    main()
