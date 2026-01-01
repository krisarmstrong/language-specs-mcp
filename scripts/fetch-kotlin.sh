#!/bin/bash
# Fetch Kotlin spec, stdlib, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/kotlin"

echo "=== Fetching Kotlin Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/packages,linters/{detekt,ktlint},formatters,patterns}

echo "Fetching Kotlin specification..."
curl -sL "https://kotlinlang.org/spec/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Kotlin Language Specification\n\nSee: https://kotlinlang.org/spec/" > "$SPECS_DIR/spec.md"

echo "Fetching Kotlin stdlib reference..."
curl -sL "https://kotlinlang.org/api/latest/jvm/stdlib/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# Kotlin Standard Library\n\nSee: https://kotlinlang.org/api/latest/jvm/stdlib/" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching Kotlin package index..."
curl -sL "https://kotlinlang.org/api/latest/jvm/stdlib/allpackages-index.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/packages/index.md" 2>/dev/null || \
  echo "# Kotlin Packages\n\nSee: https://kotlinlang.org/api/latest/jvm/stdlib/allpackages-index.html" > "$SPECS_DIR/stdlib/packages/index.md"

KOTLIN_PACKAGES=$(curl -sL "https://kotlinlang.org/api/latest/jvm/stdlib/allpackages-index.html" | \
  grep -oE 'href=\"[a-zA-Z0-9_./-]+/package-summary.html\"' | \
  sed 's/href=\"//;s#/package-summary.html\"##' | sort -u)

for pkg in $KOTLIN_PACKAGES; do
  pkg_name=$(echo "$pkg" | sed 's#/#.#g')
  echo "  - kotlin/$pkg_name"
  curl -sL "https://kotlinlang.org/api/latest/jvm/stdlib/${pkg}/package-summary.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/packages/${pkg_name}.md" 2>/dev/null || \
    echo "# ${pkg_name}\n\nSee: https://kotlinlang.org/api/latest/jvm/stdlib/${pkg}/package-summary.html" > "$SPECS_DIR/stdlib/packages/${pkg_name}.md"
done

echo "Fetching detekt rules..."
curl -sL "https://detekt.dev/docs/rules/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/detekt/overview.md" 2>/dev/null || \
  echo "# detekt Rules\n\nSee: https://detekt.dev/docs/rules/" > "$SPECS_DIR/linters/detekt/overview.md"

DETEKT_RULESETS=$(curl -sL "https://detekt.dev/docs/rules/" | \
  grep -oE '/docs/rules/[a-zA-Z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for ruleset in $DETEKT_RULESETS; do
  echo "  - detekt/$ruleset"
  curl -sL "https://detekt.dev/docs/rules/${ruleset}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/detekt/${ruleset}.md" 2>/dev/null || \
    echo "# ${ruleset}\n\nSee: https://detekt.dev/docs/rules/${ruleset}" > "$SPECS_DIR/linters/detekt/${ruleset}.md"
done

echo "Fetching ktlint rules..."
curl -sL "https://pinterest.github.io/ktlint/latest/rules/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/ktlint/overview.md" 2>/dev/null || \
  echo "# ktlint Rules\n\nSee: https://pinterest.github.io/ktlint/latest/rules/" > "$SPECS_DIR/linters/ktlint/overview.md"

KTLINT_RULES=$(curl -sL "https://pinterest.github.io/ktlint/latest/rules/" | \
  grep -oE 'href="#[a-z0-9-]+"' | \
  sed 's/href="#//;s/"//' | sort -u)

for rule in $KTLINT_RULES; do
  echo "  - ktlint/$rule"
  echo "# $rule\n\nSee: https://pinterest.github.io/ktlint/latest/rules/#${rule}" > "$SPECS_DIR/linters/ktlint/${rule}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# Kotlin Idioms

## Prefer data classes for simple models

```kotlin
data class User(val id: String, val name: String)
```

## Use sealed classes for closed hierarchies

```kotlin
sealed interface Result
data class Success(val value: String) : Result
data class Failure(val error: Throwable) : Result
```

## Use `let`, `apply`, and `also` for scoped operations
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Kotlin Formatters

## ktlint

See: https://pinterest.github.io/ktlint/latest/rules/

## ktfmt

See: https://github.com/facebook/ktfmt
EOF

cat > "$SPECS_DIR/formatters/ktfmt.md" << 'EOF'
# ktfmt Options

See: https://github.com/facebook/ktfmt
EOF

echo "=== Kotlin specs complete ==="
