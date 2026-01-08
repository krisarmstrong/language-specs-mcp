#!/usr/bin/env python3
"""Shared pytest fixtures for specforge-mcp tests."""

import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path for all tests
SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))


@pytest.fixture
def specs_dir(tmp_path):
    """Create a temporary specs directory structure."""
    specs = tmp_path / "specs"
    specs.mkdir()
    return specs


@pytest.fixture
def sample_language(specs_dir):
    """Create a sample language directory with sources.json."""
    lang_dir = specs_dir / "python"
    lang_dir.mkdir()

    sources = {
        "language": "python",
        "version": "3.12",
        "files": [
            {"path": "spec.md", "urls": ["https://example.com/spec"]},
            {"path": "stdlib/os.md", "urls": ["https://example.com/os"]},
        ],
    }
    (lang_dir / "sources.json").write_text(json.dumps(sources))
    return lang_dir


@pytest.fixture
def sample_registry(tmp_path):
    """Create a sample tool versions registry."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()

    registry = {
        "tools": [
            {
                "name": "python",
                "version": "3.12.0",
                "label": "version",
                "files": ["specs/python/spec.md"],
                "sources": ["https://python.org"],
            },
            {
                "name": "typescript",
                "version": "5.3.0",
                "label": "version",
                "files": ["specs/typescript/spec.md"],
            },
        ]
    }
    (tools_dir / "versions.json").write_text(json.dumps(registry))
    return tools_dir / "versions.json"


@pytest.fixture
def mock_fetch(monkeypatch):
    """Mock fetch_url to avoid actual network requests."""

    def fake_fetch(url: str) -> str:
        return f"# Content from {url}\n\nSample markdown content."

    monkeypatch.setattr("_common.fetch_url", fake_fetch)
    return fake_fetch
