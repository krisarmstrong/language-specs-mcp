# no-new

Disallow `new` operators outside of assignments or comparisons

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

The goal of using `new` with a constructor is typically to create an object of a particular type and store that object in a variable, such as:

```
const person = new Person();
1
```

Copy code to clipboard

It’s less common to use `new` and not store the result, such as:

```
new Person();
1
```

Copy code to clipboard

In this case, the created object is thrown away because its reference isn’t stored anywhere, and in many cases, this means that the constructor should be replaced with a function that doesn’t require `new` to be used.

## Rule Details

This rule is aimed at maintaining consistency and convention by disallowing constructor calls using the `new` keyword that do not assign the resulting object to a variable.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3OiBcImVycm9yXCIqL1xuXG5uZXcgVGhpbmcoKTsifQ==)

```
/*eslint no-new: "error"*/

new Thing();
1
2
3
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3OiBcImVycm9yXCIqL1xuXG5jb25zdCB0aGluZyA9IG5ldyBUaGluZygpO1xuXG5Gb28oKTsifQ==)

```
/*eslint no-new: "error"*/

const thing = new Thing();

Foo();
1
2
3
4
5
```

## Version

This rule was introduced in ESLint v0.0.7.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-new.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-new.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-new.md
                    
                
                )
