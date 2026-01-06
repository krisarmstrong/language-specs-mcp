#!/usr/bin/env python3
"""Update tool versions registry from upstream sources."""

from __future__ import annotations

import json
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from _common import FetchError, fetch_url, is_prerelease_version, log

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
    return fetch_url(url)


def fetch_json(url: str) -> dict:
    return json.loads(fetch_text(url))


def fetch_github_tag(repo: str, tag_prefix: str | None) -> str:
    data = fetch_json(f"https://api.github.com/repos/{repo}/tags?per_page=100")
    if not isinstance(data, list):
        return ""
    for entry in data:
        name = entry.get("name", "")
        if tag_prefix and not name.startswith(tag_prefix):
            continue
        normalized = normalize_version(strip_tag_prefix(name, tag_prefix))
        if not is_prerelease_version(normalized):
            return name
    return ""


def get_latest_version(tool: dict) -> str | None:
    latest = tool.get("latest")
    if not latest:
        return None
    latest_type = latest.get("type")

    if latest_type == "go":
        text = fetch_text(latest.get("url", "")).splitlines()[0]
        version = normalize_version(text.replace("go", ""))
        return None if is_prerelease_version(version) else version

    if latest_type == "node":
        data = fetch_json(latest.get("url", ""))
        if isinstance(data, list):
            for entry in data:
                version = normalize_version(entry.get("version", ""))
                if version and not is_prerelease_version(version):
                    return version
        return None

    if latest_type == "npm":
        pkg = latest.get("package", "")
        data = fetch_json(f"https://registry.npmjs.org/{urllib.parse.quote(pkg)}")
        version = normalize_version(data.get("dist-tags", {}).get("latest", ""))
        return None if is_prerelease_version(version) else version

    if latest_type == "pypi":
        pkg = latest.get("package", "")
        data = fetch_json(f"https://pypi.org/pypi/{urllib.parse.quote(pkg)}/json")
        version = normalize_version(data.get("info", {}).get("version", ""))
        return None if is_prerelease_version(version) else version

    if latest_type == "github-release":
        repo = latest.get("repo", "")
        try:
            data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
            tag = data.get("tag_name", "")
        except FetchError as exc:
            if "HTTP Error 404" not in str(exc):
                raise
            tag = fetch_github_tag(repo, latest.get("tagPrefix"))
        version = normalize_version(strip_tag_prefix(tag, latest.get("tagPrefix")))
        if is_prerelease_version(version):
            tag = fetch_github_tag(repo, latest.get("tagPrefix"))
            version = normalize_version(strip_tag_prefix(tag, latest.get("tagPrefix")))
        return None if is_prerelease_version(version) else version

    return None


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    checked_at = datetime.now(timezone.utc).isoformat()
    for tool in registry.get("tools", []):
        try:
            latest = get_latest_version(tool)
            if tool.get("latest"):
                tool["checkedAt"] = checked_at
            if latest:
                tool["version"] = latest
        except FetchError as exc:
            log(f"Version check failed for {tool.get('name')}: {exc}", level="warning")
        except OSError as exc:
            log(f"Version check failed for {tool.get('name')}: {exc}", level="warning")

    registry["updatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
