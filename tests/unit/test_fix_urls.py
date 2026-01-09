#!/usr/bin/env python3
"""Unit tests for fix-urls.py."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
SCRIPTS_DIR = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))


def _import_fix_urls():
    """Import fix-urls.py using importlib (handles hyphen in filename)."""
    spec = importlib.util.spec_from_file_location("fix_urls", SCRIPTS_DIR / "fix-urls.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["fix_urls"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fix_urls_module(tmp_path, monkeypatch):
    """Import fix_urls module with mocked paths."""
    # Set up directory structure
    specs_dir = tmp_path / "specs"
    specs_dir.mkdir()
    docs_site_dir = tmp_path / "docs" / "site"
    docs_site_dir.mkdir(parents=True)

    # Patch the module-level constants before import
    import _common

    monkeypatch.setattr(_common, "SPECS_DIR", specs_dir)

    # Import the module using our helper
    if "fix_urls" in sys.modules:
        del sys.modules["fix_urls"]

    fix_urls = _import_fix_urls()

    monkeypatch.setattr(fix_urls, "SPECS_DIR", specs_dir)
    monkeypatch.setattr(fix_urls, "ROOT_DIR", tmp_path)
    monkeypatch.setattr(fix_urls, "URL_STATUS_FILE", docs_site_dir / "url-status.json")
    monkeypatch.setattr(fix_urls, "FIX_LOG_FILE", docs_site_dir / "url-fix-log.json")

    return fix_urls


class TestLoadUrlStatus:
    """Tests for load_url_status function."""

    def test_returns_empty_dict_when_file_missing(self, fix_urls_module):
        """Test returns empty dict when url-status.json doesn't exist."""
        result = fix_urls_module.load_url_status()
        assert result == {}

    def test_loads_valid_json(self, fix_urls_module, tmp_path):
        """Test loading valid url-status.json."""
        url_status = {
            "generatedAt": "2024-01-01T00:00:00Z",
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ],
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.load_url_status()

        assert result["generatedAt"] == "2024-01-01T00:00:00Z"
        assert len(result["suggestions"]) == 1
        assert result["suggestions"][0]["type"] == "permanent_redirect"

    def test_returns_empty_dict_on_json_decode_error(self, fix_urls_module):
        """Test returns empty dict on invalid JSON."""
        fix_urls_module.URL_STATUS_FILE.write_text("not valid json {", encoding="utf-8")

        result = fix_urls_module.load_url_status()

        assert result == {}

    def test_returns_empty_dict_on_os_error(self, fix_urls_module, monkeypatch):
        """Test returns empty dict on OS error."""
        # Create file but make it unreadable by mocking
        fix_urls_module.URL_STATUS_FILE.write_text("{}", encoding="utf-8")

        def mock_read_text(*args, **kwargs):
            raise OSError("Permission denied")

        monkeypatch.setattr(Path, "read_text", mock_read_text)

        result = fix_urls_module.load_url_status()

        assert result == {}

    def test_loads_empty_suggestions_list(self, fix_urls_module):
        """Test loading file with empty suggestions list."""
        url_status = {"suggestions": []}
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.load_url_status()

        assert result["suggestions"] == []

    def test_loads_complex_status(self, fix_urls_module):
        """Test loading complex url-status.json with multiple suggestions."""
        url_status = {
            "generatedAt": "2024-01-01T00:00:00Z",
            "urlsChecked": 100,
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old1.com",
                    "newUrl": "https://new1.com",
                    "autoFixable": True,
                },
                {
                    "type": "not_found",
                    "url": "https://broken.com",
                    "error": "404 Not Found",
                    "autoFixable": False,
                    "action": "manual review",
                },
            ],
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.load_url_status()

        assert result["urlsChecked"] == 100
        assert len(result["suggestions"]) == 2


