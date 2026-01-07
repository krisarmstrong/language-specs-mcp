# Cross-Language Authentication Patterns

Secure authentication and authorization patterns across languages.

## Password Hashing

### Python (bcrypt / argon2)

```python
# bcrypt - widely used
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# argon2 - recommended for new projects (memory-hard)
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(
    time_cost=3,       # Iterations
    memory_cost=65536, # 64MB
    parallelism=4,     # Threads
)

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    try:
        ph.verify(hashed, password)
        return True
    except VerifyMismatchError:
        return False
```

### TypeScript (bcrypt)

```typescript
import bcrypt from 'bcrypt'

const SALT_ROUNDS = 12

async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS)
}

async function verifyPassword(
  password: string,
  hash: string
): Promise<boolean> {
  return bcrypt.compare(password, hash)
}
```

### Go (bcrypt)

```go
import "golang.org/x/crypto/bcrypt"

const bcryptCost = 12

func HashPassword(password string) (string, error) {
    bytes, err := bcrypt.GenerateFromPassword([]byte(password), bcryptCost)
    return string(bytes), err
}

func VerifyPassword(password, hash string) bool {
    err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
    return err == nil
}
```

### Rust (argon2)

```rust
use argon2::{
    password_hash::{rand_core::OsRng, PasswordHash, PasswordHasher, PasswordVerifier, SaltString},
    Argon2,
};

fn hash_password(password: &str) -> Result<String, argon2::password_hash::Error> {
    let salt = SaltString::generate(&mut OsRng);
    let argon2 = Argon2::default();
    let hash = argon2.hash_password(password.as_bytes(), &salt)?;
    Ok(hash.to_string())
}

fn verify_password(password: &str, hash: &str) -> Result<bool, argon2::password_hash::Error> {
    let parsed_hash = PasswordHash::new(hash)?;
    Ok(Argon2::default()
        .verify_password(password.as_bytes(), &parsed_hash)
        .is_ok())
}
```

### Java (BCrypt via Spring Security)

```java
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class PasswordService {
    private final BCryptPasswordEncoder encoder = new BCryptPasswordEncoder(12);

    public String hashPassword(String password) {
        return encoder.encode(password);
    }

    public boolean verifyPassword(String password, String hash) {
        return encoder.matches(password, hash);
    }
}
```

## JWT Token Management

### Python (PyJWT)

```python
import jwt
from datetime import datetime, timedelta, timezone
from typing import Any

SECRET_KEY = "your-secret-key"  # Load from environment
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "iat": datetime.now(timezone.utc)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise InvalidTokenError("Token has expired")
    except jwt.InvalidTokenError:
        raise InvalidTokenError("Invalid token")
```

### TypeScript (jsonwebtoken)

```typescript
import jwt from 'jsonwebtoken'

const SECRET_KEY = process.env.JWT_SECRET!
const ACCESS_TOKEN_EXPIRES = '30m'
const REFRESH_TOKEN_EXPIRES = '7d'

interface TokenPayload {
  sub: string
  email: string
  role: string
}

function createAccessToken(payload: TokenPayload): string {
  return jwt.sign(payload, SECRET_KEY, {
    expiresIn: ACCESS_TOKEN_EXPIRES,
    algorithm: 'HS256',
  })
}

function createRefreshToken(userId: string): string {
  return jwt.sign({ sub: userId, type: 'refresh' }, SECRET_KEY, {
    expiresIn: REFRESH_TOKEN_EXPIRES,
    algorithm: 'HS256',
  })
}

function verifyToken(token: string): TokenPayload {
  try {
    return jwt.verify(token, SECRET_KEY) as TokenPayload
  } catch (error) {
    if (error instanceof jwt.TokenExpiredError) {
      throw new AuthError('Token expired')
    }
    throw new AuthError('Invalid token')
  }
}
```

### Go (golang-jwt)

```go
import (
    "time"
    "github.com/golang-jwt/jwt/v5"
)

var secretKey = []byte(os.Getenv("JWT_SECRET"))

type Claims struct {
    UserID string `json:"sub"`
    Email  string `json:"email"`
    Role   string `json:"role"`
    jwt.RegisteredClaims
}

func CreateAccessToken(userID, email, role string) (string, error) {
    claims := Claims{
        UserID: userID,
        Email:  email,
        Role:   role,
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(time.Now().Add(30 * time.Minute)),
            IssuedAt:  jwt.NewNumericDate(time.Now()),
        },
    }

    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(secretKey)
}

func VerifyToken(tokenString string) (*Claims, error) {
    token, err := jwt.ParseWithClaims(tokenString, &Claims{}, func(token *jwt.Token) (interface{}, error) {
        if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
            return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
        }
        return secretKey, nil
    })

    if err != nil {
        return nil, err
    }

    if claims, ok := token.Claims.(*Claims); ok && token.Valid {
        return claims, nil
    }

    return nil, ErrInvalidToken
}
```

