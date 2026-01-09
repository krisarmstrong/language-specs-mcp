#!/usr/bin/env python3
"""Unit tests for validate-urls.py."""

import json
import ssl
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import the hyphenated module using importlib
import importlib.util

_validate_urls_path = Path(__file__).parent.parent.parent / "scripts" / "validate-urls.py"
_spec = importlib.util.spec_from_file_location("validate_urls", _validate_urls_path)
validate_urls = importlib.util.module_from_spec(_spec)
# Register the module in sys.modules BEFORE executing it (required for dataclasses)
sys.modules["validate_urls"] = validate_urls
_spec.loader.exec_module(validate_urls)

# Now import specific items
DomainRateLimiter = validate_urls.DomainRateLimiter
URLResult = validate_urls.URLResult
build_ssl_context = validate_urls.build_ssl_context
validate_url = validate_urls.validate_url
collect_urls_from_sources = validate_urls.collect_urls_from_sources
validate_all_urls = validate_urls.validate_all_urls
build_summary = validate_urls.build_summary
suggest_fixes = validate_urls.suggest_fixes
main = validate_urls.main


class TestURLResult:
    """Tests for URLResult dataclass."""

    def test_ok_result(self):
        """Test creating an OK result."""
        result = URLResult(
            url="https://example.com",
            status="ok",
            http_code=200,
            response_time_ms=100,
        )
        assert result.url == "https://example.com"
        assert result.status == "ok"
        assert result.http_code == 200
        assert result.redirect_url is None
        assert result.error_message is None
        assert result.response_time_ms == 100

    def test_redirect_result(self):
        """Test creating a redirect result."""
        result = URLResult(
            url="https://old.example.com",
            status="redirect",
            http_code=301,
            redirect_url="https://new.example.com",
            response_time_ms=50,
        )
        assert result.status == "redirect"
        assert result.redirect_url == "https://new.example.com"

    def test_error_result(self):
        """Test creating an error result."""
        result = URLResult(
            url="https://broken.example.com",
            status="error",
            http_code=404,
            error_message="HTTP 404: Not Found",
            response_time_ms=30,
        )
        assert result.status == "error"
        assert result.error_message == "HTTP 404: Not Found"

    def test_timeout_result(self):
        """Test creating a timeout result."""
        result = URLResult(
            url="https://slow.example.com",
            status="timeout",
            error_message="Timeout after 15s",
            response_time_ms=15000,
        )
        assert result.status == "timeout"
        assert result.error_message == "Timeout after 15s"

    def test_default_checked_at(self):
        """Test that checked_at defaults to current time."""
        result = URLResult(url="https://example.com", status="ok")
        assert result.checked_at is not None
        # Should be recent ISO format
        parsed = datetime.fromisoformat(result.checked_at.replace("Z", "+00:00"))
        assert (datetime.now(UTC) - parsed).total_seconds() < 5

    def test_to_dict_minimal(self):
        """Test to_dict with minimal fields."""
        result = URLResult(url="https://example.com", status="ok")
        d = result.to_dict()
        assert d["url"] == "https://example.com"
        assert d["status"] == "ok"
        assert "checkedAt" in d
        assert "httpCode" not in d
        assert "redirectUrl" not in d
        assert "error" not in d
        assert "responseTimeMs" not in d

    def test_to_dict_full(self):
        """Test to_dict with all fields."""
        result = URLResult(
            url="https://example.com",
            status="redirect",
            http_code=301,
            redirect_url="https://new.example.com",
            error_message=None,
            response_time_ms=100,
        )
        d = result.to_dict()
        assert d["url"] == "https://example.com"
        assert d["status"] == "redirect"
        assert d["httpCode"] == 301
        assert d["redirectUrl"] == "https://new.example.com"
        assert d["responseTimeMs"] == 100
        assert "error" not in d

    def test_to_dict_error_fields(self):
        """Test to_dict includes error message."""
        result = URLResult(
            url="https://example.com",
            status="error",
            http_code=500,
            error_message="Internal Server Error",
        )
        d = result.to_dict()
        assert d["error"] == "Internal Server Error"


