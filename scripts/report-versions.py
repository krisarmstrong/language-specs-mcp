#!/usr/bin/env python3
"""Report tool versions and optionally latest upstream."""

from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"

CHECK_LATEST = os.getenv("CHECK_LATEST") == "1"


def normalize_version(value: str) -> str:
    return value.lstrip("v").strip()


def strip_tag_prefix(value: str, prefix: str | None) -> str:
    if not prefix:
        return value
    return value[len(prefix) :] if value.startswith(prefix) else value


def fetch_text(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_json(url: str) -> dict:
    return json.loads(fetch_text(url))


def get_latest_version(tool: dict) -> str | None:
    latest = tool.get("latest")
    if not latest or not CHECK_LATEST:
        return None
    latest_type = latest.get("type")

    if latest_type == "go":
        text = fetch_text(latest.get("url", ""))
        return normalize_version(text.replace("go", ""))

    if latest_type == "node":
        data = fetch_json(latest.get("url", ""))
        version = data[0].get("version", "") if isinstance(data, list) and data else ""
        return normalize_version(version)

    if latest_type == "npm":
        pkg = latest.get("package", "")
        data = fetch_json(f"https://registry.npmjs.org/{urllib.parse.quote(pkg)}")
        return normalize_version(data.get("dist-tags", {}).get("latest", ""))

    if latest_type == "pypi":
        pkg = latest.get("package", "")
        data = fetch_json(f"https://pypi.org/pypi/{urllib.parse.quote(pkg)}/json")
        return normalize_version(data.get("info", {}).get("version", ""))

    if latest_type == "github-release":
        repo = latest.get("repo", "")
        data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
        tag = data.get("tag_name", "")
        return normalize_version(strip_tag_prefix(tag, latest.get("tagPrefix")))

    return None


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    rows = []

    for tool in registry.get("tools", []):
        latest = get_latest_version(tool)
        rows.append(
            {
                "name": tool.get("name"),
                "version": tool.get("version"),
                "latest": latest or "-",
                "files": len(tool.get("files", []) or []),
                "sources": len(tool.get("sources", []) or []),
            }
        )

    header = ["Tool", "Version", "Latest", "Files", "Sources"]
    lines = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join('---' for _ in header)} |",
    ]
    for row in rows:
        lines.append(
            f"| {row['name']} | {row['version']} | {row['latest']} | {row['files']} | {row['sources']} |"
        )

    print("\n".join(lines))


if __name__ == "__main__":
    main()
