# OWASP Top 10 (2021)

The ten most critical web application security risks.

## A01:2021 - Broken Access Control

Access control enforces policy so users cannot act outside their intended permissions.

### Vulnerabilities

- Bypassing access control checks by modifying URL, application state, or HTML page
- Allowing primary key to be changed to another user's record (IDOR)
- Elevation of privilege (acting as user without login, or as admin when logged in as user)
- Metadata manipulation (replaying/tampering JWT, cookie, hidden field)
- CORS misconfiguration allowing unauthorized API access
- Force browsing to authenticated pages or privileged pages

### Prevention

```python
# BAD - Direct object reference without authorization check
@app.get("/api/users/{user_id}/profile")
async def get_profile(user_id: int):
    return await db.get_user(user_id)  # Anyone can access any profile!

# GOOD - Verify authorization
@app.get("/api/users/{user_id}/profile")
async def get_profile(user_id: int, current_user: User = Depends(get_current_user)):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Access denied")
    return await db.get_user(user_id)
```

```typescript
// BAD - No ownership check
app.delete('/api/posts/:id', async (req, res) => {
  await Post.findByIdAndDelete(req.params.id) // Anyone can delete any post!
})

// GOOD - Verify ownership
app.delete('/api/posts/:id', authenticate, async (req, res) => {
  const post = await Post.findById(req.params.id)
  if (!post) return res.status(404).json({ error: 'Not found' })
  if (post.authorId !== req.user.id && req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Access denied' })
  }
  await post.deleteOne()
  res.status(204).send()
})
```

### Key Controls

- Deny by default (except for public resources)
- Implement access control mechanisms once, reuse throughout application
- Enforce record ownership rather than accepting user-submitted data
- Disable web server directory listing
- Log access control failures, alert on repeated failures
- Rate limit API access to minimize automated attack damage
- Invalidate JWT tokens on server after logout

---

## A02:2021 - Cryptographic Failures

Failures related to cryptography which often lead to sensitive data exposure.

### Vulnerabilities

- Transmitting data in clear text (HTTP, SMTP, FTP)
- Using old or weak cryptographic algorithms (MD5, SHA1, DES, RC4)
- Using default or weak crypto keys
- Not enforcing encryption (missing security headers)
- Not properly validating server certificates
- Using encryption without authenticated encryption modes

### Prevention

```python
# BAD - Weak hashing for passwords
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()  # NEVER!

# GOOD - Use proper password hashing
from argon2 import PasswordHasher
ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
password_hash = ph.hash(password)
```

```python
# BAD - ECB mode doesn't hide patterns
from Crypto.Cipher import AES
cipher = AES.new(key, AES.MODE_ECB)  # Patterns visible in ciphertext!

# GOOD - Use authenticated encryption (GCM)
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

nonce = get_random_bytes(12)
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
# Store: nonce + tag + ciphertext
```

### Key Controls

- Classify data by sensitivity, apply controls accordingly
- Don't store sensitive data unnecessarily
- Encrypt all sensitive data at rest
- Use strong, standard algorithms and proper key management
- Encrypt all data in transit with TLS 1.2+
- Disable caching for responses containing sensitive data
- Use authenticated encryption, not just encryption
- Generate keys using cryptographically secure random functions

---

## A03:2021 - Injection

User-supplied data is not validated, filtered, or sanitized by the application.

### Types

- SQL Injection
- NoSQL Injection
- OS Command Injection
- LDAP Injection
- Expression Language (EL) Injection
- ORM Injection

### Prevention

```python
# BAD - SQL injection
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)

# GOOD - Parameterized query
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

# GOOD - ORM (automatically parameterized)
user = session.query(User).filter(User.email == email).first()
```

```go
// BAD - Command injection
cmd := exec.Command("sh", "-c", "ping " + userInput)

// GOOD - Pass arguments separately (no shell)
cmd := exec.Command("ping", "-c", "4", hostname)
// Validate hostname format first
if !isValidHostname(hostname) {
    return errors.New("invalid hostname")
}
```

