# Biome Performance Rules

Rules that help optimize runtime performance.

## noAccumulatingSpread

Avoid spread in accumulators (O(n²)).

```typescript
// BAD - O(n²) complexity
const result = items.reduce((acc, item) => ({
  ...acc,
  [item.id]: item
}), {});

// GOOD - O(n) complexity
const result: Record<string, Item> = {};
for (const item of items) {
  result[item.id] = item;
}

// Or use Object.fromEntries
const result = Object.fromEntries(
  items.map(item => [item.id, item])
);
```

**Why:** Each spread copies the entire accumulator.

## noBarrelFile

Avoid barrel files (index.ts that re-exports).

```typescript
// BAD - barrel file (index.ts)
export { Foo } from "./foo";
export { Bar } from "./bar";
export { Baz } from "./baz";

// GOOD - import directly
import { Foo } from "./components/foo";
import { Bar } from "./components/bar";
```

**Why:** Barrel files prevent tree-shaking and slow down builds.

## noDelete

Avoid delete operator.

```typescript
// BAD - deoptimizes object
delete obj.property;

// GOOD - set to undefined
obj.property = undefined;

// Or use destructuring to omit
const { property, ...rest } = obj;
```

**Why:** delete changes object shape, causing V8 to deoptimize.

## noReExportAll

Avoid export * (re-export all).

```typescript
// BAD
export * from "./module";

// GOOD
export { foo, bar } from "./module";
```

**Why:** Prevents tree-shaking, imports everything.
