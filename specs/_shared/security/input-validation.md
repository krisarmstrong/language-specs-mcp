# Input Validation

Based on OWASP Input Validation Cheat Sheet.

## Overview

Input validation is a first line of defense. It should be applied to all input from untrusted sources: user input, API parameters, file uploads, cookies, HTTP headers, and data from external systems.

## Validation Strategies

### 1. Allow-list Validation (Preferred)

Define exactly what IS allowed, reject everything else.

```python
# Python - Allow-list validation
import re
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"

def validate_username(username: str) -> str:
    """Only alphanumeric and underscore, 3-20 chars"""
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Invalid username format")
    return username

def validate_role(role: str) -> UserRole:
    """Only allowed enum values"""
    try:
        return UserRole(role)
    except ValueError:
        raise ValueError(f"Invalid role: {role}")
```

```typescript
// TypeScript - Allow-list with Zod
import { z } from 'zod'

const UserRole = z.enum(['user', 'admin', 'moderator'])

const UsernameSchema = z
  .string()
  .min(3)
  .max(20)
  .regex(/^[a-zA-Z0-9_]+$/, 'Only alphanumeric and underscore allowed')

const UserInputSchema = z.object({
  username: UsernameSchema,
  role: UserRole,
  email: z.string().email(),
  age: z.number().int().min(0).max(150),
})

// Validate
const result = UserInputSchema.safeParse(input)
if (!result.success) {
  throw new ValidationError(result.error.issues)
}
```

### 2. Deny-list Validation (Less Secure)

Block known bad patterns. Use only as additional layer, not primary defense.

```python
# Deny-list is fragile - attackers find bypasses
BLOCKED_PATTERNS = ['<script', 'javascript:', 'onerror=']

def check_denylist(value: str) -> bool:
    lower_value = value.lower()
    return not any(pattern in lower_value for pattern in BLOCKED_PATTERNS)

# Better: Use allow-list + output encoding instead
```

## Data Type Validation

### Strings

```python
# Python with Pydantic
from pydantic import BaseModel, Field, field_validator
import re

class UserProfile(BaseModel):
    # Length constraints
    name: str = Field(..., min_length=1, max_length=100)

    # Pattern matching
    phone: str = Field(..., pattern=r'^\+?[1-9]\d{1,14}$')

    # Custom validation
    bio: str = Field(default="", max_length=500)

    @field_validator('name')
    @classmethod
    def name_must_be_printable(cls, v: str) -> str:
        if not v.isprintable():
            raise ValueError('Name must contain only printable characters')
        return v.strip()
```

```typescript
// TypeScript with Zod
const ProfileSchema = z.object({
  name: z
    .string()
    .min(1)
    .max(100)
    .refine((s) => /^[\p{L}\p{N}\s'-]+$/u.test(s), {
      message: 'Name contains invalid characters',
    }),
  phone: z.string().regex(/^\+?[1-9]\d{1,14}$/, 'Invalid phone format'),
  bio: z.string().max(500).default(''),
})
```

### Numbers

```python
# Python
from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    quantity: int = Field(..., gt=0, le=1000)
    price: float = Field(..., gt=0, le=1000000)
    discount_percent: float = Field(default=0, ge=0, le=100)
```

```typescript
// TypeScript
const OrderItemSchema = z.object({
  quantity: z.number().int().positive().max(1000),
  price: z.number().positive().max(1000000),
  discountPercent: z.number().min(0).max(100).default(0),
})
```

### Dates

```python
from datetime import date, datetime
from pydantic import BaseModel, field_validator

class EventBooking(BaseModel):
    event_date: date

    @field_validator('event_date')
    @classmethod
    def date_must_be_future(cls, v: date) -> date:
        if v < date.today():
            raise ValueError('Event date must be in the future')
        return v
```

```typescript
const BookingSchema = z.object({
  eventDate: z.coerce.date().refine((d) => d > new Date(), {
    message: 'Event date must be in the future',
  }),
})
```

### Arrays/Lists

```python
from pydantic import BaseModel, Field

class BulkOrder(BaseModel):
    # Limit array size
    item_ids: list[int] = Field(..., min_length=1, max_length=100)

    # Validate each element
    tags: list[str] = Field(default_factory=list, max_length=10)
```

```typescript
const BulkOrderSchema = z.object({
  itemIds: z.array(z.number().int().positive()).min(1).max(100),
  tags: z.array(z.string().max(50)).max(10).default([]),
})
```

## Email Validation

```python
# Python - Use email-validator library
from email_validator import validate_email, EmailNotValidError

def validate_email_address(email: str) -> str:
    try:
        # Validate and normalize
        result = validate_email(email, check_deliverability=False)
        return result.normalized
    except EmailNotValidError as e:
        raise ValueError(f"Invalid email: {e}")

# Or with Pydantic
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr  # Built-in email validation
```

```typescript
// TypeScript - Zod has built-in email
const UserSchema = z.object({
  email: z.string().email(),
})

// For stricter validation, use a library
import isEmail from 'validator/lib/isEmail'

const StrictEmailSchema = z.string().refine((e) => isEmail(e), {
  message: 'Invalid email format',
})
```

