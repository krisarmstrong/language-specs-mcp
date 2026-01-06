# no-new-native-nonconstructor

Disallow `new` operators with global non-constructor functions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Handled by TypeScript](#handled_by_typescript)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Further Reading](#further-reading)
8. [Resources](#resources)

It is a convention in JavaScript that global variables beginning with an uppercase letter typically represent classes that can be instantiated using the `new` operator, such as `new Array` and `new Map`. Confusingly, JavaScript also provides some global variables that begin with an uppercase letter that cannot be called using the `new` operator and will throw an error if you attempt to do so. These are typically functions that are related to data types and are easy to mistake for classes. Consider the following example:

```
// throws a TypeError
const foo = new Symbol("foo");

// throws a TypeError
const result = new BigInt(9007199254740991);
1
2
3
4
5
```

Copy code to clipboard

Both `new Symbol` and `new BigInt` throw a type error because they are functions and not classes. It is easy to make this mistake by assuming the uppercase letters indicate classes.

## Rule Details

This rule is aimed at preventing the accidental calling of native JavaScript global functions with the `new` operator. These functions are:

- `Symbol`
- `BigInt`

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3LW5hdGl2ZS1ub25jb25zdHJ1Y3RvcjogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0gbmV3IFN5bWJvbCgnZm9vJyk7XG5jb25zdCBiYXIgPSBuZXcgQmlnSW50KDkwMDcxOTkyNTQ3NDA5OTEpOyJ9)

```
/*eslint no-new-native-nonconstructor: "error"*/

const foo = new Symbol('foo');
const bar = new BigInt(9007199254740991);
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3LW5hdGl2ZS1ub25jb25zdHJ1Y3RvcjogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0gU3ltYm9sKCdmb28nKTtcbmNvbnN0IGJhciA9IEJpZ0ludCg5MDA3MTk5MjU0NzQwOTkxKTtcblxuLy8gSWdub3JlcyBzaGFkb3dlZCBTeW1ib2wuXG5mdW5jdGlvbiBiYXooU3ltYm9sKSB7XG4gICAgY29uc3QgcXV4ID0gbmV3IFN5bWJvbChcImJhelwiKTtcbn1cbmZ1bmN0aW9uIHF1dXgoQmlnSW50KSB7XG4gICAgY29uc3QgY29yZ2UgPSBuZXcgQmlnSW50KDkwMDcxOTkyNTQ3NDA5OTEpO1xufVxuIn0=)

```
/*eslint no-new-native-nonconstructor: "error"*/

const foo = Symbol('foo');
const bar = BigInt(9007199254740991);

// Ignores shadowed Symbol.
function baz(Symbol) {
    const qux = new Symbol("baz");
}
function quux(BigInt) {
    const corge = new BigInt(9007199254740991);
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

## When Not To Use It

This rule should not be used in ES3/5 environments.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Related Rules

- [no-obj-calls](/docs/latest/rules/no-obj-calls)

## Version

This rule was introduced in ESLint v8.27.0.

## Further Reading

[ECMAScript® 2023 Language Specification](https://tc39.es/ecma262/#sec-symbol-constructor)
 tc39.es[ECMAScript® 2023 Language Specification](https://tc39.es/ecma262/#sec-bigint-constructor)
 tc39.es

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-new-native-nonconstructor.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-new-native-nonconstructor.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-new-native-nonconstructor.md
                    
                
                )
