# YAML Generation Checklist

**Read this BEFORE writing YAML. Indentation and quoting matter—a lot.**

## Critical: You Must Do These

### 1. Use Consistent Indentation (2 Spaces Recommended)
```yaml
# BAD - mixed indentation
services:
  web:
      image: nginx     # 4 spaces
      ports:
        - "80:80"      # 6 spaces - inconsistent!

# GOOD - consistent 2-space indentation
services:
  web:
    image: nginx
    ports:
      - "80:80"
```

### 2. Quote Strings That Look Like Other Types
```yaml
# DANGEROUS - these are not strings!
version: 1.0        # Float, not string "1.0"
version: 3.10       # Float 3.1, not string "3.10"!
enabled: yes        # Boolean true
enabled: no         # Boolean false
enabled: on         # Boolean true
time: 12:30:00      # Sexagesimal number!
country: NO         # Boolean false, not Norway!

# SAFE - quoted strings
version: "1.0"
version: "3.10"     # Now it's really "3.10"
enabled: "yes"
time: "12:30:00"
country: "NO"
```

### 3. Always Quote Special Characters
```yaml
# BAD - will cause parse errors or unexpected behavior
message: Hello: World     # Colon issue
path: C:\Users\name       # Backslash escape
regex: [a-z]+             # Looks like array
command: echo "hello"     # Nested quotes

# GOOD - quoted
message: "Hello: World"
path: 'C:\Users\name'     # Single quotes for literal
regex: "[a-z]+"
command: 'echo "hello"'
```

### 4. Use Block Scalars for Multi-line Strings
```yaml
# BAD - hard to read, escape issues
description: "This is a long description that spans multiple lines and includes \"quotes\" and other special characters"

# GOOD - literal block (preserves newlines and spacing)
description: |
  This is a long description
  that preserves line breaks
  exactly as written.

# GOOD - folded block (joins lines with spaces)
description: >
  This is a long description
  that will be joined into
  a single line with spaces.

# With chomping indicators
content: |+   # Keep trailing newlines
content: |-   # Strip trailing newlines
```

### 5. Use Anchors and Aliases to Avoid Repetition
```yaml
# BAD - duplicated content
development:
  database:
    host: localhost
    port: 5432
    pool: 5
test:
  database:
    host: localhost
    port: 5432
    pool: 5

# GOOD - anchor and alias
defaults: &database_defaults
  host: localhost
  port: 5432
  pool: 5

development:
  database:
    <<: *database_defaults

test:
  database:
    <<: *database_defaults

production:
  database:
    <<: *database_defaults
    host: db.production.com
    pool: 20
```

## Important: Strong Recommendations

### 6. Use Explicit Types When Ambiguous
```yaml
# When you need specific types
port: !!int "8080"
version: !!str 1.0
enabled: !!bool "true"
empty: !!null ""
```

### 7. Prefer Consistent Key Quoting Style
```yaml
# Pick one style and stick with it

# Style 1: No quotes (for simple keys)
name: myapp
version: "1.0"

# Style 2: Always quote string values
name: "myapp"
version: "1.0"

# Keys with special characters MUST be quoted
"key:with:colons": value
"key with spaces": value
```

### 8. Format Lists Consistently
```yaml
# Block style (preferred for readability)
dependencies:
  - package-a
  - package-b
  - package-c

# Flow style (for short lists)
tags: [api, backend, v2]

# Don't mix in the same file
```

### 9. Format Maps Consistently
```yaml
# Block style (preferred)
database:
  host: localhost
  port: 5432

# Flow style (for simple, short maps)
point: {x: 10, y: 20}

# Avoid flow style for complex nested structures
```

### 10. Use Comments Effectively
```yaml
# Application configuration
# Updated: 2024-01-15

server:
  # Host to bind to (0.0.0.0 for all interfaces)
  host: 0.0.0.0

  # Port number (must be > 1024 for non-root)
  port: 8080

  # Timeout in seconds
  timeout: 30  # Increase for slow networks
```

## Common Pitfalls

### 11. Beware of Implicit Type Conversion
```yaml
# These may not be what you expect:
octal: 0777          # Octal number in YAML 1.1
float: .inf          # Infinity
null_value: ~        # null
null_also: null      # null
empty:               # null (no value)
```

### 12. Handle Empty Values Correctly
```yaml
# Explicit null
value: null
value: ~

# Empty string
value: ""
value: ''

# Not the same as missing key!
# Missing key: key doesn't exist
# Null value: key exists with null value
# Empty string: key exists with empty string value
```

### 13. Validate Environment-Specific Values
```yaml
# GOOD - clear environment separation
defaults: &defaults
  log_level: info
  timeout: 30

development:
  <<: *defaults
  debug: true
  log_level: debug

production:
  <<: *defaults
  debug: false
  # Override only what's different
```

## Security

### 14. Never Include Secrets in YAML Files
```yaml
# DANGEROUS - secrets in config
database:
  password: MySecretPassword123

# SAFE - use environment variable references
database:
  password: ${DB_PASSWORD}
  # Or
  password: !env DB_PASSWORD

# SAFE - reference external secret store
database:
  password: !secret database_password
```

### 15. Be Careful with YAML Deserialization
```yaml
# In application code, be aware that YAML can contain:
# - Arbitrary type instantiation (in some parsers)
# - Large data structures (billion laughs attack)
# - Binary data

# Always use safe loaders:
# Python: yaml.safe_load() not yaml.load()
# Ruby: YAML.safe_load() not YAML.load()
# Java: Use SnakeYAML with restricted types
```

### 16. Validate Schema
```yaml
# Use JSON Schema or similar to validate YAML structure
# Example with Docker Compose (validates automatically)
# Example with Kubernetes (use kubectl --dry-run=client)
# Example with CI/CD configs (yamllint, validate tools)
```

---

**Quick Reference - Copy This Mental Model:**
- Consistent 2-space indentation
- Quote strings that look like numbers/booleans
- Quote special characters (: @ # etc.)
- Block scalars (`|` or `>`) for multi-line
- Anchors (`&`) and aliases (`*`) for DRY
- Explicit types when ambiguous (`!!str`)
- Consistent list/map formatting
- Beware implicit type conversion
- Empty string `""` vs null `~` vs missing
- Never hardcode secrets
- Use safe YAML loaders
- Validate with schema/linter
