#!/usr/bin/env python3
"""Unit tests for fetch.py."""

import json
import sys
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetch import (
    FetchResult,
    LanguageResult,
    fetch_file,
    fetch_language,
    get_languages,
    is_stale,
    load_sources,
    main,
    rate_limit,
)


class TestLoadSources:
    """Tests for load_sources function."""

    def test_loads_existing_sources(self, tmp_path, monkeypatch):
        """Test loading sources.json from a language directory."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        # Create a sources.json
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources_file = lang_dir / "sources.json"
        sources_file.write_text('{"language": "python", "files": [{"path": "spec.md"}]}')

        result = load_sources("python")
        assert result["language"] == "python"
        assert len(result["files"]) == 1

    def test_returns_empty_for_missing(self, tmp_path, monkeypatch):
        """Test that missing sources.json returns empty structure."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        result = load_sources("nonexistent")
        assert result["language"] == "nonexistent"
        assert result["files"] == []


class TestIsStale:
    """Tests for is_stale function."""

    def test_missing_fetched_at_is_stale(self, tmp_path, monkeypatch):
        """Test that missing .fetched-at means stale."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        assert is_stale("python") is True

    def test_recent_fetched_at_not_stale(self, tmp_path, monkeypatch):
        """Test that recent .fetched-at is not stale."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "STALE_DAYS", 30)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"
        recent = datetime.now(UTC).isoformat()
        fetched_at.write_text(recent)

        assert is_stale("python") is False

    def test_old_fetched_at_is_stale(self, tmp_path, monkeypatch):
        """Test that old .fetched-at is stale."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "STALE_DAYS", 30)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"
        old = (datetime.now(UTC) - timedelta(days=60)).isoformat()
        fetched_at.write_text(old)

        assert is_stale("python") is True

    def test_invalid_fetched_at_is_stale(self, tmp_path, monkeypatch):
        """Test that invalid .fetched-at is treated as stale."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"
        fetched_at.write_text("not-a-date")

        assert is_stale("python") is True

    def test_fetched_at_directory_not_exists(self, tmp_path, monkeypatch):
        """Test that non-existent directory is stale."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        # Don't create the directory
        assert is_stale("nonexistent") is True


class TestGetLanguages:
    """Tests for get_languages function."""

    def test_finds_language_dirs(self, tmp_path, monkeypatch):
        """Test finding language directories with sources.json."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        # Create some language directories
        for lang in ["python", "typescript", "go"]:
            lang_dir = tmp_path / lang
            lang_dir.mkdir()
            (lang_dir / "sources.json").write_text('{"files": []}')

        # Create one without sources.json (should be excluded)
        (tmp_path / "rust").mkdir()

        # Create hidden dir (should be excluded)
        (tmp_path / "_templates").mkdir()

        languages = get_languages()
        assert "python" in languages
        assert "typescript" in languages
        assert "go" in languages
        assert "rust" not in languages
        assert "_templates" not in languages

    def test_returns_sorted(self, tmp_path, monkeypatch):
        """Test that languages are returned sorted."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        for lang in ["python", "go", "typescript"]:
            lang_dir = tmp_path / lang
            lang_dir.mkdir()
            (lang_dir / "sources.json").write_text('{"files": []}')

        languages = get_languages()
        assert languages == sorted(languages)

    def test_empty_specs_dir(self, tmp_path, monkeypatch):
        """Test with empty specs directory."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        languages = get_languages()
        assert languages == []

    def test_excludes_files(self, tmp_path, monkeypatch):
        """Test that files are excluded from language list."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        # Create a file in specs dir (not a directory)
        (tmp_path / "README.md").write_text("# Specs")
        # Create a valid language dir
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "sources.json").write_text('{"files": []}')

        languages = get_languages()
        assert "python" in languages
        assert "README.md" not in languages


class TestFetchResult:
    """Tests for FetchResult dataclass."""

    def test_success_result(self):
        result = FetchResult(path="spec.md", success=True, url="https://example.com")
        assert result.success is True
        assert result.error is None

    def test_failure_result(self):
        result = FetchResult(
            path="spec.md", success=False, url="https://example.com", error="Connection failed"
        )
        assert result.success is False
        assert result.error == "Connection failed"

    def test_default_values(self):
        """Test default values for optional fields."""
        result = FetchResult(path="test.md", success=True)
        assert result.url is None
        assert result.error is None


class TestLanguageResult:
    """Tests for LanguageResult dataclass."""

    def test_default_counts(self):
        result = LanguageResult(language="python")
        assert result.success == 0
        assert result.failed == 0
        assert result.skipped == 0
        assert result.errors == []

    def test_with_counts(self):
        result = LanguageResult(
            language="python", success=10, failed=2, skipped=5, errors=["Error 1", "Error 2"]
        )
        assert result.success == 10
        assert result.failed == 2
        assert len(result.errors) == 2

    def test_mutable_errors_list(self):
        """Test that errors list can be modified."""
        result = LanguageResult(language="python")
        result.errors.append("new error")
        assert "new error" in result.errors


class TestRateLimit:
    """Tests for rate_limit function."""

    def test_rate_limit_first_request_no_wait(self, monkeypatch):
        """Test that first request to a domain doesn't wait."""
        import fetch

        # Clear the last request dict
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 1.0)

        start = time.monotonic()
        rate_limit("example.com")
        elapsed = time.monotonic() - start

        # First request should not wait
        assert elapsed < 0.1

    def test_rate_limit_subsequent_request_waits(self, monkeypatch):
        """Test that subsequent requests to same domain wait."""
        import fetch

        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0.2)

        # First request
        rate_limit("example.com")

        # Second request should wait
        start = time.monotonic()
        rate_limit("example.com")
        elapsed = time.monotonic() - start

        # Should have waited close to RATE_LIMIT_SECONDS
        assert elapsed >= 0.15

    def test_rate_limit_different_domains_no_wait(self, monkeypatch):
        """Test that different domains don't affect each other."""
        import fetch

        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 1.0)

        rate_limit("example.com")

        start = time.monotonic()
        rate_limit("other.com")
        elapsed = time.monotonic() - start

        # Different domain should not wait
        assert elapsed < 0.1


