# mypy Error Codes

## Type Errors

### arg-type

Argument has incompatible type.

```python
# BAD
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(42)  # error: Argument 1 has incompatible type "int"; expected "str"

# GOOD
greet("Alice")
```

### assignment

Incompatible assignment.

```python
# BAD
x: int = "hello"  # error: Incompatible types in assignment

# GOOD
x: int = 42
```

### call-arg

Too many/few arguments.

```python
# BAD
def foo(a: int, b: int) -> int:
    return a + b

foo(1)        # error: Missing positional argument "b"
foo(1, 2, 3)  # error: Too many arguments

# GOOD
foo(1, 2)
```

### call-overload

No matching overload.

```python
# BAD
from typing import overload

@overload
def process(x: int) -> int: ...
@overload
def process(x: str) -> str: ...

def process(x):
    return x

process([1, 2, 3])  # error: No overload variant matches

# GOOD
process(42)
process("hello")
```

### dict-item

Dict item has incompatible type.

```python
# BAD
d: dict[str, int] = {"a": "b"}  # error: Dict entry has incompatible type

# GOOD
d: dict[str, int] = {"a": 1}
```

### index

Invalid index type.

```python
# BAD
lst: list[int] = [1, 2, 3]
lst["0"]  # error: Invalid index type "str"

# GOOD
lst[0]
```

### list-item

List item has incompatible type.

```python
# BAD
lst: list[int] = [1, "two", 3]  # error: List item has incompatible type

# GOOD
lst: list[int] = [1, 2, 3]
```

### operator

Unsupported operand types.

```python
# BAD
"hello" + 42  # error: Unsupported operand types for + ("str" and "int")

# GOOD
"hello" + str(42)
```

### return

Incompatible return type.

```python
# BAD
def get_name() -> str:
    return 42  # error: Incompatible return value type

# GOOD
def get_name() -> str:
    return "Alice"
```

### return-value

Return value expected.

```python
# BAD
def get_value() -> int:
    print("no return")  # error: Missing return statement

# GOOD
def get_value() -> int:
    return 42
```

### type-arg

Invalid type argument.

```python
# BAD
from typing import TypeVar
T = TypeVar('T', bound=int)

def foo(x: T) -> T: ...

foo("hello")  # error: Value of type variable "T" cannot be "str"

# GOOD
foo(42)
```

### type-var

Invalid type variable usage.

```python
# BAD
from typing import TypeVar, Generic
T = TypeVar('T')

class Foo(Generic[T]):
    def bar(self) -> T:
        return "string"  # error: Incompatible return value

# GOOD
class Foo(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
    
    def bar(self) -> T:
        return self.value
```

### union-attr

Attribute not on all union members.

```python
# BAD
def process(x: int | str) -> None:
    x.upper()  # error: "int" has no attribute "upper"

# GOOD
def process(x: int | str) -> None:
    if isinstance(x, str):
        x.upper()
```

### var-annotated

Variable needs type annotation.

```python
# BAD (with --disallow-untyped-defs)
def foo():
    x = []  # error: Need type annotation for "x"
    return x

# GOOD
def foo() -> list[int]:
    x: list[int] = []
    return x
```

## Import Errors

### import

Cannot find module.

```python
# BAD
import nonexistent_module  # error: Cannot find implementation or library stub

# Fix: install the package or add type stubs
# Or ignore: import nonexistent_module  # type: ignore[import]
```

### import-untyped

Importing from untyped module.

```python
# BAD (with --disallow-untyped-imports)
from untyped_lib import something  # error: Module has no type annotations

# GOOD
from untyped_lib import something  # type: ignore[import-untyped]
# Or install type stubs: pip install types-untyped_lib
```

### no-redef

Name redefined.

```python
# BAD
def foo() -> int:
    return 1

def foo() -> str:  # error: Name "foo" already defined
    return "hello"

# GOOD - use overload
from typing import overload

@overload
def foo(x: int) -> int: ...
@overload
def foo(x: str) -> str: ...

def foo(x: int | str) -> int | str:
    return x
```

## Function Errors

### abstract

Abstract method not implemented.

```python
# BAD
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str: ...

class Dog(Animal):  # error: Cannot instantiate abstract class
    pass

# GOOD
class Dog(Animal):
    def speak(self) -> str:
        return "Woof"
```

### override

Invalid override.

```python
# BAD
class Base:
    def foo(self, x: int) -> int:
        return x

class Derived(Base):
    def foo(self, x: str) -> str:  # error: Signature incompatible with supertype
        return x

# GOOD
class Derived(Base):
    def foo(self, x: int) -> int:
        return x * 2
```

### no-untyped-def

Function missing type annotations.

