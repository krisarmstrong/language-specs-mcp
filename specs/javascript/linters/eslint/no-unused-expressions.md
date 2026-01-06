# no-unused-expressions

Disallow unused expressions

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowShortCircuit](#allowshortcircuit)
  2. [allowTernary](#allowternary)
  3. [allowShortCircuit and allowTernary](#allowshortcircuit-and-allowternary)
  4. [allowTaggedTemplates](#allowtaggedtemplates)
  5. [enforceForJSX](#enforceforjsx)
  6. [ignoreDirectives](#ignoredirectives)
  7. [TypeScript Support](#typescript-support)

3. [Version](#version)
4. [Resources](#resources)

An unused expression which has no effect on the state of the program indicates a logic error.

For example, `n + 1;` is not a syntax error, but it might be a typing mistake where a programmer meant an assignment statement `n += 1;` instead. Sometimes, such unused expressions may be eliminated by some build tools in production environment, which possibly breaks application logic.

## Rule Details

This rule aims to eliminate unused expressions which have no effect on the state of the program.

This rule does not apply to function calls or constructor calls with the `new` operator, because they could have side effects on the state of the program.

```
let i = 0;
function increment() { i += 1; }
increment(); // return value is unused, but i changed as a side effect

let nThings = 0;
function Thing() { nThings += 1; }
new Thing(); // constructed object is unused, but nThings changed as a side effect
1
2
3
4
5
6
7
```

Copy code to clipboard

This rule does not apply to directives (which are in the form of literal string expressions such as `"use strict";` at the beginning of a script, module, or function) when using ES5+ environments. In ES3 environments, directives are treated as unused expressions by default, but this behavior can be changed using the `ignoreDirectives` option.

Sequence expressions (those using a comma, such as `a = 1, b = 2`) are always considered unused unless their return value is assigned or used in a condition evaluation, or a function call is made with the sequence expression value.

## Options

This rule, in its default state, does not require any arguments. If you would like to enable one or more of the following you may pass an object with the options set as follows:

- `allowShortCircuit` set to `true` will allow you to use short circuit evaluations in your expressions (Default: `false`).
- `allowTernary` set to `true` will enable you to use ternary operators in your expressions similarly to short circuit evaluations (Default: `false`).
- `allowTaggedTemplates` set to `true` will enable you to use tagged template literals in your expressions (Default: `false`).
- `enforceForJSX` set to `true` will flag unused JSX element expressions (Default: `false`).
- `ignoreDirectives` set to `true` will prevent directives from being reported as unused expressions when linting with `ecmaVersion: 3` (Default: `false`).

These options allow unused expressions only if all of the code paths either directly change the state (for example, assignment statement) or could have side effects (for example, function call).

Examples of incorrect code for the default `{ "allowShortCircuit": false, "allowTernary": false }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBcImVycm9yXCIqL1xuXG4wXG5cbmlmKDApIDBcblxuezB9XG5cbmYoMCksIHt9XG5cbmEgJiYgYigpXG5cbmEsIGIoKVxuXG5jID0gYSwgYjtcblxuYSgpICYmIGZ1bmN0aW9uIG5hbWVkRnVuY3Rpb25JbkV4cHJlc3Npb25Db250ZXh0ICgpIHtmKCk7fVxuXG4oZnVuY3Rpb24gYW5JbmNvbXBsZXRlSUlGRSAoKSB7fSk7XG5cbmluamVjdEdsb2JhbGBib2R5eyBjb2xvcjogcmVkOyB9YFxuIn0=)

```
/*eslint no-unused-expressions: "error"*/

0

if(0) 0

{0}

f(0), {}

a && b()

a, b()

c = a, b;

a() && function namedFunctionInExpressionContext () {f();}

(function anIncompleteIIFE () {});

injectGlobal`body{ color: red; }`

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

Examples of correct code for the default `{ "allowShortCircuit": false, "allowTernary": false }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBcImVycm9yXCIqL1xuXG57fSAvLyBJbiB0aGlzIGNvbnRleHQsIHRoaXMgaXMgYSBibG9jayBzdGF0ZW1lbnQsIG5vdCBhbiBvYmplY3QgbGl0ZXJhbFxuXG57IG15TGFiZWw6IGZvbygpIH0gLy8gSW4gdGhpcyBjb250ZXh0LCB0aGlzIGlzIGEgYmxvY2sgc3RhdGVtZW50IHdpdGggYSBsYWJlbCBhbmQgZXhwcmVzc2lvbiwgbm90IGFuIG9iamVjdCBsaXRlcmFsXG5cbmZ1bmN0aW9uIG5hbWVkRnVuY3Rpb25EZWNsYXJhdGlvbiAoKSB7fVxuXG4oZnVuY3Rpb24gYUdlbnVpbmVJSUZFICgpIHt9KCkpO1xuXG5mKClcblxuYSA9IDBcblxubmV3IENcblxuZGVsZXRlIGEuYlxuXG52b2lkIGEifQ==)

```
/*eslint no-unused-expressions: "error"*/

{} // In this context, this is a block statement, not an object literal

{ myLabel: foo() } // In this context, this is a block statement with a label and expression, not an object literal

function namedFunctionDeclaration () {}

(function aGenuineIIFE () {}());

f()

a = 0

new C

delete a.b

void a
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
```

Note that one or more string expression statements (with or without semi-colons) will only be considered as unused if they are not in the beginning of a script, module, or function (alone and uninterrupted by other statements). Otherwise, they will be treated as part of a “directive prologue”, a section potentially usable by JavaScript engines. This includes “strict mode” directives.

Examples of correct code for this rule in regard to directives:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBcImVycm9yXCIqL1xuXG5cInVzZSBzdHJpY3RcIjtcblwidXNlIGFzbVwiXG5cInVzZSBzdHJpY3RlclwiO1xuXCJ1c2UgYmFiZWxcIlxuXCJhbnkgb3RoZXIgc3RyaW5ncyBsaWtlIHRoaXMgaW4gdGhlIGRpcmVjdGl2ZSBwcm9sb2d1ZVwiO1xuXCJ0aGlzIGlzIHN0aWxsIHRoZSBkaXJlY3RpdmUgcHJvbG9ndWVcIjtcblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIFwiYmFyXCI7XG59XG5cbmNsYXNzIEZvbyB7XG4gICAgc29tZU1ldGhvZCgpIHtcbiAgICAgICAgXCJ1c2Ugc3RyaWN0XCI7XG4gICAgfVxufSJ9)

```
/*eslint no-unused-expressions: "error"*/

"use strict";
"use asm"
"use stricter";
"use babel"
"any other strings like this in the directive prologue";
"this is still the directive prologue";

function foo() {
    "bar";
}

class Foo {
    someMethod() {
        "use strict";
    }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
```

Examples of incorrect code for this rule in regard to directives:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBcImVycm9yXCIqL1xuXG5kb1NvbWV0aGluZygpO1xuXCJ1c2Ugc3RyaWN0XCI7IC8vIHRoaXMgaXNuJ3QgaW4gYSBkaXJlY3RpdmUgcHJvbG9ndWUsIGJlY2F1c2UgdGhlcmUgaXMgYSBub24tZGlyZWN0aXZlIHN0YXRlbWVudCBiZWZvcmUgaXRcblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIFwiYmFyXCIgKyAxO1xufVxuXG5jbGFzcyBGb28ge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIFwidXNlIHN0cmljdFwiOyAvLyBjbGFzcyBzdGF0aWMgYmxvY2tzIGRvIG5vdCBoYXZlIGRpcmVjdGl2ZSBwcm9sb2d1ZXNcbiAgICB9XG59In0=)

```
/*eslint no-unused-expressions: "error"*/

doSomething();
"use strict"; // this isn't in a directive prologue, because there is a non-directive statement before it

function foo() {
    "bar" + 1;
}

class Foo {
    static {
        "use strict"; // class static blocks do not have directive prologues
    }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
```

### allowShortCircuit

Examples of incorrect code for the `{ "allowShortCircuit": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTaG9ydENpcmN1aXRcIjogdHJ1ZSB9XSovXG5cbmEgfHwgYiJ9)

```
/*eslint no-unused-expressions: ["error", { "allowShortCircuit": true }]*/

a || b
1
2
3
```

Examples of correct code for the `{ "allowShortCircuit": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTaG9ydENpcmN1aXRcIjogdHJ1ZSB9XSovXG5cbmEgJiYgYigpXG5hKCkgfHwgKGIgPSBjKSJ9)

```
/*eslint no-unused-expressions: ["error", { "allowShortCircuit": true }]*/

a && b()
a() || (b = c)
1
2
3
4
```

### allowTernary

Examples of incorrect code for the `{ "allowTernary": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dUZXJuYXJ5XCI6IHRydWUgfV0qL1xuXG5hID8gYiA6IDBcbmEgPyBiIDogYygpIn0=)

```
/*eslint no-unused-expressions: ["error", { "allowTernary": true }]*/

a ? b : 0
a ? b : c()
1
2
3
4
```

Examples of correct code for the `{ "allowTernary": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dUZXJuYXJ5XCI6IHRydWUgfV0qL1xuXG5hID8gYigpIDogYygpXG5hID8gKGIgPSBjKSA6IGQoKSJ9)

```
/*eslint no-unused-expressions: ["error", { "allowTernary": true }]*/

a ? b() : c()
a ? (b = c) : d()
1
2
3
4
```

### allowShortCircuit and allowTernary

Examples of correct code for the `{ "allowShortCircuit": true, "allowTernary": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTaG9ydENpcmN1aXRcIjogdHJ1ZSwgXCJhbGxvd1Rlcm5hcnlcIjogdHJ1ZSB9XSovXG5cbmEgPyBiKCkgfHwgKGMgPSBkKSA6IGUoKSJ9)

```
/*eslint no-unused-expressions: ["error", { "allowShortCircuit": true, "allowTernary": true }]*/

a ? b() || (c = d) : e()
1
2
3
```

### allowTaggedTemplates

Examples of incorrect code for the `{ "allowTaggedTemplates": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dUYWdnZWRUZW1wbGF0ZXNcIjogdHJ1ZSB9XSovXG5cbmBzb21lIHVudGFnZ2VkIHRlbXBsYXRlIHN0cmluZ2A7In0=)

```
/*eslint no-unused-expressions: ["error", { "allowTaggedTemplates": true }]*/

`some untagged template string`;
1
2
3
```

Examples of correct code for the `{ "allowTaggedTemplates": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dUYWdnZWRUZW1wbGF0ZXNcIjogdHJ1ZSB9XSovXG5cbnRhZ2Bzb21lIHRhZ2dlZCB0ZW1wbGF0ZSBzdHJpbmdgOyJ9)

```
/*eslint no-unused-expressions: ["error", { "allowTaggedTemplates": true }]*/

tag`some tagged template string`;
1
2
3
```

### enforceForJSX

JSX is most-commonly used in the React ecosystem, where it is compiled to `React.createElement` expressions. Though free from side-effects, these calls are not automatically flagged by the `no-unused-expression` rule. If you’re using React, or any other side-effect-free JSX pragma, this option can be enabled to flag these expressions.

Examples of incorrect code for the `{ "enforceForJSX": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXJPcHRpb25zIjp7ImVjbWFGZWF0dXJlcyI6eyJqc3giOnRydWV9fX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiZW5mb3JjZUZvckpTWFwiOiB0cnVlIH1dKi9cblxuPE15Q29tcG9uZW50IC8+O1xuXG48PjwvPjsifQ==)

```
/*eslint no-unused-expressions: ["error", { "enforceForJSX": true }]*/

<MyComponent />;

<></>;
1
2
3
4
5
```

Examples of correct code for the `{ "enforceForJSX": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXJPcHRpb25zIjp7ImVjbWFGZWF0dXJlcyI6eyJqc3giOnRydWV9fX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBbXCJlcnJvclwiLCB7IFwiZW5mb3JjZUZvckpTWFwiOiB0cnVlIH1dKi9cblxuY29uc3QgbXlDb21wb25lbnRQYXJ0aWFsID0gPE15Q29tcG9uZW50IC8+O1xuXG5jb25zdCBteUZyYWdtZW50ID0gPD48Lz47In0=)

```
/*eslint no-unused-expressions: ["error", { "enforceForJSX": true }]*/

const myComponentPartial = <MyComponent />;

const myFragment = <></>;
1
2
3
4
5
```

### ignoreDirectives

When set to `false` (default), this rule reports directives (like `"use strict"`) as unused expressions when linting with `ecmaVersion: 3`. This default behavior exists because ES3 environments do not formally support directives, meaning such strings are effectively unused expressions in that specific context.

Set this option to `true` to prevent directives from being reported as unused, even when `ecmaVersion: 3` is specified. This option is primarily useful for projects that need to maintain a single codebase containing directives while supporting both older ES3 environments and modern (ES5+) environments.

Note: In ES5+ environments, directives are always ignored regardless of this setting.

Examples of incorrect code for the `{ "ignoreDirectives": false }` option and `ecmaVersion: 3`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJlY21hVmVyc2lvbiI6Mywic291cmNlVHlwZSI6InNjcmlwdCJ9fSwidGV4dCI6Ii8qZXNsaW50IG5vLXVudXNlZC1leHByZXNzaW9uczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZURpcmVjdGl2ZXNcIjogZmFsc2UgfV0qL1xuXG5cInVzZSBzdHJpY3RcIjtcblwidXNlIGFzbVwiXG5cInVzZSBzdHJpY3RlclwiO1xuXCJ1c2UgYmFiZWxcIlxuXCJhbnkgb3RoZXIgc3RyaW5ncyBsaWtlIHRoaXMgaW4gdGhlIGRpcmVjdGl2ZSBwcm9sb2d1ZVwiO1xuXCJ0aGlzIGlzIHN0aWxsIHRoZSBkaXJlY3RpdmUgcHJvbG9ndWVcIjtcblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIFwiYmFyXCI7XG59In0=)

```
/*eslint no-unused-expressions: ["error", { "ignoreDirectives": false }]*/

"use strict";
"use asm"
"use stricter";
"use babel"
"any other strings like this in the directive prologue";
"this is still the directive prologue";

function foo() {
    "bar";
}
1
2
3
4
5
6
7
8
9
10
11
12
```

Examples of correct code for the `{ "ignoreDirectives": true }` option and `ecmaVersion: 3`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJlY21hVmVyc2lvbiI6Mywic291cmNlVHlwZSI6InNjcmlwdCJ9fSwidGV4dCI6Ii8qZXNsaW50IG5vLXVudXNlZC1leHByZXNzaW9uczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZURpcmVjdGl2ZXNcIjogdHJ1ZSB9XSovXG5cblwidXNlIHN0cmljdFwiO1xuXCJ1c2UgYXNtXCJcblwidXNlIHN0cmljdGVyXCI7XG5cInVzZSBiYWJlbFwiXG5cImFueSBvdGhlciBzdHJpbmdzIGxpa2UgdGhpcyBpbiB0aGUgZGlyZWN0aXZlIHByb2xvZ3VlXCI7XG5cInRoaXMgaXMgc3RpbGwgdGhlIGRpcmVjdGl2ZSBwcm9sb2d1ZVwiO1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgXCJiYXJcIjtcbn0ifQ==)

```
/*eslint no-unused-expressions: ["error", { "ignoreDirectives": true }]*/

"use strict";
"use asm"
"use stricter";
"use babel"
"any other strings like this in the directive prologue";
"this is still the directive prologue";

function foo() {
    "bar";
}
1
2
3
4
5
6
7
8
9
10
11
12
```

### TypeScript Support

This rule supports TypeScript-specific expressions and follows these guidelines:

1. Directives (like `'use strict'`) are allowed in module and namespace declarations
2. Type-related expressions are treated as unused if their wrapped value expressions are unused: 

  - Type assertions (`x as number`, `<number>x`)
  - Non-null assertions (`x!`)
  - Type instantiations (`Set<number>`)

Note: Although type expressions never have runtime side effects (e.g., `x!` is equivalent to `x` at runtime), they can be used to assert types for testing purposes.

Examples of correct code for this rule when using TypeScript:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBcImVycm9yXCIgKi9cblxuLy8gVHlwZSBleHByZXNzaW9ucyB3cmFwcGluZyBmdW5jdGlvbiBjYWxscyBhcmUgYWxsb3dlZFxuZnVuY3Rpb24gZ2V0U2V0KCkge1xuICAgIHJldHVybiBTZXQ7XG59XG5nZXRTZXQoKTxudW1iZXI+O1xuZ2V0U2V0KCkgYXMgU2V0PHVua25vd24+O1xuZ2V0U2V0KCkhO1xuXG4vLyBEaXJlY3RpdmVzIGluIG1vZHVsZXMgYW5kIG5hbWVzcGFjZXNcbm1vZHVsZSBGb28ge1xuICAgICd1c2Ugc3RyaWN0JztcbiAgICAnaGVsbG8gd29ybGQnO1xufVxuXG5uYW1lc3BhY2UgQmFyIHtcbiAgICAndXNlIHN0cmljdCc7XG4gICAgZXhwb3J0IGNsYXNzIEJheiB7fVxufSJ9)

```
/* eslint no-unused-expressions: "error" */

// Type expressions wrapping function calls are allowed
function getSet() {
    return Set;
}
getSet()<number>;
getSet() as Set<unknown>;
getSet()!;

// Directives in modules and namespaces
module Foo {
    'use strict';
    'hello world';
}

namespace Bar {
    'use strict';
    export class Baz {}
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

Examples of incorrect code for this rule when using TypeScript:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgbm8tdW51c2VkLWV4cHJlc3Npb25zOiBcImVycm9yXCIgKi9cblxuLy8gU3RhbmRhbG9uZSB0eXBlIGV4cHJlc3Npb25zXG5TZXQ8bnVtYmVyPjtcbjEgYXMgbnVtYmVyO1xud2luZG93ITtcblxuLy8gRXhwcmVzc2lvbnMgaW5zaWRlIG5hbWVzcGFjZXNcbm5hbWVzcGFjZSBCYXIge1xuICAgIDEyMztcbn0ifQ==)

```
/* eslint no-unused-expressions: "error" */

// Standalone type expressions
Set<number>;
1 as number;
window!;

// Expressions inside namespaces
namespace Bar {
    123;
}
1
2
3
4
5
6
7
8
9
10
11
```

## Version

This rule was introduced in ESLint v0.1.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unused-expressions.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unused-expressions.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unused-expressions.md
                    
                
                )
