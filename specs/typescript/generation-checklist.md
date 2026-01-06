# TypeScript/JavaScript Generation Checklist

**Read this BEFORE writing TS/JS code. These rules prevent the most common bugs.**

## Critical: You Must Do These

### 1. Use `const` by Default, `let` When Needed, Never `var`
```typescript
// BAD - hoisting issues, function-scoped
var count = 0;

// GOOD - block-scoped, immutable binding
const config = { port: 3000 };

// GOOD - when reassignment needed
let counter = 0;
counter++;
```

### 2. Use `===` and `!==`, Never `==` or `!=`
```typescript
// BAD - type coercion surprises
if (x == null)
if (count == "5")

// GOOD - strict equality
if (x === null || x === undefined)
if (count === 5)
```

### 3. Always Handle Promise Rejections
```typescript
// BAD - unhandled rejection
fetchData();

// GOOD - handle errors
try {
    await fetchData();
} catch (error) {
    console.error("Fetch failed:", error);
}

// Or with .catch()
fetchData().catch(handleError);
```

### 4. Use Optional Chaining and Nullish Coalescing
```typescript
// BAD - verbose null checks
const name = user && user.profile && user.profile.name;
const port = config.port !== undefined ? config.port : 3000;

// GOOD - modern syntax
const name = user?.profile?.name;
const port = config.port ?? 3000;
```

### 5. Avoid `any` - Use `unknown` for Unknown Types
```typescript
// BAD - disables type checking
function process(data: any) {
    return data.foo.bar;  // No error, but might crash
}

// GOOD - forces type checking
function process(data: unknown) {
    if (isValidData(data)) {
        return data.foo.bar;  // Type-safe after guard
    }
}
```

## Important: Strong Recommendations

### 6. Use `readonly` for Immutable Data
```typescript
// BAD - can be mutated
interface Config {
    apiUrl: string;
    timeout: number;
}

// GOOD - prevents accidental mutation
interface Config {
    readonly apiUrl: string;
    readonly timeout: number;
}
```

### 7. Prefer `Array.prototype` Methods Over Loops
```typescript
// BAD - imperative, error-prone
const results = [];
for (let i = 0; i < items.length; i++) {
    if (items[i].active) {
        results.push(items[i].name);
    }
}

// GOOD - declarative, chainable
const results = items
    .filter(item => item.active)
    .map(item => item.name);
```

### 8. Use Template Literals for String Building
```typescript
// BAD - hard to read
const msg = "Hello, " + name + "! You have " + count + " messages.";

// GOOD - readable
const msg = `Hello, ${name}! You have ${count} messages.`;
```

### 9. Destructure Objects and Arrays
```typescript
// BAD - repetitive
const name = user.name;
const email = user.email;
const first = items[0];

// GOOD - concise
const { name, email } = user;
const [first] = items;
```

### 10. Use Type Guards for Narrowing
```typescript
// BAD - type assertion (unsafe)
const name = (data as User).name;

// GOOD - type guard (safe)
function isUser(data: unknown): data is User {
    return typeof data === "object" && data !== null && "name" in data;
}

if (isUser(data)) {
    const name = data.name;  // Safe
}
```

## Async: Get It Right

### 11. Prefer async/await Over .then() Chains
```typescript
// BAD - callback pyramid
fetchUser()
    .then(user => fetchOrders(user.id))
    .then(orders => processOrders(orders))
    .catch(handleError);

// GOOD - linear flow
try {
    const user = await fetchUser();
    const orders = await fetchOrders(user.id);
    await processOrders(orders);
} catch (error) {
    handleError(error);
}
```

### 12. Use Promise.all for Concurrent Operations
```typescript
// BAD - sequential when could be parallel
const user = await fetchUser();
const orders = await fetchOrders();
const settings = await fetchSettings();

// GOOD - parallel execution
const [user, orders, settings] = await Promise.all([
    fetchUser(),
    fetchOrders(),
    fetchSettings(),
]);
```

### 13. Don't Return Await in Try Block (Unless Needed)
```typescript
// UNNECESSARY - extra microtask
async function getData() {
    try {
        return await fetch(url);
    } catch (e) {
        // This is fine - catch needs await
    }
}

// But without catch, just return the promise:
async function getData() {
    return fetch(url);  // No await needed
}
```

## Security: Never Do These

### 14. Never Insert User Input as HTML
Use `element.textContent` for plain text display.
If HTML rendering is required, sanitize with DOMPurify first.
See ESLint: no-unsanitized/property

### 15. Never Build URLs with String Concatenation
```typescript
// DANGEROUS - injection risk
const url = `/api/users/${userId}`;

// SAFE - use URL API
const url = new URL(`/api/users/${encodeURIComponent(userId)}`, baseUrl);
```

### 16. Never Dynamically Construct Code from User Input
Avoid any pattern that interprets strings as executable code.
See ESLint: no-implied-eval, no-new-func

## TypeScript-Specific

### 17. Enable Strict Mode in tsconfig.json
```json
{
    "compilerOptions": {
        "strict": true
    }
}
```

### 18. Prefer Interfaces for Object Shapes, Types for Unions
```typescript
// GOOD - interface for objects (extensible)
interface User {
    name: string;
    email: string;
}

// GOOD - type for unions/computed
type Status = "pending" | "active" | "closed";
type Nullable<T> = T | null;
```

### 19. Use `satisfies` for Type Checking Without Widening
```typescript
// Type is widened to Record<string, string>
const routes: Record<string, string> = {
    home: "/",
    about: "/about",
};

// Type is preserved as { home: string; about: string }
const routes = {
    home: "/",
    about: "/about",
} satisfies Record<string, string>;
```

---

**Quick Reference - Copy This Mental Model:**
- `const` > `let` > never `var`
- `===` always, never `==`
- Handle all Promise rejections
- `?.` and `??` for null safety
- `unknown` > `any`
- `readonly` for immutable data
- Array methods > loops
- async/await > .then chains
- Never insert user input as HTML
- Enable `"strict": true`
