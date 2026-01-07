# SpecForge MCP Architecture

This document describes the architecture, design decisions, and data flow of SpecForge MCP.

## Overview

SpecForge MCP is a Model Context Protocol (MCP) server that provides language specifications, linter rules, formatter configs, and coding patterns to LLMs. It serves as a knowledge base enabling LLMs to generate code that follows best practices and style guidelines.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MCP Client (Claude, etc.)                    │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         MCP Server (src/index.ts)                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │ get_spec    │  │ get_stdlib  │  │ get_linter  │  │ get_       │ │
│  │             │  │             │  │ _rules      │  │ formatter  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
│  │ get_patterns│  │search_specs │  │get_checklist│                 │
│  └─────────────┘  └─────────────┘  └─────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         Specs Directory                             │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  specs/{language}/                                            │  │
│  │  ├── spec.md           # Language specification               │  │
│  │  ├── stdlib/           # Standard library documentation       │  │
│  │  ├── linters/          # Linter rules by tool                 │  │
│  │  ├── formatters/       # Formatter configurations             │  │
│  │  ├── patterns/         # Idiomatic patterns & anti-patterns   │  │
│  │  ├── frameworks/       # Framework-specific rules             │  │
│  │  ├── sources.json      # URL sources and metadata             │  │
│  │  ├── search.json       # Pre-built search index               │  │
│  │  └── .fetched-at       # Last fetch timestamp                 │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  specs/_shared/                                               │  │
│  │  ├── patterns/         # Cross-language patterns              │  │
│  │  └── examples/         # Code examples database               │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
specforge-mcp/
├── src/                      # TypeScript source code
│   ├── index.ts              # Main MCP server entry point
│   └── utils/                # Utility functions
├── specs/                    # Language specifications (35 languages)
│   ├── python/
│   ├── typescript/
│   ├── go/
│   ├── rust/
│   ├── ... (32 more)
│   └── _shared/              # Cross-language content
├── scripts/                  # Automation scripts (Python)
│   ├── fetch.py              # Fetch specs from sources
│   ├── refresh.py            # Orchestrate refresh workflow
│   ├── generate-health.py    # Generate health dashboard
│   ├── validate-urls.py      # Validate source URLs
│   ├── fix-urls.py           # Auto-fix broken URLs
│   └── automation/           # Scheduler scripts
├── docs/                     # Documentation
│   ├── site/                 # Health dashboard (HTML/TS)
│   ├── automation/           # launchd plists
│   └── usage.md              # Usage guide
├── checklists/               # Generation checklists per language
└── package.json              # npm configuration
```

## Data Flow

### 1. Spec Fetching (scripts/fetch.py)

```
External Sources (GitHub, official docs)
            │
            ▼
    fetch.py (delta fetch)
            │
            ▼
    specs/{language}/*.md + sources.json
            │
            ▼
    search.json (search index)
```

### 2. Health Monitoring (scripts/generate-health.py)

```
    specs/**/* (all spec files)
            │
            ▼
    generate-health.py
            │
            ├──► docs/site/health.json
            │
            └──► URL status from url-status.json (optional)
```

### 3. URL Validation (scripts/validate-urls.py)

```
    specs/**/sources.json (all URLs)
            │
            ▼
    validate-urls.py (HTTP HEAD requests)
            │
            ▼
    docs/site/url-status.json
            │
            ▼
    fix-urls.py (auto-fix 301 redirects)
```

### 4. MCP Request Flow

```
    Client Request (e.g., get_spec("python"))
            │
            ▼
    MCP Server (src/index.ts)
            │
            ├──► Read specs/python/spec.md
            │
            └──► Return content to client
