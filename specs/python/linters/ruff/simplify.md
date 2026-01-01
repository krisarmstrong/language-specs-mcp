# flake8-simplify (SIM) - Simplification

Makes code more readable by suggesting simpler alternatives.

## Boolean Simplifications

### SIM101: Use `any()` or `all()`

```python
# BAD
if a or b or c:
if a and b and c:

# Consider
if any([a, b, c]):
if all([a, b, c]):
```

### SIM102: Use single `if` instead of nested

```python
# BAD
if a:
    if b:
        do_something()

# GOOD
if a and b:
    do_something()
```

### SIM103: Return boolean directly

```python
# BAD
if condition:
    return True
return False

# GOOD
return condition

# BAD
if condition:
    return True
else:
    return False

# GOOD
return condition
```

### SIM105: Use `contextlib.suppress`

```python
# BAD
try:
    do_something()
except ValueError:
    pass

# GOOD
from contextlib import suppress
with suppress(ValueError):
    do_something()
```

### SIM107: Return from try with no finally

```python
# BAD
try:
    return do_something()
except:
    return default

# GOOD
try:
    result = do_something()
except:
    result = default
return result
```

### SIM108: Use ternary operator

```python
# BAD
if condition:
    x = a
else:
    x = b

# GOOD
x = a if condition else b
```

### SIM109: Use `in` for multiple comparisons

```python
# BAD
if x == a or x == b or x == c:

# GOOD
if x in (a, b, c):
```

### SIM110: Use `any()` with generator

```python
# BAD
for item in items:
    if condition(item):
        return True
return False

# GOOD
return any(condition(item) for item in items)
```

### SIM111: Use `all()` with generator

```python
# BAD
for item in items:
    if not condition(item):
        return False
return True

# GOOD
return all(condition(item) for item in items)
```

### SIM112: Use `os.environ.get` instead of `in` check

```python
# BAD
if "KEY" in os.environ:
    value = os.environ["KEY"]
else:
    value = default

# GOOD
value = os.environ.get("KEY", default)
```

### SIM114: Combine `if` branches with same body

```python
# BAD
if a:
    do_something()
elif b:
    do_something()

# GOOD
if a or b:
    do_something()
```

### SIM115: Use context manager for open

```python
# BAD
f = open("file.txt")
content = f.read()
f.close()

# GOOD
with open("file.txt") as f:
    content = f.read()
```

### SIM116: Use dict instead of if/elif chain

```python
# BAD
if key == "a":
    return 1
elif key == "b":
    return 2
elif key == "c":
    return 3

# GOOD
mapping = {"a": 1, "b": 2, "c": 3}
return mapping.get(key)
```

### SIM117: Use single `with` statement

```python
# BAD
with open("a") as a:
    with open("b") as b:
        pass

# GOOD
with open("a") as a, open("b") as b:
    pass
```

### SIM118: Use `key in dict` instead of `key in dict.keys()`

```python
# BAD
if key in d.keys():

# GOOD
if key in d:
```

## Expression Simplifications

### SIM201: Use `x != y` instead of `not x == y`

```python
# BAD
if not a == b:

# GOOD
if a != b:
```

### SIM202: Use `x == y` instead of `not x != y`

```python
# BAD
if not a != b:

# GOOD
if a == b:
```

### SIM208: Use `x` instead of `not not x`

```python
# BAD
if not not condition:

# GOOD
if condition:
```

### SIM210: Use `bool()` instead of `True if x else False`

```python
# BAD
result = True if x else False

# GOOD
result = bool(x)
```

### SIM211: Use `not x` instead of `False if x else True`

```python
# BAD
result = False if x else True

# GOOD
result = not x
```

### SIM212: Use `b if b else a` instead of `a if not b else b`

```python
# BAD
result = a if not b else b

# GOOD
result = b or a
```

### SIM220: Use `False` instead of `a and not a`

### SIM221: Use `True` instead of `a or not a`

### SIM222: Use `True` instead of `a or True`

### SIM223: Use `False` instead of `a and False`

## Statement Simplifications

### SIM300: Use Yoda conditions

```python
# BAD
if "hello" == x:

# GOOD
if x == "hello":
```

### SIM401: Use `dict.get` with default

```python
# BAD
if key in d:
    value = d[key]
else:
    value = default

# GOOD
value = d.get(key, default)
```

### SIM904: Assign `dict` items directly

```python
# BAD
d = {}
d["key1"] = value1
d["key2"] = value2

# GOOD
d = {
    "key1": value1,
    "key2": value2,
}
```

### SIM905: Split static string

```python
# BAD
"a,b,c".split(",")

# GOOD
["a", "b", "c"]
```

### SIM910: Use `dict.get(key)` instead of `dict.get(key, None)`

```python
# BAD
d.get("key", None)

# GOOD
d.get("key")
```

### SIM911: Use `zip()` instead of `zip(dict.keys(), dict.values())`

```python
# BAD
zip(d.keys(), d.values())

# GOOD
d.items()
```

## Configuration

```toml
[tool.ruff.lint]
select = ["SIM"]
```
