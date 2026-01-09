#!/usr/bin/env python3
"""Unit tests for generate-health.py."""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

# Add scripts directory to path
SCRIPTS_DIR = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

# Load generate-health module with hyphenated name
spec = importlib.util.spec_from_file_location("generate_health", SCRIPTS_DIR / "generate-health.py")
generate_health = importlib.util.module_from_spec(spec)
sys.modules["generate_health"] = generate_health
spec.loader.exec_module(generate_health)


class TestLoadTools:
    """Tests for load_tools function."""

    def test_returns_empty_dict_when_file_missing(self, tmp_path, monkeypatch):
        """Test returns empty dict when versions.json doesn't exist."""
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tmp_path / "nonexistent.json")

        result = generate_health.load_tools()
        assert result == {}

    def test_loads_tools_by_name(self, tmp_path, monkeypatch):
        """Test tools are indexed by name."""
        tools_file = tmp_path / "versions.json"
        tools_data = {
            "tools": [
                {"name": "python", "version": "3.12.0"},
                {"name": "go", "version": "1.21.0"},
            ]
        }
        tools_file.write_text(json.dumps(tools_data))
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_file)

        result = generate_health.load_tools()
        assert "python" in result
        assert result["python"]["version"] == "3.12.0"
        assert "go" in result
        assert result["go"]["version"] == "1.21.0"

    def test_handles_empty_tools_list(self, tmp_path, monkeypatch):
        """Test handles empty tools list."""
        tools_file = tmp_path / "versions.json"
        tools_file.write_text(json.dumps({"tools": []}))
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_file)

        result = generate_health.load_tools()
        assert result == {}

    def test_handles_missing_tools_key(self, tmp_path, monkeypatch):
        """Test handles JSON without tools key."""
        tools_file = tmp_path / "versions.json"
        tools_file.write_text(json.dumps({"other": "data"}))
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_file)

        result = generate_health.load_tools()
        assert result == {}


class TestLoadSearchSummary:
    """Tests for load_search_summary function."""

    def test_returns_none_and_empty_when_file_missing(self, tmp_path, monkeypatch):
        """Test returns (None, {}) when search.json doesn't exist."""
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", tmp_path / "nonexistent.json")

        generated_at, counts = generate_health.load_search_summary()
        assert generated_at is None
        assert counts == {}

    def test_loads_search_summary(self, tmp_path, monkeypatch):
        """Test loads search summary correctly."""
        search_file = tmp_path / "search.json"
        search_data = {
            "generatedAt": "2024-01-15T10:30:00Z",
            "languages": [
                {"language": "python", "count": 150},
                {"language": "go", "count": 75},
            ],
        }
        search_file.write_text(json.dumps(search_data))
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", search_file)

        generated_at, counts = generate_health.load_search_summary()
        assert generated_at == "2024-01-15T10:30:00Z"
        assert counts["python"] == 150
        assert counts["go"] == 75

    def test_handles_missing_generated_at(self, tmp_path, monkeypatch):
        """Test handles missing generatedAt field."""
        search_file = tmp_path / "search.json"
        search_data = {"languages": [{"language": "python", "count": 100}]}
        search_file.write_text(json.dumps(search_data))
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", search_file)

        generated_at, counts = generate_health.load_search_summary()
        assert generated_at is None
        assert counts["python"] == 100

    def test_handles_empty_languages(self, tmp_path, monkeypatch):
        """Test handles empty languages list."""
        search_file = tmp_path / "search.json"
        search_data = {"generatedAt": "2024-01-15T10:30:00Z", "languages": []}
        search_file.write_text(json.dumps(search_data))
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", search_file)

        generated_at, counts = generate_health.load_search_summary()
        assert generated_at == "2024-01-15T10:30:00Z"
        assert counts == {}


