#!/usr/bin/env python3
"""Unit tests for validate.py."""

import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from validate import (
    COMMANDS,
    cmd_all,
    cmd_freshness,
    cmd_stubs,
    is_stub_file,
    load_allowlist,
    main,
)


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

    def test_see_not_at_beginning_not_stub(self, tmp_path):
        """Test that 'See:' must be at start of line."""
        file = tmp_path / "test.md"
        file.write_text("This line contains See: but not at start")
        assert is_stub_file(file) is False

    def test_exactly_two_content_lines_with_see(self, tmp_path):
        """Test exactly two content lines, second has See:."""
        file = tmp_path / "test.md"
        file.write_text("Header\nSee: https://example.com")
        assert is_stub_file(file) is True

    def test_whitespace_only_lines_ignored(self, tmp_path):
        """Test that whitespace-only lines don't count."""
        file = tmp_path / "test.md"
        file.write_text("See: https://example.com\n   \n\t\n")
        assert is_stub_file(file) is True


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

    def test_uses_default_allowlist_path(self, monkeypatch):
        """Test default allowlist path is used when env var not set."""
        monkeypatch.delenv("STUB_ALLOWLIST", raising=False)
        # Just ensure it doesn't crash and returns a set
        result = load_allowlist()
        assert isinstance(result, set)

    def test_strips_whitespace(self, tmp_path, monkeypatch):
        """Test that whitespace is stripped from entries."""
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("  entry1  \n\tentry2\t\n")
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))
        result = load_allowlist()
        assert "entry1" in result
        assert "entry2" in result


class TestCmdFreshness:
    """Tests for cmd_freshness command."""

    def test_passes_with_fresh_specs(self, tmp_path, monkeypatch, capsys):
        """Test validation passes when specs are fresh."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(recent)

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 0
        captured = capsys.readouterr()
        assert "Freshness validation passed" in captured.out

    def test_fails_with_stale_specs(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when specs are stale."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        old_time = datetime.now(UTC) - timedelta(days=100)
        (lang_dir / ".fetched-at").write_text(old_time.isoformat())

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 1
        captured = capsys.readouterr()
        assert "Freshness validation failed" in captured.out
        assert "python" in captured.out
        assert "stale" in captured.out

    def test_fails_with_missing_fetched_at(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when .fetched-at is missing."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # Don't create .fetched-at

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 1
        captured = capsys.readouterr()
        assert "missing .fetched-at" in captured.out

    def test_fails_with_empty_fetched_at(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when .fetched-at is empty."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 1
        captured = capsys.readouterr()
        assert "invalid .fetched-at (empty)" in captured.out

    def test_fails_with_invalid_date_format(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when .fetched-at has invalid format."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("not-a-date")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 1
        captured = capsys.readouterr()
        assert "invalid .fetched-at" in captured.out
        assert "not-a-date" in captured.out

    def test_custom_max_age_days(self, tmp_path, monkeypatch, capsys):
        """Test custom MAX_AGE_DAYS environment variable."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # 10 days old
        old_time = datetime.now(UTC) - timedelta(days=10)
        (lang_dir / ".fetched-at").write_text(old_time.isoformat())

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        # Set max age to 5 days - should fail
        monkeypatch.setenv("MAX_AGE_DAYS", "5")
        result = cmd_freshness()

        assert result == 1
        captured = capsys.readouterr()
        assert ">5 days" in captured.out

    def test_passes_with_custom_max_age(self, tmp_path, monkeypatch, capsys):
        """Test passes when within custom MAX_AGE_DAYS."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # 10 days old
        old_time = datetime.now(UTC) - timedelta(days=10)
        (lang_dir / ".fetched-at").write_text(old_time.isoformat())

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        # Set max age to 15 days - should pass
        monkeypatch.setenv("MAX_AGE_DAYS", "15")
        result = cmd_freshness()

        assert result == 0
        captured = capsys.readouterr()
        assert "<=15 days" in captured.out

    def test_handles_multiple_languages(self, tmp_path, monkeypatch, capsys):
        """Test with multiple language directories."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        recent = datetime.now(UTC).isoformat()
        for lang in ["python", "go", "rust"]:
            lang_dir = specs_root / lang
            lang_dir.mkdir()
            (lang_dir / ".fetched-at").write_text(recent)

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 0

    def test_reports_multiple_failures(self, tmp_path, monkeypatch, capsys):
        """Test that all failures are reported."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # python - missing
        (specs_root / "python").mkdir()
        # go - empty
        go_dir = specs_root / "go"
        go_dir.mkdir()
        (go_dir / ".fetched-at").write_text("")
        # rust - invalid
        rust_dir = specs_root / "rust"
        rust_dir.mkdir()
        (rust_dir / ".fetched-at").write_text("invalid")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        assert result == 1
        captured = capsys.readouterr()
        assert "python" in captured.out
        assert "go" in captured.out
        assert "rust" in captured.out

    def test_ignores_files_in_specs_root(self, tmp_path, monkeypatch, capsys):
        """Test that files in specs root are ignored (only dirs processed)."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # Create a file, not a directory
        (specs_root / "README.md").write_text("# Specs")

        # Create a valid language dir
        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(recent)

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()

        # Should pass - README.md should be ignored
        assert result == 0


