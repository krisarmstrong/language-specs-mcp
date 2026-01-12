---
description: "Get detailed explanation of a specific linter rule"
argument-hint: "<language> <linter> <rule>"
allowed-tools: [mcp__specforge__get_linter_rule, mcp__specforge__list_available]
---

Get detailed explanation of why a linter rule exists and how to satisfy it.

Arguments:
- $1: Programming language (e.g., python, typescript, go)
- $2: Linter name (e.g., ruff, biome, eslint, golangci-lint)
- $3: Rule name (e.g., E501, noExplicitAny, errcheck)

Use get_linter_rule with:
- language: $1
- linter: $2
- rule: $3

If arguments are missing, explain the command usage and list available linters for the specified language using list_available.

Full arguments: $ARGUMENTS
