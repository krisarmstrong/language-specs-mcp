#!/usr/bin/env python3
"""Update tool versions registry from upstream sources."""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"


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
    if not latest:
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

    for tool in registry.get("tools", []):
        try:
            latest = get_latest_version(tool)
            if latest:
                tool["version"] = latest
        except OSError:
            continue

    registry["updatedAt"] = datetime.utcnow().strftime("%Y-%m-%d")
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
