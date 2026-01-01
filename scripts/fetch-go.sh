#!/bin/bash
# Fetch Go specs from authoritative sources

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/go"

echo "=== Fetching Go Specs ==="

# Create directories
mkdir -p "$SPECS_DIR"/{stdlib,linters/golangci-lint,formatters,patterns}

# Go Language Specification
echo "Fetching Go spec..."
if ! curl -sL "https://go.dev/ref/spec" | \
  sed -n '/<article/,/<\/article>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null; then
  if ! curl -sL "https://raw.githubusercontent.com/golang/go/master/doc/go_spec.html" > "$SPECS_DIR/spec.html" 2>/dev/null; then
    echo "# Go Language Specification\n\nSee: https://go.dev/ref/spec" > "$SPECS_DIR/spec.md"
  fi
fi

# Effective Go
echo "Fetching Effective Go..."
if ! curl -sL "https://go.dev/doc/effective_go" | \
  sed -n '/<article/,/<\/article>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/effective-go.md" 2>/dev/null; then
  if ! curl -sL "https://go.dev/doc/effective_go" > "$SPECS_DIR/effective-go.html" 2>/dev/null; then
    echo "# Effective Go\n\nSee: https://go.dev/doc/effective_go" > "$SPECS_DIR/effective-go.md"
  fi
fi

# Go Proverbs (idiomatic patterns)
cat > "$SPECS_DIR/patterns/proverbs.md" << 'EOF'
# Go Proverbs

By Rob Pike

- Don't communicate by sharing memory, share memory by communicating.
- Concurrency is not parallelism.
- Channels orchestrate; mutexes serialize.
- The bigger the interface, the weaker the abstraction.
- Make the zero value useful.
- interface{} says nothing.
- Gofmt's style is no one's favorite, yet gofmt is everyone's favorite.
- A little copying is better than a little dependency.
- Syscall must always be guarded with build tags.
- Cgo must always be guarded with build tags.
- Cgo is not Go.
- With the unsafe package there are no guarantees.
- Clear is better than clever.
- Reflection is never clear.
- Errors are values.
- Don't just check errors, handle them gracefully.
- Design the architecture, name the components, document the details.
- Documentation is for users.
- Don't panic.
EOF

# Go formatters
cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Go Formatters

## gofmt

See: https://pkg.go.dev/cmd/gofmt

## goimports

See: https://pkg.go.dev/golang.org/x/tools/cmd/goimports

## gofumpt

See: https://github.com/mvdan/gofumpt

## golines

See: https://github.com/segmentio/golines
EOF

cat > "$SPECS_DIR/formatters/gofmt.md" << 'EOF'
# gofmt Options

See: https://pkg.go.dev/cmd/gofmt
EOF

cat > "$SPECS_DIR/formatters/goimports.md" << 'EOF'
# goimports Options

See: https://pkg.go.dev/golang.org/x/tools/cmd/goimports
EOF

cat > "$SPECS_DIR/formatters/gofumpt.md" << 'EOF'
# gofumpt Options

See: https://github.com/mvdan/gofumpt
EOF

cat > "$SPECS_DIR/formatters/golines.md" << 'EOF'
# golines Options

See: https://github.com/segmentio/golines
EOF

# Error handling patterns
cat > "$SPECS_DIR/patterns/error-handling.md" << 'EOF'
# Go Error Handling Patterns

## Basic Pattern

```go
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doing something: %w", err)
}
```

## NEVER ignore errors

```go
// BAD - fails errcheck
result, _ := doSomething()

// GOOD
result, err := doSomething()
if err != nil {
    return err
}
```

## Error wrapping (Go 1.13+)

```go
// Wrap with context
if err != nil {
    return fmt.Errorf("failed to process %s: %w", name, err)
}

// Check wrapped errors
if errors.Is(err, os.ErrNotExist) {
    // handle not found
}

// Type assert wrapped errors
var pathErr *os.PathError
if errors.As(err, &pathErr) {
    // handle path error
}
```

## Sentinel errors

```go
// Define at package level
var ErrNotFound = errors.New("not found")

// Use errors.Is to check
if errors.Is(err, ErrNotFound) {
    // handle
}
```

## Custom error types

```go
type ValidationError struct {
    Field string
    Msg   string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Msg)
}
```
EOF

