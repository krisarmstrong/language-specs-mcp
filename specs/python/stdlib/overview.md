# Python Standard Library Quick Reference

## Essential Modules

| Module | Purpose |
|--------|---------|
| `pathlib` | File paths (use over os.path) |
| `json` | JSON encoding/decoding |
| `dataclasses` | Data containers |
| `typing` | Type hints |
| `collections` | Specialized containers |
| `itertools` | Iterator utilities |
| `functools` | Higher-order functions |
| `contextlib` | Context manager utilities |
| `asyncio` | Async I/O |
| `logging` | Logging facility |
| `re` | Regular expressions |
| `datetime` | Date and time |
| `enum` | Enumerations |
| `abc` | Abstract base classes |

## Type Hints (typing module)

```python
from typing import Any, TypeVar, Generic
from collections.abc import Callable, Iterator, Mapping

# Basic
x: int = 1
y: str | None = None
z: list[int] = [1, 2, 3]

# Callable
Handler = Callable[[Request], Response]

# Generic
T = TypeVar("T")

class Stack(Generic[T]):
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...
```

## Collections

```python
from collections import defaultdict, Counter, deque, namedtuple

# defaultdict - auto-initialize missing keys
counts = defaultdict(int)
counts["a"] += 1

# Counter - count occurrences
c = Counter("abracadabra")
c.most_common(3)  # [('a', 5), ('b', 2), ('r', 2)]

# deque - efficient double-ended queue
d = deque(maxlen=3)
d.append(1)
d.appendleft(0)

# namedtuple (prefer dataclass for new code)
Point = namedtuple("Point", ["x", "y"])
```
