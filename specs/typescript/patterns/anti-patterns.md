# TypeScript Anti-Patterns

Common mistakes and code smells to avoid in TypeScript code.

## Using `any` Type

```typescript
// BAD - Defeats purpose of TypeScript
function process(data: any): any {
  return data.value;
}

// GOOD - Proper typing
function process<T extends { value: string }>(data: T): string {
  return data.value;
}

// ALSO GOOD - Use unknown for truly unknown types
function processUnknown(data: unknown): string {
  if (typeof data === "object" && data !== null && "value" in data) {
    return String((data as { value: unknown }).value);
  }
  throw new Error("Invalid data");
}
```

## Type Assertions Instead of Type Guards

```typescript
// BAD - Runtime errors possible
function getLength(value: string | string[]): number {
  return (value as string[]).length; // Crash if string!
}

// GOOD - Type guard
function getLength(value: string | string[]): number {
  if (Array.isArray(value)) {
    return value.length;
  }
  return value.length;
}
```

## Non-null Assertion Abuse

```typescript
// BAD - Hides potential null issues
function getName(user: User | null): string {
  return user!.name; // Crash if null!
}

// GOOD - Proper null handling
function getName(user: User | null): string {
  if (!user) {
    throw new Error("User is required");
  }
  return user.name;
}

// ALSO GOOD - Optional chaining with default
function getName(user: User | null): string {
  return user?.name ?? "Anonymous";
}
```

## Callback Hell

```typescript
// BAD - Pyramid of doom
fetchUser(id, (user) => {
  fetchPosts(user.id, (posts) => {
    fetchComments(posts[0].id, (comments) => {
      console.log(comments);
    });
  });
});

// GOOD - Async/await
async function loadData(id: string) {
  const user = await fetchUser(id);
  const posts = await fetchPosts(user.id);
  const comments = await fetchComments(posts[0].id);
  return comments;
}
```

## Enum with String Values as Union

```typescript
// BAD - Enums have runtime overhead
enum Status {
  Active = "active",
  Inactive = "inactive",
  Pending = "pending",
}

// GOOD - Const object with as const
const Status = {
  Active: "active",
  Inactive: "inactive",
  Pending: "pending",
} as const;

type Status = (typeof Status)[keyof typeof Status];
```

## Ignoring Promise Rejections

```typescript
// BAD - Unhandled rejection
async function save() {
  await database.save(data); // Error swallowed
}
save();

// GOOD - Handle errors
async function save() {
  try {
    await database.save(data);
  } catch (error) {
    logger.error("Save failed", error);
    throw error;
  }
}

// ALSO GOOD - Use void operator for intentional fire-and-forget
void save().catch(console.error);
```

## Mutating Function Parameters

```typescript
// BAD - Side effects
function addItem(items: string[], item: string): string[] {
  items.push(item); // Mutates original!
  return items;
}

// GOOD - Return new array
function addItem(items: readonly string[], item: string): string[] {
  return [...items, item];
}
```

## Object Spread for Deep Clone

```typescript
// BAD - Only shallow copy
const copy = { ...original };
copy.nested.value = "changed"; // Mutates original!

// GOOD - Deep clone with structuredClone
const copy = structuredClone(original);

// ALSO GOOD - Immutable updates with spread
const updated = {
  ...original,
  nested: {
    ...original.nested,
    value: "changed",
  },
};
```

## Checking Array Length Wrong

```typescript
// BAD - Falsy check fails for empty array
if (items) {
  // Still runs for empty array []
  processItems(items);
}

// GOOD - Check length explicitly
if (items.length > 0) {
  processItems(items);
}

// ALSO GOOD - Use optional chaining
if (items?.length) {
  processItems(items);
}
```

## instanceof with Primitives

```typescript
// BAD - Doesn't work for primitives
const str = "hello";
if (str instanceof String) {
  // False! Primitives aren't objects
}

// GOOD - Use typeof for primitives
if (typeof str === "string") {
  // Works correctly
}
```

## Loose Equality

```typescript
// BAD - Type coercion surprises
if (value == null) {
  // Matches both null AND undefined
}
if (value == 0) {
  // Matches 0, "", false, null...
}

// GOOD - Strict equality
if (value === null || value === undefined) {
  // Explicit
}
if (value === 0) {
  // Only matches 0
}

// Exception: == null is acceptable for null/undefined check
if (value == null) {
  // This is actually a common pattern
}
```

## Not Using const for Immutable References

```typescript
// BAD - let when value never changes
let config = loadConfig();
let PI = 3.14159;

// GOOD - const for immutable bindings
const config = loadConfig();
const PI = 3.14159;
```

## String-based Property Access

```typescript
// BAD - No type safety
const value = obj["propertyName"];

// GOOD - Dot notation with type safety
const value = obj.propertyName;

// When dynamic access is needed, use keyof
function getValue<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

## Throwing Non-Error Objects

```typescript
// BAD - Loses stack trace
throw "Something went wrong";
throw { message: "Error" };

// GOOD - Throw Error instances
throw new Error("Something went wrong");

// BETTER - Custom error classes
class ValidationError extends Error {
  constructor(
    message: string,
    public field: string
  ) {
    super(message);
    this.name = "ValidationError";
  }
}
```

## Using Index Signatures Liberally

```typescript
// BAD - Loses type safety
interface Config {
  [key: string]: any;
}

// GOOD - Explicit properties with optional
interface Config {
  apiUrl: string;
  timeout?: number;
  retries?: number;
}

// When needed, use Record with specific types
type FeatureFlags = Record<string, boolean>;
```

## Not Using Discriminated Unions

```typescript
// BAD - Hard to narrow types
interface Response {
  success: boolean;
  data?: Data;
  error?: string;
}

// GOOD - Discriminated union
type Response = { success: true; data: Data } | { success: false; error: string };

function handle(response: Response) {
  if (response.success) {
    // TypeScript knows data exists
    console.log(response.data);
  } else {
    // TypeScript knows error exists
    console.log(response.error);
  }
}
```
