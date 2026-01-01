# Ruff - flake8-bugbear Rules (B)

Opinionated, bug-finding rules.

## B002: Use of `**=` for assignment

```python
# BAD
x =+ 1  # probably meant +=

# GOOD
x += 1
```

## B003: Assigning to os.environ doesn't clear

```python
# BAD
os.environ = {"PATH": "/bin"}  # doesn't work as expected

# GOOD
os.environ.clear()
os.environ.update({"PATH": "/bin"})
```

## B004: Using hasattr for __call__ is unreliable

```python
# BAD
if hasattr(obj, "__call__"):
    obj()

# GOOD
if callable(obj):
    obj()
```

## B005: Using .strip() with multi-char string

```python
# BAD
"hello".strip("he")  # strips each char, not substring

# GOOD
"hello".removeprefix("he")  # Python 3.9+
"hello".lstrip("h")
```

## B006: Mutable default argument

```python
# BAD - mutable default is shared!
def foo(items=[]):
    items.append(1)
    return items

foo()  # [1]
foo()  # [1, 1]  # same list!

# GOOD
def foo(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

## B007: Loop variable not used

```python
# BAD
for i in range(10):  # i not used
    print("hello")

# GOOD
for _ in range(10):
    print("hello")
```

## B008: Function call in default argument

```python
# BAD - called once at definition time
def foo(now=datetime.now()):
    return now

# GOOD - called each invocation
def foo(now=None):
    if now is None:
        now = datetime.now()
    return now
```

## B009: Do not call getattr with constant

```python
# BAD
getattr(obj, "foo")

# GOOD
obj.foo
```

## B010: Do not call setattr with constant

```python
# BAD
setattr(obj, "foo", value)

# GOOD
obj.foo = value
```

## B011: Do not assert False

```python
# BAD
assert False, "message"

# GOOD
raise AssertionError("message")
```

## B012: Return in finally

```python
# BAD - swallows exceptions
try:
    risky()
finally:
    return default  # exception lost!

# GOOD
try:
    return risky()
except Exception:
    return default
```

## B014: Redundant exception in except

```python
# BAD
except (ValueError, ValueError):  # duplicate

# GOOD
except ValueError:
```

## B015: Useless comparison

```python
# BAD
x == 5  # result discarded

# GOOD
result = x == 5
if x == 5:
    ...
```

## B016: Raise literal

```python
# BAD
raise "error"

# GOOD
raise ValueError("error")
```

## B017: assertRaises(Exception)

```python
# BAD - too broad
with pytest.raises(Exception):
    risky()

# GOOD
with pytest.raises(ValueError):
    risky()
```

## B018: Useless expression

```python
# BAD
"this does nothing"
42

# GOOD - remove or assign
# Unless it's a docstring
```

## B019: Use @functools.lru_cache with parentheses

```python
# BAD
@functools.lru_cache
def expensive():
    ...

# GOOD
@functools.lru_cache()
def expensive():
    ...
```

## B020: Loop variable shadows outer

```python
# BAD
items = [1, 2, 3]
for items in [[4], [5]]:  # shadows outer items
    print(items)

# GOOD
for batch in [[4], [5]]:
    print(batch)
```

## B023: Function in loop that uses loop variable

```python
# BAD - all functions use last value
funcs = []
for i in range(3):
    funcs.append(lambda: i)
# All return 2!

# GOOD - capture value
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)
```

## B024: Abstract class without abstract methods

```python
# BAD
from abc import ABC

class Foo(ABC):  # no abstract methods
    def bar(self):
        pass

# GOOD
from abc import ABC, abstractmethod

class Foo(ABC):
    @abstractmethod
    def bar(self):
        pass
```

## B025: try-except-pass

```python
# BAD
try:
    risky()
except Exception:
    pass

# GOOD - at least log
try:
    risky()
except Exception:
    logger.exception("Failed")
```

## B026: Star-argument unpacking after keyword argument

```python
# BAD
foo(a=1, *args)

# GOOD
foo(*args, a=1)
```

## B028: No explicit stacklevel in warnings.warn

```python
# BAD
warnings.warn("deprecated")

# GOOD
warnings.warn("deprecated", stacklevel=2)
```

## B029: except with empty tuple

```python
# BAD
except ():
    pass

# GOOD
except Exception:
    pass
```

## B030: except with non-exception type

```python
# BAD
except 42:
    pass

# GOOD
except ValueError:
    pass
```

## B031: Reusing groupby generator

```python
# BAD
for key, group in itertools.groupby(data, key_func):
    groups[key] = group  # group is consumed by next iteration!

# GOOD
for key, group in itertools.groupby(data, key_func):
    groups[key] = list(group)
```

## B032: Unintentional type annotation

```python
# BAD
x: int  # This is a type annotation with no value

# GOOD (if you meant annotation)
x: int = 0

# GOOD (if you meant type comment)
x = 0  # type: int
```

## B033: Duplicate set item

```python
# BAD
{1, 2, 1}  # duplicate

# GOOD
{1, 2}
```

## B034: re.sub/split without flags

```python
# BAD - might match different than expected
re.sub("pattern", repl, string, count)

# GOOD - explicit flags
re.sub("pattern", repl, string, count=count)
re.sub("pattern", repl, string, flags=re.IGNORECASE)
```

## B904: Raise without from in except handler

```python
# BAD - loses original traceback
except ValueError:
    raise RuntimeError("failed")

# GOOD
except ValueError as e:
    raise RuntimeError("failed") from e

# Or if intentionally suppressing
except ValueError:
    raise RuntimeError("failed") from None
```

## B905: zip without explicit strict

```python
# BAD
zip(a, b)  # silently truncates if different lengths

# GOOD (Python 3.10+)
zip(a, b, strict=True)
```
