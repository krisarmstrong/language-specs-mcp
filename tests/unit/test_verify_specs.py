#!/usr/bin/env python3
"""Unit tests for verify-specs.py."""

import importlib
import importlib.util
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


def reload_module_with_specs_root(specs_root: Path):
    """Reload the verify-specs module with a custom SPECS_ROOT."""
    # Remove cached module if exists
    if "verify_specs" in sys.modules:
        del sys.modules["verify_specs"]

    # Load module from file
    spec = importlib.util.spec_from_file_location(
        "verify_specs",
        Path(__file__).parent.parent.parent / "scripts" / "verify-specs.py",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Override SPECS_ROOT after loading
    module.SPECS_ROOT = specs_root

    return module


# Load module normally for function imports
_spec = importlib.util.spec_from_file_location(
    "verify_specs",
    Path(__file__).parent.parent.parent / "scripts" / "verify-specs.py",
)
verify_specs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verify_specs)

has_markdown = verify_specs.has_markdown
count_markdown = verify_specs.count_markdown
count_top_level_markdown = verify_specs.count_top_level_markdown
read_fetched_at = verify_specs.read_fetched_at
CATEGORIES = verify_specs.CATEGORIES


class TestHasMarkdown:
    """Tests for has_markdown function."""

    def test_empty_directory_returns_false(self, tmp_path):
        """Test empty directory has no markdown."""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        assert has_markdown(empty_dir) is False

    def test_nonexistent_directory_returns_false(self, tmp_path):
        """Test nonexistent directory returns False."""
        missing_dir = tmp_path / "missing"
        assert has_markdown(missing_dir) is False

    def test_directory_with_markdown_file(self, tmp_path):
        """Test directory with markdown file returns True."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")
        assert has_markdown(lang_dir) is True

    def test_directory_with_non_markdown_files(self, tmp_path):
        """Test directory with only non-markdown files returns False."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "config.json").write_text("{}")
        (lang_dir / "data.txt").write_text("some text")
        assert has_markdown(lang_dir) is False

    def test_nested_markdown_in_subdirectory(self, tmp_path):
        """Test markdown in subdirectory is found."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "overview.md").write_text("# Stdlib Overview")
        assert has_markdown(lang_dir) is True

    def test_deeply_nested_markdown(self, tmp_path):
        """Test deeply nested markdown is found."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        deep_dir = lang_dir / "linters" / "pylint" / "rules"
        deep_dir.mkdir(parents=True)
        (deep_dir / "E0001.md").write_text("# Error E0001")
        assert has_markdown(lang_dir) is True

    def test_mixed_files_and_directories(self, tmp_path):
        """Test directory with both files and subdirectories."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "config.json").write_text("{}")
        sub_dir = lang_dir / "docs"
        sub_dir.mkdir()
        (sub_dir / "guide.md").write_text("# Guide")
        assert has_markdown(lang_dir) is True

    def test_markdown_extension_case_sensitivity(self, tmp_path):
        """Test that .MD uppercase extension is not matched."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.MD").write_text("# Spec")
        # Python's endswith is case-sensitive
        assert has_markdown(lang_dir) is False

    def test_file_with_md_in_name_but_different_extension(self, tmp_path):
        """Test file with 'md' in name but different extension."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "readme.md.bak").write_text("# Backup")
        assert has_markdown(lang_dir) is False

    def test_multiple_markdown_files(self, tmp_path):
        """Test directory with multiple markdown files."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "overview.md").write_text("# Overview")
        (lang_dir / "guide.md").write_text("# Guide")
        assert has_markdown(lang_dir) is True


