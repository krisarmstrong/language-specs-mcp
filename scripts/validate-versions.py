#!/usr/bin/env python3
"""Validate tool versions registry against spec files and optionally latest upstream."""

from __future__ import annotations

import json
import os
from pathlib import Path

from _common import FetchError, get_latest_version, log, normalize_version

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "tools" / "versions.json"

CHECK_LATEST = os.getenv("CHECK_LATEST") == "1"


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
                latest = get_latest_version(tool, check_enabled=True)
                if latest and normalize_version(tool.get("version", "")) != latest:
                    failures.append(
                        f"{tool.get('name')}: registry {tool.get('version')} != latest {latest}"
                    )
            except FetchError as exc:
                log(f"Latest version check failed for {tool.get('name')}: {exc}", level="warning")
                failures.append(f"{tool.get('name')}: failed to check latest version")
            except OSError as exc:
                log(f"Latest version check failed for {tool.get('name')}: {exc}", level="warning")
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
