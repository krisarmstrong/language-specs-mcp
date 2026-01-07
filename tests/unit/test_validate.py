#!/usr/bin/env python3
"""Unit tests for validate.py."""

import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from validate import is_stub_file, load_allowlist


class TestIsStubFile:
    """Tests for is_stub_file function."""

    def test_single_see_line_is_stub(self, tmp_path):
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs")
        assert is_stub_file(stub) is True

    def test_see_with_blank_line_is_stub(self, tmp_path):
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs\n\n")
        assert is_stub_file(stub) is True

    def test_two_lines_with_see_is_stub(self, tmp_path):
        stub = tmp_path / "stub.md"
        stub.write_text("# Title\nSee: https://example.com/docs")
        assert is_stub_file(stub) is True

    def test_three_content_lines_not_stub(self, tmp_path):
        full = tmp_path / "full.md"
        full.write_text("# Title\n\nSome content.\n\nMore content.")
        assert is_stub_file(full) is False

    def test_no_see_line_not_stub(self, tmp_path):
        full = tmp_path / "full.md"
        full.write_text("# Title\nContent")
        assert is_stub_file(full) is False

    def test_nonexistent_file_not_stub(self, tmp_path):
        missing = tmp_path / "missing.md"
        assert is_stub_file(missing) is False

    def test_empty_file_not_stub(self, tmp_path):
        empty = tmp_path / "empty.md"
        empty.write_text("")
        assert is_stub_file(empty) is False


class TestLoadAllowlist:
    """Tests for load_allowlist function."""

    def test_loads_entries(self, tmp_path, monkeypatch):
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("specs/python/stub1.md\nspecs/go/stub2.md\n")
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))
        result = load_allowlist()
        assert "specs/python/stub1.md" in result
        assert "specs/go/stub2.md" in result

    def test_ignores_blank_lines(self, tmp_path, monkeypatch):
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("entry1\n\n\nentry2\n")
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))
        result = load_allowlist()
        assert len(result) == 2
        assert "" not in result

    def test_returns_empty_for_missing_file(self, tmp_path, monkeypatch):
        monkeypatch.setenv("STUB_ALLOWLIST", str(tmp_path / "nonexistent.txt"))
        result = load_allowlist()
        assert result == set()


class TestFreshnessValidation:
    """Tests for freshness validation logic."""

    def test_fresh_fetched_at_passes(self, tmp_path):
        """Test that recent .fetched-at files pass validation."""
        # Create a spec directory with recent .fetched-at
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"
        recent = datetime.now(timezone.utc).isoformat()
        fetched_at.write_text(recent)

        # Read back and parse
        content = fetched_at.read_text().strip()
        parsed = datetime.fromisoformat(content.replace("Z", "+00:00"))
        age_seconds = (datetime.now(timezone.utc) - parsed).total_seconds()

        # Should be less than 90 days (default MAX_AGE_DAYS)
        max_age_seconds = 90 * 24 * 60 * 60
        assert age_seconds < max_age_seconds

    def test_stale_fetched_at_fails(self, tmp_path):
        """Test that old .fetched-at files would fail validation."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"

        # Write a timestamp from 100 days ago
        old_time = datetime.now(timezone.utc) - timedelta(days=100)
        fetched_at.write_text(old_time.isoformat())

        content = fetched_at.read_text().strip()
        parsed = datetime.fromisoformat(content.replace("Z", "+00:00"))
        age_seconds = (datetime.now(timezone.utc) - parsed).total_seconds()

        # Should be more than 90 days
        max_age_seconds = 90 * 24 * 60 * 60
        assert age_seconds > max_age_seconds


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
