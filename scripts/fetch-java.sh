#!/bin/bash
# Fetch Java language spec, stdlib, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/java"

echo "=== Fetching Java Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/packages,linters/{error-prone,spotbugs,checkstyle},formatters,patterns}

echo "Fetching Java Language Specification (SE 21)..."
curl -sL "https://docs.oracle.com/javase/specs/jls/se21/html/jls-1.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Java Language Specification (SE 21)\n\nSee: https://docs.oracle.com/javase/specs/jls/se21/html/jls-1.html" > "$SPECS_DIR/spec.md"

echo "Fetching Java SE API reference..."
curl -sL "https://docs.oracle.com/en/java/javase/21/docs/api/index.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# Java SE API Reference\n\nSee: https://docs.oracle.com/en/java/javase/21/docs/api/index.html" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching Java package index..."
curl -sL "https://docs.oracle.com/en/java/javase/21/docs/api/allpackages-index.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/packages/index.md" 2>/dev/null || \
  echo "# Java Packages\n\nSee: https://docs.oracle.com/en/java/javase/21/docs/api/allpackages-index.html" > "$SPECS_DIR/stdlib/packages/index.md"

JAVA_PACKAGES=$(curl -sL "https://docs.oracle.com/en/java/javase/21/docs/api/allpackages-index.html" | \
  grep -oE 'href=\"[a-zA-Z0-9_./-]+/package-summary.html\"' | \
  sed 's/href=\"//;s#/package-summary.html\"##' | sort -u)

for pkg in $JAVA_PACKAGES; do
  pkg_name=$(echo "$pkg" | sed 's#/#.#g')
  echo "  - java/$pkg_name"
  curl -sL "https://docs.oracle.com/en/java/javase/21/docs/api/${pkg}/package-summary.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/packages/${pkg_name}.md" 2>/dev/null || \
    echo "# ${pkg_name}\n\nSee: https://docs.oracle.com/en/java/javase/21/docs/api/${pkg}/package-summary.html" > "$SPECS_DIR/stdlib/packages/${pkg_name}.md"
done

echo "Fetching Error Prone bug patterns..."
curl -sL "https://errorprone.info/bugpatterns" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/error-prone/overview.md" 2>/dev/null || \
  echo "# Error Prone Bug Patterns\n\nSee: https://errorprone.info/bugpatterns" > "$SPECS_DIR/linters/error-prone/overview.md"

ERRORPRONE_RULES=$(curl -sL "https://errorprone.info/bugpatterns" | \
  grep -oE '/bugpattern/[A-Za-z0-9_]+' | \
  sed 's#.*/##' | sort -u)

for rule in $ERRORPRONE_RULES; do
  echo "  - error-prone/$rule"
  curl -sL "https://errorprone.info/bugpattern/${rule}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/error-prone/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://errorprone.info/bugpattern/${rule}" > "$SPECS_DIR/linters/error-prone/${rule}.md"
done

echo "Fetching SpotBugs bug descriptions..."
curl -sL "https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/spotbugs/overview.md" 2>/dev/null || \
  echo "# SpotBugs Bug Descriptions\n\nSee: https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html" > "$SPECS_DIR/linters/spotbugs/overview.md"

echo "Fetching Checkstyle checks..."
curl -sL "https://checkstyle.sourceforge.io/checks.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/checkstyle/overview.md" 2>/dev/null || \
  echo "# Checkstyle Checks\n\nSee: https://checkstyle.sourceforge.io/checks.html" > "$SPECS_DIR/linters/checkstyle/overview.md"

CHECKSTYLE_RULES=$(curl -sL "https://checkstyle.sourceforge.io/checks.html" | \
  grep -oE 'checks/[a-zA-Z0-9_/-]+\\.html' | \
  sed 's#.*/##;s/\\.html$//' | sort -u)

for rule in $CHECKSTYLE_RULES; do
  echo "  - checkstyle/$rule"
  curl -sL "https://checkstyle.sourceforge.io/checks/${rule}.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/checkstyle/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://checkstyle.sourceforge.io/checks/${rule}.html" > "$SPECS_DIR/linters/checkstyle/${rule}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# Java Idioms

## Prefer try-with-resources

```java
try (var input = Files.newInputStream(path)) {
    // use input
}
```

## Use records for simple data carriers

```java
public record User(String id, String name) {}
```

## Prefer standard collections interfaces

Use `List`, `Set`, and `Map` in APIs instead of concrete types.
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Java Formatters

## google-java-format

See: https://github.com/google/google-java-format
EOF

cat > "$SPECS_DIR/formatters/google-java-format.md" << 'EOF'
# google-java-format Options

See: https://github.com/google/google-java-format
EOF

echo "=== Java specs complete ==="
