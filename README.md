# SpecForge MCP Server

Make LLMs write better code, not just code that works.

**Purpose:** Give AI assistants authoritative language specs, generation checklists, and linter rules—replacing training data from Stack Overflow and random GitHub repos with actual best practices.

## Quick Start

**New here?** See [QUICKSTART.md](QUICKSTART.md) for 5-minute setup.

**LLM Integration:** See [System Prompt Template](docs/SYSTEM_PROMPT_TEMPLATE.md) to configure LLMs to use SpecForge automatically.

## Key Feature: Generation Checklists

Every supported language now has a `generation-checklist.md` with 10-20 critical rules to follow BEFORE writing code:

```
specs/python/generation-checklist.md     # Type hints, pathlib, context managers...
specs/typescript/generation-checklist.md # const/let, ===, Promise handling...
specs/go/generation-checklist.md         # Error handling, defer, context...
specs/rust/generation-checklist.md       # Ownership, ?, no unwrap...
... (35 languages total)
```

**The Difference:**

| Without SpecForge | With SpecForge |
|-------------------|----------------|
| Code that "works" | Code that follows best practices |
| Silent bugs | Caught by linter-aware patterns |
| Security vulnerabilities | Security anti-patterns avoided |
| Inconsistent style | Idiomatic code |

### MCP Tools

| Tool | Purpose |
|------|---------|
| `get_checklist(language)` | **Call FIRST** - Critical rules before writing code |
| `get_spec(language, category, topic)` | Full language specification |
| `get_linter_rule(language, linter, rule)` | Specific linter rule explanation |
| `search_specs(query)` | Search across all specs |
| `list_available(language, category)` | List available topics |

## Supported Languages

| Language | Spec | Stdlib | Linters | Formatters | Patterns |
|----------|------|--------|---------|------------|----------|
| Assembly (x86-64, ARM, RISC-V, WASM) | ✅ | ✅ (ABI refs) | - | - | ✅ |
| BASIC | ✅ | ✅ | - | - | ✅ |
| Bash | ✅ | ✅ | shellcheck | shfmt | ✅ |
| Batch | ✅ | ✅ | - | - | ✅ |
| Go | ✅ | ✅ | golangci-lint | gofmt, goimports, gofumpt, golines | ✅ |
| C# | ✅ | ✅ (namespace pages) | .NET analyzers, StyleCop | dotnet format | ✅ |
| JavaScript | ✅ | ✅ (Node + Web APIs) | ESLint, standardjs, xo | Prettier, Biome | ✅ |
| TypeScript | ✅ | ✅ | Biome | Prettier, Biome | ✅ |
| C | ✅ | ✅ | clang-tidy, cppcheck | clang-format | ✅ |
| C++ | ✅ | ✅ | clang-tidy, cppcheck | clang-format | ✅ |
| CSS | ✅ | ✅ | stylelint | Prettier | ✅ |
| HTML | ✅ | ✅ | html-validate, htmlhint | Prettier | ✅ |
| Git | ✅ | ✅ | gitlint, commitlint | commitlint/commitizen | ✅ |
| Java | ✅ | ✅ (package pages) | Error Prone, SpotBugs, Checkstyle, PMD | google-java-format | ✅ |
| Kotlin | ✅ | ✅ (package pages) | detekt, ktlint | ktlint, ktfmt | ✅ |
| Lua | ✅ | ✅ | luacheck | stylua | ✅ |
| PowerShell | ✅ | ✅ | PSScriptAnalyzer | - | ✅ |
| Python | ✅ | ✅ (module pages) | Ruff, Pylint, Flake8, mypy | black | ✅ |
| Rust | ✅ | ✅ (module pages) | clippy | rustfmt | ✅ |
| SQL | ✅ | ✅ (Postgres/MySQL/SQLite/SQL Server) | sqlfluff | sqlfluff | ✅ |
| Swift | ✅ | ✅ (module pages) | SwiftLint | swift-format | ✅ |
| PHP | ✅ | ✅ | PHPStan, Psalm | PHP-CS-Fixer | ✅ |
| Ruby | ✅ | ✅ | RuboCop | RuboCop | ✅ |
| Dart | ✅ | ✅ | Dart linter | dart format | ✅ |
| R | ✅ | ✅ | lintr | styler | ✅ |
| Julia | ✅ | ✅ | JET, StaticLint | JuliaFormatter | ✅ |
| Scala | ✅ | ✅ | Scalafix, WartRemover | Scalafmt | ✅ |
| Elixir | ✅ | ✅ | Credo | mix format | ✅ |
| Clojure | ✅ | ✅ | clj-kondo, eastwood | zprint | ✅ |
| Haskell | ✅ | ✅ | HLint | fourmolu, ormolu | ✅ |
| Zig | ✅ | ✅ | - | zig fmt | ✅ |
| OCaml | ✅ | ✅ | odoc | ocamlformat | ✅ |
| Markdown | ✅ | - | markdownlint | Prettier, markdownfmt | ✅ |
| YAML | ✅ | - | yamllint | Prettier, yamlfix | ✅ |
| Dockerfile | ✅ | - | hadolint | - | ✅ |