```javascript
// BAD - NoSQL injection (MongoDB)
db.users.find({ username: req.body.username, password: req.body.password })
// Attacker sends: { "username": "admin", "password": { "$ne": "" } }

// GOOD - Validate and sanitize
const username = String(req.body.username).slice(0, 100)
const password = String(req.body.password)
if (typeof username !== 'string' || typeof password !== 'string') {
  throw new Error('Invalid input')
}
```

### Key Controls

- Use parameterized queries / prepared statements exclusively
- Use positive server-side input validation
- Escape special characters for any residual dynamic queries
- Use LIMIT and other SQL controls to prevent mass disclosure
- Separate commands from arguments (no shell execution)

---

## A04:2021 - Insecure Design

Risks related to design and architectural flaws.

### Vulnerabilities

- Missing or ineffective security controls
- Business logic flaws
- Missing rate limiting on sensitive operations
- Not requiring re-authentication for sensitive actions
- Lack of segregation between tenants

### Prevention

```python
# BAD - No rate limiting on login
@app.post("/login")
async def login(credentials: Credentials):
    user = await authenticate(credentials)
    return create_token(user)

# GOOD - Rate limit login attempts
from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)

@app.post("/login")
@limiter.limit("5/minute")  # 5 attempts per minute per IP
async def login(request: Request, credentials: Credentials):
    # Also implement per-account lockout
    if await is_account_locked(credentials.email):
        raise HTTPException(status_code=429, detail="Account temporarily locked")

    user = await authenticate(credentials)
    if not user:
        await record_failed_attempt(credentials.email)
        raise HTTPException(status_code=401)

    await clear_failed_attempts(credentials.email)
    return create_token(user)
```

```python
# BAD - No re-authentication for sensitive action
@app.post("/api/account/delete")
async def delete_account(current_user: User = Depends(get_current_user)):
    await db.delete_user(current_user.id)

# GOOD - Require password confirmation
@app.post("/api/account/delete")
async def delete_account(
    password: str,
    current_user: User = Depends(get_current_user)
):
    if not verify_password(password, current_user.password_hash):
        raise HTTPException(status_code=403, detail="Invalid password")
    await db.delete_user(current_user.id)
```

### Key Controls

- Establish secure development lifecycle with security professionals
- Use threat modeling for authentication, access control, business logic
- Write unit and integration tests for security controls
- Segregate tenants at all tiers
- Limit resource consumption by user or service

---

## A05:2021 - Security Misconfiguration

### Vulnerabilities

- Missing security hardening or improperly configured cloud permissions
- Unnecessary features enabled (ports, services, pages, accounts, privileges)
- Default accounts and passwords unchanged
- Error handling reveals stack traces
- Security settings in frameworks not set to secure values
- Missing security headers
- Software out of date

### Prevention

```python
# BAD - Debug mode in production
app = FastAPI(debug=True)  # Exposes stack traces!

# GOOD - Environment-aware configuration
app = FastAPI(
    debug=settings.DEBUG,  # False in production
    docs_url="/docs" if settings.DEBUG else None,  # Hide in production
    redoc_url=None,
)
```

```typescript
// BAD - Detailed errors to client
app.use((err, req, res, next) => {
  res.status(500).json({
    error: err.message,
    stack: err.stack, // NEVER expose in production!
  })
})

// GOOD - Generic errors in production
app.use((err, req, res, next) => {
  console.error(err) // Log full error server-side
  res.status(500).json({
    error:
      process.env.NODE_ENV === 'production'
        ? 'Internal server error'
        : err.message,
  })
})
```

```nginx
# Security headers (nginx)
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self'" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

### Key Controls

- Repeatable hardening process, automated deployment
- Minimal platform without unnecessary features
- Review and update configurations for all security notes and patches
- Segmented architecture with effective separation
- Send security directives to clients (security headers)
- Automated verification of configurations

---

## A06:2021 - Vulnerable and Outdated Components

### Vulnerabilities

- Not knowing versions of all components (client and server-side)
- Software vulnerable, unsupported, or out of date
- Not scanning for vulnerabilities regularly
- Not fixing or upgrading underlying platform in timely fashion
- Not testing compatibility of updated libraries

### Prevention

```bash
# Python - Check for vulnerabilities
pip install safety
safety check

