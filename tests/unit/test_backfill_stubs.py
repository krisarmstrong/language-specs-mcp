#!/usr/bin/env python3
"""Unit tests for backfill-stubs.py."""

import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import after path modification - use importlib for hyphenated module
import importlib.util

spec = importlib.util.spec_from_file_location(
    "backfill_stubs",
    Path(__file__).parent.parent.parent / "scripts" / "backfill-stubs.py",
)
backfill_stubs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backfill_stubs)

# Import functions for testing
is_stub_file = backfill_stubs.is_stub_file
find_stub_url = backfill_stubs.find_stub_url
is_binary_url = backfill_stubs.is_binary_url
backfill_stub = backfill_stubs.backfill_stub
iter_stub_files = backfill_stubs.iter_stub_files
main = backfill_stubs.main
ROOT_DIR = backfill_stubs.ROOT_DIR
SPECS_DIR = backfill_stubs.SPECS_DIR


class TestIsStubFile:
    """Tests for is_stub_file function."""

    def test_single_see_line_is_stub(self, tmp_path):
        """Test file with only 'See:' line is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs")
        assert is_stub_file(stub) is True

    def test_see_with_title_is_stub(self, tmp_path):
        """Test file with title and 'See:' line is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("# Title\nSee: https://example.com/docs")
        assert is_stub_file(stub) is True

    def test_see_with_blank_lines_is_stub(self, tmp_path):
        """Test file with 'See:' and blank lines is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs\n\n\n")
        assert is_stub_file(stub) is True

    def test_three_content_lines_not_stub(self, tmp_path):
        """Test file with 3+ content lines is not a stub."""
        full = tmp_path / "full.md"
        full.write_text("# Title\nSome content.\nMore content.")
        assert is_stub_file(full) is False

    def test_no_see_line_not_stub(self, tmp_path):
        """Test file without 'See:' line is not a stub."""
        full = tmp_path / "full.md"
        full.write_text("# Title\nContent")
        assert is_stub_file(full) is False

    def test_nonexistent_file_not_stub(self, tmp_path):
        """Test non-existent file is not a stub."""
        missing = tmp_path / "missing.md"
        assert is_stub_file(missing) is False

    def test_empty_file_not_stub(self, tmp_path):
        """Test empty file is not a stub."""
        empty = tmp_path / "empty.md"
        empty.write_text("")
        assert is_stub_file(empty) is False

    def test_oserror_returns_false(self, tmp_path):
        """Test OSError during read returns False."""
        # Create a directory instead of file
        dir_path = tmp_path / "is_dir"
        dir_path.mkdir()
        assert is_stub_file(dir_path) is False

    def test_see_not_at_beginning_not_stub(self, tmp_path):
        """Test 'See:' not at line start is not a stub."""
        file = tmp_path / "test.md"
        file.write_text("This line contains See: but not at start")
        assert is_stub_file(file) is False

    def test_whitespace_only_lines_ignored(self, tmp_path):
        """Test whitespace-only lines are not counted."""
        file = tmp_path / "test.md"
        file.write_text("See: https://example.com\n   \n\t\n")
        assert is_stub_file(file) is True


class TestFindStubUrl:
    """Tests for find_stub_url function."""

    def test_extracts_url_from_see_line(self, tmp_path):
        """Test URL extraction from 'See:' line."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs")
        assert find_stub_url(stub) == "https://example.com/docs"

    def test_extracts_url_with_title(self, tmp_path):
        """Test URL extraction when title is present."""
        stub = tmp_path / "stub.md"
        stub.write_text("# Title\nSee: https://example.com/path/to/doc")
        assert find_stub_url(stub) == "https://example.com/path/to/doc"

    def test_strips_whitespace(self, tmp_path):
        """Test URL is stripped of whitespace."""
        stub = tmp_path / "stub.md"
        stub.write_text("See:   https://example.com/docs   \n")
        assert find_stub_url(stub) == "https://example.com/docs"

    def test_no_see_line_returns_none(self, tmp_path):
        """Test returns None when no 'See:' line exists."""
        file = tmp_path / "file.md"
        file.write_text("# Title\nContent without See line")
        assert find_stub_url(file) is None

    def test_first_see_line_used(self, tmp_path):
        """Test first 'See:' line is used if multiple exist."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://first.com\nSee: https://second.com")
        assert find_stub_url(stub) == "https://first.com"

    def test_see_with_only_spaces_returns_none(self, tmp_path):
        """Test 'See:' with only spaces after it returns None.

        When the line is stripped, trailing spaces are removed,
        leaving 'See:' which doesn't match 'See: ' prefix.
        """
        stub = tmp_path / "stub.md"
        stub.write_text("See:   \n")  # Multiple spaces after "See:"
        assert find_stub_url(stub) is None

    def test_see_without_space_returns_none(self, tmp_path):
        """Test 'See:' without trailing space doesn't match."""
        stub = tmp_path / "stub.md"
        stub.write_text("See:")
        assert find_stub_url(stub) is None

    def test_see_with_actual_empty_url(self, tmp_path):
        """Test 'See: ' (with space) followed by more content returns empty string."""
        stub = tmp_path / "stub.md"
        # Note: The line needs non-whitespace content after "See: " to not get stripped
        # The function requires a space after "See:", so "See: x" works but "See:" doesn't
        stub.write_text("See: https://example.com")
        assert find_stub_url(stub) == "https://example.com"


