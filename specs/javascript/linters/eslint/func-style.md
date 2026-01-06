# func-style

Enforce the consistent use of either `function` declarations or expressions assigned to variables

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [expression](#expression)
  2. [declaration](#declaration)
  3. [allowArrowFunctions](#allowarrowfunctions)
  4. [allowTypeAnnotation](#allowtypeannotation)
  5. [overrides](#overrides)

    1. [namedExports](#namedexports)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

There are two ways of defining functions in JavaScript: `function` declarations and function expressions assigned to variables. Function declarations are statements that begin with the `function` keyword. Function expressions can either be arrow functions or use the `function` keyword with an optional name. Here are some examples:

```
// function declaration
function doSomething() {
    // ...
}

// arrow function expression assigned to a variable
const doSomethingElse = () => {
    // ...
};

// function expression assigned to a variable
const doSomethingAgain = function() {
    // ...
};
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

Copy code to clipboard

The primary difference between `function` declarations and function expressions is that declarations are hoisted to the top of the scope in which they are defined, which allows you to write code that uses the function before its declaration. For example:

```
doSomething(); // ok

function doSomething() {
    // ...
}
1
2
3
4
5
```

Copy code to clipboard

For function expressions, you must define the function before it is used, otherwise it causes an error. Example:

```
doSomething();  // error!

const doSomething = function() {
    // ...
};
1
2
3
4
5
```

Copy code to clipboard

In this case, `doSomething` is `undefined` at the time of invocation and so causes a runtime error.

Due to these different behaviors, it is common to have guidelines as to which style of function should be used. There is really no correct or incorrect choice here, it is just a preference.

## Rule Details

This rule enforces a particular type of function style, either `function` declarations or expressions assigned to variables. You can specify which you prefer in the configuration.

Note: This rule does not apply to all functions. For example, a callback function passed as an argument to another function is not considered by this rule.

## Options

This rule has a string option:

- `"expression"` (default) requires the use of function expressions instead of function declarations
- `"declaration"` requires the use of function declarations instead of function expressions

This rule has an object option for two exceptions:

- `"allowArrowFunctions"`: `true` (default `false`) allows the use of arrow functions. This option applies only when the string option is set to `"declaration"` (arrow functions are always allowed when the string option is set to `"expression"`, regardless of this option)
- `"allowTypeAnnotation"`: `true` (default `false`) allows the use of function expressions and arrow functions when the variable declaration has type annotation, regardless of the `allowArrowFunctions` option. This option applies only when the string option is set to `"declaration"`. (TypeScript only)
- `"overrides"`: 

  - `"namedExports": "expression" | "declaration" | "ignore"`: used to override function styles in named exports 

    - `"expression"`: like string option
    - `"declaration"`: like string option
    - `"ignore"`: either style is acceptable

### expression

Examples of incorrect code for this rule with the default `"expression"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJleHByZXNzaW9uXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIC4uLlxufSJ9)

```
/*eslint func-style: ["error", "expression"]*/

function foo() {
    // ...
}
1
2
3
4
5
```

Examples of correct code for this rule with the default `"expression"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJleHByZXNzaW9uXCJdKi9cblxuY29uc3QgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgLy8gLi4uXG59O1xuXG5jb25zdCBmb28xID0gKCkgPT4ge307XG5cbi8vIGFsbG93ZWQgYXMgYWxsb3dBcnJvd0Z1bmN0aW9ucyA6IGZhbHNlIGlzIGFwcGxpZWQgb25seSBmb3IgZGVjbGFyYXRpb24ifQ==)

```
/*eslint func-style: ["error", "expression"]*/

const foo = function() {
    // ...
};

const foo1 = () => {};

// allowed as allowArrowFunctions : false is applied only for declaration
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

Overloaded function declarations are not reported as errors by this rule. These are functions that have multiple declarations with the same name but different parameter types or return types (commonly used in TypeScript to provide type information for different ways of calling the same function).

Examples of correct TypeScript code for this rule with the default `"expression"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBmdW5jLXN0eWxlOiBbXCJlcnJvclwiLCBcImV4cHJlc3Npb25cIl0qL1xuXG5mdW5jdGlvbiBwcm9jZXNzKHZhbHVlOiBzdHJpbmcpOiBzdHJpbmc7XG5mdW5jdGlvbiBwcm9jZXNzKHZhbHVlOiBudW1iZXIpOiBudW1iZXI7XG5mdW5jdGlvbiBwcm9jZXNzKHZhbHVlOiB1bmtub3duKSB7XG4gICAgcmV0dXJuIHZhbHVlO1xufSJ9)

```
/*eslint func-style: ["error", "expression"]*/

function process(value: string): string;
function process(value: number): number;
function process(value: unknown) {
    return value;
}
1
2
3
4
5
6
7
```

### declaration

Examples of incorrect code for this rule with the `"declaration"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJkZWNsYXJhdGlvblwiXSovXG5cbmNvbnN0IGZvbyA9IGZ1bmN0aW9uKCkge1xuICAgIC8vIC4uLlxufTtcblxuY29uc3QgZm9vMSA9ICgpID0+IHt9OyJ9)

```
/*eslint func-style: ["error", "declaration"]*/

const foo = function() {
    // ...
};

const foo1 = () => {};
1
2
3
4
5
6
7
```

Examples of correct code for this rule with the `"declaration"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJkZWNsYXJhdGlvblwiXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICAvLyAuLi5cbn1cblxuLy8gTWV0aG9kcyAoZnVuY3Rpb25zIGFzc2lnbmVkIHRvIG9iamVjdHMpIGFyZSBub3QgY2hlY2tlZCBieSB0aGlzIHJ1bGVcblNvbWVPYmplY3QuZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgLy8gLi4uXG59OyJ9)

```
/*eslint func-style: ["error", "declaration"]*/

function foo() {
    // ...
}

// Methods (functions assigned to objects) are not checked by this rule
SomeObject.foo = function() {
    // ...
};
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
```

### allowArrowFunctions

Examples of additional correct code for this rule with the `"declaration", { "allowArrowFunctions": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJkZWNsYXJhdGlvblwiLCB7IFwiYWxsb3dBcnJvd0Z1bmN0aW9uc1wiOiB0cnVlIH1dKi9cblxuY29uc3QgZm9vID0gKCkgPT4ge307In0=)

```
/*eslint func-style: ["error", "declaration", { "allowArrowFunctions": true }]*/

const foo = () => {};
1
2
3
```

### allowTypeAnnotation

Examples of incorrect TypeScript code for this rule with the `"declaration", { "allowTypeAnnotation": true }` options:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBmdW5jLXN0eWxlOiBbXCJlcnJvclwiLCBcImRlY2xhcmF0aW9uXCIsIHsgXCJhbGxvd1R5cGVBbm5vdGF0aW9uXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmb28gPSBmdW5jdGlvbigpOiB2b2lkIHt9OyJ9)

```
/*eslint func-style: ["error", "declaration", { "allowTypeAnnotation": true }]*/

const foo = function(): void {};
1
2
3
```

Examples of correct TypeScript code for this rule with the `"declaration", { "allowTypeAnnotation": true }` options:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBmdW5jLXN0eWxlOiBbXCJlcnJvclwiLCBcImRlY2xhcmF0aW9uXCIsIHsgXCJhbGxvd1R5cGVBbm5vdGF0aW9uXCI6IHRydWUgfV0qL1xuXG50eXBlIEZuID0gKCkgPT4gdW5kZWZpbmVkO1xuXG5jb25zdCBmb286IEZuID0gZnVuY3Rpb24oKSB7fTtcblxuY29uc3QgYmFyOiBGbiA9ICgpID0+IHt9OyJ9)

```
/*eslint func-style: ["error", "declaration", { "allowTypeAnnotation": true }]*/

type Fn = () => undefined;

const foo: Fn = function() {};

const bar: Fn = () => {};
1
2
3
4
5
6
7
```

### overrides

#### namedExports

##### expression

Examples of incorrect code for this rule with the `"declaration"` and `{"overrides": { "namedExports": "expression" }}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJkZWNsYXJhdGlvblwiLCB7IFwib3ZlcnJpZGVzXCI6IHsgXCJuYW1lZEV4cG9ydHNcIjogXCJleHByZXNzaW9uXCIgfSB9XSovXG5cbmV4cG9ydCBmdW5jdGlvbiBmb28oKSB7XG4gICAgLy8gLi4uXG59In0=)

```
/*eslint func-style: ["error", "declaration", { "overrides": { "namedExports": "expression" } }]*/

export function foo() {
    // ...
}
1
2
3
4
5
```

Examples of correct code for this rule with the `"declaration"` and `{"overrides": { "namedExports": "expression" }}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJkZWNsYXJhdGlvblwiLCB7IFwib3ZlcnJpZGVzXCI6IHsgXCJuYW1lZEV4cG9ydHNcIjogXCJleHByZXNzaW9uXCIgfSB9XSovXG5cbmV4cG9ydCBjb25zdCBmb28gPSBmdW5jdGlvbigpIHtcbiAgICAvLyAuLi5cbn07XG5cbmV4cG9ydCBjb25zdCBiYXIgPSAoKSA9PiB7fTsifQ==)

```
/*eslint func-style: ["error", "declaration", { "overrides": { "namedExports": "expression" } }]*/

export const foo = function() {
    // ...
};

export const bar = () => {};
1
2
3
4
5
6
7
```

##### declaration

Examples of incorrect code for this rule with the `"expression"` and `{"overrides": { "namedExports": "declaration" }}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJleHByZXNzaW9uXCIsIHsgXCJvdmVycmlkZXNcIjogeyBcIm5hbWVkRXhwb3J0c1wiOiBcImRlY2xhcmF0aW9uXCIgfSB9XSovXG5cbmV4cG9ydCBjb25zdCBmb28gPSBmdW5jdGlvbigpIHtcbiAgICAvLyAuLi5cbn07XG5cbmV4cG9ydCBjb25zdCBiYXIgPSAoKSA9PiB7fTsifQ==)

```
/*eslint func-style: ["error", "expression", { "overrides": { "namedExports": "declaration" } }]*/

export const foo = function() {
    // ...
};

export const bar = () => {};
1
2
3
4
5
6
7
```

Examples of correct code for this rule with the `"expression"` and `{"overrides": { "namedExports": "declaration" }}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJleHByZXNzaW9uXCIsIHsgXCJvdmVycmlkZXNcIjogeyBcIm5hbWVkRXhwb3J0c1wiOiBcImRlY2xhcmF0aW9uXCIgfSB9XSovXG5cbmV4cG9ydCBmdW5jdGlvbiBmb28oKSB7XG4gICAgLy8gLi4uXG59In0=)

