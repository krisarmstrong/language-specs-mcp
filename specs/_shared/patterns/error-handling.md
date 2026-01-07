# Cross-Language Error Handling Patterns

Universal principles for error handling across programming languages.

## Core Principles

1. **Be Specific** - Catch specific errors, not generic ones
2. **Fail Fast** - Validate inputs early, fail immediately on invalid state
3. **Don't Swallow Errors** - Always log or propagate errors
4. **Use Custom Errors** - Create domain-specific error types
5. **Include Context** - Error messages should explain what happened and why

## Language Implementations

### Python

```python
# Custom exception hierarchy
class AppError(Exception):
    """Base exception for application errors."""
    pass

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    def __init__(self, resource: str, id: str):
        super().__init__(f"{resource} with id '{id}' not found")

# Usage with context
def get_user(user_id: str) -> User:
    try:
        return database.find_user(user_id)
    except DatabaseError as e:
        logger.error(f"Database error fetching user {user_id}", exc_info=True)
        raise NotFoundError("User", user_id) from e
```

### TypeScript

```typescript
// Custom error classes
class AppError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500
  ) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}

class ValidationError extends AppError {
  constructor(
    public field: string,
    message: string
  ) {
    super(message, "VALIDATION_ERROR", 400);
  }
}

class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(`${resource} with id '${id}' not found`, "NOT_FOUND", 404);
  }
}

// Result type pattern
type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };

function parseJSON<T>(json: string): Result<T> {
  try {
    return { ok: true, value: JSON.parse(json) };
  } catch (error) {
    return { ok: false, error: error as Error };
  }
}
```

### Go

```go
// Custom error types
type AppError struct {
    Code    string
    Message string
    Err     error
}

func (e *AppError) Error() string {
    if e.Err != nil {
        return fmt.Sprintf("%s: %v", e.Message, e.Err)
    }
    return e.Message
}

func (e *AppError) Unwrap() error {
    return e.Err
}

// Sentinel errors
var (
    ErrNotFound     = &AppError{Code: "NOT_FOUND", Message: "resource not found"}
    ErrUnauthorized = &AppError{Code: "UNAUTHORIZED", Message: "unauthorized"}
)

// Wrapping errors with context
func GetUser(id string) (*User, error) {
    user, err := db.FindUser(id)
    if err != nil {
        if errors.Is(err, sql.ErrNoRows) {
            return nil, fmt.Errorf("get user %s: %w", id, ErrNotFound)
        }
        return nil, fmt.Errorf("get user %s: %w", id, err)
    }
    return user, nil
}
```

### Rust

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("validation error on field '{field}': {message}")]
    Validation { field: String, message: String },

    #[error("{resource} with id '{id}' not found")]
    NotFound { resource: String, id: String },

    #[error("database error: {0}")]
    Database(#[from] sqlx::Error),
}

// Using Result
fn get_user(id: &str) -> Result<User, AppError> {
    let user = db::find_user(id)
        .map_err(|e| AppError::NotFound {
            resource: "User".into(),
            id: id.into(),
        })?;
    Ok(user)
}
```

## Anti-Patterns

### Don't Catch and Ignore

```python
# BAD
try:
    risky_operation()
except Exception:
    pass  # Silent failure!

# GOOD
try:
    risky_operation()
except SpecificError as e:
    logger.warning(f"Operation failed: {e}")
    return default_value
```

### Don't Use Exceptions for Flow Control

```typescript
// BAD
function findUser(id: string): User {
  const user = users.find((u) => u.id === id);
  if (!user) throw new Error("Not found"); // Exception for expected case
  return user;
}

// GOOD
function findUser(id: string): User | undefined {
  return users.find((u) => u.id === id);
}
```

### Don't Expose Internal Details

```go
// BAD - Exposes implementation details
return fmt.Errorf("postgres connection failed: %s", connString)

// GOOD - Abstract the error
return fmt.Errorf("database unavailable")
```
