# OWASP Security Checklist for Code Generation

**Review this checklist before generating code that handles user input, authentication, or sensitive data.**

## OWASP Top 10 (2021) Quick Reference

| # | Risk | One-Line Fix |
|---|------|--------------|
| A01 | Broken Access Control | Check permissions on EVERY endpoint |
| A02 | Cryptographic Failures | Use TLS, hash passwords with bcrypt/argon2 |
| A03 | Injection | Parameterized queries, never string concat |
| A04 | Insecure Design | Threat model before coding |
| A05 | Security Misconfiguration | Disable debug mode, remove defaults |
| A06 | Vulnerable Components | Update dependencies, audit regularly |
| A07 | Auth Failures | MFA, rate limiting, secure session management |
| A08 | Data Integrity Failures | Verify signatures, use trusted CI/CD |
| A09 | Logging Failures | Log security events, don't log secrets |
| A10 | SSRF | Validate/allowlist URLs, block internal IPs |

---

## A01: Broken Access Control

### Must Do
```python
# ALWAYS check authorization, not just authentication
@app.get("/users/{user_id}/data")
async def get_user_data(user_id: int, current_user: User = Depends(get_current_user)):
    # BAD: Only checks if logged in
    return await fetch_user_data(user_id)

    # GOOD: Checks if user can access this specific resource
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(403, "Access denied")
    return await fetch_user_data(user_id)
```

### Checklist
- [ ] Every endpoint checks authorization, not just authentication
- [ ] Default deny: reject unless explicitly allowed
- [ ] Rate limit sensitive endpoints
- [ ] Log access control failures
- [ ] Use indirect object references (UUIDs not sequential IDs)

---

## A02: Cryptographic Failures

### Password Storage
```python
# NEVER
password_hash = hashlib.md5(password.encode()).hexdigest()  # Crackable
password_hash = hashlib.sha256(password.encode()).hexdigest()  # No salt

# ALWAYS
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")
password_hash = pwd_context.hash(password)
```

### Secrets
```python
# NEVER
SECRET_KEY = "my-secret-key"  # Hardcoded
token = ''.join(random.choices('abc123', k=32))  # Predictable

# ALWAYS
SECRET_KEY = os.environ["SECRET_KEY"]  # From environment
token = secrets.token_urlsafe(32)  # Cryptographic
```

### Checklist
- [ ] Passwords hashed with argon2id, bcrypt, or scrypt (NOT MD5/SHA)
- [ ] Secrets from environment variables, not code
- [ ] TLS for all network communication
- [ ] Sensitive data encrypted at rest
- [ ] No sensitive data in URLs or logs

---

## A03: Injection

### SQL Injection
```python
# VULNERABLE
query = f"SELECT * FROM users WHERE email = '{email}'"

# SECURE
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
# OR with ORM
User.query.filter_by(email=email).first()
```

### Command Injection
```python
# VULNERABLE - uses shell with user input
subprocess.run(f"grep {pattern} {file}", shell=True)

# SECURE - array form, no shell
subprocess.run(["grep", pattern, file], check=True, shell=False)
```

### Path Traversal
```python
# VULNERABLE
def download(filename):
    return send_file(f"uploads/{filename}")  # ../../../etc/passwd

# SECURE
from pathlib import Path
UPLOAD_DIR = Path("uploads").resolve()

def download(filename):
    path = (UPLOAD_DIR / filename).resolve()
    if not path.is_relative_to(UPLOAD_DIR):
        abort(400)
    return send_file(path)
```

### Checklist
- [ ] All SQL uses parameterized queries or ORM
- [ ] Shell commands use array form, never shell=True with user input
- [ ] File paths validated against directory traversal
- [ ] XML parsing disables external entities (XXE)
- [ ] Template engines auto-escape by default

---

## A04: Insecure Design

