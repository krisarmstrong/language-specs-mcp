# Biome Nursery Lints

Experimental rules that may be promoted to stable categories.

## noApproximativeNumericConstant

Avoid approximating built-in math constants.

```typescript
// BAD
const pi = 3.14159;
const e = 2.71828;

// GOOD
const pi = Math.PI;
const e = Math.E;
```

## noCommonJs

Disallow CommonJS require/exports.

```typescript
// BAD
const fs = require("fs");
module.exports = { foo };

// GOOD
import fs from "node:fs";
export { foo };
```

## noConstantMathMinMaxClamp

Avoid Math.min/max with constant that clamps nothing.

```typescript
// BAD
Math.max(0, -5);  // always 0
Math.min(100, 200);  // always 100

// GOOD - dynamic values
Math.max(0, userInput);
Math.min(100, value);
```

## noDuplicateElseIf

No duplicate conditions in else-if.

```typescript
// BAD
if (a) {
} else if (b) {
} else if (a) {  // duplicate!
}

// GOOD
if (a) {
} else if (b) {
} else if (c) {
}
```

## noDuplicateJsonKeys

No duplicate keys in JSON.

```json
// BAD
{
  "name": "foo",
  "name": "bar"
}

// GOOD
{
  "name": "foo"
}
```

## noEmptyBlockStatements

No empty block statements.

```typescript
// BAD
if (condition) {
}

try {
} catch (e) {
}

// GOOD
if (condition) {
  doSomething();
}

try {
  riskyOp();
} catch (e) {
  handleError(e);
}
```

## noEvolvingTypes

Disallow variables that evolve type through reassignment.

```typescript
// BAD
let x = 1;      // number
x = "hello";    // now string!

// GOOD
let x: number | string = 1;
x = "hello";
```

## noExcessiveNestedTestSuites

Limit test suite nesting depth.

```typescript
// BAD
describe("a", () => {
  describe("b", () => {
    describe("c", () => {
      describe("d", () => {
        describe("e", () => {  // too deep
          it("test", () => {});
        });
      });
    });
  });
});

// GOOD - flatten
describe("a > b > c", () => {
  it("test case", () => {});
});
```

## noFlatMapIdentity

No flatMap with identity function.

```typescript
// BAD
arr.flatMap(x => x);

// GOOD
arr.flat();
```

## noGlobalAssign

No assigning to global objects.

```typescript
// BAD
Object = null;
Array = class {};
window = {};

// GOOD - don't modify globals
```

## noGlobalEval

Avoid global eval.

```typescript
// BAD
eval("code");
new Function("return 1");

// GOOD - avoid dynamic code execution
```

## noInvalidBuiltinInstantiation

Correct instantiation of builtins.

```typescript
// BAD
new Symbol("desc");   // Symbol is not a constructor
new BigInt(1);        // BigInt is not a constructor
Symbol.for("key")();  // Symbol.for returns a symbol, not function

// GOOD
Symbol("desc");
BigInt(1);
Symbol.for("key");
```

## noInvalidNewBuiltin

Don't use new with non-constructors.

```typescript
// BAD
new Symbol();
new BigInt();

// GOOD
Symbol();
BigInt(1);
```

## noMissingGenericFamilyKeyword

CSS font-family needs generic fallback.

```css
/* BAD */
.foo {
  font-family: "Helvetica";
}

/* GOOD */
.foo {
  font-family: "Helvetica", sans-serif;
}
```

## noMissingVarFunction

CSS custom properties need var().

```css
/* BAD */
.foo {
  color: --my-color;
}

/* GOOD */
.foo {
  color: var(--my-color);
}
```

## noNodejsModules

Disallow Node.js builtin modules.

```typescript
// BAD (in browser code)
import fs from "fs";
import path from "path";

// GOOD - use browser-compatible alternatives
```

## noOctalEscape

No octal escape sequences in strings.

```typescript
// BAD
const str = "\251";  // octal escape

// GOOD
const str = "\u00A9";  // unicode escape
const str = "©";       // literal
```

## noProcessEnv

Avoid direct process.env access.

```typescript
// BAD
const key = process.env.API_KEY;

// GOOD - centralize config
import { config } from "./config";
const key = config.apiKey;
```

## noRestrictedImports

Disallow specific imports.

```typescript
// Configure in biome.json
{
  "linter": {
    "rules": {
      "nursery": {
        "noRestrictedImports": {
          "level": "error",
          "options": {
            "paths": {
              "lodash": "Use native methods instead"
            }
          }
        }
      }
    }
  }
}
```

## noSecrets

