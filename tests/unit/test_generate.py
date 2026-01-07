#!/usr/bin/env python3
"""Unit tests for generate.py."""

import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from generate import (
    list_markdown_files,
    read_fetched_at,
    get_language_dirs,
    to_entry,
    detect_category,
)


class TestListMarkdownFiles:
    """Tests for list_markdown_files function."""

    def test_finds_md_files(self, tmp_path):
        (tmp_path / "test.md").write_text("# Test")
        (tmp_path / "other.md").write_text("# Other")
        files = list_markdown_files(tmp_path)
        assert len(files) == 2
        assert all(f.suffix == ".md" for f in files)

    def test_recursive_search(self, tmp_path):
        (tmp_path / "root.md").write_text("# Root")
        subdir = tmp_path / "sub"
        subdir.mkdir()
        (subdir / "nested.md").write_text("# Nested")
        files = list_markdown_files(tmp_path)
        assert len(files) == 2

    def test_ignores_non_md(self, tmp_path):
        (tmp_path / "test.md").write_text("# Test")
        (tmp_path / "test.txt").write_text("Text")
        (tmp_path / "test.json").write_text("{}")
        files = list_markdown_files(tmp_path)
        assert len(files) == 1

    def test_empty_dir(self, tmp_path):
        files = list_markdown_files(tmp_path)
        assert files == []

    def test_nonexistent_dir(self, tmp_path):
        files = list_markdown_files(tmp_path / "nonexistent")
        assert files == []


class TestReadFetchedAt:
    """Tests for read_fetched_at function."""

    def test_reads_timestamp(self, tmp_path):
        (tmp_path / ".fetched-at").write_text("2024-01-01T00:00:00Z")
        result = read_fetched_at(tmp_path)
        assert result == "2024-01-01T00:00:00Z"

    def test_missing_file(self, tmp_path):
        result = read_fetched_at(tmp_path)
        assert result == "unknown"

    def test_empty_file(self, tmp_path):
        (tmp_path / ".fetched-at").write_text("")
        result = read_fetched_at(tmp_path)
        assert result == "unknown"

    def test_strips_whitespace(self, tmp_path):
        (tmp_path / ".fetched-at").write_text("  2024-01-01T00:00:00Z  \n")
        result = read_fetched_at(tmp_path)
        assert result == "2024-01-01T00:00:00Z"


class TestDetectCategory:
    """Tests for detect_category function."""

    def test_top_level_is_spec(self):
        assert detect_category("spec.md") == "spec"
        assert detect_category("overview.md") == "spec"

    def test_stdlib_category(self):
        assert detect_category("stdlib/os.md") == "stdlib"
        assert detect_category("stdlib/sub/module.md") == "stdlib"

    def test_lib_mapped_to_stdlib(self):
        assert detect_category("lib/core.md") == "stdlib"

    def test_linters_category(self):
        assert detect_category("linters/eslint/no-unused-vars.md") == "linters"

    def test_formatters_category(self):
        assert detect_category("formatters/prettier.md") == "formatters"

    def test_patterns_category(self):
        assert detect_category("patterns/singleton.md") == "patterns"

    def test_unknown_defaults_to_spec(self):
        assert detect_category("random/thing.md") == "spec"


class TestToEntry:
    """Tests for to_entry function."""

    def test_creates_entry(self, tmp_path):
        file_path = tmp_path / "test.md"
        file_path.write_text("# Test")
        entry = to_entry("spec", tmp_path, file_path)
        assert entry["category"] == "spec"
        assert entry["path"] == "test.md"
        assert entry["name"] == "test"

    def test_nested_path(self, tmp_path):
        subdir = tmp_path / "sub"
        subdir.mkdir()
        file_path = subdir / "nested.md"
        file_path.write_text("# Nested")
        entry = to_entry("stdlib", tmp_path, file_path)
        assert entry["path"] == "sub/nested.md"
        assert entry["name"] == "sub/nested"


class TestGetLanguageDirs:
    """Tests for get_language_dirs function."""

    def test_returns_directories(self):
        dirs = get_language_dirs()
        assert len(dirs) > 0
        assert all(d.is_dir() for d in dirs)

    def test_excludes_hidden(self):
        dirs = get_language_dirs()
        names = [d.name for d in dirs]
        assert not any(n.startswith("_") for n in names)
        assert not any(n.startswith(".") for n in names)

    def test_sorted(self):
        dirs = get_language_dirs()
        names = [d.name for d in dirs]
        assert names == sorted(names)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