Notes on specs:
- Some ecosystems do not publish a single open spec; we use the most authoritative public references available.
- C++ uses cppreference, as ISO C++ specs are copyrighted.
- TypeScript uses the official Handbook (the formal spec is archived).
- SQL uses vendor references (PostgreSQL/MySQL/SQLite/SQL Server).
- Assembly uses vendor/architecture references plus ABI docs in stdlib.

## BASIC Ecosystem Notes

If you are working with modern or classic BASIC, these are common environments and alternatives:
- QB64 Phoenix Edition (QB64 PE): https://github.com/QB64-Phoenix-Edition/QB64pe
  - Compiles to native 64-bit executables, supports higher-res graphics and modern audio, ships with a retro IDE.
  - Compatible with legacy .BAS and QuickBASIC 4.5 code.
- QBJS (web-based): https://qbjs.org/
  - Runs in modern browsers, good for Chromebook/mobile use.
- FreeBASIC: https://www.freebasic.net/
  - High compatibility with QuickBASIC plus pointers and OOP features.
- PC-BASIC: https://robhagemans.github.io/pcbasic/
  - Emulator for GW-BASIC and line-numbered programs.
- BlitzMax NG: https://blitzmax.org/
  - Modern BASIC aimed at speed and game development.
- Classic QBasic 1.1:
  - 16-bit DOS program; use DOSBox-X or vDosPlus to run on modern Windows.
  - Original files are commonly mirrored on sites like WinWorld (use trusted archives).

## Installation

Requirements:
- Node.js >= 20
- Python 3.14.2
- pandoc (optional, improves markdown conversion quality; built-in converter runs without it)

## Getting Started

Clone, install, and refresh from GitHub:

```bash
git clone https://github.com/openai/specforge-mcp.git
cd specforge-mcp
npm install
npm run refresh
npm test
```

`npm run refresh` runs `fetch:delta` and the generate scripts so the dataset stays consistent. `npm test` verifies the MCP tooling before you deploy or serve the server.

## Fetching Specs

```bash
# All languages (parallel by default)
npm run fetch:all

# Serial (lower network/CPU pressure)
npm run fetch:all:serial

# Parallel (explicit)
npm run fetch:all:parallel

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
npm run fetch:php
npm run fetch:ruby
npm run fetch:dart
npm run fetch:r
npm run fetch:julia
npm run fetch:scala
npm run fetch:elixir
npm run fetch:clojure
npm run fetch:haskell
npm run fetch:zig
npm run fetch:ocaml
npm run fetch:markdown
npm run fetch:yaml
npm run fetch:dockerfile
```

Parallel fetch tuning:

```bash
# Limit concurrency and add tighter timeouts
FETCH_TASK_TIMEOUT_MS=900000 FETCH_TASK_KILL_MS=30000 npm run fetch:all:parallel -- --max-concurrency 2
```

Scope runs (parallel by default):

