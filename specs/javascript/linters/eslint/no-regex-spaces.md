# no-regex-spaces

Disallow multiple spaces in regular expressions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Regular expressions can be very complex and difficult to understand, which is why it’s important to keep them as simple as possible in order to avoid mistakes. One of the more error-prone things you can do with a regular expression is to use more than one space, such as:

```
const re = /foo   bar/;
1
```

Copy code to clipboard

In this regular expression, it’s very hard to tell how many spaces are intended to be matched. It’s better to use only one space and then specify how many spaces are expected, such as:

```
const re = /foo {3}bar/;
1
```

Copy code to clipboard

Now it is very clear that three spaces are expected to be matched.

## Rule Details

This rule disallows multiple spaces in regular expression literals.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVnZXgtc3BhY2VzOiBcImVycm9yXCIqL1xuXG5jb25zdCByZSA9IC9mb28gICBiYXIvO1xuY29uc3QgcmUxID0gbmV3IFJlZ0V4cChcImZvbyAgIGJhclwiKTsifQ==)

```
/*eslint no-regex-spaces: "error"*/

const re = /foo   bar/;
const re1 = new RegExp("foo   bar");
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVnZXgtc3BhY2VzOiBcImVycm9yXCIqL1xuXG5jb25zdCByZSA9IC9mb28gezN9YmFyLztcbmNvbnN0IHJlMSA9IG5ldyBSZWdFeHAoXCJmb28gezN9YmFyXCIpOyJ9)

```
/*eslint no-regex-spaces: "error"*/

const re = /foo {3}bar/;
const re1 = new RegExp("foo {3}bar");
1
2
3
4
```

## When Not To Use It

If you want to allow multiple spaces in a regular expression, then you can safely turn this rule off.

## Related Rules

- [no-div-regex](/docs/latest/rules/no-div-regex)
- [no-control-regex](/docs/latest/rules/no-control-regex)

## Version

This rule was introduced in ESLint v0.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-regex-spaces.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-regex-spaces.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-regex-spaces.md
                    
                
                )
