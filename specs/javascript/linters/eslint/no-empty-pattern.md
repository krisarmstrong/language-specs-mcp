# no-empty-pattern

Disallow empty destructuring patterns

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowObjectPatternsAsParameters](#allowobjectpatternsasparameters)

3. [Version](#version)
4. [Resources](#resources)

When using destructuring, it’s possible to create a pattern that has no effect. This happens when empty curly braces are used to the right of an embedded object destructuring pattern, such as:

```
// doesn't create any variables
const {a: {}} = foo;
1
2
```

Copy code to clipboard

In this code, no new variables are created because `a` is just a location helper while the `{}` is expected to contain the variables to create, such as:

```
// creates variable b
const {a: { b }} = foo;
1
2
```

Copy code to clipboard

In many cases, the empty object pattern is a mistake where the author intended to use a default value instead, such as:

```
// creates variable a
const {a = {}} = foo;
1
2
```

Copy code to clipboard

The difference between these two patterns is subtle, especially because the problematic empty pattern looks just like an object literal.

## Rule Details

This rule aims to flag any empty patterns in destructured objects and arrays, and as such, will report a problem whenever one is encountered.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktcGF0dGVybjogXCJlcnJvclwiKi9cblxuY29uc3Qge30gPSBmb287XG5jb25zdCBbXSA9IGZvbztcbmNvbnN0IHthOiB7fX0gPSBmb287XG5jb25zdCB7YTogW119ID0gZm9vO1xuZnVuY3Rpb24gZm9vKHt9KSB7fVxuZnVuY3Rpb24gYmFyKFtdKSB7fVxuZnVuY3Rpb24gYmF6KHthOiB7fX0pIHt9XG5mdW5jdGlvbiBxdXgoe2E6IFtdfSkge30ifQ==)

```
/*eslint no-empty-pattern: "error"*/

const {} = foo;
const [] = foo;
const {a: {}} = foo;
const {a: []} = foo;
function foo({}) {}
function bar([]) {}
function baz({a: {}}) {}
function qux({a: []}) {}
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktcGF0dGVybjogXCJlcnJvclwiKi9cblxuY29uc3Qge2EgPSB7fX0gPSBmb287XG5jb25zdCB7YiA9IFtdfSA9IGZvbztcbmZ1bmN0aW9uIGZvbyh7YSA9IHt9fSkge31cbmZ1bmN0aW9uIGJhcih7YSA9IFtdfSkge30ifQ==)

```
/*eslint no-empty-pattern: "error"*/

const {a = {}} = foo;
const {b = []} = foo;
function foo({a = {}}) {}
function bar({a = []}) {}
1
2
3
4
5
6
```

## Options

This rule has an object option for exceptions:

### allowObjectPatternsAsParameters

Set to `false` by default. Setting this option to `true` allows empty object patterns as function parameters.

Note: This rule doesn’t allow empty array patterns as function parameters.

Examples of incorrect code for this rule with the `{"allowObjectPatternsAsParameters": true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktcGF0dGVybjogW1wiZXJyb3JcIiwgeyBcImFsbG93T2JqZWN0UGF0dGVybnNBc1BhcmFtZXRlcnNcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGZvbyh7YToge319KSB7fVxuY29uc3QgYmFyID0gZnVuY3Rpb24oe2E6IHt9fSkge307XG5jb25zdCBxdXggPSAoe2E6IHt9fSkgPT4ge307XG5jb25zdCBxdXV4ID0gKHt9ID0gYmFyKSA9PiB7fTtcbmNvbnN0IGl0ZW0gPSAoe30gPSB7IGJhcjogMSB9KSA9PiB7fTtcblxuZnVuY3Rpb24gYmF6KFtdKSB7fSJ9)

```
/*eslint no-empty-pattern: ["error", { "allowObjectPatternsAsParameters": true }]*/

function foo({a: {}}) {}
const bar = function({a: {}}) {};
const qux = ({a: {}}) => {};
const quux = ({} = bar) => {};
const item = ({} = { bar: 1 }) => {};

function baz([]) {}
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

Examples of correct code for this rule with the `{"allowObjectPatternsAsParameters": true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktcGF0dGVybjogW1wiZXJyb3JcIiwgeyBcImFsbG93T2JqZWN0UGF0dGVybnNBc1BhcmFtZXRlcnNcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGZvbyh7fSkge31cbmNvbnN0IGJhciA9IGZ1bmN0aW9uKHt9KSB7fTtcbmNvbnN0IHF1eCA9ICh7fSkgPT4ge307XG5cbmZ1bmN0aW9uIGJheih7fSA9IHt9KSB7fSJ9)

```
/*eslint no-empty-pattern: ["error", { "allowObjectPatternsAsParameters": true }]*/

function foo({}) {}
const bar = function({}) {};
const qux = ({}) => {};

function baz({} = {}) {}
1
2
3
4
5
6
7
```

## Version

This rule was introduced in ESLint v1.7.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-empty-pattern.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-empty-pattern.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-empty-pattern.md
                    
                
                )
