# prefer-numeric-literals

Disallow `parseInt()` and `Number.parseInt()` in favor of binary, octal, and hexadecimal literals

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Compatibility](#compatibility)
4. [Version](#version)
5. [Resources](#resources)

The `parseInt()` and `Number.parseInt()` functions can be used to turn binary, octal, and hexadecimal strings into integers. As binary, octal, and hexadecimal literals are supported in ES6, this rule encourages use of those numeric literals instead of `parseInt()` or `Number.parseInt()`.

```
0b111110111 === 503;
0o767 === 503;
1
2
```

Copy code to clipboard

## Rule Details

This rule disallows calls to `parseInt()` or `Number.parseInt()` if called with two arguments: a string; and a radix option of 2 (binary), 8 (octal), or 16 (hexadecimal).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW51bWVyaWMtbGl0ZXJhbHM6IFwiZXJyb3JcIiovXG5cbnBhcnNlSW50KFwiMTExMTEwMTExXCIsIDIpID09PSA1MDM7XG5wYXJzZUludChgMTExMTEwMTExYCwgMikgPT09IDUwMztcbnBhcnNlSW50KFwiNzY3XCIsIDgpID09PSA1MDM7XG5wYXJzZUludChcIjFGN1wiLCAxNikgPT09IDUwMztcbk51bWJlci5wYXJzZUludChcIjExMTExMDExMVwiLCAyKSA9PT0gNTAzO1xuTnVtYmVyLnBhcnNlSW50KFwiNzY3XCIsIDgpID09PSA1MDM7XG5OdW1iZXIucGFyc2VJbnQoXCIxRjdcIiwgMTYpID09PSA1MDM7In0=)

```
/*eslint prefer-numeric-literals: "error"*/

parseInt("111110111", 2) === 503;
parseInt(`111110111`, 2) === 503;
parseInt("767", 8) === 503;
parseInt("1F7", 16) === 503;
Number.parseInt("111110111", 2) === 503;
Number.parseInt("767", 8) === 503;
Number.parseInt("1F7", 16) === 503;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW51bWVyaWMtbGl0ZXJhbHM6IFwiZXJyb3JcIiovXG5cbnBhcnNlSW50KDEpO1xucGFyc2VJbnQoMSwgMyk7XG5OdW1iZXIucGFyc2VJbnQoMSk7XG5OdW1iZXIucGFyc2VJbnQoMSwgMyk7XG5cbjBiMTExMTEwMTExID09PSA1MDM7XG4wbzc2NyA9PT0gNTAzO1xuMHgxRjcgPT09IDUwMztcblxuYVtwYXJzZUludF0oMSwyKTtcblxucGFyc2VJbnQoZm9vKTtcbnBhcnNlSW50KGZvbywgMik7XG5OdW1iZXIucGFyc2VJbnQoZm9vKTtcbk51bWJlci5wYXJzZUludChmb28sIDIpOyJ9)

```
/*eslint prefer-numeric-literals: "error"*/

parseInt(1);
parseInt(1, 3);
Number.parseInt(1);
Number.parseInt(1, 3);

0b111110111 === 503;
0o767 === 503;
0x1F7 === 503;

a[parseInt](1,2);

parseInt(foo);
parseInt(foo, 2);
Number.parseInt(foo);
Number.parseInt(foo, 2);
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

## When Not To Use It

If you want to allow use of `parseInt()` or `Number.parseInt()` for binary, octal, or hexadecimal integers, or if you are not using ES6 (because binary and octal literals are not supported in ES5 and below), you may wish to disable this rule.

## Compatibility

- JSCS: [requireNumericLiterals](https://jscs-dev.github.io/rule/requireNumericLiterals)

## Version

This rule was introduced in ESLint v3.5.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-numeric-literals.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-numeric-literals.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-numeric-literals.md
                    
                
                )
