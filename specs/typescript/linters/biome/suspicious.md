# Biome Suspicious Rules

Rules that detect patterns that are likely bugs.

## noApproximativeNumericConstant

Use Math constants instead of approximations.

```typescript
// BAD
const pi = 3.14159;
const e = 2.718;

// GOOD
const pi = Math.PI;
const e = Math.E;
```

## noArrayIndexKey

Covered in correctness.

## noAssignInExpressions

Prevent accidental assignment in expressions.

```typescript
// BAD
if (x = 1) {}  // probably meant ===

// GOOD
if (x === 1) {}

// If intentional, be explicit
if ((x = getValue())) {}
```

## noAsyncPromiseExecutor

Promise executor shouldn't be async.

```typescript
// BAD
new Promise(async (resolve) => {
  await something();
  resolve();
});

// GOOD
new Promise((resolve) => {
  something().then(resolve);
});
```

## noCatchAssign

Don't reassign catch parameter.

```typescript
// BAD
try {
  // ...
} catch (e) {
  e = new Error("replaced");  // don't do this
}

// GOOD
try {
  // ...
} catch (e) {
  const wrapped = new Error("context", { cause: e });
  throw wrapped;
}
```

## noClassAssign

Don't reassign class declarations.

```typescript
// BAD
class Foo {}
Foo = 1;

// GOOD - use a variable if needed
let FooClass = class {};
FooClass = class {};
```

## noCommentText

Prevent comment-like text in JSX.

```tsx
// BAD
<div>/* comment */</div>
<div>// comment</div>

// GOOD
<div>{/* comment */}</div>
```

## noCompareNegZero

Comparing to -0 is almost always wrong.

```typescript
// BAD
if (x === -0) {}

// GOOD
if (Object.is(x, -0)) {}
```

## noConfusingLabels

Labels shouldn't conflict with scope.

```typescript
// BAD
function foo() {
  foo: {}  // same name as function
}
```

## noConfusingVoidType

void is only for return types.

```typescript
// BAD
const fn: () => void | number = () => {};

// GOOD
const fn: () => void = () => {};
const fn: () => undefined | number = () => undefined;
```

## noConsole

Don't leave console statements.

```typescript
// BAD
console.log("debug");

// GOOD
console.error("Error occurred");  // OK
console.warn("Warning");          // OK

// Or use a logger
logger.debug("debug");
```

Configuration:
```json
{
  "suspicious": {
    "noConsole": {
      "level": "warn",
      "options": {
        "allow": ["warn", "error", "info", "debug"]
      }
    }
  }
}
```

## noConstEnum