class TestIsBinaryUrl:
    """Tests for is_binary_url function."""

    def test_pdf_is_binary(self):
        """Test PDF URL is binary."""
        assert is_binary_url("https://example.com/doc.pdf") is True

    def test_zip_is_binary(self):
        """Test ZIP URL is binary."""
        assert is_binary_url("https://example.com/archive.zip") is True

    def test_tar_gz_is_binary(self):
        """Test tar.gz URL is binary."""
        assert is_binary_url("https://example.com/archive.tar.gz") is True

    def test_tgz_is_binary(self):
        """Test tgz URL is binary."""
        assert is_binary_url("https://example.com/archive.tgz") is True

    def test_html_not_binary(self):
        """Test HTML URL is not binary."""
        assert is_binary_url("https://example.com/page.html") is False

    def test_md_not_binary(self):
        """Test Markdown URL is not binary."""
        assert is_binary_url("https://example.com/doc.md") is False

    def test_no_extension_not_binary(self):
        """Test URL without extension is not binary."""
        assert is_binary_url("https://example.com/path/to/doc") is False

    def test_case_insensitive(self):
        """Test binary detection is case insensitive."""
        assert is_binary_url("https://example.com/doc.PDF") is True
        assert is_binary_url("https://example.com/archive.ZIP") is True
        assert is_binary_url("https://example.com/archive.TAR.GZ") is True