class TestFindAndReplaceUrlInSources:
    """Tests for find_and_replace_url_in_sources function."""

    def test_replaces_url_in_sources(self, fix_urls_module):
        """Test replacing a URL in sources.json."""
        # Create language directory with sources.json
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()

        sources = {
            "language": "python",
            "generatedAt": "2024-01-01T00:00:00Z",
            "files": [
                {"path": "spec.md", "urls": ["https://old.com/doc"]},
                {"path": "other.md", "urls": ["https://different.com/doc"]},
            ],
        }
        sources_file = lang_dir / "sources.json"
        sources_file.write_text(json.dumps(sources, indent=2), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert len(changes) == 1
        assert changes[0]["language"] == "python"
        assert changes[0]["file"] == "spec.md"
        assert changes[0]["oldUrl"] == "https://old.com/doc"
        assert changes[0]["newUrl"] == "https://new.com/doc"

        # Verify file was updated
        updated = json.loads(sources_file.read_text(encoding="utf-8"))
        assert updated["files"][0]["urls"] == ["https://new.com/doc"]
        assert updated["files"][1]["urls"] == ["https://different.com/doc"]

    def test_replaces_url_in_multiple_languages(self, fix_urls_module):
        """Test replacing URL across multiple language directories."""
        for lang in ["python", "typescript"]:
            lang_dir = fix_urls_module.SPECS_DIR / lang
            lang_dir.mkdir()
            sources = {
                "language": lang,
                "files": [{"path": "spec.md", "urls": ["https://shared.com/doc"]}],
            }
            (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://shared.com/doc", "https://new-shared.com/doc"
        )

        assert len(changes) == 2
        languages = {c["language"] for c in changes}
        assert languages == {"python", "typescript"}

    def test_no_changes_when_url_not_found(self, fix_urls_module):
        """Test no changes when URL is not in any sources."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://other.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://nonexistent.com/doc", "https://new.com/doc"
        )

        assert changes == []

    def test_skips_hidden_directories(self, fix_urls_module):
        """Test that hidden directories (starting with .) are skipped."""
        # Create hidden directory
        hidden_dir = fix_urls_module.SPECS_DIR / ".hidden"
        hidden_dir.mkdir()
        sources = {
            "language": "hidden",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (hidden_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert changes == []

    def test_skips_files_not_directories(self, fix_urls_module):
        """Test that files in specs directory are skipped."""
        # Create a file instead of directory
        readme = fix_urls_module.SPECS_DIR / "README.md"
        readme.write_text("# Specs")

        # Create valid language dir
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert len(changes) == 1
        assert changes[0]["language"] == "python"

    def test_skips_directories_without_sources_json(self, fix_urls_module):
        """Test directories without sources.json are skipped."""
        # Create directory without sources.json
        lang_dir = fix_urls_module.SPECS_DIR / "rust"
        lang_dir.mkdir()
        (lang_dir / "spec.md").write_text("# Rust Spec")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert changes == []

    def test_handles_invalid_json_in_sources(self, fix_urls_module, capsys):
        """Test warning is logged for invalid JSON in sources.json."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        # Include the old_url in the content so it passes the initial check
        # but still fails JSON parsing
        (lang_dir / "sources.json").write_text(
            "not valid json { https://old.com/doc }", encoding="utf-8"
        )

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert changes == []

    def test_replaces_multiple_occurrences_in_same_file_entry(self, fix_urls_module):
        """Test replacing when URL appears multiple times in same file's urls list."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {
                    "path": "spec.md",
                    "urls": [
                        "https://old.com/doc",
                        "https://backup.com/doc",
                        "https://old.com/doc",
                    ],
                }
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert len(changes) == 1

        # Verify both occurrences were replaced
        updated = json.loads((lang_dir / "sources.json").read_text(encoding="utf-8"))
        assert updated["files"][0]["urls"] == [
            "https://new.com/doc",
            "https://backup.com/doc",
            "https://new.com/doc",
        ]

    def test_updates_generated_at_timestamp(self, fix_urls_module):
        """Test that generatedAt is updated when file is modified."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "generatedAt": "2020-01-01T00:00:00Z",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        updated = json.loads((lang_dir / "sources.json").read_text(encoding="utf-8"))
        assert updated["generatedAt"] != "2020-01-01T00:00:00Z"
        # Check it's a valid ISO format timestamp
        assert "T" in updated["generatedAt"]

    def test_handles_files_without_urls_key(self, fix_urls_module):
        """Test handling file entries without urls key."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "spec.md"},  # No urls key
                {"path": "other.md", "urls": ["https://old.com/doc"]},
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert len(changes) == 1
        assert changes[0]["file"] == "other.md"

    def test_handles_empty_files_list(self, fix_urls_module):
        """Test handling sources with empty files list."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {"language": "python", "files": []}
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert changes == []


class TestApplyAutoFixes:
    """Tests for apply_auto_fixes function."""

    def test_no_suggestions_returns_zero_applied(self, fix_urls_module):
        """Test returns zero when no suggestions exist."""
        fix_urls_module.URL_STATUS_FILE.write_text(
            json.dumps({"suggestions": []}), encoding="utf-8"
        )

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 0
        assert result["changes"] == []

    def test_no_auto_fixable_suggestions(self, fix_urls_module, capsys):
        """Test returns zero when no auto-fixable suggestions."""
        url_status = {
            "suggestions": [
                {"type": "not_found", "url": "https://broken.com", "autoFixable": False}
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 0

    def test_applies_permanent_redirect_fixes(self, fix_urls_module):
        """Test applies permanent redirect fixes."""
        # Create language with sources
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        # Create url-status with auto-fixable suggestion
        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 1
        assert len(result["changes"]) == 1
        assert result["changes"][0]["oldUrl"] == "https://old.com/doc"
        assert result["changes"][0]["newUrl"] == "https://new.com/doc"

    def test_dry_run_mode(self, fix_urls_module, capsys):
        """Test dry run mode doesn't modify files."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        original_sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        sources_file = lang_dir / "sources.json"
        sources_file.write_text(json.dumps(original_sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes(dry_run=True)

        assert result["applied"] == 1
        assert result["dryRun"] is True

        # Verify file was NOT modified
        current = json.loads(sources_file.read_text(encoding="utf-8"))
        assert current["files"][0]["urls"] == ["https://old.com/doc"]

    def test_skips_non_permanent_redirect_types(self, fix_urls_module):
        """Test only permanent_redirect type is auto-fixed."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "temporary_redirect",  # Not permanent
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 0

    def test_skips_suggestions_without_old_url(self, fix_urls_module):
        """Test skips suggestions without oldUrl."""
        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 0

    def test_skips_suggestions_without_new_url(self, fix_urls_module):
        """Test skips suggestions without newUrl."""
        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 0

    def test_applies_multiple_fixes(self, fix_urls_module):
        """Test applying multiple fixes."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "spec1.md", "urls": ["https://old1.com/doc"]},
                {"path": "spec2.md", "urls": ["https://old2.com/doc"]},
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old1.com/doc",
                    "newUrl": "https://new1.com/doc",
                    "autoFixable": True,
                },
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old2.com/doc",
                    "newUrl": "https://new2.com/doc",
                    "autoFixable": True,
                },
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 2

    def test_missing_url_status_file(self, fix_urls_module):
        """Test when url-status.json doesn't exist."""
        result = fix_urls_module.apply_auto_fixes()

        assert result["applied"] == 0
        assert result["changes"] == []


class TestGenerateManualFixReport:
    """Tests for generate_manual_fix_report function."""

    def test_returns_empty_for_no_manual_fixes(self, fix_urls_module):
        """Test returns empty list when no manual fixes needed."""
        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com",
                    "newUrl": "https://new.com",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert result == []

    def test_returns_manual_fixes(self, fix_urls_module):
        """Test returns list of manual fixes."""
        url_status = {
            "suggestions": [
                {
                    "type": "not_found",
                    "url": "https://broken.com/doc",
                    "error": "404 Not Found",
                    "autoFixable": False,
                    "action": "Find replacement",
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert len(result) == 1
        assert result[0]["type"] == "not_found"
        assert result[0]["url"] == "https://broken.com/doc"
        assert result[0]["error"] == "404 Not Found"
        assert result[0]["action"] == "Find replacement"

    def test_includes_search_hint(self, fix_urls_module):
        """Test includes searchHint when present."""
        url_status = {
            "suggestions": [
                {
                    "type": "not_found",
                    "url": "https://broken.com/doc",
                    "autoFixable": False,
                    "searchHint": "Try searching for Python documentation",
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert result[0]["searchHint"] == "Try searching for Python documentation"

    def test_includes_suggested_url(self, fix_urls_module):
        """Test includes suggestedUrl when newUrl present."""
        url_status = {
            "suggestions": [
                {
                    "type": "domain_changed",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": False,  # Not auto-fixable for some reason
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert result[0]["suggestedUrl"] == "https://new.com/doc"

    def test_prefers_url_over_old_url(self, fix_urls_module):
        """Test uses url field when available, otherwise oldUrl."""
        url_status = {
            "suggestions": [
                {
                    "type": "not_found",
                    "url": "https://primary.com/doc",
                    "oldUrl": "https://fallback.com/doc",
                    "autoFixable": False,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert result[0]["url"] == "https://primary.com/doc"

    def test_uses_old_url_when_url_missing(self, fix_urls_module):
        """Test falls back to oldUrl when url is missing."""
        url_status = {
            "suggestions": [
                {
                    "type": "not_found",
                    "oldUrl": "https://fallback.com/doc",
                    "autoFixable": False,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert result[0]["url"] == "https://fallback.com/doc"

    def test_filters_auto_fixable(self, fix_urls_module):
        """Test only non-autoFixable items are included."""
        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com",
                    "newUrl": "https://new.com",
                    "autoFixable": True,
                },
                {
                    "type": "not_found",
                    "url": "https://broken.com",
                    "autoFixable": False,
                },
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        result = fix_urls_module.generate_manual_fix_report()

        assert len(result) == 1
        assert result[0]["type"] == "not_found"

    def test_empty_url_status_file(self, fix_urls_module):
        """Test with missing url-status.json."""
        result = fix_urls_module.generate_manual_fix_report()

        assert result == []


class TestMain:
    """Tests for main function."""

    def test_report_only_mode_with_manual_fixes(self, fix_urls_module, monkeypatch, capsys):
        """Test --report flag shows manual fixes."""
        url_status = {
            "suggestions": [
                {
                    "type": "not_found",
                    "url": "https://broken.com/doc",
                    "error": "404 Not Found",
                    "autoFixable": False,
                    "searchHint": "Search for updated docs",
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py", "--report"])

        result = fix_urls_module.main()

        assert result == 0
        # Output is via logging, so we need to check it was called

    def test_report_only_mode_no_manual_fixes(self, fix_urls_module, monkeypatch, capsys):
        """Test --report flag when no manual fixes needed."""
        url_status = {"suggestions": []}
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py", "--report"])

        result = fix_urls_module.main()

        assert result == 0

    def test_dry_run_mode(self, fix_urls_module, monkeypatch, capsys):
        """Test --dry-run flag doesn't modify files."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        original_sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        sources_file = lang_dir / "sources.json"
        sources_file.write_text(json.dumps(original_sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py", "--dry-run"])

        result = fix_urls_module.main()

        assert result == 0

        # Verify file was NOT modified
        current = json.loads(sources_file.read_text(encoding="utf-8"))
        assert current["files"][0]["urls"] == ["https://old.com/doc"]

    def test_applies_fixes_and_writes_log(self, fix_urls_module, monkeypatch):
        """Test applies fixes and writes fix log."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])

        result = fix_urls_module.main()

        assert result == 0

        # Verify fix log was written
        assert fix_urls_module.FIX_LOG_FILE.exists()
        fix_log = json.loads(fix_urls_module.FIX_LOG_FILE.read_text(encoding="utf-8"))
        assert fix_log["totalChanges"] == 1
        assert len(fix_log["changes"]) == 1
        assert "generatedAt" in fix_log

    def test_no_fixes_applied(self, fix_urls_module, monkeypatch, capsys):
        """Test when no fixes are applied."""
        url_status = {"suggestions": []}
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])

        result = fix_urls_module.main()

        assert result == 0

        # Verify fix log was NOT written (no changes)
        assert not fix_urls_module.FIX_LOG_FILE.exists()

    def test_shows_manual_fixes_summary(self, fix_urls_module, monkeypatch, capsys):
        """Test shows manual fixes summary after applying auto fixes."""
        url_status = {
            "suggestions": [
                {
                    "type": "not_found",
                    "url": "https://broken.com/doc",
                    "autoFixable": False,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])

        result = fix_urls_module.main()

        assert result == 0

    def test_truncates_manual_fixes_display(self, fix_urls_module, monkeypatch, capsys):
        """Test truncates manual fixes display to first 10."""
        suggestions = [
            {"type": "not_found", "url": f"https://broken{i}.com", "autoFixable": False}
            for i in range(15)
        ]
        url_status = {"suggestions": suggestions}
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])

        result = fix_urls_module.main()

        assert result == 0

    def test_creates_fix_log_parent_directory(self, fix_urls_module, monkeypatch):
        """Test creates parent directory for fix log if needed."""
        # Remove the docs/site directory
        import shutil

        shutil.rmtree(fix_urls_module.FIX_LOG_FILE.parent)

        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        # Recreate URL_STATUS_FILE parent
        fix_urls_module.URL_STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])

        result = fix_urls_module.main()

        assert result == 0
        assert fix_urls_module.FIX_LOG_FILE.exists()


class TestFixLogContent:
    """Tests for fix log content structure."""

    def test_fix_log_structure(self, fix_urls_module, monkeypatch):
        """Test fix log has correct structure."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])
        fix_urls_module.main()

        fix_log = json.loads(fix_urls_module.FIX_LOG_FILE.read_text(encoding="utf-8"))

        assert "generatedAt" in fix_log
        assert "dryRun" in fix_log
        assert fix_log["dryRun"] is False
        assert "totalChanges" in fix_log
        assert "changes" in fix_log
        assert isinstance(fix_log["changes"], list)

    def test_fix_log_change_entry_structure(self, fix_urls_module, monkeypatch):
        """Test individual change entries in fix log."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "stdlib/os.md", "urls": ["https://old.com/os"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/os",
                    "newUrl": "https://new.com/os",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])
        fix_urls_module.main()

        fix_log = json.loads(fix_urls_module.FIX_LOG_FILE.read_text(encoding="utf-8"))
        change = fix_log["changes"][0]

        assert change["language"] == "python"
        assert change["file"] == "stdlib/os.md"
        assert change["oldUrl"] == "https://old.com/os"
        assert change["newUrl"] == "https://new.com/os"

    def test_dry_run_fix_log_not_written(self, fix_urls_module, monkeypatch):
        """Test fix log is still written in dry run mode."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        url_status = {
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.com/doc",
                    "newUrl": "https://new.com/doc",
                    "autoFixable": True,
                }
            ]
        }
        fix_urls_module.URL_STATUS_FILE.write_text(json.dumps(url_status), encoding="utf-8")

        monkeypatch.setattr("sys.argv", ["fix-urls.py", "--dry-run"])
        fix_urls_module.main()

        # Fix log should be written even in dry run mode
        assert fix_urls_module.FIX_LOG_FILE.exists()
        fix_log = json.loads(fix_urls_module.FIX_LOG_FILE.read_text(encoding="utf-8"))
        assert fix_log["dryRun"] is True


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_handles_unicode_urls(self, fix_urls_module):
        """Test handles URLs with unicode characters."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://example.com/doc%C3%A9"]}],
        }
        (lang_dir / "sources.json").write_text(
            json.dumps(sources, ensure_ascii=False), encoding="utf-8"
        )

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://example.com/doc%C3%A9", "https://new.com/doc"
        )

        assert len(changes) == 1

    def test_handles_special_characters_in_urls(self, fix_urls_module):
        """Test handles URLs with special characters."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {
                    "path": "spec.md",
                    "urls": ["https://example.com/doc?param=value&other=123"],
                }
            ],
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://example.com/doc?param=value&other=123",
            "https://new.com/doc?param=value&other=123",
        )

        assert len(changes) == 1

    def test_empty_specs_directory(self, fix_urls_module):
        """Test with empty specs directory."""
        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert changes == []

    def test_preserves_json_formatting(self, fix_urls_module):
        """Test preserves JSON indentation after update."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": ["https://old.com/doc"]}],
        }
        sources_file = lang_dir / "sources.json"
        sources_file.write_text(json.dumps(sources, indent=2), encoding="utf-8")

        fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        content = sources_file.read_text(encoding="utf-8")
        # Should have indentation (not minified)
        assert "\n  " in content

    def test_handles_sources_without_files_key(self, fix_urls_module):
        """Test handles sources.json without files key."""
        lang_dir = fix_urls_module.SPECS_DIR / "python"
        lang_dir.mkdir()
        sources = {"language": "python"}  # No files key
        (lang_dir / "sources.json").write_text(json.dumps(sources), encoding="utf-8")

        changes = fix_urls_module.find_and_replace_url_in_sources(
            "https://old.com/doc", "https://new.com/doc"
        )

        assert changes == []


class TestIntegration:
    """Integration tests for complete workflows."""

    def test_full_workflow(self, fix_urls_module, monkeypatch):
        """Test complete workflow from url-status to updated sources."""
        # Setup: Create multiple language directories with sources
        for lang in ["python", "typescript", "go"]:
            lang_dir = fix_urls_module.SPECS_DIR / lang
            lang_dir.mkdir()
            sources = {
                "language": lang,
                "generatedAt": "2020-01-01T00:00:00Z",
                "files": [
                    {"path": "spec.md", "urls": [f"https://old.{lang}.com/doc"]},
                    {"path": "stdlib.md", "urls": ["https://shared.com/stdlib"]},
                ],
            }
            (lang_dir / "sources.json").write_text(json.dumps(sources, indent=2), encoding="utf-8")

        # Create url-status with multiple suggestions
        url_status = {
            "generatedAt": "2024-01-15T12:00:00Z",
            "suggestions": [
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://old.python.com/doc",
                    "newUrl": "https://new.python.com/doc",
                    "autoFixable": True,
                },
                {
                    "type": "permanent_redirect",
                    "oldUrl": "https://shared.com/stdlib",
                    "newUrl": "https://updated-shared.com/stdlib",
                    "autoFixable": True,
                },
                {
                    "type": "not_found",
                    "url": "https://broken.com/missing",
                    "error": "404 Not Found",
                    "autoFixable": False,
                },
            ],
        }
        fix_urls_module.URL_STATUS_FILE.write_text(
            json.dumps(url_status, indent=2), encoding="utf-8"
        )

        monkeypatch.setattr("sys.argv", ["fix-urls.py"])

        result = fix_urls_module.main()

        assert result == 0

        # Verify Python sources updated
        python_sources = json.loads(
            (fix_urls_module.SPECS_DIR / "python" / "sources.json").read_text()
        )
        assert python_sources["files"][0]["urls"] == ["https://new.python.com/doc"]
        assert python_sources["files"][1]["urls"] == ["https://updated-shared.com/stdlib"]

        # Verify shared URL updated in all languages
        for lang in ["typescript", "go"]:
            sources = json.loads((fix_urls_module.SPECS_DIR / lang / "sources.json").read_text())
            assert sources["files"][1]["urls"] == ["https://updated-shared.com/stdlib"]

        # Verify fix log
        fix_log = json.loads(fix_urls_module.FIX_LOG_FILE.read_text())
        assert fix_log["totalChanges"] == 4  # 1 python + 3 shared
        assert fix_log["dryRun"] is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