class TestLoadUrlStatus:
    """Tests for load_url_status function."""

    def test_returns_empty_dict_when_file_missing(self, tmp_path, monkeypatch):
        """Test returns empty dict when url-status.json doesn't exist."""
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", tmp_path / "nonexistent.json")

        result = generate_health.load_url_status()
        assert result == {}

    def test_loads_url_status(self, tmp_path, monkeypatch):
        """Test loads URL status correctly."""
        url_file = tmp_path / "url-status.json"
        url_data = {
            "generatedAt": "2024-01-15T10:30:00Z",
            "summary": {"total": 100, "ok": 95, "error": 5},
            "errorsByLanguage": {"python": ["http://broken.com"]},
        }
        url_file.write_text(json.dumps(url_data))
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", url_file)

        result = generate_health.load_url_status()
        assert result["generatedAt"] == "2024-01-15T10:30:00Z"
        assert result["summary"]["ok"] == 95

    def test_handles_invalid_json(self, tmp_path, monkeypatch):
        """Test handles invalid JSON gracefully."""
        url_file = tmp_path / "url-status.json"
        url_file.write_text("not valid json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", url_file)

        result = generate_health.load_url_status()
        assert result == {}

    def test_handles_os_error(self, tmp_path, monkeypatch):
        """Test handles OSError gracefully."""
        # Create a directory with the same name to trigger OSError
        url_file = tmp_path / "url-status.json"
        url_file.mkdir()
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", url_file)

        result = generate_health.load_url_status()
        assert result == {}


class TestReadFetchedAt:
    """Tests for read_fetched_at function."""

    def test_returns_none_when_file_missing(self, tmp_path):
        """Test returns None when .fetched-at doesn't exist."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        result = generate_health.read_fetched_at(lang_dir)
        assert result is None

    def test_reads_valid_timestamp(self, tmp_path):
        """Test reads valid ISO timestamp."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())

        result = generate_health.read_fetched_at(lang_dir)
        assert result is not None
        assert result.year == now.year
        assert result.month == now.month

    def test_returns_none_for_invalid_format(self, tmp_path):
        """Test returns None for invalid timestamp format."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("not-a-date")

        result = generate_health.read_fetched_at(lang_dir)
        assert result is None

    def test_strips_whitespace(self, tmp_path):
        """Test strips whitespace from timestamp."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(f"  {now.isoformat()}  \n")

        result = generate_health.read_fetched_at(lang_dir)
        assert result is not None


class TestCountMarkdownFiles:
    """Tests for count_markdown_files function."""

    def test_returns_zero_for_missing_directory(self, tmp_path):
        """Test returns 0 for non-existent directory."""
        result = generate_health.count_markdown_files(tmp_path / "nonexistent")
        assert result == 0

    def test_counts_markdown_files(self, tmp_path):
        """Test counts .md files correctly."""
        (tmp_path / "file1.md").write_text("# Doc 1")
        (tmp_path / "file2.md").write_text("# Doc 2")
        (tmp_path / "file3.txt").write_text("Not markdown")

        result = generate_health.count_markdown_files(tmp_path)
        assert result == 2

    def test_counts_nested_files(self, tmp_path):
        """Test counts files in nested directories."""
        nested = tmp_path / "subdir" / "deep"
        nested.mkdir(parents=True)
        (tmp_path / "root.md").write_text("# Root")
        (nested / "nested.md").write_text("# Nested")

        result = generate_health.count_markdown_files(tmp_path)
        assert result == 2

    def test_empty_directory_returns_zero(self, tmp_path):
        """Test empty directory returns 0."""
        result = generate_health.count_markdown_files(tmp_path)
        assert result == 0

    def test_ignores_non_files(self, tmp_path):
        """Test ignores directories ending in .md."""
        # Create a directory with .md extension (unusual but possible)
        fake_md_dir = tmp_path / "folder.md"
        fake_md_dir.mkdir()
        (fake_md_dir / "actual.md").write_text("# Actual file")

        # Should only count the actual file, not the directory
        result = generate_health.count_markdown_files(tmp_path)
        assert result == 1


