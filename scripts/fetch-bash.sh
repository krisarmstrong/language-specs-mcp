#!/bin/bash
# Fetch Bash references, stdlib, linters, formatters, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/bash"

echo "=== Fetching Bash Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters/shellcheck,formatters,patterns}

echo "Fetching Bash reference manual..."
curl -sL "https://www.gnu.org/software/bash/manual/bash.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Bash Reference Manual\n\nSee: https://www.gnu.org/software/bash/manual/bash.html" > "$SPECS_DIR/spec.md"

echo "Fetching Bash builtins reference..."
curl -sL "https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/builtins.md" 2>/dev/null || \
  echo "# Bash Builtins\n\nSee: https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins" > "$SPECS_DIR/stdlib/builtins.md"

echo "Fetching Bash reserved words..."
curl -sL "https://www.gnu.org/software/bash/manual/bash.html#Reserved-Words" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/reserved-words.md" 2>/dev/null || \
  echo "# Bash Reserved Words\n\nSee: https://www.gnu.org/software/bash/manual/bash.html#Reserved-Words" > "$SPECS_DIR/stdlib/reserved-words.md"

cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF_STD'
# Bash Reference

See: https://www.gnu.org/software/bash/manual/bash.html
EOF_STD

echo "Fetching ShellCheck rules..."
curl -sL "https://www.shellcheck.net/wiki/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/shellcheck/overview.md" 2>/dev/null || \
  echo "# ShellCheck Rules\n\nSee: https://www.shellcheck.net/wiki/" > "$SPECS_DIR/linters/shellcheck/overview.md"

SHELLCHECK_RULES=$(curl -sL "https://www.shellcheck.net/wiki/" | \
  grep -oE 'SC[0-9]{4}' | sort -u)

for rule in $SHELLCHECK_RULES; do
  echo "  - shellcheck/$rule"
  echo "# $rule\n\nSee: https://www.shellcheck.net/wiki/$rule" > "$SPECS_DIR/linters/shellcheck/${rule}.md"
done

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# Bash Formatters

## shfmt

See: https://github.com/mvdan/sh
EOF_FMT

cat > "$SPECS_DIR/formatters/shfmt.md" << 'EOF_SHFMT'
# shfmt Options

See: https://github.com/mvdan/sh#shfmt
EOF_SHFMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# Bash Idioms

## Strict mode

```bash
set -euo pipefail
IFS=$'\n\t'
```

## Prefer [[ ]] tests

```bash
if [[ -f "$path" ]]; then
  echo "exists"
fi
```

## Quote variables

```bash
echo "$var"
```
EOF_PAT

echo "=== Bash specs complete ==="
