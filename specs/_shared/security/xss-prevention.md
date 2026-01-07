# Cross-Site Scripting (XSS) Prevention

Based on OWASP XSS Prevention Cheat Sheet.

## Overview

XSS attacks occur when an attacker injects malicious scripts into content that is then served to other users. The malicious script executes in the victim's browser with access to cookies, session tokens, and other sensitive information.

## Types of XSS

1. **Reflected XSS** - Malicious script comes from the current HTTP request
2. **Stored XSS** - Malicious script is stored on the server (database, file, etc.)
3. **DOM-based XSS** - Vulnerability exists in client-side code rather than server-side

## Primary Defense: Output Encoding

Encode data when outputting to HTML based on the context.

### HTML Context (Between Tags)

```python
# Python - Use framework's auto-escaping
from markupsafe import escape

user_input = "<script>alert('xss')</script>"
safe_output = escape(user_input)
# Result: &lt;script&gt;alert('xss')&lt;/script&gt;
```

```typescript
// TypeScript - HTML entity encoding
function escapeHtml(unsafe: string): string {
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;')
}
```

```go
// Go - html/template auto-escapes
import "html/template"

tmpl := template.Must(template.New("page").Parse(`
    <div>{{ .UserInput }}</div>
`))
// UserInput is automatically HTML-escaped
```

### Attribute Context

```html
<!-- SAFE - Quoted attribute with encoding -->
<div data-value="{{ user_input | escape }}">

<!-- VULNERABLE - Unquoted attribute -->
<div data-value={{ user_input }}>
```

Avoid placing user data in event handler attributes entirely.

### JavaScript Context

```typescript
// SAFE - JSON encoding for JavaScript context
const userData = JSON.stringify(userInput)
// Use in script: const data = ${userData};

// For HTML templates
<script>
  const userConfig = {{ user_data | tojson | safe }};
</script>
```

```python
# Python/Jinja2 - JSON encoding
import json

@app.template_filter('json_encode')
def json_encode(value):
    return json.dumps(value)

# Template: <script>const data = {{ user_data | json_encode }};</script>
```

### URL Context

```python
# Python - URL encoding
from urllib.parse import quote, urlencode

# Single parameter
safe_param = quote(user_input, safe='')

# Building query string
params = urlencode({'search': user_input, 'page': 1})
url = f"/search?{params}"
```

```typescript
// TypeScript - URL encoding
const safeParam = encodeURIComponent(userInput)
const url = `/search?q=${safeParam}`

// Using URLSearchParams
const params = new URLSearchParams({ search: userInput })
const url = `/search?${params.toString()}`
```

### CSS Context

```python
# Validate CSS values against allow-list
ALLOWED_COLORS = {"red", "blue", "green", "#000000", "#ffffff"}

def safe_color(user_color: str) -> str:
    if user_color in ALLOWED_COLORS:
        return user_color
    return "inherit"  # Safe default
```

Avoid putting user input in CSS whenever possible.

## Framework-Specific Protection

### React

React escapes content by default when using JSX expressions:

```tsx
// SAFE - React escapes by default
function UserProfile({ name }: { name: string }) {
  return <div>{name}</div> // Automatically escaped
}
```

If you need to render HTML content, always sanitize first with DOMPurify:

```tsx
import DOMPurify from 'dompurify'

function SafeHtmlContent({ html }: { html: string }) {
  // Sanitize before rendering
  const cleanHtml = DOMPurify.sanitize(html)
  // Then use React's raw HTML rendering with the sanitized content
  return <div dangerouslySetInnerHTML={{ __html: cleanHtml }} />
}
```

### Vue.js

```vue
<template>
  <!-- SAFE - Double mustache escapes -->
  <div>{{ userInput }}</div>

  <!-- If you need HTML, sanitize first -->
  <div v-html="sanitizedHtml"></div>
</template>

<script setup>
import DOMPurify from 'dompurify'
import { computed } from 'vue'

const props = defineProps<{ userInput: string }>()

const sanitizedHtml = computed(() => DOMPurify.sanitize(props.userInput))
</script>
```

### Django

```html
<!-- SAFE - Auto-escaping enabled by default -->
<div>{{ user_input }}</div>
```

