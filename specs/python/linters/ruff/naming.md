# Ruff - pep8-naming Rules (N)

PEP 8 naming conventions.

## N801: Class name should use CapWords

```python
# BAD
class my_class:
    pass

class myClass:
    pass

# GOOD
class MyClass:
    pass
```

## N802: Function name should be lowercase

```python
# BAD
def MyFunction():
    pass

def myFunction():
    pass

# GOOD
def my_function():
    pass
```

## N803: Argument name should be lowercase

```python
# BAD
def foo(myArg):
    pass

# GOOD
def foo(my_arg):
    pass
```

## N804: First argument of classmethod should be 'cls'

```python
# BAD
class Foo:
    @classmethod
    def bar(self):
        pass

# GOOD
class Foo:
    @classmethod
    def bar(cls):
        pass
```

## N805: First argument of method should be 'self'

```python
# BAD
class Foo:
    def bar(this):
        pass

# GOOD
class Foo:
    def bar(self):
        pass
```

## N806: Variable in function should be lowercase

```python
# BAD
def foo():
    MyVar = 1
    return MyVar

# GOOD
def foo():
    my_var = 1
    return my_var
```

## N807: Function name should not start/end with '__'

```python
# BAD
def __my_function__():
    pass

# GOOD
def my_function():
    pass

# OK - dunder methods in classes
class Foo:
    def __init__(self):
        pass
```

## N811: Constant imported as non-constant

```python
# BAD
from math import PI as pi

# GOOD
from math import PI
# or
from math import PI as MY_PI
```

## N812: Lowercase imported as non-lowercase

```python
# BAD
from os import path as PATH

# GOOD
from os import path
```

## N813: CamelCase imported as lowercase

```python
# BAD
from typing import TypeVar as typevar

# GOOD
from typing import TypeVar
```

## N814: CamelCase imported as constant

```python
# BAD
from typing import TypeVar as TYPE_VAR

# GOOD
from typing import TypeVar
```

## N815: mixedCase variable in class scope

```python
# BAD
class Foo:
    myVar = 1

# GOOD
class Foo:
    my_var = 1
```

## N816: mixedCase variable in global scope

```python
# BAD
myGlobal = 1

# GOOD
my_global = 1
MY_CONSTANT = 1
```

## N817: CamelCase imported as acronym

```python
# BAD
from collections import OrderedDict as OD

# GOOD
from collections import OrderedDict
```

## N818: Exception name should end in Error

```python
# BAD
class MyException(Exception):
    pass

# GOOD
class MyError(Exception):
    pass

class ValidationError(Exception):
    pass
```

## N999: Invalid module name

```python
# BAD filename: MyModule.py, my-module.py

# GOOD filename: my_module.py
```
