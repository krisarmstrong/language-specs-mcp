---
description: "Parse project config files to extract coding standards"
argument-hint: "<config-file-path>"
allowed-tools: [mcp__specforge__get_project_rules, Read, Glob]
---

Parse project configuration files to extract active lint rules and coding standards.

Arguments:
- $1: Path to config file (e.g., pyproject.toml, .eslintrc.json, biome.json, tsconfig.json)

If no argument provided, search for common config files in the current project:
1. Use Glob to find: pyproject.toml, .eslintrc*, biome.json, tsconfig.json
2. For each found file, use get_project_rules to extract the configuration

Use get_project_rules with:
- config_path: $1

This helps understand a project's coding standards before writing code.

Full arguments: $ARGUMENTS