class TestIsStubFile:
    """Tests for is_stub_file function."""

    def test_single_see_line_is_stub(self, tmp_path):
        """Test file with single 'See:' line is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs")
        assert generate_health.is_stub_file(stub) is True

    def test_two_lines_with_see_is_stub(self, tmp_path):
        """Test file with title and See: is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("# Title\nSee: https://example.com/docs")
        assert generate_health.is_stub_file(stub) is True

    def test_more_than_two_lines_not_stub(self, tmp_path):
        """Test file with more than 2 content lines is not a stub."""
        full = tmp_path / "full.md"
        full.write_text("# Title\n\nContent here.\n\nMore content.")
        assert generate_health.is_stub_file(full) is False

    def test_no_see_line_not_stub(self, tmp_path):
        """Test file without See: is not a stub."""
        full = tmp_path / "full.md"
        full.write_text("# Title\nContent")
        assert generate_health.is_stub_file(full) is False

    def test_nonexistent_file_not_stub(self, tmp_path):
        """Test nonexistent file is not a stub."""
        missing = tmp_path / "missing.md"
        assert generate_health.is_stub_file(missing) is False

    def test_empty_file_not_stub(self, tmp_path):
        """Test empty file is not a stub."""
        empty = tmp_path / "empty.md"
        empty.write_text("")
        assert generate_health.is_stub_file(empty) is False

    def test_whitespace_only_lines_ignored(self, tmp_path):
        """Test whitespace-only lines don't count."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com\n   \n\t\n")
        assert generate_health.is_stub_file(stub) is True

    def test_read_error_returns_false(self, tmp_path, monkeypatch):
        """Test OSError during read returns False."""
        file = tmp_path / "file.md"
        file.write_text("See: https://example.com")

        # Make the file unreadable by mocking read_text
        original_read_text = Path.read_text

        def mock_read_text(self, *args, **kwargs):
            if self.name == "file.md":
                raise OSError("Permission denied")
            return original_read_text(self, *args, **kwargs)

        monkeypatch.setattr(Path, "read_text", mock_read_text)
        assert generate_health.is_stub_file(file) is False


class TestListSubdirs:
    """Tests for list_subdirs function."""

    def test_returns_empty_for_missing_directory(self, tmp_path):
        """Test returns empty tuple for non-existent directory."""
        result = generate_health.list_subdirs(tmp_path / "nonexistent")
        assert result == ()

    def test_returns_sorted_subdirectories(self, tmp_path):
        """Test returns sorted list of subdirectories."""
        (tmp_path / "zebra").mkdir()
        (tmp_path / "alpha").mkdir()
        (tmp_path / "middle").mkdir()
        (tmp_path / "file.txt").write_text("Not a dir")

        result = list(generate_health.list_subdirs(tmp_path))
        names = [p.name for p in result]
        assert names == ["alpha", "middle", "zebra"]

    def test_excludes_files(self, tmp_path):
        """Test only includes directories, not files."""
        (tmp_path / "dir1").mkdir()
        (tmp_path / "file.md").write_text("File")

        result = list(generate_health.list_subdirs(tmp_path))
        assert len(result) == 1
        assert result[0].name == "dir1"


class TestGatherCategoryData:
    """Tests for gather_category_data function."""

    def test_spec_category_exists(self, tmp_path, monkeypatch):
        """Test spec category when spec.md exists."""
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        lang_dir = tmp_path / "specs" / "python"
        lang_dir.mkdir(parents=True)
        (lang_dir / "spec.md").write_text("# Spec")

        result = generate_health.gather_category_data(lang_dir, "spec")
        assert result["count"] == 1
        assert result["missing"] is False
        assert "spec.md" in result["path"]

    def test_spec_category_missing(self, tmp_path, monkeypatch):
        """Test spec category when spec.md is missing."""
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        lang_dir = tmp_path / "specs" / "python"
        lang_dir.mkdir(parents=True)

        result = generate_health.gather_category_data(lang_dir, "spec")
        assert result["count"] == 0
        assert result["missing"] is True
        assert result["path"] == ""

    def test_stdlib_category(self, tmp_path, monkeypatch):
        """Test stdlib category counts."""
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        lang_dir = tmp_path / "specs" / "python"
        stdlib = lang_dir / "stdlib"
        stdlib.mkdir(parents=True)
        (stdlib / "os.md").write_text("# os")
        (stdlib / "sys.md").write_text("# sys")

        result = generate_health.gather_category_data(lang_dir, "stdlib")
        assert result["count"] == 2
        assert result["missing"] is False

    def test_missing_category_directory(self, tmp_path, monkeypatch):
        """Test category when directory doesn't exist."""
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        lang_dir = tmp_path / "specs" / "python"
        lang_dir.mkdir(parents=True)

        result = generate_health.gather_category_data(lang_dir, "patterns")
        assert result["count"] == 0
        assert result["missing"] is True


