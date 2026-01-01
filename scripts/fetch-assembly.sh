#!/bin/bash
# Fetch x86-64 assembly references, patterns, and tooling notes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/assembly"

echo "=== Fetching Assembly Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters,formatters,patterns}

echo "Fetching x86-64 instruction reference..."
curl -sL "https://www.felixcloutier.com/x86/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/x86-64.md" 2>/dev/null || \
  echo "# x86-64 Instruction Set Reference\n\nSee: https://www.felixcloutier.com/x86/" > "$SPECS_DIR/x86-64.md"

echo "Fetching AArch64 (ARMv8-A) reference..."
curl -sL "https://developer.arm.com/documentation/ddi0487/latest" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/aarch64.md" 2>/dev/null || \
  echo "# AArch64 Architecture Reference Manual (ARMv8-A)\n\nSee: https://developer.arm.com/documentation/ddi0487/latest" > "$SPECS_DIR/aarch64.md"

echo "Fetching ARM32 (ARMv7-A) reference..."
curl -sL "https://developer.arm.com/documentation/ddi0406/latest" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/arm32.md" 2>/dev/null || \
  echo "# ARM Architecture Reference Manual (ARMv7-A)\n\nSee: https://developer.arm.com/documentation/ddi0406/latest" > "$SPECS_DIR/arm32.md"

echo "Fetching RISC-V specification..."
curl -sL "https://riscv.org/technical/specifications/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/riscv.md" 2>/dev/null || \
  echo "# RISC-V Specifications\n\nSee: https://riscv.org/technical/specifications/" > "$SPECS_DIR/riscv.md"

echo "Fetching WebAssembly core spec..."
curl -sL "https://webassembly.github.io/spec/core/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/wasm.md" 2>/dev/null || \
  echo "# WebAssembly Core Specification\n\nSee: https://webassembly.github.io/spec/core/" > "$SPECS_DIR/wasm.md"

cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF'
# Assembly ABI and Platform References

Assembly has no standard library, but ABI and calling convention references are essential.

## System V AMD64 ABI (Linux/macOS)

See: https://refspecs.linuxfoundation.org/elf/x86_64-abi-0.99.pdf

## Microsoft x64 Calling Convention

See: https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention
EOF

cat > "$SPECS_DIR/linters/overview.md" << 'EOF'
# Assembly Linting

There is no widely adopted, language-agnostic linter for assembly.

## Recommendations

- Enable strict warnings in your assembler (NASM/YASM/GAS/LLVM).
- Use disassemblers and static analysis tools for verification.
- Consider formatters like asmfmt for consistent style.
EOF

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# Assembly Idioms

## Follow the ABI

- Preserve callee-saved registers.
- Keep the stack aligned per ABI requirements.
- Use the correct calling convention for the platform.

## Prefer Clear Register Usage

- Minimize register aliasing.
- Use comments to document register roles in non-trivial routines.
EOF

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# Assembly Formatters

There is no widely adopted formatter for assembly across architectures.
EOF

echo "=== Assembly specs complete ==="