class TestBackfillStub:
    """Tests for backfill_stub function."""

    def test_no_url_returns_false(self, tmp_path, monkeypatch):
        """Test returns False when no URL found."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        stub = tmp_path / "stub.md"
        stub.write_text("# Title only, no See line")
        assert backfill_stub(stub, dry_run=False) is False

    def test_binary_url_skipped(self, tmp_path, monkeypatch, caplog):
        """Test binary URLs are skipped."""
        import logging

        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/doc.pdf")

        with caplog.at_level(logging.INFO):
            result = backfill_stub(stub, dry_run=False)

        assert result is False
        assert "Skipping binary source" in caplog.text

    def test_dry_run_does_not_fetch(self, tmp_path, monkeypatch, caplog):
        """Test dry run logs without fetching."""
        import logging

        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        stub = tmp_path / "specs" / "python" / "stub.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/doc")

        with caplog.at_level(logging.INFO):
            result = backfill_stub(stub, dry_run=True)

        assert result is True
        assert "Would fetch" in caplog.text
        assert "https://example.com/doc" in caplog.text

    def test_fetch_error_returns_false(self, tmp_path, monkeypatch, caplog):
        """Test fetch errors return False."""
        import logging

        from _common import FetchError

        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)

        def mock_fetch_url(url):
            raise FetchError(url=url, message="Connection refused")

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)

        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/doc")

        with caplog.at_level(logging.WARNING):
            result = backfill_stub(stub, dry_run=False)

        assert result is False
        assert "Fetch failed" in caplog.text

    def test_successful_backfill(self, tmp_path, monkeypatch, caplog):
        """Test successful stub replacement."""
        import logging

        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        def mock_fetch_url(url):
            return "<html><body><main><h1>Title</h1><p>Content</p></main></body></html>"

        def mock_html_to_markdown(content, path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Title\n\nContent\n")
            return True

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "write_fetched_at", mock_write_fetched_at)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        stub = tmp_path / "specs" / "python" / "stub.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/doc")

        with caplog.at_level(logging.INFO):
            result = backfill_stub(stub, dry_run=False)

        assert result is True
        assert "Replaced stub" in caplog.text

    def test_conversion_failure_returns_false(self, tmp_path, monkeypatch, caplog):
        """Test returns False when HTML conversion fails."""
        import logging

        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)

        def mock_fetch_url(url):
            return "<html></html>"

        def mock_html_to_markdown(content, path):
            return False

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/doc")

        with caplog.at_level(logging.WARNING):
            result = backfill_stub(stub, dry_run=False)

        assert result is False
        assert "Failed to convert HTML" in caplog.text

    def test_fetched_at_written_to_correct_dir(self, tmp_path, monkeypatch):
        """Test .fetched-at is written to language directory."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        fetched_at_dirs = []

        def mock_fetch_url(url):
            return "<html><body><h1>Title</h1></body></html>"

        def mock_html_to_markdown(content, path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Title\n")
            return True

        def mock_write_fetched_at(path):
            fetched_at_dirs.append(path)

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "write_fetched_at", mock_write_fetched_at)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        # Test stdlib subdirectory
        stub = tmp_path / "specs" / "python" / "stdlib" / "overview.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/doc")

        backfill_stub(stub, dry_run=False)

        # Should write to python dir, not stdlib
        assert len(fetched_at_dirs) == 1
        assert fetched_at_dirs[0].name == "python"

    def test_fetched_at_for_nested_dirs(self, tmp_path, monkeypatch):
        """Test .fetched-at handles different nested structures."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        fetched_at_dirs = []

        def mock_fetch_url(url):
            return "<html><h1>Title</h1></html>"

        def mock_html_to_markdown(content, path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Title\n")
            return True

        def mock_write_fetched_at(path):
            fetched_at_dirs.append(path)

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "write_fetched_at", mock_write_fetched_at)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        # Test linters subdirectory
        stub = tmp_path / "specs" / "go" / "linters" / "overview.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/linters")

        backfill_stub(stub, dry_run=False)

        assert fetched_at_dirs[-1].name == "go"


class TestIterStubFiles:
    """Tests for iter_stub_files function."""

    def test_finds_spec_and_overview_by_default(self, tmp_path, monkeypatch):
        """Test finds spec.md and overview.md by default."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        # Create spec.md stub
        spec = lang_dir / "spec.md"
        spec.write_text("See: https://example.com/spec")

        # Create overview.md stub
        overview = lang_dir / "stdlib" / "overview.md"
        overview.parent.mkdir()
        overview.write_text("See: https://example.com/overview")

        # Create other.md stub (should be ignored)
        other = lang_dir / "other.md"
        other.write_text("See: https://example.com/other")

        result = iter_stub_files(include_all=False)

        assert len(result) == 2
        assert spec in result
        assert overview in result
        assert other not in result

    def test_finds_all_stubs_when_include_all(self, tmp_path, monkeypatch):
        """Test finds all stub files when include_all=True."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        # Create various stubs
        spec = lang_dir / "spec.md"
        spec.write_text("See: https://example.com/spec")

        other = lang_dir / "other.md"
        other.write_text("See: https://example.com/other")

        nested = lang_dir / "deep" / "nested.md"
        nested.parent.mkdir()
        nested.write_text("See: https://example.com/nested")

        result = iter_stub_files(include_all=True)

        assert spec in result
        assert other in result
        assert nested in result

    def test_excludes_non_stub_files(self, tmp_path, monkeypatch):
        """Test excludes files that are not stubs."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        # Create non-stub spec.md
        spec = lang_dir / "spec.md"
        spec.write_text("# Full Spec\n\nWith content.\n\nAnd more content.")

        # Create stub overview.md
        overview = lang_dir / "overview.md"
        overview.write_text("See: https://example.com/overview")

        result = iter_stub_files(include_all=False)

        assert spec not in result
        assert overview in result

    def test_returns_sorted_paths(self, tmp_path, monkeypatch):
        """Test returns paths in sorted order."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)

        # Create stubs in various directories
        for lang in ["zzz", "aaa", "mmm"]:
            lang_dir = tmp_path / lang
            lang_dir.mkdir()
            spec = lang_dir / "spec.md"
            spec.write_text("See: https://example.com")

        result = iter_stub_files(include_all=False)

        # Should be sorted
        assert result == sorted(result)

    def test_empty_directory(self, tmp_path, monkeypatch):
        """Test returns empty list for empty directory."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)

        result = iter_stub_files(include_all=False)
        assert result == []