class TestFetchFile:
    """Tests for fetch_file function."""

    def test_fetch_file_no_path(self, tmp_path, monkeypatch):
        """Test fetch_file returns error when no path specified."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        file_spec = {"urls": ["https://example.com/spec"]}
        result = fetch_file("python", file_spec)

        assert result.success is False
        assert result.path == "unknown"
        assert "No path specified" in result.error

    def test_fetch_file_no_urls_skips(self, tmp_path, monkeypatch):
        """Test fetch_file skips when no URLs provided."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        file_spec = {"path": "spec.md", "urls": []}
        result = fetch_file("python", file_spec)

        assert result.success is True
        assert result.path == "spec.md"

    def test_fetch_file_success_markdown(self, tmp_path, monkeypatch):
        """Test successful fetch of markdown content."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            return "# Test Markdown\n\nContent here."

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {"path": "spec.md", "urls": ["https://example.com/spec.md"]}
        result = fetch_file("python", file_spec)

        assert result.success is True
        assert result.path == "spec.md"
        assert result.url == "https://example.com/spec.md"

        # Verify file was written
        output_file = lang_dir / "spec.md"
        assert output_file.exists()
        assert "# Test Markdown" in output_file.read_text()

    def test_fetch_file_html_conversion(self, tmp_path, monkeypatch):
        """Test fetch_file converts HTML to markdown."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            return "<html><body><h1>Title</h1><p>Content</p></body></html>"

        def mock_html_to_markdown(content, output_path):
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text("# Title\n\nContent\n")
            return True

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr("fetch.write_text", lambda p, c: p.write_text(c))

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {"path": "spec.md", "urls": ["https://example.com/spec.html"]}
        result = fetch_file("python", file_spec)

        assert result.success is True

    def test_fetch_file_html_conversion_fallback(self, tmp_path, monkeypatch):
        """Test fetch_file falls back to raw content when HTML conversion fails."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        html_content = "<html><body><h1>Title</h1></body></html>"

        def mock_fetch_url(url):
            return html_content

        def mock_html_to_markdown(content, output_path):
            return False  # Conversion failed

        written_content = []

        def mock_write_text(path, content):
            path.parent.mkdir(parents=True, exist_ok=True)
            written_content.append((str(path), content))
            path.write_text(content)

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr("fetch.write_text", mock_write_text)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {"path": "spec.md", "urls": ["https://example.com/spec.html"]}
        result = fetch_file("python", file_spec)

        assert result.success is True
        # Check that raw content was written as fallback
        assert any(html_content in content for _, content in written_content)

    def test_fetch_file_fetch_error_tries_next_url(self, tmp_path, monkeypatch):
        """Test fetch_file tries next URL on FetchError."""
        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        call_count = [0]

        def mock_fetch_url(url):
            call_count[0] += 1
            if "primary" in url:
                raise FetchError(url=url, message="Connection failed")
            return "# Success from secondary"

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {
            "path": "spec.md",
            "urls": ["https://primary.com/spec", "https://secondary.com/spec"],
        }
        result = fetch_file("python", file_spec)

        assert result.success is True
        assert call_count[0] == 2
        assert result.url == "https://secondary.com/spec"

    def test_fetch_file_all_urls_fail(self, tmp_path, monkeypatch):
        """Test fetch_file returns failure when all URLs fail."""
        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            raise FetchError(url=url, message="Connection failed")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {
            "path": "spec.md",
            "urls": ["https://example.com/spec", "https://backup.com/spec"],
        }
        result = fetch_file("python", file_spec)

        assert result.success is False
        assert "Connection failed" in result.error
        assert result.url == "https://example.com/spec"

    def test_fetch_file_generic_exception(self, tmp_path, monkeypatch):
        """Test fetch_file handles generic exceptions."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            raise RuntimeError("Unexpected error")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {"path": "spec.md", "urls": ["https://example.com/spec"]}
        result = fetch_file("python", file_spec)

        assert result.success is False
        assert "Unexpected error" in result.error

    def test_fetch_file_creates_parent_dirs(self, tmp_path, monkeypatch):
        """Test fetch_file creates nested directories."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            return "# Content"

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        file_spec = {"path": "stdlib/os/path.md", "urls": ["https://example.com/path"]}
        result = fetch_file("python", file_spec)

        assert result.success is True
        output_file = lang_dir / "stdlib" / "os" / "path.md"
        assert output_file.exists()


class TestFetchLanguage:
    """Tests for fetch_language function."""

    def test_fetch_language_no_sources(self, tmp_path, monkeypatch, caplog):
        """Test fetch_language with no sources.json."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        with caplog.at_level(logging.WARNING):
            result = fetch_language("nonexistent")

        assert result.language == "nonexistent"
        assert result.success == 0
        assert result.failed == 0

    def test_fetch_language_empty_files(self, tmp_path, monkeypatch, caplog):
        """Test fetch_language with empty files list."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "sources.json").write_text('{"language": "python", "files": []}')

        with caplog.at_level(logging.WARNING):
            result = fetch_language("python")

        assert result.success == 0

    def test_fetch_language_skips_no_urls(self, tmp_path, monkeypatch):
        """Test fetch_language skips files with no URLs."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "spec.md"},  # No URLs
                {"path": "other.md", "urls": []},  # Empty URLs
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        result = fetch_language("python")

        assert result.skipped == 2
        assert result.success == 0
        assert result.failed == 0

    def test_fetch_language_dry_run(self, tmp_path, monkeypatch, caplog):
        """Test fetch_language in dry run mode."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/spec"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.INFO):
            result = fetch_language("python", dry_run=True)

        assert result.success == 1
        assert result.failed == 0
        assert "[dry-run]" in caplog.text

        # Verify no file was actually created
        assert not (lang_dir / "spec.md").exists()
        # Verify no .fetched-at was written
        assert not (lang_dir / ".fetched-at").exists()

    def test_fetch_language_success(self, tmp_path, monkeypatch):
        """Test successful fetch_language."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            return f"# Content from {url}"

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "spec.md", "urls": ["https://example.com/spec"]},
                {"path": "stdlib.md", "urls": ["https://example.com/stdlib"]},
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        result = fetch_language("python")

        assert result.success == 2
        assert result.failed == 0
        assert (lang_dir / ".fetched-at").exists()

    def test_fetch_language_with_failures(self, tmp_path, monkeypatch):
        """Test fetch_language with some failures."""
        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            if "fail" in url:
                raise FetchError(url=url, message="Not found")
            return f"# Content from {url}"

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "spec.md", "urls": ["https://example.com/spec"]},
                {"path": "fail.md", "urls": ["https://example.com/fail"]},
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        result = fetch_language("python")

        assert result.success == 1
        assert result.failed == 1
        assert len(result.errors) == 1
        assert "fail.md" in result.errors[0]

    def test_fetch_language_no_fetched_at_on_all_failure(self, tmp_path, monkeypatch):
        """Test that .fetched-at is not written when all fetches fail."""
        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        def mock_fetch_url(url):
            raise FetchError(url=url, message="Failed")

        write_fetched_at_called = []

        def mock_write_fetched_at(path):
            write_fetched_at_called.append(path)

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/spec"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        result = fetch_language("python")

        assert result.success == 0
        assert result.failed == 1
        # write_fetched_at should not have been called
        assert len(write_fetched_at_called) == 0


