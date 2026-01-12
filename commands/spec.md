---
description: "Get language specification, documentation, or style guide"
argument-hint: "<language> <category> <topic>"
allowed-tools: [mcp__specforge__get_spec, mcp__specforge__list_available, mcp__specforge__search_specs]
---

Get authoritative language specification for the requested language, category, and topic.

Arguments:
- $1: Programming language (e.g., python, typescript, go, rust)
- $2: Category (spec, stdlib, linters, patterns, formatters)
- $3: Topic (e.g., error-handling, fmt, async)

Use the get_spec tool with:
- language: $1
- category: $2
- topic: $3

If no arguments provided, list available languages and categories.

If only language provided, use list_available to show what's available for that language.

Full arguments: $ARGUMENTS
