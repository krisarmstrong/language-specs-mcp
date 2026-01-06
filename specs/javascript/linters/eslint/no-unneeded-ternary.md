# no-unneeded-ternary

Disallow ternary operators when simpler alternatives exist

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [defaultAssignment](#defaultassignment)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

It’s a common mistake in JavaScript to use a conditional expression to select between two Boolean values instead of using `!` to convert the test to a Boolean. Here are some examples:

```
// Bad
const isYes = answer === 1 ? true : false;

// Good
const isYes = answer === 1;

// Bad
const isNo = answer === 1 ? false : true;

// Good
const isNo = answer !== 1;
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

Another common mistake is using a single variable as both the conditional test and the consequent. In such cases, the logical `OR` can be used to provide the same functionality. Here is an example:

```
// Bad
foo(bar ? bar : 1);

// Good
foo(bar || 1);
1
2
3
4
5
```

Copy code to clipboard

## Rule Details

This rule disallow ternary operators when simpler alternatives exist.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5uZWVkZWQtdGVybmFyeTogXCJlcnJvclwiKi9cblxuY29uc3QgYSA9IHggPT09IDIgPyB0cnVlIDogZmFsc2U7XG5cbmNvbnN0IGIgPSB4ID8gdHJ1ZSA6IGZhbHNlOyJ9)

```
/*eslint no-unneeded-ternary: "error"*/

const a = x === 2 ? true : false;

const b = x ? true : false;
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5uZWVkZWQtdGVybmFyeTogXCJlcnJvclwiKi9cblxuY29uc3QgYSA9IHggPT09IDIgPyBcIlllc1wiIDogXCJOb1wiO1xuXG5jb25zdCBiID0geCAhPT0gZmFsc2U7XG5cbmNvbnN0IGMgPSB4ID8gXCJZZXNcIiA6IFwiTm9cIjtcblxuY29uc3QgZCA9IHggPyB5IDogeDtcblxuZih4ID8geCA6IDEpOyAvLyBkZWZhdWx0IGFzc2lnbm1lbnQgLSB3b3VsZCBiZSBkaXNhbGxvd2VkIGlmIGRlZmF1bHRBc3NpZ25tZW50IG9wdGlvbiBzZXQgdG8gZmFsc2UuIFNlZSBvcHRpb24gZGV0YWlscyBiZWxvdy4ifQ==)

```
/*eslint no-unneeded-ternary: "error"*/

const a = x === 2 ? "Yes" : "No";

const b = x !== false;

const c = x ? "Yes" : "No";

const d = x ? y : x;

f(x ? x : 1); // default assignment - would be disallowed if defaultAssignment option set to false. See option details below.
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

## Options

This rule has an object option:

- `"defaultAssignment": true` (default) allows the conditional expression as a default assignment pattern
- `"defaultAssignment": false` disallows the conditional expression as a default assignment pattern

### defaultAssignment

When set to `true`, which it is by default, The `defaultAssignment` option allows expressions of the form `x ? x : expr` (where `x` is any identifier and `expr` is any expression).

Examples of additional incorrect code for this rule with the `{ "defaultAssignment": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5uZWVkZWQtdGVybmFyeTogW1wiZXJyb3JcIiwgeyBcImRlZmF1bHRBc3NpZ25tZW50XCI6IGZhbHNlIH1dKi9cblxuY29uc3QgYSA9IHggPyB4IDogMTtcblxuZih4ID8geCA6IDEpOyJ9)

```
/*eslint no-unneeded-ternary: ["error", { "defaultAssignment": false }]*/

const a = x ? x : 1;

f(x ? x : 1);
1
2
3
4
5
```

Note that `defaultAssignment: false` still allows expressions of the form `x ? expr : x` (where the identifier is on the right hand side of the ternary).

## When Not To Use It

You can turn this rule off if you are not concerned with unnecessary complexity in conditional expressions.

## Related Rules

- [no-ternary](/docs/latest/rules/no-ternary)
- [no-nested-ternary](/docs/latest/rules/no-nested-ternary)

## Version

This rule was introduced in ESLint v0.21.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unneeded-ternary.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unneeded-ternary.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unneeded-ternary.md
                    
                
                )
