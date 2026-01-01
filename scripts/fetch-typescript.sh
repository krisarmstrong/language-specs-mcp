#!/bin/bash
# Fetch TypeScript specs from authoritative sources

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/typescript"

echo "=== Fetching TypeScript Specs ==="

mkdir -p "$SPECS_DIR"/{lib,linters/biome,formatters,patterns}

# TypeScript handbook (main reference since spec is archived)
echo "Fetching TypeScript handbook..."
HANDBOOK_PAGES="basic-types interfaces functions classes generics enums type-inference type-compatibility"

for page in $HANDBOOK_PAGES; do
  echo "  - $page"
  curl -sL "https://www.typescriptlang.org/docs/handbook/$page.html" | \
    pandoc -f html -t markdown -o "$SPECS_DIR/lib/$page.md" 2>/dev/null || \
    echo "# $page\n\nSee: https://www.typescriptlang.org/docs/handbook/$page.html" > "$SPECS_DIR/lib/$page.md"
done

# Core TypeScript patterns
cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
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
EOF

# TypeScript formatters
cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# TypeScript Formatters

## Prettier

See: https://prettier.io/docs/en/

## Biome Format

See: https://biomejs.dev/formatter/
EOF

cat > "$SPECS_DIR/formatters/prettier.md" << 'EOF'
# Prettier Options

See: https://prettier.io/docs/en/options.html
EOF

cat > "$SPECS_DIR/formatters/biome.md" << 'EOF'
# Biome Formatter Options

See: https://biomejs.dev/formatter/
EOF

# Biome rules
echo "Fetching Biome rule docs..."
cat > "$SPECS_DIR/linters/biome/noExplicitAny.md" << 'EOF'
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
EOF

cat > "$SPECS_DIR/linters/biome/noNonNullAssertion.md" << 'EOF'
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
EOF

BIOME_RULES=$(curl -sL "https://biomejs.dev/linter/rules/" | \
  grep -oE '/linter/rules/[a-z0-9-]+' | \
  sed 's#.*/##' | sort -u)

for rule in $BIOME_RULES; do
  echo "  - biome/$rule"
  curl -sL "https://biomejs.dev/linter/rules/${rule}/" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/biome/${rule}.md" 2>/dev/null || \
    echo "# ${rule}\n\nSee: https://biomejs.dev/linter/rules/${rule}/" > "$SPECS_DIR/linters/biome/${rule}.md"
done

cat > "$SPECS_DIR/linters/biome/noUnusedVariables.md" << 'EOF'
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
EOF

cat > "$SPECS_DIR/linters/biome/noConsole.md" << 'EOF'
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
EOF

echo "=== TypeScript specs complete ==="