# Stdlib docs
echo "Fetching stdlib docs..."
if command -v go >/dev/null 2>&1; then
  STDLIB_PKGS=$(go list std 2>/dev/null || true)
else
  STDLIB_PKGS="fmt errors io os net/http encoding/json context sync time strings bytes"
fi

for pkg in $STDLIB_PKGS; do
  filename="${pkg//\//-}"
  echo "  - $pkg"
  go doc -all "$pkg" > "$SPECS_DIR/stdlib/$filename.md" 2>/dev/null || echo "    (skipped)"
done

# golangci-lint rules (from config, including disabled)
echo "Fetching golangci-lint rule docs..."
GOLANGCI_CONFIG_URL="https://raw.githubusercontent.com/maratori/golangci-lint-config/main/.golangci.yml"
GOLANGCI_CONFIG_PATH="$SCRIPT_DIR/../.golangci.yml"

if [ ! -f "$GOLANGCI_CONFIG_PATH" ]; then
  curl -sL "$GOLANGCI_CONFIG_URL" -o "$GOLANGCI_CONFIG_PATH" 2>/dev/null || true
fi

enabled_rules=()
optional_rules=()
disabled_rules=()
section="enabled"
in_linters=0
in_enable=0

while IFS= read -r line; do
  trimmed="${line#"${line%%[![:space:]]*}"}"

  if [[ $trimmed == "linters:" ]]; then
    in_linters=1
    continue
  fi
  if [[ $in_linters -eq 1 && $trimmed == "enable:" ]]; then
    in_enable=1
    continue
  fi
  if [[ $in_enable -eq 1 && $trimmed == "settings:" ]]; then
    break
  fi

  if [[ $in_enable -eq 1 ]]; then
    if [[ $trimmed =~ ^##[[:space:]]+you[[:space:]]+may[[:space:]]+want[[:space:]]+to[[:space:]]+enable ]]; then
      section="optional"
      continue
    fi
    if [[ $trimmed =~ ^##[[:space:]]+disabled ]]; then
      section="disabled"
      continue
    fi

    if [[ $trimmed =~ ^-[[:space:]]*([a-zA-Z0-9_-]+) ]]; then
      name="${BASH_REMATCH[1]}"
      if [[ $section == "enabled" ]]; then
        enabled_rules+=("$name")
      elif [[ $section == "optional" ]]; then
        optional_rules+=("$name")
      else
        disabled_rules+=("$name")
      fi
    elif [[ $trimmed =~ ^#-[[:space:]]*([a-zA-Z0-9_-]+) ]]; then
      name="${BASH_REMATCH[1]}"
      if [[ $section == "disabled" ]]; then
        disabled_rules+=("$name")
      else
        optional_rules+=("$name")
      fi
    fi
  fi
done < "$GOLANGCI_CONFIG_PATH"

all_rules="$(printf "%s\n" "${enabled_rules[@]}" "${optional_rules[@]}" "${disabled_rules[@]}" | sort -u)"
if ! printf "%s\n" "$all_rules" | grep -q "^embeddedstructfieldcheck$"; then
  all_rules=$(printf "%s\n%s\n" "$all_rules" "embeddedstructfieldcheck" | sort -u)
fi

for rule in $all_rules; do
  echo "  - $rule"
  curl -sL "https://golangci-lint.run/docs/linters/$rule/" | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/golangci-lint/$rule.md" 2>/dev/null || \
    echo "# $rule\n\nSee: https://golangci-lint.run/docs/linters/$rule/" > "$SPECS_DIR/linters/golangci-lint/$rule.md"
done

cat > "$SPECS_DIR/linters/golangci-lint/overview.md" << EOF
# golangci-lint Rules (from .golangci.yml)

Source: $GOLANGCI_CONFIG_URL

## Enabled
$(printf "%s\n" "${enabled_rules[@]}" | sort -u | sed 's/^/- /')

## Optional
$(printf "%s\n" "${optional_rules[@]}" | sort -u | sed 's/^/- /')

## Disabled
$(printf "%s\n" "${disabled_rules[@]}" | sort -u | sed 's/^/- /')
EOF

cat > "$SPECS_DIR/linters/golangci-lint/config.md" << EOF
# golangci-lint Config (.golangci.yml)

Source: $GOLANGCI_CONFIG_URL

\`\`\`yaml
$(cat "$GOLANGCI_CONFIG_PATH")
\`\`\`
EOF

echo "=== Go specs complete ==="
