#!/usr/bin/env python3
"""Attempt to replace stub markdown files with fetched content."""

from __future__ import annotations

import argparse
from pathlib import Path

from _common import FetchError, extract_main, fetch_url, html_to_markdown, log, write_fetched_at

ROOT_DIR = Path(__file__).resolve().parent.parent
SPECS_DIR = ROOT_DIR / "specs"


def is_stub_file(path: Path) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return False
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(lines) > 2:
        return False
    return any(line.startswith("See: ") for line in lines)


def find_stub_url(path: Path) -> str | None:
    content = path.read_text(encoding="utf-8")
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("See: "):
            return stripped.replace("See: ", "", 1).strip()
    return None


def is_binary_url(url: str) -> bool:
    lower = url.lower()
    return any(lower.endswith(suffix) for suffix in (".pdf", ".zip", ".tar.gz", ".tgz"))


def backfill_stub(path: Path, dry_run: bool) -> bool:
    url = find_stub_url(path)
    if not url:
        return False
    if is_binary_url(url):
        log(f"Skipping binary source {url}")
        return False
    if dry_run:
        log(f"Would fetch {url} -> {path.relative_to(ROOT_DIR)}")
        return True
    try:
        html = fetch_url(url)
    except FetchError as exc:
        log(f"Fetch failed for {url}: {exc}", level="warning")
        return False
    main = extract_main(html)
    if html_to_markdown(main, path):
        lang_dir = path.parent
        if path.parent.name in {"stdlib", "linters", "formatters", "patterns", "lib"}:
            lang_dir = path.parent.parent
        write_fetched_at(lang_dir)
        log(f"Replaced stub {path.relative_to(ROOT_DIR)}")
        return True
    log(f"Failed to convert HTML for {url}", level="warning")
    return False


def iter_stub_files(include_all: bool) -> list[Path]:
    targets = []
    for path in SPECS_DIR.rglob("*.md"):
        if not include_all and path.name not in {"spec.md", "overview.md"}:
            continue
        if is_stub_file(path):
            targets.append(path)
    return sorted(targets)


def main() -> None:
    parser = argparse.ArgumentParser(description="Replace stub markdown files by fetching sources.")
    parser.add_argument(
        "--all", action="store_true", help="Process all stub files, not just spec/overview."
    )
    parser.add_argument("--limit", type=int, default=0, help="Limit number of files processed.")
    parser.add_argument("--dry-run", action="store_true", help="Log actions without writing files.")
    args = parser.parse_args()

    stubs = iter_stub_files(include_all=args.all)
    if args.limit > 0:
        stubs = stubs[: args.limit]

    if not stubs:
        print("No stub files found for the selected scope.")
        return

    replaced = 0
    for path in stubs:
        if backfill_stub(path, args.dry_run):
            replaced += 1

    print(f"Processed {len(stubs)} stub files; replaced {replaced}.")


if __name__ == "__main__":
    main()
