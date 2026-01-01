# Ruff - Pylint Rules (PL)

Rules from Pylint implemented in Ruff.

## Convention (PLC)

### PLC0105: TypeVar name mismatch

```python
# BAD
T = TypeVar("U")  # name doesn't match

# GOOD
T = TypeVar("T")
```

### PLC0131: TypeAlias annotation in TypeVar

```python
# BAD
T: TypeAlias = TypeVar("T")

# GOOD
T = TypeVar("T")
type MyAlias = int  # 3.12+
```

### PLC0132: TypeVar name doesn't match assignment

```python
# BAD
MyType = TypeVar("T")

# GOOD
T = TypeVar("T")
MyTypeVar = TypeVar("MyTypeVar")
```

### PLC0205: Class __slots__ not iterable

```python
# BAD
class Foo:
    __slots__ = "x"  # should be iterable

# GOOD
class Foo:
    __slots__ = ("x",)
    # or
    __slots__ = ["x"]
```

### PLC0208: Iteration over set with modification

```python
# BAD
for item in items:
    items.add(new_item)  # modifying during iteration

# GOOD
for item in list(items):
    items.add(new_item)
```

### PLC0414: Useless import alias

```python
# BAD
import os as os
from sys import path as path

# GOOD
import os
from sys import path
```

### PLC0415: Import outside top level

```python
# BAD
def foo():
    import os  # should be at top

# GOOD
import os

def foo():
    os.getcwd()
```

### PLC2401: Non-ASCII name

```python
# BAD
名前 = "value"  # non-ASCII identifier

# GOOD
name = "value"
```

### PLC2801: Unnecessary dunder call

```python
# BAD
x.__add__(y)
x.__str__()

# GOOD
x + y
str(x)
```

### PLC3002: Unnecessary direct lambda call

```python
# BAD
(lambda: 42)()

# GOOD
42
```

## Error (PLE)

### PLE0100: __init__ returns non-None

```python
# BAD
class Foo:
    def __init__(self):
        return 42

# GOOD
class Foo:
    def __init__(self):
        self.value = 42
```

### PLE0101: return in __init__

```python
# BAD
class Foo:
    def __init__(self):
        return self  # should return None

# GOOD
class Foo:
    def __init__(self):
        pass
```

### PLE0116: continue in finally

```python
# BAD
try:
    pass
finally:
    continue  # undefined behavior

# GOOD
try:
    pass
finally:
    pass
continue
```

### PLE0117: nonlocal outside function

```python
# BAD
nonlocal x  # at module level

# GOOD
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
```

### PLE0118: Used before assignment in try

```python
# BAD
try:
    x = func()
except:
    pass
print(x)  # x might not be defined

# GOOD
x = None
try:
    x = func()
except:
    pass
if x is not None:
    print(x)
```

### PLE0237: Non-slot assignment

```python
# BAD
class Foo:
    __slots__ = ("x",)

f = Foo()
f.y = 1  # y not in slots

# GOOD
class Foo:
    __slots__ = ("x", "y")

f = Foo()
f.y = 1
```

### PLE0241: Duplicate base class

```python
# BAD
class Foo(Bar, Bar):  # duplicate
    pass

# GOOD
class Foo(Bar):
    pass
```

### PLE0302: Unexpected special method signature

```python
# BAD
class Foo:
    def __len__(self, x):  # __len__ takes no args
        return 0

# GOOD
class Foo:
    def __len__(self):
        return 0
```

### PLE0604: Invalid __all__ object

```python
# BAD
__all__ = (func,)  # should be strings

# GOOD
__all__ = ("func",)
```

### PLE0605: Invalid __all__ item

```python
# BAD
__all__ = [1, 2, 3]  # should be strings

# GOOD
__all__ = ["foo", "bar"]
```

### PLE1142: await outside async

```python
# BAD
def foo():
    await something()  # not async

# GOOD
async def foo():
    await something()
```

### PLE1205: Too many arguments for logging

```python
# BAD
logging.info("value: %s %s", value)  # missing argument

# GOOD
logging.info("value: %s", value)
```

### PLE1206: Not enough arguments for logging

```python
# BAD
logging.info("a: %s, b: %s", a)  # missing b

# GOOD
logging.info("a: %s, b: %s", a, b)
```

### PLE1307: Bad string format type

```python
# BAD
"%d" % "string"  # wants int

# GOOD
"%s" % "string"
"%d" % 42
```

### PLE1310: Bad str/bytes strip call

```python
# BAD
"hello".strip("helo")  # strips chars, not substring!

# GOOD
"hello".removeprefix("he")  # 3.9+
"hello".removesuffix("lo")
```

### PLE1507: Invalid envvar default