class TestMain:
    """Tests for main function."""

    def test_main_help(self, monkeypatch, capsys):
        """Test main with --help flag."""

        monkeypatch.setattr("sys.argv", ["fetch.py", "--help"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "Options:" in captured.out
        assert "--dry-run" in captured.out
        assert "--delta" in captured.out

    def test_main_help_short(self, monkeypatch, capsys):
        """Test main with -h flag."""

        monkeypatch.setattr("sys.argv", ["fetch.py", "-h"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "Options:" in captured.out

    def test_main_all_languages(self, tmp_path, monkeypatch, caplog):
        """Test main fetching all languages."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)
        monkeypatch.setattr("sys.argv", ["fetch.py"])

        def mock_fetch_url(url):
            return "# Content"

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        # Create test languages
        for lang in ["python", "typescript"]:
            lang_dir = tmp_path / lang
            lang_dir.mkdir()
            sources = {
                "language": lang,
                "files": [{"path": "spec.md", "urls": [f"https://example.com/{lang}"]}],
            }
            (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 0
        assert "Summary" in caplog.text
        assert "Files fetched: 2" in caplog.text

    def test_main_specific_languages(self, tmp_path, monkeypatch, caplog):
        """Test main fetching specific languages."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)
        monkeypatch.setattr("sys.argv", ["fetch.py", "python"])

        def mock_fetch_url(url):
            return "# Content"

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        # Create test language
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/python"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 0
        assert "Languages: 1" in caplog.text

    def test_main_dry_run(self, tmp_path, monkeypatch, caplog):
        """Test main in dry run mode."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr("sys.argv", ["fetch.py", "--dry-run"])

        # Create test language
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/python"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 0
        assert "DRY RUN MODE" in caplog.text
        # Verify no file was created
        assert not (lang_dir / "spec.md").exists()

    def test_main_delta_mode_all_fresh(self, tmp_path, monkeypatch, caplog):
        """Test main in delta mode when all specs are fresh."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr(fetch, "STALE_DAYS", 30)
        monkeypatch.setattr("sys.argv", ["fetch.py", "--delta"])

        # Create test language with recent .fetched-at
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {"language": "python", "files": []}
        (lang_dir / "sources.json").write_text(json.dumps(sources))
        (lang_dir / ".fetched-at").write_text(datetime.now(UTC).isoformat())

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 0
        assert "All specs are fresh" in caplog.text

    def test_main_delta_mode_stale(self, tmp_path, monkeypatch, caplog):
        """Test main in delta mode with stale specs."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr(fetch, "STALE_DAYS", 30)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)
        monkeypatch.setattr("sys.argv", ["fetch.py", "--delta"])

        def mock_fetch_url(url):
            return "# Content"

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        # Create stale language
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/python"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))
        old_date = (datetime.now(UTC) - timedelta(days=60)).isoformat()
        (lang_dir / ".fetched-at").write_text(old_date)

        # Create fresh language
        fresh_dir = tmp_path / "typescript"
        fresh_dir.mkdir()
        (fresh_dir / "sources.json").write_text('{"language": "typescript", "files": []}')
        (fresh_dir / ".fetched-at").write_text(datetime.now(UTC).isoformat())

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 0
        assert "Delta mode: 1/2 languages are stale" in caplog.text

    def test_main_with_failures_returns_error(self, tmp_path, monkeypatch, caplog):
        """Test main returns 1 when there are failures."""
        import logging

        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)
        monkeypatch.setattr("sys.argv", ["fetch.py"])

        def mock_fetch_url(url):
            raise FetchError(url=url, message="Connection failed")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        # Create test language
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/python"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 1
        assert "Files failed: 1" in caplog.text
        assert "Errors:" in caplog.text

    def test_main_fatal_error_in_executor(self, tmp_path, monkeypatch, caplog):
        """Test main handles fatal errors in thread executor."""
        import logging

        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr("sys.argv", ["fetch.py"])

        original_fetch_language = fetch.fetch_language

        def mock_fetch_language(lang, dry_run=False):
            if lang == "python":
                raise RuntimeError("Fatal error in thread")
            return original_fetch_language(lang, dry_run)

        monkeypatch.setattr("fetch.fetch_language", mock_fetch_language)

        # Create test language
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {"language": "python", "files": []}
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.ERROR):
            main()

        # Should still complete (result may be 0 since no successful fetches)
        assert "Fatal error" in caplog.text

    def test_main_limits_error_display(self, tmp_path, monkeypatch, caplog):
        """Test main limits number of errors displayed per language."""
        import logging

        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "MAX_WORKERS", 1)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)
        monkeypatch.setattr("sys.argv", ["fetch.py"])

        def mock_fetch_url(url):
            raise FetchError(url=url, message=f"Error for {url}")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)

        # Create test language with many files
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": f"file{i}.md", "urls": [f"https://example.com/file{i}"]}
                for i in range(10)  # 10 files to exceed the 3-error limit
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 1
        # Count error lines - should be limited to 3 per language
        error_lines = [line for line in caplog.text.split("\n") if "[python]" in line]
        assert len(error_lines) <= 3


class TestEnvironmentVariables:
    """Tests for environment variable configuration."""

    def test_max_workers_from_env(self, monkeypatch):
        """Test MAX_WORKERS is read from environment."""
        # This tests the module-level constant
        monkeypatch.setenv("FETCH_WORKERS", "8")

        # Re-import to pick up new env value
        import importlib

        import fetch

        importlib.reload(fetch)

        assert fetch.MAX_WORKERS == 8

        # Restore default
        monkeypatch.delenv("FETCH_WORKERS", raising=False)
        importlib.reload(fetch)

    def test_stale_days_from_env(self, monkeypatch):
        """Test STALE_DAYS is read from environment."""
        monkeypatch.setenv("FETCH_STALE_DAYS", "14")

        import importlib

        import fetch

        importlib.reload(fetch)

        assert fetch.STALE_DAYS == 14

        # Restore default
        monkeypatch.delenv("FETCH_STALE_DAYS", raising=False)
        importlib.reload(fetch)

    def test_rate_limit_from_env(self, monkeypatch):
        """Test RATE_LIMIT_SECONDS is read from environment."""
        monkeypatch.setenv("FETCH_RATE_LIMIT", "2.0")

        import importlib

        import fetch

        importlib.reload(fetch)

        assert fetch.RATE_LIMIT_SECONDS == 2.0

        # Restore default
        monkeypatch.delenv("FETCH_RATE_LIMIT", raising=False)
        importlib.reload(fetch)


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_fetch_file_empty_path(self, tmp_path, monkeypatch):
        """Test fetch_file with empty path string."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)

        file_spec = {"path": "", "urls": ["https://example.com/spec"]}
        result = fetch_file("python", file_spec)

        assert result.success is False
        assert "No path specified" in result.error

    def test_fetch_file_html_detection_by_content(self, tmp_path, monkeypatch):
        """Test HTML detection by content (not URL extension)."""
        import fetch

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        # HTML content without .html extension in URL
        html_content = "<!DOCTYPE html><html><head></head><body>Content</body></html>"

        def mock_fetch_url(url):
            return html_content

        def mock_html_to_markdown(content, output_path):
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text("# Converted")
            return True

        def mock_write_text(path, content):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.html_to_markdown", mock_html_to_markdown)
        monkeypatch.setattr("fetch.write_text", mock_write_text)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        # URL without .html extension
        file_spec = {"path": "spec.md", "urls": ["https://example.com/spec"]}
        result = fetch_file("python", file_spec)

        assert result.success is True

    def test_fetch_language_mixed_results(self, tmp_path, monkeypatch):
        """Test fetch_language with mix of success, failure, and skip."""
        import fetch
        from _common import FetchError

        monkeypatch.setattr(fetch, "SPECS_DIR", tmp_path)
        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0)

        call_urls = []

        def mock_fetch_url(url):
            call_urls.append(url)
            if "fail" in url:
                raise FetchError(url=url, message="Failed")
            return "# Content"

        def mock_write_fetched_at(path):
            (path / ".fetched-at").write_text("2024-01-01T00:00:00Z")

        monkeypatch.setattr("fetch.fetch_url", mock_fetch_url)
        monkeypatch.setattr("fetch.write_fetched_at", mock_write_fetched_at)

        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "success.md", "urls": ["https://example.com/success"]},
                {"path": "fail.md", "urls": ["https://example.com/fail"]},
                {"path": "skip.md"},  # No URLs - should skip
                {"path": "empty_urls.md", "urls": []},  # Empty URLs - should skip
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        result = fetch_language("python")

        assert result.success == 1
        assert result.failed == 1
        assert result.skipped == 2
        assert len(result.errors) == 1

    def test_concurrent_rate_limiting(self, monkeypatch):
        """Test rate limiting is thread-safe."""
        from concurrent.futures import ThreadPoolExecutor

        import fetch

        monkeypatch.setattr(fetch, "_last_request", {})
        monkeypatch.setattr(fetch, "RATE_LIMIT_SECONDS", 0.05)

        results = []

        def rate_limit_call(domain):
            start = time.monotonic()
            rate_limit(domain)
            return time.monotonic() - start

        # Call rate_limit concurrently for same domain
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(rate_limit_call, "same-domain.com") for _ in range(4)]
            results = [f.result() for f in futures]

        # At least one call should have waited (not the first one)
        # Due to rate limiting, subsequent calls should take longer
        assert any(r >= 0.04 for r in results[1:])  # At least one waited


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
