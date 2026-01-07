# Session Management Security

Based on OWASP Session Management Cheat Sheet.

## Overview

Secure session management is critical for maintaining authenticated state. Sessions must protect against hijacking, fixation, and replay attacks.

## Session ID Generation

### Requirements

- **High entropy**: At least 128 bits of randomness
- **Unpredictable**: Use cryptographically secure random generator
- **Unique**: No collisions in practical use

```python
# Python - Secure session ID generation
import secrets

def generate_session_id() -> str:
    # 256 bits of entropy, URL-safe
    return secrets.token_urlsafe(32)
```

```typescript
// TypeScript
import crypto from 'crypto'

function generateSessionId(): string {
  return crypto.randomBytes(32).toString('base64url')
}
```

```go
// Go
import (
    "crypto/rand"
    "encoding/base64"
)

func GenerateSessionID() (string, error) {
    b := make([]byte, 32)
    if _, err := rand.Read(b); err != nil {
        return "", err
    }
    return base64.URLEncoding.EncodeToString(b), nil
}
```

## Session Storage

### Server-Side Sessions (Recommended)

```python
# Python/FastAPI with Redis
import redis
import json
from datetime import timedelta

redis_client = redis.Redis(host='localhost', port=6379, db=0)
SESSION_TTL = timedelta(hours=24)

async def create_session(user_id: str, data: dict) -> str:
    session_id = secrets.token_urlsafe(32)
    session_data = {
        "user_id": user_id,
        "created_at": datetime.utcnow().isoformat(),
        **data
    }
    redis_client.setex(
        f"session:{session_id}",
        SESSION_TTL,
        json.dumps(session_data)
    )
    return session_id

async def get_session(session_id: str) -> dict | None:
    data = redis_client.get(f"session:{session_id}")
    if data:
        # Refresh TTL on access (sliding expiration)
        redis_client.expire(f"session:{session_id}", SESSION_TTL)
        return json.loads(data)
    return None

async def destroy_session(session_id: str) -> None:
    redis_client.delete(f"session:{session_id}")
```

```typescript
// Express.js with Redis
import session from 'express-session'
import RedisStore from 'connect-redis'
import { createClient } from 'redis'

const redisClient = createClient({ url: process.env.REDIS_URL })
await redisClient.connect()

app.use(
  session({
    store: new RedisStore({ client: redisClient }),
    secret: process.env.SESSION_SECRET!,
    name: 'sessionId', // Custom cookie name (not 'connect.sid')
    resave: false,
    saveUninitialized: false,
    rolling: true, // Refresh expiration on each request
    cookie: {
      secure: process.env.NODE_ENV === 'production',
      httpOnly: true,
      sameSite: 'strict',
      maxAge: 24 * 60 * 60 * 1000, // 24 hours
    },
  })
)
```

### JWT Sessions (Stateless)

```python
# Python - JWT with short expiration
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.environ["JWT_SECRET"]
ACCESS_TOKEN_EXPIRE = timedelta(minutes=15)
REFRESH_TOKEN_EXPIRE = timedelta(days=7)

def create_access_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + ACCESS_TOKEN_EXPIRE
    payload = {
        "sub": user_id,
        "type": "access",
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def create_refresh_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + REFRESH_TOKEN_EXPIRE
    token_id = secrets.token_urlsafe(16)  # For revocation tracking
    payload = {
        "sub": user_id,
        "type": "refresh",
        "jti": token_id,
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }
    # Store token_id in database for revocation
    store_refresh_token(user_id, token_id, expire)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token: str, token_type: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if payload.get("type") != token_type:
            raise ValueError("Invalid token type")
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
```

## Session Fixation Prevention

Regenerate session ID after authentication state changes.

```python
# Python - Session regeneration on login
async def login(credentials: Credentials, request: Request, response: Response):
    user = await authenticate(credentials)
    if not user:
        raise HTTPException(status_code=401)

    # Destroy old session if exists
    old_session_id = request.cookies.get("session_id")
    if old_session_id:
        await destroy_session(old_session_id)

    # Create new session with new ID
    new_session_id = await create_session(user.id, {"authenticated": True})

    response.set_cookie(
        key="session_id",
        value=new_session_id,
        httponly=True,
        secure=True,
        samesite="strict",
    )
    return {"message": "Login successful"}
```

```typescript
// Express.js - Regenerate session
app.post('/login', async (req, res) => {
  const user = await authenticate(req.body)
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' })
  }

  // Regenerate session ID to prevent fixation
  req.session.regenerate((err) => {
    if (err) {
      return res.status(500).json({ error: 'Session error' })
    }

    // Store user info in new session
    req.session.userId = user.id
    req.session.authenticated = true

    res.json({ message: 'Login successful' })
  })
})
```

## Session Timeout

### Absolute Timeout

Session expires after fixed time regardless of activity.

```python
# Python - Absolute timeout check
async def get_session(session_id: str) -> dict | None:
    data = redis_client.get(f"session:{session_id}")
    if not data:
        return None

    session = json.loads(data)
    created_at = datetime.fromisoformat(session["created_at"])

    # Absolute timeout: 8 hours from creation
    if datetime.utcnow() - created_at > timedelta(hours=8):
        await destroy_session(session_id)
        return None

    return session
```