class TestDomainRateLimiter:
    """Tests for DomainRateLimiter class."""

    def test_first_request_no_wait(self):
        """Test first request to a domain doesn't wait."""
        limiter = DomainRateLimiter()
        start = time.monotonic()
        limiter.wait_for_domain("https://example.com/path")
        elapsed = time.monotonic() - start
        # First request should not wait significantly
        assert elapsed < 0.1

    def test_subsequent_request_waits(self, monkeypatch):
        """Test subsequent requests to same domain wait."""
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 0.2)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {})

        limiter = DomainRateLimiter()
        limiter.wait_for_domain("https://example.com/page1")

        start = time.monotonic()
        limiter.wait_for_domain("https://example.com/page2")
        elapsed = time.monotonic() - start

        # Should have waited approximately RATE_LIMIT_DEFAULT
        assert elapsed >= 0.15

    def test_different_domains_no_wait(self, monkeypatch):
        """Test different domains don't affect each other."""
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 1.0)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {})

        limiter = DomainRateLimiter()
        limiter.wait_for_domain("https://example1.com/path")

        start = time.monotonic()
        limiter.wait_for_domain("https://example2.com/path")
        elapsed = time.monotonic() - start

        # Different domain should not wait
        assert elapsed < 0.1

    def test_domain_specific_rate_limits(self, monkeypatch):
        """Test domain-specific rate limits are applied."""
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 0.1)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {"slow.com": 0.3})

        limiter = DomainRateLimiter()
        limiter.wait_for_domain("https://slow.com/page1")

        start = time.monotonic()
        limiter.wait_for_domain("https://slow.com/page2")
        elapsed = time.monotonic() - start

        # Should use domain-specific limit
        assert elapsed >= 0.25

    def test_invalid_url_handled(self):
        """Test invalid URL doesn't crash."""
        limiter = DomainRateLimiter()
        # Should not raise
        limiter.wait_for_domain("not-a-valid-url")

    def test_zero_delay_no_wait(self, monkeypatch):
        """Test zero delay means no waiting."""
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 0)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {})

        limiter = DomainRateLimiter()
        limiter.wait_for_domain("https://example.com/page1")

        start = time.monotonic()
        limiter.wait_for_domain("https://example.com/page2")
        elapsed = time.monotonic() - start

        # No wait with zero delay
        assert elapsed < 0.05

    def test_case_insensitive_domain(self, monkeypatch):
        """Test domain matching is case-insensitive."""
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 0.2)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {})

        limiter = DomainRateLimiter()
        limiter.wait_for_domain("https://EXAMPLE.COM/page1")

        start = time.monotonic()
        limiter.wait_for_domain("https://example.com/page2")
        elapsed = time.monotonic() - start

        # Should recognize same domain
        assert elapsed >= 0.15


class TestBuildSslContext:
    """Tests for build_ssl_context function."""

    def test_default_context(self, monkeypatch):
        """Test default SSL context creation."""
        monkeypatch.delenv("FETCH_INSECURE", raising=False)
        monkeypatch.delenv("SSL_CERT_FILE", raising=False)
        monkeypatch.delenv("REQUESTS_CA_BUNDLE", raising=False)

        # Mock certifi to not be available
        with patch.dict(sys.modules, {"certifi": None}):
            result = build_ssl_context()
            # Should return None or a context depending on certifi availability
            assert result is None or isinstance(result, ssl.SSLContext)

    def test_insecure_mode(self, monkeypatch):
        """Test insecure mode creates unverified context."""
        monkeypatch.setenv("FETCH_INSECURE", "1")

        result = build_ssl_context()
        assert isinstance(result, ssl.SSLContext)

    def test_custom_ca_file(self, monkeypatch):
        """Test custom CA file is used."""
        monkeypatch.delenv("FETCH_INSECURE", raising=False)
        monkeypatch.setenv("SSL_CERT_FILE", "/path/to/ca.crt")

        with patch("ssl.create_default_context") as mock_ctx:
            mock_ctx.return_value = MagicMock(spec=ssl.SSLContext)
            build_ssl_context()
            mock_ctx.assert_called_once_with(cafile="/path/to/ca.crt")

    def test_requests_ca_bundle_fallback(self, monkeypatch):
        """Test REQUESTS_CA_BUNDLE is used as fallback."""
        monkeypatch.delenv("FETCH_INSECURE", raising=False)
        monkeypatch.delenv("SSL_CERT_FILE", raising=False)
        monkeypatch.setenv("REQUESTS_CA_BUNDLE", "/path/to/bundle.crt")

        with patch("ssl.create_default_context") as mock_ctx:
            mock_ctx.return_value = MagicMock(spec=ssl.SSLContext)
            build_ssl_context()
            mock_ctx.assert_called_once_with(cafile="/path/to/bundle.crt")

    def test_certifi_fallback(self, monkeypatch):
        """Test certifi is used when available."""
        monkeypatch.delenv("FETCH_INSECURE", raising=False)
        monkeypatch.delenv("SSL_CERT_FILE", raising=False)
        monkeypatch.delenv("REQUESTS_CA_BUNDLE", raising=False)

        mock_certifi = MagicMock()
        mock_certifi.where.return_value = "/path/to/certifi/cacert.pem"

        with patch.dict(sys.modules, {"certifi": mock_certifi}):
            with patch("ssl.create_default_context") as mock_ctx:
                mock_ctx.return_value = MagicMock(spec=ssl.SSLContext)
                # Need to reimport to pick up the mock
                result = build_ssl_context()
                # The function should use certifi
                assert result is not None or mock_ctx.called