### Checklist
- [ ] Threat model exists for sensitive features
- [ ] Business logic has server-side validation (don't trust client)
- [ ] Rate limiting on resource-intensive operations
- [ ] Segregation between tenants in multi-tenant systems
- [ ] Fail securely (deny by default on errors)

---

## A05: Security Misconfiguration

### Production Settings
```python
# Django
DEBUG = False
ALLOWED_HOSTS = ["myapp.com"]
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Flask
app.config["DEBUG"] = False
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
```

### Checklist
- [ ] Debug mode disabled in production
- [ ] Default credentials changed
- [ ] Unnecessary features/endpoints removed
- [ ] Security headers set (CSP, X-Frame-Options, etc.)
- [ ] Error messages don't leak stack traces

---

## A06: Vulnerable Components

### Checklist
- [ ] Dependencies audited: `npm audit`, `pip-audit`, `cargo audit`
- [ ] Automated dependency updates (Dependabot, Renovate)
- [ ] Only use maintained libraries
- [ ] Remove unused dependencies
- [ ] Subscribe to security advisories

---

## A07: Authentication Failures

### Secure Authentication
```python
# Password requirements
MIN_PASSWORD_LENGTH = 12
# Check against breached passwords (HaveIBeenPwned API)

# Rate limiting
from slowapi import Limiter
@limiter.limit("5/minute")
@app.post("/login")
async def login(credentials: LoginRequest):
    ...

# Session management
SESSION_LIFETIME = timedelta(hours=1)
REFRESH_TOKEN_LIFETIME = timedelta(days=7)
```

### Checklist
- [ ] Strong password policy (12+ chars, check breached passwords)
- [ ] Rate limiting on login (5 attempts/minute)
- [ ] MFA available for sensitive accounts
- [ ] Session tokens are random, long, and expire
- [ ] Logout invalidates session server-side
- [ ] Password reset tokens single-use and time-limited

---

## A08: Software and Data Integrity

### Checklist
- [ ] Dependencies from trusted sources only
- [ ] CI/CD pipeline secured
- [ ] Code reviews required for merges
- [ ] Signed commits/releases for critical systems
- [ ] Integrity checks on downloaded files

---

## A09: Security Logging and Monitoring

### What to Log
```python
# GOOD - Security events
logger.info(f"Login successful: user={user.id}")
logger.warning(f"Login failed: email={email}, ip={request.remote_addr}")
logger.warning(f"Access denied: user={user.id}, resource={resource_id}")
logger.error(f"Rate limit exceeded: ip={request.remote_addr}")

# BAD - Sensitive data
logger.info(f"Login: email={email}, password={password}")  # NEVER
logger.info(f"Payment: card={card_number}")  # NEVER
```

### Checklist
- [ ] Log authentication success/failure
- [ ] Log authorization failures
- [ ] Log input validation failures
- [ ] NEVER log passwords, tokens, or PII
- [ ] Alerts on suspicious patterns

---

## A10: Server-Side Request Forgery (SSRF)

### Secure URL Fetching
```python
# VULNERABLE
@app.post("/fetch")
async def fetch_url(url: str):
    response = requests.get(url)  # Can access internal network!
    return response.text

# SECURE
from urllib.parse import urlparse
import ipaddress

ALLOWED_HOSTS = {"api.example.com", "cdn.example.com"}

def is_safe_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    if parsed.hostname not in ALLOWED_HOSTS:
        return False
    # Block internal IPs
    try:
        ip = ipaddress.ip_address(parsed.hostname)
        if ip.is_private or ip.is_loopback:
            return False
    except ValueError:
        pass  # Hostname, not IP
    return True

@app.post("/fetch")
async def fetch_url(url: str):
    if not is_safe_url(url):
        raise HTTPException(400, "URL not allowed")
    response = requests.get(url, timeout=10)
    return response.text
```

### Checklist
- [ ] Allowlist of permitted domains for outbound requests
- [ ] Block requests to private IP ranges (10.x, 192.168.x, 127.x)
- [ ] Block requests to cloud metadata endpoints (169.254.169.254)
- [ ] Validate URL scheme (http/https only)
- [ ] Set timeouts on all outbound requests
