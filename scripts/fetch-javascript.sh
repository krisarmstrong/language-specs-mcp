#!/bin/bash
# Fetch JavaScript references, stdlib, linters, formatters, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/javascript"

echo "=== Fetching JavaScript Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/{node,web},linters/eslint,formatters,patterns}

echo "Fetching ECMAScript spec..."
curl -sL "https://tc39.es/ecma262/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# ECMAScript Language Specification\n\nSee: https://tc39.es/ecma262/" > "$SPECS_DIR/spec.md"

echo "Fetching JavaScript reference..."
curl -sL "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# JavaScript Reference\n\nSee: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching Web API overview..."
curl -sL "https://developer.mozilla.org/en-US/docs/Web/API" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/web/overview.md" 2>/dev/null || \
  echo "# Web API Reference\n\nSee: https://developer.mozilla.org/en-US/docs/Web/API" > "$SPECS_DIR/stdlib/web/overview.md"

WEB_APIS=$(curl -sL "https://developer.mozilla.org/en-US/docs/Web/API" | \
  grep -oE '/Web/API/[A-Za-z0-9_%-]+' | \
  sed 's#.*/##' | sort -u)

for api in $WEB_APIS; do
  echo "  - web/$api"
  curl -sL "https://developer.mozilla.org/en-US/docs/Web/API/${api}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/web/${api}.md" 2>/dev/null || \
    echo "# ${api}\n\nSee: https://developer.mozilla.org/en-US/docs/Web/API/${api}" > "$SPECS_DIR/stdlib/web/${api}.md"
done

echo "Fetching Node.js API index..."
curl -sL "https://nodejs.org/api/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/node/overview.md" 2>/dev/null || \
  echo "# Node.js API Reference\n\nSee: https://nodejs.org/api/" > "$SPECS_DIR/stdlib/node/overview.md"

NODE_MODULES=$(curl -sL "https://nodejs.org/api/" | \
  grep -oE 'href=\"[a-zA-Z0-9_-]+\\.html\"' | \
  sed 's/href=\"//;s/\\.html\"//' | sort -u)

for mod in $NODE_MODULES; do
  echo "  - node/$mod"
  curl -sL "https://nodejs.org/api/${mod}.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/node/${mod}.md" 2>/dev/null || \
    echo "# Node.js ${mod} Module\n\nSee: https://nodejs.org/api/${mod}.html" > "$SPECS_DIR/stdlib/node/${mod}.md"
done

echo "Fetching ESLint rules..."
curl -sL "https://eslint.org/docs/latest/rules/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/eslint/overview.md" 2>/dev/null || \
  echo "# ESLint Rules\n\nSee: https://eslint.org/docs/latest/rules/" > "$SPECS_DIR/linters/eslint/overview.md"

ESLINT_RULES=$(curl -sL "https://eslint.org/docs/latest/rules/" | \
  grep -oE '/docs/latest/rules/[a-zA-Z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for rule in $ESLINT_RULES; do
  echo "  - eslint/$rule"
  curl -sL "https://eslint.org/docs/latest/rules/${rule}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/eslint/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://eslint.org/docs/latest/rules/${rule}" > "$SPECS_DIR/linters/eslint/${rule}.md"
done

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# JavaScript Formatters

## Prettier

See: https://prettier.io/docs/en/

## Biome Format

See: https://biomejs.dev/formatter/
EOF_FMT

cat > "$SPECS_DIR/formatters/prettier.md" << 'EOF_FMT'
# Prettier Options

See: https://prettier.io/docs/en/options.html
EOF_FMT

cat > "$SPECS_DIR/formatters/biome.md" << 'EOF_FMT'
# Biome Formatter Options

See: https://biomejs.dev/formatter/
EOF_FMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# JavaScript Idioms

## Prefer const/let over var

```javascript
const id = "abc";
let count = 0;
```

## Use async/await for async control flow

```javascript
const data = await fetch(url).then((res) => res.json());
```

## Avoid implicit globals

```javascript
"use strict";
```
EOF_PAT

echo "=== JavaScript specs complete ==="
