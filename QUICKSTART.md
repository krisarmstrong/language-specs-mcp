# SpecForge MCP - Quick Start Guide

Get LLMs to write better code in 5 minutes.

## What This Is

SpecForge MCP provides language specifications, best practices, and generation checklists to LLMs through the Model Context Protocol. The result: LLMs generate code that follows actual language standards and lint rules, not just "code that works."

## For LLM Users (Claude, ChatGPT, etc.)

### Instant Better Code

Before writing code, ask the LLM to check the generation checklist:

```
Before writing this Python code, check the SpecForge generation checklist.
```

This gives the LLM concentrated best practices to follow.

### Available Commands

| Command | What It Does |
|---------|--------------|
| `get_checklist(language)` | Critical rules to follow BEFORE writing code |
| `get_spec(language)` | Full language specification |
| `get_linter_rule(language, rule)` | Specific linter rule explanation |
| `search_specs(language, query)` | Search for specific topics |

### Example Usage

```
User: Write a Python function to read a config file

LLM: [Calls get_checklist("python") first]
     Then writes code using:
     - pathlib instead of os.path
     - context managers for file handling
     - proper exception handling (not bare except)
     - type hints
```

## For Developers

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/specforge-mcp.git
cd specforge-mcp

# Install dependencies
npm install

# Build
npm run build
```

### Configure with Claude Desktop

Add to `~/.config/claude/claude_desktop_config.json` (Linux/Mac) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "specforge": {
      "command": "node",
      "args": ["/path/to/specforge-mcp/dist/index.js"]
    }
  }
}
```

### Configure with Other MCP Clients

The server implements standard MCP. Point your client to:
- **Command**: `node`
- **Args**: `["/path/to/specforge-mcp/dist/index.js"]`

## What's Inside

### Generation Checklists (Layer 1)
Concentrated rules for each language. Read these BEFORE writing code.

```
specs/python/generation-checklist.md
specs/typescript/generation-checklist.md
specs/rust/generation-checklist.md
... (35 languages)
```

### Language Specifications (Layer 2)
Deep reference material when you need details.

```
specs/python/spec.md
specs/python/stdlib/overview.md
```

### Linter Rules (Layer 3)
Individual rule explanations with examples.

```
specs/python/linters/ruff/E101.md
specs/typescript/linters/eslint/no-unused-vars.md
```

## Supported Languages

Python, TypeScript, JavaScript, Go, Rust, Java, C, C++, C#, Ruby, PHP, Swift, Kotlin, Scala, Elixir, Clojure, Haskell, R, Julia, Dart, Lua, SQL, CSS, HTML, Markdown, YAML, Dockerfile, PowerShell, Git, Assembly, Basic, Batch, Zig, OCaml, Bash

## Key Features

| Feature | Benefit |
|---------|---------|
| **Generation Checklists** | 10-20 critical rules per language to prevent common bugs |
| **Linter Integration** | Rules from ESLint, Ruff, ShellCheck, Hadolint, etc. |
| **Current Versions** | Always up-to-date language/tool versions |
| **Security Focus** | Security anti-patterns called out explicitly |

## Example: The Difference

### Without SpecForge
```python
# LLM generates "working" code with issues:
# - No context manager (resource leak)
# - Using dangerous dynamic code execution
# - No type hints
def read_config(path):
    f = open(path)
    data = f.read()
    f.close()
    return parse_unsafe(data)  # Security risk!
```

### With SpecForge
```python
# LLM generates quality code
from pathlib import Path
import json

def read_config(path: Path) -> dict:
    """Read JSON config file."""
    with path.open() as f:
        return json.load(f)
```

## Updating Specs

```bash
# Fetch latest versions
npm run refresh

# Validate all specs
npm run validate
```

## Troubleshooting

### Server Not Responding
1. Check the path in your config is correct
2. Ensure `npm run build` completed successfully
3. Check server logs for errors

### Missing Language
Some languages have partial support. Check `specs/<language>/` for available content.

### Outdated Information
Run `npm run refresh` to update to latest versions.

## Contributing

1. Fork the repository
2. Add/update specs in `specs/<language>/`
3. Run `npm run validate`
4. Submit a pull request

## Next Steps

1. **LLM Users**: Start asking your LLM to "check the SpecForge checklist before writing code"
2. **Developers**: Configure the MCP server with your preferred client
3. **Contributors**: Check the issues for areas needing improvement

---

**Questions?** Open an issue at [github.com/your-org/specforge-mcp/issues](https://github.com/your-org/specforge-mcp/issues)
