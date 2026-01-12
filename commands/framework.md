---
description: "Get framework-specific checklist and best practices"
argument-hint: "<language> <framework>"
allowed-tools: [mcp__specforge__get_framework_checklist]
---

Get framework-specific checklist and best practices for popular frameworks.

Arguments:
- $1: Programming language (e.g., python, typescript, javascript)
- $2: Framework name (e.g., react, fastapi, django, express, nextjs, vue)

Use get_framework_checklist with:
- language: $1
- framework: $2

Supported frameworks by language:
- JavaScript/TypeScript: react, express, nextjs, vue, angular
- Python: fastapi, django, flask

Full arguments: $ARGUMENTS
