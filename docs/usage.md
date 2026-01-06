# Usage Guide

This MCP server is meant to be the source of truth for language specs, stdlib references, linters, formatters, and coding patterns.

Requirements:
- Node.js >= 20
- Python 3.14.2
- pandoc (optional, improves markdown conversion quality; built-in converter runs without it)

## LLM Value

The repo packages authoritative documentation so LLMs can:

- cite canonical language specs and standard library behavior before answering syntax or API questions,
- dig into linter rules to explain why something is flagged and what the safest fix looks like,
- reference formatter guidance and patterns to keep generated code consistent and performant,
- lean on health metadata, tooling-version records, and search indexes to understand what’s covered and how fresh it is.

## Quick Start

After cloning, refresh the repo and run the checks so you can start serving the MCP endpoints:

```bash
git clone https://github.com/openai/specforge-mcp.git
cd specforge-mcp
npm install
npm run refresh
npm test
```

`npm run refresh` executes `fetch:delta` and `generate:all` so the dashboard, indexes, and manifests stay in sync.

## Prompt Patterns

Use a short instruction to force tool usage.

Claude Code:

```text
Always consult the SpecForge MCP server for spec, stdlib, linter, formatter, and patterns questions before answering.
```

Codex CLI:

```text
Use the SpecForge MCP server first for any language or tooling questions; cite results in the answer.
```

VS Code extensions:

```text
Use the SpecForge MCP server for authoritative references. Prefer MCP results over general knowledge.
```

## When To Use The Server

- Language syntax or semantics questions
- Standard library usage or behavior
- Linter/formatter rule explanations and fixes
- Idiomatic patterns and best practices

## Tool Behavior Notes

- `search_specs` supports `allow_fallback` (boolean). Set to `false` or configure `SEARCH_FALLBACK_STRATEGY=warn` when indexes are missing to skip the markdown fallback; the server will report which languages lack search data.
- `list_resources` is paginated. Use the `cursor` field from the response to request the next page.
- `RESOURCE_PAGE_SIZE` (default 250, min 25, max 1000) keeps each `resources/list` response bounded when you walk very large catalogs.
- `health.json` summarizes every language's freshness, spec coverage, and default linter/formatter counts. Use it or the `health.html` dashboard (via `npm run dashboard`) when you want a bird's-eye view.

## Logging

- Set `SPECFORGE_LOG_LEVEL` (or `LOG_LEVEL`) to control verbosity (default: `INFO`).
- Override `SPECFORGE_LOG_FORMAT` or `SPECFORGE_LOG_DATE_FORMAT` to customize output.
- Set `GITHUB_TOKEN` to avoid GitHub API rate limits during version updates.
- Create a token in GitHub Settings → Developer settings → Personal access tokens (no scopes needed for public data).
- If you already use GitHub CLI, `gh auth token` prints a usable token.

## Automation & Scheduling

Run `npm run refresh` to execute `fetch:delta` and `generate:all` in order; this keeps indexes, manifests, and the dashboard data aligned with upstream sources.

Use `.env` to store `GITHUB_TOKEN` and other env vars (copy from `.env.example`).
The `.env` file is ignored by git.

Quality gates:

```bash
npm run validate:versions
npm run validate:stubs
```

Diagnostics:

```bash
npm run doctor
```

Stub remediation (spec/overview only by default):

```bash
npm run backfill:stubs
```

Schedule that command via cron, launchd, GitHub Actions, etc. Here are defaults you can copy and customize (every four hours):

```bash
0 */4 * * * cd /Users/krisarmstrong/Developer/_tools/specforge-mcp && npm run refresh >> refresh.log 2>&1
```

The script prints each command before running it and exits with the first failing status so you can hook alerts into your job runner.

GitHub Actions already refresh the repo for you via `.github/workflows/refresh.yml`, which mirrors this command on a four-hour schedule and can be triggered manually.

Launchd (macOS) template:

```bash
cp docs/automation/com.specforge.refresh.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.specforge.refresh.plist
```

Helper scripts:

```bash
./scripts/automation/install.sh
./scripts/automation/uninstall.sh
```

Cron template:

```bash
cat docs/automation/cron.txt
```

Update the paths and `GITHUB_TOKEN` value in the templates to match your setup.

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
