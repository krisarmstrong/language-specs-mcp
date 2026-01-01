#!/bin/bash
# Fetch Rust reference, stdlib, and linters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/rust"

echo "=== Fetching Rust Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/modules,linters/clippy,formatters,patterns}

echo "Fetching Rust Reference..."
curl -sL "https://doc.rust-lang.org/reference/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Rust Reference\n\nSee: https://doc.rust-lang.org/reference/" > "$SPECS_DIR/spec.md"

echo "Fetching Rust standard library docs..."
curl -sL "https://doc.rust-lang.org/std/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# Rust Standard Library\n\nSee: https://doc.rust-lang.org/std/" > "$SPECS_DIR/stdlib/overview.md"

RUST_MODULES=$(curl -sL "https://doc.rust-lang.org/std/all.html" | \
  grep -oE 'std::[a-zA-Z0-9_]+' | sort -u)

for mod in $RUST_MODULES; do
  name="${mod#std::}"
  echo "  - rust/$name"
  echo "# ${mod}\n\nSee: https://doc.rust-lang.org/std/${name}/index.html" > "$SPECS_DIR/stdlib/modules/${name}.md"
done

echo "Fetching Clippy lints..."
curl -sL "https://rust-lang.github.io/rust-clippy/master/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/clippy/overview.md" 2>/dev/null || \
  echo "# Clippy Lints\n\nSee: https://rust-lang.github.io/rust-clippy/master/" > "$SPECS_DIR/linters/clippy/overview.md"

CLIPPY_LINTS=$(curl -sL "https://rust-lang.github.io/rust-clippy/master/" | \
  grep -oE 'href="#[a-z0-9_]+"' | \
  sed 's/href="#//;s/"//' | sort -u)

for lint in $CLIPPY_LINTS; do
  echo "  - clippy/$lint"
  echo "# $lint\n\nSee: https://rust-lang.github.io/rust-clippy/master/#${lint}" > "$SPECS_DIR/linters/clippy/${lint}.md"
done

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# Rust Idioms

## Prefer iterators over indexing

```rust
for item in items.iter() {
    // ...
}
```

## Use `Result` and `?` for error propagation

```rust
let data = read_to_string(path)?;
```

## Favor borrowing over cloning
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Rust Formatters

## rustfmt

See: https://github.com/rust-lang/rustfmt
EOF

cat > "$SPECS_DIR/formatters/rustfmt.md" << 'EOF'
# rustfmt Options

See: https://github.com/rust-lang/rustfmt/blob/master/Configurations.md
EOF

echo "=== Rust specs complete ==="