### Rust (jsonwebtoken)

```rust
use jsonwebtoken::{decode, encode, DecodingKey, EncodingKey, Header, Validation};
use serde::{Deserialize, Serialize};
use chrono::{Duration, Utc};

#[derive(Debug, Serialize, Deserialize)]
struct Claims {
    sub: String,
    email: String,
    role: String,
    exp: i64,
    iat: i64,
}

fn create_access_token(user_id: &str, email: &str, role: &str, secret: &[u8]) -> Result<String, jsonwebtoken::errors::Error> {
    let now = Utc::now();
    let claims = Claims {
        sub: user_id.to_string(),
        email: email.to_string(),
        role: role.to_string(),
        iat: now.timestamp(),
        exp: (now + Duration::minutes(30)).timestamp(),
    };

    encode(&Header::default(), &claims, &EncodingKey::from_secret(secret))
}

fn verify_token(token: &str, secret: &[u8]) -> Result<Claims, jsonwebtoken::errors::Error> {
    let token_data = decode::<Claims>(
        token,
        &DecodingKey::from_secret(secret),
        &Validation::default(),
    )?;
    Ok(token_data.claims)
}
```

## OAuth 2.0 / OpenID Connect

### Python (authlib)

```python
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

config = Config(".env")
oauth = OAuth(config)

oauth.register(
    name="google",
    client_id=config("GOOGLE_CLIENT_ID"),
    client_secret=config("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

# In route handler
async def login_google(request: Request):
    redirect_uri = request.url_for("auth_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")
    # Create or update user in database
    return create_session(user_info)
```

### TypeScript (passport.js)

```typescript
import passport from 'passport'
import { Strategy as GoogleStrategy } from 'passport-google-oauth20'

passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
      callbackURL: '/auth/google/callback',
    },
    async (accessToken, refreshToken, profile, done) => {
      try {
        // Find or create user
        let user = await findUserByGoogleId(profile.id)
        if (!user) {
          user = await createUser({
            googleId: profile.id,
            email: profile.emails?.[0]?.value,
            name: profile.displayName,
          })
        }
        done(null, user)
      } catch (error) {
        done(error as Error)
      }
    }
  )
)

// Routes
app.get(
  '/auth/google',
  passport.authenticate('google', { scope: ['profile', 'email'] })
)

app.get(
  '/auth/google/callback',
  passport.authenticate('google', { failureRedirect: '/login' }),
  (req, res) => {
    res.redirect('/dashboard')
  }
)
```

## Session Management

### Python (Redis Sessions)

```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import redis
import secrets

redis_client = redis.Redis(host="localhost", port=6379, db=0)
SESSION_TTL = 3600 * 24  # 24 hours

def create_session(user_id: str) -> str:
    session_id = secrets.token_urlsafe(32)
    redis_client.setex(f"session:{session_id}", SESSION_TTL, user_id)
    return session_id

def get_session_user(session_id: str) -> str | None:
    user_id = redis_client.get(f"session:{session_id}")
    if user_id:
        # Refresh TTL on access
        redis_client.expire(f"session:{session_id}", SESSION_TTL)
        return user_id.decode()
    return None

def invalidate_session(session_id: str) -> None:
    redis_client.delete(f"session:{session_id}")

# Dependency
async def get_current_user(
    authorization: str = Depends(HTTPBearer()),
) -> User:
    session_id = authorization.credentials
    user_id = get_session_user(session_id)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid session")
    return await get_user_by_id(user_id)
```

### TypeScript (express-session + Redis)

```typescript
import session from 'express-session'
import RedisStore from 'connect-redis'
import { createClient } from 'redis'

const redisClient = createClient({ url: process.env.REDIS_URL })
await redisClient.connect()

app.use(
  session({
    store: new RedisStore({ client: redisClient }),
    secret: process.env.SESSION_SECRET!,
    resave: false,
    saveUninitialized: false,
    cookie: {
      secure: process.env.NODE_ENV === 'production',
      httpOnly: true,
      maxAge: 24 * 60 * 60 * 1000, // 24 hours
      sameSite: 'strict',
    },
  })
)

// Type augmentation for session
declare module 'express-session' {
  interface SessionData {
    userId: string
    email: string
  }
}

// Usage
app.post('/login', async (req, res) => {
  const user = await authenticateUser(req.body)
  req.session.userId = user.id
  req.session.email = user.email
  res.json({ success: true })
})

app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ error: 'Logout failed' })
    }
    res.clearCookie('connect.sid')
    res.json({ success: true })
  })
})
```

