#!/usr/bin/env python3
"""Unit tests for generate.py."""

import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from generate import (
    cmd_all,
    cmd_index,
    cmd_search,
    detect_category,
    get_language_dirs,
    list_markdown_files,
    main,
    read_fetched_at,
    to_entry,
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

    def test_deeply_nested(self, tmp_path):
        """Test deeply nested directory structure."""
        deep = tmp_path / "a" / "b" / "c"
        deep.mkdir(parents=True)
        (deep / "deep.md").write_text("# Deep")
        files = list_markdown_files(tmp_path)
        assert len(files) == 1
        assert files[0].name == "deep.md"


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

    def test_whitespace_only(self, tmp_path):
        """Test file with only whitespace."""
        (tmp_path / ".fetched-at").write_text("   \n\t  ")
        result = read_fetched_at(tmp_path)
        assert result == "unknown"


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

    def test_nested_stdlib(self):
        """Test deeply nested stdlib paths."""
        assert detect_category("stdlib/os/path/sub.md") == "stdlib"

    def test_nested_lib(self):
        """Test deeply nested lib paths."""
        assert detect_category("lib/core/utils.md") == "stdlib"


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

    def test_deeply_nested_entry(self, tmp_path):
        """Test deeply nested file entry."""
        deep_path = tmp_path / "a" / "b" / "c"
        deep_path.mkdir(parents=True)
        file_path = deep_path / "deep.md"
        file_path.write_text("# Deep")
        entry = to_entry("linters", tmp_path, file_path)
        assert entry["path"] == "a/b/c/deep.md"
        assert entry["name"] == "a/b/c/deep"
        assert entry["category"] == "linters"


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


class TestCmdIndex:
    """Tests for cmd_index function (index generation)."""

    def test_generates_index_files(self, tmp_path, monkeypatch):
        """Test that cmd_index generates index.json files."""
        # Create mock specs directory structure
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create a language directory with content
        python_dir = specs_dir / "python"
        python_dir.mkdir()
        (python_dir / ".fetched-at").write_text("2024-01-15T12:00:00Z")
        (python_dir / "spec.md").write_text("# Python Spec")

        # Create stdlib directory
        stdlib_dir = python_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "os.md").write_text("# OS Module")

        # Create linters directory
        linters_dir = python_dir / "linters"
        linters_dir.mkdir()
        (linters_dir / "pylint.md").write_text("# Pylint")

        # Patch SPECS_ROOT
        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        # Run cmd_index
        result = cmd_index()

        # Check return value
        assert result == 0

        # Check root index.json was created
        root_index_path = specs_dir / "index.json"
        assert root_index_path.exists()
        root_index = json.loads(root_index_path.read_text())
        assert "generatedAt" in root_index
        assert "languages" in root_index
        assert len(root_index["languages"]) == 1
        assert root_index["languages"][0]["language"] == "python"

        # Check language index.json was created
        lang_index_path = python_dir / "index.json"
        assert lang_index_path.exists()
        lang_index = json.loads(lang_index_path.read_text())
        assert lang_index["language"] == "python"
        assert lang_index["fetchedAt"] == "2024-01-15T12:00:00Z"
        assert "counts" in lang_index
        assert "categories" in lang_index
        assert "items" in lang_index

    def test_handles_lib_directory(self, tmp_path, monkeypatch):
        """Test that lib directory is recognized as stdlib."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "ruby"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        # Use lib instead of stdlib
        lib_dir = lang_dir / "lib"
        lib_dir.mkdir()
        (lib_dir / "core.md").write_text("# Core")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        lang_index = json.loads((lang_dir / "index.json").read_text())
        assert lang_index["counts"]["stdlib"] == 1

    def test_handles_formatters(self, tmp_path, monkeypatch):
        """Test that formatters directory is processed."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "javascript"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        formatters_dir = lang_dir / "formatters"
        formatters_dir.mkdir()
        (formatters_dir / "prettier.md").write_text("# Prettier")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        lang_index = json.loads((lang_dir / "index.json").read_text())
        assert lang_index["counts"]["formatters"] == 1

    def test_handles_patterns(self, tmp_path, monkeypatch):
        """Test that patterns directory is processed."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "java"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        patterns_dir = lang_dir / "patterns"
        patterns_dir.mkdir()
        (patterns_dir / "singleton.md").write_text("# Singleton")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        lang_index = json.loads((lang_dir / "index.json").read_text())
        assert lang_index["counts"]["patterns"] == 1

    def test_empty_language_dir(self, tmp_path, monkeypatch):
        """Test handling of empty language directory."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "empty"
        lang_dir.mkdir()

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        lang_index = json.loads((lang_dir / "index.json").read_text())
        assert lang_index["language"] == "empty"
        assert all(count == 0 for count in lang_index["counts"].values())

    def test_multiple_languages(self, tmp_path, monkeypatch):
        """Test processing multiple language directories."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        for lang in ["python", "javascript", "rust"]:
            lang_dir = specs_dir / lang
            lang_dir.mkdir()
            (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")
            (lang_dir / "spec.md").write_text(f"# {lang.title()} Spec")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        root_index = json.loads((specs_dir / "index.json").read_text())
        assert len(root_index["languages"]) == 3


class TestCmdSearch:
    """Tests for cmd_search function (search index generation)."""

    def test_generates_search_index(self, tmp_path, monkeypatch):
        """Test that cmd_search generates search.json files."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        (python_dir / "spec.md").write_text("# Python Language Specification\n\nContent here.")

        stdlib_dir = python_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "os.md").write_text("# OS Module\n\nOS operations.")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_search()
        assert result == 0

        # Check root search.json
        root_search_path = specs_dir / "search.json"
        assert root_search_path.exists()
        root_search = json.loads(root_search_path.read_text())
        assert "generatedAt" in root_search
        assert "languages" in root_search
        assert len(root_search["languages"]) == 1
        assert root_search["languages"][0]["language"] == "python"
        assert root_search["languages"][0]["count"] == 2

        # Check language search.json
        lang_search_path = python_dir / "search.json"
        assert lang_search_path.exists()
        lang_search = json.loads(lang_search_path.read_text())
        assert lang_search["language"] == "python"
        assert len(lang_search["entries"]) == 2

    def test_search_entry_structure(self, tmp_path, monkeypatch):
        """Test structure of search entries."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Test Content\n\nThis is test content.")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_search()
        assert result == 0

        lang_search = json.loads((lang_dir / "search.json").read_text())
        entry = lang_search["entries"][0]

        assert "path" in entry
        assert "category" in entry
        assert "name" in entry
        assert "content" in entry
        assert entry["path"] == "spec.md"
        assert entry["category"] == "spec"
        assert entry["name"] == "spec"
        assert "# Test Content" in entry["content"]

    def test_search_category_detection(self, tmp_path, monkeypatch):
        """Test category detection in search entries."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()

        # Create files in different categories
        (lang_dir / "top.md").write_text("# Top level")

        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "module.md").write_text("# Module")

        linters_dir = lang_dir / "linters"
        linters_dir.mkdir()
        (linters_dir / "rule.md").write_text("# Rule")

        lib_dir = lang_dir / "lib"
        lib_dir.mkdir()
        (lib_dir / "lib.md").write_text("# Lib")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_search()
        assert result == 0

        lang_search = json.loads((lang_dir / "search.json").read_text())
        entries = {e["path"]: e["category"] for e in lang_search["entries"]}

        assert entries["top.md"] == "spec"
        assert entries["stdlib/module.md"] == "stdlib"
        assert entries["linters/rule.md"] == "linters"
        assert entries["lib/lib.md"] == "stdlib"

    def test_empty_language_search(self, tmp_path, monkeypatch):
        """Test search index for empty language directory."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "empty"
        lang_dir.mkdir()

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_search()
        assert result == 0

        lang_search = json.loads((lang_dir / "search.json").read_text())
        assert lang_search["entries"] == []

    def test_multiple_languages_search(self, tmp_path, monkeypatch):
        """Test search index for multiple languages."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        for lang in ["go", "rust"]:
            lang_dir = specs_dir / lang
            lang_dir.mkdir()
            (lang_dir / "spec.md").write_text(f"# {lang.title()} Spec")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_search()
        assert result == 0

        root_search = json.loads((specs_dir / "search.json").read_text())
        assert len(root_search["languages"]) == 2


