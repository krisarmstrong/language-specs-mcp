#!/bin/bash
# Fetch PowerShell references, stdlib, linters, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/powershell"

echo "=== Fetching PowerShell Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/cmdlets,linters/psscriptanalyzer,formatters,patterns}

echo "Fetching PowerShell language specification..."
curl -sL "https://learn.microsoft.com/en-us/powershell/scripting/lang-spec/chapter-01" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# PowerShell Language Specification\n\nSee: https://learn.microsoft.com/en-us/powershell/scripting/lang-spec/" > "$SPECS_DIR/spec.md"

echo "Fetching PowerShell cmdlet reference..."
curl -sL "https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# PowerShell Cmdlet Reference\n\nSee: https://learn.microsoft.com/en-us/powershell/scripting/" > "$SPECS_DIR/stdlib/overview.md"

CMDLET_INDEX=$(curl -sL "https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4" | \
  grep -oE '/powershell/module/[A-Za-z0-9_.-]+' | \
  sed 's#.*/##' | sort -u)

for mod in $CMDLET_INDEX; do
  echo "  - powershell/$mod"
  curl -sL "https://learn.microsoft.com/en-us/powershell/module/${mod}?view=powershell-7.4" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/cmdlets/${mod}.md" 2>/dev/null || \
    echo "# ${mod}\n\nSee: https://learn.microsoft.com/en-us/powershell/module/${mod}?view=powershell-7.4" > "$SPECS_DIR/stdlib/cmdlets/${mod}.md"
done

echo "Fetching PSScriptAnalyzer rules..."
curl -sL "https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/overview?view=ps-modules" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/psscriptanalyzer/overview.md" 2>/dev/null || \
  echo "# PSScriptAnalyzer\n\nSee: https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/overview" > "$SPECS_DIR/linters/psscriptanalyzer/overview.md"

curl -sL "https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/rules?view=ps-modules" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/psscriptanalyzer/rules.md" 2>/dev/null || \
  echo "# PSScriptAnalyzer Rules\n\nSee: https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/rules?view=ps-modules" > "$SPECS_DIR/linters/psscriptanalyzer/rules.md"

PSSA_RULES=$(curl -sL "https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/rules?view=ps-modules" | \
  grep -oE '/psscriptanalyzer/rules/[a-zA-Z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for rule in $PSSA_RULES; do
  echo "  - psscriptanalyzer/$rule"
  curl -sL "https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/${rule}?view=ps-modules" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/psscriptanalyzer/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/${rule}?view=ps-modules" > "$SPECS_DIR/linters/psscriptanalyzer/${rule}.md"
done

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# PowerShell Formatters

PowerShell has built-in formatting cmdlets, but no widely adopted code formatter.
EOF_FMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# PowerShell Idioms

## Prefer cmdlets over aliases

```powershell
Get-ChildItem
```

## Use splatting for readability

```powershell
$params = @{ Path = $path; Recurse = $true }
Get-ChildItem @params
```
EOF_PAT

echo "=== PowerShell specs complete ==="
