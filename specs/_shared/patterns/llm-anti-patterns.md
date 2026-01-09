# LLM-Generated Code Anti-Patterns

**Common mistakes that LLMs make when generating code. Review this before accepting AI-generated code.**

## Cross-Language Anti-Patterns

### 1. Hallucinated APIs

LLMs frequently invent functions/methods that don't exist.

```python
# HALLUCINATED - These don't exist
import os
os.get_current_user()  # Not a real function
os.is_admin()          # Not a real function

# REAL APIs
import os
import getpass
getpass.getuser()      # Get current username
os.getuid() == 0       # Check if root (Unix)
```

```javascript
// HALLUCINATED
array.findLast(x => x > 5)  // Only in ES2023+
string.replaceAll(/pattern/)  // Needs 'g' flag

// CORRECT
array.reverse().find(x => x > 5)  // Pre-ES2023
string.replace(/pattern/g, '')    // With global flag
```

### 2. Outdated Patterns

LLMs trained on older code suggest deprecated approaches.

```python
# OUTDATED (Python 2 / early Python 3)
from typing import List, Dict, Optional
def process(items: List[str]) -> Dict[str, int]:

# MODERN (Python 3.9+)
def process(items: list[str]) -> dict[str, int]:
```

```javascript
// OUTDATED
var x = 5;
callback(function(err, data) {});

// MODERN
const x = 5;
const data = await asyncFunction();
```

### 3. Ignoring Error Handling

LLMs often generate "happy path" code without error handling.

```python
# LLM-GENERATED (no error handling)
def fetch_user(user_id):
    response = requests.get(f"/users/{user_id}")
    return response.json()["data"]

# PRODUCTION-READY
def fetch_user(user_id: int) -> User | None:
    try:
        response = requests.get(
            f"/users/{user_id}",
            timeout=10
        )
        response.raise_for_status()
        return User(**response.json()["data"])
    except requests.RequestException as e:
        logger.error(f"Failed to fetch user {user_id}: {e}")
        return None
    except (KeyError, ValidationError) as e:
        logger.error(f"Invalid response for user {user_id}: {e}")
        return None
```

### 4. SQL Injection Vulnerabilities

LLMs frequently generate injectable SQL.

```python
# VULNERABLE - LLM-generated
def get_user(username):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)

# SECURE - Parameterized
def get_user(username: str):
    cursor.execute(
        "SELECT * FROM users WHERE name = %s",
        (username,)
    )
```

```javascript
// VULNERABLE
const query = `SELECT * FROM users WHERE id = ${userId}`;

// SECURE
const query = 'SELECT * FROM users WHERE id = $1';
await pool.query(query, [userId]);
```

### 5. Hardcoded Secrets

LLMs include placeholder secrets that get committed.

```python
# DANGEROUS - LLM placeholder
API_KEY = "sk-your-api-key-here"
DATABASE_URL = "postgresql://user:password@localhost/db"

# CORRECT - Environment variables
import os
API_KEY = os.environ["API_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]
```

### 6. Missing Input Validation

```python
# VULNERABLE - No validation
@app.post("/users")
def create_user(data: dict):
    User.create(**data)  # Accepts anything

# SECURE - Validated
from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)

@app.post("/users")
def create_user(data: CreateUserRequest):
    User.create(**data.model_dump())
```

### 7. Race Conditions in Async Code

```python
# RACE CONDITION - Shared mutable state
counter = 0

async def increment():
    global counter
    temp = counter
    await asyncio.sleep(0.01)
    counter = temp + 1

# CORRECT - Use locks
counter = 0
lock = asyncio.Lock()

async def increment():
    global counter
    async with lock:
        counter += 1
```

### 8. Resource Leaks

```python
# LEAK - File never closed on exception
def read_config():
    f = open("config.json")
    data = json.load(f)
    f.close()
    return data

# CORRECT - Context manager
def read_config():
    with open("config.json") as f:
        return json.load(f)
```

```javascript
// LEAK - Connection never released
async function query(sql) {
    const client = await pool.connect();
    const result = await client.query(sql);
    return result.rows;
}

// CORRECT - Always release
async function query(sql) {
    const client = await pool.connect();
    try {
        const result = await client.query(sql);
        return result.rows;
    } finally {
        client.release();
    }
}
```

### 9. Insecure Randomness

```python
# INSECURE - Predictable for security use
import random
token = ''.join(random.choices('abcdef0123456789', k=32))

# SECURE - Cryptographic randomness
import secrets
token = secrets.token_hex(16)
```

### 10. Path Traversal Vulnerabilities

```python
# VULNERABLE
def read_file(filename):
    with open(f"uploads/{filename}") as f:
        return f.read()

# SECURE
from pathlib import Path

UPLOADS_DIR = Path("uploads").resolve()

def read_file(filename: str) -> str:
    path = (UPLOADS_DIR / filename).resolve()
    if not path.is_relative_to(UPLOADS_DIR):
        raise ValueError("Invalid path")
    return path.read_text()
```

## Language-Specific Anti-Patterns

### Python

| Anti-Pattern | LLM Code | Correct Code |
|--------------|----------|--------------|
| String formatting | `"Hello " + name` | `f"Hello {name}"` |
| List building | `result = []; for x in items: result.append(x)` | `result = [x for x in items]` |
| Dict get | `if key in d: return d[key]` | `return d.get(key)` |
| Boolean check | `if len(items) > 0:` | `if items:` |
| None check | `if x == None:` | `if x is None:` |

### JavaScript/TypeScript

| Anti-Pattern | LLM Code | Correct Code |
|--------------|----------|--------------|
| Equality | `if (x == y)` | `if (x === y)` |
| Undefined check | `if (x == undefined)` | `if (x === undefined)` or `if (x == null)` |
| Array check | `typeof arr === 'array'` | `Array.isArray(arr)` |
| Object clone | `const copy = obj` | `const copy = { ...obj }` |
| Async forEach | `arr.forEach(async (x) => {})` | `await Promise.all(arr.map(async (x) => {}))` |

### Go

| Anti-Pattern | LLM Code | Correct Code |
|--------------|----------|--------------|
| Error ignore | `result, _ := doSomething()` | `result, err := doSomething(); if err != nil { return err }` |
| Nil slice | `var s []string; s[0] = "x"` | `s := make([]string, 1); s[0] = "x"` |
| String concat | `s := ""; for _, x := range items { s += x }` | `var b strings.Builder; for _, x := range items { b.WriteString(x) }` |
| Goroutine leak | `go func() { <-ch }()` (channel never closes) | Always ensure channels close or use context |

### Rust

| Anti-Pattern | LLM Code | Correct Code |
|--------------|----------|--------------|
| Panic on error | `.unwrap()` | `.map_err(\|e\| ...)? ` or `?` |
| Clone abuse | `.clone()` everywhere | Borrow when possible |
| String building | `format!()` in loops | Use `String::with_capacity()` + `push_str()` |
| Mutex poison | `.lock().unwrap()` | Handle `PoisonError` or use `parking_lot` |

## Detection Checklist

Before accepting LLM-generated code, verify:

- [ ] All imported modules/functions actually exist
- [ ] Error handling covers failure cases
- [ ] No hardcoded secrets or credentials
- [ ] User input is validated and sanitized
- [ ] SQL queries are parameterized
- [ ] File paths are validated against traversal
- [ ] Resources (files, connections) are properly closed
- [ ] Async code handles concurrency correctly
- [ ] Security-sensitive operations use crypto-grade randomness
- [ ] Code follows current language idioms (not outdated patterns)
