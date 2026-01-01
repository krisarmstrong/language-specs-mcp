# Assembly Idioms

## Follow the ABI

- Preserve callee-saved registers.
- Keep the stack aligned per ABI requirements.
- Use the correct calling convention for the platform.

## Prefer Clear Register Usage

- Minimize register aliasing.
- Use comments to document register roles in non-trivial routines.