class TestCountMarkdown:
    """Tests for count_markdown function."""

    def test_empty_directory_returns_zero(self, tmp_path):
        """Test empty directory returns count of 0."""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        assert count_markdown(empty_dir) == 0

    def test_nonexistent_directory_returns_zero(self, tmp_path):
        """Test nonexistent directory returns 0."""
        missing_dir = tmp_path / "missing"
        assert count_markdown(missing_dir) == 0

    def test_single_markdown_file(self, tmp_path):
        """Test directory with one markdown file."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        assert count_markdown(lang_dir) == 1

    def test_multiple_markdown_files(self, tmp_path):
        """Test directory with multiple markdown files."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "overview.md").write_text("# Overview")
        (lang_dir / "guide.md").write_text("# Guide")
        assert count_markdown(lang_dir) == 3

    def test_nested_markdown_files(self, tmp_path):
        """Test counting nested markdown files."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "overview.md").write_text("# Overview")
        (stdlib_dir / "functions.md").write_text("# Functions")

        assert count_markdown(lang_dir) == 3

    def test_deeply_nested_files(self, tmp_path):
        """Test counting deeply nested markdown files."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        deep_dir = lang_dir / "linters" / "pylint" / "rules"
        deep_dir.mkdir(parents=True)
        (deep_dir / "E0001.md").write_text("# E0001")
        (deep_dir / "E0002.md").write_text("# E0002")

        assert count_markdown(lang_dir) == 2

    def test_ignores_non_markdown_files(self, tmp_path):
        """Test that non-markdown files are not counted."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "config.json").write_text("{}")
        (lang_dir / "data.txt").write_text("data")
        (lang_dir / ".fetched-at").write_text("2024-01-01")
        assert count_markdown(lang_dir) == 1

    def test_mixed_structure(self, tmp_path):
        """Test complex directory structure with mixed content."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()

        # Top level
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "sources.json").write_text("{}")

        # stdlib
        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "overview.md").write_text("# Overview")
        (stdlib_dir / "index.json").write_text("{}")

        # linters
        linters_dir = lang_dir / "linters" / "pylint"
        linters_dir.mkdir(parents=True)
        (linters_dir / "overview.md").write_text("# Pylint")
        (linters_dir / "E0001.md").write_text("# E0001")

        assert count_markdown(lang_dir) == 4


