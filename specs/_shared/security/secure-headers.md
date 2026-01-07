# HTTP Security Headers

Based on OWASP HTTP Security Headers Cheat Sheet.

## Essential Security Headers

### Content-Security-Policy (CSP)

Controls resources the browser is allowed to load. Primary defense against XSS.

```http
# Strict policy (recommended baseline)
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self';
```

**Directives explained:**
- `default-src 'self'` - Only load resources from same origin by default
- `script-src 'self'` - Only execute scripts from same origin
- `style-src 'self'` - Only load styles from same origin
- `img-src 'self' data:` - Images from same origin + data URIs
- `frame-ancestors 'none'` - Prevent clickjacking (replaces X-Frame-Options)
- `base-uri 'self'` - Restrict `<base>` tag
- `form-action 'self'` - Forms can only submit to same origin

```python
# Python/FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    )
    return response
```

```typescript
// Express.js with helmet
import helmet from 'helmet'

app.use(
  helmet.contentSecurityPolicy({
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'"],
      imgSrc: ["'self'", 'data:'],
      fontSrc: ["'self'"],
      connectSrc: ["'self'"],
      frameAncestors: ["'none'"],
      baseUri: ["'self'"],
      formAction: ["'self'"],
    },
  })
)
```

### Strict-Transport-Security (HSTS)

Forces HTTPS connections.

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

- `max-age=31536000` - Remember for 1 year
- `includeSubDomains` - Apply to all subdomains
- `preload` - Allow inclusion in browser preload lists

```python
# Python
response.headers["Strict-Transport-Security"] = (
    "max-age=31536000; includeSubDomains; preload"
)
```

```typescript
// Express.js
app.use(
  helmet.hsts({
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true,
  })
)
```

### X-Content-Type-Options

Prevents MIME type sniffing.

```http
X-Content-Type-Options: nosniff
```

```python
response.headers["X-Content-Type-Options"] = "nosniff"
```

### X-Frame-Options

Prevents clickjacking (legacy, use CSP frame-ancestors instead).

```http
X-Frame-Options: DENY
# Or for same-origin framing:
X-Frame-Options: SAMEORIGIN
```

### Referrer-Policy

Controls referrer information sent with requests.

```http
# Recommended - Send origin only for cross-origin requests
Referrer-Policy: strict-origin-when-cross-origin

# Most restrictive - Never send referrer
Referrer-Policy: no-referrer
```

```python
response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
```

### Permissions-Policy (formerly Feature-Policy)

Controls browser features and APIs.

```http
Permissions-Policy: geolocation=(), camera=(), microphone=(), payment=()
```

This disables geolocation, camera, microphone, and payment APIs.

```python
response.headers["Permissions-Policy"] = (
    "geolocation=(), camera=(), microphone=(), payment=()"
)
```

### X-XSS-Protection

Legacy XSS filter (modern browsers ignore, but set for older browsers).

```http
X-XSS-Protection: 1; mode=block
```

## Complete Security Headers Implementation

### Python/FastAPI

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

SECURITY_HEADERS = {
    "Content-Security-Policy": (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https:; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    ),
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "geolocation=(), camera=(), microphone=()",
    "X-XSS-Protection": "1; mode=block",
}

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    for header, value in SECURITY_HEADERS.items():
        response.headers[header] = value
    return response
```

### Express.js with Helmet

```typescript
import express from 'express'
import helmet from 'helmet'

const app = express()

// Helmet sets most security headers automatically
app.use(helmet())

// Custom CSP configuration
app.use(
  helmet.contentSecurityPolicy({
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:'],
      fontSrc: ["'self'"],
      connectSrc: ["'self'"],
      frameAncestors: ["'none'"],
      baseUri: ["'self'"],
      formAction: ["'self'"],
    },
  })
)

// Additional headers
app.use(
  helmet.permittedCrossDomainPolicies({
    permittedPolicies: 'none',
  })
)
```

### Go

```go
func securityHeaders(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; "+
            "img-src 'self' data:; frame-ancestors 'none'")
        w.Header().Set("Strict-Transport-Security",
            "max-age=31536000; includeSubDomains; preload")
        w.Header().Set("X-Content-Type-Options", "nosniff")
        w.Header().Set("X-Frame-Options", "DENY")
        w.Header().Set("Referrer-Policy", "strict-origin-when-cross-origin")
        w.Header().Set("Permissions-Policy", "geolocation=(), camera=()")

        next.ServeHTTP(w, r)
    })
}
```

### Nginx

```nginx
# /etc/nginx/conf.d/security-headers.conf

add_header Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; frame-ancestors 'none'" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), camera=(), microphone=()" always;
```

## CORS Headers

Cross-Origin Resource Sharing for APIs.

```python
# Python/FastAPI - Restrictive CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com", "https://app.example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=86400,  # Cache preflight for 24 hours
)
```

```typescript
// Express.js
import cors from 'cors'

app.use(
  cors({
    origin: ['https://example.com', 'https://app.example.com'],
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Authorization', 'Content-Type'],
    maxAge: 86400,
  })
)
```

**CORS Security Rules:**
- Never use `Access-Control-Allow-Origin: *` with credentials
- Validate Origin header against allowlist
- Be specific with allowed methods and headers
- Use appropriate max-age for preflight caching

## Cookie Security Attributes

```python
# Python/FastAPI
from fastapi import Response

response.set_cookie(
    key="session",
    value=session_id,
    httponly=True,      # Not accessible via JavaScript
    secure=True,        # HTTPS only
    samesite="strict",  # CSRF protection
    max_age=3600,       # 1 hour
    path="/",
    domain=".example.com",
)
```

```typescript
// Express.js
res.cookie('session', sessionId, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  maxAge: 3600000,
  path: '/',
  domain: '.example.com',
})
```

## Testing Security Headers

### Online Tools
- securityheaders.com - Scan and grade headers
- observatory.mozilla.org - Mozilla's security scanner

### Command Line

```bash
# Check headers with curl
curl -I https://example.com

# Check specific header
curl -s -I https://example.com | grep -i content-security-policy
```

## Header Checklist

| Header | Purpose | Recommended Value |
|--------|---------|-------------------|
| Content-Security-Policy | XSS prevention | `default-src 'self'` minimum |
| Strict-Transport-Security | Force HTTPS | `max-age=31536000; includeSubDomains` |
| X-Content-Type-Options | Prevent MIME sniffing | `nosniff` |
| X-Frame-Options | Clickjacking prevention | `DENY` or `SAMEORIGIN` |
| Referrer-Policy | Control referrer info | `strict-origin-when-cross-origin` |
| Permissions-Policy | Disable unused features | Disable what you don't need |
| Cache-Control | Sensitive data caching | `no-store` for sensitive pages |
