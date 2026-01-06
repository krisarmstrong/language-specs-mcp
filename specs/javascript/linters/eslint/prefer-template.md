# prefer-template

Require template literals instead of string concatenation

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

In ES2015 (ES6), we can use template literals instead of string concatenation.

```
const str = "Hello, " + name + "!";
1
```

Copy code to clipboard

```
const str = `Hello, ${name}!`;
1
```

Copy code to clipboard

## Rule Details

This rule is aimed to flag usage of `+` operators with strings.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXRlbXBsYXRlOiBcImVycm9yXCIqL1xuXG5jb25zdCBzdHIgPSBcIkhlbGxvLCBcIiArIG5hbWUgKyBcIiFcIjtcbmNvbnN0IHN0cjEgPSBcIlRpbWU6IFwiICsgKDEyICogNjAgKiA2MCAqIDEwMDApOyJ9)

```
/*eslint prefer-template: "error"*/

const str = "Hello, " + name + "!";
const str1 = "Time: " + (12 * 60 * 60 * 1000);
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXRlbXBsYXRlOiBcImVycm9yXCIqL1xuXG5jb25zdCBzdHIgPSBcIkhlbGxvIFdvcmxkIVwiO1xuY29uc3Qgc3RyMSA9IGBIZWxsbywgJHtuYW1lfSFgO1xuY29uc3Qgc3RyMiA9IGBUaW1lOiAkezEyICogNjAgKiA2MCAqIDEwMDB9YDtcblxuLy8gVGhpcyBpcyByZXBvcnRlZCBieSBgbm8tdXNlbGVzcy1jb25jYXRgLlxuY29uc3Qgc3RyNCA9IFwiSGVsbG8sIFwiICsgXCJXb3JsZCFcIjsifQ==)

```
/*eslint prefer-template: "error"*/

const str = "Hello World!";
const str1 = `Hello, ${name}!`;
const str2 = `Time: ${12 * 60 * 60 * 1000}`;

// This is reported by `no-useless-concat`.
const str4 = "Hello, " + "World!";
1
2
3
4
5
6
7
8
```

## When Not To Use It

This rule should not be used in ES3/5 environments.

In ES2015 (ES6) or later, if you don’t want to be notified about string concatenation, you can safely disable this rule.

## Related Rules

- [no-useless-concat](/docs/latest/rules/no-useless-concat)
- [quotes](/docs/latest/rules/quotes)

## Version

This rule was introduced in ESLint v1.2.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-template.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-template.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-template.md
                    
                
                )
