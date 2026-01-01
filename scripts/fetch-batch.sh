#!/bin/bash
# Fetch Windows Batch (CMD) references, stdlib, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/batch"

echo "=== Fetching Batch Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters,formatters,patterns}

echo "Fetching CMD command reference..."
curl -sL "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Windows Command Reference\n\nSee: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands" > "$SPECS_DIR/spec.md"

cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF_STD'
# Windows CMD Built-in Commands

See: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
EOF_STD

cat > "$SPECS_DIR/linters/overview.md" << 'EOF_LINT'
# Batch Linting

There is no widely adopted modern linter for Windows Batch scripts.
EOF_LINT

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# Batch Formatters

No widely adopted formatter for Windows Batch scripts.
EOF_FMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# Batch Idioms

## Use SetLocal

```bat
@echo off
setlocal EnableExtensions EnableDelayedExpansion
```

## Quote paths

```bat
if exist "%~f0" echo Running
```

## Prefer CALL for subroutines

```bat
call :do_work
exit /b

:do_work
  echo Work
  exit /b
```
EOF_PAT

echo "=== Batch specs complete ==="
