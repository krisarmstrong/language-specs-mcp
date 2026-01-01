# mypy Overview

Static type checker for Python.

**Source:** https://mypy.readthedocs.io/

## Running

```bash
# Basic
mypy src/

# Strict mode
mypy --strict src/

# With config
mypy --config-file mypy.ini src/
```

## Configuration

`mypy.ini` or `pyproject.toml`:

```ini
[mypy]
python_version = 3.12
strict = true
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[mypy.plugins.numpy]
# numpy plugin settings

[mypy-some_untyped_module.*]
ignore_missing_imports = true
```

Or in `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
```

## Inline Type Ignores

```python
# Ignore specific error on line
x = problematic_call()  # type: ignore[arg-type]

# Ignore all errors on line
x = problematic_call()  # type: ignore

# Reveal type for debugging
reveal_type(x)  # mypy will print the inferred type
```

## Error Code Categories

| Category | Description |
|----------|-------------|
| import | Import-related errors |
| name | Name/attribute errors |
| call | Function call errors |
| arg-type | Argument type errors |
| return | Return type errors |
| assignment | Assignment errors |
| override | Method override errors |
| misc | Miscellaneous errors |