## URL Validation

```python
from urllib.parse import urlparse
from pydantic import BaseModel, field_validator

class LinkSubmission(BaseModel):
    url: str

    @field_validator('url')
    @classmethod
    def validate_url(cls, v: str) -> str:
        try:
            result = urlparse(v)
            # Only allow http/https
            if result.scheme not in ('http', 'https'):
                raise ValueError('Only HTTP(S) URLs allowed')
            if not result.netloc:
                raise ValueError('Invalid URL')
            return v
        except Exception:
            raise ValueError('Invalid URL format')
```

```typescript
const UrlSchema = z.string().url().refine(
  (url) => {
    try {
      const parsed = new URL(url)
      return ['http:', 'https:'].includes(parsed.protocol)
    } catch {
      return false
    }
  },
  { message: 'Only HTTP(S) URLs allowed' }
)
```

## File Upload Validation

```python
from pathlib import Path
import magic  # python-magic library

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.pdf'}
ALLOWED_MIME_TYPES = {
    'image/jpeg', 'image/png', 'image/gif', 'application/pdf'
}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def validate_upload(filename: str, content: bytes) -> None:
    # Check file extension
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"File type {ext} not allowed")

    # Check file size
    if len(content) > MAX_FILE_SIZE:
        raise ValueError("File too large")

    # Check actual MIME type (not just extension)
    mime_type = magic.from_buffer(content, mime=True)
    if mime_type not in ALLOWED_MIME_TYPES:
        raise ValueError(f"File content type {mime_type} not allowed")

    # Additional checks for images
    if mime_type.startswith('image/'):
        validate_image_content(content)

def validate_image_content(content: bytes) -> None:
    from PIL import Image
    import io

    try:
        img = Image.open(io.BytesIO(content))
        img.verify()  # Check for corruption

        # Limit dimensions
        if img.width > 4096 or img.height > 4096:
            raise ValueError("Image dimensions too large")
    except Exception as e:
        raise ValueError(f"Invalid image: {e}")
```

```typescript
// TypeScript/Node.js
import { fileTypeFromBuffer } from 'file-type'

const ALLOWED_MIME_TYPES = new Set([
  'image/jpeg',
  'image/png',
  'image/gif',
  'application/pdf',
])
const MAX_FILE_SIZE = 10 * 1024 * 1024

async function validateUpload(
  filename: string,
  buffer: Buffer
): Promise<void> {
  // Check size
  if (buffer.length > MAX_FILE_SIZE) {
    throw new Error('File too large')
  }

  // Check actual file type
  const type = await fileTypeFromBuffer(buffer)
  if (!type || !ALLOWED_MIME_TYPES.has(type.mime)) {
    throw new Error(`File type not allowed: ${type?.mime ?? 'unknown'}`)
  }
}
```

## Sanitization vs Validation

**Validation**: Check if input meets criteria, reject if not
**Sanitization**: Transform input to make it safe

```python
# Validation - Reject invalid input
def validate_age(age: str) -> int:
    value = int(age)  # Raises if not numeric
    if not (0 <= value <= 150):
        raise ValueError("Age must be between 0 and 150")
    return value

# Sanitization - Transform input
def sanitize_filename(filename: str) -> str:
    # Remove path separators and null bytes
    safe = filename.replace('/', '').replace('\\', '').replace('\x00', '')
    # Keep only safe characters
    safe = re.sub(r'[^\w\-.]', '_', safe)
    # Limit length
    return safe[:255]
```

## Server-Side Validation is Mandatory

Client-side validation is for UX only. Always validate on the server.

```python
# FastAPI - Server-side validation with Pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    password: str = Field(..., min_length=8)

@app.post("/users")
async def create_user(user: UserCreate):
    # Pydantic automatically validates before this function runs
    # Invalid input returns 422 Unprocessable Entity
    return await user_service.create(user)
```

```typescript
// Express.js - Validate with Zod middleware
import { z } from 'zod'

const CreateUserSchema = z.object({
  username: z.string().min(3).max(20).regex(/^[a-zA-Z0-9_]+$/),
  email: z.string().email(),
  password: z.string().min(8),
})

function validate<T>(schema: z.Schema<T>) {
  return (req: Request, res: Response, next: NextFunction) => {
    const result = schema.safeParse(req.body)
    if (!result.success) {
      return res.status(422).json({ errors: result.error.issues })
    }
    req.body = result.data
    next()
  }
}

app.post('/users', validate(CreateUserSchema), createUser)
```

## Validation Error Messages

Don't leak sensitive information in error messages.

```python
# BAD - Reveals too much
raise ValueError(f"User {username} already exists in database users table")

# GOOD - Generic message
raise ValueError("Username is not available")

# BAD - Helps attackers enumerate
if not user:
    raise ValueError("User not found")
if not check_password(password, user.password_hash):
    raise ValueError("Wrong password")

# GOOD - Same message for both cases
if not user or not check_password(password, user.password_hash):
    raise ValueError("Invalid username or password")
```
