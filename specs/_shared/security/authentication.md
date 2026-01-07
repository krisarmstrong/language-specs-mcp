# Authentication Security

Based on OWASP Authentication Cheat Sheet.

## Overview

Authentication verifies user identity. Weak authentication leads to account takeover, data breaches, and unauthorized access. This guide covers secure implementation patterns.

## Password Requirements

### Minimum Requirements (NIST 800-63B)

- **Minimum length**: 8 characters (12+ recommended)
- **Maximum length**: At least 64 characters
- **Allow all characters**: Including spaces and Unicode
- **No composition rules**: Don't force uppercase/number/symbol requirements
- **Check against breached passwords**: Use haveibeenpwned or similar

```python
# Python - Password validation
import re
from typing import Tuple
import httpx  # For API calls

MIN_PASSWORD_LENGTH = 12
MAX_PASSWORD_LENGTH = 128

async def validate_password(password: str) -> Tuple[bool, str]:
    """Validate password against security requirements."""

    # Length checks
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters"

    if len(password) > MAX_PASSWORD_LENGTH:
        return False, f"Password must be at most {MAX_PASSWORD_LENGTH} characters"

    # Check against breached passwords (haveibeenpwned)
    if await is_password_breached(password):
        return False, "This password has been exposed in a data breach"

    # Check for common patterns
    if is_common_pattern(password):
        return False, "Password is too common or predictable"

    return True, "Password is valid"

def is_common_pattern(password: str) -> bool:
    """Check for common weak patterns."""
    lower = password.lower()

    # Sequential characters
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
        return True
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij)', lower):
        return True

    # Repeated characters
    if re.search(r'(.)\1{3,}', password):
        return True

    # Common words (extend this list)
    common_words = ['password', 'qwerty', 'letmein', 'welcome', 'admin']
    if any(word in lower for word in common_words):
        return True

    return False
```

```typescript
// TypeScript - Password validation with zxcvbn
import zxcvbn from 'zxcvbn'

interface ValidationResult {
  valid: boolean
  message: string
  score?: number
}

const MIN_PASSWORD_LENGTH = 12
const MAX_PASSWORD_LENGTH = 128
const MIN_STRENGTH_SCORE = 3 // zxcvbn scores 0-4

export function validatePassword(password: string): ValidationResult {
  if (password.length < MIN_PASSWORD_LENGTH) {
    return {
      valid: false,
      message: `Password must be at least ${MIN_PASSWORD_LENGTH} characters`,
    }
  }

  if (password.length > MAX_PASSWORD_LENGTH) {
    return {
      valid: false,
      message: `Password must be at most ${MAX_PASSWORD_LENGTH} characters`,
    }
  }

  // Use zxcvbn for strength estimation
  const result = zxcvbn(password)

  if (result.score < MIN_STRENGTH_SCORE) {
    return {
      valid: false,
      message: result.feedback.warning || 'Password is too weak',
      score: result.score,
    }
  }

  return { valid: true, message: 'Password is valid', score: result.score }
}
```

### Breached Password Check

```python
# Python - Check haveibeenpwned API (k-anonymity model)
import hashlib
import httpx

async def is_password_breached(password: str) -> bool:
    """Check if password appears in known breaches using k-anonymity."""
    # Hash the password with SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Query API with only the prefix (k-anonymity)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            headers={"Add-Padding": "true"}  # Prevent timing attacks
        )

    # Check if our suffix appears in the response
    hashes = response.text.splitlines()
    for line in hashes:
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            return True  # Password found in breach

    return False
```

```typescript
// TypeScript - Breached password check
import crypto from 'crypto'

export async function isPasswordBreached(password: string): Promise<boolean> {
  const sha1Hash = crypto
    .createHash('sha1')
    .update(password)
    .digest('hex')
    .toUpperCase()

  const prefix = sha1Hash.slice(0, 5)
  const suffix = sha1Hash.slice(5)

  const response = await fetch(
    `https://api.pwnedpasswords.com/range/${prefix}`,
    { headers: { 'Add-Padding': 'true' } }
  )

  const hashes = await response.text()
  return hashes.split('\n').some((line) => line.startsWith(suffix))
}
```

## Multi-Factor Authentication (MFA)

### TOTP Implementation

```python
# Python - TOTP with pyotp
import pyotp
import qrcode
import io
import base64

