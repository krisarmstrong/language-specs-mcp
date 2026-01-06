# SQLFluff Configuration

SQLFluff is an extensible and modular SQL linter and auto-formatter supporting 27+ dialects.

## Configuration File Formats

SQLFluff searches for configuration in this priority order:
1. `setup.cfg`
2. `tox.ini`
3. `pep8.ini`
4. `.sqlfluff`
5. `pyproject.toml`

The first four use INI-style formatting; `pyproject.toml` uses TOML syntax.

## Configuration File Locations

Configuration cascades from most general to most specific:
- SQLFluff package defaults
- User's OS-specific app config directory (`~/.config/sqlfluff` on macOS/Unix)
- User's home directory
- Directories between home and current working directory
- Current working directory
- Subdirectories toward the file being linted
- Directory containing the file being linted

Later files override earlier ones.

## Section Structure

**INI-style files (.sqlfluff, setup.cfg, etc.):**
```ini
[sqlfluff]
dialect = snowflake
templater = jinja
max_line_length = 120

[sqlfluff:indentation]
indented_joins = False

[sqlfluff:rules:capitalisation.keywords]
capitalisation_policy = upper
```

**pyproject.toml:**
```toml
[tool.sqlfluff.core]
dialect = "snowflake"
templater = "jinja"
max_line_length = 120

[tool.sqlfluff.indentation]
indented_joins = false

[tool.sqlfluff.rules.capitalisation.keywords]
capitalisation_policy = "upper"
```

## Core Settings

| Option | Description | Default |
|--------|-------------|---------|
| `dialect` | SQL dialect (ansi, bigquery, mysql, postgres, snowflake, etc.) | ansi |
| `templater` | Template engine (raw, jinja, python, placeholder, dbt) | jinja |
| `max_line_length` | Maximum line length | 80 |
| `exclude_rules` | Comma-separated rules to disable | - |
| `rules` | Comma-separated rules to enable (overrides exclude) | - |
| `processes` | Parallel processes (-1 for auto) | 1 |
| `large_file_skip_byte_limit` | Skip files larger than this | 0 (disabled) |

## Indentation Settings

```ini
[sqlfluff:indentation]
indent_unit = space
tab_space_size = 4
indented_joins = False
indented_ctes = False
indented_using_on = True
indented_on_contents = True
allow_implicit_indents = True
```

## Rule Configuration

Rules are configured under `[sqlfluff:rules]` with rule-specific subsections:

```ini
[sqlfluff:rules:capitalisation.keywords]
capitalisation_policy = consistent
# Options: consistent, upper, lower, capitalise

[sqlfluff:rules:capitalisation.identifiers]
extended_capitalisation_policy = consistent

[sqlfluff:rules:aliasing.table]
aliasing = explicit

[sqlfluff:rules:aliasing.column]
aliasing = explicit

[sqlfluff:rules:convention.select_trailing_comma]
select_clause_trailing_comma = forbid
```

## Layout Configuration

```ini
[sqlfluff:layout:type:comma]
spacing_before = touch
line_position = trailing

[sqlfluff:layout:type:binary_operator]
line_position = leading

[sqlfluff:layout:type:statement_terminator]
spacing_before = touch
line_position = trailing
```

## In-File Directives

Use SQL comments to apply configuration to individual files:

```sql
-- sqlfluff:dialect:postgres
-- sqlfluff:max_line_length:120
-- sqlfluff:rules:capitalisation.keywords:capitalisation_policy:upper
```

## Disabling Rules

**Disable for entire file:**
```sql
-- sqlfluff:noqa
SELECT * FROM table
```

**Disable specific rules:**
```sql
-- sqlfluff:noqa: LT01, LT02
SELECT * FROM table
```

**Disable for a range:**
```sql
-- sqlfluff:noqa:start
SELECT * FROM table
-- sqlfluff:noqa:end
```

**Disable inline:**
```sql
SELECT * FROM table  -- noqa: AM04
```

## .sqlfluffignore File

Exclude files using glob patterns:

```
# Ignore migrations
migrations/
**/migrations/*.sql

# Ignore generated files
*.generated.sql

# Ignore specific directories
test_data/
vendor/
```

## Templating Configuration

**Jinja templating:**
```ini
[sqlfluff:templater:jinja]
apply_dbt_builtins = True
library_path = sqlfluff_libs

[sqlfluff:templater:jinja:context]
my_variable = value
```

**Placeholder templating:**
```ini
[sqlfluff:templater:placeholder]
param_style = colon
# Options: colon (:name), numeric_colon (:1), pyformat (%(name)s),
#          dollar ($name), question (?), numeric_dollar ($1), percent (%s),
#          ampersand (&name)
```

## CLI Options

```bash
# Lint files
sqlfluff lint path/to/sql/

# Fix files automatically
sqlfluff fix path/to/sql/

# Parse and show structure
sqlfluff parse path/to/file.sql

# Show configuration
sqlfluff rules

# Specify dialect
sqlfluff lint --dialect postgres path/to/sql/
```

See: https://docs.sqlfluff.com/en/stable/configuration/index.html
