#!/usr/bin/env python3
"""Unit tests for versions.py."""

import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from versions import (
    load_registry,
    file_has_version_line,
    file_has_sources,
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

        result = file_has_sources(
            "specs/python/spec.md",
            ["https://docs.python.org"]
        )
        assert result is True

    def test_missing_sources(self, tmp_path, monkeypatch):
        """Test detecting missing sources."""
        test_file = tmp_path / "specs" / "python" / "spec.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("# Python\n\nNo sources here.")

        import versions
        monkeypatch.setattr(versions, "ROOT_DIR", tmp_path)

        result = file_has_sources(
            "specs/python/spec.md",
            ["https://docs.python.org"]
        )
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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
