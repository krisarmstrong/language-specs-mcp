#!/usr/bin/env python3
"""Unit tests for refresh.py."""

import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from refresh import COMMANDS, ROOT_DIR, URL_VALIDATION_COMMANDS, main, run


class TestRun:
    """Tests for run function."""

    def test_run_executes_command(self):
        """Test run executes subprocess.run with correct args."""
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            run(["npm", "run", "test"])
            mock_run.assert_called_once_with(["npm", "run", "test"], check=True, cwd=ROOT_DIR)

    def test_run_uses_root_dir_as_cwd(self):
        """Test run uses ROOT_DIR as working directory."""
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            run(["echo", "hello"])
            _, kwargs = mock_run.call_args
            assert kwargs["cwd"] == ROOT_DIR

    def test_run_propagates_exception(self):
        """Test run raises CalledProcessError on failure."""
        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, "npm")
            with pytest.raises(subprocess.CalledProcessError):
                run(["npm", "run", "fail"])

    def test_run_prints_command(self, capsys):
        """Test run prints the command being executed."""
        with patch("subprocess.run"):
            run(["npm", "run", "test:unit"])
        captured = capsys.readouterr()
        assert "Running: npm run test:unit" in captured.out


class TestMainDefaultFlow:
    """Tests for main function default execution flow."""

    def test_main_runs_all_commands(self, monkeypatch, capsys):
        """Test main runs all default commands."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 0
        assert ["npm", "run", "fetch:delta"] in executed_commands
        assert ["npm", "run", "update:versions"] in executed_commands
        assert ["npm", "run", "stamp:versions"] in executed_commands
        assert ["npm", "run", "generate:all"] in executed_commands
        captured = capsys.readouterr()
        assert "Refresh completed." in captured.out

    def test_main_stops_on_failure(self, monkeypatch):
        """Test main stops execution when a command fails."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        call_count = 0

        def mock_run(cmd, check, cwd):
            nonlocal call_count
            call_count += 1
            if call_count == 2:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 1
        # Should have stopped after 2 calls
        assert call_count == 2

    def test_main_returns_error_code(self, monkeypatch):
        """Test main returns the error code from failed command."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        def mock_run(cmd, check, cwd):
            error = subprocess.CalledProcessError(42, cmd)
            error.returncode = 42
            raise error

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 42

    def test_main_returns_1_when_returncode_is_none(self, monkeypatch):
        """Test main returns 1 when CalledProcessError has no returncode."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        def mock_run(cmd, check, cwd):
            error = subprocess.CalledProcessError(0, cmd)
            error.returncode = 0  # This evaluates to falsy
            raise error

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        # Should return 1 when error.returncode is falsy
        assert result == 1


class TestSkipFetch:
    """Tests for SKIP_FETCH environment variable."""

    def test_skip_fetch_skips_fetch_command(self, monkeypatch, capsys):
        """Test SKIP_FETCH=1 skips the fetch:delta command."""
        monkeypatch.setenv("SKIP_FETCH", "1")
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 0
        assert ["npm", "run", "fetch:delta"] not in executed_commands
        assert ["npm", "run", "update:versions"] in executed_commands
        assert ["npm", "run", "stamp:versions"] in executed_commands
        assert ["npm", "run", "generate:all"] in executed_commands

        captured = capsys.readouterr()
        assert "Skipping fetch (SKIP_FETCH=1)" in captured.out

    def test_skip_fetch_other_values_do_not_skip(self, monkeypatch):
        """Test SKIP_FETCH with non-1 values does not skip."""
        monkeypatch.setenv("SKIP_FETCH", "true")
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        assert ["npm", "run", "fetch:delta"] in executed_commands