```python
# BAD (with --disallow-untyped-defs)
def add(a, b):  # error: Function is missing type annotations
    return a + b

# GOOD
def add(a: int, b: int) -> int:
    return a + b
```

### no-untyped-call

Calling untyped function.

```python
# BAD (with --disallow-untyped-calls)
def untyped(x):
    return x

def typed(x: int) -> int:
    return untyped(x)  # error: Call to untyped function in typed context

# GOOD
def typed_untyped(x: int) -> int:
    return x

def typed(x: int) -> int:
    return typed_untyped(x)
```

## Class Errors

### attr-defined

Attribute not defined.

```python
# BAD
class Foo:
    def __init__(self) -> None:
        self.x = 1

foo = Foo()
print(foo.y)  # error: "Foo" has no attribute "y"

# GOOD
print(foo.x)
```

### has-type

Cannot determine type of attribute.

```python
# BAD
class Foo:
    x = None  # Cannot determine type

# GOOD
class Foo:
    x: int | None = None
```

### method-assign

Assigning to method.

```python
# BAD
class Foo:
    def bar(self) -> None: ...

foo = Foo()
foo.bar = lambda: None  # error: Cannot assign to a method

# GOOD - use different attribute name
foo.custom_bar = lambda: None
```

### misc

Miscellaneous errors.

```python
# Various errors that don't fit other categories
class Foo:
    __slots__ = ['x']
    y: int  # error: "y" not in __slots__
```

### name-defined

Name not defined.

```python
# BAD
print(undefined_var)  # error: Name "undefined_var" is not defined

# GOOD
undefined_var = "now defined"
print(undefined_var)
```

### safe-super

Unsafe super() call.

```python
# BAD
class Foo:
    @staticmethod
    def bar() -> None:
        super().baz()  # error: super() outside of method

# GOOD
class Foo:
    def bar(self) -> None:
        super().baz()
```

### valid-type

Invalid type.

```python
# BAD
x: "NonexistentType"  # error: Name "NonexistentType" is not defined

# GOOD
from typing import Any
x: Any  # or define the type
```

## Optional/None Errors

### truthy-bool

Suspicious boolean value.

```python
# BAD (with --strict-equality)
from typing import Sequence

def foo(x: Sequence[int]) -> None:
    if x:  # error: Sequence in boolean context
        print(x)

# GOOD - explicit check
def foo(x: Sequence[int]) -> None:
    if len(x) > 0:
        print(x)
```

### union-attr

Attribute error on union.

```python
# BAD
def process(x: str | None) -> int:
    return len(x)  # error: Item "None" has no attribute "__len__"

# GOOD
def process(x: str | None) -> int:
    if x is None:
        return 0
    return len(x)
```

### redundant-cast

Redundant cast.

```python
# BAD
from typing import cast
x: int = 5
y = cast(int, x)  # error: Redundant cast to "int"

# GOOD
y = x
```

### redundant-expr

Redundant expression.

```python
# BAD
x: int = 5
if isinstance(x, int):  # error: Redundant isinstance call
    pass

# Remove redundant check
```

### unreachable

Unreachable code.

```python
# BAD
def foo() -> int:
    return 1
    print("unreachable")  # error: Statement is unreachable

# GOOD
def foo() -> int:
    print("before return")
    return 1
```

## Literal/Enum Errors

### literal-required

Literal type required.

```python
# BAD
from typing import Literal

def foo(x: Literal["a", "b"]) -> None: ...

value = "a"  # type is str
foo(value)  # error: Argument has incompatible type "str"; expected "Literal['a', 'b']"

# GOOD
value: Literal["a", "b"] = "a"
foo(value)
```

### type-abstract

Cannot instantiate abstract type.

```python
# BAD
from typing import Protocol

class Printable(Protocol):
    def print(self) -> None: ...

x = Printable()  # error: Cannot instantiate protocol class

# GOOD
class Document:
    def print(self) -> None:
        print("Document")

x: Printable = Document()
```

## Strict Mode Errors

### strict-equality

Invalid equality comparison.

```python
# BAD (with --strict-equality)
x: int = 5
if x == "5":  # error: Non-overlapping equality check
    pass

# GOOD
if str(x) == "5":
    pass
```

### no-any-return

Returning Any.

```python
# BAD (with --warn-return-any)
from typing import Any

def foo() -> str:
    x: Any = get_value()
    return x  # error: Returning Any from function with declared return type "str"

# GOOD
def foo() -> str:
    x: Any = get_value()
    return str(x)
```

### no-any-expr

Expression has type Any.

```python
# BAD (with --disallow-any-expr)
from typing import Any
x: Any = 5
y = x + 1  # error: Expression has type "Any"

# GOOD
x: int = 5
y = x + 1
```