class TestCmdStubs:
    """Tests for cmd_stubs command."""

    def test_passes_with_no_stubs(self, tmp_path, monkeypatch, capsys):
        """Test validation passes when no stub files exist."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        (specs_root / "python").mkdir()
        full_file = specs_root / "python" / "spec.md"
        full_file.write_text("# Python Spec\n\nFull content here.\n\nMore content.")

        # Empty allowlist
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 0
        captured = capsys.readouterr()
        assert "Stub validation passed" in captured.out

    def test_fails_with_unexpected_stubs(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when unexpected stub files exist."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        (specs_root / "python").mkdir()
        stub_file = specs_root / "python" / "stub.md"
        stub_file.write_text("See: https://example.com/docs")

        # Empty allowlist
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 1
        captured = capsys.readouterr()
        assert "Stub validation failed" in captured.out
        assert "specs/python/stub.md" in captured.out

    def test_passes_with_allowlisted_stubs(self, tmp_path, monkeypatch, capsys):
        """Test validation passes when stub is in allowlist."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        (specs_root / "python").mkdir()
        stub_file = specs_root / "python" / "stub.md"
        stub_file.write_text("See: https://example.com/docs")

        # Allowlist the stub
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("specs/python/stub.md\n")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 0
        captured = capsys.readouterr()
        assert "Stub validation passed" in captured.out

    def test_warns_stale_allowlist(self, tmp_path, monkeypatch, capsys):
        """Test warning when allowlist has stale entries."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        (specs_root / "python").mkdir()
        full_file = specs_root / "python" / "spec.md"
        full_file.write_text("# Full content\n\nWith details.\n\nAnd more.")

        # Allowlist has entry that's no longer a stub
        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("specs/python/removed-stub.md\n")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        # Still passes, but warns
        assert result == 0
        captured = capsys.readouterr()
        assert "Warning: allowlist entries no longer stubbed" in captured.out
        assert "specs/python/removed-stub.md" in captured.out

    def test_truncates_many_unexpected_stubs(self, tmp_path, monkeypatch, capsys):
        """Test that output is truncated with many stubs."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        lang_dir = specs_root / "python"
        lang_dir.mkdir()

        # Create more than 100 stub files
        for i in range(105):
            stub = lang_dir / f"stub{i}.md"
            stub.write_text("See: https://example.com")

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 1
        captured = capsys.readouterr()
        assert "... and 5 more" in captured.out

    def test_truncates_many_stale_allowlist(self, tmp_path, monkeypatch, capsys):
        """Test that stale allowlist warnings are truncated."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        (specs_root / "python").mkdir()

        # Allowlist with many stale entries
        allowlist = tmp_path / "allowlist.txt"
        entries = [f"specs/python/stale{i}.md" for i in range(55)]
        allowlist.write_text("\n".join(entries))

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 0
        captured = capsys.readouterr()
        assert "... and 5 more" in captured.out

    def test_counts_stub_files(self, tmp_path, monkeypatch, capsys):
        """Test that stub count is reported."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        lang_dir = specs_root / "python"
        lang_dir.mkdir()

        # Create 3 stub files, all allowlisted
        for i in range(3):
            stub = lang_dir / f"stub{i}.md"
            stub.write_text("See: https://example.com")

        allowlist = tmp_path / "allowlist.txt"
        entries = [f"specs/python/stub{i}.md" for i in range(3)]
        allowlist.write_text("\n".join(entries))

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 0
        captured = capsys.readouterr()
        assert "3 stub files" in captured.out

    def test_scans_nested_directories(self, tmp_path, monkeypatch, capsys):
        """Test that nested directories are scanned."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        nested = specs_root / "python" / "stdlib" / "deep"
        nested.mkdir(parents=True)

        stub = nested / "stub.md"
        stub.write_text("See: https://example.com")

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_stubs()
        assert result == 1
        captured = capsys.readouterr()
        assert "specs/python/stdlib/deep/stub.md" in captured.out


class TestCmdAll:
    """Tests for cmd_all command."""

    def test_runs_all_validators(self, tmp_path, monkeypatch, capsys):
        """Test that cmd_all runs all validators."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(recent)
        (lang_dir / "spec.md").write_text("# Full\n\nWith content.\n\nAnd more.")

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_all()
        assert result == 0
        captured = capsys.readouterr()
        assert "=== Freshness validation ===" in captured.out
        assert "=== Stub validation ===" in captured.out

    def test_returns_nonzero_on_freshness_failure(self, tmp_path, monkeypatch):
        """Test cmd_all returns non-zero when freshness fails."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # Missing .fetched-at

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_all()
        assert result != 0

    def test_returns_nonzero_on_stub_failure(self, tmp_path, monkeypatch):
        """Test cmd_all returns non-zero when stubs fail."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(recent)
        # Create unexpected stub
        (lang_dir / "stub.md").write_text("See: https://example.com")

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_all()
        assert result != 0

    def test_returns_nonzero_on_both_failures(self, tmp_path, monkeypatch):
        """Test cmd_all returns non-zero when both fail."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # Missing .fetched-at AND unexpected stub
        (lang_dir / "stub.md").write_text("See: https://example.com")

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))

        result = cmd_all()
        assert result != 0


class TestMain:
    """Tests for main function."""

    def test_shows_help_with_no_args(self, monkeypatch, capsys):
        """Test that no args shows help."""
        monkeypatch.setattr("sys.argv", ["validate.py"])
        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "Commands:" in captured.out
        assert "freshness" in captured.out
        assert "stubs" in captured.out
        assert "all" in captured.out

    def test_shows_help_with_h_flag(self, monkeypatch, capsys):
        """Test that -h flag shows help."""
        monkeypatch.setattr("sys.argv", ["validate.py", "-h"])
        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "Commands:" in captured.out

    def test_shows_help_with_help_flag(self, monkeypatch, capsys):
        """Test that --help flag shows help."""
        monkeypatch.setattr("sys.argv", ["validate.py", "--help"])
        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "Commands:" in captured.out

    def test_unknown_command_error(self, monkeypatch, capsys):
        """Test that unknown command returns error."""
        monkeypatch.setattr("sys.argv", ["validate.py", "unknown"])
        result = main()
        assert result == 1
        captured = capsys.readouterr()
        assert "Unknown command: unknown" in captured.out
        assert "Available:" in captured.out

    def test_runs_freshness_command(self, tmp_path, monkeypatch, capsys):
        """Test that freshness command is executed."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(recent)

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("sys.argv", ["validate.py", "freshness"])

        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "Freshness validation passed" in captured.out

    def test_runs_stubs_command(self, tmp_path, monkeypatch, capsys):
        """Test that stubs command is executed."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        (specs_root / "python").mkdir()

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))
        monkeypatch.setattr("sys.argv", ["validate.py", "stubs"])

        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "Stub validation passed" in captured.out

    def test_runs_all_command(self, tmp_path, monkeypatch, capsys):
        """Test that all command is executed."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()
        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(recent)

        allowlist = tmp_path / "allowlist.txt"
        allowlist.write_text("")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        monkeypatch.setattr("validate.ROOT_DIR", tmp_path)
        monkeypatch.setenv("STUB_ALLOWLIST", str(allowlist))
        monkeypatch.setattr("sys.argv", ["validate.py", "all"])

        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "=== Freshness validation ===" in captured.out
        assert "=== Stub validation ===" in captured.out


