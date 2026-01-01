# Ruff - pyupgrade Rules (UP)

Modernize Python code to newer syntax.

## UP001: Remove __metaclass__ = type

```python
# BAD (Python 2)
class Foo:
    __metaclass__ = type

# GOOD (Python 3)
class Foo:
    pass
```

## UP003: Use type(...) instead of type(...)

```python
# BAD
type("Foo", (object,), {})

# GOOD (if dynamic class needed)
type("Foo", (), {})
```

## UP004: Remove useless object inheritance

```python
# BAD
class Foo(object):
    pass

# GOOD
class Foo:
    pass
```

## UP005: Replace deprecated unittest aliases

```python
# BAD
self.assertEquals(a, b)
self.assertNotEquals(a, b)

# GOOD
self.assertEqual(a, b)
self.assertNotEqual(a, b)
```

## UP006: Use type instead of Type for builtin

```python
# BAD (Python 3.9+)
from typing import List, Dict, Tuple

def foo(x: List[int]) -> Dict[str, int]:
    pass

# GOOD
def foo(x: list[int]) -> dict[str, int]:
    pass
```

## UP007: Use X | Y instead of Union

```python
# BAD (Python 3.10+)
from typing import Union, Optional

def foo(x: Union[int, str]) -> Optional[str]:
    pass

# GOOD
def foo(x: int | str) -> str | None:
    pass
```

## UP008: Use super() without arguments

```python
# BAD
class Foo(Bar):
    def __init__(self):
        super(Foo, self).__init__()

# GOOD
class Foo(Bar):
    def __init__(self):
        super().__init__()
```

## UP009: UTF-8 encoding declaration is unnecessary

```python
# BAD (Python 3 default is UTF-8)
# -*- coding: utf-8 -*-

# GOOD - remove it
```

## UP010: Remove unnecessary __future__ imports

```python
# BAD (Python 3)
from __future__ import print_function
from __future__ import division

# GOOD - remove them (already default in Python 3)
```

## UP011: Remove unnecessary parentheses in class definition

```python
# BAD
class Foo():
    pass

# GOOD
class Foo:
    pass
```

## UP012: Use f-string instead of format

```python
# BAD
"Hello {}".format(name)
"Hello {name}".format(name=name)

# GOOD
f"Hello {name}"
```

## UP013: Use TypedDict class syntax

```python
# BAD
MyDict = TypedDict("MyDict", {"a": int, "b": str})

# GOOD
class MyDict(TypedDict):
    a: int
    b: str
```

## UP014: Use NamedTuple class syntax

```python
# BAD
Point = namedtuple("Point", ["x", "y"])

# GOOD
class Point(NamedTuple):
    x: int
    y: int
```

## UP015: Remove redundant open mode

```python
# BAD
open("file", "r")
open("file", mode="r")

# GOOD
open("file")
```

## UP017: Use datetime.UTC

```python
# BAD (Python 3.11+)
import datetime
datetime.timezone.utc

# GOOD
import datetime
datetime.UTC
```

## UP018: Remove native literal

```python
# BAD
str("hello")
int(42)
float(3.14)
bool(True)

# GOOD
"hello"
42
3.14
True
```

## UP024: Replace aliased error with original

```python
# BAD
try:
    pass
except IOError:  # alias for OSError
    pass

# GOOD
try:
    pass
except OSError:
    pass
```

## UP025: Remove unicode literal prefix

```python
# BAD (Python 3)
u"hello"
u'world'

# GOOD
"hello"
"world"
```

## UP026: Replace deprecated mock imports

```python
# BAD
from mock import Mock

# GOOD
from unittest.mock import Mock
```

## UP027: Unpack list comprehension

```python
# BAD
[*[x for x in items]]

# GOOD
[x for x in items]
```

## UP028: Use yield from

```python
# BAD
for item in iterable:
    yield item

# GOOD
yield from iterable
```

## UP029: Remove unnecessary default encoding

```python
# BAD
"hello".encode("utf-8")
b"hello".decode("utf-8")

# GOOD
"hello".encode()
b"hello".decode()
```

## UP030: Use implicit format spec

```python
# BAD
"{0}".format(value)
"{0:}".format(value)

# GOOD
"{}".format(value)
f"{value}"
```

## UP031: Use f-string instead of % formatting

```python
# BAD
"Hello %s" % name
"Hello %(name)s" % {"name": name}

# GOOD
f"Hello {name}"
```

## UP032: Use f-string instead of .format

```python
# BAD
"Hello {}".format(name)

# GOOD
f"Hello {name}"
```

## UP033: Use @functools.cache

```python
# BAD (Python 3.9+)
@functools.lru_cache(maxsize=None)
def expensive():
    pass

# GOOD
@functools.cache
def expensive():
    pass
```

## UP034: Use exponentiation operator

```python
# BAD
pow(2, 3)

# GOOD
2 ** 3
```

## UP035: Deprecated imports

```python
# BAD (Python 3.9+)
from typing import List, Dict, Tuple, Set

# GOOD - use builtins
list, dict, tuple, set

# BAD (Python 3.9+)
from typing import Callable, Iterable

# GOOD
from collections.abc import Callable, Iterable
```

## UP036: Remove version block for old Python

```python
# BAD
import sys
if sys.version_info >= (3, 0):
    pass  # we're on Python 3 anyway

# GOOD - remove version check
```

## UP037: Remove quotes from type annotation

```python
# BAD (with __future__ annotations)
def foo() -> "int":
    pass

# GOOD
def foo() -> int:
    pass
```

## UP038: Use X | Y in isinstance

```python
# BAD (Python 3.10+)
isinstance(x, (int, str))

# GOOD
isinstance(x, int | str)
```

## UP039: Unnecessary parentheses after class

```python
# BAD
class Foo(A, B,):

# GOOD
class Foo(A, B):
```

## UP040: Use TypeAlias for type aliases

```python
# BAD (Python 3.10+)
IntList = list[int]

# GOOD
IntList: TypeAlias = list[int]

# BETTER (Python 3.12+)
type IntList = list[int]
```

## UP041: Replace timeout classes

```python
# BAD (Python 3.11+)
asyncio.TimeoutError

# GOOD
TimeoutError
```

## UP043: Use root logging methods

```python
# BAD
logging.getLogger().warning("message")

# GOOD
logging.warning("message")
```
