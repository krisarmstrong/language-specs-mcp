# SpecForge Claude Code Plugin

SpecForge can run as both an MCP server and a native Claude Code plugin. This document covers the plugin mode.

## Installation

### Option 1: Install from Git Repository

```bash
/plugin install github:krisarmstrong/specforge-mcp
```

### Option 2: Install from Local Directory

```bash
/plugin install /path/to/specforge-mcp
```

### Option 3: Add to Project Settings

Add to your project's `.claude/settings.json`:

```json
{
  "plugins": ["github:krisarmstrong/specforge-mcp"]
}
```

## Available Slash Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/spec` | Get language specification | `/spec python stdlib pathlib` |
| `/checklist` | Get pre-coding checklist | `/checklist typescript` |
| `/lint-rule` | Get linter rule explanation | `/lint-rule python ruff E501` |
| `/search-specs` | Search all specifications | `/search-specs async error handling` |
| `/framework` | Get framework checklist | `/framework python fastapi` |
| `/project-rules` | Parse project config | `/project-rules pyproject.toml` |

## Specialized Agents

The plugin includes specialized agents that Claude automatically uses when relevant:

### spec-advisor
Advises on coding standards and best practices before writing code.

### security-reviewer
Reviews code for security vulnerabilities using OWASP guidelines.

### linter-helper
Helps understand and fix linter warnings and errors.

### code-standards
Enforces project coding conventions during code review.

## Auto-Invoked Skills

The SpecForge skill automatically activates when:
- Writing code in any of the 35+ supported languages
- Encountering linter warnings or errors
- Implementing security-sensitive features
- Using frameworks like React, FastAPI, Django, etc.

## WebUI

Start the WebUI for a graphical interface:

```bash
npm run webui:install  # First time only
npm run dev:webui      # Development mode
npm run start:webui    # Production mode
```

Access at: http://localhost:3847

### WebUI Features

- **Spec Browser**: Browse all language specifications by category
- **Search**: Full-text search across all specifications
- **Memories**: Store project-specific notes for future sessions
- **Configuration**: Manage plugin settings

## Dual Mode Operation

SpecForge supports both MCP server and plugin modes:

### As MCP Server (for other tools)

```bash
npm run start:mcp
```

Or add to your MCP configuration:

```json
{
  "specforge": {
    "command": "npx",
    "args": ["specforge-mcp"]
  }
}
```

### As Claude Code Plugin

Use the `/plugin install` command as shown above.

## Supported Languages

assembly, basic, bash, batch, c, cpp, csharp, css, dart, dockerfile, 
elixir, clojure, go, git, haskell, html, java, javascript, julia, 
kotlin, lua, markdown, ocaml, php, powershell, python, r, ruby, 
rust, scala, sql, swift, typescript, yaml, zig

## Available Tools (MCP)

| Tool | Description |
|------|-------------|
| `get_spec` | Get language specification |
| `get_checklist` | Get pre-coding checklist |
| `get_linter_rule` | Get linter rule explanation |
| `search_specs` | Search specifications |
| `list_available` | List available specs |
| `get_security_checklist` | Get OWASP security checklist |
| `get_anti_patterns` | Get LLM anti-patterns |
| `get_framework_checklist` | Get framework checklist |
| `get_project_rules` | Parse project config |

## Configuration

Environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `SPECS_DIR` | Path to specs directory | `./specs` |
| `RESOURCE_PAGE_SIZE` | Resources per page | `250` |
| `SEARCH_FALLBACK_STRATEGY` | `scan` or `warn` | `scan` |

## File Structure

```
specforge-mcp/
├── .claude-plugin/
│   └── plugin.json         # Plugin manifest
├── commands/               # Slash commands
│   ├── spec.md
│   ├── checklist.md
│   ├── lint-rule.md
│   ├── search-specs.md
│   ├── framework.md
│   └── project-rules.md
├── agents/                 # Specialized agents
│   ├── spec-advisor.md
│   ├── security-reviewer.md
│   ├── linter-helper.md
│   └── code-standards.md
├── skills/
│   └── specforge/
│       └── SKILL.md       # Auto-invoked skill
├── hooks/
│   └── hooks.json         # Session hooks
├── .mcp.json              # MCP server config
├── webui/                 # WebUI application
│   ├── src/
│   └── package.json
├── specs/                 # Language specifications
│   └── <language>/
└── src/
    └── index.ts           # MCP server implementation
```

## Hooks

The plugin includes hooks that:
- Notify you of available commands at session start
- Remind you to check the checklist before writing code

## Troubleshooting

### Plugin not loading

1. Ensure the plugin is installed: `/plugin list`
2. Check plugin health: `/plugin info specforge`
3. Reinstall if needed: `/plugin uninstall specforge && /plugin install ...`

### MCP server issues

1. Check if built: `ls dist/index.js`
2. Rebuild: `npm run build`
3. Check logs for errors

### WebUI not starting

1. Install dependencies: `npm run webui:install`
2. Check port availability: Port 3847
3. Check console for errors

## Contributing

See CONTRIBUTING.md for guidelines.

## License

MIT License - see LICENSE for details.
