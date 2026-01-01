# noConsole

Disallow the use of `console`.

## Why

Console statements are typically used for debugging and should not be in production code.

## Invalid

```typescript
console.log("debug");
```

## Valid

```typescript
console.error("Error occurred");
console.warn("Warning");
console.info("Info message");

// Or use a proper logger
logger.debug("debug");
```

## Configuration

Allow specific methods:

```json
{
  "noConsole": {
    "level": "warn",
    "options": {
      "allow": ["warn", "error", "info", "debug"]
    }
  }
}
```