class TestValidateUrls:
    """Tests for VALIDATE_URLS environment variable."""

    def test_validate_urls_adds_validation_commands(self, monkeypatch, capsys):
        """Test VALIDATE_URLS=1 adds URL validation commands."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "1")

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 0
        assert ["npm", "run", "validate:urls"] in executed_commands
        assert ["npm", "run", "fix:urls"] in executed_commands
        assert ["npm", "run", "generate:health"] in executed_commands

        captured = capsys.readouterr()
        assert "URL validation enabled (VALIDATE_URLS=1)" in captured.out

    def test_validate_urls_failure_continues(self, monkeypatch, capsys):
        """Test URL validation failures don't stop refresh."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "1")

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            if "validate:urls" in cmd or "fix:urls" in cmd:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        # Should succeed despite URL validation errors
        assert result == 0
        assert ["npm", "run", "validate:urls"] in executed_commands
        assert ["npm", "run", "fix:urls"] in executed_commands
        assert ["npm", "run", "generate:health"] in executed_commands

        captured = capsys.readouterr()
        assert "URL validation error - continuing with refresh" in captured.err

    def test_validate_urls_other_values_do_not_validate(self, monkeypatch):
        """Test VALIDATE_URLS with non-1 values does not add validation."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "true")

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        assert ["npm", "run", "validate:urls"] not in executed_commands


class TestCombinedFlags:
    """Tests for combined environment variable scenarios."""

    def test_skip_fetch_with_validate_urls(self, monkeypatch, capsys):
        """Test SKIP_FETCH=1 and VALIDATE_URLS=1 together."""
        monkeypatch.setenv("SKIP_FETCH", "1")
        monkeypatch.setenv("VALIDATE_URLS", "1")

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 0
        # Fetch should be skipped
        assert ["npm", "run", "fetch:delta"] not in executed_commands
        # Validation should still run
        assert ["npm", "run", "validate:urls"] in executed_commands
        assert ["npm", "run", "fix:urls"] in executed_commands
        # Generate commands should run
        assert ["npm", "run", "update:versions"] in executed_commands
        assert ["npm", "run", "generate:health"] in executed_commands

        captured = capsys.readouterr()
        assert "Skipping fetch (SKIP_FETCH=1)" in captured.out
        assert "URL validation enabled (VALIDATE_URLS=1)" in captured.out


class TestCommandOrder:
    """Tests for command execution order."""

    def test_commands_execute_in_order(self, monkeypatch):
        """Test commands execute in correct order."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        # Verify order
        assert executed_commands[0] == ["npm", "run", "fetch:delta"]
        assert executed_commands[1] == ["npm", "run", "update:versions"]
        assert executed_commands[2] == ["npm", "run", "stamp:versions"]
        assert executed_commands[3] == ["npm", "run", "generate:all"]

    def test_validate_urls_commands_after_core(self, monkeypatch):
        """Test URL validation commands run after core commands."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "1")

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        # Find indices
        generate_all_idx = executed_commands.index(["npm", "run", "generate:all"])
        validate_urls_idx = executed_commands.index(["npm", "run", "validate:urls"])

        # URL validation should come after generate:all
        assert validate_urls_idx > generate_all_idx


class TestConstants:
    """Tests for module constants."""

    def test_commands_list_content(self):
        """Test COMMANDS list contains expected commands."""
        assert COMMANDS == [
            ["npm", "run", "fetch:delta"],
            ["npm", "run", "update:versions"],
            ["npm", "run", "stamp:versions"],
            ["npm", "run", "generate:all"],
        ]

    def test_url_validation_commands_content(self):
        """Test URL_VALIDATION_COMMANDS list contains expected commands."""
        assert URL_VALIDATION_COMMANDS == [
            ["npm", "run", "validate:urls"],
            ["npm", "run", "fix:urls"],
        ]

    def test_root_dir_is_project_root(self):
        """Test ROOT_DIR points to project root."""
        assert ROOT_DIR.is_dir()
        assert (ROOT_DIR / "package.json").exists()


class TestErrorMessages:
    """Tests for error message output."""

    def test_failed_command_prints_error(self, monkeypatch, capsys):
        """Test failed command prints error message with command."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        def mock_run(cmd, check, cwd):
            raise subprocess.CalledProcessError(1, cmd)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        captured = capsys.readouterr()
        assert "Command failed (npm run fetch:delta)" in captured.err

    def test_url_validation_error_prints_warning(self, monkeypatch, capsys):
        """Test URL validation error prints warning."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "1")

        call_count = 0

        def mock_run(cmd, check, cwd):
            nonlocal call_count
            call_count += 1
            if "validate:urls" in cmd:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        captured = capsys.readouterr()
        assert "URL validation error - continuing with refresh" in captured.err


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_empty_environment(self, monkeypatch):
        """Test with no environment variables set."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.delenv("VALIDATE_URLS", raising=False)

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        assert result == 0
        assert len(executed_commands) == 4

    def test_fix_urls_failure_continues(self, monkeypatch, capsys):
        """Test fix:urls failure continues execution."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "1")

        def mock_run(cmd, check, cwd):
            if "fix:urls" in cmd:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            result = main()

        # Should succeed - fix:urls is a URL validation command
        assert result == 0

    def test_generate_health_runs_after_url_validation(self, monkeypatch):
        """Test generate:health runs last when URL validation enabled."""
        monkeypatch.delenv("SKIP_FETCH", raising=False)
        monkeypatch.setenv("VALIDATE_URLS", "1")

        executed_commands = []

        def mock_run(cmd, check, cwd):
            executed_commands.append(cmd)
            return MagicMock(returncode=0)

        with patch("subprocess.run", side_effect=mock_run):
            main()

        # generate:health should be the last command
        assert executed_commands[-1] == ["npm", "run", "generate:health"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
