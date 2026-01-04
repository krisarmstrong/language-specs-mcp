# Usage Guide

This MCP server is meant to be the source of truth for language specs, stdlib references, linters, formatters, and coding patterns.

Requirements:
- Node.js >= 20
- Python 3.14.2
- pandoc (optional, improves markdown conversion)

## Prompt Patterns

Use a short instruction to force tool usage.

Claude Code:

```text
Always consult the language-specs MCP server for spec, stdlib, linter, formatter, and patterns questions before answering.
```

Codex CLI:

```text
Use the language-specs MCP server first for any language or tooling questions; cite results in the answer.
```

VS Code extensions:

```text
Use the language-specs MCP server for authoritative references. Prefer MCP results over general knowledge.
```

## When To Use The Server

- Language syntax or semantics questions
- Standard library usage or behavior
- Linter/formatter rule explanations and fixes
- Idiomatic patterns and best practices

## Tool Behavior Notes

- `search_specs` supports `allow_fallback` (boolean). Set to `false` to skip full-file scanning when indexes are missing.
- `list_resources` is paginated. Use the `cursor` field from the response to request the next page.
- `health.json` summarizes every language's freshness, spec coverage, and default linter/formatter counts. Use it or the `health.html` dashboard (via `npm run dashboard`) when you want a bird's-eye view.

## Provenance

Run `npm run generate:manifests` to build `specs/<language>/sources.json` with SHA-256 hashes and source URLs for each document.
This gives you a verifiable audit trail for every spec we surface.

## Request Examples

Get a spec:

```json
{ "language": "go", "category": "spec", "topic": "spec" }
```

Get stdlib docs:

```json
{ "language": "python", "category": "stdlib", "topic": "pathlib" }
```

Get a linter rule:

```json
{ "language": "typescript", "linter": "biome", "rule": "noExplicitAny" }
```

Search:

```json
{ "query": "error handling" }
```
