#!/bin/bash
# Fetch Swift guide, stdlib, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/swift"

echo "=== Fetching Swift Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/modules,linters/swiftlint,formatters,patterns}

echo "Fetching The Swift Programming Language..."
curl -sL "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/" | \
  LC_ALL=C sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# The Swift Programming Language\n\nSee: https://docs.swift.org/swift-book/documentation/the-swift-programming-language/" > "$SPECS_DIR/spec.md"

echo "Fetching Swift standard library reference..."
curl -sL "https://developer.apple.com/documentation/swift/swift_standard_library" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# Swift Standard Library\n\nSee: https://developer.apple.com/documentation/swift/swift_standard_library" > "$SPECS_DIR/stdlib/overview.md"

SWIFT_MODULES=$(curl -sL "https://developer.apple.com/documentation/swift" | \
  grep -oE '/documentation/swift/[A-Za-z0-9_]+' | \
  sed 's#.*/##' | sort -u)

for mod in $SWIFT_MODULES; do
  echo "  - swift/$mod"
  curl -sL "https://developer.apple.com/documentation/swift/${mod}" | \
    LC_ALL=C sed -n '/<main/,/<\\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/modules/${mod}.md" 2>/dev/null || \
    echo "# ${mod}\n\nSee: https://developer.apple.com/documentation/swift/${mod}" > "$SPECS_DIR/stdlib/modules/${mod}.md"
done

echo "Fetching SwiftLint rule directory..."
curl -sL "https://realm.github.io/SwiftLint/rule-directory.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/swiftlint/overview.md" 2>/dev/null || \
  echo "# SwiftLint Rules\n\nSee: https://realm.github.io/SwiftLint/rule-directory.html" > "$SPECS_DIR/linters/swiftlint/overview.md"

SWIFTLINT_RULES=$(curl -sL "https://realm.github.io/SwiftLint/rule-directory.html" | \
  grep -oE 'href="#[a-zA-Z0-9_-]+"' | \
  sed 's/href="#//;s/"//' | sort -u)

for rule in $SWIFTLINT_RULES; do
  echo "  - swiftlint/$rule"
  echo "# $rule\n\nSee: https://realm.github.io/SwiftLint/rule-directory.html#${rule}" > "$SPECS_DIR/linters/swiftlint/${rule}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# Swift Idioms

## Prefer value types

Use structs by default; use classes when identity is required.

## Use optionals explicitly

```swift
let value: String?
```

## Favor protocol-oriented design
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Swift Formatters

## swift-format

See: https://github.com/apple/swift-format
EOF

cat > "$SPECS_DIR/formatters/swift-format.md" << 'EOF'
# swift-format Options

See: https://github.com/apple/swift-format/blob/main/Documentation/Configuration.md
EOF

echo "=== Swift specs complete ==="
