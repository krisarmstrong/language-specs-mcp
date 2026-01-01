# Ruff - Pyflakes Rules (F)

Pyflakes detects various errors in Python programs.

## F401: Module imported but unused

```python
# BAD
import os  # never used

# GOOD - remove unused import
# Or use __all__ to indicate public API
```

## F402: Import shadowed by loop variable

```python
# BAD
from os import path
for path in paths:  # shadows import
    print(path)

# GOOD
from os import path as os_path
for p in paths:
    print(p)
```

## F403: `from module import *` used

```python
# BAD
from os import *

# GOOD
from os import path, getcwd
```

## F405: Name may be undefined from star import

```python
# BAD
from os import *
getcwd()  # might not be defined

# GOOD
from os import getcwd
getcwd()
```

## F501-F509: Invalid printf-style format

```python
# BAD
"%s %s" % (one,)  # F507: not enough args
"%(a)s" % {"b": 1}  # F505: missing key

# GOOD
"%s" % (one,)
"%(a)s" % {"a": 1}
```

## F521-F525: Invalid .format() calls

```python
# BAD
"{} {}".format(1)  # F524: not enough args
"{0} {2}".format(1, 2)  # F525: missing index 1

# GOOD
"{} {}".format(1, 2)
"{0} {1}".format(1, 2)
```

## F601: Dictionary key literal repeated

```python
# BAD
{"a": 1, "a": 2}  # duplicate key

# GOOD
{"a": 1, "b": 2}
```

## F602: Dictionary key variable repeated

```python
# BAD
key = "a"
{key: 1, key: 2}

# GOOD
{key: 1, "other": 2}
```

## F621: Too many expressions in star-unpacking

```python
# BAD
a, *b, c, *d = values  # two starred expressions

# GOOD
a, *b, c = values
```

## F631: Assert test is a tuple (always True)

```python
# BAD
assert (condition, message)  # tuple is always truthy!

# GOOD
assert condition, message
```

## F632: Use == instead of is for comparison to literal

```python
# BAD
if x is "hello":  # string interning unreliable

# GOOD
if x == "hello":
```

## F633: Invalid print statement syntax (Python 2)

```python
# BAD
print "hello"  # Python 2 syntax

# GOOD
print("hello")
```

## F634: If test is a tuple (always True)

```python
# BAD
if (x, y):  # tuple is always truthy
    ...

# GOOD
if x and y:
    ...
```

## F701-F707: Syntax errors

```python
# F701: break outside loop
# F702: continue outside loop
# F704: yield outside function
# F706: return outside function
# F707: except: with other clauses
```

## F811: Redefinition of unused name

```python
# BAD
def foo():
    pass

def foo():  # shadows previous
    pass

# GOOD
def foo_v1():
    pass

def foo_v2():
    pass
```

## F821: Undefined name

```python
# BAD
print(undefined_variable)

# GOOD
defined_variable = 1
print(defined_variable)
```

## F822: Undefined name in __all__

```python
# BAD
__all__ = ["foo", "bar"]  # bar doesn't exist

# GOOD
def foo(): pass
def bar(): pass
__all__ = ["foo", "bar"]
```

## F823: Local variable referenced before assignment

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

## F841: Local variable assigned but never used

```python
# BAD
def foo():
    x = 1  # never used
    return 2

# GOOD
def foo():
    return 2

# Or underscore prefix for intentionally unused
def foo():
    _x = 1  # explicitly unused
    return 2
```

## F842: Local variable annotated but never used

```python
# BAD
def foo():
    x: int  # annotated but never used

# GOOD - remove it
```

## F901: raise NotImplemented should be NotImplementedError

```python
# BAD
raise NotImplemented

# GOOD
raise NotImplementedError
```
