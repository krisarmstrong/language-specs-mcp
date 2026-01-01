#!/bin/bash
# Fetch HTML specs, references, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/html"

echo "=== Fetching HTML Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters/html-validate,formatters,patterns}

echo "Fetching HTML Living Standard..."
curl -sL "https://html.spec.whatwg.org/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# HTML Living Standard\n\nSee: https://html.spec.whatwg.org/" > "$SPECS_DIR/spec.md"

echo "Fetching HTML element reference..."
curl -sL "https://developer.mozilla.org/en-US/docs/Web/HTML/Element" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# HTML Element Reference\n\nSee: https://developer.mozilla.org/en-US/docs/Web/HTML/Element" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching HTML-validate rules..."
curl -sL "https://html-validate.org/rules/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/html-validate/overview.md" 2>/dev/null || \
  echo "# HTML-validate Rules\n\nSee: https://html-validate.org/rules/" > "$SPECS_DIR/linters/html-validate/overview.md"

HTML_VALIDATE_RULES=$(curl -sL "https://html-validate.org/rules/" | \
  grep -oE '/rules/[a-z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for rule in $HTML_VALIDATE_RULES; do
  echo "  - html-validate/$rule"
  echo "# $rule\n\nSee: https://html-validate.org/rules/${rule}" > "$SPECS_DIR/linters/html-validate/${rule}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# HTML Idioms

## Use semantic elements

Prefer `header`, `main`, `nav`, `section`, `article`, and `footer`.

## Keep accessibility in mind

- Provide `alt` text for images.
- Ensure form controls have labels.
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# HTML Formatters

## Prettier

See: https://prettier.io/docs/en/
EOF

cat > "$SPECS_DIR/formatters/prettier.md" << 'EOF'
# Prettier Options

See: https://prettier.io/docs/en/options.html
EOF

echo "=== HTML specs complete ==="