# Or use pip-audit
pip install pip-audit
pip-audit

# Node.js - Check for vulnerabilities
npm audit
npm audit fix

# Go - Check for vulnerabilities
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck ./...

# Rust - Check for vulnerabilities
cargo install cargo-audit
cargo audit
```

```yaml
# GitHub Actions - Automated dependency scanning
name: Security Scan
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * *' # Daily

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Snyk to check for vulnerabilities
        uses: snyk/actions/python@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

      - name: Run npm audit
        run: npm audit --audit-level=high
```

### Key Controls

- Remove unused dependencies, features, components, files
- Continuously inventory component versions (client and server)
- Monitor CVE and NVD for vulnerabilities
- Use software composition analysis tools
- Only obtain components from official sources over secure links
- Monitor for unmaintained libraries

---

## A07:2021 - Identification and Authentication Failures

### Vulnerabilities

- Permits brute force or credential stuffing attacks
- Permits default, weak, or well-known passwords
- Uses weak credential recovery (knowledge-based answers)
- Uses plain text, encrypted, or weakly hashed passwords
- Missing or ineffective multi-factor authentication
- Exposes session identifier in URL
- Reuses session identifier after login
- Does not properly invalidate sessions

### Prevention

```python
# Password strength validation
import re

def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 12:
        return False, "Password must be at least 12 characters"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain lowercase letter"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain uppercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain special character"

    # Check against common passwords (use a proper list)
    common = {"password123", "qwerty123", "letmein123"}
    if password.lower() in common:
        return False, "Password is too common"

    return True, ""
```

```python
# Session regeneration on login
from fastapi import Response
import secrets

async def login(credentials: Credentials, response: Response):
    user = await authenticate(credentials)
    if not user:
        raise HTTPException(status_code=401)

    # Create new session (invalidates any existing)
    session_id = secrets.token_urlsafe(32)
    await redis.setex(f"session:{session_id}", 3600, user.id)

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=3600,
    )
    return {"message": "Login successful"}
```

### Key Controls

- Implement multi-factor authentication
- Don't ship with default credentials
- Implement weak password checks
- Align password policies with NIST 800-63b
- Harden against credential enumeration (same response for all outcomes)
- Limit failed login attempts with increasing delays
- Use server-side, secure session manager with high-entropy session IDs

---

## A08:2021 - Software and Data Integrity Failures

### Vulnerabilities

- Relying on plugins, libraries, or modules from untrusted sources
- Insecure CI/CD pipeline allowing unauthorized code
- Auto-update functionality without integrity verification
- Insecure deserialization of untrusted data

### Prevention

```python
# BAD - Deserializing untrusted data with unsafe formats
# Using serialization libraries that can instantiate arbitrary objects
# allows attackers to execute code during deserialization

# GOOD - Use safe formats (JSON) that only represent data
import json
data = json.loads(user_input)  # Safe - only data, no code execution
```

```python
# BAD - YAML with arbitrary object instantiation
import yaml
data = yaml.load(user_input)  # Can instantiate Python objects!

# GOOD - Safe YAML loading (data only)
data = yaml.safe_load(user_input)
```

```javascript
// Subresource Integrity (SRI) for CDN resources
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxPnwPYwLAvBCPAI..."
  crossorigin="anonymous"
></script>
```

```yaml
# Lock file verification in CI/CD
- name: Verify dependencies
  run: |
    # Python
    pip install --require-hashes -r requirements.txt

    # Node.js
    npm ci  # Uses package-lock.json exactly
```

### Key Controls

- Use digital signatures to verify software/data from expected source
- Ensure CI/CD pipeline has proper access control and configuration
- Do not send unsigned or unencrypted serialized data to untrusted clients
- Use integrity checks or digital signatures on serialized data
- Use SRI for external resources
- Avoid deserializing data from untrusted sources with formats that support code execution

---

## A09:2021 - Security Logging and Monitoring Failures

### Vulnerabilities

- Auditable events not logged (logins, failed logins, high-value transactions)
- Warnings and errors generate no, inadequate, or unclear log messages
- Logs not monitored for suspicious activity
- Logs only stored locally
- No alerting thresholds or escalation processes
- No logging of API calls

### Prevention

```python
import logging
import structlog
from datetime import datetime

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
)
logger = structlog.get_logger()

