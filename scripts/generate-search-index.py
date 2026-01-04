#!/usr/bin/env python3
"""Generate search indexes for specs."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SPECS_ROOT = SCRIPT_DIR.parent / "specs"


def list_markdown_files(dir_path: Path) -> list[Path]:
    if not dir_path.exists():
        return []
    files: list[Path] = []
    for entry in dir_path.iterdir():
        if entry.is_file() and entry.name.endswith(".md"):
            files.append(entry)
        elif entry.is_dir():
            files.extend(list_markdown_files(entry))
    return files


def detect_category(rel_path: str) -> str:
    segments = rel_path.split("/")
    if len(segments) == 1:
        return "spec"
    first = segments[0]
    if first == "lib":
        return "stdlib"
    if first in {"stdlib", "linters", "formatters", "patterns"}:
        return first
    return "spec"


def main() -> None:
    language_dirs = sorted([p for p in SPECS_ROOT.iterdir() if p.is_dir()])

    root_index = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "languages": [],
    }

    for lang_dir in language_dirs:
        language = lang_dir.name
        files = list_markdown_files(lang_dir)
        entries = []

        for file_path in files:
            rel_path = file_path.relative_to(lang_dir).as_posix()
            content = file_path.read_text(encoding="utf-8")
            entries.append(
                {
                    "path": rel_path,
                    "category": detect_category(rel_path),
                    "name": rel_path.replace(".md", ""),
                    "content": content,
                }
            )

        language_index = {
            "language": language,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "entries": entries,
        }

        (lang_dir / "search.json").write_text(json.dumps(language_index), encoding="utf-8")
        root_index["languages"].append({"language": language, "count": len(entries)})

    (SPECS_ROOT / "search.json").write_text(
        json.dumps(root_index, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
