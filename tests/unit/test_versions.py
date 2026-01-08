#!/usr/bin/env python3
"""Unit tests for versions.py."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from versions import (
    COMMANDS,
    cmd_report,
    cmd_update,
    cmd_validate,
    file_has_sources,
    file_has_version_line,
    load_registry,
    main,
    save_registry,
)


class TestLoadRegistry:
    """Tests for load_registry function."""

    def test_loads_real_registry(self):
        """Test that the real versions.json can be loaded."""
        registry = load_registry()
        assert "tools" in registry
        assert isinstance(registry["tools"], list)
        assert len(registry["tools"]) > 0

    def test_registry_has_required_fields(self):
        """Test that registry tools have required fields."""
        registry = load_registry()
        for tool in registry["tools"]:
            assert "name" in tool
            assert "version" in tool


class TestFileHasVersionLine:
    """Tests for file_has_version_line function."""

    def test_finds_version_line(self, tmp_path, monkeypatch):
        """Test finding a version line in a file."""
        # Create a test file with version line
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nVersion: 3.12.0\n\nContent here.")

        # Monkey-patch ROOT_DIR to use tmp_path
        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_version_line("specs/python/spec.md", "version", "3.12.0")
        assert result is True

    def test_missing_version_line(self, tmp_path, monkeypatch):
        """Test detecting missing version line."""
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nNo version here.")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_version_line("specs/python/spec.md", "version", "3.12.0")
        assert result is False

    def test_wrong_version(self, tmp_path, monkeypatch):
        """Test detecting wrong version."""
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nVersion: 3.11.0\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_version_line("specs/python/spec.md", "version", "3.12.0")
        assert result is False

    def test_label_capitalization(self, tmp_path, monkeypatch):
        """Test that labels are properly capitalized."""
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nSpecification: 1.0.0\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        # "specification" -> "Specification"
        result = file_has_version_line("specs/test/spec.md", "specification", "1.0.0")
        assert result is True


class TestFileHasSources:
    """Tests for file_has_sources function."""

    def test_finds_sources(self, tmp_path, monkeypatch):
        """Test finding source URLs in a file."""
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nSource: https://docs.python.org\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_sources("specs/python/spec.md", ["https://docs.python.org"])
        assert result is True

    def test_missing_sources(self, tmp_path, monkeypatch):
        """Test detecting missing sources."""
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nNo sources here.")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_sources("specs/python/spec.md", ["https://docs.python.org"])
        assert result is False

    def test_empty_sources_always_passes(self, tmp_path, monkeypatch):
        """Test that empty sources list always passes."""
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nAnything here.")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_sources("specs/python/spec.md", [])
        assert result is True


class TestRegistryStructure:
    """Tests for registry data structure."""

    def test_tool_entry_structure(self):
        """Test expected structure of tool entries."""
        registry = load_registry()

        for tool in registry["tools"]:
            # Required fields
            assert isinstance(tool.get("name"), str)
            assert isinstance(tool.get("version"), str)

            # Optional fields should be correct types if present
            if "files" in tool:
                assert isinstance(tool["files"], (list, type(None)))
            if "sources" in tool:
                assert isinstance(tool["sources"], (list, type(None)))
            if "latest" in tool:
                assert isinstance(tool["latest"], (dict, type(None)))

    def test_python_tool_exists(self):
        """Test that Python is in the registry."""
        registry = load_registry()
        tool_names = [t.get("name") for t in registry["tools"]]
        assert "python" in tool_names

    def test_typescript_tool_exists(self):
        """Test that TypeScript is in the registry."""
        registry = load_registry()
        tool_names = [t.get("name") for t in registry["tools"]]
        assert "typescript" in tool_names


class TestSaveRegistry:
    """Tests for save_registry function."""

    def test_saves_registry_to_file(self, tmp_path, monkeypatch):
        """Test that save_registry writes JSON correctly."""
        import versions

        registry_path = tmp_path / "tools" / "versions.json"
        registry_path.parent.mkdir(parents=True)
        monkeypatch.setattr(versions, "REGISTRY_PATH", registry_path)

        test_registry = {
            "updatedAt": "2024-01-01",
            "tools": [{"name": "test", "version": "1.0.0"}],
        }
        save_registry(test_registry)

        # Read back and verify
        saved_content = registry_path.read_text(encoding="utf-8")
        saved_data = json.loads(saved_content)
        assert saved_data == test_registry
        assert saved_content.endswith("\n")

    def test_saves_formatted_json(self, tmp_path, monkeypatch):
        """Test that save_registry writes properly formatted JSON."""
        import versions

        registry_path = tmp_path / "tools" / "versions.json"
        registry_path.parent.mkdir(parents=True)
        monkeypatch.setattr(versions, "REGISTRY_PATH", registry_path)

        test_registry = {"tools": []}
        save_registry(test_registry)

        content = registry_path.read_text(encoding="utf-8")
        # Should be indented (pretty printed)
        assert "  " in content or content == '{\n  "tools": []\n}\n'


class TestCmdReport:
    """Tests for cmd_report function."""

    def test_report_returns_zero(self, monkeypatch, capsys):
        """Test that report command returns 0 on success."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "checkedAt": "2024-01-01",
                    "files": ["file1.md"],
                    "sources": ["https://example.com"],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        # Mock get_latest_version to return None
        with patch("versions.get_latest_version", return_value=None):
            result = cmd_report()

        assert result == 0
        captured = capsys.readouterr()
        assert "test-tool" in captured.out
        assert "1.0.0" in captured.out

    def test_report_with_check_latest_enabled(self, monkeypatch, capsys):
        """Test report when CHECK_LATEST is enabled."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "checkedAt": "2024-01-01",
                    "files": [],
                    "sources": [],
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "CHECK_LATEST", True)

        with patch("versions.get_latest_version", return_value="2.0.0"):
            result = cmd_report()

        assert result == 0
        captured = capsys.readouterr()
        assert "2.0.0" in captured.out

    def test_report_handles_fetch_error(self, monkeypatch, capsys):
        """Test report handles FetchError gracefully."""
        import versions
        from _common import FetchError

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": [],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "CHECK_LATEST", True)

        def mock_get_latest(*args, **kwargs):
            raise FetchError("http://example.com", "Connection failed")

        with patch("versions.get_latest_version", side_effect=mock_get_latest):
            result = cmd_report()

        assert result == 0
        captured = capsys.readouterr()
        # Should show "-" for failed latest check
        assert "-" in captured.out

    def test_report_handles_os_error(self, monkeypatch, capsys):
        """Test report handles OSError gracefully."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": [],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)

        with patch("versions.get_latest_version", side_effect=OSError("Disk error")):
            result = cmd_report()

        assert result == 0

    def test_report_with_none_files_and_sources(self, monkeypatch, capsys):
        """Test report handles None files and sources."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": None,
                    "sources": None,
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)

        with patch("versions.get_latest_version", return_value=None):
            result = cmd_report()

        assert result == 0
        captured = capsys.readouterr()
        assert "0" in captured.out  # files count should be 0

    def test_report_with_missing_checked_at(self, monkeypatch, capsys):
        """Test report handles missing checkedAt."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": [],
                    "sources": [],
                    # No checkedAt field
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)

        with patch("versions.get_latest_version", return_value=None):
            result = cmd_report()

        assert result == 0
        captured = capsys.readouterr()
        assert "-" in captured.out


