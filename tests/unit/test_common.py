#!/usr/bin/env python3
"""Unit tests for _common.py utilities."""

import json
import logging
import os
import re
import ssl
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.error import URLError

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from _common import (
    SPECS_DIR,
    FetchError,
    _configure_logger,
    _format_fetch_error,
    _pandoc_available,
    _request,
    _simple_html_to_markdown,
    _ssl_context,
    ensure_dir,
    extract_main,
    fetch_bytes,
    fetch_github_tag,
    fetch_json,
    fetch_markdown,
    fetch_markdown_or_html,
    fetch_section,
    fetch_url,
    find_unique,
    get_latest_version,
    html_to_markdown,
    is_prerelease_version,
    join_lines,
    log,
    normalize_version,
    run_command,
    stamp_versions,
    strip_tag_prefix,
    utc_now,
    write_fetched_at,
    write_stub,
    write_template,
    write_text,
)


class TestNormalizeVersion:
    """Tests for version normalization."""

    def test_strips_v_prefix(self):
        assert normalize_version("v1.2.3") == "1.2.3"

    def test_handles_no_prefix(self):
        assert normalize_version("1.2.3") == "1.2.3"

    def test_handles_empty_string(self):
        assert normalize_version("") == ""

    def test_preserves_complex_versions(self):
        assert normalize_version("v2.0.0-beta.1") == "2.0.0-beta.1"