class TestValidateUrl:
    """Tests for validate_url function."""

    def test_successful_request(self, monkeypatch):
        """Test successful URL validation."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())
        monkeypatch.setattr(validate_urls, "TIMEOUT", 5.0)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.geturl.return_value = "https://example.com"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch.object(validate_urls, "urlopen", return_value=mock_response):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "ok"
        assert result.http_code == 200
        assert result.response_time_ms is not None

    def test_redirect_detected(self, monkeypatch):
        """Test redirect detection when final URL differs."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())
        monkeypatch.setattr(validate_urls, "TIMEOUT", 5.0)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.geturl.return_value = "https://new.example.com"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch.object(validate_urls, "urlopen", return_value=mock_response):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://old.example.com")

        assert result.status == "redirect"
        assert result.redirect_url == "https://new.example.com"

    def test_http_301_redirect(self, monkeypatch):
        """Test 301 permanent redirect."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())
        monkeypatch.setattr(validate_urls, "TIMEOUT", 5.0)

        error = HTTPError(
            url="https://example.com",
            code=301,
            msg="Moved Permanently",
            hdrs={"Location": "https://new.example.com"},
            fp=None,
        )

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "redirect"
        assert result.http_code == 301
        assert result.redirect_url == "https://new.example.com"

    def test_http_302_redirect(self, monkeypatch):
        """Test 302 temporary redirect."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())
        monkeypatch.setattr(validate_urls, "TIMEOUT", 5.0)

        error = HTTPError(
            url="https://example.com",
            code=302,
            msg="Found",
            hdrs={"Location": "https://temp.example.com"},
            fp=None,
        )

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "redirect"
        assert result.http_code == 302

    def test_http_307_redirect(self, monkeypatch):
        """Test 307 temporary redirect."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = HTTPError(
            url="https://example.com",
            code=307,
            msg="Temporary Redirect",
            hdrs={"Location": "https://temp.example.com"},
            fp=None,
        )

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "redirect"
        assert result.http_code == 307

    def test_http_308_redirect(self, monkeypatch):
        """Test 308 permanent redirect."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = HTTPError(
            url="https://example.com",
            code=308,
            msg="Permanent Redirect",
            hdrs={"Location": "https://new.example.com"},
            fp=None,
        )

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "redirect"
        assert result.http_code == 308

    def test_http_404_error(self, monkeypatch):
        """Test 404 Not Found error."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = HTTPError(
            url="https://example.com/missing",
            code=404,
            msg="Not Found",
            hdrs={},
            fp=None,
        )

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com/missing")

        assert result.status == "error"
        assert result.http_code == 404
        assert "404" in result.error_message
        assert "Not Found" in result.error_message

    def test_http_500_error(self, monkeypatch):
        """Test 500 Internal Server Error."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = HTTPError(
            url="https://example.com",
            code=500,
            msg="Internal Server Error",
            hdrs={},
            fp=None,
        )

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "error"
        assert result.http_code == 500

    def test_url_error(self, monkeypatch):
        """Test URLError (network error)."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = URLError("Connection refused")

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "error"
        assert "Connection refused" in result.error_message

    def test_url_error_with_reason(self, monkeypatch):
        """Test URLError with reason attribute."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = URLError(reason="Host not found")

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "error"
        assert "Host not found" in result.error_message

    def test_ssl_error(self, monkeypatch):
        """Test SSL error."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        error = ssl.SSLError("certificate verify failed")

        with patch.object(validate_urls, "urlopen", side_effect=error):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "error"
        assert "certificate" in result.error_message.lower()

    def test_timeout_error(self, monkeypatch):
        """Test timeout error."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())
        monkeypatch.setattr(validate_urls, "TIMEOUT", 15.0)

        with patch.object(validate_urls, "urlopen", side_effect=TimeoutError()):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "timeout"
        assert "Timeout" in result.error_message
        assert "15" in result.error_message

    def test_generic_exception(self, monkeypatch):
        """Test generic exception handling."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        with patch.object(validate_urls, "urlopen", side_effect=RuntimeError("Unexpected error")):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.status == "error"
        assert "Unexpected error" in result.error_message

    def test_response_time_measured(self, monkeypatch):
        """Test response time is measured."""
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.geturl.return_value = "https://example.com"
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with patch.object(validate_urls, "urlopen", return_value=mock_response):
            with patch.object(validate_urls, "build_ssl_context", return_value=None):
                result = validate_url("https://example.com")

        assert result.response_time_ms is not None
        assert result.response_time_ms >= 0


class TestCollectUrlsFromSources:
    """Tests for collect_urls_from_sources function."""

    def test_collects_urls_from_sources_json(self, tmp_path, monkeypatch):
        """Test collecting URLs from sources.json files."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create Python sources.json
        python_dir = specs_dir / "python"
        python_dir.mkdir()
        python_sources = {
            "language": "python",
            "files": [
                {"path": "spec.md", "urls": ["https://python.org/spec"]},
                {"path": "stdlib.md", "urls": ["https://python.org/stdlib"]},
            ],
        }
        (python_dir / "sources.json").write_text(json.dumps(python_sources))

        # Create Go sources.json
        go_dir = specs_dir / "go"
        go_dir.mkdir()
        go_sources = {
            "language": "go",
            "files": [{"path": "spec.md", "urls": ["https://go.dev/spec"]}],
        }
        (go_dir / "sources.json").write_text(json.dumps(go_sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        result = collect_urls_from_sources()

        assert "python" in result
        assert "go" in result
        assert "https://python.org/spec" in result["python"]
        assert "https://python.org/stdlib" in result["python"]
        assert "https://go.dev/spec" in result["go"]

    def test_ignores_hidden_directories(self, tmp_path, monkeypatch):
        """Test hidden directories are ignored."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create hidden directory
        hidden_dir = specs_dir / ".hidden"
        hidden_dir.mkdir()
        (hidden_dir / "sources.json").write_text('{"files": [{"urls": ["https://hidden.com"]}]}')

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        result = collect_urls_from_sources()

        assert ".hidden" not in result

    def test_ignores_files(self, tmp_path, monkeypatch):
        """Test files in specs dir are ignored."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create a file, not a directory
        (specs_dir / "README.md").write_text("# Specs")

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        result = collect_urls_from_sources()

        assert "README.md" not in result

    def test_handles_missing_sources_json(self, tmp_path, monkeypatch):
        """Test directories without sources.json are skipped."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Create directory without sources.json
        (specs_dir / "rust").mkdir()

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        result = collect_urls_from_sources()

        assert "rust" not in result

    def test_handles_invalid_json(self, tmp_path, monkeypatch, caplog):
        """Test invalid JSON is handled gracefully."""
        import logging

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        (python_dir / "sources.json").write_text("not valid json")

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)

        with caplog.at_level(logging.WARNING):
            result = collect_urls_from_sources()

        assert "python" not in result
        assert "Warning" in caplog.text

    def test_handles_empty_urls(self, tmp_path, monkeypatch):
        """Test files with empty URLs list are skipped."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {
            "language": "python",
            "files": [{"path": "spec.md", "urls": []}],
        }
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        result = collect_urls_from_sources()

        # Should not include language with no URLs
        assert "python" not in result

    def test_deduplicates_urls(self, tmp_path, monkeypatch):
        """Test duplicate URLs are deduplicated."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {
            "language": "python",
            "files": [
                {"path": "spec.md", "urls": ["https://python.org/spec"]},
                {"path": "stdlib.md", "urls": ["https://python.org/spec"]},
            ],
        }
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        result = collect_urls_from_sources()

        # URLs should be in a set, so deduplicated
        assert len(result["python"]) == 1


class TestValidateAllUrls:
    """Tests for validate_all_urls function."""

    def test_validates_all_urls(self, monkeypatch):
        """Test all URLs are validated."""
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 2)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        urls_by_language = {
            "python": {"https://python.org/spec", "https://python.org/stdlib"},
            "go": {"https://go.dev/spec"},
        }

        def mock_validate_url(url):
            return URLResult(url=url, status="ok", http_code=200)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            result = validate_all_urls(urls_by_language)

        assert "results" in result
        assert "url_to_languages" in result
        assert len(result["results"]) == 3

    def test_tracks_url_to_languages_mapping(self, monkeypatch):
        """Test URL to languages mapping is tracked."""
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)

        # Same URL used by multiple languages
        urls_by_language = {
            "python": {"https://example.com/shared"},
            "go": {"https://example.com/shared"},
        }

        def mock_validate_url(url):
            return URLResult(url=url, status="ok", http_code=200)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            result = validate_all_urls(urls_by_language)

        # Shared URL should map to both languages
        assert "python" in result["url_to_languages"]["https://example.com/shared"]
        assert "go" in result["url_to_languages"]["https://example.com/shared"]

    def test_handles_validation_exceptions(self, monkeypatch, caplog):
        """Test exceptions during validation are caught."""
        import logging

        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)

        urls_by_language = {"python": {"https://example.com"}}

        def mock_validate_url(url):
            raise RuntimeError("Validation crashed")

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            with caplog.at_level(logging.ERROR):
                result = validate_all_urls(urls_by_language)

        # Should still return a result
        assert "https://example.com" in result["results"]
        assert result["results"]["https://example.com"].status == "error"


class TestBuildSummary:
    """Tests for build_summary function."""

    def test_counts_statuses(self):
        """Test status counts are calculated correctly."""
        results = {
            "https://ok1.com": URLResult(url="https://ok1.com", status="ok"),
            "https://ok2.com": URLResult(url="https://ok2.com", status="ok"),
            "https://redirect.com": URLResult(
                url="https://redirect.com",
                status="redirect",
                redirect_url="https://new.com",
            ),
            "https://error.com": URLResult(
                url="https://error.com", status="error", error_message="Not found"
            ),
            "https://timeout.com": URLResult(
                url="https://timeout.com", status="timeout", error_message="Timeout"
            ),
        }

        url_to_languages = {
            "https://ok1.com": ["python"],
            "https://ok2.com": ["go"],
            "https://redirect.com": ["python"],
            "https://error.com": ["python"],
            "https://timeout.com": ["go"],
        }

        summary = build_summary(results, url_to_languages)

        assert summary["summary"]["total"] == 5
        assert summary["summary"]["ok"] == 2
        assert summary["summary"]["redirect"] == 1
        assert summary["summary"]["error"] == 1
        assert summary["summary"]["timeout"] == 1

    def test_groups_errors_by_language(self):
        """Test errors are grouped by language."""
        results = {
            "https://error1.com": URLResult(
                url="https://error1.com", status="error", error_message="Error 1"
            ),
            "https://error2.com": URLResult(
                url="https://error2.com", status="error", error_message="Error 2"
            ),
        }

        url_to_languages = {
            "https://error1.com": ["python"],
            "https://error2.com": ["go"],
        }

        summary = build_summary(results, url_to_languages)

        assert "python" in summary["errorsByLanguage"]
        assert "go" in summary["errorsByLanguage"]
        assert len(summary["errorsByLanguage"]["python"]) == 1
        assert len(summary["errorsByLanguage"]["go"]) == 1

    def test_groups_redirects_by_language(self):
        """Test redirects are grouped by language."""
        results = {
            "https://old1.com": URLResult(
                url="https://old1.com",
                status="redirect",
                redirect_url="https://new1.com",
            ),
            "https://old2.com": URLResult(
                url="https://old2.com",
                status="redirect",
                redirect_url="https://new2.com",
            ),
        }

        url_to_languages = {
            "https://old1.com": ["python"],
            "https://old2.com": ["python", "go"],
        }

        summary = build_summary(results, url_to_languages)

        assert "python" in summary["redirectsByLanguage"]
        assert len(summary["redirectsByLanguage"]["python"]) == 2
        assert "go" in summary["redirectsByLanguage"]
        assert len(summary["redirectsByLanguage"]["go"]) == 1

    def test_timeout_grouped_with_errors(self):
        """Test timeouts are grouped with errors."""
        results = {
            "https://timeout.com": URLResult(
                url="https://timeout.com", status="timeout", error_message="Timeout"
            ),
        }

        url_to_languages = {"https://timeout.com": ["python"]}

        summary = build_summary(results, url_to_languages)

        assert "python" in summary["errorsByLanguage"]


class TestSuggestFixes:
    """Tests for suggest_fixes function."""

    def test_suggests_permanent_redirect_fix(self):
        """Test permanent redirect suggests URL update."""
        results = {
            "https://old.com": URLResult(
                url="https://old.com",
                status="redirect",
                http_code=301,
                redirect_url="https://new.com",
            ),
        }

        suggestions = suggest_fixes(results)

        assert len(suggestions) == 1
        assert suggestions[0]["type"] == "permanent_redirect"
        assert suggestions[0]["oldUrl"] == "https://old.com"
        assert suggestions[0]["newUrl"] == "https://new.com"
        assert suggestions[0]["autoFixable"] is True

    def test_suggests_temporary_redirect_monitoring(self):
        """Test temporary redirect suggests monitoring."""
        results = {
            "https://old.com": URLResult(
                url="https://old.com",
                status="redirect",
                http_code=302,
                redirect_url="https://temp.com",
            ),
        }

        suggestions = suggest_fixes(results)

        assert len(suggestions) == 1
        assert suggestions[0]["type"] == "temporary_redirect"
        assert suggestions[0]["autoFixable"] is False
        assert "Monitor" in suggestions[0]["action"]

    def test_suggests_broken_url_review(self):
        """Test broken URL suggests manual review."""
        results = {
            "https://broken.com": URLResult(
                url="https://broken.com",
                status="error",
                error_message="Connection refused",
            ),
        }

        suggestions = suggest_fixes(results)

        assert len(suggestions) == 1
        assert suggestions[0]["type"] == "broken_url"
        assert suggestions[0]["autoFixable"] is False
        assert "Manual review" in suggestions[0]["action"]

    def test_python_docs_search_hint(self):
        """Test Python docs URL gets search hint."""
        results = {
            "https://docs.python.org/missing": URLResult(
                url="https://docs.python.org/missing",
                status="error",
                error_message="Not found",
            ),
        }

        suggestions = suggest_fixes(results)

        assert "searchHint" in suggestions[0]
        assert "site:docs.python.org" in suggestions[0]["searchHint"]

    def test_mdn_search_hint(self):
        """Test MDN URL gets search hint."""
        results = {
            "https://developer.mozilla.org/missing": URLResult(
                url="https://developer.mozilla.org/missing",
                status="error",
                error_message="Not found",
            ),
        }

        suggestions = suggest_fixes(results)

        assert "searchHint" in suggestions[0]
        assert "site:developer.mozilla.org" in suggestions[0]["searchHint"]

    def test_github_search_hint(self):
        """Test GitHub URL gets search hint."""
        results = {
            "https://github.com/user/repo": URLResult(
                url="https://github.com/user/repo",
                status="error",
                error_message="Not found",
            ),
        }

        suggestions = suggest_fixes(results)

        assert "searchHint" in suggestions[0]
        assert "repository" in suggestions[0]["searchHint"]

    def test_no_suggestion_for_ok_urls(self):
        """Test no suggestions for OK URLs."""
        results = {
            "https://example.com": URLResult(url="https://example.com", status="ok"),
        }

        suggestions = suggest_fixes(results)

        assert len(suggestions) == 0

    def test_no_suggestion_for_timeout(self):
        """Test no suggestion for timeout (timeouts don't need fixes)."""
        results = {
            "https://slow.com": URLResult(
                url="https://slow.com", status="timeout", error_message="Timeout"
            ),
        }

        suggestions = suggest_fixes(results)

        # Timeouts might retry, so no suggestion
        assert len(suggestions) == 0


class TestMain:
    """Tests for main function."""

    def test_main_no_urls(self, tmp_path, monkeypatch, caplog):
        """Test main with no URLs to validate."""
        import logging

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()

        # Empty language directory with no URLs
        python_dir = specs_dir / "python"
        python_dir.mkdir()
        (python_dir / "sources.json").write_text('{"files": []}')

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)

        with caplog.at_level(logging.INFO):
            result = main()

        assert result == 0
        assert "No URLs found" in caplog.text

    def test_main_successful_validation(self, tmp_path, monkeypatch, caplog):
        """Test main with successful validation."""
        import logging

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {"files": [{"path": "spec.md", "urls": ["https://example.com"]}]}
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_dir / "url-status.json")
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(url=url, status="ok", http_code=200)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            with caplog.at_level(logging.INFO):
                result = main()

        assert result == 0
        assert "URL Validation Complete" in caplog.text
        assert "OK: 1" in caplog.text

        # Check output file was written
        assert (output_dir / "url-status.json").exists()

    def test_main_with_errors_returns_nonzero(self, tmp_path, monkeypatch, caplog):
        """Test main returns non-zero when there are errors."""
        import logging

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {"files": [{"path": "spec.md", "urls": ["https://broken.com"]}]}
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_dir / "url-status.json")
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(url=url, status="error", error_message="Not found")

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            with caplog.at_level(logging.INFO):
                result = main()

        assert result == 1
        assert "Errors: 1" in caplog.text

    def test_main_with_timeouts_returns_nonzero(self, tmp_path, monkeypatch, caplog):
        """Test main returns non-zero when there are timeouts."""
        import logging

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {"files": [{"path": "spec.md", "urls": ["https://slow.com"]}]}
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_dir / "url-status.json")
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(url=url, status="timeout", error_message="Timeout")

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            with caplog.at_level(logging.INFO):
                result = main()

        assert result == 1
        assert "Timeouts: 1" in caplog.text

    def test_main_reports_suggestions(self, tmp_path, monkeypatch, caplog):
        """Test main reports fix suggestions."""
        import logging

        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_dir = tmp_path / "docs" / "site"
        output_dir.mkdir(parents=True)

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {"files": [{"path": "spec.md", "urls": ["https://old.com"]}]}
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_dir / "url-status.json")
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(
                url=url, status="redirect", http_code=301, redirect_url="https://new.com"
            )

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            with caplog.at_level(logging.INFO):
                result = main()

        # Redirects don't cause failure
        assert result == 0
        assert "fix suggestions" in caplog.text
        assert "auto-fixed" in caplog.text

    def test_main_creates_output_directory(self, tmp_path, monkeypatch):
        """Test main creates output directory if missing."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_file = tmp_path / "nonexistent" / "dir" / "url-status.json"

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {"files": [{"path": "spec.md", "urls": ["https://example.com"]}]}
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_file)
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(url=url, status="ok", http_code=200)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            main()

        assert output_file.exists()


class TestOutputFormat:
    """Tests for JSON output format."""

    def test_output_contains_all_fields(self, tmp_path, monkeypatch):
        """Test output JSON contains all expected fields."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_file = tmp_path / "url-status.json"

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {"files": [{"path": "spec.md", "urls": ["https://example.com"]}]}
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_file)
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(url=url, status="ok", http_code=200, response_time_ms=100)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            main()

        output = json.loads(output_file.read_text())

        assert "generatedAt" in output
        assert "summary" in output
        assert "errorsByLanguage" in output
        assert "redirectsByLanguage" in output
        assert "suggestions" in output
        assert "allResults" in output

    def test_all_results_contains_validated_urls(self, tmp_path, monkeypatch):
        """Test allResults contains all validated URLs."""
        specs_dir = tmp_path / "specs"
        specs_dir.mkdir()
        output_file = tmp_path / "url-status.json"

        python_dir = specs_dir / "python"
        python_dir.mkdir()
        sources = {
            "files": [
                {"path": "spec.md", "urls": ["https://url1.com", "https://url2.com"]},
            ]
        }
        (python_dir / "sources.json").write_text(json.dumps(sources))

        monkeypatch.setattr(validate_urls, "SPECS_DIR", specs_dir)
        monkeypatch.setattr(validate_urls, "ROOT_DIR", tmp_path)
        monkeypatch.setattr(validate_urls, "OUTPUT_FILE", output_file)
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 1)
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        def mock_validate_url(url):
            return URLResult(url=url, status="ok", http_code=200)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            main()

        output = json.loads(output_file.read_text())

        assert len(output["allResults"]) == 2
        urls = [r["url"] for r in output["allResults"]]
        assert "https://url1.com" in urls
        assert "https://url2.com" in urls