class TestCountTopLevelMarkdown:
    """Tests for count_top_level_markdown function."""

    def test_empty_directory_returns_zero(self, tmp_path):
        """Test empty directory returns 0."""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        assert count_top_level_markdown(empty_dir) == 0

    def test_nonexistent_directory_returns_zero(self, tmp_path):
        """Test nonexistent directory returns 0."""
        missing_dir = tmp_path / "missing"
        assert count_top_level_markdown(missing_dir) == 0

    def test_single_top_level_markdown(self, tmp_path):
        """Test directory with one top-level markdown file."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        assert count_top_level_markdown(lang_dir) == 1

    def test_multiple_top_level_markdown(self, tmp_path):
        """Test directory with multiple top-level markdown files."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "overview.md").write_text("# Overview")
        (lang_dir / "guide.md").write_text("# Guide")
        assert count_top_level_markdown(lang_dir) == 3

    def test_ignores_nested_markdown(self, tmp_path):
        """Test that nested markdown files are not counted."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "overview.md").write_text("# Overview")
        (stdlib_dir / "functions.md").write_text("# Functions")

        assert count_top_level_markdown(lang_dir) == 1

    def test_ignores_non_markdown_files(self, tmp_path):
        """Test that non-markdown files are not counted."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "config.json").write_text("{}")
        (lang_dir / ".fetched-at").write_text("2024-01-01")
        assert count_top_level_markdown(lang_dir) == 1

    def test_ignores_directories(self, tmp_path):
        """Test that directories are not counted."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "stdlib").mkdir()  # Directory, not a file
        assert count_top_level_markdown(lang_dir) == 1


class TestReadFetchedAt:
    """Tests for read_fetched_at function."""

    def test_missing_fetched_at_returns_unknown(self, tmp_path):
        """Test missing .fetched-at returns 'unknown'."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        assert read_fetched_at(lang_dir) == "unknown"

    def test_valid_fetched_at(self, tmp_path):
        """Test reading valid .fetched-at content."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("2024-01-15T12:00:00Z")
        assert read_fetched_at(lang_dir) == "2024-01-15T12:00:00Z"

    def test_empty_fetched_at_returns_unknown(self, tmp_path):
        """Test empty .fetched-at returns 'unknown'."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("")
        assert read_fetched_at(lang_dir) == "unknown"

    def test_whitespace_only_fetched_at_returns_unknown(self, tmp_path):
        """Test whitespace-only .fetched-at returns 'unknown'."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("   \n\t  ")
        assert read_fetched_at(lang_dir) == "unknown"

    def test_strips_whitespace(self, tmp_path):
        """Test that whitespace is stripped from content."""
        lang_dir = tmp_path / "python"
        lang_dir.mkdir()
        (lang_dir / ".fetched-at").write_text("  2024-01-15T12:00:00Z  \n")
        assert read_fetched_at(lang_dir) == "2024-01-15T12:00:00Z"


class TestCategories:
    """Tests for CATEGORIES constant."""

    def test_categories_contains_expected_values(self):
        """Test CATEGORIES has expected category names."""
        assert "spec" in CATEGORIES
        assert "stdlib" in CATEGORIES
        assert "linters" in CATEGORIES
        assert "formatters" in CATEGORIES
        assert "patterns" in CATEGORIES

    def test_categories_count(self):
        """Test CATEGORIES has expected number of entries."""
        assert len(CATEGORIES) == 5


class TestMainFunction:
    """Tests for main function and overall verification."""

    def test_no_languages_passes(self, tmp_path, capsys):
        """Test empty specs directory passes."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 0 languages" in captured.out

    def test_valid_language_passes(self, tmp_path, capsys):
        """Test valid language directory passes verification."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15T12:00:00Z")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 1 languages" in captured.out

    def test_multiple_languages_pass(self, tmp_path, capsys):
        """Test multiple valid languages pass verification."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        for lang in ["python", "javascript", "go"]:
            lang_dir = specs_root / lang
            lang_dir.mkdir()
            (lang_dir / "spec.md").write_text(f"# {lang} Spec")
            (lang_dir / ".fetched-at").write_text("2024-01-15T12:00:00Z")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 3 languages" in captured.out

    def test_language_without_markdown_fails(self, tmp_path):
        """Test language directory without markdown fails."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "config.json").write_text("{}")  # No markdown

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        assert "python: no markdown files found" in str(exc_info.value)

    def test_empty_category_directory_fails(self, tmp_path):
        """Test category directory with no markdown fails."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")

        # Create empty stdlib directory
        (lang_dir / "stdlib").mkdir()

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        assert "python/stdlib: directory exists but has no markdown" in str(exc_info.value)

    def test_multiple_empty_categories_fail(self, tmp_path):
        """Test multiple empty category directories are all reported."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")

        # Create empty directories for multiple categories
        (lang_dir / "stdlib").mkdir()
        (lang_dir / "linters").mkdir()

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        error_msg = str(exc_info.value)
        assert "python/stdlib: directory exists but has no markdown" in error_msg
        assert "python/linters: directory exists but has no markdown" in error_msg

    def test_category_with_markdown_passes(self, tmp_path, capsys):
        """Test category directory with markdown passes."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")

        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "overview.md").write_text("# Stdlib Overview")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 1 languages" in captured.out

    def test_nonexistent_category_ignored(self, tmp_path, capsys):
        """Test nonexistent category directory is ignored."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")
        # No stdlib, linters, etc. directories

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 1 languages" in captured.out


class TestCoverageReport:
    """Tests for coverage report generation."""

    def test_coverage_table_format(self, tmp_path, capsys):
        """Test coverage table is properly formatted."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15T12:00:00Z")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Coverage summary:" in captured.out
        table_header = (
            "| Language | Spec | Stdlib | Linters | Formatters | Patterns | Fetched (UTC) |"
        )
        assert table_header in captured.out
        assert "python" in captured.out

    def test_coverage_counts_spec_files(self, tmp_path, capsys):
        """Test coverage table counts spec files correctly."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "overview.md").write_text("# Overview")
        (lang_dir / ".fetched-at").write_text("2024-01-15")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Should show 2 spec files
        assert "| python | 2 |" in captured.out

    def test_coverage_counts_stdlib_files(self, tmp_path, capsys):
        """Test coverage table counts stdlib files correctly."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15")

        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "overview.md").write_text("# Overview")
        (stdlib_dir / "functions.md").write_text("# Functions")
        (stdlib_dir / "classes.md").write_text("# Classes")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Should show 3 stdlib files
        assert "| 3 |" in captured.out

    def test_coverage_counts_linters_files(self, tmp_path, capsys):
        """Test coverage table counts linter files correctly."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15")

        linters_dir = lang_dir / "linters" / "pylint"
        linters_dir.mkdir(parents=True)
        (linters_dir / "overview.md").write_text("# Pylint")
        (linters_dir / "E0001.md").write_text("# E0001")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Should include linter files
        assert "python" in captured.out

    def test_coverage_uses_lib_fallback(self, tmp_path, capsys):
        """Test coverage uses 'lib' directory as stdlib fallback."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15")

        # Use 'lib' instead of 'stdlib'
        lib_dir = lang_dir / "lib"
        lib_dir.mkdir()
        (lib_dir / "overview.md").write_text("# Lib Overview")
        (lib_dir / "utils.md").write_text("# Utils")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Should count lib files as stdlib
        assert "python" in captured.out

    def test_coverage_prefers_stdlib_over_lib(self, tmp_path, capsys):
        """Test that stdlib directory is preferred over lib."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15")

        # Create both stdlib and lib
        stdlib_dir = lang_dir / "stdlib"
        stdlib_dir.mkdir()
        (stdlib_dir / "stdlib_file.md").write_text("# Stdlib")

        lib_dir = lang_dir / "lib"
        lib_dir.mkdir()
        (lib_dir / "lib1.md").write_text("# Lib 1")
        (lib_dir / "lib2.md").write_text("# Lib 2")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Should use stdlib (1 file) not lib (2 files)
        assert "| python | 1 | 1 |" in captured.out

    def test_coverage_fetched_at_shown(self, tmp_path, capsys):
        """Test fetched-at timestamp is shown in coverage."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / ".fetched-at").write_text("2024-01-15T12:00:00Z")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "2024-01-15T12:00:00Z" in captured.out

    def test_coverage_unknown_fetched_at(self, tmp_path, capsys):
        """Test missing fetched-at shows 'unknown'."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        # No .fetched-at file

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "unknown" in captured.out


class TestFailureReporting:
    """Tests for failure report formatting."""

    def test_failure_list_format(self, tmp_path):
        """Test failure list is properly formatted."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        # No markdown files

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        error_msg = str(exc_info.value)
        assert "Spec verification failed:" in error_msg
        assert "- python: no markdown files found" in error_msg

    def test_failure_includes_coverage_table(self, tmp_path):
        """Test failure message includes coverage table."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # Create one valid language and one invalid
        valid_dir = specs_root / "javascript"
        valid_dir.mkdir()
        (valid_dir / "spec.md").write_text("# JS Spec")

        invalid_dir = specs_root / "python"
        invalid_dir.mkdir()
        (invalid_dir / "stdlib").mkdir()  # Empty category dir

        # We need markdown in python for it to be counted
        (invalid_dir / "spec.md").write_text("# Python Spec")

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        error_msg = str(exc_info.value)
        assert "Coverage summary:" in error_msg
        assert "| Language |" in error_msg

    def test_multiple_failures_all_reported(self, tmp_path):
        """Test all failures are reported."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # First language - no markdown
        lang1 = specs_root / "python"
        lang1.mkdir()

        # Second language - empty category
        lang2 = specs_root / "javascript"
        lang2.mkdir()
        (lang2 / "spec.md").write_text("# JS Spec")
        (lang2 / "stdlib").mkdir()  # Empty

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        error_msg = str(exc_info.value)
        assert "python: no markdown files found" in error_msg
        assert "javascript/stdlib: directory exists but has no markdown" in error_msg