class TestGatherLinters:
    """Tests for gather_linters function."""

    def test_no_linters_directory(self, tmp_path):
        """Test when linters directory doesn't exist."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        result = generate_health.gather_linters(lang_dir)
        assert result == []

    def test_multiple_linters(self, tmp_path):
        """Test gathering multiple linters."""
        lang_dir = tmp_path / "python"
        linters = lang_dir / "linters"
        linters.mkdir(parents=True)

        pylint = linters / "pylint"
        pylint.mkdir()
        (pylint / "rule1.md").write_text("# Rule 1")
        (pylint / "rule2.md").write_text("# Rule 2")

        mypy = linters / "mypy"
        mypy.mkdir()
        (mypy / "error1.md").write_text("# Error 1")

        result = generate_health.gather_linters(lang_dir)
        assert len(result) == 2

        # Sort for consistent assertion
        by_name = {r["name"]: r for r in result}
        assert by_name["pylint"]["count"] == 2
        assert by_name["mypy"]["count"] == 1

    def test_empty_linter_directory(self, tmp_path):
        """Test linter directory with no markdown files."""
        lang_dir = tmp_path / "python"
        linters = lang_dir / "linters"
        empty_linter = linters / "empty"
        empty_linter.mkdir(parents=True)

        result = generate_health.gather_linters(lang_dir)
        assert len(result) == 1
        assert result[0]["name"] == "empty"
        assert result[0]["count"] == 0


class TestGatherFormatters:
    """Tests for gather_formatters function."""

    def test_no_formatters_directory(self, tmp_path):
        """Test when formatters directory doesn't exist."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        result = generate_health.gather_formatters(lang_dir)
        assert result == []

    def test_multiple_formatters(self, tmp_path):
        """Test gathering multiple formatters."""
        lang_dir = tmp_path / "python"
        formatters = lang_dir / "formatters"
        formatters.mkdir(parents=True)

        black = formatters / "black"
        black.mkdir()
        (black / "config.md").write_text("# Config")

        autopep8 = formatters / "autopep8"
        autopep8.mkdir()

        result = generate_health.gather_formatters(lang_dir)
        assert len(result) == 2


