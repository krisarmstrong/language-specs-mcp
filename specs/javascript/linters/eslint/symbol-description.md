# symbol-description

Require symbol descriptions

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

The `Symbol` function may have an optional description:

```
const foo = Symbol("some description");

const someString = "some description";
const bar = Symbol(someString);
1
2
3
4
```

Copy code to clipboard

Using `description` promotes easier debugging: when a symbol is logged the description is used:

```
const foo = Symbol("some description");

> console.log(foo);
// Symbol(some description)
1
2
3
4
```

Copy code to clipboard

It may facilitate identifying symbols when one is observed during debugging.

## Rule Details

This rules requires a description when creating symbols.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc3ltYm9sLWRlc2NyaXB0aW9uOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSBTeW1ib2woKTsifQ==)

```
/*eslint symbol-description: "error"*/

const foo = Symbol();
1
2
3
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc3ltYm9sLWRlc2NyaXB0aW9uOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSBTeW1ib2woXCJzb21lIGRlc2NyaXB0aW9uXCIpO1xuXG5jb25zdCBzb21lU3RyaW5nID0gXCJzb21lIGRlc2NyaXB0aW9uXCI7XG5jb25zdCBiYXIgPSBTeW1ib2woc29tZVN0cmluZyk7In0=)

```
/*eslint symbol-description: "error"*/

const foo = Symbol("some description");

const someString = "some description";
const bar = Symbol(someString);
1
2
3
4
5
6
```

## When Not To Use It

This rule should not be used in ES3/5 environments. In addition, this rule can be safely turned off if you don’t want to enforce presence of `description` when creating Symbols.

## Version

This rule was introduced in ESLint v3.4.0.

## Further Reading

[ECMAScript 2015 Language Specification – ECMA-262 6th Edition](https://www.ecma-international.org/ecma-262/6.0/#sec-symbol-description)
 www.ecma-international.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/symbol-description.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/symbol-description.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/symbol-description.md
                    
                
                )