# Log security events
async def login(credentials: Credentials, request: Request):
    user = await authenticate(credentials)

    if not user:
        logger.warning(
            "login_failed",
            email=credentials.email,
            ip=request.client.host,
            user_agent=request.headers.get("user-agent"),
        )
        raise HTTPException(status_code=401)

    logger.info(
        "login_success",
        user_id=user.id,
        email=user.email,
        ip=request.client.host,
    )
    return create_token(user)

# Log high-value operations
async def transfer_funds(transfer: TransferRequest, user: User):
    logger.info(
        "fund_transfer",
        user_id=user.id,
        from_account=transfer.from_account,
        to_account=transfer.to_account,
        amount=str(transfer.amount),
        currency=transfer.currency,
    )
    # ... perform transfer
```

### Key Controls

- Log all login, access control, and server-side input validation failures
- Logs should have enough context to identify suspicious accounts
- Logs should be in a format easily consumed by log management solutions
- Ensure high-value transactions have audit trail with integrity controls
- Establish effective monitoring and alerting
- Establish incident response and recovery plan

---

## A10:2021 - Server-Side Request Forgery (SSRF)

### Vulnerabilities

- Fetching remote resources without validating user-supplied URLs
- Allowing access to internal services through URL manipulation
- Following redirects to internal resources

### Prevention

```python
from urllib.parse import urlparse
import ipaddress

ALLOWED_SCHEMES = {"http", "https"}
BLOCKED_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "169.254.169.254"}  # AWS metadata

def validate_url(url: str) -> bool:
    try:
        parsed = urlparse(url)

        # Check scheme
        if parsed.scheme not in ALLOWED_SCHEMES:
            return False

        # Check for blocked hosts
        hostname = parsed.hostname.lower()
        if hostname in BLOCKED_HOSTS:
            return False

        # Check for internal IPs
        try:
            ip = ipaddress.ip_address(hostname)
            if ip.is_private or ip.is_loopback or ip.is_link_local:
                return False
        except ValueError:
            pass  # Not an IP, that's fine

        # Block internal network patterns
        if hostname.endswith(".internal") or hostname.endswith(".local"):
            return False

        return True
    except Exception:
        return False

# BAD - No validation
@app.post("/fetch")
async def fetch_url(url: str):
    response = await httpx.get(url)  # Can access internal services!
    return response.text

# GOOD - Validate URL
@app.post("/fetch")
async def fetch_url(url: str):
    if not validate_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL")

    async with httpx.AsyncClient(follow_redirects=False) as client:
        response = await client.get(url, timeout=10.0)

        # If redirect, validate the new URL too
        if response.is_redirect:
            redirect_url = response.headers.get("location")
            if not validate_url(redirect_url):
                raise HTTPException(status_code=400, detail="Invalid redirect")

        return response.text
```

```go
// Go - SSRF prevention
func isAllowedURL(rawURL string) bool {
    parsed, err := url.Parse(rawURL)
    if err != nil {
        return false
    }

    // Check scheme
    if parsed.Scheme != "http" && parsed.Scheme != "https" {
        return false
    }

    // Resolve hostname to IP and check
    ips, err := net.LookupIP(parsed.Hostname())
    if err != nil {
        return false
    }

    for _, ip := range ips {
        if ip.IsLoopback() || ip.IsPrivate() || ip.IsLinkLocalUnicast() {
            return false
        }
    }

    return true
}
```

### Key Controls

- Sanitize and validate all client-supplied input data
- Enforce URL schema, port, and destination with allowlist
- Do not send raw responses to clients
- Disable HTTP redirections
- Use network segmentation to limit SSRF impact
- For frontends, deny by default and use allowlist for legitimate services