```python
# BAD
os.getenv("KEY", 123)  # default should be str

# GOOD
os.getenv("KEY", "default")
```

### PLE2502: Bidirectional control character

```python
# BAD - contains invisible unicode
# Trojan source attack
```

## Refactor (PLR)

### PLR0124: Comparison with self

```python
# BAD
if x == x:  # always True
    pass

# GOOD
if x is not None:
    pass
```

### PLR0133: Comparison of constants

```python
# BAD
if 1 == 1:
    pass

# GOOD
if True:
    pass
```

### PLR0206: Property with parameters

```python
# BAD
class Foo:
    @property
    def bar(self, x):  # property can't have params
        return x

# GOOD
class Foo:
    @property
    def bar(self):
        return self._bar
```

### PLR0402: Use from import

```python
# BAD
import os.path
os.path.join(...)

# GOOD
from os import path
path.join(...)

# Or
from os.path import join
join(...)
```

### PLR0904-0917: Complexity limits

- PLR0904: Too many public methods
- PLR0911: Too many return statements
- PLR0912: Too many branches
- PLR0913: Too many arguments
- PLR0914: Too many local variables
- PLR0915: Too many statements
- PLR0916: Too many boolean expressions
- PLR0917: Too many positional arguments

```python
# BAD - too complex
def foo(a, b, c, d, e, f, g, h):  # too many args
    if a:
        if b:
            if c:  # too many branches
                pass
```

### PLR1701: Repeated isinstance calls

```python
# BAD
isinstance(x, int) or isinstance(x, str)

# GOOD
isinstance(x, (int, str))
# Or 3.10+
isinstance(x, int | str)
```

### PLR1711: Useless return

```python
# BAD
def foo():
    return None  # implicit anyway

# GOOD
def foo():
    pass
```

### PLR1714: Repeated equality comparison

```python
# BAD
if x == 1 or x == 2 or x == 3:
    pass

# GOOD
if x in {1, 2, 3}:
    pass
```

### PLR1722: Use sys.exit()

```python
# BAD
exit()
quit()

# GOOD
import sys
sys.exit()
```

### PLR2004: Magic value in comparison

```python
# BAD
if age > 18:
    pass

# GOOD
ADULT_AGE = 18
if age > ADULT_AGE:
    pass
```

### PLR5501: Collapsible else-if

```python
# BAD
if a:
    pass
else:
    if b:
        pass

# GOOD
if a:
    pass
elif b:
    pass
```

## Warning (PLW)

### PLW0120: Useless else on loop

```python
# BAD
for x in items:
    if condition:
        break
else:  # only runs if no break
    pass  # empty else

# Remove empty else
for x in items:
    if condition:
        break
```

### PLW0127: Self-assignment

```python
# BAD
x = x

# Remove it
```

### PLW0128: Redeclared variable in assignment

```python
# BAD
x, x = 1, 2  # x assigned twice

# GOOD
x, y = 1, 2
```

### PLW0129: Assert on string literal

```python
# BAD
assert "always true"  # non-empty string is truthy

# GOOD
assert condition, "message"
```

### PLW0131: Named expression in except

```python
# BAD
try:
    pass
except (err := Exception):  # walrus in except
    pass

# GOOD
try:
    pass
except Exception as err:
    pass
```

### PLW0406: Import self

```python
# BAD (in module foo.py)
import foo  # importing itself

# Remove self-import
```

### PLW0602: Global without assignment

```python
# BAD
x = 1
def foo():
    global x  # x not assigned in function

# GOOD - remove global if not needed
def foo():
    print(x)  # reading is fine without global
```

### PLW0603: Global statement

```python
# BAD
def foo():
    global x
    x = 1

# GOOD - return value instead
def foo():
    return 1

x = foo()
```

### PLW0711: Binary op exception

```python
# BAD
except TypeError or ValueError:  # wrong!

# GOOD
except (TypeError, ValueError):
```

### PLW1508: Invalid envvar default

```python
# BAD
os.environ.get("KEY", None)  # None is already default

# GOOD
os.environ.get("KEY")
os.environ.get("KEY", "default")
```

### PLW1509: Subprocess popen preexec_fn

```python
# BAD - unsafe in multithreaded code
subprocess.Popen(cmd, preexec_fn=fn)

# GOOD - use start_new_session or other options
subprocess.Popen(cmd, start_new_session=True)
```

### PLW2901: Redefined loop name

```python
# BAD
for i in range(10):
    for i in range(5):  # shadows outer i
        pass

# GOOD
for i in range(10):
    for j in range(5):
        pass
```

### PLW3301: Nested min/max

```python
# BAD
min(1, min(2, 3))

# GOOD
min(1, 2, 3)
```
