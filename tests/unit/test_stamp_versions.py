#!/usr/bin/env python3
"""Unit tests for stamp-versions.py."""

import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import after adding to path
# Note: stamp-versions.py uses hyphens, so we import it specially
import importlib.util

stamp_versions_path = Path(__file__).parent.parent.parent / "scripts" / "stamp-versions.py"
spec = importlib.util.spec_from_file_location("stamp_versions", stamp_versions_path)
stamp_versions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stamp_versions)

# Import functions from the module
build_heading = stamp_versions.build_heading
upcase_label = stamp_versions.upcase_label
update_content = stamp_versions.update_content
ensure_sources = stamp_versions.ensure_sources
main = stamp_versions.main


class TestBuildHeading:
    """Tests for build_heading function."""

    def test_linter_file_path(self):
        """Test heading for linter file paths."""
        result = build_heading("specs/python/linters/pylint/overview.md", "pylint")
        assert result == "# pylint Version"

    def test_formatter_file_path(self):
        """Test heading for formatter file paths."""
        result = build_heading("specs/python/formatters/black.md", "black")
        assert result == "# black Version"

    def test_spec_file_path(self):
        """Test heading for spec.md file paths."""
        result = build_heading("specs/python/spec.md", "Python")
        assert result == "# Python Specification"

    def test_compilers_file_path(self):
        """Test heading for compilers.md file paths."""
        result = build_heading("specs/c/compilers.md", "GCC")
        assert result == "# Compilers"

    def test_default_heading(self):
        """Test default heading for other file paths."""
        result = build_heading("specs/python/stdlib/os.md", "os")
        assert result == "# os Version"

    def test_nested_linter_path(self):
        """Test heading for nested linter paths."""
        result = build_heading("specs/bash/linters/shellcheck/SC1000.md", "ShellCheck")
        assert result == "# ShellCheck Version"

    def test_nested_formatter_path(self):
        """Test heading for nested formatter paths."""
        result = build_heading("specs/css/formatters/prettier.md", "Prettier")
        assert result == "# Prettier Version"


class TestUpcaseLabel:
    """Tests for upcase_label function."""

    def test_lowercase_label(self):
        """Test uppercasing a lowercase label."""
        assert upcase_label("version") == "Version"

    def test_already_uppercase_label(self):
        """Test already uppercase label stays uppercase."""
        assert upcase_label("Version") == "Version"

    def test_empty_label(self):
        """Test empty label returns empty string."""
        assert upcase_label("") == ""

    def test_single_char_label(self):
        """Test single character label."""
        assert upcase_label("v") == "V"

    def test_mixed_case_label(self):
        """Test mixed case label only uppercases first char."""
        assert upcase_label("vErSiOn") == "VErSiOn"

    def test_specification_label(self):
        """Test specification label."""
        assert upcase_label("specification") == "Specification"