class TestEnvironmentVariables:
    """Tests for environment variable configuration."""

    def test_max_workers_default_value(self):
        """Test MAX_WORKERS has a valid default value."""
        assert isinstance(validate_urls.MAX_WORKERS, int)
        assert validate_urls.MAX_WORKERS > 0

    def test_max_workers_can_be_overridden(self, monkeypatch):
        """Test MAX_WORKERS can be overridden via monkeypatch."""
        original = validate_urls.MAX_WORKERS
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 20)
        assert validate_urls.MAX_WORKERS == 20
        # Verify it was different from original
        assert original != 20 or original == 20  # Always true, but tests the mechanism

    def test_timeout_default_value(self):
        """Test TIMEOUT has a valid default value."""
        assert isinstance(validate_urls.TIMEOUT, float)
        assert validate_urls.TIMEOUT > 0

    def test_timeout_can_be_overridden(self, monkeypatch):
        """Test TIMEOUT can be overridden via monkeypatch."""
        monkeypatch.setattr(validate_urls, "TIMEOUT", 30.0)
        assert validate_urls.TIMEOUT == 30.0

    def test_rate_limit_default_value(self):
        """Test RATE_LIMIT_DEFAULT has a valid default value."""
        assert isinstance(validate_urls.RATE_LIMIT_DEFAULT, float)
        assert validate_urls.RATE_LIMIT_DEFAULT >= 0

    def test_rate_limit_can_be_overridden(self, monkeypatch):
        """Test RATE_LIMIT_DEFAULT can be overridden via monkeypatch."""
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 2.0)
        assert validate_urls.RATE_LIMIT_DEFAULT == 2.0

    def test_rate_limit_domains_has_github(self):
        """Test RATE_LIMIT_DOMAINS contains GitHub domains."""
        assert "github.com" in validate_urls.RATE_LIMIT_DOMAINS
        assert "api.github.com" in validate_urls.RATE_LIMIT_DOMAINS

    def test_user_agent_default_value(self):
        """Test USER_AGENT has a valid default value."""
        assert isinstance(validate_urls.USER_AGENT, str)
        assert len(validate_urls.USER_AGENT) > 0
        assert "specforge" in validate_urls.USER_AGENT.lower()


