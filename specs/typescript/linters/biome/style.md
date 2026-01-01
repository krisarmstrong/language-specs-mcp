# Biome Style Rules

Rules that enforce consistent code style.

## noArguments

Use rest parameters instead of arguments.

```typescript
// BAD
function foo() {
  console.log(arguments);
}

// GOOD
function foo(...args: unknown[]) {
  console.log(args);
}
```

## noCommaOperator

Prevent comma operator.

```typescript
// BAD
const x = (1, 2, 3);  // x = 3, confusing

// GOOD
const x = 3;
```

## noDefaultExport

Prefer named exports.

```typescript
// BAD
export default function foo() {}

// GOOD
export function foo() {}
```

## noImplicitBoolean

Require explicit boolean in JSX.

```tsx
// BAD
<Input disabled />

// GOOD
<Input disabled={true} />
```

## noInferrableTypes

Remove obvious type annotations.

```typescript
// BAD
const x: number = 1;
const s: string = "hello";

// GOOD
const x = 1;
const s = "hello";

// Keep when not inferrable
const x: number = getValue();
```

## noNamespace

Avoid TypeScript namespaces.

```typescript
// BAD
namespace Foo {
  export const x = 1;
}

// GOOD
export const x = 1;
// Or use modules
```

## noNegationElse

Avoid negated conditions with else.

```typescript
// BAD
if (!condition) {
  foo();
} else {
  bar();
}

// GOOD
if (condition) {
  bar();
} else {
  foo();
}
```

## noNonNullAssertion

Avoid non-null assertions.

```typescript
// BAD
const x = obj.maybeNull!;
func()!;

// GOOD
if (obj.maybeNull) {
  const x = obj.maybeNull;
}

// Or use optional chaining
const x = obj.maybeNull ?? defaultValue;
```

## noParameterAssign

Don't reassign parameters.

```typescript
// BAD
function foo(x: number) {
  x = x + 1;  // modifies parameter
  return x;
}

// GOOD
function foo(x: number) {
  const result = x + 1;
  return result;
}
```

## noParameterProperties

Avoid parameter properties.

```typescript
// BAD
class Foo {
  constructor(private x: number) {}
}

// GOOD
class Foo {
  private x: number;
  constructor(x: number) {
    this.x = x;
  }
}
```

## noRestrictedGlobals

Ban specific global variables.

```typescript
// Configurable - can ban things like:
event;    // use event parameter instead
name;     // shadows window.name
length;   // confusing
```

## noShoutyConstants

Avoid all-caps for non-constants.

```typescript
// BAD
let MUTABLE_VALUE = 1;
MUTABLE_VALUE = 2;

// GOOD
const CONSTANT_VALUE = 1;
let mutableValue = 2;
```

## noUnusedTemplateLiteral

Use string when template isn't needed.

```typescript
// BAD
const s = `no interpolation`;

// GOOD
const s = "no interpolation";

// OK - has interpolation
const s = `Hello ${name}`;
```

## noUselessElse

Remove unnecessary else.

```typescript
// BAD
function foo() {
  if (x) {
    return 1;
  } else {
    return 2;
  }
}

// GOOD
function foo() {
  if (x) {
    return 1;
  }
  return 2;
}
```

## noVar

Use let/const instead of var.

```typescript
// BAD
var x = 1;

// GOOD
const x = 1;
let y = 2;
```

## useAsConstAssertion

Use as const for literal types.

```typescript
// BAD
const x = { a: 1 } as { a: 1 };

// GOOD
const x = { a: 1 } as const;
```

## useBlockStatements

Require braces for control statements.

```typescript
// BAD
if (x) doSomething();
for (const x of arr) process(x);

// GOOD
if (x) {
  doSomething();
}
for (const x of arr) {
  process(x);
}
```

## useCollapsedElseIf