```bash
npm run fetch:stdlib
npm run fetch:linters
npm run fetch:formatters
npm run fetch:patterns
```

Delta runs (only stale or missing `.fetched-at`):

```bash
npm run fetch:delta
```

## Coverage

Run `npm run verify` to validate specs and print a per-language coverage table.

Example output:

```text
Spec verification passed for 21 languages.

Coverage summary:
| Language | Spec | Stdlib | Linters | Formatters | Patterns | Fetched (UTC) |
|---|---|---|---|---|---|---|
| go | 1 | 350 | 420 | 4 | 5 | 2025-01-01T00:00:00Z |
```

## Indexes and Manifests

Generate repository indexes and provenance manifests:

```bash
npm run generate:index
npm run generate:manifests
npm run generate:search
```

The index is written to `specs/index.json` and `specs/<language>/index.json`.
Manifests are written to `specs/<language>/sources.json` with SHA-256 hashes and source URLs.
Search indexes are written to `specs/<language>/search.json` for context search in the site.

## Provenance

Every fetched document is traced to its source URL and a SHA-256 hash in `specs/<language>/sources.json`.
Run `npm run generate:manifests` to refresh these provenance records and audit the upstream sources we cite.

## Health Dashboard

Generate a machine-readable health summary and serve a lightweight dashboard for quick inspection.

```
npm run generate:health
npm run dashboard
```

The dashboard is available at `http://localhost:9000/health.html` and the data lives in `docs/site/health.json`.
LLMs can also call the data file directly to see freshness, linter/formatter coverage, and tooling sources for each language.

## Automation & Refresh

Keep the specs, indexes, and health metadata up to date with `npm run refresh`. That script runs `fetch:delta` and `generate:all` in sequence so the dashboard stays in sync with the latest sources. The same command is wired into `.github/workflows/refresh.yml`, so GitHub Actions refreshes the data every four hours (or whenever you trigger the workflow manually).

Schedule it with your preferred cron/agent. Example:

```bash
0 */4 * * * cd /Users/krisarmstrong/Developer/_tools/specforge-mcp && npm run refresh >> refresh.log 2>&1
```

GitHub Actions or a local `launchd` job can call the same command; the script will print progress for each step and bubble up any failure code.

## How To Use With LLMs

This MCP server is the authoritative source for language syntax, standard library behavior, linter rules, formatter guidance, and idiomatic patterns. Use it to keep LLM outputs aligned to best practices, linting/formatting expectations, tooling versions, and even security/performance callouts buried in the referenced docs.

Before generating code or answering questions, consult these tools:

- `get_spec`: verify the language/category/topic you are about to describe.
- `get_linter_rule`: read the motivating guidance behind lint rules and how to satisfy them safely.
- `search_specs`: explore patterns, best practices, or guesswork you want to avoid.
- `list_available`: confirm what topics exist before making assumptions.
- `health.json`/`health.html`: check freshness, tooling coverage, and per-language readiness.
- `tools/versions.json`: stay in sync with the recorded tooling versions so downstream automation and security updates match.

Add a short instruction so the model always queries the MCP server first:

Claude Code (add to `CLAUDE.md` or `AGENTS.md`):

```text
When answering language, stdlib, linting, or formatting questions, call the SpecForge MCP server first and cite the result.
```

Codex CLI (add to `AGENTS.md`):

```text
Always consult the SpecForge MCP server for spec/stdlib/linter/formatter details before answering.
```

VS Code:

```text
Use an MCP-capable extension (Claude Code, Continue, Cline, etc), add this server, and include the same instruction in the project prompt or repo docs.
```

Tool tips:
- Use `list_available` when you are unsure of a topic name.
- Use `search_specs` with `allow_fallback: false` for predictable latency on large installs.
- Use `list_resources` pagination via the returned `cursor` for large catalogs.

Full usage guide: `docs/usage.md`.

## Search & Resource tuning

