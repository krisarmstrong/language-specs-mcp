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
