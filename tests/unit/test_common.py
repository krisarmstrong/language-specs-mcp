#!/usr/bin/env python3
"""Unit tests for _common.py utilities."""

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from _common import (
    SPECS_DIR,
    normalize_version,
    write_text,
    write_fetched_at,
)


class TestNormalizeVersion:
    """Tests for version normalization."""

    def test_strips_v_prefix(self):
        assert normalize_version("v1.2.3") == "1.2.3"

    def test_handles_no_prefix(self):
        assert normalize_version("1.2.3") == "1.2.3"

    def test_handles_empty_string(self):
        assert normalize_version("") == ""

    def test_preserves_complex_versions(self):
        assert normalize_version("v2.0.0-beta.1") == "2.0.0-beta.1"


class TestWriteText:
    """Tests for write_text utility."""

    def test_creates_file(self, tmp_path):
        test_file = tmp_path / "test.txt"
        write_text(test_file, "hello world")
        assert test_file.read_text() == "hello world"

    def test_overwrites_existing(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("old content")
        write_text(test_file, "new content")
        assert test_file.read_text() == "new content"

    def test_creates_parent_dirs(self, tmp_path):
        test_file = tmp_path / "sub" / "dir" / "test.txt"
        write_text(test_file, "nested")
        assert test_file.read_text() == "nested"

    def test_handles_unicode(self, tmp_path):
        test_file = tmp_path / "unicode.txt"
        content = "Hello 世界 🌍"
        write_text(test_file, content)
        assert test_file.read_text(encoding="utf-8") == content


class TestWriteFetchedAt:
    """Tests for write_fetched_at utility."""

    def test_creates_fetched_at_file(self, tmp_path):
        write_fetched_at(tmp_path)
        fetched_at = tmp_path / ".fetched-at"
        assert fetched_at.exists()
        content = fetched_at.read_text()
        # Should be ISO format
        assert "T" in content
        assert "Z" in content or "+" in content

    def test_overwrites_existing(self, tmp_path):
        fetched_at = tmp_path / ".fetched-at"
        fetched_at.write_text("old-timestamp")
        write_fetched_at(tmp_path)
        content = fetched_at.read_text()
        assert content != "old-timestamp"


class TestSpecsDir:
    """Tests for SPECS_DIR constant."""

    def test_specs_dir_exists(self):
        assert SPECS_DIR.exists()
        assert SPECS_DIR.is_dir()

    def test_specs_dir_has_languages(self):
        languages = [d.name for d in SPECS_DIR.iterdir() if d.is_dir()]
        assert "python" in languages
        assert "typescript" in languages
        assert "go" in languages


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
