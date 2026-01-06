# no-func-assign

Disallow reassigning `function` declarations

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Handled by TypeScript](#handled_by_typescript)
3. [Version](#version)
4. [Resources](#resources)

JavaScript functions can be written as a FunctionDeclaration `function foo() { ... }` or as a FunctionExpression `const foo = function() { ... };`. While a JavaScript interpreter might tolerate it, overwriting/reassigning a function written as a FunctionDeclaration is often indicative of a mistake or issue.

```
function foo() {}
foo = bar;
1
2
```

Copy code to clipboard

## Rule Details

This rule disallows reassigning `function` declarations.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZnVuYy1hc3NpZ246IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbygpIHt9XG5mb28gPSBiYXI7XG5cbmZ1bmN0aW9uIGJheigpIHtcbiAgICBiYXogPSBiYXI7XG59XG5cbmxldCBhID0gZnVuY3Rpb24gaGVsbG8oKSB7XG4gIGhlbGxvID0gMTIzO1xufTsifQ==)

```
/*eslint no-func-assign: "error"*/

function foo() {}
foo = bar;

function baz() {
    baz = bar;
}

let a = function hello() {
  hello = 123;
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
```

Examples of incorrect code for this rule, unlike the corresponding rule in JSHint:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZnVuYy1hc3NpZ246IFwiZXJyb3JcIiovXG5cbmZvbyA9IGJhcjtcbmZ1bmN0aW9uIGZvbygpIHt9In0=)

```
/*eslint no-func-assign: "error"*/

foo = bar;
function foo() {}
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZnVuYy1hc3NpZ246IFwiZXJyb3JcIiovXG5cbmxldCBmb28gPSBmdW5jdGlvbiAoKSB7fVxuZm9vID0gYmFyO1xuXG5mdW5jdGlvbiBiYXooYmF6KSB7IC8vIGBiYXpgIGlzIHNoYWRvd2VkLlxuICAgIGJheiA9IGJhcjtcbn1cblxuZnVuY3Rpb24gcXV4KCkge1xuICAgIGNvbnN0IHF1eCA9IGJhcjsgIC8vIGBxdXhgIGlzIHNoYWRvd2VkLlxufSJ9)

```
/*eslint no-func-assign: "error"*/

let foo = function () {}
foo = bar;

function baz(baz) { // `baz` is shadowed.
    baz = bar;
}

function qux() {
    const qux = bar;  // `qux` is shadowed.
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

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-func-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-func-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-func-assign.md
                    
                
                )
