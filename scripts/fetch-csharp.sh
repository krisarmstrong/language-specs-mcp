#!/bin/bash
# Fetch C# language specification, stdlib, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/csharp"

echo "=== Fetching C# Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/namespaces,linters/{dotnet-analyzers,stylecop},formatters,patterns}

echo "Fetching C# language specification..."
curl -sL "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# C# Language Specification\n\nSee: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/" > "$SPECS_DIR/spec.md"

echo "Fetching .NET API reference..."
curl -sL "https://learn.microsoft.com/en-us/dotnet/api/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# .NET API Reference\n\nSee: https://learn.microsoft.com/en-us/dotnet/api/" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching .NET namespaces..."
DOTNET_NAMESPACES=$(curl -sL "https://learn.microsoft.com/en-us/dotnet/api/?view=net-8.0" | \
  grep -oE '/dotnet/api/[A-Za-z0-9_.]+' | \
  sed 's#.*/##' | sort -u)

for ns in $DOTNET_NAMESPACES; do
  echo "  - dotnet/$ns"
  curl -sL "https://learn.microsoft.com/en-us/dotnet/api/${ns}?view=net-8.0" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/namespaces/${ns}.md" 2>/dev/null || \
    echo "# ${ns}\n\nSee: https://learn.microsoft.com/en-us/dotnet/api/${ns}?view=net-8.0" > "$SPECS_DIR/stdlib/namespaces/${ns}.md"
done

echo "Fetching .NET analyzers overview..."
curl -sL "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/dotnet-analyzers/overview.md" 2>/dev/null || \
  echo "# .NET Code Analysis Overview\n\nSee: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview" > "$SPECS_DIR/linters/dotnet-analyzers/overview.md"

echo "Fetching .NET analyzer rules..."
curl -sL "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/dotnet-analyzers/quality-rules.md" 2>/dev/null || \
  echo "# .NET Quality Rules\n\nSee: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/" > "$SPECS_DIR/linters/dotnet-analyzers/quality-rules.md"

DOTNET_RULES=$(curl -sL "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/" | \
  grep -oE '/dotnet/fundamentals/code-analysis/quality-rules/ca[0-9]{4}' | \
  sed 's#.*/##' | sort -u)

for rule in $DOTNET_RULES; do
  echo "  - dotnet-analyzers/$rule"
  curl -sL "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/${rule}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/dotnet-analyzers/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/${rule}" > "$SPECS_DIR/linters/dotnet-analyzers/${rule}.md"
done

echo "Fetching StyleCop analyzers..."
curl -sL "https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/DOCUMENTATION.md" > \
  "$SPECS_DIR/linters/stylecop/overview.md" 2>/dev/null || \
  echo "# StyleCop Analyzers\n\nSee: https://github.com/DotNetAnalyzers/StyleCopAnalyzers" > "$SPECS_DIR/linters/stylecop/overview.md"

STYLECOP_RULES=$(curl -sL "https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/DOCUMENTATION.md" | \
  grep -oE 'SA[0-9]{4}\\.md' | \
  sed 's/\\.md$//' | sort -u)

for rule in $STYLECOP_RULES; do
  echo "  - stylecop/$rule"
  curl -sL "https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/documentation/${rule}.md" > \
    "$SPECS_DIR/linters/stylecop/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/master/documentation/${rule}.md" > "$SPECS_DIR/linters/stylecop/${rule}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# C# Idioms

## Use async/await for I/O

Prefer async APIs for network and disk operations.

## Prefer `using` declarations for disposal

```csharp
using var stream = File.OpenRead(path);
```

## Embrace nullable reference types

Enable nullable and use `string?` when values can be null.

## Use records for immutable data

```csharp
public record User(string Id, string Name);
```
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# C# Formatters

## dotnet format

See: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format
EOF

cat > "$SPECS_DIR/formatters/dotnet-format.md" << 'EOF'
# dotnet format Options

See: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format
EOF

echo "=== C# specs complete ==="