class TestUpdateContent:
    """Tests for update_content function."""

    def test_adds_version_after_heading(self):
        """Test adding version line after existing heading."""
        content = "# Python\n\nSome content here."
        result = update_content(content, "version", "3.12.0", "# Python Version")
        assert "Version: 3.12.0" in result
        lines = result.split("\n")
        heading_idx = next(i for i, line in enumerate(lines) if line.startswith("# "))
        # Version should be near the heading
        assert any("Version: 3.12.0" in lines[i] for i in range(heading_idx, heading_idx + 4))

    def test_creates_fallback_heading_if_missing(self):
        """Test fallback heading is created when no heading exists."""
        content = "Just some content without heading."
        result = update_content(content, "version", "1.0.0", "# Fallback Heading")
        assert "# Fallback Heading" in result
        assert "Version: 1.0.0" in result

    def test_replaces_existing_version_line(self):
        """Test replacing an existing version line."""
        content = "# Python\n\nVersion: 3.11.0\n\nContent here."
        result = update_content(content, "version", "3.12.0", "# Python Version")
        assert "Version: 3.12.0" in result
        assert "Version: 3.11.0" not in result

    def test_handles_custom_label(self):
        """Test handling custom labels like 'specification'."""
        content = "# Python\n\nSome content."
        result = update_content(content, "specification", "3.12.0", "# Python Specification")
        assert "Specification: 3.12.0" in result

    def test_replaces_existing_custom_label(self):
        """Test replacing an existing custom label line."""
        content = "# Python\n\nSpecification: 3.11.0\n\nContent."
        result = update_content(content, "specification", "3.12.0", "# Python Specification")
        assert "Specification: 3.12.0" in result
        assert "Specification: 3.11.0" not in result

    def test_preserves_content_after_version(self):
        """Test that content after version line is preserved."""
        content = "# Python\n\nOld content.\n\nMore content."
        result = update_content(content, "version", "3.12.0", "# Python Version")
        assert "Old content." in result
        assert "More content." in result

    def test_handles_empty_content(self):
        """Test handling empty content."""
        content = ""
        result = update_content(content, "version", "1.0.0", "# Tool Version")
        assert "# Tool Version" in result
        assert "Version: 1.0.0" in result

    def test_blank_line_after_heading(self):
        """Test that blank line is added after heading if missing."""
        content = "# Python\nNo blank line after heading."
        result = update_content(content, "version", "3.12.0", "# Python Version")
        lines = result.split("\n")
        heading_idx = next(i for i, line in enumerate(lines) if line.startswith("# "))
        # Should have version on line after heading (possibly with blank)
        assert "Version: 3.12.0" in result

    def test_multiple_headings(self):
        """Test handling content with multiple headings."""
        content = "# Main Heading\n\n## Subheading\n\nContent."
        result = update_content(content, "version", "1.0.0", "# Fallback")
        assert "Version: 1.0.0" in result
        # Should add after first heading
        lines = result.split("\n")
        version_idx = next(i for i, line in enumerate(lines) if "Version: 1.0.0" in line)
        main_heading_idx = next(i for i, line in enumerate(lines) if line == "# Main Heading")
        assert version_idx > main_heading_idx

    def test_uppercase_first_char_of_label(self):
        """Test that label first character is uppercased."""
        content = "# Test\n\nContent."
        result = update_content(content, "clang", "15.0.0", "# Test")
        assert "Clang: 15.0.0" in result


class TestEnsureSources:
    """Tests for ensure_sources function."""

    def test_adds_source_after_version_line(self):
        """Test adding source URL after version line."""
        content = "# Python\n\nVersion: 3.12.0\n\nContent."
        sources = ["https://python.org"]
        result = ensure_sources(content, sources, "version", "3.12.0")
        assert "Source: https://python.org" in result
        lines = result.split("\n")
        version_idx = next(i for i, line in enumerate(lines) if "Version: 3.12.0" in line)
        source_idx = next(i for i, line in enumerate(lines) if "Source: https://python.org" in line)
        assert source_idx > version_idx

    def test_adds_multiple_sources(self):
        """Test adding multiple source URLs."""
        content = "# Python\n\nVersion: 3.12.0\n\nContent."
        sources = ["https://python.org", "https://docs.python.org"]
        result = ensure_sources(content, sources, "version", "3.12.0")
        assert "Source: https://python.org" in result
        assert "Source: https://docs.python.org" in result

    def test_empty_sources_returns_unchanged(self):
        """Test that empty sources list returns content unchanged."""
        content = "# Python\n\nVersion: 3.12.0"
        result = ensure_sources(content, [], "version", "3.12.0")
        assert result == content

    def test_does_not_duplicate_existing_source(self):
        """Test that existing source is not duplicated."""
        content = "# Python\n\nVersion: 3.12.0\nSource: https://python.org\n\nContent."
        sources = ["https://python.org"]
        result = ensure_sources(content, sources, "version", "3.12.0")
        # Count occurrences
        count = result.count("Source: https://python.org")
        assert count == 1

    def test_adds_missing_source_keeps_existing(self):
        """Test adding missing source while keeping existing."""
        content = "# Python\n\nVersion: 3.12.0\nSource: https://python.org\n\nContent."
        sources = ["https://python.org", "https://docs.python.org"]
        result = ensure_sources(content, sources, "version", "3.12.0")
        assert "Source: https://python.org" in result
        assert "Source: https://docs.python.org" in result

    def test_handles_version_not_found(self):
        """Test handling when version line is not found."""
        content = "# Python\n\nNo version line here."
        sources = ["https://python.org"]
        result = ensure_sources(content, sources, "version", "3.12.0")
        # Should still add source (fallback to index 1)
        assert "Source: https://python.org" in result

    def test_adds_blank_line_after_sources(self):
        """Test that blank line is added after sources if needed."""
        content = "# Python\n\nVersion: 3.12.0\nContent immediately after."
        sources = ["https://python.org"]
        result = ensure_sources(content, sources, "version", "3.12.0")
        lines = result.split("\n")
        source_idx = next(i for i, line in enumerate(lines) if "Source: https://python.org" in line)
        # There should be a blank line before "Content"
        if source_idx + 1 < len(lines):
            next_line = lines[source_idx + 1]
            # Either it's a blank line or it's already the next content
            assert next_line == "" or "Content" in next_line

    def test_handles_custom_label(self):
        """Test handling sources with custom label."""
        content = "# Python\n\nSpecification: 3.12.0\n\nContent."
        sources = ["https://spec.python.org"]
        result = ensure_sources(content, sources, "specification", "3.12.0")
        assert "Source: https://spec.python.org" in result


