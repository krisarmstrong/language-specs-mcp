# no-shadow

Disallow variable declarations from shadowing variables declared in the outer scope

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [builtinGlobals](#builtinglobals)
  2. [hoist](#hoist)

    1. [hoist: functions](#hoist-functions)
    2. [hoist: all](#hoist-all)
    3. [hoist: never](#hoist-never)
    4. [hoist: types](#hoist-types)
    5. [hoist: functions-and-types](#hoist-functions-and-types)

  3. [allow](#allow)
  4. [ignoreOnInitialization](#ignoreoninitialization)
  5. [ignoreTypeValueShadow](#ignoretypevalueshadow)
  6. [ignoreFunctionTypeParameterNameValueShadow](#ignorefunctiontypeparameternamevalueshadow)
  7. [Why does the rule report on enum members that share the same name as a variable in a parent scope?](#why-does-the-rule-report-on-enum-members-that-share-the-same-name-as-a-variable-in-a-parent-scope)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Shadowing is the process by which a local variable shares the same name as a variable in its containing scope. For example:

```
const a = 3;
function b() {
    const a = 10;
}
1
2
3
4
```

Copy code to clipboard

In this case, the variable `a` inside of `b()` is shadowing the variable `a` in the global scope. This can cause confusion while reading the code and it’s impossible to access the global variable.

## Rule Details

This rule aims to eliminate shadowed variable declarations.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBcImVycm9yXCIqL1xuXG5jb25zdCBhID0gMztcbmZ1bmN0aW9uIGIoKSB7XG4gICAgY29uc3QgYSA9IDEwO1xufVxuXG5jb25zdCBjID0gZnVuY3Rpb24gKCkge1xuICAgIGNvbnN0IGEgPSAxMDtcbn1cblxuZnVuY3Rpb24gZChhKSB7XG4gICAgYSA9IDEwO1xufVxuZChhKTtcblxuaWYgKHRydWUpIHtcbiAgICBjb25zdCBhID0gNTtcbn0ifQ==)

```
/*eslint no-shadow: "error"*/

const a = 3;
function b() {
    const a = 10;
}

const c = function () {
    const a = 10;
}

function d(a) {
    a = 10;
}
d(a);

if (true) {
    const a = 5;
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
```

## Options

This rule takes one option, an object, with the following properties:

- `"builtinGlobals"`
- `"hoist"`
- `"allow"`
- `"ignoreOnInitialization"`
- `"ignoreTypeValueShadow"` (TypeScript only)
- `"ignoreFunctionTypeParameterNameValueShadow"` (TypeScript only)

```
{
    "no-shadow": ["error", { "builtinGlobals": false, "hoist": "functions", "allow": [], "ignoreOnInitialization": false }]
}
1
2
3
```

Copy code to clipboard

### builtinGlobals

The `builtinGlobals` option is `false` by default. If it is `true`, the rule prevents shadowing of built-in global variables: `Object`, `Array`, `Number`, and so on.

Examples of incorrect code for the `{ "builtinGlobals": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiYnVpbHRpbkdsb2JhbHNcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBjb25zdCBPYmplY3QgPSAwO1xufSJ9)

```
/*eslint no-shadow: ["error", { "builtinGlobals": true }]*/

function foo() {
    const Object = 0;
}
1
2
3
4
5
```

### hoist

The `hoist` option has five settings:

- `functions` (by default) - reports shadowing before the outer functions are defined.
- `all` - reports all shadowing before the outer variables/functions are defined.
- `never` - never report shadowing before the outer variables/functions are defined.
- `types` (TypeScript only) - reports shadowing before the outer types are defined.
- `functions-and-types` (TypeScript only) - reports shadowing before the outer functions and types are defined.

#### hoist: functions

Examples of incorrect code for the default `{ "hoist": "functions" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiaG9pc3RcIjogXCJmdW5jdGlvbnNcIiB9XSovXG5cbmlmICh0cnVlKSB7XG4gICAgY29uc3QgYiA9IDY7XG59XG5cbmZ1bmN0aW9uIGIoKSB7fSJ9)

```
/*eslint no-shadow: ["error", { "hoist": "functions" }]*/

if (true) {
    const b = 6;
}

function b() {}
1
2
3
4
5
6
7
```

Although `const b` in the `if` statement is before the function declaration in the outer scope, it is incorrect.

Examples of correct code for the default `{ "hoist": "functions" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiaG9pc3RcIjogXCJmdW5jdGlvbnNcIiB9XSovXG5cbmlmICh0cnVlKSB7XG4gICAgY29uc3QgYSA9IDM7XG59XG5cbmNvbnN0IGEgPSA1OyJ9)

```
/*eslint no-shadow: ["error", { "hoist": "functions" }]*/

if (true) {
    const a = 3;
}

const a = 5;
1
2
3
4
5
6
7
```

Because `const a` in the `if` statement is before the variable declaration in the outer scope, it is correct.

#### hoist: all

Examples of incorrect code for the `{ "hoist": "all" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiaG9pc3RcIjogXCJhbGxcIiB9XSovXG5cbmlmICh0cnVlKSB7XG4gICAgY29uc3QgYSA9IDM7XG4gICAgY29uc3QgYiA9IDY7XG59XG5cbmNvbnN0IGEgPSA1O1xuZnVuY3Rpb24gYigpIHt9In0=)

```
/*eslint no-shadow: ["error", { "hoist": "all" }]*/

if (true) {
    const a = 3;
    const b = 6;
}

const a = 5;
function b() {}
1
2
3
4
5
6
7
8
9
```

#### hoist: never

Examples of correct code for the `{ "hoist": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiaG9pc3RcIjogXCJuZXZlclwiIH1dKi9cblxuaWYgKHRydWUpIHtcbiAgICBjb25zdCBhID0gMztcbiAgICBjb25zdCBiID0gNjtcbn1cblxuY29uc3QgYSA9IDU7XG5mdW5jdGlvbiBiKCkge30ifQ==)

```
/*eslint no-shadow: ["error", { "hoist": "never" }]*/

if (true) {
    const a = 3;
    const b = 6;
}

const a = 5;
function b() {}
1
2
3
4
5
6
7
8
9
```

Because `const a` and `const b` in the `if` statement are before the declarations in the outer scope, they are correct.

#### hoist: types

Examples of incorrect code for the `{ "hoist": "types" }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1zaGFkb3c6IFtcImVycm9yXCIsIHsgXCJob2lzdFwiOiBcInR5cGVzXCIgfV0qL1xuXG50eXBlIEJhcjxGb28+ID0gMTtcbnR5cGUgRm9vID0gMTsifQ==)

```
/*eslint no-shadow: ["error", { "hoist": "types" }]*/

type Bar<Foo> = 1;
type Foo = 1;
1
2
3
4
```

#### hoist: functions-and-types

Examples of incorrect code for the `{ "hoist": "functions-and-types" }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1zaGFkb3c6IFtcImVycm9yXCIsIHsgXCJob2lzdFwiOiBcImZ1bmN0aW9ucy1hbmQtdHlwZXNcIiB9XSovXG5cbi8vIHR5cGVzXG50eXBlIEJhcjxGb28+ID0gMTtcbnR5cGUgRm9vID0gMTtcblxuLy8gZnVuY3Rpb25zXG5pZiAodHJ1ZSkge1xuICBjb25zdCBiID0gNjtcbn1cblxuZnVuY3Rpb24gYigpIHt9In0=)

```
/*eslint no-shadow: ["error", { "hoist": "functions-and-types" }]*/

// types
type Bar<Foo> = 1;
type Foo = 1;

// functions
if (true) {
  const b = 6;
}

function b() {}
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

### allow

The `allow` option is an array of identifier names for which shadowing is allowed. For example, `"resolve"`, `"reject"`, `"done"`, `"cb"`.

Examples of correct code for the `{ "allow": ["done"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiYWxsb3dcIjogW1wiZG9uZVwiXSB9XSovXG5cbmltcG9ydCBhc3luYyBmcm9tICdhc3luYyc7XG5cbmZ1bmN0aW9uIGZvbyhkb25lKSB7XG4gIGFzeW5jLm1hcChbMSwgMl0sIGZ1bmN0aW9uIChlLCBkb25lKSB7XG4gICAgZG9uZShudWxsLCBlICogMilcbiAgfSwgZG9uZSk7XG59XG5cbmZvbyhmdW5jdGlvbiAoZXJyLCByZXN1bHQpIHtcbiAgY29uc29sZS5sb2coeyBlcnIsIHJlc3VsdCB9KTtcbn0pOyJ9)

```
/*eslint no-shadow: ["error", { "allow": ["done"] }]*/

import async from 'async';

function foo(done) {
  async.map([1, 2], function (e, done) {
    done(null, e * 2)
  }, done);
}

foo(function (err, result) {
  console.log({ err, result });
});
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
```

### ignoreOnInitialization

The `ignoreOnInitialization` option is `false` by default. If it is `true`, it prevents reporting shadowing of variables in their initializers when the shadowed variable is presumably still uninitialized.

The shadowed variable must be on the left side. The shadowing variable must be on the right side and declared in a callback function or in an IIFE.

Examples of incorrect code for the `{ "ignoreOnInitialization": "true" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiaWdub3JlT25Jbml0aWFsaXphdGlvblwiOiB0cnVlIH1dKi9cblxuY29uc3QgeCA9IHggPT4geDsifQ==)

```
/*eslint no-shadow: ["error", { "ignoreOnInitialization": true }]*/

const x = x => x;
1
2
3
```

Because the shadowing variable `x` will shadow the already initialized shadowed variable `x`.

Examples of correct code for the `{ "ignoreOnInitialization": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93OiBbXCJlcnJvclwiLCB7IFwiaWdub3JlT25Jbml0aWFsaXphdGlvblwiOiB0cnVlIH1dKi9cblxuY29uc3QgeCA9IGZvbyh4ID0+IHgpXG5cbmNvbnN0IHkgPSAoeSA9PiB5KSgpIn0=)

```
/*eslint no-shadow: ["error", { "ignoreOnInitialization": true }]*/

const x = foo(x => x)

const y = (y => y)()
1
2
3
4
5
```

The rationale for callback functions is the assumption that they will be called during the initialization, so that at the time when the shadowing variable will be used, the shadowed variable has not yet been initialized.

### ignoreTypeValueShadow

Whether to ignore types named the same as a variable. Default: `true`.

This is generally safe because you cannot use variables in type locations without a typeof operator, so there’s little risk of confusion.

Examples of correct code with `{ "ignoreTypeValueShadow": true }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1zaGFkb3c6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVUeXBlVmFsdWVTaGFkb3dcIjogdHJ1ZSB9XSovXG5cbnR5cGUgRm9vID0gbnVtYmVyO1xuaW50ZXJmYWNlIEJhciB7XG4gIHByb3A6IG51bWJlcjtcbn1cblxuZnVuY3Rpb24gZigpIHtcbiAgY29uc3QgRm9vID0gMTtcbiAgY29uc3QgQmFyID0gJ3Rlc3QnO1xufSJ9)

```
/*eslint no-shadow: ["error", { "ignoreTypeValueShadow": true }]*/

type Foo = number;
interface Bar {
  prop: number;
}

function f() {
  const Foo = 1;
  const Bar = 'test';
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

Note: Shadowing specifically refers to two identical identifiers that are in different, nested scopes. This is different from redeclaration, which is when two identical identifiers are in the same scope. Redeclaration is covered by the [no-redeclare](/rules/no-redeclare) rule instead.

### ignoreFunctionTypeParameterNameValueShadow

Whether to ignore function parameters named the same as a variable. Default: `true`.

Each of a function type’s arguments creates a value variable within the scope of the function type. This is done so that you can reference the type later using the typeof operator:

```
type Func = (test: string) => typeof test;

declare const fn: Func;
const result = fn('str'); // typeof result === string
1
2
3
4
```

Copy code to clipboard

This means that function type arguments shadow value variable names in parent scopes:

```
let test = 1;
type TestType = typeof test; // === number
type Func = (test: string) => typeof test; // this "test" references the argument, not the variable

declare const fn: Func;
const result = fn('str'); // typeof result === string
1
2
3
4
5
6
```

Copy code to clipboard

If you do not use the `typeof` operator in a function type return type position, you can safely turn this option on.

Examples of correct code with `{ "ignoreFunctionTypeParameterNameValueShadow": true }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1zaGFkb3c6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVGdW5jdGlvblR5cGVQYXJhbWV0ZXJOYW1lVmFsdWVTaGFkb3dcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IHRlc3QgPSAxO1xudHlwZSBGdW5jID0gKHRlc3Q6IHN0cmluZykgPT4gdHlwZW9mIHRlc3Q7In0=)

```
/*eslint no-shadow: ["error", { "ignoreFunctionTypeParameterNameValueShadow": true }]*/

const test = 1;
type Func = (test: string) => typeof test;
1
2
3
4
```

### Why does the rule report on enum members that share the same name as a variable in a parent scope?

This isn’t a bug — the rule is working exactly as intended! The report is correct because of a lesser-known aspect of enums: enum members introduce a variable within the enum’s own scope, allowing them to be referenced without needing a qualifier.

Here’s a simple example to explain:

```
const A = 2;
enum Test {
  A = 1,
  B = A,
}

console.log(Test.B); // what should be logged?
1
2
3
4
5
6
7
```

Copy code to clipboard

At first glance, you might think it should log `2`, because the outer variable A’s value is `2`. However, it actually logs `1`, the value of `Test.A`. This happens because inside the enum `B = A` is treated as `B = Test.A`. Due to this behavior, the enum member has shadowed the outer variable declaration.

## Related Rules

- [no-shadow-restricted-names](/docs/latest/rules/no-shadow-restricted-names)

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[Variable shadowing - Wikipedia](https://en.wikipedia.org/wiki/Variable_shadowing)
 en.wikipedia.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-shadow.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-shadow.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-shadow.md
                    
                
                )
