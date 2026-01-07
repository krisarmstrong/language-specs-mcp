# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.6.x   | :white_check_mark: |
| < 1.6   | :x:                |

## Reporting a Vulnerability

Please do not open public issues for security vulnerabilities.

Use GitHub Security Advisories for private disclosure:
https://docs.github.com/en/code-security/security-advisories/creating-a-security-advisory

If you cannot use Security Advisories, contact the project maintainer directly.

## Security Considerations

### URL Fetching

SpecForge MCP fetches content from external URLs defined in `sources.json` files. Security measures include:

- **Rate limiting**: Per-domain rate limiting prevents abuse (configurable via `FETCH_RATE_LIMIT`)
- **Timeout protection**: All requests have configurable timeouts (`FETCH_TIMEOUT`)
- **SSL/TLS validation**: Certificate validation is enabled by default
- **User-Agent identification**: Requests identify as `specforge-mcp` for transparency

To disable SSL verification (not recommended for production):
```bash
FETCH_INSECURE=1 python scripts/fetch.py
```

### Input Validation

- All file paths are validated to prevent directory traversal
- URLs are validated before fetching
- JSON inputs are parsed with standard library (no eval)

### Dependencies

Known security considerations:

- **MCP SDK**: Check for updates regularly
- **Node.js dependencies**: Run `npm audit` to check for vulnerabilities
- **Python dependencies**: Minimal external dependencies used

### Environment Variables

Sensitive configuration should use environment variables:

| Variable | Purpose | Default |
|----------|---------|---------|
| `FETCH_USER_AGENT` | Custom user agent | `specforge-mcp/1.0` |
| `FETCH_TIMEOUT` | Request timeout (seconds) | `30` |
| `FETCH_INSECURE` | Disable SSL verification | `0` (disabled) |
| `SSL_CERT_FILE` | Custom CA certificate bundle | System default |

### File System Access

The MCP server has read access to the `specs/` directory. Write operations are limited to:

- Fetched spec files in `specs/<language>/`
- Generated index files (`search.json`, `index.json`)
- Timestamp markers (`.fetched-at`)

### Best Practices

1. **Run in isolation**: Use containers or VMs for untrusted environments
2. **Limit permissions**: Run with minimum required file system access
3. **Monitor logs**: Check for unusual activity in fetch logs
4. **Keep updated**: Regularly update dependencies and spec content
5. **Validate sources**: Review `sources.json` changes before merging

## Dependency Auditing

Run periodic security audits:

```bash
# Node.js dependencies
npm audit

# Python (if using pip-audit)
pip-audit

# Check for outdated dependencies
npm outdated
```
