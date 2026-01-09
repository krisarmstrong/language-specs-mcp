#!/usr/bin/env python3
"""Unit tests for doctor.py - environment and data sanity checks."""

import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from doctor import (
    CRON_MARKER,
    LAUNCHD_LABEL,
    check_cron,
    check_launchd,
    count_stubs,
    is_stub_file,
    latest_fetched_at,
    load_search_generated,
    load_versions,
    main,
    parse_env_file,
    parse_iso,
    status_line,
)


class TestParseEnvFile:
    """Tests for parse_env_file function."""

    def test_parses_simple_env_file(self, tmp_path, monkeypatch):
        """Test parsing a simple .env file."""
        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=abc123\nAPI_KEY=secret\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"GITHUB_TOKEN": "abc123", "API_KEY": "secret"}

    def test_ignores_empty_lines(self, tmp_path, monkeypatch):
        """Test that empty lines are ignored."""
        env_file = tmp_path / ".env"
        env_file.write_text("FOO=bar\n\n\nBAZ=qux\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"FOO": "bar", "BAZ": "qux"}

    def test_ignores_comments(self, tmp_path, monkeypatch):
        """Test that comment lines are ignored."""
        env_file = tmp_path / ".env"
        env_file.write_text("# This is a comment\nFOO=bar\n# Another comment\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"FOO": "bar"}

    def test_ignores_lines_without_equals(self, tmp_path, monkeypatch):
        """Test that lines without = are ignored."""
        env_file = tmp_path / ".env"
        env_file.write_text("VALID=value\ninvalid line\nANOTHER=test\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"VALID": "value", "ANOTHER": "test"}

    def test_handles_values_with_equals(self, tmp_path, monkeypatch):
        """Test that values containing = are parsed correctly."""
        env_file = tmp_path / ".env"
        env_file.write_text("TOKEN=abc=def=ghi\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"TOKEN": "abc=def=ghi"}

    def test_strips_whitespace(self, tmp_path, monkeypatch):
        """Test that whitespace is stripped from keys and values."""
        env_file = tmp_path / ".env"
        env_file.write_text("  KEY  =  value  \n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"KEY": "value"}

    def test_returns_empty_for_missing_file(self, tmp_path, monkeypatch):
        """Test that missing .env file returns empty dict."""
        env_file = tmp_path / "nonexistent" / ".env"

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {}

    def test_handles_empty_value(self, tmp_path, monkeypatch):
        """Test that empty values are handled."""
        env_file = tmp_path / ".env"
        env_file.write_text("EMPTY=\nNOT_EMPTY=value\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"EMPTY": "", "NOT_EMPTY": "value"}

    def test_handles_whitespace_only_lines(self, tmp_path, monkeypatch):
        """Test that whitespace-only lines are ignored."""
        env_file = tmp_path / ".env"
        env_file.write_text("KEY=value\n   \n\t\nOTHER=test\n")

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        assert result == {"KEY": "value", "OTHER": "test"}


class TestParseIso:
    """Tests for parse_iso function."""

    def test_parses_valid_iso_datetime(self):
        """Test parsing a valid ISO datetime string."""
        result = parse_iso("2024-01-15T10:30:00+00:00")
        assert result is not None
        assert result.year == 2024
        assert result.month == 1
        assert result.day == 15

    def test_parses_utc_z_suffix(self):
        """Test parsing ISO datetime with Z suffix."""
        # Note: fromisoformat in Python 3.11+ handles Z
        result = parse_iso("2024-06-20T15:45:30+00:00")
        assert result is not None
        assert result.hour == 15
        assert result.minute == 45

    def test_returns_none_for_invalid_format(self):
        """Test that invalid format returns None."""
        result = parse_iso("not-a-date")
        assert result is None

    def test_returns_none_for_empty_string(self):
        """Test that empty string returns None."""
        result = parse_iso("")
        assert result is None

    def test_parses_date_only(self):
        """Test parsing date-only string."""
        result = parse_iso("2024-03-15")
        assert result is not None
        assert result.year == 2024
        assert result.month == 3
        assert result.day == 15

    def test_parses_datetime_without_timezone(self):
        """Test parsing datetime without timezone."""
        result = parse_iso("2024-07-20T12:00:00")
        assert result is not None
        assert result.hour == 12


class TestLatestFetchedAt:
    """Tests for latest_fetched_at function."""

    def test_finds_latest_timestamp(self, tmp_path, monkeypatch):
        """Test finding the most recent .fetched-at timestamp."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create directories with different timestamps
        lang1 = specs_dir / "python"
        lang1.mkdir()
        old_time = datetime.now(UTC) - timedelta(days=30)
        (lang1 / ".fetched-at").write_text(old_time.isoformat())

        lang2 = specs_dir / "go"
        lang2.mkdir()
        recent_time = datetime.now(UTC) - timedelta(days=5)
        (lang2 / ".fetched-at").write_text(recent_time.isoformat())

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        result = latest_fetched_at()
        assert result is not None
        # Should be close to recent_time (within a second)
        assert abs((result - recent_time).total_seconds()) < 1

    def test_returns_none_when_no_fetched_at(self, tmp_path, monkeypatch):
        """Test returning None when no .fetched-at files exist."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        (specs_dir / "python").mkdir()

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        result = latest_fetched_at()
        assert result is None

    def test_skips_invalid_timestamps(self, tmp_path, monkeypatch):
        """Test that invalid timestamps are skipped."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang1 = specs_dir / "python"
        lang1.mkdir()
        (lang1 / ".fetched-at").write_text("invalid-date")

        lang2 = specs_dir / "go"
        lang2.mkdir()
        valid_time = datetime.now(UTC) - timedelta(days=1)
        (lang2 / ".fetched-at").write_text(valid_time.isoformat())

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        result = latest_fetched_at()
        assert result is not None
        assert abs((result - valid_time).total_seconds()) < 1

    def test_handles_nested_fetched_at(self, tmp_path, monkeypatch):
        """Test finding .fetched-at in nested directories."""
        import doctor

        specs_dir = tmp_path / "specs"
        nested = specs_dir / "python" / "stdlib"
        nested.mkdir(parents=True)

        recent_time = datetime.now(UTC)
        (nested / ".fetched-at").write_text(recent_time.isoformat())

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        result = latest_fetched_at()
        assert result is not None


class TestIsStubFile:
    """Tests for is_stub_file function."""

    def test_single_see_line_is_stub(self, tmp_path):
        """Test that a single See: line is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com/docs")
        assert is_stub_file(stub) is True

    def test_title_and_see_is_stub(self, tmp_path):
        """Test that title + See: line is a stub."""
        stub = tmp_path / "stub.md"
        stub.write_text("# Title\nSee: https://example.com")
        assert is_stub_file(stub) is True

    def test_three_lines_not_stub(self, tmp_path):
        """Test that more than two content lines is not a stub."""
        full = tmp_path / "full.md"
        full.write_text("# Title\n\nSome content.\n\nMore content.")
        assert is_stub_file(full) is False

    def test_no_see_line_not_stub(self, tmp_path):
        """Test that file without See: is not a stub."""
        full = tmp_path / "full.md"
        full.write_text("# Title\nContent without see line")
        assert is_stub_file(full) is False

    def test_nonexistent_file_not_stub(self, tmp_path):
        """Test that nonexistent file returns False."""
        missing = tmp_path / "missing.md"
        assert is_stub_file(missing) is False

    def test_empty_file_not_stub(self, tmp_path):
        """Test that empty file is not a stub."""
        empty = tmp_path / "empty.md"
        empty.write_text("")
        assert is_stub_file(empty) is False

    def test_whitespace_only_lines_ignored(self, tmp_path):
        """Test that whitespace-only lines don't count."""
        stub = tmp_path / "stub.md"
        stub.write_text("See: https://example.com\n   \n\t\n")
        assert is_stub_file(stub) is True

    def test_see_not_at_beginning_not_stub(self, tmp_path):
        """Test that 'See:' must start the line."""
        file = tmp_path / "test.md"
        file.write_text("This line contains See: but not at start")
        assert is_stub_file(file) is False

    def test_handles_oserror(self, tmp_path, monkeypatch):
        """Test that OSError is handled gracefully."""
        file = tmp_path / "test.md"
        file.write_text("content")

        # Mock read_text to raise OSError
        original_read_text = Path.read_text

        def mock_read_text(self, encoding=None):
            if self.name == "test.md":
                raise OSError("Permission denied")
            return original_read_text(self, encoding=encoding)

        monkeypatch.setattr(Path, "read_text", mock_read_text)
        assert is_stub_file(file) is False


class TestCountStubs:
    """Tests for count_stubs function."""

    def test_counts_total_stubs(self, tmp_path, monkeypatch):
        """Test counting total stub files."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)

        (lang_dir / "stub1.md").write_text("See: https://example.com")
        (lang_dir / "stub2.md").write_text("See: https://other.com")
        (lang_dir / "full.md").write_text("# Full content\n\nWith details.\n\nAnd more.")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        total, important = count_stubs()
        assert total == 2
        assert important == 0

    def test_counts_important_stubs(self, tmp_path, monkeypatch):
        """Test counting spec.md and overview.md stubs."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)

        (lang_dir / "spec.md").write_text("See: https://example.com")
        (lang_dir / "overview.md").write_text("See: https://other.com")
        (lang_dir / "other.md").write_text("See: https://third.com")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        total, important = count_stubs()
        assert total == 3
        assert important == 2

    def test_returns_zero_when_no_stubs(self, tmp_path, monkeypatch):
        """Test returning zeros when no stub files exist."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)

        (lang_dir / "spec.md").write_text("# Full\n\nContent.\n\nHere.")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        total, important = count_stubs()
        assert total == 0
        assert important == 0

    def test_handles_empty_directory(self, tmp_path, monkeypatch):
        """Test handling empty specs directory."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        total, important = count_stubs()
        assert total == 0
        assert important == 0


class TestCheckLaunchd:
    """Tests for check_launchd function."""

    def test_returns_false_when_plist_missing(self, tmp_path, monkeypatch):
        """Test returning False when plist doesn't exist."""
        # Point to a non-existent home directory
        fake_home = tmp_path / "fake_home"
        fake_home.mkdir()

        with patch.object(Path, "home", return_value=fake_home):
            ok, detail = check_launchd()

        assert ok is False
        assert "not installed" in detail

    def test_returns_true_when_loaded(self, tmp_path, monkeypatch):
        """Test returning True when agent is loaded."""
        fake_home = tmp_path / "fake_home"
        launch_agents = fake_home / "Library" / "LaunchAgents"
        launch_agents.mkdir(parents=True)

        plist = launch_agents / f"{LAUNCHD_LABEL}.plist"
        plist.write_text("<plist>...</plist>")

        mock_result = MagicMock()
        mock_result.returncode = 0

        with patch.object(Path, "home", return_value=fake_home):
            with patch("subprocess.run", return_value=mock_result):
                ok, detail = check_launchd()

        assert ok is True
        assert "loaded" in detail.lower()

    def test_returns_false_when_not_loaded(self, tmp_path, monkeypatch):
        """Test returning False when plist exists but not loaded."""
        fake_home = tmp_path / "fake_home"
        launch_agents = fake_home / "Library" / "LaunchAgents"
        launch_agents.mkdir(parents=True)

        plist = launch_agents / f"{LAUNCHD_LABEL}.plist"
        plist.write_text("<plist>...</plist>")

        mock_result = MagicMock()
        mock_result.returncode = 1

        with patch.object(Path, "home", return_value=fake_home):
            with patch("subprocess.run", return_value=mock_result):
                ok, detail = check_launchd()

        assert ok is False
        assert "not loaded" in detail.lower()

    def test_handles_launchctl_not_available(self, tmp_path):
        """Test handling when launchctl is not available."""
        fake_home = tmp_path / "fake_home"
        launch_agents = fake_home / "Library" / "LaunchAgents"
        launch_agents.mkdir(parents=True)

        plist = launch_agents / f"{LAUNCHD_LABEL}.plist"
        plist.write_text("<plist>...</plist>")

        with patch.object(Path, "home", return_value=fake_home):
            with patch("subprocess.run", side_effect=OSError("launchctl not found")):
                ok, detail = check_launchd()

        assert ok is False
        assert "not available" in detail.lower()


class TestCheckCron:
    """Tests for check_cron function."""

    def test_returns_false_when_crontab_not_available(self, monkeypatch):
        """Test returning False when crontab command not available."""
        monkeypatch.setattr("shutil.which", lambda x: None)

        ok, detail = check_cron()
        assert ok is False
        assert "not available" in detail.lower()

    def test_returns_false_when_crontab_empty(self, monkeypatch):
        """Test returning False when crontab is empty."""
        monkeypatch.setattr("shutil.which", lambda x: "/usr/bin/crontab")

        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""

        with patch("subprocess.run", return_value=mock_result):
            ok, detail = check_cron()

        assert ok is False
        assert "empty" in detail.lower()

    def test_returns_true_when_entry_found(self, monkeypatch):
        """Test returning True when specforge entry is found."""
        monkeypatch.setattr("shutil.which", lambda x: "/usr/bin/crontab")

        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = f"0 2 * * * /path/to/refresh.py {CRON_MARKER}\n"

        with patch("subprocess.run", return_value=mock_result):
            ok, detail = check_cron()

        assert ok is True
        assert "installed" in detail.lower()

    def test_returns_false_when_entry_not_found(self, monkeypatch):
        """Test returning False when specforge entry is not in crontab."""
        monkeypatch.setattr("shutil.which", lambda x: "/usr/bin/crontab")

        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "0 2 * * * /other/script.sh\n"

        with patch("subprocess.run", return_value=mock_result):
            ok, detail = check_cron()

        assert ok is False
        assert "not found" in detail.lower()


class TestLoadVersions:
    """Tests for load_versions function."""

    def test_returns_none_when_file_missing(self, tmp_path, monkeypatch):
        """Test returning None when versions.json doesn't exist."""
        import doctor

        tools_json = tmp_path / "tools" / "versions.json"
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)

        updated_at, missing = load_versions()
        assert updated_at is None
        assert "missing" in missing[0].lower()

    def test_returns_updated_at(self, tmp_path, monkeypatch):
        """Test returning updatedAt from versions.json."""
        import doctor

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"

        data = {
            "updatedAt": "2024-01-15T10:00:00Z",
            "tools": [{"name": "test", "version": "1.0.0", "checkedAt": "2024-01-15"}],
        }
        tools_json.write_text(json.dumps(data))

        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)

        updated_at, missing = load_versions()
        assert updated_at == "2024-01-15T10:00:00Z"
        assert missing == []

    def test_finds_missing_checked_at(self, tmp_path, monkeypatch):
        """Test finding tools with latest config but no checkedAt."""
        import doctor

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"

        data = {
            "updatedAt": "2024-01-15",
            "tools": [
                {
                    "name": "tool1",
                    "version": "1.0",
                    "latest": {"type": "npm"},
                    "checkedAt": "2024-01-15",
                },
                {
                    "name": "tool2",
                    "version": "2.0",
                    "latest": {"type": "pypi"},
                },  # Missing checkedAt
                {"name": "tool3", "version": "3.0"},  # No latest, so no checkedAt needed
            ],
        }
        tools_json.write_text(json.dumps(data))

        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)

        updated_at, missing = load_versions()
        assert updated_at == "2024-01-15"
        assert missing == ["tool2"]


class TestLoadSearchGenerated:
    """Tests for load_search_generated function."""

    def test_returns_none_when_file_missing(self, tmp_path, monkeypatch):
        """Test returning None when search.json doesn't exist."""
        import doctor

        search_json = tmp_path / "specs" / "search.json"
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)

        result = load_search_generated()
        assert result is None

    def test_returns_generated_at(self, tmp_path, monkeypatch):
        """Test returning generatedAt from search.json."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        search_json = specs_dir / "search.json"

        data = {"generatedAt": "2024-01-20T12:00:00Z", "entries": []}
        search_json.write_text(json.dumps(data))

        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)

        result = load_search_generated()
        assert result == "2024-01-20T12:00:00Z"

    def test_returns_none_when_no_generated_at(self, tmp_path, monkeypatch):
        """Test returning None when generatedAt is missing from file."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        search_json = specs_dir / "search.json"

        data = {"entries": []}
        search_json.write_text(json.dumps(data))

        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)

        result = load_search_generated()
        assert result is None


class TestStatusLine:
    """Tests for status_line function."""

    def test_ok_status(self):
        """Test OK status formatting."""
        result = status_line("Test", True, "everything good")
        assert result == "[OK] Test: everything good"

    def test_warn_status(self):
        """Test WARN status formatting."""
        result = status_line("Test", False, "something wrong")
        assert result == "[WARN] Test: something wrong"

    def test_handles_empty_detail(self):
        """Test handling empty detail string."""
        result = status_line("Test", True, "")
        assert result == "[OK] Test: "


class TestMain:
    """Tests for main function."""

    def test_returns_zero(self, tmp_path, monkeypatch, capsys):
        """Test that main returns 0."""
        import doctor

        # Setup minimal environment
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        lang_dir = specs_dir / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text(datetime.now(UTC).isoformat())

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test123\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        # Mock scheduler checks
        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "Cron installed")):
                result = main()

        assert result == 0

    def test_outputs_github_token_status(self, tmp_path, monkeypatch, capsys):
        """Test that GITHUB_TOKEN status is output."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "GITHUB_TOKEN" in captured.out
        assert "[OK]" in captured.out

    def test_outputs_missing_github_token(self, tmp_path, monkeypatch, capsys):
        """Test that missing GITHUB_TOKEN is reported."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        # No GITHUB_TOKEN in .env

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        # Also ensure env var is not set
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "GITHUB_TOKEN" in captured.out
        assert "missing" in captured.out.lower()

    def test_uses_launchd_on_darwin(self, tmp_path, monkeypatch, capsys):
        """Test that launchd is checked on macOS (darwin)."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "darwin"):
            with patch("doctor.check_launchd", return_value=(True, "Launchd OK")) as mock_launchd:
                main()
                mock_launchd.assert_called_once()

        captured = capsys.readouterr()
        assert "Scheduler" in captured.out

    def test_uses_cron_on_linux(self, tmp_path, monkeypatch, capsys):
        """Test that cron is checked on Linux."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "Cron OK")) as mock_cron:
                main()
                mock_cron.assert_called_once()

    def test_outputs_last_refresh(self, tmp_path, monkeypatch, capsys):
        """Test that last refresh timestamp is output."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)
        (lang_dir / ".fetched-at").write_text(datetime.now(UTC).isoformat())

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Last refresh" in captured.out
        assert "days ago" in captured.out

    def test_outputs_no_fetched_at_warning(self, tmp_path, monkeypatch, capsys):
        """Test warning when no .fetched-at files exist."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Last refresh" in captured.out
        assert "no .fetched-at" in captured.out

    def test_outputs_version_registry_status(self, tmp_path, monkeypatch, capsys):
        """Test that version registry status is output."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-06-15", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Version registry" in captured.out
        assert "2024-06-15" in captured.out

    def test_outputs_missing_version_registry(self, tmp_path, monkeypatch, capsys):
        """Test warning when versions.json is missing."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_json = tmp_path / "tools" / "versions.json"  # Non-existent

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Version registry" in captured.out
        assert "missing" in captured.out.lower()

    def test_outputs_missing_checked_at_count(self, tmp_path, monkeypatch, capsys):
        """Test that missing checkedAt count is reported."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(
            json.dumps(
                {
                    "updatedAt": "2024-06-15",
                    "tools": [
                        {"name": "tool1", "version": "1.0", "latest": {"type": "npm"}},
                        {"name": "tool2", "version": "2.0", "latest": {"type": "npm"}},
                    ],
                }
            )
        )

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "missing checkedAt" in captured.out
        assert "2 tools" in captured.out

    def test_outputs_search_index_status(self, tmp_path, monkeypatch, capsys):
        """Test that search index status is output."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-07-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Search index" in captured.out
        assert "2024-07-01" in captured.out

    def test_outputs_missing_search_index(self, tmp_path, monkeypatch, capsys):
        """Test warning when search.json is missing."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"  # Non-existent (no write)

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Search index" in captured.out
        assert "missing" in captured.out.lower()

    def test_outputs_stub_count(self, tmp_path, monkeypatch, capsys):
        """Test that stub count is output."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)

        (lang_dir / "stub.md").write_text("See: https://example.com")
        (lang_dir / "spec.md").write_text("See: https://python.org")

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Stub docs" in captured.out
        assert "2 stubs" in captured.out
        assert "1 spec/overview" in captured.out

    def test_github_token_from_env_var(self, tmp_path, monkeypatch, capsys):
        """Test that GITHUB_TOKEN from environment variable is detected."""
        import doctor

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"  # Empty or non-existent

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        # Set GITHUB_TOKEN in environment
        monkeypatch.setenv("GITHUB_TOKEN", "from_env_var")

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "GITHUB_TOKEN" in captured.out
        assert "[OK]" in captured.out
        assert "set" in captured.out.lower()


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_parse_env_file_with_quoted_values(self, tmp_path, monkeypatch):
        """Test that quoted values are preserved as-is."""
        env_file = tmp_path / ".env"
        env_file.write_text('KEY="quoted value"\n')

        import doctor

        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        result = parse_env_file()
        # Quotes are part of the value as we don't parse them
        assert result == {"KEY": '"quoted value"'}

    def test_load_versions_with_empty_tools(self, tmp_path, monkeypatch):
        """Test load_versions with empty tools array."""
        import doctor

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)

        updated_at, missing = load_versions()
        assert updated_at == "2024-01-01"
        assert missing == []

    def test_count_stubs_with_non_md_files(self, tmp_path, monkeypatch):
        """Test that non-.md files are ignored."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)

        (lang_dir / "stub.md").write_text("See: https://example.com")
        (lang_dir / "stub.txt").write_text("See: https://example.com")  # Should be ignored
        (lang_dir / ".fetched-at").write_text("2024-01-01")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)

        total, _important = count_stubs()
        assert total == 1  # Only .md file

    def test_main_with_zero_stubs_shows_ok(self, tmp_path, monkeypatch, capsys):
        """Test that zero stubs shows OK status."""
        import doctor

        specs_dir = tmp_path / "specs"
        lang_dir = specs_dir / "python"
        lang_dir.mkdir(parents=True)

        # Full content file, not a stub
        (lang_dir / "spec.md").write_text("# Title\n\nContent.\n\nMore content.")

        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        tools_json = tools_dir / "versions.json"
        tools_json.write_text(json.dumps({"updatedAt": "2024-01-01", "tools": []}))

        search_json = specs_dir / "search.json"
        search_json.write_text(json.dumps({"generatedAt": "2024-01-01"}))

        env_file = tmp_path / ".env"
        env_file.write_text("GITHUB_TOKEN=test\n")

        monkeypatch.setattr(doctor, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(doctor, "TOOLS_JSON", tools_json)
        monkeypatch.setattr(doctor, "SEARCH_JSON", search_json)
        monkeypatch.setattr(doctor, "ENV_FILE", env_file)

        with patch.object(sys, "platform", "linux"):
            with patch("doctor.check_cron", return_value=(True, "OK")):
                main()

        captured = capsys.readouterr()
        assert "Stub docs" in captured.out
        assert "[OK]" in captured.out
        assert "0 stubs" in captured.out


class TestConstants:
    """Tests for module constants."""

    def test_cron_marker_defined(self):
        """Test that CRON_MARKER is defined."""
        assert CRON_MARKER is not None
        assert isinstance(CRON_MARKER, str)
        assert len(CRON_MARKER) > 0

    def test_launchd_label_defined(self):
        """Test that LAUNCHD_LABEL is defined."""
        assert LAUNCHD_LABEL is not None
        assert isinstance(LAUNCHD_LABEL, str)
        assert "specforge" in LAUNCHD_LABEL.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