def generate_totp_secret() -> str:
    """Generate a new TOTP secret for a user."""
    return pyotp.random_base32()

def get_totp_provisioning_uri(secret: str, user_email: str, issuer: str) -> str:
    """Generate provisioning URI for authenticator apps."""
    totp = pyotp.TOTP(secret)
    return totp.provisioning_uri(name=user_email, issuer_name=issuer)

def generate_qr_code(provisioning_uri: str) -> str:
    """Generate QR code as base64 image."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(provisioning_uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    return base64.b64encode(buffer.getvalue()).decode()

def verify_totp(secret: str, code: str) -> bool:
    """Verify a TOTP code with timing tolerance."""
    totp = pyotp.TOTP(secret)
    # valid_window=1 allows codes from 30 seconds before/after
    return totp.verify(code, valid_window=1)
```

```typescript
// TypeScript - TOTP with otplib
import { authenticator } from 'otplib'

export function generateTotpSecret(): string {
  return authenticator.generateSecret()
}

export function getTotpUri(
  secret: string,
  userEmail: string,
  issuer: string
): string {
  return authenticator.keyuri(userEmail, issuer, secret)
}

export function verifyTotp(secret: string, token: string): boolean {
  // Set window to allow for clock drift
  authenticator.options = { window: 1 }
  return authenticator.verify({ token, secret })
}
```

### Backup Codes

```python
# Python - Generate backup codes
import secrets

def generate_backup_codes(count: int = 10) -> list[str]:
    """Generate one-time backup codes."""
    codes = []
    for _ in range(count):
        # 8-character alphanumeric codes
        code = secrets.token_hex(4).upper()
        # Format as XXXX-XXXX for readability
        formatted = f"{code[:4]}-{code[4:]}"
        codes.append(formatted)
    return codes

def hash_backup_codes(codes: list[str]) -> list[str]:
    """Hash backup codes for storage."""
    import hashlib
    return [
        hashlib.sha256(code.encode()).hexdigest()
        for code in codes
    ]

def verify_backup_code(provided_code: str, stored_hashes: list[str]) -> int | None:
    """Verify backup code and return index if valid."""
    import hashlib
    provided_hash = hashlib.sha256(provided_code.encode()).hexdigest()

    for i, stored_hash in enumerate(stored_hashes):
        if secrets.compare_digest(provided_hash, stored_hash):
            return i  # Return index to mark as used
    return None
```

## Account Lockout

### Progressive Delays

```python
# Python - Account lockout with progressive delays
import time
from datetime import datetime, timedelta
from dataclasses import dataclass
import redis

redis_client = redis.Redis()

@dataclass
class LoginAttempt:
    attempts: int
    locked_until: datetime | None
    last_attempt: datetime

LOCKOUT_THRESHOLDS = [
    (3, 30),      # After 3 failures: 30 second delay
    (5, 300),     # After 5 failures: 5 minute delay
    (10, 3600),   # After 10 failures: 1 hour delay
    (15, 86400),  # After 15 failures: 24 hour delay
]

def get_lockout_duration(attempts: int) -> int:
    """Get lockout duration in seconds based on attempt count."""
    for threshold, duration in reversed(LOCKOUT_THRESHOLDS):
        if attempts >= threshold:
            return duration
    return 0

async def check_login_allowed(user_id: str) -> tuple[bool, int]:
    """Check if login attempt is allowed. Returns (allowed, wait_seconds)."""
    key = f"login_attempts:{user_id}"
    data = redis_client.hgetall(key)

    if not data:
        return True, 0

    attempts = int(data.get(b'attempts', 0))
    locked_until = data.get(b'locked_until')

    if locked_until:
        locked_time = datetime.fromisoformat(locked_until.decode())
        if datetime.utcnow() < locked_time:
            wait_seconds = int((locked_time - datetime.utcnow()).total_seconds())
            return False, wait_seconds

    return True, 0

async def record_failed_attempt(user_id: str) -> int:
    """Record failed login attempt. Returns lockout duration."""
    key = f"login_attempts:{user_id}"

    # Increment attempts
    attempts = redis_client.hincrby(key, 'attempts', 1)

    # Calculate lockout
    lockout_duration = get_lockout_duration(attempts)

    if lockout_duration > 0:
        locked_until = datetime.utcnow() + timedelta(seconds=lockout_duration)
        redis_client.hset(key, 'locked_until', locked_until.isoformat())

    # Set expiry on key (auto-cleanup after 24 hours of inactivity)
    redis_client.expire(key, 86400)

    return lockout_duration

async def clear_failed_attempts(user_id: str) -> None:
    """Clear failed attempts after successful login."""
    redis_client.delete(f"login_attempts:{user_id}")
```

```typescript
// TypeScript - Rate limiting with sliding window
import { Redis } from 'ioredis'

const redis = new Redis()

interface RateLimitResult {
  allowed: boolean
  remaining: number
  resetAfter: number
}

export async function checkRateLimit(
  key: string,
  limit: number,
  windowSeconds: number
): Promise<RateLimitResult> {
  const now = Date.now()
  const windowStart = now - windowSeconds * 1000

  // Use sorted set for sliding window
  const multi = redis.multi()
  multi.zremrangebyscore(key, 0, windowStart) // Remove old entries
  multi.zadd(key, now, `${now}`) // Add current request
  multi.zcard(key) // Count requests in window
  multi.expire(key, windowSeconds) // Set expiry

  const results = await multi.exec()
  const requestCount = results?.[2]?.[1] as number

  return {
    allowed: requestCount <= limit,
    remaining: Math.max(0, limit - requestCount),
    resetAfter: windowSeconds,
  }
}
```

## Password Reset

### Secure Reset Flow

```python
# Python - Secure password reset
import secrets
from datetime import datetime, timedelta
import hashlib

RESET_TOKEN_EXPIRY = timedelta(hours=1)

async def create_password_reset_token(user_id: str) -> str:
    """Create a secure password reset token."""
    # Generate cryptographically secure token
    token = secrets.token_urlsafe(32)

    # Hash token for storage (don't store plaintext)
    token_hash = hashlib.sha256(token.encode()).hexdigest()

    # Store hash with expiry
    expiry = datetime.utcnow() + RESET_TOKEN_EXPIRY
    await db.run_query(
        """
        INSERT INTO password_reset_tokens (user_id, token_hash, expires_at)
        VALUES ($1, $2, $3)
        ON CONFLICT (user_id) DO UPDATE SET
            token_hash = $2,
            expires_at = $3,
            used = false
        """,
        user_id, token_hash, expiry
    )

    return token  # Return plaintext token to send via email

async def verify_reset_token(token: str) -> str | None:
    """Verify reset token and return user_id if valid."""
    token_hash = hashlib.sha256(token.encode()).hexdigest()

    result = await db.fetch_row(
        """
        SELECT user_id FROM password_reset_tokens
        WHERE token_hash = $1
          AND expires_at > NOW()
          AND used = false
        """,
        token_hash
    )

    return result['user_id'] if result else None

async def invalidate_reset_token(token: str) -> None:
    """Mark token as used after password reset."""
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    await db.run_query(
        "UPDATE password_reset_tokens SET used = true WHERE token_hash = $1",
        token_hash
    )
```

### Reset Email Best Practices

```python
# Python - Password reset email
async def send_password_reset_email(email: str) -> None:
    """Send password reset email with constant-time response."""
    user = await get_user_by_email(email)

    if user:
        token = await create_password_reset_token(user.id)
        reset_url = f"https://example.com/reset-password?token={token}"

        await send_email(
            to=email,
            subject="Password Reset Request",
            body=f"""
            You requested a password reset. Click the link below to reset your password:

            {reset_url}

            This link expires in 1 hour.

            If you didn't request this, you can safely ignore this email.
            """
        )

    # IMPORTANT: Same response time regardless of user existence
    # This prevents user enumeration attacks
    # Add artificial delay if user doesn't exist to match timing
```

## Remember Me Functionality

```python
# Python - Secure "Remember Me" implementation
import secrets
import hashlib
from datetime import datetime, timedelta

REMEMBER_TOKEN_EXPIRY = timedelta(days=30)

async def create_remember_token(user_id: str, device_info: dict) -> str:
    """Create a long-lived remember-me token."""
    # Generate secure token
    token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(token.encode()).hexdigest()

    expiry = datetime.utcnow() + REMEMBER_TOKEN_EXPIRY

    # Store with device info for security review
    await db.run_query(
        """
        INSERT INTO remember_tokens
        (user_id, token_hash, expires_at, device_info, created_at)
        VALUES ($1, $2, $3, $4, NOW())
        """,
        user_id, token_hash, expiry, device_info
    )

    return token

async def verify_remember_token(token: str) -> str | None:
    """Verify remember-me token and return user_id."""
    token_hash = hashlib.sha256(token.encode()).hexdigest()

    result = await db.fetch_row(
        """
        SELECT user_id, id FROM remember_tokens
        WHERE token_hash = $1 AND expires_at > NOW()
        """,
        token_hash
    )

    if result:
        # Rotate token on use (prevent token reuse attacks)
        await db.run_query(
            "DELETE FROM remember_tokens WHERE id = $1",
            result['id']
        )
        return result['user_id']

    return None
```

## Login Implementation

```python
# Python/FastAPI - Complete login endpoint
from fastapi import FastAPI, HTTPException, Response, Request
from pydantic import BaseModel, EmailStr
import secrets

app = FastAPI()

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    remember_me: bool = False
    totp_code: str | None = None

@app.post("/auth/login")
async def login(
    request: Request,
    response: Response,
    credentials: LoginRequest
):
    # Check rate limiting
    allowed, wait_time = await check_login_allowed(credentials.email)
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail=f"Too many attempts. Try again in {wait_time} seconds."
        )

    # Verify credentials
    user = await get_user_by_email(credentials.email)

    # Constant-time comparison even if user doesn't exist
    if not user:
        # Perform dummy hash to prevent timing attacks
        verify_password("dummy", get_dummy_hash())
        await record_failed_attempt(credentials.email)
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(credentials.password, user.password_hash):
        await record_failed_attempt(credentials.email)
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Check MFA if enabled
    if user.mfa_enabled:
        if not credentials.totp_code:
            raise HTTPException(
                status_code=401,
                detail="MFA code required",
                headers={"X-MFA-Required": "true"}
            )

        if not verify_totp(user.totp_secret, credentials.totp_code):
            await record_failed_attempt(credentials.email)
            raise HTTPException(status_code=401, detail="Invalid MFA code")

    # Clear failed attempts
    await clear_failed_attempts(credentials.email)

    # Create session
    session_id = await create_session(
        user.id,
        {"ip": request.client.host, "user_agent": request.headers.get("user-agent")}
    )

    # Set session cookie
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=86400  # 24 hours
    )

    # Handle remember me
    if credentials.remember_me:
        remember_token = await create_remember_token(
            user.id,
            {"ip": request.client.host, "user_agent": request.headers.get("user-agent")}
        )
        response.set_cookie(
            key="remember_token",
            value=remember_token,
            httponly=True,
            secure=True,
            samesite="strict",
            max_age=30 * 24 * 3600  # 30 days
        )

    return {
        "message": "Login successful",
        "user": {"id": user.id, "email": user.email}
    }
```

## Security Checklist

### Password Security
- [ ] Minimum 12 character passwords
- [ ] Maximum length at least 64 characters
- [ ] All characters allowed (including spaces, Unicode)
- [ ] No arbitrary composition rules
- [ ] Check against breached password databases
- [ ] Use Argon2id or bcrypt for hashing

### Authentication Flow
- [ ] Constant-time credential comparison
- [ ] Generic error messages (prevent enumeration)
- [ ] Account lockout with progressive delays
- [ ] Rate limiting on login endpoints
- [ ] Session regeneration after login
- [ ] Secure session cookie attributes

### Multi-Factor Authentication
- [ ] Support TOTP-based MFA
- [ ] Provide backup codes
- [ ] Allow users to view/revoke MFA devices
- [ ] Re-authenticate before MFA changes

### Password Reset
- [ ] Cryptographically secure reset tokens
- [ ] Short token expiry (1 hour max)
- [ ] Single-use tokens
- [ ] Constant-time response (prevent enumeration)
- [ ] Invalidate token after use

### Remember Me
- [ ] Separate long-lived token (not session extension)
- [ ] Token rotation on use
- [ ] Store device info for security review
- [ ] Allow users to revoke remember-me tokens
