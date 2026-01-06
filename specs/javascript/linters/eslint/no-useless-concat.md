# no-useless-concat

Disallow unnecessary concatenation of literals or template literals

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

It’s unnecessary to concatenate two strings together, such as:

```
const foo = "a" + "b";
1
```

Copy code to clipboard

This code is likely the result of refactoring where a variable was removed from the concatenation (such as `"a" + b + "b"`). In such a case, the concatenation isn’t important and the code can be rewritten as:

```
const foo = "ab";
1
```

Copy code to clipboard

## Rule Details

This rule aims to flag the concatenation of 2 literals when they could be combined into a single literal. Literals can be strings or template literals.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb25jYXQ6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSBgc29tZWAgKyBgc3RyaW5nYDtcblxuLy8gdGhlc2UgYXJlIHRoZSBzYW1lIGFzIFwiMTBcIlxuY29uc3QgYiA9ICcxJyArICcwJztcbmNvbnN0IGMgPSAnMScgKyBgMGA7XG5jb25zdCBkID0gYDFgICsgJzAnO1xuY29uc3QgZSA9IGAxYCArIGAwYDsifQ==)

```
/*eslint no-useless-concat: "error"*/

const a = `some` + `string`;

// these are the same as "10"
const b = '1' + '0';
const c = '1' + `0`;
const d = `1` + '0';
const e = `1` + `0`;
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb25jYXQ6IFwiZXJyb3JcIiovXG5cbi8vIHdoZW4gYSBub24gc3RyaW5nIGlzIGluY2x1ZGVkXG5jb25zdCBhID0gYSArIGI7XG5jb25zdCBiID0gJzEnICsgYTtcbmNvbnN0IGMgPSAxICsgJzEnO1xuY29uc3QgZCA9IDEgLSAyO1xuLy8gd2hlbiB0aGUgc3RyaW5nIGNvbmNhdGVuYXRpb24gaXMgbXVsdGlsaW5lXG5jb25zdCBlID0gXCJmb29cIiArXG4gICAgXCJiYXJcIjsifQ==)

```
/*eslint no-useless-concat: "error"*/

// when a non string is included
const a = a + b;
const b = '1' + a;
const c = 1 + '1';
const d = 1 - 2;
// when the string concatenation is multiline
const e = "foo" +
    "bar";
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

## When Not To Use It

If you don’t want to be notified about unnecessary string concatenation, you can safely disable this rule.

## Version

This rule was introduced in ESLint v1.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-concat.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-concat.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-concat.md
                    
                
                )
