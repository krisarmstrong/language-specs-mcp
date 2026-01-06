# no-template-curly-in-string

Disallow template literal placeholder syntax in regular strings

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

ECMAScript 6 allows programmers to create strings containing variable or expressions using template literals, instead of string concatenation, by writing expressions like `${variable}` between two backtick quotes (`). It can be easy to use the wrong quotes when wanting to use template literals, by writing `"${variable}"`, and end up with the literal value `"${variable}"` instead of a string containing the value of the injected expressions.

## Rule Details

This rule aims to warn when a regular string contains what looks like a template literal placeholder. It will warn when it finds a string containing the template literal placeholder (`${something}`) that uses either `"` or `'` for the quotes.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGVtcGxhdGUtY3VybHktaW4tc3RyaW5nOiBcImVycm9yXCIqL1xuXCJIZWxsbyAke25hbWV9IVwiO1xuJ0hlbGxvICR7bmFtZX0hJztcblwiVGltZTogJHsxMiAqIDYwICogNjAgKiAxMDAwfVwiOyJ9)

```
/*eslint no-template-curly-in-string: "error"*/
"Hello ${name}!";
'Hello ${name}!';
"Time: ${12 * 60 * 60 * 1000}";
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGVtcGxhdGUtY3VybHktaW4tc3RyaW5nOiBcImVycm9yXCIqL1xuYEhlbGxvICR7bmFtZX0hYDtcbmBUaW1lOiAkezEyICogNjAgKiA2MCAqIDEwMDB9YDtcblxudGVtcGxhdGVGdW5jdGlvbmBIZWxsbyAke25hbWV9YDsifQ==)

```
/*eslint no-template-curly-in-string: "error"*/
`Hello ${name}!`;
`Time: ${12 * 60 * 60 * 1000}`;

templateFunction`Hello ${name}`;
1
2
3
4
5
```

## When Not To Use It

This rule should not be used in ES3/5 environments.

## Version

This rule was introduced in ESLint v3.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-template-curly-in-string.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-template-curly-in-string.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-template-curly-in-string.md
                    
                
                )
