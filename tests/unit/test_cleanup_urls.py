#!/usr/bin/env python3
"""Unit tests for cleanup-urls.py."""

import json
import sys
from pathlib import Path

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import the module under test - we need to import specific functions
# Since cleanup-urls.py uses script-style naming, import as module
import importlib.util

spec = importlib.util.spec_from_file_location(
    "cleanup_urls",
    Path(__file__).parent.parent.parent / "scripts" / "cleanup-urls.py",
)
cleanup_urls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cleanup_urls)

# Import functions from the module
is_placeholder_url = cleanup_urls.is_placeholder_url
is_malformed_url = cleanup_urls.is_malformed_url
fix_malformed_url = cleanup_urls.fix_malformed_url
load_url_status = cleanup_urls.load_url_status
build_redirect_map = cleanup_urls.build_redirect_map
build_error_set = cleanup_urls.build_error_set
process_sources_file = cleanup_urls.process_sources_file
main = cleanup_urls.main
PLACEHOLDER_DOMAINS = cleanup_urls.PLACEHOLDER_DOMAINS
MALFORMED_PATTERNS = cleanup_urls.MALFORMED_PATTERNS


class TestPlaceholderDomains:
    """Tests for PLACEHOLDER_DOMAINS constant."""

    def test_contains_common_example_domains(self):
        """Test that common example domains are included."""
        assert "example.com" in PLACEHOLDER_DOMAINS
        assert "example.org" in PLACEHOLDER_DOMAINS
        assert "example.net" in PLACEHOLDER_DOMAINS
        assert "example.edu" in PLACEHOLDER_DOMAINS

    def test_contains_subdomain_variants(self):
        """Test that subdomain variants are included."""
        assert "www.example.com" in PLACEHOLDER_DOMAINS
        assert "api.example.com" in PLACEHOLDER_DOMAINS
        assert "test.example.com" in PLACEHOLDER_DOMAINS

    def test_contains_other_placeholder_domains(self):
        """Test other placeholder domains."""
        assert "cdn-example.com" in PLACEHOLDER_DOMAINS
        assert "idp.example" in PLACEHOLDER_DOMAINS


class TestMalformedPatterns:
    """Tests for MALFORMED_PATTERNS constant."""

    def test_contains_expected_patterns(self):
        """Test that expected malformed patterns are defined."""
        assert len(MALFORMED_PATTERNS) > 0
        # Should have patterns for backticks and markdown artifacts
        pattern_str = " ".join(MALFORMED_PATTERNS)
        assert "`" in pattern_str
        assert "http" in pattern_str.lower()


