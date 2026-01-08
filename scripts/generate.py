#!/usr/bin/env python3
"""Generate spec indexes and search data.

Consolidates generate-index and generate-search-index.
Note: generate-manifests.py is deprecated as sources.json is now manually curated.

Usage:
    python scripts/generate.py index    # Generate spec index files
    python scripts/generate.py search   # Generate search indexes
    python scripts/generate.py all      # Run all generators
"""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
SPECS_ROOT = ROOT_DIR / "specs"


# --- Shared Utilities ---


def list_markdown_files(dir_path: Path) -> list[Path]:
    """Recursively list all markdown files in a directory."""
    if not dir_path.exists():
        return []
    files: list[Path] = []
    for entry in dir_path.iterdir():
        if entry.is_file() and entry.name.endswith(".md"):
            files.append(entry)
        elif entry.is_dir():
            files.extend(list_markdown_files(entry))
    return files


def read_fetched_at(lang_dir: Path) -> str:
    """Read the .fetched-at timestamp for a language."""
    path = lang_dir / ".fetched-at"
    if not path.exists():
        return "unknown"
    content = path.read_text(encoding="utf-8").strip()
    return content or "unknown"


def get_language_dirs() -> list[Path]:
    """Get all language directories."""
    return sorted([p for p in SPECS_ROOT.iterdir() if p.is_dir() and not p.name.startswith("_")])


# --- Index Command ---


def to_entry(category: str, lang_dir: Path, file_path: Path) -> dict[str, str]:
    """Create an index entry for a file."""
    rel = file_path.relative_to(lang_dir).as_posix()
    name = rel.replace(".md", "")
    return {"category": category, "path": rel, "name": name}


def cmd_index() -> int:
    """Generate spec index files."""
    language_dirs = get_language_dirs()

    root_index: dict[str, Any] = {
        "generatedAt": datetime.now(UTC).isoformat(),
        "languages": [],
    }

    for lang_dir in language_dirs:
        language = lang_dir.name
        fetched_at = read_fetched_at(lang_dir)

        # Top-level spec files
        top_level = [f for f in lang_dir.iterdir() if f.is_file() and f.name.endswith(".md")]
        spec_entries = [to_entry("spec", lang_dir, f) for f in top_level]

        # Standard library
        stdlib_dir = lang_dir / "stdlib" if (lang_dir / "stdlib").exists() else lang_dir / "lib"
        stdlib_entries = [to_entry("stdlib", lang_dir, f) for f in list_markdown_files(stdlib_dir)]

        # Linters
        linter_entries = [
            to_entry("linters", lang_dir, f) for f in list_markdown_files(lang_dir / "linters")
        ]

        # Formatters
        formatter_entries = [
            to_entry("formatters", lang_dir, f)
            for f in list_markdown_files(lang_dir / "formatters")
        ]

        # Patterns
        pattern_entries = [
            to_entry("patterns", lang_dir, f) for f in list_markdown_files(lang_dir / "patterns")
        ]

        categories = {
            "spec": spec_entries,
            "stdlib": stdlib_entries,
            "linters": linter_entries,
            "formatters": formatter_entries,
            "patterns": pattern_entries,
        }

        counts = {k: len(v) for k, v in categories.items()}

        items = [
            *spec_entries,
            *stdlib_entries,
            *linter_entries,
            *formatter_entries,
            *pattern_entries,
        ]

        lang_index = {
            "language": language,
            "fetchedAt": fetched_at,
            "counts": counts,
            "categories": categories,
            "items": items,
        }

        (lang_dir / "index.json").write_text(json.dumps(lang_index, indent=2), encoding="utf-8")
        root_index["languages"].append(
            {"language": language, "fetchedAt": fetched_at, "counts": counts}
        )

    (SPECS_ROOT / "index.json").write_text(json.dumps(root_index, indent=2), encoding="utf-8")
    print(f"Generated index for {len(language_dirs)} languages")
    return 0


# --- Search Command ---


def detect_category(rel_path: str) -> str:
    """Detect the category of a file from its path."""
    segments = rel_path.split("/")
    if len(segments) == 1:
        return "spec"
    first = segments[0]
    if first == "lib":
        return "stdlib"
    if first in {"stdlib", "linters", "formatters", "patterns"}:
        return first
    return "spec"


def cmd_search() -> int:
    """Generate search indexes."""
    language_dirs = get_language_dirs()

    root_index: dict[str, Any] = {
        "generatedAt": datetime.now(UTC).isoformat(),
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
            "generatedAt": datetime.now(UTC).isoformat(),
            "entries": entries,
        }

        (lang_dir / "search.json").write_text(json.dumps(language_index), encoding="utf-8")
        root_index["languages"].append({"language": language, "count": len(entries)})

    (SPECS_ROOT / "search.json").write_text(json.dumps(root_index, indent=2), encoding="utf-8")
    print(f"Generated search index for {len(language_dirs)} languages")
    return 0


# --- All Command ---


def cmd_all() -> int:
    """Run all generators."""
    result = 0

    print("=== Generating indexes ===")
    result |= cmd_index()

    print("\n=== Generating search indexes ===")
    result |= cmd_search()

    return result


# --- Main ---

COMMANDS = {
    "index": cmd_index,
    "search": cmd_search,
    "all": cmd_all,
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Commands:")
        print("  index   Generate spec index files")
        print("  search  Generate search indexes")
        print("  all     Run all generators")
        return 0

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(COMMANDS.keys())}")
        return 1

    return COMMANDS[cmd]()


if __name__ == "__main__":
    sys.exit(main())