```
/*eslint func-style: ["error", "expression", { "overrides": { "namedExports": "declaration" } }]*/

export function foo() {
    // ...
}
1
2
3
4
5
```

Examples of correct code for this rule with the `"expression"` and `{ "allowTypeAnnotation": true, "overrides": { "namedExports": "declaration" }}` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBmdW5jLXN0eWxlOiBbXCJlcnJvclwiLCBcImV4cHJlc3Npb25cIiwgeyBcImFsbG93VHlwZUFubm90YXRpb25cIjogdHJ1ZSwgXCJvdmVycmlkZXNcIjogeyBcIm5hbWVkRXhwb3J0c1wiOiBcImRlY2xhcmF0aW9uXCIgfSB9XSovXG5cbmV4cG9ydCBjb25zdCBmb286ICgpID0+IHZvaWQgPSBmdW5jdGlvbiAoKSB7fSJ9)

```
/*eslint func-style: ["error", "expression", { "allowTypeAnnotation": true, "overrides": { "namedExports": "declaration" } }]*/

export const foo: () => void = function () {}
1
2
3
```

##### ignore

Examples of correct code for this rule with the `{"overrides": { "namedExports": "ignore" }}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1zdHlsZTogW1wiZXJyb3JcIiwgXCJleHByZXNzaW9uXCIsIHsgXCJvdmVycmlkZXNcIjogeyBcIm5hbWVkRXhwb3J0c1wiOiBcImlnbm9yZVwiIH0gfV0qL1xuXG5leHBvcnQgY29uc3QgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgLy8gLi4uXG59O1xuXG5leHBvcnQgY29uc3QgYmFyID0gKCkgPT4ge307XG5cbmV4cG9ydCBmdW5jdGlvbiBiYXooKSB7XG4gICAgLy8gLi4uXG59In0=)

```
/*eslint func-style: ["error", "expression", { "overrides": { "namedExports": "ignore" } }]*/

export const foo = function() {
    // ...
};

export const bar = () => {};

export function baz() {
    // ...
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

## When Not To Use It

If you want to allow developers to each decide how they want to write functions on their own, then you can disable this rule.

## Version

This rule was introduced in ESLint v0.2.0.

## Further Reading

[JavaScript Scoping and Hoisting](https://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)
 www.adequatelygood.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/func-style.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/func-style.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/func-style.md
                    
                
                )
