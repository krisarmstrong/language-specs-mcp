# init-declarations

Require or disallow initialization in variable declarations

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [never](#never)
  3. [ignoreForLoopInit](#ignoreforloopinit)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

In JavaScript, variables can be assigned during declaration, or at any point afterwards using an assignment statement. For example, in the following code, `foo` is initialized during declaration, while `bar` is initialized later.

```
let foo = 1;
let bar;

if (foo) {
    bar = 1;
} else {
    bar = 2;
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

Copy code to clipboard

## Rule Details

This rule is aimed at enforcing or eliminating variable initializations during declaration. For example, in the following code, `foo` is initialized during declaration, while `bar` is not.

```
let foo = 1;
let bar;

bar = 2;
1
2
3
4
```

Copy code to clipboard

This rule aims to bring consistency to variable initializations and declarations.

## Options

The rule takes two options:

1. A string which must be either `"always"` (the default), to enforce initialization at declaration, or `"never"` to disallow initialization during declaration. This rule applies to `var`, `let`, `const`, `using`, and `await using` variables, however `"never"` is ignored for `const`, `using`, and `await using` variables, as not initializing these variables would generate a parse error.
2. An object that further controls the behavior of this rule. Currently, the only available parameter is `ignoreForLoopInit`, which indicates if initialization at declaration is allowed in `for` loops when `"never"` is set, since it is a very typical use case.

You can configure the rule as follows:

Variables must be initialized at declaration (default)

```
{
    "init-declarations": ["error", "always"],
}
1
2
3
```

Copy code to clipboard

Variables must not be initialized at declaration

```
{
    "init-declarations": ["error", "never"]
}
1
2
3
```

Copy code to clipboard

Variables must not be initialized at declaration, except in for loops, where it is allowed

```
{
    "init-declarations": ["error", "never", { "ignoreForLoopInit": true }]
}
1
2
3
```

Copy code to clipboard

### always

Examples of incorrect code for the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIHZhciBiYXI7XG4gICAgbGV0IGJhejtcbn0ifQ==)

```
/*eslint init-declarations: ["error", "always"]*/

function foo() {
    var bar;
    let baz;
}
1
2
3
4
5
6
```

Examples of correct code for the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIHZhciBiYXIgPSAxO1xuICAgIGxldCBiYXogPSAyO1xuICAgIGNvbnN0IHF1eCA9IDM7XG5cdHVzaW5nIHF1dXggPSBnZXRTb21ldGhpbmcoKTtcbn1cblxuYXN5bmMgZnVuY3Rpb24gZm9vYmFyKCkge1xuXHRhd2FpdCB1c2luZyBxdXV4ID0gZ2V0U29tZXRoaW5nKCk7XG59In0=)

```
/*eslint init-declarations: ["error", "always"]*/

function foo() {
    var bar = 1;
    let baz = 2;
    const qux = 3;
	using quux = getSomething();
}

async function foobar() {
	await using quux = getSomething();
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

### never

Examples of incorrect code for the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwibmV2ZXJcIl0qL1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgdmFyIGJhciA9IDE7XG4gICAgbGV0IGJheiA9IDI7XG5cbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IDE7IGkrKykge31cbn0ifQ==)

```
/*eslint init-declarations: ["error", "never"]*/

function foo() {
    var bar = 1;
    let baz = 2;

    for (let i = 0; i < 1; i++) {}
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

Examples of correct code for the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwibmV2ZXJcIl0qL1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgdmFyIGJhcjtcbiAgICBsZXQgYmF6O1xuICAgIGNvbnN0IGJ1enogPSAxO1xuXHR1c2luZyBxdXV4ID0gZ2V0U29tZXRoaW5nKCk7XG59XG5cbmFzeW5jIGZ1bmN0aW9uIGZvb2JhcigpIHtcblx0YXdhaXQgdXNpbmcgcXV1eCA9IGdldFNvbWV0aGluZygpO1xufSJ9)

```
/*eslint init-declarations: ["error", "never"]*/

function foo() {
    var bar;
    let baz;
    const buzz = 1;
	using quux = getSomething();
}

async function foobar() {
	await using quux = getSomething();
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

The `"never"` option ignores `const`, `using`, and `await using` variable initializations.

### ignoreForLoopInit

Examples of correct code for the `"never", { "ignoreForLoopInit": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwibmV2ZXJcIiwgeyBcImlnbm9yZUZvckxvb3BJbml0XCI6IHRydWUgfV0qL1xuZm9yIChsZXQgaSA9IDA7IGkgPCAxOyBpKyspIHt9In0=)

```
/*eslint init-declarations: ["error", "never", { "ignoreForLoopInit": true }]*/
for (let i = 0; i < 1; i++) {}
1
2
```

This rule additionally supports TypeScript type syntax.

Examples of incorrect TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwibmV2ZXJcIl0gKi9cblxubGV0IGFycjogc3RyaW5nW10gPSBbJ2FycicsICdhciddO1xuXG5jb25zdCBjbGFzczEgPSBjbGFzcyBOQU1FIHtcblx0Y29uc3RydWN0b3IoKSB7XG5cdCAgdmFyIG5hbWUxOiBzdHJpbmcgPSAnaGVsbG8nO1xuXHR9XG59O1xuXG5uYW1lc3BhY2UgbXlMaWIge1xuXHRsZXQgbnVtYmVyT2ZHcmVldGluZ3M6IG51bWJlciA9IDI7XG59XG4ifQ==)

```
/* eslint init-declarations: ["error", "never"] */

let arr: string[] = ['arr', 'ar'];

const class1 = class NAME {
	constructor() {
	  var name1: string = 'hello';
	}
};

namespace myLib {
	let numberOfGreetings: number = 2;
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

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdICovXG5cbm5hbWVzcGFjZSBteUxpYiB7XG5cdGxldCBudW1iZXJPZkdyZWV0aW5nczogbnVtYmVyO1xufVxuXG5uYW1lc3BhY2UgbXlMaWIxIHtcblx0Y29uc3QgZm9vOiBudW1iZXI7XG5cdG5hbWVzcGFjZSBteUxpYjIge1xuXHQgIGxldCBiYXI6IHN0cmluZztcblx0ICBuYW1lc3BhY2UgbXlMaWIzIHtcblx0XHRsZXQgYmF6OiBvYmplY3Q7XG5cdCAgfVxuXHR9XG59XG4ifQ==)

```
/* eslint init-declarations: ["error", "always"] */

namespace myLib {
	let numberOfGreetings: number;
}

namespace myLib1 {
	const foo: number;
	namespace myLib2 {
	  let bar: string;
	  namespace myLib3 {
		let baz: object;
	  }
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
```

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwibmV2ZXJcIl0gKi9cblxuZGVjbGFyZSBjb25zdCBmb286IG51bWJlcjtcblxuZGVjbGFyZSBuYW1lc3BhY2UgbXlMaWIge1xuXHRsZXQgbnVtYmVyT2ZHcmVldGluZ3M6IG51bWJlcjtcbn1cblxuaW50ZXJmYWNlIEdyZWV0aW5nU2V0dGluZ3Mge1xuXHRncmVldGluZzogc3RyaW5nO1xuXHRkdXJhdGlvbj86IG51bWJlcjtcblx0Y29sb3I/OiBzdHJpbmc7XG59In0=)

```
/* eslint init-declarations: ["error", "never"] */

declare const foo: number;

declare namespace myLib {
	let numberOfGreetings: number;
}

interface GreetingSettings {
	greeting: string;
	duration?: number;
	color?: string;
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
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgaW5pdC1kZWNsYXJhdGlvbnM6IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdICovXG5cbmRlY2xhcmUgY29uc3QgZm9vOiBudW1iZXI7XG5cbmRlY2xhcmUgbmFtZXNwYWNlIG15TGliIHtcblx0bGV0IG51bWJlck9mR3JlZXRpbmdzOiBudW1iZXI7XG59XG5cbmludGVyZmFjZSBHcmVldGluZ1NldHRpbmdzIHtcblx0Z3JlZXRpbmc6IHN0cmluZztcblx0ZHVyYXRpb24/OiBudW1iZXI7XG5cdGNvbG9yPzogc3RyaW5nO1xufVxuIn0=)

```
/* eslint init-declarations: ["error", "always"] */

declare const foo: number;

declare namespace myLib {
	let numberOfGreetings: number;
}

interface GreetingSettings {
	greeting: string;
	duration?: number;
	color?: string;
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

## When Not To Use It

When you are indifferent as to how your variables are initialized.

## Related Rules

- [no-unassigned-vars](/docs/latest/rules/no-unassigned-vars)

## Version

This rule was introduced in ESLint v1.0.0-rc-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/init-declarations.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/init-declarations.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/init-declarations.md
                    
                
                )
