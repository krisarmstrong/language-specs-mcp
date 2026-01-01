#!/bin/bash
# Fetch Lua references, stdlib, linters, formatters, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/lua"

echo "=== Fetching Lua Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters/luacheck,formatters,patterns}

echo "Fetching Lua 5.4 manual..."
curl -sL "https://www.lua.org/manual/5.4/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Lua 5.4 Reference Manual\n\nSee: https://www.lua.org/manual/5.4/" > "$SPECS_DIR/spec.md"

echo "Fetching Lua standard libraries..."
curl -sL "https://www.lua.org/manual/5.4/manual.html#6" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# Lua Standard Libraries\n\nSee: https://www.lua.org/manual/5.4/manual.html#6" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching luacheck rules..."
curl -sL "https://luacheck.readthedocs.io/en/stable/warnings.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/luacheck/overview.md" 2>/dev/null || \
  echo "# luacheck Warnings\n\nSee: https://luacheck.readthedocs.io/en/stable/warnings.html" > "$SPECS_DIR/linters/luacheck/overview.md"

LUACHECK_CODES=$(curl -sL "https://luacheck.readthedocs.io/en/stable/warnings.html" | \
  grep -oE 'W[0-9]{3}' | sort -u)

for code in $LUACHECK_CODES; do
  echo "  - luacheck/$code"
  echo "# $code\n\nSee: https://luacheck.readthedocs.io/en/stable/warnings.html#${code}" > "$SPECS_DIR/linters/luacheck/${code}.md"
done

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# Lua Formatters

## stylua

See: https://github.com/JohnnyMorganz/StyLua
EOF_FMT

cat > "$SPECS_DIR/formatters/stylua.md" << 'EOF_FMT'
# stylua Options

See: https://github.com/JohnnyMorganz/StyLua#configuration
EOF_FMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# Lua Idioms

## Use local scope

```lua
local count = 0
```

## Prefer ipairs/pairs

```lua
for i, v in ipairs(items) do
  print(i, v)
end
```
EOF_PAT

echo "=== Lua specs complete ==="