## API Key Authentication

### Python

```python
import secrets
import hashlib
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

def generate_api_key() -> tuple[str, str]:
    """Returns (raw_key, hashed_key)"""
    raw_key = secrets.token_urlsafe(32)
    hashed = hashlib.sha256(raw_key.encode()).hexdigest()
    return raw_key, hashed

def verify_api_key(raw_key: str, stored_hash: str) -> bool:
    hashed = hashlib.sha256(raw_key.encode()).hexdigest()
    return secrets.compare_digest(hashed, stored_hash)

async def get_api_key_user(
    api_key: str = Security(api_key_header),
) -> User:
    # Hash the provided key and look up in database
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()
    api_key_record = await get_api_key_by_hash(key_hash)

    if not api_key_record or not api_key_record.is_active:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return await get_user_by_id(api_key_record.user_id)
```

### Go

```go
import (
    "crypto/sha256"
    "crypto/subtle"
    "encoding/hex"
    "crypto/rand"
)

func GenerateAPIKey() (rawKey, hashedKey string, err error) {
    bytes := make([]byte, 32)
    if _, err := rand.Read(bytes); err != nil {
        return "", "", err
    }
    rawKey = hex.EncodeToString(bytes)

    hash := sha256.Sum256([]byte(rawKey))
    hashedKey = hex.EncodeToString(hash[:])
    return rawKey, hashedKey, nil
}

func VerifyAPIKey(rawKey, storedHash string) bool {
    hash := sha256.Sum256([]byte(rawKey))
    computedHash := hex.EncodeToString(hash[:])
    return subtle.ConstantTimeCompare([]byte(computedHash), []byte(storedHash)) == 1
}

// Middleware
func APIKeyAuth(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        apiKey := r.Header.Get("X-API-Key")
        if apiKey == "" {
            http.Error(w, "API key required", http.StatusUnauthorized)
            return
        }

        keyHash := sha256Hash(apiKey)
        record, err := db.GetAPIKeyByHash(keyHash)
        if err != nil || !record.IsActive {
            http.Error(w, "Invalid API key", http.StatusUnauthorized)
            return
        }

        ctx := context.WithValue(r.Context(), userContextKey, record.UserID)
        next.ServeHTTP(w, r.WithContext(ctx))
    })
}
```

## Security Best Practices

### Constant-Time Comparison (Prevent Timing Attacks)

```python
# Python
import secrets
secrets.compare_digest(provided_token, stored_token)
```

```typescript
// TypeScript
import crypto from 'crypto'
crypto.timingSafeEqual(Buffer.from(provided), Buffer.from(stored))
```

```go
// Go
import "crypto/subtle"
subtle.ConstantTimeCompare([]byte(provided), []byte(stored)) == 1
```

### Rate Limiting Login Attempts

```python
# Python with Redis
from datetime import timedelta

MAX_ATTEMPTS = 5
LOCKOUT_DURATION = timedelta(minutes=15)

async def check_login_attempts(email: str) -> bool:
    key = f"login_attempts:{email}"
    attempts = redis_client.get(key)
    if attempts and int(attempts) >= MAX_ATTEMPTS:
        return False  # Account locked
    return True

async def record_failed_attempt(email: str):
    key = f"login_attempts:{email}"
    pipe = redis_client.pipeline()
    pipe.incr(key)
    pipe.expire(key, int(LOCKOUT_DURATION.total_seconds()))
    pipe.execute()

async def clear_login_attempts(email: str):
    redis_client.delete(f"login_attempts:{email}")
```

### Secure Cookie Settings

```typescript
// TypeScript/Express
res.cookie('session', sessionId, {
  httpOnly: true, // Not accessible via JavaScript
  secure: true, // HTTPS only
  sameSite: 'strict', // CSRF protection
  maxAge: 24 * 60 * 60 * 1000, // 24 hours
  path: '/',
  domain: '.example.com',
})
```

```python
# Python/FastAPI
from fastapi.responses import Response

response.set_cookie(
    key="session",
    value=session_id,
    httponly=True,
    secure=True,
    samesite="strict",
    max_age=86400,
    path="/",
    domain=".example.com",
)
```
