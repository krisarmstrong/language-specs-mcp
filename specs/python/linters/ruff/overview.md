# Ruff Linter Rules
Version: 0.14.10

Source: https://docs.astral.sh/ruff/rules/


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
| UP007 | Use `X | Y` instead of `Union` | Modernize |

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