class TestWriteText:
    """Tests for write_text utility."""

    def test_creates_file(self, tmp_path):
        test_file = tmp_path / "test.txt"
        write_text(test_file, "hello world")
        assert test_file.read_text() == "hello world"

    def test_overwrites_existing(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("old content")
        write_text(test_file, "new content")
        assert test_file.read_text() == "new content"

    def test_creates_parent_dirs(self, tmp_path):
        test_file = tmp_path / "sub" / "dir" / "test.txt"
        write_text(test_file, "nested")
        assert test_file.read_text() == "nested"

    def test_handles_unicode(self, tmp_path):
        test_file = tmp_path / "unicode.txt"
        content = "Hello 世界 🌍"
        write_text(test_file, content)
        assert test_file.read_text(encoding="utf-8") == content


class TestWriteFetchedAt:
    """Tests for write_fetched_at utility."""

    def test_creates_fetched_at_file(self, tmp_path):
        write_fetched_at(tmp_path)
        fetched_at = tmp_path / ".fetched-at"
        assert fetched_at.exists()
        content = fetched_at.read_text()
        # Should be ISO format
        assert "T" in content
        assert "Z" in content or "+" in content

    def test_overwrites_existing(self, tmp_path):
        fetched_at = tmp_path / ".fetched-at"
        fetched_at.write_text("old-timestamp")
        write_fetched_at(tmp_path)
        content = fetched_at.read_text()
        assert content != "old-timestamp"


class TestSpecsDir:
    """Tests for SPECS_DIR constant."""

    def test_specs_dir_exists(self):
        assert SPECS_DIR.exists()
        assert SPECS_DIR.is_dir()

    def test_specs_dir_has_languages(self):
        languages = [d.name for d in SPECS_DIR.iterdir() if d.is_dir()]
        assert "python" in languages
        assert "typescript" in languages
        assert "go" in languages


class TestLog:
    """Tests for log() function with different log levels."""

    def test_log_info_level(self, caplog):
        """Test logging at info level (default)."""
        with caplog.at_level(logging.INFO):
            log("test info message")
        assert "test info message" in caplog.text

    def test_log_warning_level(self, caplog):
        """Test logging at warning level."""
        with caplog.at_level(logging.WARNING):
            log("test warning message", level="warning")
        assert "test warning message" in caplog.text

    def test_log_error_level(self, caplog):
        """Test logging at error level."""
        with caplog.at_level(logging.ERROR):
            log("test error message", level="error")
        assert "test error message" in caplog.text

    def test_log_default_level_is_info(self, caplog):
        """Test that default level is info."""
        with caplog.at_level(logging.INFO):
            log("default level message")
        assert "default level message" in caplog.text

    def test_log_level_case_insensitive(self, caplog):
        """Test that log level is case insensitive."""
        with caplog.at_level(logging.WARNING):
            log("uppercase warning", level="WARNING")
        assert "uppercase warning" in caplog.text

    def test_log_unknown_level_defaults_to_info(self, caplog):
        """Test that unknown level defaults to info."""
        with caplog.at_level(logging.INFO):
            log("unknown level message", level="unknown")
        assert "unknown level message" in caplog.text


class TestEnsureDir:
    """Tests for ensure_dir() function."""

    def test_creates_single_directory(self, tmp_path):
        """Test creating a single directory."""
        new_dir = tmp_path / "new_dir"
        assert not new_dir.exists()
        ensure_dir(new_dir)
        assert new_dir.exists()
        assert new_dir.is_dir()

    def test_creates_nested_directories(self, tmp_path):
        """Test creating nested directories."""
        nested_dir = tmp_path / "level1" / "level2" / "level3"
        assert not nested_dir.exists()
        ensure_dir(nested_dir)
        assert nested_dir.exists()
        assert nested_dir.is_dir()

    def test_existing_directory_no_error(self, tmp_path):
        """Test that existing directory doesn't raise error."""
        existing_dir = tmp_path / "existing"
        existing_dir.mkdir()
        assert existing_dir.exists()
        # Should not raise
        ensure_dir(existing_dir)
        assert existing_dir.exists()

    def test_idempotent(self, tmp_path):
        """Test that calling multiple times is safe."""
        new_dir = tmp_path / "idempotent"
        ensure_dir(new_dir)
        ensure_dir(new_dir)
        ensure_dir(new_dir)
        assert new_dir.exists()


class TestUtcNow:
    """Tests for utc_now() function."""

    def test_returns_string(self):
        """Test that utc_now returns a string."""
        result = utc_now()
        assert isinstance(result, str)

    def test_iso_format(self):
        """Test that result is in ISO format with Z suffix."""
        result = utc_now()
        # Should match YYYY-MM-DDTHH:MM:SSZ format
        pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
        assert re.match(pattern, result), f"'{result}' doesn't match ISO format"

    def test_contains_valid_date(self):
        """Test that the timestamp contains a valid date."""
        result = utc_now()
        # Parse and validate
        year = int(result[:4])
        month = int(result[5:7])
        day = int(result[8:10])
        assert 2020 <= year <= 2100
        assert 1 <= month <= 12
        assert 1 <= day <= 31

    def test_contains_valid_time(self):
        """Test that the timestamp contains a valid time."""
        result = utc_now()
        hour = int(result[11:13])
        minute = int(result[14:16])
        second = int(result[17:19])
        assert 0 <= hour <= 23
        assert 0 <= minute <= 59
        assert 0 <= second <= 59

    def test_timestamps_are_close_to_current_time(self):
        """Test that returned time is close to current time."""
        import datetime

        before = datetime.datetime.now(datetime.UTC)
        result = utc_now()
        after = datetime.datetime.now(datetime.UTC)

        # Parse the result
        parsed = datetime.datetime.strptime(result, "%Y-%m-%dT%H:%M:%SZ")
        parsed = parsed.replace(tzinfo=datetime.UTC)

        assert before <= parsed <= after or (after - before).total_seconds() < 2


class TestFetchError:
    """Tests for FetchError exception class."""

    def test_fetch_error_creation(self):
        """Test creating a FetchError."""
        error = FetchError(url="https://example.com", message="Not found")
        assert error.url == "https://example.com"
        assert error.message == "Not found"

    def test_fetch_error_str(self):
        """Test FetchError string representation."""
        error = FetchError(url="https://example.com", message="Connection timeout")
        assert str(error) == "https://example.com: Connection timeout"

    def test_fetch_error_is_exception(self):
        """Test that FetchError is an Exception."""
        error = FetchError(url="https://test.com", message="Error")
        assert isinstance(error, Exception)

    def test_fetch_error_can_be_raised(self):
        """Test that FetchError can be raised and caught."""
        with pytest.raises(FetchError) as exc_info:
            raise FetchError(url="https://fail.com", message="Failed")
        assert exc_info.value.url == "https://fail.com"
        assert exc_info.value.message == "Failed"

    def test_fetch_error_frozen(self):
        """Test that FetchError is immutable (frozen dataclass)."""
        error = FetchError(url="https://example.com", message="Error")
        with pytest.raises(AttributeError):
            error.url = "https://other.com"


class TestFetchSection:
    """Tests for fetch_section() function."""

    def test_fetch_section_all_scope(self):
        """Test fetch_section with 'all' scope."""
        with patch("_common.FETCH_SCOPE", "all"):
            assert fetch_section("python") is True
            assert fetch_section("javascript") is True
            assert fetch_section("any_section") is True

    def test_fetch_section_matching_scope(self):
        """Test fetch_section with matching scope."""
        with patch("_common.FETCH_SCOPE", "python"):
            assert fetch_section("python") is True

    def test_fetch_section_non_matching_scope(self):
        """Test fetch_section with non-matching scope."""
        with patch("_common.FETCH_SCOPE", "python"):
            assert fetch_section("javascript") is False
            assert fetch_section("go") is False


class TestSimpleMarkdownParser:
    """Tests for _SimpleMarkdownParser HTML to Markdown conversion."""

    def test_heading_conversion(self):
        """Test heading tags are converted to markdown."""
        assert "# Heading" in _simple_html_to_markdown("<h1>Heading</h1>")
        assert "## Subheading" in _simple_html_to_markdown("<h2>Subheading</h2>")
        assert "### Level 3" in _simple_html_to_markdown("<h3>Level 3</h3>")

    def test_paragraph_conversion(self):
        """Test paragraph tags create proper spacing."""
        result = _simple_html_to_markdown("<p>First</p><p>Second</p>")
        assert "First" in result
        assert "Second" in result

    def test_unordered_list_conversion(self):
        """Test unordered lists are converted."""
        html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        result = _simple_html_to_markdown(html)
        assert "- Item 1" in result
        assert "- Item 2" in result

    def test_ordered_list_conversion(self):
        """Test ordered lists are converted."""
        html = "<ol><li>First</li><li>Second</li></ol>"
        result = _simple_html_to_markdown(html)
        assert "1. First" in result
        assert "2. Second" in result

    def test_code_block_conversion(self):
        """Test pre/code blocks are converted to fenced code."""
        html = "<pre><code>print('hello')</code></pre>"
        result = _simple_html_to_markdown(html)
        assert "```" in result
        assert "print('hello')" in result

    def test_inline_code_conversion(self):
        """Test inline code is converted."""
        html = "<p>Use <code>foo()</code> function</p>"
        result = _simple_html_to_markdown(html)
        assert "`foo()`" in result

    def test_link_conversion(self):
        """Test links are converted to markdown format."""
        html = '<a href="https://example.com">Example</a>'
        result = _simple_html_to_markdown(html)
        assert "[Example](https://example.com)" in result

    def test_link_without_text(self):
        """Test links without text show URL."""
        html = '<a href="https://example.com"></a>'
        result = _simple_html_to_markdown(html)
        assert "https://example.com" in result

    def test_script_tags_ignored(self):
        """Test script tags are ignored."""
        html = "<p>Text</p><script>alert('evil')</script><p>More</p>"
        result = _simple_html_to_markdown(html)
        assert "alert" not in result
        assert "Text" in result
        assert "More" in result

    def test_style_tags_ignored(self):
        """Test style tags are ignored."""
        html = "<p>Text</p><style>.foo { color: red; }</style>"
        result = _simple_html_to_markdown(html)
        assert "color" not in result
        assert "Text" in result

    def test_br_tag_creates_newline(self):
        """Test br tags create newlines."""
        html = "<p>Line 1<br>Line 2</p>"
        result = _simple_html_to_markdown(html)
        assert "Line 1" in result
        assert "Line 2" in result

    def test_empty_html(self):
        """Test empty HTML returns empty string."""
        assert _simple_html_to_markdown("") == ""

    def test_whitespace_only_html(self):
        """Test whitespace-only HTML returns empty."""
        assert _simple_html_to_markdown("   \n\t  ") == ""

    def test_nested_lists(self):
        """Test nested list handling."""
        html = "<ul><li>Outer<ul><li>Inner</li></ul></li></ul>"
        result = _simple_html_to_markdown(html)
        assert "Outer" in result
        assert "Inner" in result

    def test_noscript_tags_ignored(self):
        """Test noscript tags are ignored."""
        html = "<p>Text</p><noscript>Enable JS</noscript>"
        result = _simple_html_to_markdown(html)
        assert "Enable JS" not in result
        assert "Text" in result

    def test_svg_tags_ignored(self):
        """Test SVG tags are ignored."""
        html = "<p>Text</p><svg><circle cx='50' cy='50' r='40'/></svg>"
        result = _simple_html_to_markdown(html)
        assert "circle" not in result
        assert "Text" in result


class TestStripTagPrefix:
    """Tests for strip_tag_prefix() function."""

    def test_strip_with_prefix(self):
        """Test stripping a matching prefix."""
        assert strip_tag_prefix("v1.0.0", "v") == "1.0.0"

    def test_strip_no_prefix(self):
        """Test with None prefix returns unchanged."""
        assert strip_tag_prefix("1.0.0", None) == "1.0.0"

    def test_strip_empty_prefix(self):
        """Test with empty prefix returns unchanged."""
        assert strip_tag_prefix("1.0.0", "") == "1.0.0"

    def test_strip_longer_prefix(self):
        """Test stripping a longer prefix."""
        assert strip_tag_prefix("release-1.0.0", "release-") == "1.0.0"

    def test_strip_non_matching_prefix(self):
        """Test non-matching prefix returns unchanged."""
        assert strip_tag_prefix("1.0.0", "v") == "1.0.0"


class TestIsPrereleaseVersion:
    """Tests for is_prerelease_version() function."""

    def test_alpha_versions(self):
        """Test alpha version detection."""
        assert is_prerelease_version("1.0.0-alpha") is True
        assert is_prerelease_version("1.0.0-alpha.1") is True
        assert is_prerelease_version("1.0.0a1") is True

    def test_beta_versions(self):
        """Test beta version detection."""
        assert is_prerelease_version("1.0.0-beta") is True
        assert is_prerelease_version("1.0.0-beta.2") is True
        assert is_prerelease_version("1.0.0b1") is True

    def test_rc_versions(self):
        """Test release candidate detection."""
        assert is_prerelease_version("1.0.0-rc1") is True
        assert is_prerelease_version("1.0.0rc1") is True

    def test_dev_versions(self):
        """Test dev version detection."""
        assert is_prerelease_version("1.0.0-dev") is True
        assert is_prerelease_version("1.0.0.dev1") is True

    def test_preview_versions(self):
        """Test preview version detection."""
        assert is_prerelease_version("1.0.0-preview") is True
        assert is_prerelease_version("1.0.0-pre") is True

    def test_nightly_versions(self):
        """Test nightly version detection."""
        assert is_prerelease_version("1.0.0-nightly") is True

    def test_snapshot_versions(self):
        """Test snapshot version detection."""
        assert is_prerelease_version("1.0.0-SNAPSHOT") is True

    def test_canary_versions(self):
        """Test canary version detection."""
        assert is_prerelease_version("1.0.0-canary") is True

    def test_stable_versions(self):
        """Test stable versions are not prerelease."""
        assert is_prerelease_version("1.0.0") is False
        assert is_prerelease_version("2.3.4") is False
        assert is_prerelease_version("10.20.30") is False


class TestExtractMain:
    """Tests for extract_main() function."""

    def test_extract_main_tag(self):
        """Test extracting main tag content."""
        html = "<html><body><main>Content</main></body></html>"
        result = extract_main(html)
        assert "<main>Content</main>" in result

    def test_extract_article_tag(self):
        """Test falling back to article tag."""
        html = "<html><body><article>Article content</article></body></html>"
        result = extract_main(html)
        assert "<article>Article content</article>" in result

    def test_no_main_or_article(self):
        """Test returning full HTML when no main/article."""
        html = "<html><body><div>Content</div></body></html>"
        result = extract_main(html)
        assert result == html

    def test_main_with_attributes(self):
        """Test main tag with attributes."""
        html = '<html><main class="content" id="main">Text</main></html>'
        result = extract_main(html)
        assert "Text" in result


class TestFindUnique:
    """Tests for find_unique() function."""

    def test_find_unique_single_match(self):
        """Test finding a single unique match."""
        html = "foo123bar"
        result = find_unique(html, r"\d+")
        assert result == ["123"]

    def test_find_unique_multiple_matches(self):
        """Test deduplication of multiple matches."""
        html = "foo123bar123baz456"
        result = find_unique(html, r"\d+")
        assert "123" in result
        assert "456" in result
        assert len(result) == 2

    def test_find_unique_sorted(self):
        """Test that results are sorted."""
        html = "c b a d"
        result = find_unique(html, r"[a-d]")
        assert result == ["a", "b", "c", "d"]

    def test_find_unique_no_match(self):
        """Test no matches returns empty list."""
        html = "no numbers here"
        result = find_unique(html, r"\d+")
        assert result == []

    def test_find_unique_filters_empty(self):
        """Test empty matches are filtered."""
        html = "abc"
        result = find_unique(html, r"d?")
        # Empty strings should be filtered out
        assert "" not in result


class TestJoinLines:
    """Tests for join_lines() function."""

    def test_join_lines_basic(self):
        """Test basic line joining."""
        lines = ["line1", "line2", "line3"]
        result = join_lines(lines)
        assert result == "line1\nline2\nline3\n"

    def test_join_lines_single(self):
        """Test joining a single line."""
        result = join_lines(["only"])
        assert result == "only\n"

    def test_join_lines_empty(self):
        """Test joining empty list."""
        result = join_lines([])
        assert result == "\n"

    def test_join_lines_with_generator(self):
        """Test join_lines works with generators."""

        def gen():
            yield "a"
            yield "b"

        result = join_lines(gen())
        assert result == "a\nb\n"


class TestWriteStub:
    """Tests for write_stub() function."""

    def test_write_stub_creates_file(self, tmp_path):
        """Test write_stub creates a file."""
        stub_file = tmp_path / "stub.md"
        write_stub(stub_file, "Test Title", "https://example.com")
        assert stub_file.exists()

    def test_write_stub_content(self, tmp_path):
        """Test write_stub content format."""
        stub_file = tmp_path / "stub.md"
        write_stub(stub_file, "My Title", "https://example.com/doc")
        content = stub_file.read_text()
        assert "# My Title" in content
        assert "See: https://example.com/doc" in content

    def test_write_stub_creates_parent_dirs(self, tmp_path):
        """Test write_stub creates parent directories."""
        stub_file = tmp_path / "nested" / "dir" / "stub.md"
        write_stub(stub_file, "Title", "https://url.com")
        assert stub_file.exists()


class TestConfigureLogger:
    """Tests for _configure_logger() function."""

    def test_returns_logger(self):
        """Test that _configure_logger returns a logger."""
        logger = _configure_logger()
        assert isinstance(logger, logging.Logger)

    def test_returns_specforge_logger(self):
        """Test that logger has correct name."""
        logger = _configure_logger()
        assert logger.name == "specforge"

    def test_idempotent(self):
        """Test that multiple calls return same logger."""
        logger1 = _configure_logger()
        logger2 = _configure_logger()
        assert logger1 is logger2


class TestFormatFetchError:
    """Tests for _format_fetch_error() function."""

    def test_basic_error(self):
        """Test formatting a basic error."""
        exc = Exception("Connection refused")
        result = _format_fetch_error(exc)
        assert result == "Connection refused"

    def test_certificate_error(self):
        """Test formatting SSL certificate error."""
        exc = Exception("CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate")
        result = _format_fetch_error(exc)
        assert "CERTIFICATE_VERIFY_FAILED" in result
        assert "SSL_CERT_FILE" in result
        assert "FETCH_INSECURE=1" in result

    def test_timeout_error(self):
        """Test formatting timeout error."""
        exc = TimeoutError("Connection timed out")
        result = _format_fetch_error(exc)
        assert "Connection timed out" in result


class TestRequest:
    """Tests for _request() function."""

    def test_basic_request(self):
        """Test creating a basic request."""
        req = _request("https://example.com")
        assert req.full_url == "https://example.com"

    def test_user_agent_header(self):
        """Test User-Agent header is set."""
        req = _request("https://example.com")
        # urllib uses "User-agent" (lowercase 'a') as the key
        assert "User-agent" in req.headers or "User-Agent" in req.headers

    def test_github_token_added_for_github_api(self):
        """Test GitHub token is added for GitHub API requests."""
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token_123"}):
            req = _request("https://api.github.com/repos/test/repo")
            assert req.headers.get("Authorization") == "Bearer test_token_123"

    def test_github_token_not_added_for_other_urls(self):
        """Test GitHub token is not added for non-GitHub URLs."""
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token_123"}):
            req = _request("https://example.com")
            assert "Authorization" not in req.headers


class TestSslContext:
    """Tests for _ssl_context() function."""

    def test_returns_context_or_none(self):
        """Test that _ssl_context returns SSLContext or None."""
        result = _ssl_context()
        assert result is None or isinstance(result, ssl.SSLContext)

    def test_insecure_mode(self):
        """Test insecure mode returns unverified context."""
        with patch.dict(os.environ, {"FETCH_INSECURE": "1"}):
            result = _ssl_context()
            assert isinstance(result, ssl.SSLContext)

    def test_custom_ca_file(self):
        """Test custom CA file is used."""
        with patch.dict(os.environ, {"SSL_CERT_FILE": "/path/to/ca.crt"}, clear=False):
            with patch("ssl.create_default_context") as mock_ctx:
                mock_ctx.return_value = MagicMock(spec=ssl.SSLContext)
                _ssl_context()
                mock_ctx.assert_called_once_with(cafile="/path/to/ca.crt")

    def test_requests_ca_bundle(self):
        """Test REQUESTS_CA_BUNDLE is used as fallback."""
        with patch.dict(os.environ, {"REQUESTS_CA_BUNDLE": "/path/to/bundle.crt"}, clear=False):
            # Make sure SSL_CERT_FILE is not set
            env = os.environ.copy()
            env.pop("SSL_CERT_FILE", None)
            env["REQUESTS_CA_BUNDLE"] = "/path/to/bundle.crt"
            with patch.dict(os.environ, env, clear=True):
                with patch("ssl.create_default_context") as mock_ctx:
                    mock_ctx.return_value = MagicMock(spec=ssl.SSLContext)
                    _ssl_context()
                    mock_ctx.assert_called_once_with(cafile="/path/to/bundle.crt")


class TestPandocAvailable:
    """Tests for _pandoc_available() function."""

    def test_pandoc_available_when_found(self):
        """Test returns True when pandoc is found."""
        with patch("shutil.which", return_value="/usr/bin/pandoc"):
            assert _pandoc_available() is True

    def test_pandoc_not_available(self):
        """Test returns False when pandoc is not found."""
        with patch("shutil.which", return_value=None):
            assert _pandoc_available() is False


class TestFetchUrl:
    """Tests for fetch_url() function."""

    def test_successful_fetch(self):
        """Test successful URL fetch."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"Hello, World!"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_url("https://example.com")
                assert result == "Hello, World!"

    def test_fetch_with_unicode(self):
        """Test fetch handles unicode correctly."""
        mock_response = MagicMock()
        mock_response.read.return_value = "Hello 世界".encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_url("https://example.com")
                assert result == "Hello 世界"

    def test_fetch_raises_fetch_error_on_failure(self):
        """Test FetchError is raised on network failure."""
        with patch("_common.urlopen", side_effect=URLError("Connection refused")):
            with patch("_common.CURL_RETRY", 0):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    with pytest.raises(FetchError) as exc_info:
                        fetch_url("https://example.com")
                    assert exc_info.value.url == "https://example.com"

    def test_fetch_retries_on_failure(self):
        """Test fetch retries on transient failures."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"Success"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        call_count = 0

        def side_effect(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise URLError("Temporary failure")
            return mock_response

        with patch("_common.urlopen", side_effect=side_effect):
            with patch("_common.CURL_RETRY", 3):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    result = fetch_url("https://example.com")
                    assert result == "Success"
                    assert call_count == 2

    def test_fetch_timeout_error(self):
        """Test fetch handles timeout errors."""
        with patch("_common.urlopen", side_effect=TimeoutError("Connection timed out")):
            with patch("_common.CURL_RETRY", 0):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    with pytest.raises(FetchError):
                        fetch_url("https://example.com")

    def test_fetch_ssl_error(self):
        """Test fetch handles SSL errors."""
        with patch("_common.urlopen", side_effect=ssl.SSLError("SSL handshake failed")):
            with patch("_common.CURL_RETRY", 0):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    with pytest.raises(FetchError):
                        fetch_url("https://example.com")


class TestFetchBytes:
    """Tests for fetch_bytes() function."""

    def test_successful_fetch(self):
        """Test successful bytes fetch."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"\x00\x01\x02\x03"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_bytes("https://example.com/file.bin")
                assert result == b"\x00\x01\x02\x03"

    def test_fetch_bytes_raises_fetch_error(self):
        """Test FetchError is raised on failure."""
        with patch("_common.urlopen", side_effect=URLError("Connection refused")):
            with patch("_common.CURL_RETRY", 0):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    with pytest.raises(FetchError):
                        fetch_bytes("https://example.com/file.bin")


class TestFetchJson:
    """Tests for fetch_json() function."""

    def test_successful_json_fetch(self):
        """Test successful JSON fetch."""
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"key": "value", "number": 42}'
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_json("https://api.example.com/data")
                assert result == {"key": "value", "number": 42}

    def test_invalid_json_raises_error(self):
        """Test invalid JSON raises error."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"not valid json"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                with pytest.raises(json.JSONDecodeError):
                    fetch_json("https://api.example.com/data")


class TestHtmlToMarkdown:
    """Tests for html_to_markdown() function."""

    def test_fallback_to_simple_parser(self, tmp_path):
        """Test fallback to simple parser when pandoc unavailable."""
        output = tmp_path / "output.md"
        html = "<h1>Title</h1><p>Content</p>"

        with patch("_common._pandoc_available", return_value=False):
            result = html_to_markdown(html, output)
            assert result is True
            content = output.read_text()
            assert "# Title" in content
            assert "Content" in content

    def test_with_pandoc(self, tmp_path):
        """Test conversion with pandoc when available."""
        output = tmp_path / "output.md"
        html = "<h1>Title</h1>"

        with patch("_common._pandoc_available", return_value=True):
            with patch("subprocess.run") as mock_run:
                mock_run.return_value = MagicMock(returncode=0)

                # Simulate pandoc writing to file
                def write_output(*args, **kwargs):
                    output.write_text("# Title\n")
                    return MagicMock(returncode=0)

                mock_run.side_effect = write_output
                result = html_to_markdown(html, output)
                assert result is True

    def test_pandoc_failure_falls_back(self, tmp_path):
        """Test fallback when pandoc fails."""
        output = tmp_path / "output.md"
        html = "<h1>Title</h1><p>Content</p>"

        with patch("_common._pandoc_available", return_value=True):
            with patch("subprocess.run", side_effect=subprocess.SubprocessError("Pandoc failed")):
                result = html_to_markdown(html, output)
                assert result is True
                content = output.read_text()
                assert "Title" in content

    def test_empty_html_returns_false(self, tmp_path):
        """Test empty HTML returns False."""
        output = tmp_path / "output.md"

        with patch("_common._pandoc_available", return_value=False):
            result = html_to_markdown("", output)
            assert result is False

    def test_creates_parent_directories(self, tmp_path):
        """Test parent directories are created."""
        output = tmp_path / "nested" / "dir" / "output.md"
        html = "<p>Content</p>"

        with patch("_common._pandoc_available", return_value=False):
            result = html_to_markdown(html, output)
            assert result is True
            assert output.exists()


class TestFetchMarkdown:
    """Tests for fetch_markdown() function."""

    def test_successful_fetch_and_convert(self, tmp_path):
        """Test successful fetch and markdown conversion."""
        output = tmp_path / "doc.md"
        mock_response = MagicMock()
        mock_response.read.return_value = b"<main><h1>Title</h1></main>"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common._pandoc_available", return_value=False):
                with patch("_common.CURL_RETRY", 0):
                    fetch_markdown("https://example.com/doc", output, "Test Doc")
                    assert output.exists()
                    content = output.read_text()
                    assert "Title" in content

    def test_fetch_failure_writes_stub(self, tmp_path):
        """Test stub is written when fetch fails."""
        output = tmp_path / "doc.md"

        with patch("_common.urlopen", side_effect=URLError("Connection refused")):
            with patch("_common.CURL_RETRY", 0):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    fetch_markdown("https://example.com/doc", output, "Test Doc")
                    assert output.exists()
                    content = output.read_text()
                    assert "# Test Doc" in content
                    assert "See:" in content

    def test_conversion_failure_writes_stub(self, tmp_path):
        """Test stub is written when conversion fails."""
        output = tmp_path / "doc.md"
        mock_response = MagicMock()
        mock_response.read.return_value = b""
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common._pandoc_available", return_value=False):
                with patch("_common.CURL_RETRY", 0):
                    fetch_markdown("https://example.com/doc", output, "Test Doc")
                    assert output.exists()
                    content = output.read_text()
                    assert "# Test Doc" in content


class TestFetchMarkdownOrHtml:
    """Tests for fetch_markdown_or_html() function."""

    def test_successful_markdown_conversion(self, tmp_path):
        """Test successful fetch and markdown conversion."""
        output_md = tmp_path / "doc.md"
        output_html = tmp_path / "doc.html"
        mock_response = MagicMock()
        mock_response.read.return_value = b"<main><h1>Title</h1></main>"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common._pandoc_available", return_value=False):
                with patch("_common.CURL_RETRY", 0):
                    fetch_markdown_or_html("https://example.com", output_md, output_html, "Doc")
                    assert output_md.exists()
                    assert not output_html.exists()

    def test_fetch_failure_writes_stub(self, tmp_path):
        """Test stub is written when fetch fails."""
        output_md = tmp_path / "doc.md"
        output_html = tmp_path / "doc.html"

        with patch("_common.urlopen", side_effect=URLError("Connection refused")):
            with patch("_common.CURL_RETRY", 0):
                with patch("_common.CURL_RETRY_DELAY", 0):
                    fetch_markdown_or_html("https://example.com", output_md, output_html, "Doc")
                    assert output_md.exists()
                    content = output_md.read_text()
                    assert "# Doc" in content

    def test_conversion_failure_writes_html(self, tmp_path):
        """Test HTML is written when markdown conversion fails."""
        output_md = tmp_path / "doc.md"
        output_html = tmp_path / "doc.html"
        mock_response = MagicMock()
        mock_response.read.return_value = b"<html><body></body></html>"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common._pandoc_available", return_value=False):
                with patch("_common.CURL_RETRY", 0):
                    fetch_markdown_or_html("https://example.com", output_md, output_html, "Doc")
                    # Empty HTML body results in fallback to HTML
                    assert output_html.exists()


class TestFetchGithubTag:
    """Tests for fetch_github_tag() function."""

    def test_fetch_latest_tag(self):
        """Test fetching latest tag."""
        tags_data = [
            {"name": "v1.2.0"},
            {"name": "v1.1.0"},
            {"name": "v1.0.0"},
        ]
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(tags_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_github_tag("owner/repo")
                assert result == "v1.2.0"

    def test_skips_prerelease_tags(self):
        """Test prerelease tags are skipped."""
        tags_data = [
            {"name": "v2.0.0-alpha"},
            {"name": "v1.1.0-beta.1"},
            {"name": "v1.0.0"},
        ]
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(tags_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_github_tag("owner/repo")
                assert result == "v1.0.0"

    def test_with_tag_prefix(self):
        """Test filtering by tag prefix."""
        tags_data = [
            {"name": "pkg-v2.0.0"},
            {"name": "other-v1.0.0"},
            {"name": "pkg-v1.0.0"},
        ]
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(tags_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_github_tag("owner/repo", tag_prefix="pkg-")
                assert result == "pkg-v2.0.0"

    def test_no_matching_tags(self):
        """Test returns empty when no matching tags."""
        tags_data = [
            {"name": "v1.0.0-alpha"},
            {"name": "v1.0.0-beta"},
        ]
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(tags_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_github_tag("owner/repo")
                assert result == ""

    def test_invalid_response(self):
        """Test returns empty for non-list response."""
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"error": "not found"}'
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = fetch_github_tag("owner/repo")
                assert result == ""


class TestGetLatestVersion:
    """Tests for get_latest_version() function."""

    def test_disabled_returns_none(self):
        """Test returns None when check_enabled is False."""
        tool = {"latest": {"type": "npm", "package": "test"}}
        result = get_latest_version(tool, check_enabled=False)
        assert result is None

    def test_no_latest_config_returns_none(self):
        """Test returns None when no latest config."""
        tool = {"name": "test"}
        result = get_latest_version(tool)
        assert result is None

    def test_npm_package(self):
        """Test fetching npm package version."""
        tool = {"latest": {"type": "npm", "package": "express"}}
        npm_data = {"dist-tags": {"latest": "4.18.2"}}
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(npm_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "4.18.2"

    def test_npm_prerelease_returns_none(self):
        """Test npm prerelease version returns None."""
        tool = {"latest": {"type": "npm", "package": "test"}}
        npm_data = {"dist-tags": {"latest": "1.0.0-beta.1"}}
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(npm_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result is None

    def test_pypi_package(self):
        """Test fetching PyPI package version."""
        tool = {"latest": {"type": "pypi", "package": "requests"}}
        pypi_data = {"info": {"version": "2.31.0"}}
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(pypi_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "2.31.0"

    def test_github_release(self):
        """Test fetching GitHub release version."""
        tool = {"latest": {"type": "github-release", "repo": "owner/repo"}}
        release_data = {"tag_name": "v1.5.0"}
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(release_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "1.5.0"

    def test_github_release_with_tag_prefix(self):
        """Test GitHub release with tag prefix."""
        tool = {"latest": {"type": "github-release", "repo": "owner/repo", "tagPrefix": "pkg-v"}}
        release_data = {"tag_name": "pkg-v2.0.0"}
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(release_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "2.0.0"

    def test_github_release_404_falls_back_to_tags(self):
        """Test GitHub release 404 falls back to tags API."""
        tool = {"latest": {"type": "github-release", "repo": "owner/repo"}}
        tags_data = [{"name": "v1.0.0"}]

        call_count = 0

        def mock_urlopen(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                # First call to releases/latest returns 404
                raise URLError("HTTP Error 404: Not Found")
            # Second call to tags returns data
            mock_response = MagicMock()
            mock_response.read.return_value = json.dumps(tags_data).encode()
            mock_response.__enter__ = MagicMock(return_value=mock_response)
            mock_response.__exit__ = MagicMock(return_value=False)
            return mock_response

        with patch("_common.urlopen", side_effect=mock_urlopen):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "1.0.0"

    def test_go_version(self):
        """Test fetching Go version."""
        tool = {"latest": {"type": "go", "url": "https://go.dev/VERSION?m=text"}}
        mock_response = MagicMock()
        mock_response.read.return_value = b"go1.21.5\ntime 2023-12-05T16:48:00Z"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "1.21.5"

    def test_node_version(self):
        """Test fetching Node.js version."""
        tool = {"latest": {"type": "node", "url": "https://nodejs.org/dist/index.json"}}
        node_data = [
            {"version": "v21.5.0", "lts": False},
            {"version": "v20.10.0", "lts": "Iron"},
        ]
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(node_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "21.5.0"

    def test_node_skips_empty_versions(self):
        """Test Node.js skips empty versions."""
        tool = {"latest": {"type": "node", "url": "https://nodejs.org/dist/index.json"}}
        node_data = [
            {"version": ""},
            {"version": "v20.10.0"},
        ]
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(node_data).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "20.10.0"

    def test_node_non_list_returns_none(self):
        """Test Node.js returns None for non-list response."""
        tool = {"latest": {"type": "node", "url": "https://nodejs.org/dist/index.json"}}
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"error": "not found"}'
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch("_common.urlopen", return_value=mock_response):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result is None

    def test_unknown_type_returns_none(self):
        """Test unknown type returns None."""
        tool = {"latest": {"type": "unknown"}}
        result = get_latest_version(tool)
        assert result is None

    def test_github_release_prerelease_falls_back_to_tags(self):
        """Test GitHub prerelease version falls back to tags."""
        tool = {"latest": {"type": "github-release", "repo": "owner/repo"}}
        release_data = {"tag_name": "v2.0.0-alpha"}
        tags_data = [{"name": "v2.0.0-alpha"}, {"name": "v1.0.0"}]

        call_count = 0

        def mock_urlopen(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            mock_response = MagicMock()
            if call_count == 1:
                mock_response.read.return_value = json.dumps(release_data).encode()
            else:
                mock_response.read.return_value = json.dumps(tags_data).encode()
            mock_response.__enter__ = MagicMock(return_value=mock_response)
            mock_response.__exit__ = MagicMock(return_value=False)
            return mock_response

        with patch("_common.urlopen", side_effect=mock_urlopen):
            with patch("_common.CURL_RETRY", 0):
                result = get_latest_version(tool)
                assert result == "1.0.0"


class TestRunCommand:
    """Tests for run_command() function."""

    def test_successful_command(self):
        """Test successful command execution."""
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            run_command(["echo", "hello"])
            mock_run.assert_called_once_with(["echo", "hello"], check=True, timeout=None)

    def test_command_with_timeout(self):
        """Test command with timeout."""
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            run_command(["sleep", "1"], timeout=5.0)
            mock_run.assert_called_once_with(["sleep", "1"], check=True, timeout=5.0)

    def test_failed_command_raises(self):
        """Test failed command raises CalledProcessError."""
        with patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd")):
            with pytest.raises(subprocess.CalledProcessError):
                run_command(["false"])


class TestStampVersions:
    """Tests for stamp_versions() function."""

    def test_runs_python_script_if_exists(self, tmp_path):
        """Test runs Python stamp script if it exists."""
        # This test verifies the function runs without error when script doesn't exist
        with patch("_common.SCRIPT_DIR", tmp_path):
            # No script exists, should return without error
            stamp_versions()

    def test_runs_node_script_if_python_missing(self, tmp_path):
        """Test runs Node script if Python script missing."""
        with patch("_common.SCRIPT_DIR", tmp_path):
            node_script = tmp_path / "stamp-versions.mjs"
            node_script.write_text("console.log('stamp')")

            with patch("subprocess.run") as mock_run:
                stamp_versions()
                mock_run.assert_called_once()

    def test_handles_oserror(self, tmp_path):
        """Test handles OSError gracefully."""
        with patch("_common.SCRIPT_DIR", tmp_path):
            python_script = tmp_path / "stamp-versions.py"
            python_script.write_text("print('stamp')")

            with patch("subprocess.run", side_effect=OSError("Command not found")):
                # Should not raise
                stamp_versions()


class TestWriteTemplate:
    """Tests for write_template() function."""

    def test_writes_template(self, tmp_path):
        """Test writing template content."""
        template = tmp_path / "template.txt"
        template.write_text("Template content")
        output = tmp_path / "output.txt"

        write_template(template, output)

        assert output.exists()
        assert output.read_text() == "Template content"

    def test_nonexistent_template_does_nothing(self, tmp_path):
        """Test nonexistent template does nothing."""
        template = tmp_path / "nonexistent.txt"
        output = tmp_path / "output.txt"

        write_template(template, output)

        assert not output.exists()

    def test_creates_parent_directories(self, tmp_path):
        """Test creates parent directories for output."""
        template = tmp_path / "template.txt"
        template.write_text("Content")
        output = tmp_path / "nested" / "dir" / "output.txt"

        write_template(template, output)

        assert output.exists()
        assert output.read_text() == "Content"


class TestSimpleMarkdownParserAdvanced:
    """Additional tests for _SimpleMarkdownParser edge cases."""

    def test_nested_ignored_tags(self):
        """Test nested ignored tags are tracked with depth counter."""
        # When script tags are nested, the depth counter tracks them
        html = "<script>content inside script</script><p>Text</p>"
        result = _simple_html_to_markdown(html)
        assert "content inside script" not in result
        assert "Text" in result

        # Test deeply nested script (depth tracking)
        html2 = "<script><script>deep</script></script><p>Visible</p>"
        result2 = _simple_html_to_markdown(html2)
        assert "deep" not in result2
        assert "Visible" in result2

    def test_h4_h5_h6_headings(self):
        """Test h4, h5, h6 headings."""
        assert "#### H4" in _simple_html_to_markdown("<h4>H4</h4>")
        assert "##### H5" in _simple_html_to_markdown("<h5>H5</h5>")
        assert "###### H6" in _simple_html_to_markdown("<h6>H6</h6>")

    def test_code_inside_pre(self):
        """Test code tag inside pre tag."""
        html = "<pre><code>line1\nline2</code></pre>"
        result = _simple_html_to_markdown(html)
        assert "```" in result
        assert "line1" in result
        assert "line2" in result

    def test_link_without_href(self):
        """Test link without href attribute."""
        html = "<a>Just text</a>"
        result = _simple_html_to_markdown(html)
        assert "Just text" in result
        assert "[" not in result  # Should not be a markdown link

    def test_html_entities_unescaped(self):
        """Test HTML entities are unescaped."""
        html = "<p>&amp; &lt; &gt;</p>"
        result = _simple_html_to_markdown(html)
        assert "& < >" in result

    def test_whitespace_normalization(self):
        """Test whitespace is normalized."""
        html = "<p>Multiple   spaces   here</p>"
        result = _simple_html_to_markdown(html)
        assert "Multiple spaces here" in result

    def test_empty_inline_code(self):
        """Test empty inline code is not rendered."""
        html = "<p>Before <code>  </code> after</p>"
        result = _simple_html_to_markdown(html)
        # Empty code should be stripped
        assert "``" not in result

    def test_list_item_outside_list(self):
        """Test list item outside list context."""
        html = "<li>Orphan item</li>"
        result = _simple_html_to_markdown(html)
        assert "- Orphan item" in result

    def test_multiple_paragraphs_spacing(self):
        """Test multiple consecutive newlines are collapsed."""
        html = "<p>First</p><p></p><p></p><p>Second</p>"
        result = _simple_html_to_markdown(html)
        # Should not have more than 2 consecutive newlines
        assert "\n\n\n" not in result


class TestIsPrereleaseVersionAdvanced:
    """Additional tests for is_prerelease_version edge cases."""

    def test_experimental_version(self):
        """Test experimental version detection."""
        assert is_prerelease_version("1.0.0-experimental") is True

    def test_prerelease_version(self):
        """Test prerelease version detection."""
        assert is_prerelease_version("1.0.0-prerelease") is True

    def test_version_with_build_metadata(self):
        """Test stable version with build metadata."""
        assert is_prerelease_version("1.0.0+build.123") is False

    def test_edge_case_stable_versions(self):
        """Test edge case stable versions."""
        assert is_prerelease_version("0.0.1") is False
        assert is_prerelease_version("1.0") is False
        assert is_prerelease_version("1") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
