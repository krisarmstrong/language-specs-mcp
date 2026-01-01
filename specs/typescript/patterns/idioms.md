# TypeScript Idiomatic Patterns

## Use explicit types for function signatures

```typescript
// BAD
function process(data) {
  return data.map(x => x.value);
}

// GOOD
function process(data: Item[]): string[] {
  return data.map((x) => x.value);
}
```

## Never use `any`

```typescript
// BAD
const data: any = response.body;

// GOOD
interface ResponseBody {
  items: Item[];
  total: number;
}
const data: ResponseBody = response.body;

// If truly unknown, use `unknown` and narrow
const data: unknown = response.body;
if (isResponseBody(data)) {
  // data is now ResponseBody
}
```

## Use `readonly` for immutable data

```typescript
interface Config {
  readonly apiUrl: string;
  readonly timeout: number;
}
```

## Prefer interfaces over type aliases for objects

```typescript
// Prefer
interface User {
  id: string;
  name: string;
}

// Over
type User = {
  id: string;
  name: string;
};
```

## Use discriminated unions

```typescript
interface Success {
  kind: "success";
  data: Data;
}

interface Failure {
  kind: "failure";
  error: Error;
}

type Result = Success | Failure;

function handle(result: Result) {
  switch (result.kind) {
    case "success":
      return result.data;
    case "failure":
      throw result.error;
  }
}
```

## Use `satisfies` for type checking without widening

```typescript
const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000,
} satisfies Config;
```

## Prefer `for...of` over `forEach`

```typescript
// BAD - can't break, can't await properly
items.forEach((item) => {
  process(item);
});

// GOOD
for (const item of items) {
  await process(item);
}
```

## Use type guards

```typescript
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}
```
