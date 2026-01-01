#!/bin/bash
# Fetch Python 3.14 specs from authoritative sources

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/python"

echo "=== Fetching Python 3.14 Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/modules,linters/{ruff,pylint},formatters,patterns}

# Python language reference
echo "Fetching Python docs..."
PYTHON_VERSION="3.14"

# PEP 8 - Style Guide
cat > "$SPECS_DIR/pep8.md" << 'EOF'
# PEP 8 - Python Style Guide (Summary)

## Indentation

- Use 4 spaces per indentation level
- Never mix tabs and spaces

## Maximum Line Length

- Limit lines to 79 characters (code)
- Limit lines to 72 characters (docstrings/comments)
- Can extend to 99 for teams that agree

## Imports

```python
# Standard library
import os
import sys

# Third party
import numpy as np
import pandas as pd

# Local
from mypackage import mymodule
```

- One import per line
- Absolute imports preferred
- Avoid wildcard imports (`from x import *`)

## Whitespace

```python
# GOOD
spam(ham[1], {eggs: 2})
foo = (0,)
if x == 4: print(x, y); x, y = y, x

# BAD
spam( ham[ 1 ], { eggs: 2 } )
foo = (0, )
if x == 4 : print(x , y) ; x , y = y , x
```

## Naming Conventions

| Type | Convention |
|------|------------|
| Modules | `lowercase_with_underscores` |
| Classes | `CapWords` |
| Functions | `lowercase_with_underscores` |
| Variables | `lowercase_with_underscores` |
| Constants | `UPPERCASE_WITH_UNDERSCORES` |
| Private | `_single_leading_underscore` |
| "Mangled" | `__double_leading_underscore` |

## Type Hints (PEP 484)

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"

def process(items: list[int]) -> dict[str, int]:
    return {"count": len(items)}
```
EOF

# Modern Python patterns
cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# Python Idiomatic Patterns (3.10+)

## Type Hints (Always Use)

```python
# BAD
def process(data):
    return data.get("value")

# GOOD
def process(data: dict[str, Any]) -> str | None:
    return data.get("value")
```

## Match Statements (3.10+)

```python
def handle_response(response: Response) -> str:
    match response.status:
        case 200:
            return response.body
        case 404:
            raise NotFoundError()
        case 500:
            raise ServerError()
        case _:
            raise UnknownError(response.status)
```

## Dataclasses

```python
from dataclasses import dataclass

# BAD - boilerplate
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age})"

# GOOD
@dataclass
class User:
    name: str
    age: int
```

## Context Managers

```python
# File handling
with open("file.txt") as f:
    content = f.read()

# Multiple contexts
with (
    open("input.txt") as infile,
    open("output.txt", "w") as outfile,
):
    outfile.write(infile.read())

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")
```

## List/Dict/Set Comprehensions

```python
# List
squares = [x**2 for x in range(10)]

# Dict
counts = {word: len(word) for word in words}

# Set
unique_lengths = {len(word) for word in words}

# Generator (memory efficient)
squares_gen = (x**2 for x in range(10))
```

## Walrus Operator (3.8+)

```python
# Read until empty
while (line := file.readline()):
    process(line)

# Check and use
if (match := pattern.search(text)):
    print(match.group())
```

## f-strings (Always Use)

```python
# BAD
"Hello, " + name + "!"
"Hello, {}!".format(name)
"Hello, %s!" % name

# GOOD
f"Hello, {name}!"
f"Value: {value:.2f}"
f"Debug: {obj=}"  # Shows 'obj=<value>'
```

## Exception Handling

```python
# Specific exceptions
try:
    value = data["key"]
except KeyError:
    value = default

# Exception groups (3.11+)
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
except* ValueError as eg:
    for exc in eg.exceptions:
        handle(exc)
```

## Pathlib (Not os.path)

```python
# BAD
import os
path = os.path.join(base, "subdir", "file.txt")
if os.path.exists(path):
    with open(path) as f:
        pass

# GOOD
from pathlib import Path
path = Path(base) / "subdir" / "file.txt"
if path.exists():
    content = path.read_text()
```

## Enum

```python
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETE = auto()
    FAILED = auto()

