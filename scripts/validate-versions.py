#!/usr/bin/env python3
"""Validate tool versions registry against spec files and optionally latest upstream."""

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


def file_has_version_line(file_path: str, label: str, version: str) -> bool:
    full_path = ROOT_DIR / file_path
    content = full_path.read_text(encoding="utf-8")
    formatted_label = label[:1].upper() + label[1:]
    target = f"{formatted_label}: {version}"
    return target in content


def file_has_sources(file_path: str, sources: list[str]) -> bool:
    if not sources:
        return True
    full_path = ROOT_DIR / file_path
    content = full_path.read_text(encoding="utf-8")
    return all(source in content for source in sources)


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
        version = data.get("dist-tags", {}).get("latest", "")
        return normalize_version(version)

    if latest_type == "pypi":
        pkg = latest.get("package", "")
        data = fetch_json(f"https://pypi.org/pypi/{urllib.parse.quote(pkg)}/json")
        version = data.get("info", {}).get("version", "")
        return normalize_version(version)

    if latest_type == "github-release":
        repo = latest.get("repo", "")
        data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
        tag = data.get("tag_name", "")
        stripped = strip_tag_prefix(tag, latest.get("tagPrefix"))
        return normalize_version(stripped)

    return None


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    failures: list[str] = []
    warnings: list[str] = []

    for tool in registry.get("tools", []):
        if tool.get("latest") and tool.get("version") == "unknown":
            failures.append(f"{tool.get('name')}: version is unknown but has a latest source")

        files = tool.get("files", []) or []
        if not files:
            warnings.append(f"{tool.get('name')}: no file references to validate")
        else:
            label = tool.get("label") or "Version"
            for file in files:
                try:
                    if not file_has_version_line(file, label, tool.get("version", "")):
                        failures.append(
                            f"{tool.get('name')}: missing {label}: {tool.get('version')} in {file}"
                        )
                    if not file_has_sources(file, tool.get("sources", []) or []):
                        failures.append(
                            f"{tool.get('name')}: missing source URL in {file}"
                        )
                except OSError:
                    failures.append(f"{tool.get('name')}: unable to read {file}")

        if CHECK_LATEST:
            try:
                latest = get_latest_version(tool)
                if latest and normalize_version(tool.get("version", "")) != latest:
                    failures.append(
                        f"{tool.get('name')}: registry {tool.get('version')} != latest {latest}"
                    )
            except OSError:
                failures.append(f"{tool.get('name')}: failed to check latest version")

    if warnings:
        print("Warnings:")
        print("\n".join(f"- {item}" for item in warnings))

    if failures:
        raise SystemExit(
            "Version validation failed:\n" + "\n".join(f"- {item}" for item in failures)
        )

    print("Version validation passed.")


if __name__ == "__main__":
    main()
