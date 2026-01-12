---
description: "Get coding checklist before writing code in a language"
argument-hint: "<language>"
allowed-tools: [mcp__specforge__get_checklist, mcp__specforge__get_security_checklist, mcp__specforge__get_anti_patterns]
---

Get the generation checklist for a programming language. This includes critical rules, security guidelines, and common anti-patterns to avoid.

Arguments:
- $1: Programming language (e.g., python, typescript, go, rust)

If $1 is "security", return the OWASP security checklist.
If $1 is "anti-patterns", return the LLM anti-patterns guide.
Otherwise, use get_checklist with the specified language.

IMPORTANT: This checklist should be consulted BEFORE writing code to ensure best practices are followed and common mistakes are avoided.

Full arguments: $ARGUMENTS