Avoid const enum (can't be used with isolatedModules).

```typescript
// BAD
const enum Color { Red, Green, Blue }

// GOOD
enum Color { Red, Green, Blue }
// Or use string literals
type Color = "red" | "green" | "blue";
```

## noControlCharactersInRegex

Prevent control characters in regex.

```typescript
// BAD
const re = /\x00/;

// GOOD
const re = /\0/;  // null character if needed
```

## noDebugger

Remove debugger statements.

```typescript
// BAD
debugger;

// Remove it
```

## noDoubleEquals

Use strict equality.

```typescript
// BAD
if (x == y) {}
if (x != y) {}

// GOOD
if (x === y) {}
if (x !== y) {}
```

## noDuplicateCase

Prevent duplicate switch cases.

## noDuplicateClassMembers

Prevent duplicate class members.

```typescript
// BAD
class Foo {
  bar() {}
  bar() {}  // duplicate!
}
```

## noDuplicateJsxProps

Prevent duplicate JSX props.

```tsx
// BAD
<div id="a" id="b" />

// GOOD
<div id="a" />
```

## noDuplicateObjectKeys

Prevent duplicate object keys.

```typescript
// BAD
const obj = { a: 1, a: 2 };

// GOOD
const obj = { a: 1, b: 2 };
```

## noDuplicateParameters

Prevent duplicate function parameters.

```typescript
// BAD
function foo(a, a) {}

// GOOD
function foo(a, b) {}
```

## noEmptyBlockStatements

Prevent empty blocks.

```typescript
// BAD
if (x) {
}

// GOOD
if (x) {
  // intentionally empty
}
```

## noEmptyInterface

Prevent empty interfaces.

```typescript
// BAD
interface Empty {}

// GOOD
interface WithMember {
  member: string;
}

// Or use type
type Empty = Record<string, never>;
```

## noExplicitAny

Don't use any type.

```typescript
// BAD
const data: any = response;
function fn(x: any): any {}

// GOOD
const data: unknown = response;
function fn(x: unknown): string {}

// Or be specific
interface Data {
  items: Item[];
}
const data: Data = response;
```

## noExportsInTest

Don't export from test files.

```typescript
// BAD (in .test.ts)
export function helper() {}

// GOOD - keep test helpers in test file or separate non-test module
```

## noExtraNonNullAssertion

Remove redundant non-null assertions.

```typescript
// BAD
x!!!;
x!?.y;

// GOOD
x!;
x?.y;
```

## noFallthroughSwitchClause

Prevent unintentional fallthrough.

```typescript
// BAD
switch (x) {
  case 1:
    doSomething();
  case 2:  // falls through!
    doMore();
}

// GOOD
switch (x) {
  case 1:
    doSomething();
    break;
  case 2:
    doMore();
}

// Or explicit fallthrough comment
switch (x) {
  case 1:
    doSomething();
    // fallthrough
  case 2:
    doMore();
}
```

## noFunctionAssign

Don't reassign function declarations.

```typescript
// BAD
function foo() {}
foo = 1;
```

## noGlobalAssign

Don't reassign globals.

```typescript
// BAD
undefined = 1;
Object = null;
```

## noGlobalIsFinite

Use Number.isFinite instead.

```typescript
// BAD
isFinite("1");  // coerces to number

// GOOD
Number.isFinite(1);
```

## noGlobalIsNan

Use Number.isNaN instead.

```typescript
// BAD
isNaN("x");  // coerces

// GOOD
Number.isNaN(x);
```

## noImplicitAnyLet

Require type on let without initializer.

```typescript
// BAD
let x;  // implicitly any

// GOOD
let x: string;
let x = "";
```

## noImportAssign

Don't reassign imports.

```typescript
// BAD
import { foo } from "mod";
foo = 1;
```

## noLabelVar

Labels shouldn't match variable names.

```typescript
// BAD
const x = 1;
x: {}
```

## noMisleadingCharacterClass

Prevent confusing regex character classes.

## noMisleadingInstantiation

Use `new` properly.

```typescript
// BAD
new Symbol();

// GOOD
Symbol("desc");
```

## noMisrefactoredShorthandAssign

Prevent confusing compound assignment.

```typescript
// BAD
x = x ?? 1;  // probably meant ??=

// GOOD
x ??= 1;
```

## noPrototypeBuiltins

Don't call Object prototype methods directly.

```typescript
// BAD
obj.hasOwnProperty("foo");

// GOOD
Object.hasOwn(obj, "foo");
Object.prototype.hasOwnProperty.call(obj, "foo");
```

## noRedeclare

Prevent redeclaring variables.

```typescript
// BAD
var x = 1;
var x = 2;

// GOOD
let x = 1;
x = 2;
```

## noRedundantUseStrict

Remove redundant "use strict".

```typescript
// BAD (in ESM or already-strict context)
"use strict";

// Just remove it - ESM is always strict
```

## noSelfCompare

Prevent comparing value to itself.

```typescript
// BAD
if (x === x) {}  // always true (except NaN)

// If checking for NaN, use:
if (Number.isNaN(x)) {}
```

## noShadowRestrictedNames

Don't shadow restricted names.

```typescript
// BAD
const undefined = 1;
const NaN = 2;
function eval() {}
```

## noSparseArray

Prevent sparse arrays.

```typescript
// BAD
const arr = [1, , 3];  // sparse

// GOOD
const arr = [1, undefined, 3];
```

## noThenProperty

Avoid 'then' property (confuses async).

```typescript
// BAD
const obj = {
  then: () => {}
};
await obj;  // calls obj.then!

// GOOD
const obj = {
  resolve: () => {}
};
```

## noUnsafeDeclarationMerging

Prevent declaration merging issues.

```typescript
// BAD
interface Foo {
  x: string;
}
class Foo {  // merges with interface
  y: number;
}
```

## noUnsafeNegation

Prevent confusing negation.

```typescript
// BAD
if (!x in obj) {}  // negates x, not result

// GOOD
if (!(x in obj)) {}
```

## useAwait

Async functions must use await.

```typescript
// BAD
async function foo() {
  return 1;  // no await
}

// GOOD
async function foo() {
  return await getValue();
}

// Or don't make it async
function foo() {
  return 1;
}
```

## useDefaultSwitchClauseLast

default case should be last.

```typescript
// BAD
switch (x) {
  default:
    break;
  case 1:
    break;
}

// GOOD
switch (x) {
  case 1:
    break;
  default:
    break;
}
```

## useGetterReturn

Getters must return a value.

```typescript
// BAD
const obj = {
  get foo() {
    // no return!
  }
};

// GOOD
const obj = {
  get foo() {
    return this._foo;
  }
};
```

## useIsArray

Use Array.isArray not instanceof.

```typescript
// BAD
if (x instanceof Array) {}

// GOOD
if (Array.isArray(x)) {}
```

## useNamespaceKeyword

Use namespace not module.

```typescript
// BAD
module Foo {}

// GOOD
namespace Foo {}
```

## useValidTypeof

Validate typeof comparisons.

```typescript
// BAD
typeof x === "nunber";  // typo
typeof x === "null";    // typeof returns "object" for null

// GOOD
typeof x === "number";
x === null;
```
