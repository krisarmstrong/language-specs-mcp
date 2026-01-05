#!/usr/bin/env python3
"""Generate provenance manifests for specs."""

from __future__ import annotations

import hashlib
import json
import re
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


def extract_urls(content: str) -> list[str]:
    matches = re.findall(r"https?://[^\s)\"']+", content)
    cleaned = [re.sub(r"[),.;\]]+$", "", url) for url in matches]
    return sorted(set(cleaned))


def sha256_hex(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def main() -> None:
    language_dirs = sorted([p for p in SPECS_ROOT.iterdir() if p.is_dir()])

    for lang_dir in language_dirs:
        language = lang_dir.name
        files = list_markdown_files(lang_dir)
        manifest = {
            "language": language,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "files": [],
        }

        for file_path in files:
            content = file_path.read_text(encoding="utf-8")
            manifest["files"].append(
                {
                    "path": file_path.relative_to(lang_dir).as_posix(),
                    "sha256": sha256_hex(content),
                    "urls": extract_urls(content),
                }
            )

        (lang_dir / "sources.json").write_text(
            json.dumps(manifest, indent=2),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