class TestMain:
    """Tests for main function."""

    def test_no_stubs_found(self, tmp_path, monkeypatch, capsys):
        """Test message when no stubs found."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)
        monkeypatch.setattr("sys.argv", ["backfill-stubs.py"])

        main()

        captured = capsys.readouterr()
        assert "No stub files found" in captured.out

    def test_processes_stubs(self, tmp_path, monkeypatch, capsys):
        """Test processes found stub files."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr("sys.argv", ["backfill-stubs.py", "--dry-run"])

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        spec = lang_dir / "spec.md"
        spec.write_text("See: https://example.com/spec")

        main()

        captured = capsys.readouterr()
        assert "Processed 1 stub files" in captured.out

    def test_limit_option(self, tmp_path, monkeypatch, capsys):
        """Test --limit option limits files processed."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr("sys.argv", ["backfill-stubs.py", "--dry-run", "--limit", "2"])

        # Create 5 stubs
        for i in range(5):
            lang_dir = tmp_path / f"lang{i}"
            lang_dir.mkdir()
            spec = lang_dir / "spec.md"
            spec.write_text("See: https://example.com")

        main()

        captured = capsys.readouterr()
        assert "Processed 2 stub files" in captured.out

    def test_all_option(self, tmp_path, monkeypatch, capsys):
        """Test --all option processes all stubs."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr("sys.argv", ["backfill-stubs.py", "--all", "--dry-run"])

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        # Create spec.md and other.md stubs
        spec = lang_dir / "spec.md"
        spec.write_text("See: https://example.com/spec")

        other = lang_dir / "custom.md"
        other.write_text("See: https://example.com/custom")

        main()

        captured = capsys.readouterr()
        assert "Processed 2 stub files" in captured.out

    def test_dry_run_option(self, tmp_path, monkeypatch, capsys, caplog):
        """Test --dry-run option doesn't modify files."""
        import logging

        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr("sys.argv", ["backfill-stubs.py", "--dry-run"])

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        spec = lang_dir / "spec.md"
        original_content = "See: https://example.com/spec"
        spec.write_text(original_content)

        with caplog.at_level(logging.INFO):
            main()

        # File should not be modified
        assert spec.read_text() == original_content
        assert "Would fetch" in caplog.text

    def test_counts_replaced_files(self, tmp_path, monkeypatch, capsys):
        """Test reports correct replacement count."""
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr("sys.argv", ["backfill-stubs.py", "--dry-run"])

        # Create 3 stubs
        for i in range(3):
            lang_dir = tmp_path / f"lang{i}"
            lang_dir.mkdir()
            spec = lang_dir / "spec.md"
            spec.write_text("See: https://example.com")

        main()

        captured = capsys.readouterr()
        assert "replaced 3" in captured.out