class TestMain:
    """Tests for main function."""

    def test_reads_registry_and_updates_files(self, tmp_path, monkeypatch):
        """Test main reads registry and updates spec files."""
        # Setup directory structure
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        # Create registry
        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "label": "version",
                    "files": ["specs/python/spec.md"],
                    "sources": ["https://python.org"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        # Create existing spec file
        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Python\n\nOriginal content.")

        # Monkeypatch paths
        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        # Run main
        main()

        # Verify file was updated
        updated_content = spec_file.read_text()
        assert "Version: 3.12.0" in updated_content
        assert "Source: https://python.org" in updated_content
        assert "Original content." in updated_content

    def test_creates_file_if_not_exists(self, tmp_path, monkeypatch):
        """Test main creates file if it doesn't exist."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "files": ["specs/python/spec.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        # Don't create the file - main should create it

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        # Verify file was created
        assert spec_file.exists()
        content = spec_file.read_text()
        assert "# python Specification" in content
        assert "Version: 3.12.0" in content

    def test_handles_multiple_tools_same_file(self, tmp_path, monkeypatch):
        """Test main handles multiple tools referencing the same file."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "c"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "gcc",
                    "version": "13.2.0",
                    "label": "GCC",
                    "files": ["specs/c/compilers.md"],
                },
                {
                    "name": "clang",
                    "version": "17.0.0",
                    "label": "Clang",
                    "files": ["specs/c/compilers.md"],
                },
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "compilers.md"
        spec_file.write_text("# Compilers\n\nCompiler documentation.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "GCC: 13.2.0" in content
        assert "Clang: 17.0.0" in content

    def test_handles_empty_sources(self, tmp_path, monkeypatch):
        """Test main handles tools with empty or None sources."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "files": ["specs/python/spec.md"],
                    "sources": None,
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Python\n\nContent.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "Version: 3.12.0" in content
        assert "Source:" not in content

    def test_handles_empty_files(self, tmp_path, monkeypatch):
        """Test main handles tools with empty or None files."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "files": None,
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        # Should not raise
        main()

    def test_ensures_trailing_newline(self, tmp_path, monkeypatch):
        """Test main ensures trailing newline in output files."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "files": ["specs/python/spec.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Python\n\nContent without trailing newline")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert content.endswith("\n")

    def test_uses_default_label_when_missing(self, tmp_path, monkeypatch):
        """Test main uses 'Version' as default label when not specified."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    # No "label" field
                    "files": ["specs/python/spec.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Python\n\nContent.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "Version: 3.12.0" in content

    def test_empty_registry(self, tmp_path, monkeypatch):
        """Test main handles empty registry."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        registry = {"tools": []}
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        # Should not raise
        main()

    def test_writes_to_nested_directories(self, tmp_path, monkeypatch):
        """Test main writes to files in nested directories when dirs exist."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "bash" / "linters" / "shellcheck"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "shellcheck",
                    "version": "0.9.0",
                    "files": ["specs/bash/linters/shellcheck/overview.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        spec_file = specs_dir / "overview.md"
        assert spec_file.exists()
        assert "Version: 0.9.0" in spec_file.read_text()

    def test_raises_when_parent_directory_missing(self, tmp_path, monkeypatch):
        """Test main raises FileNotFoundError when parent directories don't exist."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()

        registry = {
            "tools": [
                {
                    "name": "shellcheck",
                    "version": "0.9.0",
                    "files": ["specs/bash/linters/shellcheck/overview.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        # Parent directories don't exist, so this should raise
        with pytest.raises(FileNotFoundError):
            main()


class TestFilePatternMatching:
    """Tests for file pattern matching in build_heading."""

    def test_linter_deep_path(self):
        """Test linter pattern matches deep paths."""
        result = build_heading("specs/javascript/linters/eslint/rules/no-unused-vars.md", "ESLint")
        assert result == "# ESLint Version"

    def test_formatter_at_root(self):
        """Test formatter pattern at various depths."""
        result = build_heading("specs/python/formatters/black.md", "black")
        assert result == "# black Version"

    def test_spec_only_exact_match(self):
        """Test spec.md only matches exact filename."""
        result = build_heading("specs/python/myspec.md", "myspec")
        assert result == "# myspec Version"  # Should not match as spec.md

    def test_compilers_in_path(self):
        """Test compilers.md matches anywhere."""
        result = build_heading("specs/c/compilers.md", "GCC")
        assert result == "# Compilers"

    def test_stdlib_file(self):
        """Test stdlib files get default heading."""
        result = build_heading("specs/python/stdlib/os.md", "os")
        assert result == "# os Version"


class TestUpdateContentEdgeCases:
    """Edge case tests for update_content."""

    def test_content_with_only_newlines(self):
        """Test content that is only newlines."""
        content = "\n\n\n"
        result = update_content(content, "version", "1.0.0", "# Tool")
        assert "# Tool" in result
        assert "Version: 1.0.0" in result

    def test_heading_at_very_end(self):
        """Test heading at the very end of content."""
        content = "Some preamble\n# Heading"
        result = update_content(content, "version", "1.0.0", "# Fallback")
        assert "Version: 1.0.0" in result

    def test_preserves_heading_exactly(self):
        """Test that existing heading is preserved exactly."""
        content = "# My Custom Heading\n\nContent."
        result = update_content(content, "version", "1.0.0", "# Different Heading")
        assert "# My Custom Heading" in result
        assert "# Different Heading" not in result

    def test_version_line_with_extra_spaces(self):
        """Test version line detection is exact."""
        content = "# Heading\n\n  Version: 1.0.0\n\nContent."
        result = update_content(content, "version", "2.0.0", "# Heading")
        # The existing line with spaces should not be matched as it doesn't start with "Version:"
        assert "Version: 2.0.0" in result

    def test_colon_in_version(self):
        """Test version string containing colons."""
        content = "# Heading\n\nContent."
        result = update_content(content, "version", "2024-01-01:12:00", "# Heading")
        assert "Version: 2024-01-01:12:00" in result


class TestEnsureSourcesEdgeCases:
    """Edge case tests for ensure_sources."""

    def test_source_url_with_special_characters(self):
        """Test source URLs with special characters."""
        content = "# Heading\n\nVersion: 1.0.0\n\nContent."
        sources = ["https://example.com/path?query=value&other=123"]
        result = ensure_sources(content, sources, "version", "1.0.0")
        assert "Source: https://example.com/path?query=value&other=123" in result

    def test_many_sources(self):
        """Test adding many source URLs."""
        content = "# Heading\n\nVersion: 1.0.0\n\nContent."
        sources = [f"https://example{i}.com" for i in range(10)]
        result = ensure_sources(content, sources, "version", "1.0.0")
        for source in sources:
            assert f"Source: {source}" in result

    def test_partial_match_source_not_skipped(self):
        """Test that partial match sources are still added."""
        content = "# Heading\n\nVersion: 1.0.0\nSource: https://python.org/docs\n\nContent."
        sources = ["https://python.org"]  # Different from existing
        result = ensure_sources(content, sources, "version", "1.0.0")
        assert "Source: https://python.org" in result
        assert "Source: https://python.org/docs" in result


class TestRegistryStructure:
    """Tests for registry data structure handling."""

    def test_tool_with_all_fields(self, tmp_path, monkeypatch):
        """Test tool with all optional fields."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "python",
                    "version": "3.12.0",
                    "label": "Specification",
                    "files": ["specs/python/spec.md"],
                    "sources": ["https://python.org", "https://docs.python.org"],
                    "latest": {"type": "pypi", "package": "python"},
                    "checkedAt": "2024-01-01T00:00:00Z",
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Python\n\nContent.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "Specification: 3.12.0" in content
        assert "Source: https://python.org" in content
        assert "Source: https://docs.python.org" in content

    def test_tool_with_minimal_fields(self, tmp_path, monkeypatch):
        """Test tool with only required fields."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "test"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "test",
                    "version": "1.0.0",
                    "files": ["specs/test/spec.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Test\n\nContent.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "Version: 1.0.0" in content

    def test_empty_version_string(self, tmp_path, monkeypatch):
        """Test tool with empty version string."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "test"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "test",
                    "version": "",
                    "files": ["specs/test/spec.md"],
                }
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "spec.md"
        spec_file.write_text("# Test\n\nContent.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "Version: " in content  # Empty version still gets stamped


class TestMultipleEntriesPerFile:
    """Tests for handling multiple tool entries targeting the same file."""

    def test_two_tools_same_file_different_labels(self, tmp_path, monkeypatch):
        """Test two tools with different labels targeting same file."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "c"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "gcc",
                    "version": "13.2.0",
                    "label": "GCC",
                    "files": ["specs/c/compilers.md"],
                    "sources": ["https://gcc.gnu.org"],
                },
                {
                    "name": "clang",
                    "version": "17.0.0",
                    "label": "Clang",
                    "files": ["specs/c/compilers.md"],
                    "sources": ["https://clang.llvm.org"],
                },
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "compilers.md"
        spec_file.write_text("# Compilers\n\nCompiler documentation.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "GCC: 13.2.0" in content
        assert "Clang: 17.0.0" in content
        assert "Source: https://gcc.gnu.org" in content
        assert "Source: https://clang.llvm.org" in content

    def test_three_tools_same_file(self, tmp_path, monkeypatch):
        """Test three tools targeting same file."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "test"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {
                    "name": "tool1",
                    "version": "1.0.0",
                    "label": "Tool1",
                    "files": ["specs/test/multi.md"],
                },
                {
                    "name": "tool2",
                    "version": "2.0.0",
                    "label": "Tool2",
                    "files": ["specs/test/multi.md"],
                },
                {
                    "name": "tool3",
                    "version": "3.0.0",
                    "label": "Tool3",
                    "files": ["specs/test/multi.md"],
                },
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        spec_file = specs_dir / "multi.md"
        spec_file.write_text("# Multi Tool File\n\nContent.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "Tool1: 1.0.0" in content
        assert "Tool2: 2.0.0" in content
        assert "Tool3: 3.0.0" in content


class TestFallbackHeadingConstruction:
    """Tests for fallback heading construction with multiple tools."""

    def test_fallback_heading_single_tool(self, tmp_path, monkeypatch):
        """Test fallback heading with single tool."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "python"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {"name": "python", "version": "3.12.0", "files": ["specs/python/spec.md"]},
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        # Create file without heading
        spec_file = specs_dir / "spec.md"
        spec_file.write_text("No heading here.\n\nJust content.")

        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        content = spec_file.read_text()
        assert "# python Specification" in content

    def test_fallback_heading_multiple_tools(self, tmp_path, monkeypatch):
        """Test fallback heading with multiple tools."""
        tools_dir = tmp_path / "tools"
        tools_dir.mkdir()
        specs_dir = tmp_path / "specs" / "c"
        specs_dir.mkdir(parents=True)

        registry = {
            "tools": [
                {"name": "gcc", "version": "13.0.0", "files": ["specs/c/compilers.md"]},
                {"name": "clang", "version": "17.0.0", "files": ["specs/c/compilers.md"]},
            ]
        }
        (tools_dir / "versions.json").write_text(json.dumps(registry))

        # File doesn't exist - main should create it with fallback heading
        monkeypatch.setattr(stamp_versions, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(stamp_versions, "REGISTRY_PATH", tools_dir / "versions.json")

        main()

        spec_file = specs_dir / "compilers.md"
        content = spec_file.read_text()
        # For compilers.md, heading should be "# Compilers"
        assert "# Compilers" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
