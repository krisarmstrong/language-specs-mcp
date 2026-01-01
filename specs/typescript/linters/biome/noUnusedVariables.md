# noUnusedVariables

Disallow unused variables.

## Why

Unused variables are dead code and should be removed.

## Invalid

```typescript
const unused = 5;

function fn(unusedParam: string) {
  return "hello";
}
```

## Valid

```typescript
const used = 5;
console.info(used);

function fn(_ignoredParam: string) {
  return "hello";
}
```

## Note

Prefix with underscore `_` to indicate intentionally unused.