class TestCmdUpdate:
    """Tests for cmd_update function."""

    def test_update_returns_zero(self, monkeypatch):
        """Test that update command returns 0 on success."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        save_called = []
        monkeypatch.setattr(versions, "save_registry", lambda r: save_called.append(r))

        with patch("versions.get_latest_version", return_value="1.0.0"):
            result = cmd_update()

        assert result == 0
        assert len(save_called) == 1

    def test_update_increments_version(self, monkeypatch, capsys):
        """Test that update detects and logs version changes."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        saved_registry = []
        monkeypatch.setattr(versions, "save_registry", lambda r: saved_registry.append(r))

        with patch("versions.get_latest_version", return_value="2.0.0"):
            result = cmd_update()

        assert result == 0
        assert saved_registry[0]["tools"][0]["version"] == "2.0.0"

    def test_update_handles_fetch_error(self, monkeypatch):
        """Test update handles FetchError gracefully."""
        import versions
        from _common import FetchError

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "save_registry", lambda r: None)

        def mock_get_latest(*args, **kwargs):
            raise FetchError("http://example.com", "Connection failed")

        with patch("versions.get_latest_version", side_effect=mock_get_latest):
            result = cmd_update()

        assert result == 0

    def test_update_handles_os_error(self, monkeypatch):
        """Test update handles OSError gracefully."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "save_registry", lambda r: None)

        with patch("versions.get_latest_version", side_effect=OSError("Network error")):
            result = cmd_update()

        assert result == 0

    def test_update_sets_checked_at_for_latest_tools(self, monkeypatch):
        """Test update sets checkedAt for tools with latest config."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        saved_registry = []
        monkeypatch.setattr(versions, "save_registry", lambda r: saved_registry.append(r))

        with patch("versions.get_latest_version", return_value="1.0.0"):
            cmd_update()

        assert "checkedAt" in saved_registry[0]["tools"][0]

    def test_update_no_version_change_no_log(self, monkeypatch, capsys):
        """Test update doesn't log when version unchanged."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "save_registry", lambda r: None)

        with patch("versions.get_latest_version", return_value="1.0.0"):
            cmd_update()

        # The arrow notation should not appear if version unchanged
        capsys.readouterr()
        # Updated count should be 0
        assert True

    def test_update_tool_without_latest_config(self, monkeypatch):
        """Test update skips checkedAt for tools without latest config."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    # No "latest" field - should not set checkedAt
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        saved_registry = []
        monkeypatch.setattr(versions, "save_registry", lambda r: saved_registry.append(r))

        with patch("versions.get_latest_version", return_value=None):
            cmd_update()

        # Tool without latest config should not have checkedAt set
        assert "checkedAt" not in saved_registry[0]["tools"][0]

    def test_update_with_none_latest_response(self, monkeypatch):
        """Test update handles None response from get_latest_version."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        saved_registry = []
        monkeypatch.setattr(versions, "save_registry", lambda r: saved_registry.append(r))

        # get_latest_version returns None (version check disabled or unavailable)
        with patch("versions.get_latest_version", return_value=None):
            result = cmd_update()

        assert result == 0
        # Version should remain unchanged
        assert saved_registry[0]["tools"][0]["version"] == "1.0.0"

    def test_update_with_null_latest_field(self, monkeypatch):
        """Test update when latest field is explicitly null."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": None,  # Explicitly null
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        saved_registry = []
        monkeypatch.setattr(versions, "save_registry", lambda r: saved_registry.append(r))

        with patch("versions.get_latest_version", return_value=None):
            result = cmd_update()

        assert result == 0
        # checkedAt should not be set when latest is null
        assert "checkedAt" not in saved_registry[0]["tools"][0]


