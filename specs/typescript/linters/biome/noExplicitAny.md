# noExplicitAny

Disallow the `any` type usage.

## Why

The `any` type disables type checking and should be avoided.

## Invalid

```typescript
let x: any;
function fn(param: any): any {}
```

## Valid

```typescript
let x: unknown;
function fn(param: unknown): string {}
```

## Fix

1. Use a specific type if known
2. Use `unknown` and narrow with type guards
3. Use generics for flexible typing
