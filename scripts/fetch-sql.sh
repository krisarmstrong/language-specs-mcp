#!/bin/bash
# Fetch SQL references, stdlib, linters, formatters, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/sql"

echo "=== Fetching SQL Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/{postgres,mysql,sqlite,sqlserver},linters/sqlfluff,formatters,patterns}

echo "Fetching SQL overview..."
cat > "$SPECS_DIR/spec.md" << 'EOF_STD'
# SQL Overview

The SQL standard is copyrighted; use vendor references for authoritative details.

- PostgreSQL: https://www.postgresql.org/docs/current/sql.html
- MySQL: https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html
- SQLite: https://www.sqlite.org/lang.html
- SQL Server (T-SQL): https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver16
EOF_STD

echo "Fetching PostgreSQL references..."
curl -sL "https://www.postgresql.org/docs/current/sql.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/postgres/commands.md" 2>/dev/null || \
  echo "# PostgreSQL SQL Commands\n\nSee: https://www.postgresql.org/docs/current/sql.html" > "$SPECS_DIR/stdlib/postgres/commands.md"

curl -sL "https://www.postgresql.org/docs/current/functions.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/postgres/functions.md" 2>/dev/null || \
  echo "# PostgreSQL Functions and Operators\n\nSee: https://www.postgresql.org/docs/current/functions.html" > "$SPECS_DIR/stdlib/postgres/functions.md"

echo "Fetching MySQL references..."
curl -sL "https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/mysql/commands.md" 2>/dev/null || \
  echo "# MySQL SQL Statements\n\nSee: https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html" > "$SPECS_DIR/stdlib/mysql/commands.md"

curl -sL "https://dev.mysql.com/doc/refman/8.0/en/functions.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/mysql/functions.md" 2>/dev/null || \
  echo "# MySQL Functions and Operators\n\nSee: https://dev.mysql.com/doc/refman/8.0/en/functions.html" > "$SPECS_DIR/stdlib/mysql/functions.md"

echo "Fetching SQLite references..."
curl -sL "https://www.sqlite.org/lang.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/sqlite/commands.md" 2>/dev/null || \
  echo "# SQLite SQL Language\n\nSee: https://www.sqlite.org/lang.html" > "$SPECS_DIR/stdlib/sqlite/commands.md"

curl -sL "https://www.sqlite.org/lang_corefunc.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/sqlite/functions-core.md" 2>/dev/null || \
  echo "# SQLite Core Functions\n\nSee: https://www.sqlite.org/lang_corefunc.html" > "$SPECS_DIR/stdlib/sqlite/functions-core.md"

curl -sL "https://www.sqlite.org/lang_aggfunc.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/sqlite/functions-aggregate.md" 2>/dev/null || \
  echo "# SQLite Aggregate Functions\n\nSee: https://www.sqlite.org/lang_aggfunc.html" > "$SPECS_DIR/stdlib/sqlite/functions-aggregate.md"

curl -sL "https://www.sqlite.org/lang_datefunc.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/sqlite/functions-date.md" 2>/dev/null || \
  echo "# SQLite Date and Time Functions\n\nSee: https://www.sqlite.org/lang_datefunc.html" > "$SPECS_DIR/stdlib/sqlite/functions-date.md"

echo "Fetching SQL Server references..."
curl -sL "https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver16" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/sqlserver/commands.md" 2>/dev/null || \
  echo "# SQL Server T-SQL Reference\n\nSee: https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver16" > "$SPECS_DIR/stdlib/sqlserver/commands.md"

curl -sL "https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/sqlserver/functions.md" 2>/dev/null || \
  echo "# SQL Server Functions\n\nSee: https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16" > "$SPECS_DIR/stdlib/sqlserver/functions.md"

echo "Fetching sqlfluff rules..."
curl -sL "https://docs.sqlfluff.com/en/stable/rules.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/sqlfluff/overview.md" 2>/dev/null || \
  echo "# sqlfluff Rules\n\nSee: https://docs.sqlfluff.com/en/stable/rules.html" > "$SPECS_DIR/linters/sqlfluff/overview.md"

SQLFLUFF_RULES=$(curl -sL "https://docs.sqlfluff.com/en/stable/rules.html" | \
  grep -oE 'rule-L[0-9]{3}' | sort -u)

for rule in $SQLFLUFF_RULES; do
  code="${rule#rule-}"
  echo "  - sqlfluff/$code"
  echo "# $code\n\nSee: https://docs.sqlfluff.com/en/stable/rules.html#${rule}" > "$SPECS_DIR/linters/sqlfluff/${code}.md"
done

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# SQL Formatters

## sqlfluff

See: https://docs.sqlfluff.com/en/stable/formatter.html
EOF_FMT

cat > "$SPECS_DIR/formatters/sqlfluff.md" << 'EOF_FMT'
# sqlfluff Formatter Options

See: https://docs.sqlfluff.com/en/stable/configuration.html
EOF_FMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# SQL Idioms

## Explicit column lists

```sql
SELECT id, name FROM users;
```

## Use parameterized queries

Avoid string concatenation for user input.
EOF_PAT

echo "=== SQL specs complete ==="
