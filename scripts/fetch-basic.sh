#!/bin/bash
# Fetch BASIC references, patterns, and tooling notes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/basic"

echo "=== Fetching BASIC Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters,formatters,patterns}

echo "Fetching QBasic reference..."
curl -sL "https://www.qbasic.net/en/reference/qbasic/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# BASIC Language Reference\n\nSee: https://www.qbasic.net/en/reference/qbasic/" > "$SPECS_DIR/spec.md"

cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF'
# BASIC Standard Library Reference

See: https://www.qbasic.net/en/reference/qbasic/
EOF

cat > "$SPECS_DIR/linters/overview.md" << 'EOF'
# BASIC Linting

There is no widely used, modern linter ecosystem for classic BASIC dialects.

## Recommendations

- Use compiler/interpreter warnings where available.
- Prefer structured programming constructs to avoid spaghetti control flow.
EOF

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# BASIC Idioms

## Prefer Structured Control Flow

- Use `IF...ELSE` and `SELECT CASE` over `GOTO`.
- Keep procedures short and single-purpose.

## Use Explicit Declarations

- Use `DIM` for clarity instead of relying on implicit typing.
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# BASIC Formatters

There is no widely adopted formatter for classic BASIC dialects.
EOF

echo "=== BASIC specs complete ==="