```python
# Django - Sanitize HTML if needed
import bleach

ALLOWED_TAGS = ['p', 'br', 'strong', 'em', 'a']
ALLOWED_ATTRS = {'a': ['href', 'title']}

def sanitize_html(html: str) -> str:
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        strip=True
    )
```

### Express.js

```typescript
// Use a templating engine with auto-escaping
import express from 'express'
import nunjucks from 'nunjucks'

const app = express()

nunjucks.configure('views', {
  autoescape: true, // Enable auto-escaping
  express: app,
})
```

## DOM-Based XSS Prevention

### Safe DOM Manipulation

```typescript
// SAFE - Using textContent (no HTML parsing)
element.textContent = userInput

// SAFE - Creating elements programmatically
function createUserCard(user: { name: string; bio: string }) {
  const card = document.createElement('div')
  card.className = 'user-card'

  const name = document.createElement('h3')
  name.textContent = user.name // Safe - textContent doesn't parse HTML

  const bio = document.createElement('p')
  bio.textContent = user.bio

  card.appendChild(name)
  card.appendChild(bio)
  return card
}
```

Avoid using innerHTML, outerHTML, or document.write with user input.

### URL Handling

```typescript
// SAFE - Validate URL scheme before use
function safeUrl(url: string): string {
  try {
    const parsed = new URL(url, window.location.origin)
    if (parsed.protocol === 'http:' || parsed.protocol === 'https:') {
      return parsed.href
    }
  } catch {
    // Invalid URL
  }
  return '#' // Safe fallback
}

// Usage
element.href = safeUrl(userProvidedUrl)
```

## Content Security Policy (CSP)

CSP is a defense-in-depth measure that mitigates XSS impact.

```http
# Strict CSP (recommended)
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none';

# With nonce for inline scripts (if needed)
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{random}';
```

```python
# Python/FastAPI - CSP header
from fastapi import FastAPI
import secrets

app = FastAPI()

@app.middleware("http")
async def add_csp_header(request, call_next):
    response = await call_next(request)
    nonce = secrets.token_urlsafe(16)
    response.headers["Content-Security-Policy"] = (
        f"default-src 'self'; "
        f"script-src 'self' 'nonce-{nonce}'; "
        f"style-src 'self' 'unsafe-inline'; "
        f"img-src 'self' data:; "
        f"frame-ancestors 'none'"
    )
    return response
```

```typescript
// Express.js - helmet for CSP
import helmet from 'helmet'

app.use(
  helmet.contentSecurityPolicy({
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:'],
      frameAncestors: ["'none'"],
    },
  })
)
```

## HTML Sanitization Libraries

When you need to allow some HTML (rich text editors, markdown, etc.):

### Python - bleach

```python
import bleach

# Define allowed tags and attributes
ALLOWED_TAGS = [
    'p', 'br', 'strong', 'em', 'u', 's',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'ul', 'ol', 'li',
    'a', 'img',
    'blockquote', 'code', 'pre',
]

ALLOWED_ATTRS = {
    'a': ['href', 'title'],
    'img': ['src', 'alt', 'title'],
}

def sanitize_user_html(html: str) -> str:
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        strip=True,
        protocols=['http', 'https', 'mailto'],
    )
```

### TypeScript/JavaScript - DOMPurify

```typescript
import DOMPurify from 'dompurify'

// Basic sanitization
const clean = DOMPurify.sanitize(dirtyHtml)

// With configuration
const clean = DOMPurify.sanitize(dirtyHtml, {
  ALLOWED_TAGS: ['p', 'br', 'strong', 'em', 'a', 'ul', 'ol', 'li'],
  ALLOWED_ATTR: ['href', 'title'],
  ALLOW_DATA_ATTR: false,
})
```

## Summary: XSS Prevention Rules

1. **Never trust user input** - All user data is potentially malicious
2. **Use context-appropriate encoding** - HTML, JavaScript, URL, CSS contexts need different encoding
3. **Prefer textContent over innerHTML** - For DOM manipulation
4. **Use frameworks with auto-escaping** - React, Vue, Angular, Django, Jinja2
5. **Sanitize when allowing HTML** - Use DOMPurify, bleach, or similar
6. **Implement CSP** - Defense in depth
7. **Set HttpOnly on cookies** - Prevents JavaScript access to session cookies
8. **Validate URLs** - Check scheme before using in href/src attributes
