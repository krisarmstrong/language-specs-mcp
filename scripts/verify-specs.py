#!/usr/bin/env python3
"""Verify presence and coverage of spec markdown files."""

from __future__ import annotations

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SPECS_ROOT = SCRIPT_DIR.parent / "specs"

CATEGORIES = ["spec", "stdlib", "linters", "formatters", "patterns"]


def has_markdown(dir_path: Path) -> bool:
    if not dir_path.exists():
        return False
    for entry in dir_path.iterdir():
        if entry.is_file() and entry.name.endswith(".md"):
            return True
        if entry.is_dir() and has_markdown(entry):
            return True
    return False


def count_markdown(dir_path: Path) -> int:
    if not dir_path.exists():
        return 0
    count = 0
    for entry in dir_path.iterdir():
        if entry.is_file() and entry.name.endswith(".md"):
            count += 1
        elif entry.is_dir():
            count += count_markdown(entry)
    return count


def count_top_level_markdown(dir_path: Path) -> int:
    if not dir_path.exists():
        return 0
    return sum(1 for entry in dir_path.iterdir() if entry.is_file() and entry.name.endswith(".md"))


def read_fetched_at(dir_path: Path) -> str:
    path = dir_path / ".fetched-at"
    if not path.exists():
        return "unknown"
    content = path.read_text(encoding="utf-8").strip()
    return content or "unknown"


def main() -> None:
    languages = sorted([p for p in SPECS_ROOT.iterdir() if p.is_dir()])
    failures: list[str] = []
    coverage: list[dict[str, object]] = []

    for lang_dir in languages:
        language = lang_dir.name
        if not has_markdown(lang_dir):
            failures.append(f"{language}: no markdown files found")
            continue

        for category in CATEGORIES:
            category_dir = lang_dir / category
            if category_dir.exists() and not has_markdown(category_dir):
                failures.append(f"{language}/{category}: directory exists but has no markdown")

        spec_count = count_top_level_markdown(lang_dir)
        stdlib_dir = lang_dir / "stdlib" if (lang_dir / "stdlib").exists() else lang_dir / "lib"
        stdlib_count = count_markdown(stdlib_dir)
        linters_count = count_markdown(lang_dir / "linters")
        formatters_count = count_markdown(lang_dir / "formatters")
        patterns_count = count_markdown(lang_dir / "patterns")
        fetched_at = read_fetched_at(lang_dir)

        coverage.append(
            {
                "language": language,
                "specCount": spec_count,
                "stdlibCount": stdlib_count,
                "lintersCount": linters_count,
                "formattersCount": formatters_count,
                "patternsCount": patterns_count,
                "fetchedAt": fetched_at,
            }
        )

    coverage_table = [
        "| Language | Spec | Stdlib | Linters | Formatters | Patterns | Fetched (UTC) |",
        "|---|---|---|---|---|---|---|",
        *[
            f"| {row['language']} | {row['specCount']} | {row['stdlibCount']} | {row['lintersCount']} | {row['formattersCount']} | {row['patternsCount']} | {row['fetchedAt']} |"
            for row in coverage
        ],
    ]

    if failures:
        failures_text = "\n".join(f"- {item}" for item in failures)
        table_text = "\n".join(coverage_table)
        raise SystemExit(
            f"Spec verification failed:\n{failures_text}\n\nCoverage summary:\n{table_text}"
        )

    print(f"Spec verification passed for {len(languages)} languages.")
    print("\nCoverage summary:")
    print("\n".join(coverage_table))


if __name__ == "__main__":
    main()