class TestCmdAll:
    """Tests for cmd_all function."""

    def test_runs_both_commands(self, tmp_path, monkeypatch, capsys):
        """Test that cmd_all runs both index and search."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")
        (lang_dir / "spec.md").write_text("# Python")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_all()
        assert result == 0

        # Both index.json and search.json should be created
        assert (specs_dir / "index.json").exists()
        assert (specs_dir / "search.json").exists()
        assert (lang_dir / "index.json").exists()
        assert (lang_dir / "search.json").exists()

        # Check output messages
        captured = capsys.readouterr()
        assert "Generating indexes" in captured.out
        assert "Generating search indexes" in captured.out

    def test_returns_combined_result(self, tmp_path, monkeypatch):
        """Test that cmd_all returns combined result code."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        # Both commands should succeed even with empty specs
        result = cmd_all()
        assert result == 0


class TestMain:
    """Tests for main function (CLI handling)."""

    def test_help_flag(self, monkeypatch, capsys):
        """Test --help flag displays help."""
        monkeypatch.setattr("sys.argv", ["generate.py", "--help"])

        result = main()
        assert result == 0

        captured = capsys.readouterr()
        assert "Commands:" in captured.out
        assert "index" in captured.out
        assert "search" in captured.out
        assert "all" in captured.out

    def test_h_flag(self, monkeypatch, capsys):
        """Test -h flag displays help."""
        monkeypatch.setattr("sys.argv", ["generate.py", "-h"])

        result = main()
        assert result == 0

        captured = capsys.readouterr()
        assert "Commands:" in captured.out

    def test_no_args_shows_help(self, monkeypatch, capsys):
        """Test no arguments shows help."""
        monkeypatch.setattr("sys.argv", ["generate.py"])

        result = main()
        assert result == 0

        captured = capsys.readouterr()
        assert "Commands:" in captured.out

    def test_unknown_command(self, monkeypatch, capsys):
        """Test unknown command returns error."""
        monkeypatch.setattr("sys.argv", ["generate.py", "unknown"])

        result = main()
        assert result == 1

        captured = capsys.readouterr()
        assert "Unknown command: unknown" in captured.out
        assert "Available:" in captured.out

    def test_index_command(self, tmp_path, monkeypatch, capsys):
        """Test index command."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Test")

        monkeypatch.setattr("sys.argv", ["generate.py", "index"])
        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = main()
        assert result == 0
        assert (specs_dir / "index.json").exists()

    def test_search_command(self, tmp_path, monkeypatch, capsys):
        """Test search command."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Test")

        monkeypatch.setattr("sys.argv", ["generate.py", "search"])
        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = main()
        assert result == 0
        assert (specs_dir / "search.json").exists()

    def test_all_command(self, tmp_path, monkeypatch, capsys):
        """Test all command."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")
        (lang_dir / "spec.md").write_text("# Test")

        monkeypatch.setattr("sys.argv", ["generate.py", "all"])
        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = main()
        assert result == 0
        assert (specs_dir / "index.json").exists()
        assert (specs_dir / "search.json").exists()


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_excludes_underscore_dirs(self, tmp_path, monkeypatch):
        """Test that directories starting with _ are excluded."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create a normal directory
        (specs_dir / "python").mkdir()
        (specs_dir / "python" / "spec.md").write_text("# Python")

        # Create underscore directory (should be excluded)
        (specs_dir / "_templates").mkdir()
        (specs_dir / "_templates" / "template.md").write_text("# Template")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        root_index = json.loads((specs_dir / "index.json").read_text())
        languages = [l["language"] for l in root_index["languages"]]
        assert "python" in languages
        assert "_templates" not in languages

    def test_special_characters_in_content(self, tmp_path, monkeypatch):
        """Test handling of special characters in file content."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()

        content = '# Test with "quotes" and <brackets> & ampersands\n\nUnicode: \u00e9\u00e8\u00ea'
        (lang_dir / "special.md").write_text(content, encoding="utf-8")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_search()
        assert result == 0

        lang_search = json.loads((lang_dir / "search.json").read_text())
        entry = lang_search["entries"][0]
        assert entry["content"] == content

    def test_nested_linters_structure(self, tmp_path, monkeypatch):
        """Test deeply nested linters directory structure."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "javascript"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        linters_dir = lang_dir / "linters" / "eslint" / "rules"
        linters_dir.mkdir(parents=True)
        (linters_dir / "no-unused-vars.md").write_text("# no-unused-vars")
        (linters_dir / "no-console.md").write_text("# no-console")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        lang_index = json.loads((lang_dir / "index.json").read_text())
        assert lang_index["counts"]["linters"] == 2

    def test_items_contain_all_entries(self, tmp_path, monkeypatch):
        """Test that items array contains all entries from all categories."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "test"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        # Create files in multiple categories
        (lang_dir / "spec.md").write_text("# Spec")

        (lang_dir / "stdlib").mkdir()
        (lang_dir / "stdlib" / "mod.md").write_text("# Mod")

        (lang_dir / "linters").mkdir()
        (lang_dir / "linters" / "lint.md").write_text("# Lint")

        (lang_dir / "formatters").mkdir()
        (lang_dir / "formatters" / "fmt.md").write_text("# Fmt")

        (lang_dir / "patterns").mkdir()
        (lang_dir / "patterns" / "pat.md").write_text("# Pat")

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        result = cmd_index()
        assert result == 0

        lang_index = json.loads((lang_dir / "index.json").read_text())

        # items should contain all entries
        expected_total = sum(lang_index["counts"].values())
        assert len(lang_index["items"]) == expected_total
        assert expected_total == 5

    def test_generated_at_format(self, tmp_path, monkeypatch):
        """Test that generatedAt is in ISO format."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        (specs_dir / "test").mkdir()

        monkeypatch.setattr("generate.SPECS_ROOT", specs_dir)

        cmd_index()
        cmd_search()

        root_index = json.loads((specs_dir / "index.json").read_text())
        root_search = json.loads((specs_dir / "search.json").read_text())

        # Should be valid ISO format with timezone
        from datetime import datetime

        datetime.fromisoformat(root_index["generatedAt"])
        datetime.fromisoformat(root_search["generatedAt"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
