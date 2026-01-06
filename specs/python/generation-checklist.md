# Python Generation Checklist

**Read this BEFORE writing Python code. These are the rules you WILL violate otherwise.**

## Critical: You Must Do These

### 1. Use `is None` not `== None`
```python
# BAD - can be overridden by __eq__
if x == None:

# GOOD - identity check, always correct
if x is None:
```

### 2. No Mutable Default Arguments
```python
# BAD - list is shared across all calls
def append_to(item, target=[]):
    target.append(item)
    return target

# GOOD - use None sentinel
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

### 3. No Bare Except Clauses
```python
# BAD - catches KeyboardInterrupt, SystemExit
try:
    risky()
except:
    pass

# GOOD - explicit exception type
try:
    risky()
except Exception as e:
    logger.error(e)
```

### 4. Use Context Managers for Resources
```python
# BAD - file may not close on exception
f = open("file.txt")
data = f.read()
f.close()

# GOOD - guaranteed cleanup
with open("file.txt") as f:
    data = f.read()
```

### 5. Use `pathlib` for File Paths
```python
# BAD - string manipulation, platform issues
path = os.path.join(base, "subdir", "file.txt")

# GOOD - modern, cross-platform
path = Path(base) / "subdir" / "file.txt"
```

## Important: Strong Recommendations

### 6. F-strings Over `.format()` or `%`
```python
# BAD - verbose, error-prone
msg = "Hello, %s!" % name
msg = "Hello, {}!".format(name)

# GOOD - readable, fast
msg = f"Hello, {name}!"
```

### 7. Use Type Hints on Public Functions
```python
# BAD - unclear interface
def process(data, timeout):
    ...

# GOOD - self-documenting
def process(data: dict[str, Any], timeout: float) -> bool:
    ...
```

### 8. Enumerate Instead of Range(len())
```python
# BAD - unpythonic
for i in range(len(items)):
    print(i, items[i])

# GOOD - pythonic
for i, item in enumerate(items):
    print(i, item)
```

### 9. Use List/Dict/Set Comprehensions
```python
# BAD - verbose loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# GOOD - comprehension
squares = [x ** 2 for x in range(10)]
```

### 10. Guard `if __name__ == "__main__"`
```python
# BAD - runs on import
do_stuff()

# GOOD - only runs when executed directly
if __name__ == "__main__":
    do_stuff()
```

## Security: Never Do These

### 11. Never Dynamically Evaluate User Input
Avoid functions that interpret strings as code (like dynamic evaluation).
Use `ast.literal_eval()` if you must parse literal data structures.
See: Bandit B307, S307

### 12. Never Build SQL with String Formatting
```python
# DANGEROUS - SQL injection
query = f"SELECT * FROM users WHERE id = {user_id}"

# SAFE - parameterized query
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### 13. Never Use `pickle` with Untrusted Data
```python
# DANGEROUS - arbitrary code can run
data = pickle.loads(untrusted_bytes)

# SAFE - use JSON for untrusted data
data = json.loads(untrusted_string)
```

## Style: Keep It Clean

### 14. Constants in UPPER_SNAKE_CASE
```python
# BAD
maxRetries = 3
MaxRetries = 3

# GOOD
MAX_RETRIES = 3
```

### 15. Classes in PascalCase, Functions in snake_case
```python
# BAD
class user_account:
    def GetBalance(self):
        ...

# GOOD
class UserAccount:
    def get_balance(self):
        ...
```

---

**Quick Reference - Copy This Mental Model:**
- `is None` not `== None`
- No mutable defaults
- Explicit exceptions
- Context managers for resources
- pathlib for paths
- f-strings for formatting
- Type hints on public APIs
- Never dynamically evaluate user input
- Always parameterize SQL
