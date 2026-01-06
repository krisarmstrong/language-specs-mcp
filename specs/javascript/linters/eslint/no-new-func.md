# no-new-func

Disallow `new` operators with the `Function` object

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

It’s possible to create functions in JavaScript from strings at runtime using the `Function` constructor, such as:

```
const a = new Function("a", "b", "return a + b");
const b = Function("a", "b", "return a + b");
const c = Function.call(null, "a", "b", "return a + b");
const d = Function.apply(null, ["a", "b", "return a + b"]);
const x = Function.bind(null, "a", "b", "return a + b")();
1
2
3
4
5
```

Copy code to clipboard

This is considered by many to be a bad practice due to the difficulty in debugging and reading these types of functions. In addition, Content-Security-Policy (CSP) directives may disallow the use of `eval()` and similar methods for creating code from strings.

## Rule Details

This error is raised to highlight the use of a bad practice. By passing a string to the `Function` constructor, you are requiring the engine to parse that string much in the way it has to when you call the `eval` function.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3LWZ1bmM6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSBuZXcgRnVuY3Rpb24oXCJhXCIsIFwiYlwiLCBcInJldHVybiBhICsgYlwiKTtcbmNvbnN0IGIgPSBGdW5jdGlvbihcImFcIiwgXCJiXCIsIFwicmV0dXJuIGEgKyBiXCIpO1xuY29uc3QgYyA9IEZ1bmN0aW9uLmNhbGwobnVsbCwgXCJhXCIsIFwiYlwiLCBcInJldHVybiBhICsgYlwiKTtcbmNvbnN0IGQgPSBGdW5jdGlvbi5hcHBseShudWxsLCBbXCJhXCIsIFwiYlwiLCBcInJldHVybiBhICsgYlwiXSk7XG5jb25zdCB4ID0gRnVuY3Rpb24uYmluZChudWxsLCBcImFcIiwgXCJiXCIsIFwicmV0dXJuIGEgKyBiXCIpKCk7XG5jb25zdCB5ID0gRnVuY3Rpb24uYmluZChudWxsLCBcImFcIiwgXCJiXCIsIFwicmV0dXJuIGEgKyBiXCIpOyAvLyBhc3N1bWluZyB0aGF0IHRoZSByZXN1bHQgb2YgRnVuY3Rpb24uYmluZCguLi4pIHdpbGwgYmUgZXZlbnR1YWxseSBjYWxsZWQuIn0=)

```
/*eslint no-new-func: "error"*/

const a = new Function("a", "b", "return a + b");
const b = Function("a", "b", "return a + b");
const c = Function.call(null, "a", "b", "return a + b");
const d = Function.apply(null, ["a", "b", "return a + b"]);
const x = Function.bind(null, "a", "b", "return a + b")();
const y = Function.bind(null, "a", "b", "return a + b"); // assuming that the result of Function.bind(...) will be eventually called.
1
2
3
4
5
6
7
8
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3LWZ1bmM6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHggPSBmdW5jdGlvbiAoYSwgYikge1xuICAgIHJldHVybiBhICsgYjtcbn07In0=)

```
/*eslint no-new-func: "error"*/

const x = function (a, b) {
    return a + b;
};
1
2
3
4
5
```

## When Not To Use It

In more advanced cases where you really need to use the `Function` constructor.

## Version

This rule was introduced in ESLint v0.0.7.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-new-func.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-new-func.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-new-func.md
                    
                
                )