class TestBuildLanguageRecord:
    """Tests for build_language_record function."""

    def test_basic_language_record(self, tmp_path, monkeypatch):
        """Test building a basic language record."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        # Create fetched-at timestamp
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())

        # Create spec.md
        (lang_dir / "spec.md").write_text("# Python Spec")

        tools = {}
        url_status = {}

        record = generate_health.build_language_record("python", tools, url_status)

        assert record["language"] == "python"
        assert record["fetchedAt"] is not None
        assert record["freshnessDays"] is not None
        assert record["spec"]["count"] == 1
        assert record["spec"]["missing"] is False

    def test_language_with_stale_data(self, tmp_path, monkeypatch):
        """Test language record with stale data adds note."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        # Create old timestamp (60 days ago)
        old = datetime.now(UTC) - timedelta(days=60)
        (lang_dir / ".fetched-at").write_text(old.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        record = generate_health.build_language_record("python", {}, {})

        assert record["freshnessDays"] >= 60
        assert any("older than 30 days" in note for note in record["notes"])

    def test_language_without_fetched_at(self, tmp_path, monkeypatch):
        """Test language record without .fetched-at adds note."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        (lang_dir / "spec.md").write_text("# Spec")

        record = generate_health.build_language_record("python", {}, {})

        assert record["fetchedAt"] is None
        assert record["freshnessDays"] is None
        assert any("No fetched-at" in note for note in record["notes"])

    def test_language_without_spec(self, tmp_path, monkeypatch):
        """Test language record without spec.md adds note."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())

        record = generate_health.build_language_record("python", {}, {})

        assert record["spec"]["missing"] is True
        assert any("Spec document missing" in note for note in record["notes"])

    def test_language_with_tool_version(self, tmp_path, monkeypatch):
        """Test language record with tool version info."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        tools = {
            "python": {
                "version": "3.12.0",
                "checkedAt": "2024-01-15T10:00:00Z",
                "sources": ["https://python.org"],
            }
        }

        record = generate_health.build_language_record("python", tools, {})

        assert record["toolsVersion"] == "3.12.0"
        assert record["toolCheckedAt"] == "2024-01-15T10:00:00Z"
        assert record["toolSources"] == ["https://python.org"]

    def test_language_with_stub_files(self, tmp_path, monkeypatch):
        """Test language record counts stub files."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "stub1.md").write_text("See: https://example.com")
        (lang_dir / "stub2.md").write_text("# Title\nSee: https://example.com")

        record = generate_health.build_language_record("python", {}, {})

        assert record["stubCount"] == 2
        assert any("stub documents" in note for note in record["notes"])

    def test_language_with_url_errors(self, tmp_path, monkeypatch):
        """Test language record with URL validation errors."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        url_status = {
            "errorsByLanguage": {
                "python": [
                    {"url": "http://broken1.com"},
                    {"url": "http://broken2.com"},
                ]
            },
            "redirectsByLanguage": {"python": [{"url": "http://redirect.com"}]},
        }

        record = generate_health.build_language_record("python", {}, url_status)

        assert record["urlStatus"]["errors"] == 2
        assert record["urlStatus"]["redirects"] == 1
        assert record["urlStatus"]["status"] == "degraded"
        assert any("URL validation errors" in note for note in record["notes"])
        assert any("URLs with redirects" in note for note in record["notes"])

    def test_url_status_critical(self, tmp_path, monkeypatch):
        """Test URL status becomes critical with many errors."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        url_status = {
            "errorsByLanguage": {
                "python": [
                    {"url": "http://broken1.com"},
                    {"url": "http://broken2.com"},
                    {"url": "http://broken3.com"},
                ]
            },
            "redirectsByLanguage": {},
        }

        record = generate_health.build_language_record("python", {}, url_status)

        assert record["urlStatus"]["status"] == "critical"

    def test_url_errors_and_redirects_limited(self, tmp_path, monkeypatch):
        """Test URL errors and redirects are limited to 5."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        # Create 10 errors and 10 redirects
        url_status = {
            "errorsByLanguage": {"python": [{"url": f"http://broken{i}.com"} for i in range(10)]},
            "redirectsByLanguage": {
                "python": [{"url": f"http://redirect{i}.com"} for i in range(10)]
            },
        }

        record = generate_health.build_language_record("python", {}, url_status)

        assert len(record["urlErrors"]) == 5
        assert len(record["urlRedirects"]) == 5


class TestMain:
    """Tests for main function."""

    def test_generates_health_json(self, tmp_path, monkeypatch):
        """Test main generates health.json file."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        # Create language directories
        for lang in ["python", "go"]:
            lang_dir = specs_dir / lang
            lang_dir.mkdir()
            now = datetime.now(UTC)
            (lang_dir / ".fetched-at").write_text(now.isoformat())
            (lang_dir / "spec.md").write_text(f"# {lang} Spec")

        # Create empty tools and search files
        (tools_dir / "versions.json").write_text(json.dumps({"tools": []}))
        (specs_dir / "search.json").write_text(json.dumps({"languages": []}))

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", tmp_path / "url-status.json")
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        generate_health.main()

        # Check output file exists
        output_file = output_dir / "health.json"
        assert output_file.exists()

        # Parse and verify content
        data = json.loads(output_file.read_text())
        assert "generatedAt" in data
        assert data["totalLanguages"] == 2
        assert len(data["languages"]) == 2

    def test_skips_hidden_directories(self, tmp_path, monkeypatch):
        """Test main skips directories starting with dot."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        # Create hidden and visible directories
        (specs_dir / ".hidden").mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        (tools_dir / "versions.json").write_text(json.dumps({"tools": []}))
        (specs_dir / "search.json").write_text(json.dumps({"languages": []}))

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", tmp_path / "url-status.json")
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        generate_health.main()

        output_file = output_dir / "health.json"
        data = json.loads(output_file.read_text())
        assert data["totalLanguages"] == 1

        # Verify hidden directory is not included
        languages = [r["language"] for r in data["languages"]]
        assert ".hidden" not in languages
        assert "python" in languages

    def test_adds_missing_search_index_note(self, tmp_path, monkeypatch):
        """Test adds note when search index is missing for language."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        lang_dir = specs_dir / "python"
        lang_dir.mkdir()
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        (tools_dir / "versions.json").write_text(json.dumps({"tools": []}))
        # Search summary with no python entry
        (specs_dir / "search.json").write_text(
            json.dumps({"languages": [{"language": "go", "count": 50}]})
        )

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", tmp_path / "url-status.json")
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        generate_health.main()

        output_file = output_dir / "health.json"
        data = json.loads(output_file.read_text())

        python_record = next(r for r in data["languages"] if r["language"] == "python")
        assert python_record["searchIndexCount"] is None
        assert any("Search index missing" in note for note in python_record["notes"])

    def test_includes_url_summary(self, tmp_path, monkeypatch):
        """Test includes URL summary in output."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        lang_dir = specs_dir / "python"
        lang_dir.mkdir()
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        (tools_dir / "versions.json").write_text(json.dumps({"tools": []}))
        (specs_dir / "search.json").write_text(json.dumps({"languages": []}))

        # Create URL status file
        url_status_file = tmp_path / "url-status.json"
        url_status = {
            "generatedAt": "2024-01-15T10:00:00Z",
            "summary": {
                "total": 100,
                "ok": 90,
                "redirect": 5,
                "error": 3,
                "timeout": 2,
            },
        }
        url_status_file.write_text(json.dumps(url_status))

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", url_status_file)
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        generate_health.main()

        output_file = output_dir / "health.json"
        data = json.loads(output_file.read_text())

        assert data["urlValidatedAt"] == "2024-01-15T10:00:00Z"
        assert data["urlSummary"]["total"] == 100
        assert data["urlSummary"]["ok"] == 90
        assert data["urlSummary"]["redirects"] == 5
        assert data["urlSummary"]["errors"] == 3
        assert data["urlSummary"]["timeouts"] == 2

    def test_creates_output_directory(self, tmp_path, monkeypatch):
        """Test creates output directory if missing."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site" / "nested"
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        lang_dir = specs_dir / "python"
        lang_dir.mkdir()
        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        (tools_dir / "versions.json").write_text(json.dumps({"tools": []}))
        (specs_dir / "search.json").write_text(json.dumps({"languages": []}))

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", tmp_path / "url-status.json")
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        # Directory doesn't exist yet
        assert not output_dir.exists()

        generate_health.main()

        # Directory should be created
        assert output_dir.exists()
        assert (output_dir / "health.json").exists()


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_empty_specs_directory(self, tmp_path, monkeypatch, capsys):
        """Test with empty specs directory."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        (tools_dir / "versions.json").write_text(json.dumps({"tools": []}))
        (specs_dir / "search.json").write_text(json.dumps({"languages": []}))

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", tmp_path / "url-status.json")
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        generate_health.main()

        output_file = output_dir / "health.json"
        data = json.loads(output_file.read_text())
        assert data["totalLanguages"] == 0
        assert data["languages"] == []

    def test_language_with_all_categories(self, tmp_path, monkeypatch):
        """Test language with all category types."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        # stdlib
        stdlib = lang_dir / "stdlib"
        stdlib.mkdir()
        (stdlib / "os.md").write_text("# os")

        # linters
        linters = lang_dir / "linters" / "pylint"
        linters.mkdir(parents=True)
        (linters / "rule.md").write_text("# Rule")

        # formatters
        formatters = lang_dir / "formatters" / "black"
        formatters.mkdir(parents=True)
        (formatters / "config.md").write_text("# Config")

        # patterns
        patterns = lang_dir / "patterns"
        patterns.mkdir()
        (patterns / "singleton.md").write_text("# Singleton")

        record = generate_health.build_language_record("python", {}, {})

        assert record["spec"]["count"] == 1
        assert record["stdlib"]["count"] == 1
        assert len(record["linters"]) == 1
        assert len(record["formatters"]) == 1
        assert record["patterns"]["count"] == 1

    def test_freshness_boundary_30_days(self, tmp_path, monkeypatch):
        """Test freshness at exactly 30 days boundary."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        # Exactly 30 days ago
        exactly_30 = datetime.now(UTC) - timedelta(days=30)
        (lang_dir / ".fetched-at").write_text(exactly_30.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        record = generate_health.build_language_record("python", {}, {})

        # 30 days should trigger the warning (> 30 days threshold)
        assert record["freshnessDays"] >= 30

    def test_freshness_just_under_31_days(self, tmp_path, monkeypatch):
        """Test freshness at 31 days triggers warning."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        # 31 days ago
        old = datetime.now(UTC) - timedelta(days=31)
        (lang_dir / ".fetched-at").write_text(old.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        record = generate_health.build_language_record("python", {}, {})

        assert any("older than 30 days" in note for note in record["notes"])

    def test_url_status_ok_when_no_errors(self, tmp_path, monkeypatch):
        """Test URL status is 'ok' when no errors."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)

        now = datetime.now(UTC)
        (lang_dir / ".fetched-at").write_text(now.isoformat())
        (lang_dir / "spec.md").write_text("# Spec")

        url_status = {"errorsByLanguage": {}, "redirectsByLanguage": {}}

        record = generate_health.build_language_record("python", {}, url_status)

        assert record["urlStatus"]["status"] == "ok"
        assert record["urlStatus"]["errors"] == 0
        assert record["urlStatus"]["redirects"] == 0


class TestIntegration:
    """Integration tests for generate-health.py."""

    def test_full_workflow(self, tmp_path, monkeypatch, capsys):
        """Test complete health generation workflow."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        # Create multiple languages with various states
        now = datetime.now(UTC)

        # Python - complete with tools
        python_dir = specs_dir / "python"
        python_dir.mkdir()
        (python_dir / ".fetched-at").write_text(now.isoformat())
        (python_dir / "spec.md").write_text("# Python Spec")
        python_stdlib = python_dir / "stdlib"
        python_stdlib.mkdir()
        (python_stdlib / "os.md").write_text("# os module")
        python_linters = python_dir / "linters" / "pylint"
        python_linters.mkdir(parents=True)
        (python_linters / "E0001.md").write_text("# E0001")

        # Go - stale data
        go_dir = specs_dir / "go"
        go_dir.mkdir()
        old = now - timedelta(days=60)
        (go_dir / ".fetched-at").write_text(old.isoformat())
        (go_dir / "spec.md").write_text("# Go Spec")

        # Rust - missing spec
        rust_dir = specs_dir / "rust"
        rust_dir.mkdir()
        (rust_dir / ".fetched-at").write_text(now.isoformat())

        # Setup tools
        tools_data = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "checkedAt": "2024-01-15T10:00:00Z",
                    "sources": ["https://python.org"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(tools_data))

        # Setup search summary
        search_data = {
            "generatedAt": "2024-01-15T10:30:00Z",
            "languages": [
                {"language": "python", "count": 150},
                {"language": "go", "count": 75},
            ],
        }
        (specs_dir / "search.json").write_text(json.dumps(search_data))

        # Setup URL status
        url_status_data = {
            "generatedAt": "2024-01-15T11:00:00Z",
            "summary": {"total": 50, "ok": 45, "redirect": 3, "error": 2, "timeout": 0},
            "errorsByLanguage": {"go": [{"url": "http://broken.com"}]},
            "redirectsByLanguage": {},
        }
        url_status_file = tmp_path / "url-status.json"
        url_status_file.write_text(json.dumps(url_status_data))

        monkeypatch.setattr(generate_health, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(generate_health, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(generate_health, "TOOLS_JSON", tools_dir / "versions.json")
        monkeypatch.setattr(generate_health, "SEARCH_SUMMARY", specs_dir / "search.json")
        monkeypatch.setattr(generate_health, "URL_STATUS_FILE", url_status_file)
        monkeypatch.setattr(generate_health, "OUTPUT_FILE", output_dir / "health.json")

        generate_health.main()

        output_file = output_dir / "health.json"
        data = json.loads(output_file.read_text())

        # Verify structure
        assert data["totalLanguages"] == 3
        assert "generatedAt" in data
        assert data["searchIndexGeneratedAt"] == "2024-01-15T10:30:00Z"
        assert data["urlValidatedAt"] == "2024-01-15T11:00:00Z"

        # Find each language record
        by_lang = {r["language"]: r for r in data["languages"]}

        # Python should be complete
        python_rec = by_lang["python"]
        assert python_rec["toolsVersion"] == "3.12.0"
        assert python_rec["searchIndexCount"] == 150
        assert python_rec["spec"]["missing"] is False
        assert python_rec["stdlib"]["count"] == 1
        assert len(python_rec["linters"]) == 1

        # Go should be stale
        go_rec = by_lang["go"]
        assert any("older than 30 days" in note for note in go_rec["notes"])
        assert go_rec["searchIndexCount"] == 75
        assert go_rec["urlStatus"]["errors"] == 1

        # Rust should have missing spec and search index
        rust_rec = by_lang["rust"]
        assert rust_rec["spec"]["missing"] is True
        assert any("Spec document missing" in note for note in rust_rec["notes"])
        assert rust_rec["searchIndexCount"] is None
        assert any("Search index missing" in note for note in rust_rec["notes"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
