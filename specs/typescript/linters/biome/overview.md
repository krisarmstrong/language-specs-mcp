# Biome Linter - Complete Rules Reference

**Source:** https://biomejs.dev/linter/rules/

Biome is a fast formatter and linter for JavaScript, TypeScript, JSX, JSON, CSS.

## Rule Categories

| Category | Purpose |
|----------|---------|
| correctness | Prevent bugs and incorrect behavior |
| suspicious | Potentially problematic patterns |
| style | Code style consistency |
| complexity | Reduce cognitive complexity |
| performance | Optimize runtime performance |
| security | Prevent security vulnerabilities |
| a11y | Accessibility in JSX |
| nursery | Experimental rules |

## Severity Levels

- `error`: Fails CI, must fix
- `warn`: Warning, should fix
- `off`: Disabled

## Configuration

```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.0/schema.json",
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "correctness": {
        "noUnusedVariables": "error"
      }
    }
  }
}
```