### Idle Timeout

Session expires after period of inactivity.

```python
# Python - Idle timeout with last activity tracking
async def get_session_with_activity_check(session_id: str) -> dict | None:
    data = redis_client.get(f"session:{session_id}")
    if not data:
        return None

    session = json.loads(data)
    last_activity = datetime.fromisoformat(session.get("last_activity", session["created_at"]))

    # Idle timeout: 30 minutes
    if datetime.utcnow() - last_activity > timedelta(minutes=30):
        await destroy_session(session_id)
        return None

    # Update last activity
    session["last_activity"] = datetime.utcnow().isoformat()
    redis_client.setex(f"session:{session_id}", SESSION_TTL, json.dumps(session))

    return session
```

## Secure Cookie Configuration

```python
# Python/FastAPI
response.set_cookie(
    key="session_id",
    value=session_id,
    httponly=True,       # Not accessible via JavaScript
    secure=True,         # HTTPS only
    samesite="strict",   # CSRF protection (or "lax" if needed)
    max_age=86400,       # 24 hours in seconds
    path="/",            # Cookie scope
    domain=".example.com",  # Include subdomains if needed
)
```

```typescript
// Express.js
res.cookie('sessionId', sessionId, {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'strict',
  maxAge: 24 * 60 * 60 * 1000,
  path: '/',
  domain: '.example.com',
})
```

### Cookie Attribute Reference

| Attribute | Purpose | Recommendation |
|-----------|---------|----------------|
| HttpOnly | Prevent JavaScript access | Always set |
| Secure | HTTPS only | Always set in production |
| SameSite | CSRF protection | `Strict` or `Lax` |
| Path | Cookie scope | `/` for whole site |
| Domain | Domain scope | Set explicitly |
| Max-Age | Expiration | Match session timeout |

## Logout Implementation

```python
# Python - Proper logout
async def logout(session_id: str, response: Response):
    # 1. Destroy server-side session
    await destroy_session(session_id)

    # 2. Clear session cookie
    response.delete_cookie(
        key="session_id",
        path="/",
        domain=".example.com",
        secure=True,
        httponly=True,
        samesite="strict",
    )

    # 3. If using JWT refresh tokens, revoke them
    await revoke_all_refresh_tokens(user_id)

    return {"message": "Logged out"}
```

```typescript
// Express.js
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      console.error('Logout error:', err)
    }

    // Clear cookie even if session destroy fails
    res.clearCookie('sessionId', {
      path: '/',
      domain: '.example.com',
      secure: true,
      httpOnly: true,
      sameSite: 'strict',
    })

    res.json({ message: 'Logged out' })
  })
})
```

## Multi-Device Session Management

```python
# Track all sessions for a user
async def create_session(user_id: str, device_info: dict) -> str:
    session_id = secrets.token_urlsafe(32)
    session_data = {
        "user_id": user_id,
        "device": device_info.get("user_agent", "unknown"),
        "ip": device_info.get("ip"),
        "created_at": datetime.utcnow().isoformat(),
    }

    # Store session
    redis_client.setex(f"session:{session_id}", SESSION_TTL, json.dumps(session_data))

    # Track session in user's session list
    redis_client.sadd(f"user_sessions:{user_id}", session_id)

    return session_id

async def get_user_sessions(user_id: str) -> list[dict]:
    """Get all active sessions for a user"""
    session_ids = redis_client.smembers(f"user_sessions:{user_id}")
    sessions = []
    for sid in session_ids:
        data = redis_client.get(f"session:{sid.decode()}")
        if data:
            session = json.loads(data)
            session["session_id"] = sid.decode()[:8] + "..."  # Partial ID for display
            sessions.append(session)
    return sessions

async def logout_all_devices(user_id: str):
    """Logout from all devices"""
    session_ids = redis_client.smembers(f"user_sessions:{user_id}")
    for sid in session_ids:
        redis_client.delete(f"session:{sid.decode()}")
    redis_client.delete(f"user_sessions:{user_id}")
```

## Concurrent Session Control

```python
# Limit concurrent sessions per user
MAX_SESSIONS_PER_USER = 5

async def create_session_with_limit(user_id: str, device_info: dict) -> str:
    current_sessions = redis_client.scard(f"user_sessions:{user_id}")

    if current_sessions >= MAX_SESSIONS_PER_USER:
        # Remove oldest session
        oldest = await get_oldest_session(user_id)
        if oldest:
            await destroy_session(oldest)

    return await create_session(user_id, device_info)
```

## Security Checklist

- [ ] Session IDs are generated with cryptographically secure randomness
- [ ] Session IDs have sufficient entropy (128+ bits)
- [ ] Sessions are stored server-side (not in JWT for sensitive apps)
- [ ] Session ID is regenerated after login
- [ ] Cookies have HttpOnly, Secure, and SameSite attributes
- [ ] Absolute and idle timeouts are implemented
- [ ] Logout properly destroys session and clears cookies
- [ ] Users can view and revoke their sessions
- [ ] Session fixation is prevented
- [ ] Concurrent session limits are enforced if needed