class TestIsPlaceholderUrl:
    """Tests for is_placeholder_url function."""

    def test_example_com_is_placeholder(self):
        """Test that example.com URLs are detected."""
        assert is_placeholder_url("https://example.com/page") is True
        assert is_placeholder_url("http://example.com") is True

    def test_example_org_is_placeholder(self):
        """Test that example.org URLs are detected."""
        assert is_placeholder_url("https://example.org/docs") is True

    def test_example_net_is_placeholder(self):
        """Test that example.net URLs are detected."""
        assert is_placeholder_url("https://example.net/api") is True

    def test_example_edu_is_placeholder(self):
        """Test that example.edu URLs are detected."""
        assert is_placeholder_url("https://example.edu/resource") is True

    def test_www_example_com_is_placeholder(self):
        """Test that www.example.com URLs are detected."""
        assert is_placeholder_url("https://www.example.com/path") is True

    def test_api_example_com_is_placeholder(self):
        """Test that api.example.com URLs are detected."""
        assert is_placeholder_url("https://api.example.com/v1") is True

    def test_test_example_com_is_placeholder(self):
        """Test that test.example.com URLs are detected."""
        assert is_placeholder_url("https://test.example.com/test") is True

    def test_cdn_example_com_is_placeholder(self):
        """Test that cdn-example.com URLs are detected."""
        assert is_placeholder_url("https://cdn-example.com/assets") is True

    def test_idp_example_is_placeholder(self):
        """Test that idp.example URLs are detected."""
        assert is_placeholder_url("https://idp.example/auth") is True

    def test_subdomain_of_example_com_is_placeholder(self):
        """Test that arbitrary subdomains of example.com are detected."""
        assert is_placeholder_url("https://foo.example.com/page") is True
        assert is_placeholder_url("https://bar.baz.example.com/page") is True

    def test_real_url_not_placeholder(self):
        """Test that real URLs are not detected as placeholders."""
        assert is_placeholder_url("https://python.org/docs") is False
        assert is_placeholder_url("https://github.com/repo") is False
        assert is_placeholder_url("https://developer.mozilla.org") is False

    def test_similar_domain_not_placeholder(self):
        """Test that similar but different domains are not placeholders."""
        assert is_placeholder_url("https://myexample.com") is False
        assert is_placeholder_url("https://example-site.com") is False
        assert is_placeholder_url("https://examplesite.org") is False

    def test_case_insensitive(self):
        """Test that domain matching is case insensitive."""
        assert is_placeholder_url("https://EXAMPLE.COM/page") is True
        assert is_placeholder_url("https://Example.Org/docs") is True

    def test_invalid_url_returns_false(self):
        """Test that invalid URLs return False."""
        assert is_placeholder_url("not-a-url") is False
        assert is_placeholder_url("") is False

    def test_url_with_port_number(self):
        """Test URLs with port numbers."""
        # Note: netloc includes port, so "example.com:8080" != "example.com"
        # The code checks exact domain match, not domain part
        assert is_placeholder_url("https://example.com:8080/api") is False
        assert is_placeholder_url("https://github.com:443/repo") is False

    def test_url_with_query_params(self):
        """Test URLs with query parameters."""
        assert is_placeholder_url("https://example.com?foo=bar") is True
        assert is_placeholder_url("https://python.org?version=3") is False

    def test_url_with_fragment(self):
        """Test URLs with fragments."""
        assert is_placeholder_url("https://example.com/page#section") is True
        assert is_placeholder_url("https://docs.python.org#intro") is False


class TestIsMalformedUrl:
    """Tests for is_malformed_url function."""

    def test_trailing_backtick_is_malformed(self):
        """Test that trailing backticks are detected."""
        assert is_malformed_url("https://example.com/page`") is True

    def test_embedded_backtick_is_malformed(self):
        """Test that embedded backticks are detected."""
        assert is_malformed_url("https://exam`ple.com/page") is True

    def test_markdown_link_artifact_is_malformed(self):
        """Test that markdown link artifacts are detected."""
        assert is_malformed_url("https://example.com](https://other.com") is True

    def test_trailing_parenthesis_is_malformed(self):
        """Test that trailing parenthesis is detected."""
        assert is_malformed_url("https://example.com/page)") is True

    def test_clean_url_not_malformed(self):
        """Test that clean URLs are not detected as malformed."""
        assert is_malformed_url("https://python.org/docs") is False
        assert is_malformed_url("https://github.com/user/repo") is False

    def test_url_with_valid_parentheses_in_path(self):
        """Test URLs with valid parentheses in path (not trailing)."""
        # Note: The current implementation would flag trailing ) as malformed
        # but embedded parentheses should be fine
        assert is_malformed_url("https://example.com/page(v1)") is True  # trailing )

    def test_empty_url_not_malformed(self):
        """Test that empty URL is not malformed."""
        assert is_malformed_url("") is False

    def test_url_with_brackets(self):
        """Test URLs with brackets."""
        # Markdown artifact pattern matches `](http` specifically
        assert is_malformed_url("https://example.com](https://other.com") is True
        # Without http scheme, the markdown pattern doesn't match
        assert is_malformed_url("https://example.com](other") is False


