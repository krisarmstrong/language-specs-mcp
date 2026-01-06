# no-use-before-define

Disallow the use of variables before they are defined

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [functions](#functions)
  2. [classes](#classes)
  3. [variables](#variables)
  4. [allowNamedExports](#allownamedexports)
  5. [enums (TypeScript only)](#enums-typescript-only)
  6. [typedefs (TypeScript only)](#typedefs-typescript-only)
  7. [ignoreTypeReferences (TypeScript only)](#ignoretypereferences-typescript-only)
  8. [nofunc](#nofunc)

3. [Version](#version)
4. [Resources](#resources)

In JavaScript, prior to ES6, variable and function declarations are hoisted to the top of a scope, so it’s possible to use identifiers before their formal declarations in code. This can be confusing and some believe it is best to always declare variables and functions before using them.

In ES6, block-level bindings (`let` and `const`) introduce a “temporal dead zone” where a `ReferenceError` will be thrown with any attempt to access the variable before its declaration.

## Rule Details

This rule will warn when it encounters a reference to an identifier that has not yet been declared.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFwiZXJyb3JcIiovXG5cbmFsZXJ0KGEpO1xudmFyIGEgPSAxMDtcblxuZigpO1xuZnVuY3Rpb24gZigpIHt9XG5cbmZ1bmN0aW9uIGcoKSB7XG4gICAgcmV0dXJuIGI7XG59XG52YXIgYiA9IDE7XG5cbntcbiAgICBhbGVydChjKTtcbiAgICBsZXQgYyA9IDE7XG59XG5cbntcbiAgICBjbGFzcyBDIGV4dGVuZHMgQyB7fVxufVxuXG57XG4gICAgY2xhc3MgQyB7XG4gICAgICAgIHN0YXRpYyB4ID0gXCJmb29cIjtcbiAgICAgICAgW0MueF0oKSB7fVxuICAgIH1cbn1cblxue1xuICAgIGNvbnN0IEMgPSBjbGFzcyB7XG4gICAgICAgIHN0YXRpYyB4ID0gQztcbiAgICB9XG59XG5cbntcbiAgICBjb25zdCBDID0gY2xhc3Mge1xuICAgICAgICBzdGF0aWMge1xuICAgICAgICAgICAgQy54ID0gXCJmb29cIjtcbiAgICAgICAgfVxuICAgIH1cbn1cblxuZXhwb3J0IHsgZm9vIH07XG5jb25zdCBmb28gPSAxOyJ9)

```
/*eslint no-use-before-define: "error"*/

alert(a);
var a = 10;

f();
function f() {}

function g() {
    return b;
}
var b = 1;

{
    alert(c);
    let c = 1;
}

{
    class C extends C {}
}

{
    class C {
        static x = "foo";
        [C.x]() {}
    }
}

{
    const C = class {
        static x = C;
    }
}

{
    const C = class {
        static {
            C.x = "foo";
        }
    }
}

export { foo };
const foo = 1;
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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFwiZXJyb3JcIiovXG5cbnZhciBhO1xuYSA9IDEwO1xuYWxlcnQoYSk7XG5cbmZ1bmN0aW9uIGYoKSB7fVxuZigxKTtcblxudmFyIGIgPSAxO1xuZnVuY3Rpb24gZygpIHtcbiAgICByZXR1cm4gYjtcbn1cblxue1xuICAgIGxldCBjO1xuICAgIGMrKztcbn1cblxue1xuICAgIGNsYXNzIEMge1xuICAgICAgICBzdGF0aWMgeCA9IEM7XG4gICAgfVxufVxuXG57XG4gICAgY29uc3QgQyA9IGNsYXNzIEMge1xuICAgICAgICBzdGF0aWMgeCA9IEM7XG4gICAgfVxufVxuXG57XG4gICAgY29uc3QgQyA9IGNsYXNzIHtcbiAgICAgICAgeCA9IEM7XG4gICAgfVxufVxuXG57XG4gICAgY29uc3QgQyA9IGNsYXNzIEMge1xuICAgICAgICBzdGF0aWMge1xuICAgICAgICAgICAgQy54ID0gXCJmb29cIjtcbiAgICAgICAgfVxuICAgIH1cbn1cblxuY29uc3QgZm9vID0gMTtcbmV4cG9ydCB7IGZvbyB9OyJ9)

```
/*eslint no-use-before-define: "error"*/

var a;
a = 10;
alert(a);

function f() {}
f(1);

var b = 1;
function g() {
    return b;
}

{
    let c;
    c++;
}

{
    class C {
        static x = C;
    }
}

{
    const C = class C {
        static x = C;
    }
}

{
    const C = class {
        x = C;
    }
}

{
    const C = class C {
        static {
            C.x = "foo";
        }
    }
}

const foo = 1;
export { foo };
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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
```

## Options

```
{
    "no-use-before-define": ["error", {
        "functions": true,
        "classes": true,
        "variables": true,
        "allowNamedExports": false,
        "enums": true,
        "typedefs": true,
        "ignoreTypeReferences": true
    }]
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

Copy code to clipboard

- `functions` (`boolean`) - This flag determines whether or not the rule checks function declarations. If this is `true`, the rule warns on every reference to a function before the function declaration. Otherwise, the rule ignores those references. Function declarations are hoisted, so it’s safe to disable this option (note that some idiomatic patterns, such as [mutual recursion](https://en.wikipedia.org/wiki/Mutual_recursion), are incompatible with enabling this option). Default is `true`.
- `classes` (`boolean`) - This flag determines whether or not the rule checks class declarations of upper scopes. If this is `true`, the rule warns on every reference to a class before the class declaration. Otherwise, the rule ignores such references, provided the declaration is in an upper function scope. Class declarations are not hoisted, so it might be dangerous to disable this option. Default is `true`.
- `variables` (`boolean`) - This flag determines whether or not the rule checks variable declarations in upper scopes. If this is `true`, the rule warns on every reference to a variable before the variable declaration. Otherwise, the rule ignores a reference if the declaration is in an upper scope, while still reporting the reference if it’s in the same scope as the declaration. Default is `true`.
- `allowNamedExports` (`boolean`) - If this flag is set to `true`, the rule always allows references in `export {};` declarations. These references are safe even if the variables are declared later in the code. Default is `false`.

This rule additionally supports TypeScript type syntax. The following options enable checking for the references to `type`, `interface` and `enum` declarations:

- `enums` (`boolean`) - If it is `true`, the rule warns every reference to an `enum` before it is defined. Default is `true`.
- `typedefs` (`boolean`) - If it is `true`, this rule warns every reference to a type `alias` or `interface` before its declaration. If `false`, the rule allows using type `alias`es and `interface`s before they are defined. Default is `true`.
- `ignoreTypeReferences` (`boolean`) - If it is `true`, rule will ignore all type references, such as in type annotations and assertions. Default is `true`.

This rule accepts `"nofunc"` string as an option. `"nofunc"` is the same as `{ "functions": false, "classes": true, "variables": true, "allowNamedExports": false, "enums": true, "typedefs": true, "ignoreTypeReferences": true }`.

### functions

Examples of correct code for the `{ "functions": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJmdW5jdGlvbnNcIjogZmFsc2UgfV0qL1xuXG5mKCk7XG5mdW5jdGlvbiBmKCkge30ifQ==)

```
/*eslint no-use-before-define: ["error", { "functions": false }]*/

f();
function f() {}
1
2
3
4
```

This option allows references to function declarations. For function expressions and arrow functions, please see the [variables](#variables) option.

### classes

Examples of incorrect code for the `{ "classes": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJjbGFzc2VzXCI6IGZhbHNlIH1dKi9cblxubmV3IEEoKTtcbmNsYXNzIEEge1xufVxuXG57XG4gICAgY2xhc3MgQyBleHRlbmRzIEMge31cbn1cblxue1xuICAgIGNsYXNzIEMgZXh0ZW5kcyBEIHt9XG4gICAgY2xhc3MgRCB7fVxufVxuXG57XG4gICAgY2xhc3MgQyB7XG4gICAgICAgIHN0YXRpYyB4ID0gXCJmb29cIjtcbiAgICAgICAgW0MueF0oKSB7fVxuICAgIH1cbn1cblxue1xuICAgIGNsYXNzIEMge1xuICAgICAgICBzdGF0aWMge1xuICAgICAgICAgICAgbmV3IEQoKTtcbiAgICAgICAgfVxuICAgIH1cbiAgICBjbGFzcyBEIHt9XG59In0=)

```
/*eslint no-use-before-define: ["error", { "classes": false }]*/

new A();
class A {
}

{
    class C extends C {}
}

{
    class C extends D {}
    class D {}
}

{
    class C {
        static x = "foo";
        [C.x]() {}
    }
}

{
    class C {
        static {
            new D();
        }
    }
    class D {}
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
21
22
23
24
25
26
27
28
29
30
```

Examples of correct code for the `{ "classes": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJjbGFzc2VzXCI6IGZhbHNlIH1dKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIHJldHVybiBuZXcgQSgpO1xufVxuXG5jbGFzcyBBIHtcbn0ifQ==)

```
/*eslint no-use-before-define: ["error", { "classes": false }]*/

function foo() {
    return new A();
}

class A {
}
1
2
3
4
5
6
7
8
```

### variables

Examples of incorrect code for the `{ "variables": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJ2YXJpYWJsZXNcIjogZmFsc2UgfV0qL1xuXG5jb25zb2xlLmxvZyhmb28pO1xudmFyIGZvbyA9IDE7XG5cbmYoKTtcbmNvbnN0IGYgPSAoKSA9PiB7fTtcblxuZygpO1xuY29uc3QgZyA9IGZ1bmN0aW9uKCkge307XG5cbntcbiAgICBjb25zdCBDID0gY2xhc3Mge1xuICAgICAgICBzdGF0aWMgeCA9IEM7XG4gICAgfVxufVxuXG57XG4gICAgY29uc3QgQyA9IGNsYXNzIHtcbiAgICAgICAgc3RhdGljIHggPSBmb287XG4gICAgfVxuICAgIGNvbnN0IGZvbyA9IDE7XG59XG5cbntcbiAgICBjbGFzcyBDIHtcbiAgICAgICAgc3RhdGljIHtcbiAgICAgICAgICAgIHRoaXMueCA9IGZvbztcbiAgICAgICAgfVxuICAgIH1cbiAgICBjb25zdCBmb28gPSAxO1xufSJ9)

```
/*eslint no-use-before-define: ["error", { "variables": false }]*/

console.log(foo);
var foo = 1;

f();
const f = () => {};

g();
const g = function() {};

{
    const C = class {
        static x = C;
    }
}

{
    const C = class {
        static x = foo;
    }
    const foo = 1;
}

{
    class C {
        static {
            this.x = foo;
        }
    }
    const foo = 1;
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
21
22
23
24
25
26
27
28
29
30
31
32
```

Examples of correct code for the `{ "variables": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJ2YXJpYWJsZXNcIjogZmFsc2UgfV0qL1xuXG5mdW5jdGlvbiBiYXooKSB7XG4gICAgY29uc29sZS5sb2coZm9vKTtcbn1cbnZhciBmb28gPSAxO1xuXG5jb25zdCBhID0gKCkgPT4gZigpO1xuZnVuY3Rpb24gYigpIHsgcmV0dXJuIGYoKTsgfVxuY29uc3QgYyA9IGZ1bmN0aW9uKCkgeyByZXR1cm4gZigpOyB9XG5jb25zdCBmID0gKCkgPT4ge307XG5cbmNvbnN0IGUgPSBmdW5jdGlvbigpIHsgcmV0dXJuIGcoKTsgfVxuY29uc3QgZyA9IGZ1bmN0aW9uKCkge31cblxue1xuICAgIGNvbnN0IEMgPSBjbGFzcyB7XG4gICAgICAgIHggPSBmb287XG4gICAgfVxuICAgIGNvbnN0IGZvbyA9IDE7XG59In0=)

```
/*eslint no-use-before-define: ["error", { "variables": false }]*/

function baz() {
    console.log(foo);
}
var foo = 1;

const a = () => f();
function b() { return f(); }
const c = function() { return f(); }
const f = () => {};

const e = function() { return g(); }
const g = function() {}

{
    const C = class {
        x = foo;
    }
    const foo = 1;
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
21
```

### allowNamedExports

Examples of correct code for the `{ "allowNamedExports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJhbGxvd05hbWVkRXhwb3J0c1wiOiB0cnVlIH1dKi9cblxuZXhwb3J0IHsgYSwgYiwgZiwgQyB9O1xuXG5jb25zdCBhID0gMTtcblxubGV0IGI7XG5cbmZ1bmN0aW9uIGYgKCkge31cblxuY2xhc3MgQyB7fSJ9)

```
/*eslint no-use-before-define: ["error", { "allowNamedExports": true }]*/

export { a, b, f, C };

const a = 1;

let b;

function f () {}

class C {}
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

Examples of incorrect code for the `{ "allowNamedExports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIHsgXCJhbGxvd05hbWVkRXhwb3J0c1wiOiB0cnVlIH1dKi9cblxuZXhwb3J0IGRlZmF1bHQgYTtcbmNvbnN0IGEgPSAxO1xuXG5jb25zdCBiID0gYztcbmV4cG9ydCBjb25zdCBjID0gMTtcblxuZXhwb3J0IGZ1bmN0aW9uIGZvbygpIHtcbiAgICByZXR1cm4gZDtcbn1cbmNvbnN0IGQgPSAxOyJ9)

```
/*eslint no-use-before-define: ["error", { "allowNamedExports": true }]*/

export default a;
const a = 1;

const b = c;
export const c = 1;

export function foo() {
    return d;
}
const d = 1;
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

### enums (TypeScript only)

Examples of incorrect code for the `{ "enums": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcImVudW1zXCI6IHRydWUgfV0qL1xuXG5jb25zdCB4ID0gRm9vLkZPTztcblxuZW51bSBGb28ge1xuICBGT08sXG59In0=)

```
/*eslint no-use-before-define: ["error", { "enums": true }]*/

const x = Foo.FOO;

enum Foo {
  FOO,
}
1
2
3
4
5
6
7
```

Examples of correct code for the `{ "enums": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcImVudW1zXCI6IHRydWUgfV0qL1xuXG5lbnVtIEZvbyB7XG4gIEZPTyxcbn1cblxuY29uc3QgeCA9IEZvby5GT087In0=)

```
/*eslint no-use-before-define: ["error", { "enums": true }]*/

enum Foo {
  FOO,
}

const x = Foo.FOO;
1
2
3
4
5
6
7
```

### typedefs (TypeScript only)

Examples of incorrect code for the `{ "enums": true }` with `{ "ignoreTypeReferences": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcInR5cGVkZWZzXCI6IHRydWUsIFwiaWdub3JlVHlwZVJlZmVyZW5jZXNcIjogZmFsc2UgfV0qL1xuXG5sZXQgbXlWYXI6IFN0cmluZ09yTnVtYmVyO1xuXG50eXBlIFN0cmluZ09yTnVtYmVyID0gc3RyaW5nIHwgbnVtYmVyO1xuXG5jb25zdCB4OiBGb28gPSB7fTtcblxuaW50ZXJmYWNlIEZvbyB7fSJ9)

```
/*eslint no-use-before-define: ["error", { "typedefs": true, "ignoreTypeReferences": false }]*/

let myVar: StringOrNumber;

type StringOrNumber = string | number;

const x: Foo = {};

interface Foo {}
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

Examples of correct code for the `{ "typedefs": true }` with `{ "ignoreTypeReferences": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcInR5cGVkZWZzXCI6IHRydWUsIFwiaWdub3JlVHlwZVJlZmVyZW5jZXNcIjogZmFsc2UgfV0qL1xuXG50eXBlIFN0cmluZ09yTnVtYmVyID0gc3RyaW5nIHwgbnVtYmVyO1xuXG5sZXQgbXlWYXI6IFN0cmluZ09yTnVtYmVyO1xuXG5pbnRlcmZhY2UgRm9vIHt9XG5cbmNvbnN0IHg6IEZvbyA9IHt9OyJ9)

```
/*eslint no-use-before-define: ["error", { "typedefs": true, "ignoreTypeReferences": false }]*/

type StringOrNumber = string | number;

let myVar: StringOrNumber;

interface Foo {}

const x: Foo = {};
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

### ignoreTypeReferences (TypeScript only)

Examples of incorrect code for the `{ "ignoreTypeReferences": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcImlnbm9yZVR5cGVSZWZlcmVuY2VzXCI6IGZhbHNlIH1dKi9cblxubGV0IHZhcjE6IFN0cmluZ09yTnVtYmVyO1xuXG50eXBlIFN0cmluZ09yTnVtYmVyID0gc3RyaW5nIHwgbnVtYmVyO1xuXG5sZXQgdmFyMjogRW51bTtcblxuZW51bSBFbnVtIHt9In0=)

```
/*eslint no-use-before-define: ["error", { "ignoreTypeReferences": false }]*/

let var1: StringOrNumber;

type StringOrNumber = string | number;

let var2: Enum;

enum Enum {}
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

Examples of correct code for the `{ "ignoreTypeReferences": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcImlnbm9yZVR5cGVSZWZlcmVuY2VzXCI6IGZhbHNlIH1dKi9cblxudHlwZSBTdHJpbmdPck51bWJlciA9IHN0cmluZyB8IG51bWJlcjtcblxubGV0IG15VmFyOiBTdHJpbmdPck51bWJlcjtcblxuZW51bSBFbnVtIHt9XG5cbmxldCB2YXIyOiBFbnVtOyJ9)

```
/*eslint no-use-before-define: ["error", { "ignoreTypeReferences": false }]*/

type StringOrNumber = string | number;

let myVar: StringOrNumber;

enum Enum {}

let var2: Enum;
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

Examples of correct code for the `{ "ignoreTypeReferences": false }` with `{ "typedefs": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgeyBcImlnbm9yZVR5cGVSZWZlcmVuY2VzXCI6IGZhbHNlLCBcInR5cGVkZWZzXCI6IGZhbHNlLCB9XSovXG5cbmxldCBteVZhcjogU3RyaW5nT3JOdW1iZXI7XG5cbnR5cGUgU3RyaW5nT3JOdW1iZXIgPSBzdHJpbmcgfCBudW1iZXI7XG5cbmNvbnN0IHg6IEZvbyA9IHt9O1xuXG5pbnRlcmZhY2UgRm9vIHt9In0=)

```
/*eslint no-use-before-define: ["error", { "ignoreTypeReferences": false, "typedefs": false, }]*/

let myVar: StringOrNumber;

type StringOrNumber = string | number;

const x: Foo = {};

interface Foo {}
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

### nofunc

Examples of incorrect code for the `"nofunc"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIFwibm9mdW5jXCJdKi9cblxuYSgpO1xudmFyIGEgPSBmdW5jdGlvbigpIHt9O1xuXG5jb25zb2xlLmxvZyhmb28pO1xudmFyIGZvbyA9IDE7XG5cbmZ1bmN0aW9uIGYoKSB7XG4gICAgcmV0dXJuIGI7XG59XG52YXIgYiA9IDE7XG5cbm5ldyBBKCk7XG5jbGFzcyBBIHtcbn1cblxuZnVuY3Rpb24gZygpIHtcbiAgICByZXR1cm4gbmV3IEIoKTtcbn1cbmNsYXNzIEIge1xufVxuXG5leHBvcnQgZGVmYXVsdCBiYXI7XG5jb25zdCBiYXIgPSAxO1xuXG5leHBvcnQgeyBiYXogfTtcbmNvbnN0IGJheiA9IDE7In0=)

```
/*eslint no-use-before-define: ["error", "nofunc"]*/

a();
var a = function() {};

console.log(foo);
var foo = 1;

function f() {
    return b;
}
var b = 1;

new A();
class A {
}

function g() {
    return new B();
}
class B {
}

export default bar;
const bar = 1;

export { baz };
const baz = 1;
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
23
24
25
26
27
28
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgXCJub2Z1bmNcIl0qL1xuXG5mdW5jdGlvbiBmb28oKTogRm9vIHtcblx0cmV0dXJuIEZvby5GT087XG59XG5cdFxuZW51bSBGb28ge1xuXHRGT08sXG59In0=)

```
/*eslint no-use-before-define: ["error", "nofunc"]*/

function foo(): Foo {
	return Foo.FOO;
}
	
enum Foo {
	FOO,
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
```

Examples of correct code for the `"nofunc"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlLWJlZm9yZS1kZWZpbmU6IFtcImVycm9yXCIsIFwibm9mdW5jXCJdKi9cblxuZigpO1xuZnVuY3Rpb24gZigpIHt9XG5cbmNsYXNzIEEge1xufVxubmV3IEEoKTtcblxudmFyIGEgPSAxMDtcbmFsZXJ0KGEpO1xuXG5jb25zdCBmb28gPSAxO1xuZXhwb3J0IHsgZm9vIH07XG5cbmNvbnN0IGJhciA9IDE7XG5leHBvcnQgZGVmYXVsdCBiYXI7In0=)

```
/*eslint no-use-before-define: ["error", "nofunc"]*/

f();
function f() {}

class A {
}
new A();

var a = 10;
alert(a);

const foo = 1;
export { foo };

const bar = 1;
export default bar;
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
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11c2UtYmVmb3JlLWRlZmluZTogW1wiZXJyb3JcIiwgXCJub2Z1bmNcIl0qL1xuXHRcbmVudW0gRm9vIHtcblx0Rk9PLFxufVxuXG5jb25zdCBmb28gPSBGb28uRm9vOyJ9)

```
/*eslint no-use-before-define: ["error", "nofunc"]*/
	
enum Foo {
	FOO,
}

const foo = Foo.Foo;
1
2
3
4
5
6
7
```

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-use-before-define.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-use-before-define.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-use-before-define.md
                    
                
                )