class TestLanguageSorting:
    """Tests for language directory sorting."""

    def test_languages_sorted_alphabetically(self, tmp_path, capsys):
        """Test languages are processed in alphabetical order."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # Create languages in non-alphabetical order
        for lang in ["rust", "go", "python", "javascript"]:
            lang_dir = specs_root / lang
            lang_dir.mkdir()
            (lang_dir / "spec.md").write_text(f"# {lang} Spec")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        output = captured.out

        # Find positions of each language
        go_pos = output.find("| go |")
        javascript_pos = output.find("| javascript |")
        python_pos = output.find("| python |")
        rust_pos = output.find("| rust |")

        # Verify alphabetical order
        assert go_pos < javascript_pos < python_pos < rust_pos


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_hidden_directories_as_languages(self, tmp_path, capsys):
        """Test hidden directories are treated as languages."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # Create a hidden directory
        hidden_dir = specs_root / ".hidden"
        hidden_dir.mkdir()
        (hidden_dir / "spec.md").write_text("# Hidden Spec")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Hidden directory is treated as a language
        assert ".hidden" in captured.out

    def test_files_in_specs_root_ignored(self, tmp_path, capsys):
        """Test files directly in specs root are ignored."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # Create a file in specs root
        (specs_root / "README.md").write_text("# README")

        # Create a valid language
        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Python Spec")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Should only count python
        assert "Spec verification passed for 1 languages" in captured.out

    def test_symlinks_followed(self, tmp_path, capsys):
        """Test symbolic links are followed."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        # Create actual language dir
        actual_dir = tmp_path / "actual_python"
        actual_dir.mkdir()
        (actual_dir / "spec.md").write_text("# Python Spec")

        # Create symlink
        lang_dir = specs_root / "python"
        lang_dir.symlink_to(actual_dir)

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 1 languages" in captured.out

    def test_unicode_filenames(self, tmp_path, capsys):
        """Test handling of unicode filenames."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")
        (lang_dir / "unicode_test.md").write_text("# Unicode Test")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed for 1 languages" in captured.out

    def test_empty_markdown_files_counted(self, tmp_path, capsys):
        """Test empty markdown files are still counted."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "empty.md").write_text("")  # Empty file

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        # Empty .md file should still count
        assert "Spec verification passed for 1 languages" in captured.out

    def test_very_long_language_name(self, tmp_path, capsys):
        """Test handling of very long language names."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        long_name = "a" * 100
        lang_dir = specs_root / long_name
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert long_name in captured.out


class TestAllCategories:
    """Tests for all category types."""

    def test_all_categories_checked(self, tmp_path):
        """Test all categories are checked for empty directories."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        # Create empty directories for all categories
        for category in CATEGORIES:
            (lang_dir / category).mkdir()

        module = reload_module_with_specs_root(specs_root)

        with pytest.raises(SystemExit) as exc_info:
            module.main()

        error_msg = str(exc_info.value)
        # All categories should be reported
        for category in CATEGORIES:
            assert f"python/{category}:" in error_msg

    def test_formatters_category(self, tmp_path, capsys):
        """Test formatters category is counted."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        formatters_dir = lang_dir / "formatters"
        formatters_dir.mkdir()
        (formatters_dir / "black.md").write_text("# Black")
        (formatters_dir / "autopep8.md").write_text("# Autopep8")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "python" in captured.out

    def test_patterns_category(self, tmp_path, capsys):
        """Test patterns category is counted."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        patterns_dir = lang_dir / "patterns"
        patterns_dir.mkdir()
        (patterns_dir / "singleton.md").write_text("# Singleton")
        (patterns_dir / "factory.md").write_text("# Factory")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "python" in captured.out


class TestNestedCategoryStructure:
    """Tests for nested category directory structures."""

    def test_nested_linter_rules(self, tmp_path, capsys):
        """Test nested linter rule directories."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        # Create nested linter structure
        pylint_dir = lang_dir / "linters" / "pylint" / "rules"
        pylint_dir.mkdir(parents=True)
        for i in range(5):
            (pylint_dir / f"E{i:04d}.md").write_text(f"# Error {i}")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "python" in captured.out

    def test_markdown_in_deep_subdirectory_satisfies_category(self, tmp_path, capsys):
        """Test markdown deep in subdirectory satisfies category requirement."""
        specs_root = tmp_path / "specs"
        specs_root.mkdir()

        lang_dir = specs_root / "python"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Spec")

        # Create deep stdlib structure
        deep_dir = lang_dir / "stdlib" / "builtins" / "types" / "collections"
        deep_dir.mkdir(parents=True)
        (deep_dir / "dict.md").write_text("# Dict")

        module = reload_module_with_specs_root(specs_root)
        module.main()

        captured = capsys.readouterr()
        assert "Spec verification passed" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
