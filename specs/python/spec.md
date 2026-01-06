# Python 3.14 Language Specification
Version: 3.14.0

Source: https://docs.python.org/3.14/


## Keywords

```python
False       await       else        import      pass
None        break       except      in          raise
True        class       finally     is          return
and         continue    for         lambda      try
as          def         from        nonlocal    while
assert      del         global      not         with
async       elif        if          or          yield
match       case        type        _
```

## Basic Types

### Numeric Types

```python
int         # arbitrary precision integer
float       # IEEE 754 double precision
complex     # complex number (3+4j)
bool        # True or False (subclass of int)
```

### Sequence Types

```python
str         # immutable text sequence
bytes       # immutable byte sequence
bytearray   # mutable byte sequence
list        # mutable sequence
tuple       # immutable sequence
range       # immutable sequence of numbers
```

### Set Types

```python
set         # mutable unordered collection of unique items
frozenset   # immutable set
```

### Mapping Types

```python
dict        # mutable key-value mapping
```

### None Type

```python
None        # singleton null value
```

## Type Annotations (PEP 484, 604)

### Basic Annotations

```python
x: int = 1
name: str = "hello"
values: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"a": 1}
```

### Optional and Union (3.10+)

```python
# Old style
from typing import Optional, Union
x: Optional[int] = None
y: Union[int, str] = 1

# New style (3.10+)
x: int | None = None
y: int | str = 1
```

### Callable

```python
from collections.abc import Callable

Handler = Callable[[int, str], bool]

def process(handler: Handler) -> None:
    result = handler(1, "hello")
```

### Generic Types

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
```

### Type Alias (3.12+)

```python
# Old style
IntList = list[int]

# New style (3.12+)
type IntList = list[int]
type Point = tuple[int, int]
```

## Functions

### Basic Functions

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Default arguments
def greet(name: str = "World") -> str:
    return f"Hello, {name}!"

# *args and **kwargs
def log(*args: object, **kwargs: object) -> None:
    print(*args, **kwargs)
```

### Lambda

```python
square = lambda x: x ** 2
add = lambda a, b: a + b
```

### Decorators

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logged
def process(data: str) -> None:
    pass
```

### Generators

```python
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

# Generator expression
squares = (x ** 2 for x in range(10))
```

## Classes

### Basic Class

```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
```

### Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

@dataclass
class Config:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False
```

### Inheritance

```python
class Animal:
    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

# Multiple inheritance
class Flying:
    def fly(self) -> None:
        pass

class Bird(Animal, Flying):
    def speak(self) -> str:
        return "Chirp!"
```

### Properties

```python
class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self) -> float:
        return 3.14159 * self._radius ** 2
```

### Class Methods and Static Methods

```python
class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string: str) -> "Date":
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)
    
    @staticmethod
    def is_valid(year: int, month: int, day: int) -> bool:
        return 1 <= month <= 12 and 1 <= day <= 31
```

## Control Flow

### Match Statement (3.10+)

```python
match command:
    case "quit":
        return
    case "help":
        show_help()
    case ["move", direction]:
        move(direction)
    case {"action": action, "target": target}:
        perform(action, target)
    case _:
        print("Unknown command")

# With guards
match point:
    case Point(x, y) if x == y:
        print("On diagonal")
    case Point(x, y):
        print(f"At ({x}, {y})")
```

### Exception Handling

```python
try:
    result = risky_operation()
except ValueError as e:
    handle_value_error(e)
except (TypeError, KeyError) as e:
    handle_other(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
else:
    # Only runs if no exception
    process(result)
finally:
    # Always runs
    cleanup()
```

### Exception Groups (3.11+)

```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
except* ValueError as eg:
    for exc in eg.exceptions:
        handle(exc)
except* TypeError as eg:
    for exc in eg.exceptions:
        handle(exc)
```

## Context Managers

```python
# Using with statement
with open("file.txt") as f:
    content = f.read()

# Multiple context managers
with (
    open("input.txt") as infile,
    open("output.txt", "w") as outfile,
):
    outfile.write(infile.read())

# Custom context manager (class)
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        return False  # Don't suppress exceptions

# Custom context manager (decorator)
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")
```

## Async/Await

```python
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main() -> None:
    # Concurrent execution
    results = await asyncio.gather(
        fetch("https://example.com/1"),
        fetch("https://example.com/2"),
        fetch("https://example.com/3"),
    )
    
    # Task groups (3.11+)
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch(url1))
        task2 = tg.create_task(fetch(url2))
    # All tasks complete here

asyncio.run(main())
```

### Async Generators

```python
async def countdown(n: int):
    while n > 0:
        yield n
        await asyncio.sleep(1)
        n -= 1

async def main():
    async for i in countdown(5):
        print(i)
```

## Comprehensions

```python
# List comprehension
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dict comprehension
word_lengths = {word: len(word) for word in words}

# Set comprehension
unique_lengths = {len(word) for word in words}

# Generator expression
sum_squares = sum(x ** 2 for x in range(10))

# Nested comprehension
matrix = [[i * j for j in range(5)] for i in range(5)]
```

## Walrus Operator (3.8+)

```python
# Assignment expression
if (n := len(data)) > 10:
    print(f"Too long: {n}")

# In loops
while (line := file.readline()):
    process(line)

# In comprehensions
results = [y for x in data if (y := transform(x)) is not None]
```

## F-Strings

```python
name = "Alice"
age = 30

# Basic
print(f"Hello, {name}!")

# Expressions
print(f"Next year: {age + 1}")

# Formatting
print(f"Value: {value:.2f}")
print(f"Hex: {num:#x}")
print(f"Padded: {name:>10}")

# Debug (3.8+)
print(f"{name=}")  # prints: name='Alice'
print(f"{age=}")   # prints: age=30
```

## Structural Pattern Matching (3.10+)

```python
# Literal patterns
match status:
    case 200:
        return "OK"
    case 404:
        return "Not Found"
    case 500:
        return "Server Error"

# Class patterns
match event:
    case Click(x=x, y=y):
        handle_click(x, y)
    case KeyPress(key="q"):
        quit()

# Sequence patterns
match command:
    case ["move", *directions]:
        for d in directions:
            move(d)
    case ["quit"]:
        return

# Mapping patterns
match config:
    case {"debug": True, **rest}:
        enable_debug(rest)
    case {"host": host, "port": port}:
        connect(host, port)

# Guard patterns
match point:
    case Point(x, y) if x == y:
        print("On diagonal")
```