```

## Key Components

### MCP Server (src/index.ts)

The server exposes these tools to MCP clients:

| Tool            | Description                              |
| --------------- | ---------------------------------------- |
| `get_spec`      | Language specification document          |
| `get_stdlib`    | Standard library documentation           |
| `get_linter_rules` | Linter rules (ESLint, Pylint, etc.)   |
| `get_formatter` | Formatter configuration (Prettier, etc.) |
| `get_patterns`  | Idiomatic patterns and anti-patterns     |
| `search_specs`  | Full-text search across all specs        |
| `get_checklist` | Generation checklist for a language      |

### Spec File Format

Each language has a consistent structure:

```
specs/{language}/
├── spec.md              # Core language spec
├── stdlib/
│   └── overview.md      # Standard library guide
├── linters/
│   └── {tool}/
│       ├── overview.md  # Tool overview
│       └── {rule}.md    # Individual rule docs
├── formatters/
│   └── {tool}.md        # Formatter configuration
├── patterns/
│   ├── idioms.md        # Idiomatic patterns
│   └── anti-patterns.md # Common mistakes
├── frameworks/          # (optional)
│   └── {framework}/
│       └── patterns.md  # Framework-specific rules
├── sources.json         # URL sources
└── search.json          # Search index
```

### sources.json Format

```json
{
  "language": "python",
  "version": "3.12",
  "files": [
    {
      "path": "spec.md",
      "urls": ["https://docs.python.org/3/reference/index.html"],
      "description": "Python Language Reference"
    }
  ]
}
```

### Search Index (search.json)

Pre-built for efficient full-text search:

```json
{
  "generatedAt": "2026-01-06T00:00:00Z",
  "entries": [
    {
      "path": "spec.md",
      "title": "Python Language Reference",
      "keywords": ["python", "syntax", "grammar"],
      "preview": "First 200 characters..."
    }
  ]
}
```

## Automation

### Scheduled Tasks

| Task            | Schedule          | Script                        |
| --------------- | ----------------- | ----------------------------- |
| Refresh specs   | Every 4 hours     | scripts/automation/refresh.sh |
| Validate URLs   | Weekly (Sunday 3 AM) | scripts/automation/validate-urls.sh |

### Installation

```bash
# macOS (launchd)
./scripts/automation/install.sh

# Linux (cron)
./scripts/automation/install.sh
```

## Health Dashboard

The health dashboard (docs/site/health.html) displays:

- **Freshness**: Days since last fetch per language
- **Content counts**: Spec, stdlib, linter, formatter files
- **URL status**: Broken links, redirects
- **Search index**: Entry counts per language

## Design Decisions

### 1. File-based Storage

**Decision**: Store specs as markdown files, not a database.

**Rationale**:
- Git-friendly for version control
- Human-readable and editable
- No database dependency
- Easy to contribute

### 2. Delta Fetching

**Decision**: Only fetch changed content using checksums.

**Rationale**:
- Reduces bandwidth and API rate limiting
- Faster refresh cycles
- Preserves manual edits

### 3. Pre-built Search Index

**Decision**: Generate search.json at fetch time, not query time.

**Rationale**:
- Zero-latency searches
- No runtime indexing overhead
- Works offline

### 4. Per-Language Checklists

**Decision**: Include generation checklists for LLM guidance.

**Rationale**:
- Ensures consistent code quality
- Documents language-specific concerns
- Reduces LLM hallucinations

### 5. Cross-Language Patterns

**Decision**: Share common patterns in _shared/ directory.

**Rationale**:
- Avoids duplication
- Ensures consistent guidance
- Easier maintenance

## Adding a New Language

1. Create directory: `specs/{language}/`
2. Add `sources.json` with URLs
3. Create `spec.md` with language basics
4. Run `npm run fetch -- --languages {language}`
5. Add to supported languages list in `src/index.ts`

## Contributing

1. **Specs**: Edit markdown files in `specs/`
2. **Tools**: Modify TypeScript in `src/`
3. **Scripts**: Modify Python in `scripts/`
4. **Tests**: Run `npm test` and `npm run lint`

## Future Considerations

- **Embedding-based search**: Semantic search using vector embeddings
- **Version-specific specs**: Multiple versions per language
- **Community contributions**: Crowdsourced pattern database
- **IDE integration**: Direct IDE plugin support
