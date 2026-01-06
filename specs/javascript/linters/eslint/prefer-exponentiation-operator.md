# prefer-exponentiation-operator

Disallow the use of `Math.pow` in favor of the `**` operator

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Introduced in ES2016, the infix exponentiation operator `**` is an alternative for the standard `Math.pow` function.

Infix notation is considered to be more readable and thus more preferable than the function notation.

## Rule Details

This rule disallows calls to `Math.pow` and suggests using the `**` operator instead.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWV4cG9uZW50aWF0aW9uLW9wZXJhdG9yOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSBNYXRoLnBvdygyLCA4KTtcblxuY29uc3QgYmFyID0gTWF0aC5wb3coYSwgYik7XG5cbmxldCBiYXogPSBNYXRoLnBvdyhhICsgYiwgYyArIGQpO1xuXG5sZXQgcXV1eCA9IE1hdGgucG93KC0xLCBuKTsifQ==)

```
/*eslint prefer-exponentiation-operator: "error"*/

const foo = Math.pow(2, 8);

const bar = Math.pow(a, b);

let baz = Math.pow(a + b, c + d);

let quux = Math.pow(-1, n);
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWV4cG9uZW50aWF0aW9uLW9wZXJhdG9yOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSAyICoqIDg7XG5cbmNvbnN0IGJhciA9IGEgKiogYjtcblxubGV0IGJheiA9IChhICsgYikgKiogKGMgKyBkKTtcblxubGV0IHF1dXggPSAoLTEpICoqIG47In0=)

```
/*eslint prefer-exponentiation-operator: "error"*/

const foo = 2 ** 8;

const bar = a ** b;

let baz = (a + b) ** (c + d);

let quux = (-1) ** n;
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

## When Not To Use It

This rule should not be used unless ES2016 is supported in your codebase.

## Version

This rule was introduced in ESLint v6.7.0.

## Further Reading

[Exponentiation (**) - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
 developer.mozilla.org[5848 - v8 - V8 JavaScript Engine - Monorail](https://bugs.chromium.org/p/v8/issues/detail?id=5848)
 bugs.chromium.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-exponentiation-operator.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-exponentiation-operator.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-exponentiation-operator.md
                    
                
                )