- Set `allow_fallback=false` or `SEARCH_FALLBACK_STRATEGY=warn` when you want to skip expensive markdown scans for languages that lack a search index; the server will return a warning that lists the affected languages.
- `resources/list` is already paged, but you can clamp the payload even tighter with `RESOURCE_PAGE_SIZE` (default 250, min 25, max 1000) while iterating through `cursor` values.

## Data Freshness

Each fetch script writes `specs/<language>/.fetched-at` (UTC). Refresh with:

```bash
npm run fetch:all
npm run fetch:all:serial
```

Automation templates (cron + launchd) are in `docs/automation/`.

## Troubleshooting

- Missing `pandoc`: HTML conversions use the built-in converter; results may be noisier than pandoc output.
- Encoding issues: run with `LC_ALL=C` if you see illegal byte sequence errors.
- Rate limits/timeouts: retry or use `npm run fetch:all:parallel` with lower concurrency.
- Network restrictions: ensure the CLI can access external docs.
- TLS verification failures: set `SSL_CERT_FILE` or `REQUESTS_CA_BUNDLE` to your CA bundle.
- If you have no CA bundle, install certifi (`python3 -m pip install --upgrade certifi`); fetch scripts will use it if available.
- Emergency bypass: `FETCH_INSECURE=1` disables TLS verification (not recommended).
- GitHub rate limits: set `GITHUB_TOKEN` to raise API limits for version checks.
- Token setup: create a Personal Access Token in GitHub settings (no scopes needed for public data), or run `gh auth token` if you use GitHub CLI.
- Put the token in `.env` (copy from `.env.example`). `.env` is ignored by git.
- Diagnose connectivity: `npm run diagnose:fetch -- https://eslint.org/docs/latest/rules/`
- Logging: set `SPECFORGE_LOG_LEVEL` (or `LOG_LEVEL`) and `SPECFORGE_LOG_FORMAT` for more verbose output.

## Version Registry

Pinned tool versions live in `tools/versions.json`.

Validate against local references:

```bash
npm run validate:versions
```

Validate stub allowlist (no new stub docs):

```bash
npm run validate:stubs
```

Diagnostics:

```bash
npm run doctor
```

Typical flow:

```bash
npm run update:versions
npm run stamp:versions
npm run validate:versions
```

Check against latest upstream versions (network):

```bash
npm run validate:versions:latest
```

Update the registry from upstream (network):

```bash
npm run update:versions
```

Stamp versions into docs:

```bash
npm run stamp:versions
```

Validate freshness of specs (default 90 days):

```bash
npm run validate:freshness
```

Version report:

```bash
npm run report:versions
npm run report:versions:latest
```

## Testing

Run the unit test suite:

```bash
npm test
```

CI runs `npm run verify` and `npm run validate:freshness` in addition to build/test.

## GitHub Pages Site

A lightweight browser UI lives in `docs/site`. Enable GitHub Pages to publish from `docs/site`.

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
    "SpecForge": {
      "command": "node",
      "args": ["/Users/krisarmstrong/Developer/_tools/specforge-mcp/dist/index.js"]
    }
  }
}
```

## Claude Code Configuration

Add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "SpecForge": {
      "command": "node",
      "args": ["/Users/krisarmstrong/Developer/_tools/specforge-mcp/dist/index.js"]
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

## Verification

```bash
npm run verify
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
Before writing or modifying code, consult the `SpecForge` MCP server.
Use `get_spec` for language/stdlib questions, `get_linter_rule` for lint guidance, and `search_specs` if unsure.
```

### Claude CLI

Add to your project prompt or instructions:

```
Always check `SpecForge` before proposing code.
Prefer tool output over general knowledge.
```

### Claude Desktop

Add the MCP server config (see above), then include a short reminder in your system or project prompt to consult the server.

### VS Code (MCP-capable clients)

Depending on your client extension:

- Claude Code / Continue / other MCP-enabled tools: add the same instruction in the workspace or project prompt.
- If the client supports “always use tool” rules, set `SpecForge` for spec/stdlib/lint queries.

Example prompt:

```
Use `SpecForge` for all spec/stdlib/linter/formatter questions. If you are unsure, run `search_specs` first.
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
