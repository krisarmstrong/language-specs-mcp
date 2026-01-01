# Language Specs MCP Server

MCP server providing authoritative language specifications, style guides, and linter rule explanations.

**Purpose:** Give AI assistants access to authoritative sources instead of training data garbage.

## Supported Languages

| Language | Spec | Stdlib | Linters | Formatters | Patterns |
|----------|------|--------|---------|------------|----------|
| Assembly (x86-64, ARM, RISC-V, WASM) | ✅ | ✅ (ABI refs) | - | - | ✅ |
| BASIC | ✅ | ✅ | - | - | ✅ |
| Bash | ✅ | ✅ | shellcheck | shfmt | ✅ |
| Batch | ✅ | ✅ | - | - | ✅ |
| Go | ✅ | ✅ | golangci-lint | gofmt, goimports, gofumpt, golines | ✅ |
| C# | ✅ | ✅ (namespace pages) | .NET analyzers, StyleCop | dotnet format | ✅ |
| JavaScript | ✅ | ✅ (Node + Web APIs) | ESLint | Prettier, Biome | ✅ |
| TypeScript | ✅ | ✅ | Biome | Prettier, Biome | ✅ |
| C | ✅ | ✅ | clang-tidy, cppcheck | clang-format | ✅ |
| C++ | ✅ | ✅ | clang-tidy, cppcheck | clang-format | ✅ |
| CSS | ✅ | ✅ | stylelint | Prettier | ✅ |
| HTML | ✅ | ✅ | html-validate | Prettier | ✅ |
| Git | ✅ | ✅ | gitlint, commitlint | commitlint/commitizen | ✅ |
| Java | ✅ | ✅ (package pages) | Error Prone, SpotBugs, Checkstyle | google-java-format | ✅ |
| Kotlin | ✅ | ✅ (package pages) | detekt, ktlint | ktlint, ktfmt | ✅ |
| Lua | ✅ | ✅ | luacheck | stylua | ✅ |
| PowerShell | ✅ | ✅ | PSScriptAnalyzer | - | ✅ |
| Python | ✅ | ✅ (module pages) | Ruff, Pylint | black | ✅ |
| Rust | ✅ | ✅ (module pages) | clippy | rustfmt | ✅ |
| SQL | ✅ | ✅ (Postgres/MySQL/SQLite/SQL Server) | sqlfluff | sqlfluff | ✅ |
| Swift | ✅ | ✅ (module pages) | SwiftLint | swift-format | ✅ |

## Installation

```bash
cd /Users/krisarmstrong/Developer/_tools/language-specs-mcp

# Install dependencies
npm install

# Fetch all specs
npm run fetch:all

# Build
npm run build
```

## Fetching Specs

```bash
# All languages
npm run fetch:all

# Individual
npm run fetch:assembly
npm run fetch:basic
npm run fetch:bash
npm run fetch:batch
npm run fetch:go
npm run fetch:csharp
npm run fetch:git
npm run fetch:javascript
npm run fetch:typescript
npm run fetch:c
npm run fetch:cpp
npm run fetch:css
npm run fetch:html
npm run fetch:java
npm run fetch:kotlin
npm run fetch:lua
npm run fetch:powershell
npm run fetch:python
npm run fetch:rust
npm run fetch:sql
npm run fetch:swift
```

## Contributing

See `CONTRIBUTING.md` for source guidelines, fetch script conventions, and Git standards.

## Versioning

This project follows SemVer. See `VERSIONING.md`.

## Issue Tracking

Use the GitHub issue templates for bugs and feature requests.

## CI and Releases

- CI runs on every push and PR.
- Tag a release with `vX.Y.Z` to publish GitHub releases.

## Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "language-specs": {
      "command": "node",
      "args": ["/Users/krisarmstrong/Developer/_tools/language-specs-mcp/dist/index.js"]
    }
  }
}
```

## Claude Code Configuration

Add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "language-specs": {
      "command": "node",
      "args": ["/Users/krisarmstrong/Developer/_tools/language-specs-mcp/dist/index.js"]
    }
  }
}
```

## Available Tools

### get_spec

Get authoritative language specification or documentation.

```json
{
  "language": "go",
  "category": "patterns",
  "topic": "error-handling"
}
```

Formatter example:

```json
{
  "language": "python",
  "category": "formatters",
  "topic": "black"
}
```

## Linting

```bash
npm run lint
npm run lint:fix
```

## Commit Message Checks

```bash
npm run commitlint
```

### get_linter_rule

Get detailed explanation of a specific linter rule.

```json
{
  "language": "typescript",
  "linter": "biome",
  "rule": "noExplicitAny"
}
```

### search_specs

Search across all specs for a term.

```json
{
  "query": "error handling"
}
```

### list_available

List available specs for a language/category.

```json
{
  "language": "go",
  "category": "stdlib"
}
```

## Usage with LLMs and Editors

This server only helps if the client actually calls the tools. The most reliable approach is to add a short instruction telling the model to consult the MCP server before coding.

### Codex CLI

Add to your project prompt or instructions:

```
Before writing or modifying code, consult the `language-specs` MCP server.
Use `get_spec` for language/stdlib questions, `get_linter_rule` for lint guidance, and `search_specs` if unsure.
```

### Claude CLI

Add to your project prompt or instructions:

```
Always check `language-specs` before proposing code.
Prefer tool output over general knowledge.
```

### Claude Desktop

Add the MCP server config (see above), then include a short reminder in your system or project prompt to consult the server.

### VS Code (MCP-capable clients)

Depending on your client extension:

- Claude Code / Continue / other MCP-enabled tools: add the same instruction in the workspace or project prompt.
- If the client supports “always use tool” rules, set `language-specs` for spec/stdlib/lint queries.

Example prompt:

```
Use `language-specs` for all spec/stdlib/linter/formatter questions. If you are unsure, run `search_specs` first.
```

## Is This Worth It?

Yes, if tool usage is enforced. Without explicit instructions, most LLMs will not consistently call tools, so the benefit drops sharply. With a “spec-first” habit, this dramatically improves correctness and lint compliance.

## Directory Structure

```
specs/
├── go/
│   ├── spec.md              # Language specification
│   ├── effective-go.md      # Style guide
│   ├── stdlib/              # Package docs
│   │   ├── fmt.md
│   │   ├── errors.md
│   │   └── ...
│   ├── linters/
│   │   └── golangci-lint/
│   │       ├── errcheck.md
│   │       └── ...
│   └── patterns/
│       ├── error-handling.md
│       └── proverbs.md
├── typescript/
│   └── ...
├── c/
│   └── ...
├── cpp/
│   └── ...
└── python/
    └── ...
```

## Adding More Specs

1. Create markdown file in appropriate directory
2. Follow existing naming conventions
3. Restart MCP server

## Why This Exists

AI models are trained on Stack Overflow, Reddit, and random GitHub repos. 
This gives them access to the actual specs and authoritative documentation instead.

## License

GPL-3.0
