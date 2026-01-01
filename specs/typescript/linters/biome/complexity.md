# Biome Complexity Rules

Rules that reduce cognitive complexity.

## noBannedTypes

Avoid problematic types.

```typescript
// BAD
const a: Object = {};     // use object or {}
const b: String = "";     // use string
const c: Number = 1;      // use number
const d: Boolean = true;  // use boolean
const e: Function = fn;   // use specific function type
const f: {} = {};         // use object or Record

// GOOD
const a: object = {};
const b: string = "";
const c: number = 1;
const d: boolean = true;
const e: () => void = fn;
const f: Record<string, unknown> = {};
```

## noExcessiveCognitiveComplexity

Limit cognitive complexity of functions.

```typescript
// BAD - too complex
function process(items) {
  for (const item of items) {           // +1
    if (item.active) {                  // +2 (nested)
      for (const sub of item.subs) {    // +3 (nested)
        if (sub.valid) {                // +4 (nested)
          if (sub.type === "a") {       // +5 (nested)
            // ...
          } else if (sub.type === "b") { // +1
            // ...
          }
        }
      }
    }
  }
}  // complexity: 16+

// GOOD - extract functions
function processItem(item: Item): void {
  if (!item.active) return;
  for (const sub of item.subs) {
    processSub(sub);
  }
}

function processSub(sub: Sub): void {
  if (!sub.valid) return;
  handleSubByType(sub);
}

function handleSubByType(sub: Sub): void {
  switch (sub.type) {
    case "a":
      // ...
      break;
    case "b":
      // ...
      break;
  }
}
```

Configuration:
```json
{
  "complexity": {
    "noExcessiveCognitiveComplexity": {
      "level": "error",
      "options": {
        "maxAllowedComplexity": 15
      }
    }
  }
}
```

## noExcessiveNestedTestSuites

Limit nesting in test suites.

```typescript
// BAD
describe("A", () => {
  describe("B", () => {
    describe("C", () => {
      describe("D", () => {
        describe("E", () => {
          it("works", () => {});
        });
      });
    });
  });
});

// GOOD - flatten
describe("A > B > C", () => {
  it("works for D > E case", () => {});
});
```

## noForEach

Use for-of instead of forEach.

```typescript
// BAD
items.forEach((item) => {
  process(item);
});

// GOOD
for (const item of items) {
  process(item);
}
```

**Why:**
1. Can't use break/continue
2. Can't await properly
3. Harder to debug

```typescript
// forEach breaks with async
items.forEach(async (item) => {
  await process(item);  // doesn't wait!
});

// for-of works correctly
for (const item of items) {
  await process(item);  // waits properly
}
```

## noStaticOnlyClass

Avoid classes with only static members.

```typescript
// BAD
class Utils {
  static helper() {}
  static other() {}
}

// GOOD - use module/namespace
export function helper() {}
export function other() {}

// Or use object
export const Utils = {
  helper() {},
  other() {},
};
```

## noThisInStatic

Don't use this in static methods.

```typescript
// BAD
class Foo {
  static bar() {
    return this.baz;  // confusing
  }
}

// GOOD
class Foo {
  static bar() {
    return Foo.baz;  // explicit
  }
}
```

## noUselessCatch

Remove useless catch blocks.

```typescript
// BAD
try {
  doSomething();
} catch (e) {
  throw e;  // useless
}

// GOOD - just remove try/catch
doSomething();

// Or add value
try {
  doSomething();
} catch (e) {
  log(e);
  throw e;
}
```

## noUselessConstructor

Remove empty constructors.

```typescript
// BAD
class Foo {
  constructor() {}
}

class Bar extends Baz {
  constructor(...args) {
    super(...args);
  }
}

// GOOD - remove constructor
class Foo {}

class Bar extends Baz {}
```

## noUselessEmptyExport

Remove useless empty export.

```typescript
// BAD
export {};  // not needed if other exports exist

export function foo() {}

// GOOD
export function foo() {}
```

## noUselessFragments

Remove unnecessary React fragments.

```tsx
// BAD
<>{children}</>
<><Child /></>

// GOOD
{children}
<Child />

// OK - multiple children need fragment
<>
  <Child1 />
  <Child2 />
</>
```

## noUselessLabel

Remove useless labels.

```typescript
// BAD
foo: for (const x of arr) {
  break;  // doesn't use label
}

// GOOD - remove label
for (const x of arr) {
  break;
}

// OK - label is used
outer: for (const x of arr) {
  for (const y of x) {
    break outer;  // breaks outer loop
  }
}
```

## noUselessLoneBlockStatements

Remove useless blocks.

```typescript
// BAD
{
  const x = 1;
}

// GOOD - remove block unless scoping needed
const x = 1;
```

## noUselessRename

Remove useless rename in import/export.

```typescript
// BAD
import { foo as foo } from "mod";
export { bar as bar };

// GOOD
import { foo } from "mod";
export { bar };
```

## noUselessSwitchCase

Remove useless switch case.

```typescript
// BAD
switch (x) {
  case 1:
    break;
  default:
    break;  // useless, can just remove switch
}

// If only default, use if or nothing
```

## noUselessTernary

Remove useless ternary.

```typescript
// BAD
const x = condition ? true : false;
const y = condition ? false : true;

// GOOD
const x = condition;
const y = !condition;
```

## noUselessThisAlias

Remove useless this alias.

```typescript
// BAD
const self = this;
self.method();

// GOOD
this.method();

// OK - needed for closure
const self = this;
function callback() {
  self.method();
}
```

## noUselessTypeConstraint

Remove useless type constraints.

```typescript
// BAD
function foo<T extends unknown>() {}
function bar<T extends any>() {}

// GOOD
function foo<T>() {}
function bar<T>() {}
```

## noVoid

Avoid void operator.

```typescript
// BAD
void 0;
void doSomething();

// GOOD
undefined;
doSomething();
```

## noWith

Prevent with statement.

```typescript
// BAD
with (obj) {
  foo;  // confusing scope
}

// GOOD
obj.foo;
```

## useFlatMap

Use flatMap instead of map().flat().

```typescript
// BAD
arr.map(x => x.items).flat();

// GOOD
arr.flatMap(x => x.items);
```

## useLiteralKeys

Use literal keys when possible.

```typescript
// BAD
obj["property"];

// GOOD
obj.property;

// OK - dynamic key
obj[variableKey];
```

## useOptionalChain

Use optional chaining.

```typescript
// BAD
foo && foo.bar;
foo && foo.bar && foo.bar.baz;
foo != null && foo.bar;

// GOOD
foo?.bar;
foo?.bar?.baz;
```

## useRegexLiterals

Use regex literals not RegExp constructor.

```typescript
// BAD
new RegExp("\\d+");

// GOOD
/\d+/;

// OK - dynamic pattern
new RegExp(pattern);
```

## useSimpleNumberKeys

Use number keys not string.

```typescript
// BAD
const obj = { "1": "one", "2": "two" };

// GOOD
const obj = { 1: "one", 2: "two" };
```

## useSimplifiedLogicExpression

Simplify logic expressions.

```typescript
// BAD
!!value;
!(!value);
x && x;

// GOOD
Boolean(value);
value;
x;
```
