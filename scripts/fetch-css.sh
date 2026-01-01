#!/bin/bash
# Fetch CSS specs, references, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/css"

echo "=== Fetching CSS Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters/stylelint,formatters,patterns}

echo "Fetching CSS Snapshot..."
curl -sL "https://www.w3.org/TR/css-2023/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# CSS Snapshot\n\nSee: https://www.w3.org/TR/css-2023/" > "$SPECS_DIR/spec.md"

echo "Fetching CSS reference..."
curl -sL "https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# CSS Reference\n\nSee: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching stylelint rules..."
curl -sL "https://stylelint.io/user-guide/rules" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/stylelint/overview.md" 2>/dev/null || \
  echo "# stylelint Rules\n\nSee: https://stylelint.io/user-guide/rules" > "$SPECS_DIR/linters/stylelint/overview.md"

STYLELINT_RULES=$(curl -sL "https://stylelint.io/user-guide/rules" | \
  grep -oE '/user-guide/rules/[a-z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for rule in $STYLELINT_RULES; do
  echo "  - stylelint/$rule"
  echo "# $rule\n\nSee: https://stylelint.io/user-guide/rules/${rule}" > "$SPECS_DIR/linters/stylelint/${rule}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# CSS Idioms

## Prefer modern layout

- Use Flexbox and Grid over floats.

## Use custom properties for theming

```css
:root { --brand-color: #0b5fff; }
.button { color: var(--brand-color); }
```

## Avoid overly specific selectors

Keep selectors short and maintainable.
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# CSS Formatters

## Prettier

See: https://prettier.io/docs/en/
EOF

cat > "$SPECS_DIR/formatters/prettier.md" << 'EOF'
# Prettier Options

See: https://prettier.io/docs/en/options.html
EOF

echo "=== CSS specs complete ==="
