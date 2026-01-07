# Injection Prevention

Based on OWASP Injection Prevention Cheat Sheet.

## Overview

Injection flaws occur when untrusted data is sent to an interpreter as part of a command or query. The attacker's hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.

## SQL Injection Prevention

### Defense Option 1: Prepared Statements (Parameterized Queries)

The most effective defense. Query structure is defined first, then parameters are bound.

```python
# Python - SQLAlchemy
from sqlalchemy import text

# SAFE - Parameterized query
stmt = text("SELECT * FROM users WHERE email = :email AND status = :status")
result = session.execute(stmt, {"email": user_email, "status": "active"})

# SAFE - ORM queries are automatically parameterized
user = session.query(User).filter(User.email == user_email).first()
```

```java
// Java - JDBC PreparedStatement
String sql = "SELECT * FROM users WHERE email = ? AND status = ?";
PreparedStatement stmt = connection.prepareStatement(sql);
stmt.setString(1, userEmail);
stmt.setString(2, "active");
ResultSet rs = stmt.executeQuery();

// Java - JPA
TypedQuery<User> query = em.createQuery(
    "SELECT u FROM User u WHERE u.email = :email", User.class);
query.setParameter("email", userEmail);
User user = query.getSingleResult();
```

```go
// Go - database/sql
row := db.QueryRow(
    "SELECT id, email, name FROM users WHERE email = $1 AND status = $2",
    userEmail, "active",
)

// Go - sqlx
var user User
err := db.Get(&user,
    "SELECT * FROM users WHERE email = $1 AND status = $2",
    userEmail, "active",
)
```

```typescript
// TypeScript - Prisma (automatically parameterized)
const user = await prisma.user.findFirst({
  where: {
    email: userEmail,
    status: 'active',
  },
})

// TypeScript - raw query with parameters
const users = await prisma.$queryRaw`
  SELECT * FROM users WHERE email = ${userEmail} AND status = 'active'
`
```

```rust
// Rust - sqlx (compile-time checked)
let user = sqlx::query_as!(
    User,
    "SELECT id, email, name FROM users WHERE email = $1 AND status = $2",
    user_email,
    "active"
)
.fetch_optional(&pool)
.await?;
```

### What NOT to Do (SQL Injection Vulnerabilities)

Never concatenate or interpolate user input directly into SQL strings. Avoid patterns like:
- f-string interpolation in SQL queries
- String concatenation with `+` operator
- `%` formatting operator with SQL
- Any method that embeds user data directly in the query string

### Defense Option 2: Stored Procedures

Can be safe if they don't generate dynamic SQL internally.

```sql
-- Safe stored procedure (no dynamic SQL)
CREATE PROCEDURE GetUserByEmail(IN user_email VARCHAR(255))
BEGIN
    SELECT id, email, name FROM users WHERE email = user_email;
END;
```

```python
# Calling stored procedure
cursor.callproc('GetUserByEmail', [user_email])
```

### Defense Option 3: Allow-list Input Validation

For cases where parameterization isn't possible (table names, column names, sort order).

```python
# Table name validation (cannot be parameterized)
ALLOWED_TABLES = {"users", "orders", "products"}

def get_records(table_name: str, limit: int):
    if table_name not in ALLOWED_TABLES:
        raise ValueError(f"Invalid table: {table_name}")

    # Safe because table_name is validated against allow-list
    query = f"SELECT * FROM {table_name} LIMIT %s"
    cursor.execute(query, (limit,))
```

```python
# Sort order validation
ALLOWED_SORT_ORDERS = {"ASC", "DESC"}
ALLOWED_COLUMNS = {"created_at", "name", "email"}

def get_sorted_users(sort_column: str, sort_order: str):
    if sort_column not in ALLOWED_COLUMNS:
        raise ValueError("Invalid sort column")
    if sort_order.upper() not in ALLOWED_SORT_ORDERS:
        raise ValueError("Invalid sort order")

    query = f"SELECT * FROM users ORDER BY {sort_column} {sort_order}"
    cursor.execute(query)
```

## OS Command Injection Prevention

### Primary Defense: Avoid Shell Commands

Use APIs that pass arguments directly without shell interpolation.

```python
# SAFE - Separate command and arguments (no shell)
import subprocess
import re

def ping_host(hostname: str) -> str:
    # Validate hostname format first
    if not re.match(r'^[a-zA-Z0-9.-]+$', hostname):
        raise ValueError("Invalid hostname")

    result = subprocess.run(
        ["ping", "-c", "4", hostname],  # Arguments as list
        capture_output=True,
        text=True,
        timeout=30,
        shell=False  # Important: no shell interpolation
    )
    return result.stdout
```

```go
// Go - Separate command from arguments
import "os/exec"

func pingHost(hostname string) (string, error) {
    // Validate hostname
    if !isValidHostname(hostname) {
        return "", errors.New("invalid hostname")
    }

    // Arguments passed directly, not through shell
    cmd := exec.Command("ping", "-c", "4", hostname)
    output, err := cmd.Output()
    return string(output), err
}
```