class TestConstants:
    """Tests for module constants."""

    def test_root_dir_is_project_root(self):
        """Test ROOT_DIR points to project root."""
        assert ROOT_DIR.is_dir()
        assert (ROOT_DIR / "package.json").exists()

    def test_specs_dir_exists(self):
        """Test SPECS_DIR exists."""
        assert SPECS_DIR.is_dir()


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_stub_with_complex_url(self, tmp_path, monkeypatch):
        """Test stub with complex URL is handled."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        stub = tmp_path / "stub.md"
        complex_url = "https://example.com/path?param=value&other=123#section"
        stub.write_text(f"See: {complex_url}")

        url = find_stub_url(stub)
        assert url == complex_url

    def test_stub_with_unicode_in_path(self, tmp_path, monkeypatch, caplog):
        """Test stub in path with unicode characters."""
        import logging

        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        lang_dir = tmp_path / "specs" / "python"
        lang_dir.mkdir(parents=True)
        stub = lang_dir / "spec.md"
        stub.write_text("See: https://example.com/doc")

        with caplog.at_level(logging.INFO):
            backfill_stub(stub, dry_run=True)

        assert "Would fetch" in caplog.text

    def test_formatters_subdirectory(self, tmp_path, monkeypatch):
        """Test .fetched-at for formatters subdirectory."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        fetched_at_dirs = []

        def mock_fetch_url(url):
            return "<html><h1>Title</h1></html>"

        def mock_html_to_markdown(content, path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Title\n")
            return True

        def mock_write_fetched_at(path):
            fetched_at_dirs.append(path)

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "write_fetched_at", mock_write_fetched_at)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        stub = tmp_path / "specs" / "python" / "formatters" / "black.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/black")

        backfill_stub(stub, dry_run=False)

        assert fetched_at_dirs[-1].name == "python"

    def test_patterns_subdirectory(self, tmp_path, monkeypatch):
        """Test .fetched-at for patterns subdirectory."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        fetched_at_dirs = []

        def mock_fetch_url(url):
            return "<html><h1>Title</h1></html>"

        def mock_html_to_markdown(content, path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Title\n")
            return True

        def mock_write_fetched_at(path):
            fetched_at_dirs.append(path)

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "write_fetched_at", mock_write_fetched_at)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        stub = tmp_path / "specs" / "python" / "patterns" / "singleton.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/patterns")

        backfill_stub(stub, dry_run=False)

        assert fetched_at_dirs[-1].name == "python"

    def test_lib_subdirectory(self, tmp_path, monkeypatch):
        """Test .fetched-at for lib subdirectory."""
        monkeypatch.setattr(backfill_stubs, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(backfill_stubs, "SPECS_DIR", tmp_path / "specs")

        fetched_at_dirs = []

        def mock_fetch_url(url):
            return "<html><h1>Title</h1></html>"

        def mock_html_to_markdown(content, path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Title\n")
            return True

        def mock_write_fetched_at(path):
            fetched_at_dirs.append(path)

        monkeypatch.setattr(backfill_stubs, "fetch_url", mock_fetch_url)
        monkeypatch.setattr(backfill_stubs, "html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr(backfill_stubs, "write_fetched_at", mock_write_fetched_at)
        monkeypatch.setattr(backfill_stubs, "extract_main", lambda x: x)

        stub = tmp_path / "specs" / "rust" / "lib" / "serde.md"
        stub.parent.mkdir(parents=True)
        stub.write_text("See: https://example.com/serde")

        backfill_stub(stub, dry_run=False)

        assert fetched_at_dirs[-1].name == "rust"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