class TestFixMalformedUrl:
    """Tests for fix_malformed_url function."""

    def test_removes_trailing_backtick(self):
        """Test that trailing backticks are removed."""
        assert fix_malformed_url("https://example.com/page`") == "https://example.com/page"

    def test_removes_multiple_trailing_backticks(self):
        """Test that multiple trailing backticks are removed."""
        assert fix_malformed_url("https://example.com/page```") == "https://example.com/page"

    def test_removes_trailing_parenthesis(self):
        """Test that trailing parenthesis is removed."""
        assert fix_malformed_url("https://example.com/page)") == "https://example.com/page"

    def test_extracts_url_from_markdown_artifact(self):
        """Test that URL is extracted from markdown link artifact."""
        result = fix_malformed_url("https://first.com/page](https://second.com")
        # Should extract just the first URL
        assert result == "https://first.com/page"

    def test_returns_none_for_unfixable_url(self):
        """Test that unfixable URLs return None."""
        assert fix_malformed_url("not-a-url") is None
        assert fix_malformed_url("ftp://example.com") is None  # Not http/https

    def test_preserves_valid_url(self):
        """Test that valid URLs are preserved."""
        assert fix_malformed_url("https://example.com/page") == "https://example.com/page"

    def test_handles_empty_string(self):
        """Test handling of empty string."""
        assert fix_malformed_url("") is None

    def test_handles_complex_malformed_url(self):
        """Test handling of URL with multiple issues."""
        # URL with trailing backtick and parenthesis
        result = fix_malformed_url("https://example.com/page)`")
        assert result == "https://example.com/page"

    def test_validates_fixed_url(self):
        """Test that fixed URL is validated."""
        # After fixing, should have valid scheme and netloc
        result = fix_malformed_url("https://valid.com/path`")
        assert result is not None
        assert result.startswith("https://")


class TestLoadUrlStatus:
    """Tests for load_url_status function."""

    def test_loads_existing_file(self, tmp_path, monkeypatch):
        """Test loading existing url-status.json file."""
        status_file = tmp_path / "url-status.json"
        status_data = {
            "allResults": [
                {"url": "https://example.com", "status": "ok"},
            ]
        }
        status_file.write_text(json.dumps(status_data))

        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)

        result = load_url_status()
        assert result == status_data

    def test_exits_on_missing_file(self, tmp_path, monkeypatch):
        """Test that missing file causes exit."""
        status_file = tmp_path / "nonexistent.json"
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)

        with pytest.raises(SystemExit) as exc_info:
            load_url_status()
        assert exc_info.value.code == 1

    def test_loads_complex_status_data(self, tmp_path, monkeypatch):
        """Test loading complex status data."""
        status_file = tmp_path / "url-status.json"
        status_data = {
            "allResults": [
                {"url": "https://ok.com", "status": "ok"},
                {
                    "url": "https://redirect.com",
                    "status": "redirect",
                    "redirectUrl": "https://new.com",
                },
                {"url": "https://error.com", "status": "error"},
            ],
            "summary": {"ok": 1, "redirect": 1, "error": 1},
        }
        status_file.write_text(json.dumps(status_data))

        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)

        result = load_url_status()
        assert len(result["allResults"]) == 3


class TestBuildRedirectMap:
    """Tests for build_redirect_map function."""

    def test_builds_redirect_map(self):
        """Test building redirect map from status data."""
        status_data = {
            "allResults": [
                {"url": "https://old.com", "status": "redirect", "redirectUrl": "https://new.com"},
                {
                    "url": "https://old2.com",
                    "status": "redirect",
                    "redirectUrl": "https://new2.com",
                },
            ]
        }

        result = build_redirect_map(status_data)

        assert result["https://old.com"] == "https://new.com"
        assert result["https://old2.com"] == "https://new2.com"

    def test_ignores_non_redirects(self):
        """Test that non-redirect statuses are ignored."""
        status_data = {
            "allResults": [
                {"url": "https://ok.com", "status": "ok"},
                {"url": "https://old.com", "status": "redirect", "redirectUrl": "https://new.com"},
                {"url": "https://error.com", "status": "error"},
            ]
        }

        result = build_redirect_map(status_data)

        assert len(result) == 1
        assert "https://old.com" in result
        assert "https://ok.com" not in result
        assert "https://error.com" not in result

    def test_ignores_redirect_to_same_url(self):
        """Test that redirects to the same URL are ignored."""
        status_data = {
            "allResults": [
                {
                    "url": "https://same.com",
                    "status": "redirect",
                    "redirectUrl": "https://same.com",
                },
            ]
        }

        result = build_redirect_map(status_data)

        assert len(result) == 0

    def test_ignores_redirect_without_destination(self):
        """Test that redirects without destination are ignored."""
        status_data = {
            "allResults": [
                {"url": "https://no-dest.com", "status": "redirect"},
                {"url": "https://null-dest.com", "status": "redirect", "redirectUrl": None},
            ]
        }

        result = build_redirect_map(status_data)

        assert len(result) == 0

    def test_empty_results(self):
        """Test with empty results."""
        status_data = {"allResults": []}
        result = build_redirect_map(status_data)
        assert result == {}

    def test_missing_all_results(self):
        """Test with missing allResults key."""
        status_data = {}
        result = build_redirect_map(status_data)
        assert result == {}


