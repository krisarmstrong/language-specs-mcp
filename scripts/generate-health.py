#!/usr/bin/env python3
"""Generate health metadata used by the MCP dashboard."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from _common import SPECS_DIR, log


ROOT_DIR = SPECS_DIR.parent
TOOLS_JSON = ROOT_DIR / "tools" / "versions.json"
OUTPUT_FILE = ROOT_DIR / "docs" / "site" / "health.json"


def load_tools() -> dict[str, dict]:
    if not TOOLS_JSON.exists():
        return {}
    payload = json.loads(TOOLS_JSON.read_text(encoding="utf-8"))
    return {entry["name"]: entry for entry in payload.get("tools", [])}


def read_fetched_at(lang_dir: Path) -> datetime | None:
    path = lang_dir / ".fetched-at"
    if not path.exists():
        return None
    value = path.read_text(encoding="utf-8").strip()
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def count_markdown_files(directory: Path) -> int:
    if not directory.exists():
        return 0
    return sum(1 for entry in directory.rglob("*.md") if entry.is_file())


def list_subdirs(directory: Path) -> Iterable[Path]:
    if not directory.exists():
        return ()
    return sorted(entry for entry in directory.iterdir() if entry.is_dir())


def gather_category_data(lang_dir: Path, category: str) -> dict:
    if category == "spec":
        spec_path = lang_dir / "spec.md"
        return {
            "count": 1 if spec_path.exists() else 0,
            "missing": not spec_path.exists(),
            "path": str(spec_path.relative_to(ROOT_DIR)) if spec_path.exists() else "",
        }
    path = lang_dir / category
    return {
        "count": count_markdown_files(path),
        "missing": not path.exists(),
    }


def gather_linters(lang_dir: Path) -> list[dict]:
    linter_root = lang_dir / "linters"
    linters = []
    for linter_dir in list_subdirs(linter_root):
        linters.append(
            {
                "name": linter_dir.name,
                "count": count_markdown_files(linter_dir),
            }
        )
    return linters


def gather_formatters(lang_dir: Path) -> list[dict]:
    formatter_root = lang_dir / "formatters"
    formatters = []
    for entry in list_subdirs(formatter_root):
        formatters.append(
            {
                "name": entry.name,
                "count": count_markdown_files(entry),
            }
        )
    return formatters


def build_language_record(language: str, tools: dict[str, dict]) -> dict:
    lang_dir = SPECS_DIR / language
    fetched_at = read_fetched_at(lang_dir)
    now = datetime.now(timezone.utc)
    freshness_days = None
    if fetched_at:
        freshness_days = (now - fetched_at).days
    tool_entry = tools.get(language)
    notes = []
    if not fetched_at:
        notes.append("No fetched-at timestamp (run fetch:all or fetch:delta)")
    elif freshness_days is not None and freshness_days > 30:
        notes.append("Data older than 30 days; consider refresh")

    spec_data = gather_category_data(lang_dir, "spec")
    if spec_data["missing"]:
        notes.append("Spec document missing")

    return {
        "language": language,
        "fetchedAt": fetched_at.isoformat() if fetched_at else None,
        "freshnessDays": freshness_days,
        "spec": spec_data,
        "stdlib": gather_category_data(lang_dir, "stdlib"),
        "linters": gather_linters(lang_dir),
        "formatters": gather_formatters(lang_dir),
        "patterns": gather_category_data(lang_dir, "patterns"),
        "toolsVersion": tool_entry.get("version") if tool_entry else None,
        "toolSources": tool_entry.get("sources", []) if tool_entry else [],
        "notes": notes,
    }


def main() -> None:
    tools = load_tools()
    languages = sorted([entry.name for entry in SPECS_DIR.iterdir() if entry.is_dir()])
    now = datetime.now(timezone.utc)
    records = []
    for language in languages:
        if language.startswith("."):
            continue
        record = build_language_record(language, tools)
        records.append(record)

    payload = {
        "generatedAt": now.isoformat(),
        "languages": records,
        "totalLanguages": len(records),
    }
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    log(f"Wrote {len(records)} language health records to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