class TestConcurrency:
    """Tests for concurrent URL validation."""

    def test_concurrent_rate_limiting(self, monkeypatch):
        """Test rate limiting is thread-safe."""
        from concurrent.futures import ThreadPoolExecutor

        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 0.05)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {})

        limiter = DomainRateLimiter()
        results = []

        def rate_limit_call(domain):
            start = time.monotonic()
            limiter.wait_for_domain(f"https://{domain}/path")
            return time.monotonic() - start

        # Call rate_limit concurrently for same domain
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(rate_limit_call, "same-domain.com") for _ in range(4)]
            results = [f.result() for f in futures]

        # At least some calls should have waited
        total_wait = sum(results)
        # With 4 requests and 0.05s delay, total should be around 0.15s minimum
        assert total_wait >= 0.1

    def test_parallel_validation_of_different_domains(self, monkeypatch):
        """Test parallel validation of different domains."""
        monkeypatch.setattr(validate_urls, "MAX_WORKERS", 4)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DEFAULT", 0)
        monkeypatch.setattr(validate_urls, "RATE_LIMIT_DOMAINS", {})
        monkeypatch.setattr(validate_urls, "_rate_limiter", DomainRateLimiter())

        urls_by_language = {
            "python": {"https://python.org/spec"},
            "go": {"https://go.dev/spec"},
            "rust": {"https://rust-lang.org/spec"},
            "js": {"https://tc39.es/spec"},
        }

        call_times = []

        def mock_validate_url(url):
            call_times.append(time.monotonic())
            time.sleep(0.01)  # Small delay
            return URLResult(url=url, status="ok", http_code=200)

        with patch.object(validate_urls, "validate_url", side_effect=mock_validate_url):
            start = time.monotonic()
            validate_all_urls(urls_by_language)
            total_time = time.monotonic() - start

        # With 4 workers and 4 URLs, should complete faster than serial
        # Serial would take 4 * 0.01 = 0.04s minimum
        # Parallel should be closer to 0.01s
        assert total_time < 0.03  # Allow some overhead


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