Detect hardcoded secrets.

```typescript
// BAD
const API_KEY = "sk-1234567890abcdef";
const password = "hunter2";

// GOOD
const API_KEY = process.env.API_KEY;
```

## noSkippedTests

No skipped tests.

```typescript
// BAD
it.skip("should work", () => {});
xit("should work", () => {});
test.skip("should work", () => {});

// GOOD
it("should work", () => {});
```

## noStaticElementInteractions

Static elements shouldn't have handlers.

```tsx
// BAD
<div onClick={handleClick}>Click me</div>

// GOOD
<button onClick={handleClick}>Click me</button>
<div role="button" tabIndex={0} onClick={handleClick}>Click me</div>
```

## noSubstr

Use slice instead of substr.

```typescript
// BAD (deprecated)
str.substr(1, 3);

// GOOD
str.slice(1, 4);
str.substring(1, 4);
```

## noThenProperty

Avoid objects with 'then' property.

```typescript
// BAD - looks like a thenable
const obj = {
  then: () => console.log("not a promise"),
};
await obj;  // calls obj.then()!

// GOOD
const obj = {
  handle: () => console.log("clear name"),
};
```

## noTypeOnlyImportAttributes

No import attributes on type-only imports.

```typescript
// BAD
import type { Foo } from "./foo.json" with { type: "json" };

// GOOD
import type { Foo } from "./types";
import data from "./foo.json" with { type: "json" };
```

## noUndeclaredDependencies

Import only declared dependencies.

```typescript
// BAD (if lodash not in package.json)
import _ from "lodash";

// GOOD - add to package.json first
npm install lodash
```

## noUnknownFunction

CSS: no unknown functions.

```css
/* BAD */
.foo {
  color: unknownfn(red);
}

/* GOOD */
.foo {
  color: rgb(255, 0, 0);
}
```

## noUnknownMediaFeatureName

CSS: valid media feature names.

```css
/* BAD */
@media (unknown-feature: value) {}

/* GOOD */
@media (min-width: 768px) {}
```

## noUnknownProperty

CSS: valid property names.

```css
/* BAD */
.foo {
  colour: red;
}

/* GOOD */
.foo {
  color: red;
}
```

## noUnknownPseudoClassSelector

CSS: valid pseudo-class selectors.

```css
/* BAD */
.foo:hoverr {}

/* GOOD */
.foo:hover {}
```

## noUnknownSelectorPseudoElement

CSS: valid pseudo-element selectors.

```css
/* BAD */
.foo::beforee {}

/* GOOD */
.foo::before {}
```

## noUnknownUnit

CSS: valid units.

```css
/* BAD */
.foo {
  width: 100pixels;
}

/* GOOD */
.foo {
  width: 100px;
}
```

## noUnmatchableAnbSelector

CSS: matchable An+B selectors.

```css
/* BAD */
:nth-child(0n+0) {}  /* matches nothing */

/* GOOD */
:nth-child(2n+1) {}
```

## noUnusedFunctionParameters

Flag unused function parameters.

```typescript
// BAD
function foo(a, b, c) {  // c unused
  return a + b;
}

// GOOD
function foo(a, b, _c) {  // underscore indicates intentional
  return a + b;
}

function foo(a, b) {
  return a + b;
}
```

## noUselessEscapeInRegex

No unnecessary regex escapes.

```typescript
// BAD
/\a/;  // 'a' doesn't need escaping
/\-/;  // '-' outside char class

// GOOD
/a/;
/-/;
/\d/;  // 'd' needs escaping for digit
```

## noUselessStringConcat

Avoid useless concatenation.

```typescript
// BAD
const s = "hello" + "world";
const s = `hello` + `world`;

// GOOD
const s = "helloworld";
const s = `helloworld`;
```

## noUselessUndefinedInitialization

Don't initialize to undefined.

```typescript
// BAD
let x = undefined;
let y: string | undefined = undefined;

// GOOD
let x;
let y: string | undefined;
```

## noValueAtRule

CSS: no @value (CSS Modules specific).

```css
/* BAD (use CSS variables instead) */
@value primary: blue;

/* GOOD */
:root {
  --primary: blue;
}
```

## noYodaExpression

No Yoda conditions.

```typescript
// BAD
if (5 === x) {}
if ("red" === color) {}

// GOOD
if (x === 5) {}
if (color === "red") {}
```

## useAdjacentOverloadSignatures

Group overload signatures together.

```typescript
// BAD
interface Foo {
  foo(a: string): void;
  bar(): void;
  foo(a: number): void;  // separated from other foo
}

// GOOD
interface Foo {
  foo(a: string): void;
  foo(a: number): void;
  bar(): void;
}
```