Use else if not else { if.

```typescript
// BAD
if (a) {
} else {
  if (b) {
  }
}

// GOOD
if (a) {
} else if (b) {
}
```

## useConst

Use const when variable isn't reassigned.

```typescript
// BAD
let x = 1;
console.log(x);  // x never reassigned

// GOOD
const x = 1;
console.log(x);
```

## useDefaultParameterLast

Default parameters should be last.

```typescript
// BAD
function foo(a = 1, b: number) {}

// GOOD
function foo(b: number, a = 1) {}
```

## useEnumInitializers

Require explicit enum values.

```typescript
// BAD
enum Color {
  Red,    // 0
  Green,  // 1
  Blue,   // 2
}

// GOOD
enum Color {
  Red = 0,
  Green = 1,
  Blue = 2,
}

// Or string enum
enum Color {
  Red = "red",
  Green = "green",
  Blue = "blue",
}
```

## useExponentiationOperator

Use ** instead of Math.pow.

```typescript
// BAD
Math.pow(2, 3);

// GOOD
2 ** 3;
```

## useExportType

Use export type for type-only exports.

```typescript
// BAD
export { MyType } from "./types";

// GOOD
export type { MyType } from "./types";
```

## useFilenamingConvention

Enforce file naming conventions.

```
// BAD
MyComponent.tsx
my_component.tsx

// GOOD (with camelCase config)
myComponent.tsx

// GOOD (with kebab-case config)
my-component.tsx
```

## useForOf

Use for-of instead of for loop.

```typescript
// BAD
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// GOOD
for (const item of arr) {
  console.log(item);
}
```

## useFragmentSyntax

Use <> instead of <Fragment>.

```tsx
// BAD
<Fragment>
  <Child />
</Fragment>

// GOOD
<>
  <Child />
</>
```

## useImportType

Use import type for type-only imports.

```typescript
// BAD
import { MyType } from "./types";

// GOOD
import type { MyType } from "./types";

// Mixed
import { getValue, type MyType } from "./module";
```

## useLiteralEnumMembers

Enum members should be literals.

```typescript
// BAD
const value = 1;
enum Foo {
  A = value,  // computed
}

// GOOD
enum Foo {
  A = 1,
  B = "b",
}
```

## useNamingConvention

Enforce naming conventions.

```typescript
// Default conventions:
class PascalCase {}
interface IPascalCase {}  // or without I
type PascalCase = {};
const camelCase = 1;
const SCREAMING_SNAKE_CASE = 1;  // const
function camelCase() {}
```

## useNodejsImportProtocol

Use node: protocol for Node imports.

```typescript
// BAD
import fs from "fs";
import path from "path";

// GOOD
import fs from "node:fs";
import path from "node:path";
```

## useNumberNamespace

Use Number methods instead of globals.

```typescript
// BAD
parseInt("10");
parseFloat("3.14");
isNaN(x);
isFinite(x);

// GOOD
Number.parseInt("10");
Number.parseFloat("3.14");
Number.isNaN(x);
Number.isFinite(x);
```

## useNumericLiterals

Use numeric literals not parseInt.

```typescript
// BAD
parseInt("10", 2);   // binary
parseInt("10", 8);   // octal
parseInt("10", 16);  // hex

// GOOD
0b10;  // binary
0o10;  // octal
0x10;  // hex
```

## useSelfClosingElements

Self-close empty elements.

```tsx
// BAD
<div></div>
<Component></Component>

// GOOD
<div />
<Component />
```

## useShorthandArrayType

Use T[] not Array<T>.

```typescript
// BAD
const arr: Array<string> = [];

// GOOD
const arr: string[] = [];

// OK for complex types
const arr: Array<string | number> = [];
```

## useShorthandAssign

Use compound assignment.

```typescript
// BAD
x = x + 1;
x = x * 2;
x = x ?? default;

// GOOD
x += 1;  // or x++
x *= 2;
x ??= default;
```

## useShorthandFunctionType

Use function type shorthand.

```typescript
// BAD
interface Func {
  (): void;
}

// GOOD
type Func = () => void;
```

## useSingleCaseStatement

Group single-case switches.

```typescript
// BAD
switch (x) {
  case 1:
    break;
}

// GOOD
if (x === 1) {
  // ...
}
```

## useSingleVarDeclarator

One variable per declaration.

```typescript
// BAD
let a = 1, b = 2, c = 3;

// GOOD
let a = 1;
let b = 2;
let c = 3;
```

## useTemplate

Use template literals for concatenation.

```typescript
// BAD
const s = "Hello " + name + "!";

// GOOD
const s = `Hello ${name}!`;
```

## useWhile

Use while for simple loops.

```typescript
// BAD
for (; condition; ) {
  doSomething();
}

// GOOD
while (condition) {
  doSomething();
}
```
