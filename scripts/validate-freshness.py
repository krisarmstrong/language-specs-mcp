#!/usr/bin/env python3
"""Validate freshness of fetched specs."""

from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SPECS_ROOT = SCRIPT_DIR.parent / "specs"

MAX_AGE_DAYS = int(os.getenv("MAX_AGE_DAYS", "90"))
MAX_AGE_SECONDS = MAX_AGE_DAYS * 24 * 60 * 60
NOW = datetime.now(timezone.utc)


def main() -> None:
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
        age_seconds = (NOW - parsed).total_seconds()
        if age_seconds > MAX_AGE_SECONDS:
            failures.append(f"{lang_dir.name}: stale (.fetched-at {trimmed})")

    if failures:
        failures_text = "\n".join(f"- {item}" for item in failures)
        raise SystemExit(
            f"Freshness validation failed (>{MAX_AGE_DAYS} days):\n{failures_text}"
        )

    print(f"Freshness validation passed (<={MAX_AGE_DAYS} days).")


if __name__ == "__main__":
    main()