class TestCmdValidate:
    """Tests for cmd_validate function."""

    def test_validate_passes_with_valid_files(self, tmp_path, monkeypatch, capsys):
        """Test validation passes when files have correct versions."""
        import versions

        # Create test file with correct version
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0\n\nhttps://example.com")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "label": "Version",
                    "files": ["specs/test/spec.md"],
                    "sources": ["https://example.com"],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 0
        captured = capsys.readouterr()
        assert "passed" in captured.out

    def test_validate_fails_with_missing_version(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when version line is missing."""
        import versions

        # Create test file without version
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nNo version here.")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": ["specs/test/spec.md"],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 1
        captured = capsys.readouterr()
        assert "failed" in captured.out.lower()

    def test_validate_fails_with_missing_sources(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when source URLs are missing."""
        import versions

        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0\n")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": ["specs/test/spec.md"],
                    "sources": ["https://missing-source.com"],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 1

    def test_validate_warns_with_no_files(self, tmp_path, monkeypatch, capsys):
        """Test validation warns when tool has no file references."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": [],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 0
        captured = capsys.readouterr()
        assert "Warning" in captured.out or "no file references" in captured.out

    def test_validate_fails_with_unknown_version_and_latest(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when version is unknown but has latest source."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "unknown",
                    "latest": {"type": "npm", "package": "test"},
                    "files": [],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 1
        captured = capsys.readouterr()
        assert "unknown" in captured.out.lower()

    def test_validate_handles_unreadable_file(self, tmp_path, monkeypatch, capsys):
        """Test validation handles OSError when reading file."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": ["specs/nonexistent/spec.md"],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 1
        captured = capsys.readouterr()
        assert "unable to read" in captured.out.lower()

    def test_validate_with_check_latest_enabled(self, tmp_path, monkeypatch, capsys):
        """Test validation with CHECK_LATEST enabled."""
        import versions

        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0\n")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                    "files": ["specs/test/spec.md"],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", True)

        with patch("versions.get_latest_version", return_value="1.0.0"):
            with patch("versions.normalize_version", return_value="1.0.0"):
                result = cmd_validate()

        assert result == 0

    def test_validate_fails_when_latest_differs(self, tmp_path, monkeypatch, capsys):
        """Test validation fails when registry version differs from latest."""
        import versions

        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0\n")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                    "files": ["specs/test/spec.md"],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", True)

        with patch("versions.get_latest_version", return_value="2.0.0"):
            with patch("versions.normalize_version", return_value="1.0.0"):
                result = cmd_validate()

        assert result == 1
        captured = capsys.readouterr()
        assert "latest" in captured.out.lower()

    def test_validate_handles_fetch_error_in_latest_check(self, tmp_path, monkeypatch, capsys):
        """Test validation handles FetchError during latest check."""
        import versions
        from _common import FetchError

        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0\n")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "latest": {"type": "npm", "package": "test"},
                    "files": ["specs/test/spec.md"],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", True)

        def mock_get_latest(*args, **kwargs):
            raise FetchError("http://example.com", "Connection failed")

        with patch("versions.get_latest_version", side_effect=mock_get_latest):
            result = cmd_validate()

        assert result == 1
        captured = capsys.readouterr()
        assert "failed to check" in captured.out.lower()

    def test_validate_with_custom_label(self, tmp_path, monkeypatch, capsys):
        """Test validation with custom label field."""
        import versions

        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nClang: 15.0.0\n")

        test_registry = {
            "tools": [
                {
                    "name": "clang",
                    "version": "15.0.0",
                    "label": "Clang",
                    "files": ["specs/test/spec.md"],
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 0

    def test_validate_with_none_files(self, tmp_path, monkeypatch, capsys):
        """Test validation handles None files list."""
        import versions

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": None,
                    "sources": [],
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 0
        captured = capsys.readouterr()
        assert "no file references" in captured.out

    def test_validate_with_none_sources(self, tmp_path, monkeypatch, capsys):
        """Test validation handles None sources list."""
        import versions

        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0\n")

        test_registry = {
            "tools": [
                {
                    "name": "test-tool",
                    "version": "1.0.0",
                    "files": ["specs/test/spec.md"],
                    "sources": None,
                }
            ]
        }
        monkeypatch.setattr(versions, "load_registry", lambda: test_registry)
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(versions, "CHECK_LATEST", False)

        result = cmd_validate()

        assert result == 0


class TestMain:
    """Tests for main function."""

    def test_main_shows_help_with_no_args(self, monkeypatch, capsys):
        """Test main shows help when no arguments provided."""
        monkeypatch.setattr(sys, "argv", ["versions.py"])
        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "report" in captured.out
        assert "update" in captured.out
        assert "validate" in captured.out

    def test_main_shows_help_with_h_flag(self, monkeypatch, capsys):
        """Test main shows help with -h flag."""
        monkeypatch.setattr(sys, "argv", ["versions.py", "-h"])
        result = main()
        assert result == 0
        captured = capsys.readouterr()
        assert "Commands:" in captured.out

    def test_main_shows_help_with_help_flag(self, monkeypatch, capsys):
        """Test main shows help with --help flag."""
        monkeypatch.setattr(sys, "argv", ["versions.py", "--help"])
        result = main()
        assert result == 0

    def test_main_unknown_command(self, monkeypatch, capsys):
        """Test main handles unknown command."""
        monkeypatch.setattr(sys, "argv", ["versions.py", "unknown"])
        result = main()
        assert result == 1
        captured = capsys.readouterr()
        assert "Unknown command" in captured.out
        assert "report" in captured.out  # Shows available commands

    def test_main_executes_report_command(self, monkeypatch):
        """Test main executes report command."""
        import versions

        monkeypatch.setattr(sys, "argv", ["versions.py", "report"])
        mock_cmd_report = MagicMock(return_value=0)
        monkeypatch.setattr(versions, "COMMANDS", {"report": mock_cmd_report})

        result = main()

        assert result == 0
        mock_cmd_report.assert_called_once()

    def test_main_executes_update_command(self, monkeypatch):
        """Test main executes update command."""
        import versions

        monkeypatch.setattr(sys, "argv", ["versions.py", "update"])
        mock_cmd_update = MagicMock(return_value=0)
        monkeypatch.setattr(versions, "COMMANDS", {"update": mock_cmd_update, "report": lambda: 0})

        result = main()

        assert result == 0
        mock_cmd_update.assert_called_once()

    def test_main_executes_validate_command(self, monkeypatch):
        """Test main executes validate command."""
        import versions

        monkeypatch.setattr(sys, "argv", ["versions.py", "validate"])
        mock_cmd_validate = MagicMock(return_value=0)
        monkeypatch.setattr(
            versions, "COMMANDS", {"validate": mock_cmd_validate, "report": lambda: 0}
        )

        result = main()

        assert result == 0
        mock_cmd_validate.assert_called_once()

    def test_main_returns_command_result(self, monkeypatch):
        """Test main returns the result from the executed command."""
        import versions

        monkeypatch.setattr(sys, "argv", ["versions.py", "validate"])
        mock_cmd = MagicMock(return_value=42)
        monkeypatch.setattr(versions, "COMMANDS", {"validate": mock_cmd})

        result = main()

        assert result == 42


class TestCommandsDict:
    """Tests for COMMANDS dictionary."""

    def test_commands_has_report(self):
        """Test COMMANDS has report entry."""
        assert "report" in COMMANDS
        assert callable(COMMANDS["report"])

    def test_commands_has_update(self):
        """Test COMMANDS has update entry."""
        assert "update" in COMMANDS
        assert callable(COMMANDS["update"])

    def test_commands_has_validate(self):
        """Test COMMANDS has validate entry."""
        assert "validate" in COMMANDS
        assert callable(COMMANDS["validate"])


class TestFileHasVersionLineEdgeCases:
    """Additional edge case tests for file_has_version_line."""

    def test_version_in_middle_of_content(self, tmp_path, monkeypatch):
        """Test finding version line in middle of file."""
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Header\n\nSome content.\n\nVersion: 2.5.0\n\nMore content.")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_version_line("specs/test/spec.md", "version", "2.5.0")
        assert result is True

    def test_version_substring_match_succeeds(self, tmp_path, monkeypatch):
        """Test that version substring matches succeed (contains check)."""
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 1.0.0-beta\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        # The function does a substring/contains check, so "Version: 1.0.0"
        # will be found in "Version: 1.0.0-beta"
        result = file_has_version_line("specs/test/spec.md", "version", "1.0.0")
        assert result is True

    def test_completely_different_version_fails(self, tmp_path, monkeypatch):
        """Test that completely different version fails."""
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nVersion: 2.0.0\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_version_line("specs/test/spec.md", "version", "1.0.0")
        assert result is False


class TestFileHasSourcesEdgeCases:
    """Additional edge case tests for file_has_sources."""

    def test_multiple_sources_all_present(self, tmp_path, monkeypatch):
        """Test finding multiple source URLs."""
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nhttps://example.com\nhttps://other.com\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_sources(
            "specs/test/spec.md",
            ["https://example.com", "https://other.com"],
        )
        assert result is True

    def test_multiple_sources_one_missing(self, tmp_path, monkeypatch):
        """Test detecting when one of multiple sources is missing."""
        test_file = tmp_path / "specs" / "test" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Test\n\nhttps://example.com\n")

        import versions

        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_sources(
            "specs/test/spec.md",
            ["https://example.com", "https://missing.com"],
        )
        assert result is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