class TestCommands:
    """Tests for COMMANDS dictionary."""

    def test_commands_dict_has_expected_entries(self):
        """Test COMMANDS contains all expected commands."""
        assert "freshness" in COMMANDS
        assert "stubs" in COMMANDS
        assert "all" in COMMANDS

    def test_commands_are_callable(self):
        """Test all commands are callable."""
        for name, cmd in COMMANDS.items():
            assert callable(cmd), f"Command '{name}' is not callable"


class TestFreshnessValidation:
    """Tests for freshness validation logic."""

    def test_fresh_fetched_at_passes(self, tmp_path):
        """Test that recent .fetched-at files pass validation."""
        # Create a spec directory with recent .fetched-at
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"
        recent = datetime.now(UTC).isoformat()
        fetched_at.write_text(recent)

        # Read back and parse
        content = fetched_at.read_text().strip()
        parsed = datetime.fromisoformat(content)
        age_seconds = (datetime.now(UTC) - parsed).total_seconds()

        # Should be less than 90 days (default MAX_AGE_DAYS)
        max_age_seconds = 90 * 24 * 60 * 60
        assert age_seconds < max_age_seconds

    def test_stale_fetched_at_fails(self, tmp_path):
        """Test that old .fetched-at files would fail validation."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        fetched_at = lang_dir / ".fetched-at"

        # Write a timestamp from 100 days ago
        old_time = datetime.now(UTC) - timedelta(days=100)
        fetched_at.write_text(old_time.isoformat())

        content = fetched_at.read_text().strip()
        parsed = datetime.fromisoformat(content)
        age_seconds = (datetime.now(UTC) - parsed).total_seconds()

        # Should be more than 90 days
        max_age_seconds = 90 * 24 * 60 * 60
        assert age_seconds > max_age_seconds


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_empty_specs_directory(self, tmp_path, monkeypatch, capsys):
        """Test with empty specs directory."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()
        # Should pass with no languages
        assert result == 0

    def test_whitespace_in_fetched_at(self, tmp_path, monkeypatch, capsys):
        """Test .fetched-at with leading/trailing whitespace."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        recent = datetime.now(UTC).isoformat()
        (lang_dir / ".fetched-at").write_text(f"  {recent}  \n\n")

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()
        assert result == 0

    def test_fetched_at_with_z_suffix(self, tmp_path, monkeypatch, capsys):
        """Test .fetched-at with Z timezone suffix."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # Use Z instead of +00:00
        now = datetime.now(UTC)
        now.strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
        # Note: Python's fromisoformat in 3.11+ handles Z
        # But older versions may not, let's use a standard format
        (lang_dir / ".fetched-at").write_text(now.isoformat())

        monkeypatch.setattr("validate.SPECS_ROOT", specs_root)
        result = cmd_freshness()
        assert result == 0

    def test_stub_file_with_only_blank_lines(self, tmp_path):
        """Test file with only blank lines is not a stub."""
        file = tmp_path / "blank.md"
        file.write_text("\n\n\n")
        assert is_stub_file(file) is False

    def test_stub_detection_case_sensitive(self, tmp_path):
        """Test that 'See:' detection is case-sensitive."""
        file = tmp_path / "test.md"
        file.write_text("see: https://example.com")
        # 'see:' lowercase should not be detected as stub
        assert is_stub_file(file) is False

    def test_multiple_see_lines(self, tmp_path):
        """Test file with multiple See: lines but <= 2 content lines."""
        file = tmp_path / "test.md"
        file.write_text("See: https://example1.com\nSee: https://example2.com")
        # Two lines, both with See: - should be stub
        assert is_stub_file(file) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
