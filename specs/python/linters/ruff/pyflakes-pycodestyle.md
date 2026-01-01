# Ruff Linter - Complete Reference

Ruff is an extremely fast Python linter written in Rust. Implements 800+ rules from:
- Pyflakes (F)
- pycodestyle (E, W)
- isort (I)
- pep8-naming (N)
- pyupgrade (UP)
- flake8-bugbear (B)
- flake8-comprehensions (C4)
- flake8-simplify (SIM)
- pylint (PL)
- ruff-specific (RUF)

## Configuration

```toml
# pyproject.toml
[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes
    "I",      # isort
    "N",      # pep8-naming
    "UP",     # pyupgrade
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "SIM",    # flake8-simplify
    "PL",     # pylint
    "RUF",    # ruff-specific
    "PERF",   # performance
    "FURB",   # refurb
]
ignore = [
    "E501",   # line too long (if you want)
]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["S101"]  # allow assert in tests
"__init__.py" = ["F401"]  # allow unused imports

[tool.ruff.lint.isort]
known-first-party = ["mypackage"]
```

## Pyflakes (F) - Critical Errors

### F401: Module imported but unused

```python
# BAD
import os  # never used

# GOOD
import os
os.getcwd()

# Or explicit re-export
from .module import helper as helper  # noqa: F401
```

### F402: Import shadowed by loop variable

```python
# BAD
from os import path
for path in paths:  # shadows import!
    print(path)

# GOOD
from os import path
for p in paths:
    print(p)
```

### F403: `from module import *` used

```python
# BAD
from os import *

# GOOD
from os import path, getcwd
```

### F405: Name may be undefined from star import

```python
# BAD
from os import *
print(getcwd())  # undefined if * import fails

# GOOD
from os import getcwd
print(getcwd())
```

### F501-F509: Invalid format strings

```python
# F501: Invalid format string
"{".format()  # missing closing brace

# F502: Positional placeholder not needed
"{0}".format(x, y)  # y unused

# F504: % format unused argument
"%s" % (x, y)  # y unused

# F506: % format missing argument
"%s %s" % (x,)  # missing second arg
```

### F521: `.format` invalid format string

```python
# BAD
"{0} {2}".format(a, b)  # no {1}

# GOOD
"{0} {1}".format(a, b)
```

### F522: `.format` unused positional arguments

```python
# BAD
"{0}".format(a, b, c)  # b, c unused

# GOOD
"{0} {1} {2}".format(a, b, c)
```

### F523: `.format` unused keyword arguments

```python
# BAD
"{name}".format(name=x, unused=y)

# GOOD
"{name}".format(name=x)
```

### F601: Dictionary key literal duplicated

```python
# BAD
d = {"a": 1, "a": 2}  # duplicate key

# GOOD
d = {"a": 1, "b": 2}
```

### F631: Assert tuple (always true)

```python
# BAD
assert (condition, "message")  # always True!

# GOOD
assert condition, "message"
```

### F632: Use `==` to compare to string literal

```python
# BAD
if x is "hello":  # identity, not equality

# GOOD
if x == "hello":
```

### F811: Redefinition of unused name

```python
# BAD
def foo(): pass
def foo(): pass  # redefines

# GOOD
def foo_v1(): pass
def foo_v2(): pass
```

### F821: Undefined name

```python
# BAD
print(undefined_var)

# GOOD
undefined_var = "defined"
print(undefined_var)
```

### F823: Local variable referenced before assignment

```python
# BAD
def foo():
    print(x)  # referenced before assignment
    x = 1

# GOOD
def foo():
    x = 1
    print(x)
```

### F841: Local variable assigned but never used

```python
# BAD
def foo():
    x = compute()  # never used
    return 5

# GOOD
def foo():
    _ = compute()  # explicit ignore
    return 5
```

### F901: `raise NotImplemented` should be `NotImplementedError`

```python
# BAD
raise NotImplemented  # type, not exception

# GOOD
raise NotImplementedError
```

## pycodestyle (E/W) - Style

### E101: Indentation contains mixed spaces and tabs

### E111: Indentation is not a multiple of four

```python
# BAD
if True:
   x = 1  # 3 spaces

# GOOD
if True:
    x = 1  # 4 spaces
```

### E117: Over-indented

### E122-E131: Continuation line issues

### E201-E203: Whitespace issues

```python
# BAD
spam( ham[ 1 ], { eggs: 2 } )

# GOOD
spam(ham[1], {eggs: 2})
```

### E225-E228: Missing whitespace around operator

```python
# BAD
x=1
y = x+1

# GOOD
x = 1
y = x + 1
```

### E231: Missing whitespace after ','

```python
# BAD
func(a,b,c)

# GOOD
func(a, b, c)
```

### E251: Unexpected spaces around keyword / parameter equals

```python
# BAD
def foo(x = 1):
    pass

# GOOD
def foo(x=1):
    pass
```

### E262: Inline comment should start with '# '

```python
# BAD
x = 1  #comment

# GOOD
x = 1  # comment
```

### E265: Block comment should start with '# '

### E266: Too many leading '#' for block comment

### E302: Expected 2 blank lines, found N

### E303: Too many blank lines

### E304: Blank lines found after function decorator

### E305: Expected 2 blank lines after class or function definition

### E401: Multiple imports on one line

```python
# BAD
import os, sys

# GOOD
import os
import sys
```

### E402: Module level import not at top of file

### E501: Line too long

### E701-E704: Multiple statements on one line

```python
# BAD
if x: return True

# GOOD
if x:
    return True
```

### E711: Comparison to None

```python
# BAD
if x == None:
if x != None:

# GOOD
if x is None:
if x is not None:
```

### E712: Comparison to True/False

```python
# BAD
if x == True:
if x == False:

# GOOD
if x:
if not x:

# Exception: pandas/numpy boolean indexing
df[df["col"] == True]  # sometimes needed
```

### E713: Not in test

```python
# BAD
if not x in collection:

# GOOD
if x not in collection:
```

### E714: Not is test

```python
# BAD
if not x is None:

# GOOD
if x is not None:
```

### E721: Type comparison

```python
# BAD
if type(x) == int:

# GOOD
if isinstance(x, int):
```

### E722: Bare except

```python
# BAD
try:
    risky()
except:
    pass

# GOOD
try:
    risky()
except Exception:
    pass
```

### E731: Do not assign a lambda expression

```python
# BAD
f = lambda x: x + 1

# GOOD
def f(x):
    return x + 1
```

### E741: Ambiguous variable name

```python
# BAD
l = []  # looks like 1
O = 0   # looks like 0
I = 1   # looks like l

# GOOD
items = []
zero = 0
one = 1
```

### E902: Token error

### E999: Syntax error

### W291-W293: Trailing whitespace

### W391: Blank line at end of file

### W503: Line break before binary operator (ignored by default)

### W504: Line break after binary operator

### W505: Doc line too long
