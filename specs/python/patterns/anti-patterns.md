# Python Anti-Patterns

Common mistakes and code smells to avoid in Python code.

## Mutable Default Arguments

```python
# BAD - Mutable default is shared across calls
def add_item(item, items=[]):
    items.append(item)
    return items

result1 = add_item("a")  # ["a"]
result2 = add_item("b")  # ["a", "b"] - unexpected!

# GOOD - Use None as sentinel
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Bare Except Clauses

```python
# BAD - Catches SystemExit, KeyboardInterrupt
try:
    risky_operation()
except:
    pass

# ALSO BAD - Still too broad
try:
    risky_operation()
except Exception:
    pass

# GOOD - Catch specific exceptions
try:
    risky_operation()
except (ValueError, TypeError) as e:
    logger.error(f"Operation failed: {e}")
    raise
```

## Using `type()` for Type Checking

```python
# BAD - Doesn't handle inheritance
if type(obj) == list:
    process_list(obj)

# GOOD - Handles inheritance properly
if isinstance(obj, list):
    process_list(obj)

# BETTER - Use ABC for duck typing
from collections.abc import Sequence
if isinstance(obj, Sequence):
    process_sequence(obj)
```

## String Concatenation in Loops

```python
# BAD - O(n²) memory allocations
result = ""
for item in large_list:
    result += str(item) + ", "

# GOOD - O(n) with join
result = ", ".join(str(item) for item in large_list)
```

## Not Using Context Managers

```python
# BAD - Resource leak on exception
f = open("file.txt")
content = f.read()
f.close()  # Never reached if read() fails

# GOOD - Automatic cleanup
with open("file.txt") as f:
    content = f.read()
```

## Wildcard Imports

```python
# BAD - Pollutes namespace, hides dependencies
from os.path import *
from numpy import *

# GOOD - Explicit imports
from os.path import join, exists
import numpy as np
```

## Dynamic Code Execution with Untrusted Input

```python
# BAD - Security vulnerability (allows arbitrary code execution)
# Never pass untrusted input to dynamic evaluation functions
user_input = request.get("expression")
# DANGER: Don't do this!

# GOOD - Use ast.literal_eval for safe literal evaluation
import ast
data = ast.literal_eval("{'key': 'value'}")

# BETTER - Use proper parsing/serialization
import json
data = json.loads('{"key": "value"}')
```

## Mutable Class Attributes

```python
# BAD - Shared across all instances
class User:
    permissions = []  # Shared!

    def add_permission(self, perm):
        self.permissions.append(perm)

# GOOD - Instance attribute
class User:
    def __init__(self):
        self.permissions = []
```

## Using `is` for Value Comparison

```python
# BAD - Compares identity, not value
a = 1000
b = 1000
if a is b:  # May be False!
    print("equal")

# GOOD - Use == for value comparison
if a == b:
    print("equal")

# Note: Use `is` only for None, True, False
if value is None:
    pass
```

## Nested Try-Except

```python
# BAD - Hard to follow, hides errors
try:
    try:
        try:
            risky()
        except ValueError:
            pass
    except TypeError:
        pass
except RuntimeError:
    pass

# GOOD - Flat structure, specific handling
def safe_risky():
    try:
        risky()
    except (ValueError, TypeError, RuntimeError) as e:
        logger.error(f"Operation failed: {e}")
        return None
```

## Not Using Generators for Large Data

```python
# BAD - Loads entire file into memory
def read_lines(filename):
    with open(filename) as f:
        return f.readlines()  # Could be gigabytes

# GOOD - Generator yields line by line
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

## Boolean Comparison Anti-patterns

```python
# BAD
if condition == True:
    pass
if len(items) > 0:
    pass
if item != None:
    pass

# GOOD
if condition:
    pass
if items:
    pass
if item is not None:
    pass
```

## Global State

```python
# BAD - Hidden dependencies, hard to test
counter = 0

def increment():
    global counter
    counter += 1

# GOOD - Explicit state management
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
```

## Ignoring Return Values

```python
# BAD - Silent failures
my_list.sort()  # Returns None, modifies in place
sorted_list = my_list  # Still the same object!

# GOOD - Understand what's returned
sorted_list = sorted(my_list)  # Returns new list
# or
my_list.sort()  # Modify in place, don't assign
```

## Late Binding Closures

```python
# BAD - All functions reference final i value
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])  # [2, 2, 2]

# GOOD - Capture value with default argument
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)
print([f() for f in funcs])  # [0, 1, 2]
```

## Overusing Inheritance

```python
# BAD - Deep inheritance hierarchies
class Animal: pass
class Mammal(Animal): pass
class Canine(Mammal): pass
class Dog(Canine): pass
class GermanShepherd(Dog): pass

# GOOD - Favor composition
@dataclass
class Dog:
    breed: str
    behaviors: list[Behavior]
```
