#!/usr/bin/env python3
"""Stamp tool versions into spec markdown files."""

from __future__ import annotations

import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"


def build_heading(file_path: str, tool_name: str) -> str:
    if "/linters/" in file_path:
        return f"# {tool_name} Version"
    if "/formatters/" in file_path:
        return f"# {tool_name} Version"
    if file_path.endswith("/spec.md"):
        return f"# {tool_name} Specification"
    if file_path.endswith("compilers.md"):
        return "# Compilers"
    return f"# {tool_name} Version"


def upcase_label(label: str) -> str:
    return label[:1].upper() + label[1:] if label else label


def update_content(content: str, label: str, version: str, fallback_heading: str) -> str:
    lines = content.split("\n")
    try:
        heading_index = next(i for i, line in enumerate(lines) if line.startswith("# "))
    except StopIteration:
        lines.insert(0, fallback_heading)
        lines.insert(1, "")
        heading_index = 0

    formatted_label = upcase_label(label)
    target_prefix = f"{formatted_label}:"
    new_line = f"{formatted_label}: {version}"

    for i, line in enumerate(lines):
        if line.startswith(target_prefix):
            lines[i] = new_line
            return "\n".join(lines)

    insert_at = heading_index + 1
    if lines[insert_at:insert_at + 1] != [""]:
        lines.insert(insert_at, "")
        insert_at += 1
    lines.insert(insert_at, new_line)
    lines.insert(insert_at + 1, "")
    return "\n".join(lines)


def ensure_sources(content: str, sources: list[str], label: str, version: str) -> str:
    if not sources:
        return content
    lines = content.split("\n")
    formatted_label = upcase_label(label)
    version_line = f"{formatted_label}: {version}"

    try:
        version_index = lines.index(version_line)
    except ValueError:
        version_index = 1

    insert_index = version_index + 1
    for source in sources:
        source_line = f"Source: {source}"
        if source_line not in lines:
            lines.insert(insert_index, source_line)
            insert_index += 1
    if insert_index < len(lines) and lines[insert_index] != "":
        lines.insert(insert_index, "")
    return "\n".join(lines)


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    entries_by_file: dict[str, list[dict]] = {}

    for tool in registry.get("tools", []):
        label = tool.get("label") or "Version"
        for file in tool.get("files", []) or []:
            entries_by_file.setdefault(file, []).append(
                {
                    "label": label,
                    "version": tool.get("version", ""),
                    "tool_name": tool.get("name", ""),
                    "sources": tool.get("sources", []) or [],
                }
            )

    for file_path, entries in entries_by_file.items():
        full_path = ROOT_DIR / file_path
        tool_names = ", ".join(entry["tool_name"] for entry in entries)
        fallback_heading = build_heading(file_path, tool_names)

        if full_path.exists():
            content = full_path.read_text(encoding="utf-8")
        else:
            content = f"{fallback_heading}\n"

        updated = content
        for entry in entries:
            updated = update_content(
                updated,
                entry["label"],
                entry["version"],
                fallback_heading,
            )
            updated = ensure_sources(
                updated,
                entry["sources"],
                entry["label"],
                entry["version"],
            )

        if not updated.endswith("\n"):
            updated += "\n"
        full_path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
