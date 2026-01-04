#!/usr/bin/env python3
"""Generate specs index files."""

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


def to_posix(path: Path) -> str:
    return path.as_posix()


def to_entry(category: str, lang_dir: Path, file_path: Path) -> dict[str, str]:
    rel = to_posix(file_path.relative_to(lang_dir))
    name = rel.replace(".md", "")
    return {"category": category, "path": rel, "name": name}


def read_fetched_at(lang_dir: Path) -> str:
    path = lang_dir / ".fetched-at"
    if not path.exists():
        return "unknown"
    content = path.read_text(encoding="utf-8").strip()
    return content or "unknown"


def main() -> None:
    language_dirs = sorted([p for p in SPECS_ROOT.iterdir() if p.is_dir()])

    root_index = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "languages": [],
    }

    for lang_dir in language_dirs:
        language = lang_dir.name
        fetched_at = read_fetched_at(lang_dir)

        top_level_entries = [
            entry
            for entry in lang_dir.iterdir()
            if entry.is_file() and entry.name.endswith(".md")
        ]
        spec_entries = [to_entry("spec", lang_dir, file_path) for file_path in top_level_entries]

        stdlib_dir = lang_dir / "stdlib" if (lang_dir / "stdlib").exists() else lang_dir / "lib"
        stdlib_files = list_markdown_files(stdlib_dir)
        stdlib_entries = [to_entry("stdlib", lang_dir, file_path) for file_path in stdlib_files]

        linter_files = list_markdown_files(lang_dir / "linters")
        linter_entries = [to_entry("linters", lang_dir, file_path) for file_path in linter_files]

        formatter_files = list_markdown_files(lang_dir / "formatters")
        formatter_entries = [
            to_entry("formatters", lang_dir, file_path) for file_path in formatter_files
        ]

        pattern_files = list_markdown_files(lang_dir / "patterns")
        pattern_entries = [to_entry("patterns", lang_dir, file_path) for file_path in pattern_files]

        categories = {
            "spec": spec_entries,
            "stdlib": stdlib_entries,
            "linters": linter_entries,
            "formatters": formatter_entries,
            "patterns": pattern_entries,
        }

        counts = {
            "spec": len(spec_entries),
            "stdlib": len(stdlib_entries),
            "linters": len(linter_entries),
            "formatters": len(formatter_entries),
            "patterns": len(pattern_entries),
        }

        items = [*spec_entries, *stdlib_entries, *linter_entries, *formatter_entries, *pattern_entries]

        lang_index = {
            "language": language,
            "fetchedAt": fetched_at,
            "counts": counts,
            "categories": categories,
            "items": items,
        }

        (lang_dir / "index.json").write_text(json.dumps(lang_index, indent=2), encoding="utf-8")

        root_index["languages"].append({"language": language, "fetchedAt": fetched_at, "counts": counts})

    (SPECS_ROOT / "index.json").write_text(json.dumps(root_index, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