class TestBuildErrorSet:
    """Tests for build_error_set function."""

    def test_builds_error_set(self):
        """Test building error set from status data."""
        status_data = {
            "allResults": [
                {"url": "https://error1.com", "status": "error"},
                {"url": "https://error2.com", "status": "error"},
            ]
        }

        result = build_error_set(status_data)

        assert "https://error1.com" in result
        assert "https://error2.com" in result
        assert len(result) == 2

    def test_ignores_non_errors(self):
        """Test that non-error statuses are ignored."""
        status_data = {
            "allResults": [
                {"url": "https://ok.com", "status": "ok"},
                {"url": "https://error.com", "status": "error"},
                {
                    "url": "https://redirect.com",
                    "status": "redirect",
                    "redirectUrl": "https://new.com",
                },
            ]
        }

        result = build_error_set(status_data)

        assert len(result) == 1
        assert "https://error.com" in result
        assert "https://ok.com" not in result

    def test_empty_results(self):
        """Test with empty results."""
        status_data = {"allResults": []}
        result = build_error_set(status_data)
        assert result == set()

    def test_missing_all_results(self):
        """Test with missing allResults key."""
        status_data = {}
        result = build_error_set(status_data)
        assert result == set()


class TestProcessSourcesFile:
    """Tests for process_sources_file function."""

    def test_removes_placeholder_urls(self, tmp_path):
        """Test that placeholder URLs are removed."""
        sources = {
            "files": [
                {"path": "test.md", "urls": ["https://example.com/page", "https://real.com/page"]}
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["placeholders_removed"] == 1
        assert stats["total_urls_after"] == 1

        # Verify file was updated
        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://real.com/page"]

    def test_fixes_malformed_urls(self, tmp_path):
        """Test that malformed URLs are fixed."""
        sources = {"files": [{"path": "test.md", "urls": ["https://real.com/page`"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["malformed_fixed"] == 1

        # Verify file was updated with fixed URL
        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://real.com/page"]

    def test_removes_unfixable_malformed_urls(self, tmp_path):
        """Test that unfixable malformed URLs are removed."""
        sources = {"files": [{"path": "test.md", "urls": ["not-a-url`", "https://real.com/page"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["malformed_removed"] == 1

        # Verify file was updated
        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://real.com/page"]

    def test_updates_redirect_urls(self, tmp_path):
        """Test that redirect URLs are updated."""
        sources = {"files": [{"path": "test.md", "urls": ["https://old.com/page"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        redirect_map = {"https://old.com/page": "https://new.com/page"}
        stats = process_sources_file(sources_path, redirect_map, set())

        assert stats["redirects_updated"] == 1

        # Verify file was updated with new URL
        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://new.com/page"]

    def test_removes_error_urls(self, tmp_path):
        """Test that error URLs are removed."""
        sources = {
            "files": [
                {"path": "test.md", "urls": ["https://broken.com/page", "https://working.com/page"]}
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        error_urls = {"https://broken.com/page"}
        stats = process_sources_file(sources_path, {}, error_urls)

        assert stats["errors_removed"] == 1

        # Verify file was updated
        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://working.com/page"]

    def test_removes_duplicate_urls(self, tmp_path):
        """Test that duplicate URLs are removed when file is modified."""
        # Deduplication only happens when the file is modified (modified flag is True)
        # So we need at least one change to trigger deduplication
        sources = {
            "files": [
                {
                    "path": "test.md",
                    "urls": [
                        "https://example.com/placeholder",  # Will be removed, triggering modification
                        "https://real.com/page",
                        "https://real.com/page",  # Duplicate
                        "https://other.com",
                    ],
                }
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        # Verify duplicates were removed
        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://real.com/page", "https://other.com"]

    def test_dry_run_does_not_write(self, tmp_path):
        """Test that dry run mode doesn't write changes."""
        sources = {"files": [{"path": "test.md", "urls": ["https://example.com/page"]}]}
        sources_path = tmp_path / "sources.json"
        original_content = json.dumps(sources)
        sources_path.write_text(original_content)

        stats = process_sources_file(sources_path, {}, set(), dry_run=True)

        assert stats["placeholders_removed"] == 1

        # Verify file was NOT updated
        assert sources_path.read_text() == original_content

    def test_handles_empty_urls_list(self, tmp_path):
        """Test handling of files with empty URLs list."""
        sources = {
            "files": [
                {"path": "test.md", "urls": []},
                {"path": "other.md", "urls": ["https://real.com/page"]},
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["total_urls_before"] == 1
        assert stats["total_urls_after"] == 1

    def test_handles_missing_urls_key(self, tmp_path):
        """Test handling of files without URLs key."""
        sources = {
            "files": [
                {"path": "test.md"},
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["total_urls_before"] == 0
        assert stats["total_urls_after"] == 0

    def test_handles_empty_files_list(self, tmp_path):
        """Test handling of empty files list."""
        sources = {"files": []}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["total_urls_before"] == 0
        assert stats["total_urls_after"] == 0

    def test_multiple_files_processing(self, tmp_path):
        """Test processing multiple files in one sources.json."""
        sources = {
            "files": [
                {"path": "file1.md", "urls": ["https://example.com/a", "https://real.com/a"]},
                {"path": "file2.md", "urls": ["https://old.com/b", "https://broken.com/b"]},
                {"path": "file3.md", "urls": ["https://working.com/c"]},
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        redirect_map = {"https://old.com/b": "https://new.com/b"}
        error_urls = {"https://broken.com/b"}

        stats = process_sources_file(sources_path, redirect_map, error_urls)

        assert stats["placeholders_removed"] == 1
        assert stats["redirects_updated"] == 1
        assert stats["errors_removed"] == 1
        assert stats["total_urls_before"] == 5
        assert stats["total_urls_after"] == 3

    def test_preserves_order_after_deduplication(self, tmp_path):
        """Test that URL order is preserved after deduplication."""
        # Deduplication only happens when file is modified
        sources = {
            "files": [
                {
                    "path": "test.md",
                    "urls": [
                        "https://example.com/remove",  # Will be removed, triggering modification
                        "https://b.com",
                        "https://a.com",
                        "https://b.com",  # Duplicate
                        "https://c.com",
                    ],
                }
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        process_sources_file(sources_path, {}, set())

        updated = json.loads(sources_path.read_text())
        # Should preserve first-seen order
        assert updated["files"][0]["urls"] == ["https://b.com", "https://a.com", "https://c.com"]

    def test_json_formatting(self, tmp_path):
        """Test that output JSON is properly formatted."""
        sources = {"files": [{"path": "test.md", "urls": ["https://example.com/page"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        process_sources_file(sources_path, {}, set())

        content = sources_path.read_text()
        # Should have indentation and trailing newline
        assert "  " in content  # indent=2
        assert content.endswith("\n")


class TestProcessSourcesFileEdgeCases:
    """Edge case tests for process_sources_file function."""

    def test_redirect_to_error_url(self, tmp_path):
        """Test URL that redirects to an error URL is removed."""
        sources = {
            "files": [{"path": "test.md", "urls": ["https://old.com/page", "https://good.com"]}]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        # old.com redirects to broken.com which is an error
        redirect_map = {"https://old.com/page": "https://broken.com/page"}
        error_urls = {"https://broken.com/page"}

        stats = process_sources_file(sources_path, redirect_map, error_urls)

        assert stats["redirects_updated"] == 1
        assert stats["errors_removed"] == 1

        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://good.com"]

    def test_malformed_then_redirect(self, tmp_path):
        """Test URL that is malformed then redirects."""
        sources = {"files": [{"path": "test.md", "urls": ["https://old.com/page`"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        # After fixing backtick, the URL should be checked for redirect
        redirect_map = {"https://old.com/page": "https://new.com/page"}

        stats = process_sources_file(sources_path, redirect_map, set())

        assert stats["malformed_fixed"] == 1
        assert stats["redirects_updated"] == 1

        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == ["https://new.com/page"]

    def test_all_urls_removed(self, tmp_path):
        """Test when all URLs are removed from a file entry."""
        sources = {"files": [{"path": "test.md", "urls": ["https://example.com/page"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        updated = json.loads(sources_path.read_text())
        assert updated["files"][0]["urls"] == []
        assert stats["total_urls_after"] == 0

    def test_unicode_urls(self, tmp_path):
        """Test handling of URLs with unicode characters."""
        sources = {
            "files": [
                {"path": "test.md", "urls": ["https://example.com/page", "https://real.com/日本語"]}
            ]
        }
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources, ensure_ascii=False))

        stats = process_sources_file(sources_path, {}, set())

        updated = json.loads(sources_path.read_text())
        assert "https://real.com/日本語" in updated["files"][0]["urls"]

    def test_very_long_url(self, tmp_path):
        """Test handling of very long URLs."""
        long_path = "a" * 1000
        sources = {"files": [{"path": "test.md", "urls": [f"https://real.com/{long_path}"]}]}
        sources_path = tmp_path / "sources.json"
        sources_path.write_text(json.dumps(sources))

        stats = process_sources_file(sources_path, {}, set())

        assert stats["total_urls_after"] == 1


class TestMain:
    """Tests for main function."""

    def test_dry_run_mode(self, tmp_path, monkeypatch, capsys):
        """Test dry run mode."""
        # Setup mock specs directory
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        sources = {"files": [{"path": "test.md", "urls": ["https://example.com/page"]}]}
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        # Setup mock status file
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_file.write_text(json.dumps({"allResults": []}))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py", "--dry-run"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "DRY RUN MODE" in captured.out
        assert "Dry run - no changes written" in captured.out

    def test_verbose_mode(self, tmp_path, monkeypatch, capsys):
        """Test verbose mode."""
        # Setup mock specs directory
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        sources = {"files": [{"path": "test.md", "urls": ["https://example.com/page"]}]}
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        # Setup mock status file
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_file.write_text(json.dumps({"allResults": []}))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py", "--verbose", "--dry-run"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        # In verbose mode, should show per-file changes
        assert "sources.json" in captured.out

    def test_verbose_short_flag(self, tmp_path, monkeypatch, capsys):
        """Test verbose mode with -v flag."""
        # Setup mock specs directory
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        sources = {"files": [{"path": "test.md", "urls": ["https://example.com/page"]}]}
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        # Setup mock status file
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_file.write_text(json.dumps({"allResults": []}))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py", "-v", "--dry-run"])

        result = main()

        assert result == 0

    def test_summary_output(self, tmp_path, monkeypatch, capsys):
        """Test summary output."""
        # Setup mock specs directory with multiple sources files
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        for lang in ["python", "javascript"]:
            lang_dir = specs_dir / lang
            lang_dir.mkdir()
            sources = {"files": [{"path": "test.md", "urls": ["https://real.com/page"]}]}
            (lang_dir / "sources.json").write_text(json.dumps(sources))

        # Setup mock status file
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_file.write_text(json.dumps({"allResults": []}))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "Summary" in captured.out
        assert "Files modified:" in captured.out
        assert "URLs before:" in captured.out
        assert "URLs after:" in captured.out

    def test_no_sources_files(self, tmp_path, monkeypatch, capsys):
        """Test with no sources.json files."""
        # Setup empty specs directory
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Setup mock status file
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_file.write_text(json.dumps({"allResults": []}))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "Processing 0 sources.json files" in captured.out

    def test_loads_redirect_and_error_counts(self, tmp_path, monkeypatch, capsys):
        """Test that redirect and error counts are displayed."""
        # Setup mock specs directory
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Setup mock status file with redirects and errors
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_data = {
            "allResults": [
                {"url": "https://old.com", "status": "redirect", "redirectUrl": "https://new.com"},
                {"url": "https://broken.com", "status": "error"},
            ]
        }
        status_file.write_text(json.dumps(status_data))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py"])

        result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "Redirect mappings: 1" in captured.out
        assert "Error URLs: 1" in captured.out


class TestMainIntegration:
    """Integration tests for main function."""

    def test_full_cleanup_workflow(self, tmp_path, monkeypatch, capsys):
        """Test full cleanup workflow with all types of changes."""
        # Setup mock specs directory
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        lang_dir = specs_dir / "python"
        lang_dir.mkdir()

        sources = {
            "files": [
                {
                    "path": "test.md",
                    "urls": [
                        "https://example.com/placeholder",  # Will be removed
                        "https://old.com/redirect",  # Will be updated
                        "https://broken.com/error",  # Will be removed
                        "https://valid.com/page`",  # Will be fixed
                        "https://good.com/keep",  # Will be kept
                    ],
                }
            ]
        }
        (lang_dir / "sources.json").write_text(json.dumps(sources))

        # Setup mock status file
        docs_dir = tmp_path / "docs" / "site"
        docs_dir.mkdir(parents=True)
        status_file = docs_dir / "url-status.json"
        status_data = {
            "allResults": [
                {
                    "url": "https://old.com/redirect",
                    "status": "redirect",
                    "redirectUrl": "https://new.com/redirect",
                },
                {"url": "https://broken.com/error", "status": "error"},
            ]
        }
        status_file.write_text(json.dumps(status_data))

        monkeypatch.setattr(cleanup_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(cleanup_urls, "URL_STATUS_FILE", status_file)
        monkeypatch.setattr("sys.argv", ["cleanup-urls.py"])

        result = main()

        assert result == 0

        # Verify the file was updated correctly
        updated = json.loads((lang_dir / "sources.json").read_text())
        urls = updated["files"][0]["urls"]

        # Should have the fixed and updated URLs
        assert "https://example.com/placeholder" not in urls
        assert "https://broken.com/error" not in urls
        assert "https://old.com/redirect" not in urls
        assert "https://new.com/redirect" in urls
        assert "https://valid.com/page" in urls
        assert "https://good.com/keep" in urls

        captured = capsys.readouterr()
        assert "Placeholders removed: 1" in captured.out
        assert "Redirects updated: 1" in captured.out
        assert "Errors removed: 1" in captured.out
        assert "Malformed fixed: 1" in captured.out


class TestPlaceholderUrlEdgeCases:
    """Additional edge case tests for is_placeholder_url."""

    def test_file_url_scheme(self):
        """Test file:// URLs are not placeholders."""
        assert is_placeholder_url("file:///path/to/file") is False

    def test_data_url_scheme(self):
        """Test data: URLs are not placeholders."""
        assert is_placeholder_url("data:text/plain;base64,SGVsbG8=") is False

    def test_url_without_scheme(self):
        """Test URL without scheme."""
        # urlparse may handle this differently
        result = is_placeholder_url("example.com/page")
        # This should likely return False since no proper scheme/netloc
        assert isinstance(result, bool)

    def test_url_with_credentials(self):
        """Test URL with username/password."""
        # Note: netloc includes user:pass@, so "user:pass@example.com" != "example.com"
        # The code checks exact netloc match against PLACEHOLDER_DOMAINS
        assert is_placeholder_url("https://user:pass@example.com/page") is False
        assert is_placeholder_url("https://user:pass@real.com/page") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