def handle(status: Status) -> None:
    match status:
        case Status.PENDING:
            start()
        case Status.COMPLETE:
            cleanup()
```

## functools

```python
from functools import cache, lru_cache, partial

@cache  # Unbounded cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@lru_cache(maxsize=128)  # Bounded cache
def expensive(x: int) -> int:
    return compute(x)
```
EOF

# Python formatters
cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Python Formatters

## black

See: https://black.readthedocs.io/en/stable/

## ruff format

See: https://docs.astral.sh/ruff/formatter/
EOF

cat > "$SPECS_DIR/formatters/black.md" << 'EOF'
# black Options

See: https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html
EOF

cat > "$SPECS_DIR/formatters/ruff.md" << 'EOF'
# ruff format Options

See: https://docs.astral.sh/ruff/formatter/
EOF

# Ruff rules
cat > "$SPECS_DIR/linters/ruff/overview.md" << 'EOF'
# Ruff Linter Rules

Ruff implements rules from:
- Pyflakes (F)
- pycodestyle (E, W)
- isort (I)
- pep8-naming (N)
- pyupgrade (UP)
- flake8-* plugins
- pylint (PL)
- ruff-specific (RUF)

## Essential Rules

| Code | Rule | Fix |
|------|------|-----|
| F401 | Unused import | Remove |
| F841 | Unused variable | Remove or prefix with _ |
| E501 | Line too long | Break line |
| E711 | Comparison to None | Use `is None` |
| E712 | Comparison to True/False | Use truthiness |
| UP006 | Use `list` instead of `List` | Modernize |
| UP007 | Use `X \| Y` instead of `Union` | Modernize |

## Configuration

```toml
# pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "UP",  # pyupgrade
    "N",   # pep8-naming
    "RUF", # ruff-specific
]
ignore = ["E501"]  # if you want longer lines
```
EOF

RUFF_RULES=$(curl -sL "https://docs.astral.sh/ruff/rules/" | \
  grep -oE '/ruff/rules/[a-z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for rule in $RUFF_RULES; do
  echo "  - ruff/$rule"
  curl -sL "https://docs.astral.sh/ruff/rules/${rule}/" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/ruff/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://docs.astral.sh/ruff/rules/${rule}/" > "$SPECS_DIR/linters/ruff/${rule}.md"
done

echo "Fetching pylint messages..."
curl -sL "https://pylint.readthedocs.io/en/stable/user_guide/messages/index.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/pylint/overview.md" 2>/dev/null || \
  echo "# Pylint Messages\n\nSee: https://pylint.readthedocs.io/en/stable/user_guide/messages/index.html" > "$SPECS_DIR/linters/pylint/overview.md"

PYLINT_MESSAGES=$(curl -sL "https://pylint.readthedocs.io/en/stable/user_guide/messages/index.html" | \
  grep -oE '/user_guide/messages/[a-z0-9_-]+\\.html' | \
  sed 's#.*/##;s/\\.html$//' | sort -u)

for msg in $PYLINT_MESSAGES; do
  echo "  - pylint/$msg"
  curl -sL "https://pylint.readthedocs.io/en/stable/user_guide/messages/${msg}.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/pylint/${msg}.md" 2>/dev/null || \
    echo "# ${msg}\n\nSee: https://pylint.readthedocs.io/en/stable/user_guide/messages/${msg}.html" > "$SPECS_DIR/linters/pylint/${msg}.md"
done

# Standard library quick reference
cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF'
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
EOF

echo "Fetching Python stdlib modules..."
PY_STD_MODULES=$(curl -sL "https://docs.python.org/3/library/" | \
  grep -oE '/library/[a-zA-Z0-9_]+\\.html' | \
  sed 's#.*/##;s/\\.html$//' | sort -u)

for mod in $PY_STD_MODULES; do
  echo "  - python/$mod"
  curl -sL "https://docs.python.org/3/library/${mod}.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/modules/${mod}.md" 2>/dev/null || \
    echo "# ${mod}\n\nSee: https://docs.python.org/3/library/${mod}.html" > "$SPECS_DIR/stdlib/modules/${mod}.md"
done

echo "=== Python specs complete ==="