```typescript
// TypeScript/Node.js - Use execFile, not shell execution
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function pingHost(hostname: string): Promise<string> {
  // Validate
  if (!/^[a-zA-Z0-9.-]+$/.test(hostname)) {
    throw new Error('Invalid hostname')
  }

  // execFile passes arguments directly, no shell interpretation
  const { stdout } = await execFileAsync('ping', ['-c', '4', hostname], {
    timeout: 30000,
  })
  return stdout
}
```

### What NOT to Do (Command Injection Vulnerabilities)

Avoid these dangerous patterns:
- `shell=True` with any user-influenced data in subprocess
- Functions that invoke a shell interpreter with user data
- String concatenation to build command strings

### Use Libraries Instead of Commands

```python
# Instead of calling external commands, use libraries:

# HTTP requests - use httpx/requests instead of curl
import httpx
response = httpx.get(url)

# Image processing - use Pillow instead of ImageMagick CLI
from PIL import Image
img = Image.open(input_file)
img.save(output_file)

# Archives - use shutil instead of zip/tar CLI
import shutil
shutil.make_archive(archive_name, 'zip', directory)
```

## NoSQL Injection Prevention

### MongoDB

```javascript
// VULNERABLE - Object injection allows query manipulation
// If user sends: { "password": { "$ne": "" } }
// Query becomes: find where password is NOT empty (bypasses auth)

// SAFE - Enforce string type
const username = String(req.body.username).slice(0, 100)
const password = String(req.body.password)

const user = await db.users.findOne({
  username: username, // Guaranteed to be string
  password: password, // Guaranteed to be string
})
```

```python
# Python - MongoDB with Pydantic type validation
from pydantic import BaseModel, constr

class LoginRequest(BaseModel):
    username: constr(max_length=100)
    password: str

@app.post("/login")
async def login(request: LoginRequest):
    # Pydantic ensures username and password are strings, not objects
    user = await db.users.find_one({
        "username": request.username,
        "password_hash": hash_password(request.password)
    })
```

### Redis

```python
# SAFE - Use type-safe Redis client methods
def get_user_data(user_id: str):
    # Validate user_id format
    if not user_id.isalnum():
        raise ValueError("Invalid user ID")

    # Use Redis client methods, not raw command strings
    return redis.get(f"user:{user_id}")
```

## LDAP Injection Prevention

```python
# SAFE - Escape LDAP special characters
import ldap

def find_user(username: str):
    # Escape LDAP special characters: * ( ) \ NUL
    escaped = ldap.filter.escape_filter_chars(username)
    search_filter = f"(uid={escaped})"

    conn.search(
        search_base="ou=users,dc=example,dc=com",
        search_filter=search_filter,
        search_scope=ldap.SCOPE_SUBTREE
    )
```

## XPath Injection Prevention

```python
# SAFE - Use parameterized XPath (lxml)
from lxml import etree

def find_user(username: str, password: str):
    tree = etree.parse("users.xml")
    # Parameterized query - values are properly escaped
    users = tree.xpath(
        "//user[username=$username and password=$password]",
        username=username,
        password=password
    )
    return users[0] if users else None
```

## Template Injection Prevention

### Server-Side Template Injection (SSTI)

```python
# SAFE - Pass data to template context, don't interpolate into template string
from jinja2 import Template

def render_greeting(name: str):
    template = Template("Hello, {{ name }}!")
    return template.render(name=name)  # name is properly escaped

# BETTER - Use autoescape for HTML contexts
from jinja2 import Environment, select_autoescape

env = Environment(autoescape=select_autoescape(['html', 'xml']))
template = env.from_string("Hello, {{ name }}!")
```

### What NOT to Do (Template Injection)

Never interpolate user input into the template string itself before parsing. User input should only be passed as template context variables.

## Summary: Defense Hierarchy

1. **Parameterized queries** - First choice for SQL
2. **Safe APIs** - Use type-safe libraries (ORMs, API clients)
3. **Allow-list validation** - For structural elements (table names, columns)
4. **Escape user input** - Last resort, error-prone
5. **Least privilege** - Limit database/system account permissions

## Detection Checklist for Code Review

Look for these vulnerability patterns:

**SQL Injection indicators:**
- String formatting with f-strings, `.format()`, `%` operator in SQL
- String concatenation (`+`) building SQL queries
- User input not going through ORM or parameterized query

**Command Injection indicators:**
- `shell=True` with any user-influenced data
- String concatenation building shell commands
- Functions that spawn shells with user data

**NoSQL Injection indicators:**
- Request body objects passed directly to database queries
- Missing type validation on query parameters

**Template Injection indicators:**
- User input interpolated into template strings before parsing
- Dynamic template string construction with user data
