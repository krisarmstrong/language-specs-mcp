# CLAUDE.md - AI Assistant Guidance

This file provides guidance for AI assistants (Claude, Codex, etc.) working on the SpecForge MCP codebase.

## Project Overview

SpecForge MCP is a Model Context Protocol server that provides LLMs with authoritative language specifications, linter rules, formatter guidance, and coding patterns. It replaces training data from Stack Overflow with actual best practices.

## Architecture

```
specforge-mcp/
├── src/                    # TypeScript MCP server (single file)
│   └── index.ts           # MCP protocol implementation (806 lines)
├── scripts/               # Python data pipeline
│   ├── _common.py         # Shared utilities (fetch, parse, log)
│   ├── fetch.py           # Data-driven spec fetcher
│   ├── generate.py        # Search index generator
│   ├── validate.py        # JSON schema validation
│   ├── versions.py        # Tool version management
│   └── [utilities]        # URL validation, health, etc.
├── specs/                 # Generated specification data (35 languages)
│   └── <language>/
│       ├── sources.json   # URLs and provenance
│       ├── search.json    # Search index
│       ├── spec.md        # Language specification
│       ├── stdlib/        # Standard library docs
│       ├── linters/       # Linter rule docs
│       ├── formatters/    # Formatter docs
│       └── patterns/      # Best practice patterns
├── tests/                 # Unit tests (pytest + node:test)
│   └── unit/             # Python unit tests
├── tools/                # Tool version registry
│   └── versions.json     # Pinned linter/formatter versions
└── docs/                 # Documentation and site
    └── site/             # Health dashboard
```

## Key Principles

1. **Data-Driven Architecture**: Specs are fetched via `sources.json` config files, not hardcoded logic
2. **Provenance Tracking**: Every document has source URLs and SHA-256 hashes
3. **Strict Linting**: Python uses ruff (60+ rules), TypeScript uses biome
4. **High Test Coverage**: Core scripts maintain 97%+ coverage

## Code Standards

### Python (scripts/)

- Python 3.11+ required
- Use `from __future__ import annotations` for forward references
- Type hints required for function signatures
- Use pathlib.Path, not os.path
- Use context managers for file/network operations
- Run `ruff check` and `ruff format` before committing

### TypeScript (src/)

- Node.js 20+ required
- Strict TypeScript mode
- Use biome for linting and formatting
- Avoid `any` types - use specific types or generics

## Testing

```bash
# Python tests
python3 -m pytest tests/ -v

# TypeScript tests
npm test

# Coverage
python3 -m pytest tests/ --cov=scripts --cov-report=term-missing

# All checks
npm run lint && npm test && python3 -m pytest tests/
```

## Common Tasks

### Adding a New Language

1. Create `specs/<language>/sources.json` with URLs
2. Run `npm run fetch:<language>`
3. Add language to `LANGUAGES` array in `src/index.ts`
4. Run `npm run generate:all`

### Updating Tool Versions

```bash
npm run update:versions    # Fetch latest from upstream
npm run stamp:versions     # Stamp into spec files
npm run validate:versions  # Verify consistency
```

### Refreshing All Data

```bash
npm run refresh            # Delta fetch + regenerate
npm run fetch:all          # Full refetch
```

## MCP Tools Provided

| Tool | Purpose |
|------|---------|
| `get_checklist` | Critical rules BEFORE writing code |
| `get_spec` | Language specification |
| `get_linter_rule` | Specific linter rule |
| `search_specs` | Search all specifications |
| `list_available` | List available topics |

## File Naming Conventions

- Specs: `<topic>.md` or `<tool>/<rule>.md`
- Scripts: `<verb>-<noun>.py` (e.g., `validate-urls.py`)
- Tests: `test_<module>.py` in `tests/unit/`

## Security Notes

- Path traversal protection in `resolveSpecPath()` (src/index.ts)
- URL validation before fetching
- No user input executed as code

## Do NOT

- Add dependencies without justification
- Commit secrets or API keys
- Skip linting or tests
- Modify specs/ files directly (they're generated)

## Helpful Commands

```bash
npm run doctor             # Environment diagnostics
npm run verify             # Validate all specs
npm run dashboard          # Start health dashboard
npm run diagnose:fetch     # Debug network issues
```

## Commit Message Format

```
<type>: <description>

Types: feat, fix, docs, test, chore, refactor
```

## Questions?

Check `docs/usage.md` for user-facing documentation or `README.md` for full setup instructions.
