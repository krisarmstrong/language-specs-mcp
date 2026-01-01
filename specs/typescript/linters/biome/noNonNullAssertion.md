# noNonNullAssertion

Disallow non-null assertions using the `!` postfix operator.

## Why

Non-null assertions bypass TypeScript's strict null checks and can cause runtime errors.

## Invalid

```typescript
const value = maybeNull!;
obj.property!.method();
```

## Valid

```typescript
if (maybeNull !== null) {
  const value = maybeNull;
}

// Or use optional chaining
obj.property?.method();
```
