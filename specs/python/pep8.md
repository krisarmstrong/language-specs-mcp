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