## useAriaPropsSupportedByRole

ARIA props must match role.

```tsx
// BAD
<div role="checkbox" aria-invalid="true" />

// GOOD
<div role="checkbox" aria-checked="true" />
```

## useArrayLiterals

Prefer array literals.

```typescript
// BAD
const arr = new Array();
const arr = Array(1, 2, 3);

// GOOD
const arr = [];
const arr = [1, 2, 3];
```

## useAtIndex

Use at() for negative indexing.

```typescript
// BAD
arr[arr.length - 1];
str.charAt(str.length - 2);

// GOOD
arr.at(-1);
str.at(-2);
```

## useCollapsedIf

Collapse nested if statements.

```typescript
// BAD
if (a) {
  if (b) {
    doSomething();
  }
}

// GOOD
if (a && b) {
  doSomething();
}
```

## useConsistentBuiltinInstantiation

Consistent builtin construction.

```typescript
// BAD - inconsistent
new Object();
Boolean(true);
new Array();
String("hello");

// GOOD - pick one style consistently
// Prefer literal syntax where possible
const obj = {};
const arr = [];
const str = "hello";
const bool = true;
```

## useConsistentCurlyBraces

Consistent curly braces.

```typescript
// BAD - inconsistent
if (a) doOne();
if (b) {
  doTwo();
}

// GOOD - consistent
if (a) {
  doOne();
}
if (b) {
  doTwo();
}
```

## useDateNow

Use Date.now() for timestamps.

```typescript
// BAD
new Date().getTime();
new Date().valueOf();
+new Date();

// GOOD
Date.now();
```

## useDefaultSwitchClause

Require default in switch.

```typescript
// BAD
switch (x) {
  case 1: break;
  case 2: break;
}

// GOOD
switch (x) {
  case 1: break;
  case 2: break;
  default: break;
}
```

## useDeprecatedReason

Require reason for @deprecated.

```typescript
// BAD
/** @deprecated */
function foo() {}

// GOOD
/** @deprecated Use bar() instead */
function foo() {}
```

## useExplicitLengthCheck

Explicit length comparisons.

```typescript
// BAD
if (arr.length) {}
if (!arr.length) {}

// GOOD
if (arr.length > 0) {}
if (arr.length === 0) {}
```

## useFocusableInteractive

Interactive elements must be focusable.

```tsx
// BAD
<div onClick={handleClick}>Click</div>

// GOOD
<div onClick={handleClick} tabIndex={0}>Click</div>
<button onClick={handleClick}>Click</button>
```

## useGenericFontNames

CSS font stacks need generic family.

```css
/* BAD */
body {
  font-family: "Roboto";
}

/* GOOD */
body {
  font-family: "Roboto", sans-serif;
}
```

## useImportExtensions

Require import extensions.

```typescript
// BAD
import { foo } from "./foo";

// GOOD
import { foo } from "./foo.js";
import { foo } from "./foo.ts";
```

## useImportRestrictions

Control import sources.

```typescript
// Configure allowed/disallowed import patterns
// in biome.json
```

## useJsxCurlyBraceConvention

Consistent JSX curly braces.

```tsx
// BAD - inconsistent
<Component prop={"value"} />
<Component prop="value" />

// GOOD - consistent
<Component prop="value" />
```

## useNumberToFixedDigitsArgument

toFixed needs argument.

```typescript
// BAD
num.toFixed();

// GOOD
num.toFixed(2);
```

## useSemanticElements

Use semantic HTML.

```tsx
// BAD
<div role="navigation">...</div>
<div role="main">...</div>
<div role="article">...</div>

// GOOD
<nav>...</nav>
<main>...</main>
<article>...</article>
```

## useSortedClasses

Sort Tailwind classes.

```tsx
// BAD
<div className="p-4 flex bg-red-500 mt-2" />

// GOOD (sorted by Tailwind convention)
<div className="flex mt-2 bg-red-500 p-4" />
```

## useStrictMode

Require "use strict".

```javascript
// BAD (non-module)
function foo() {}

// GOOD
"use strict";
function foo() {}
```

## useTrimStartEnd

Use trimStart/trimEnd.

```typescript
// BAD (deprecated)
str.trimLeft();
str.trimRight();

// GOOD
str.trimStart();
str.trimEnd();
```

## useValidAutocomplete

Valid autocomplete values.

```html
<!-- BAD -->
<input autocomplete="invalid" />

<!-- GOOD -->
<input autocomplete="email" />
<input autocomplete="current-password" />
```
