#!/usr/bin/env python3
"""Unit tests for fetch.py."""

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetch import (
    load_sources,
    is_stale,
    get_languages,
    FetchResult,
    LanguageResult,
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
        recent = datetime.now(timezone.utc).isoformat()
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
        old = (datetime.now(timezone.utc) - timedelta(days=60)).isoformat()
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


class TestFetchResult:
    """Tests for FetchResult dataclass."""

    def test_success_result(self):
        result = FetchResult(path="spec.md", success=True, url="https://example.com")
        assert result.success is True
        assert result.error is None

    def test_failure_result(self):
        result = FetchResult(
            path="spec.md",
            success=False,
            url="https://example.com",
            error="Connection failed"
        )
        assert result.success is False
        assert result.error == "Connection failed"


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
            language="python",
            success=10,
            failed=2,
            skipped=5,
            errors=["Error 1", "Error 2"]
        )
        assert result.success == 10
        assert result.failed == 2
        assert len(result.errors) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
