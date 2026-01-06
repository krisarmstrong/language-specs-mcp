# no-octal-escape

Disallow octal escape sequences in string literals

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

As of the ECMAScript 5 specification, octal escape sequences in string literals are deprecated and should not be used. Unicode escape sequences should be used instead.

```
const foo = "Copyright \251";
1
```

Copy code to clipboard

## Rule Details

This rule disallows octal escape sequences in string literals.

If ESLint parses code in strict mode, the parser (instead of this rule) reports the error.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tb2N0YWwtZXNjYXBlOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSBcIkNvcHlyaWdodCBcXDI1MVwiOyJ9)

```
/*eslint no-octal-escape: "error"*/

const foo = "Copyright \251";
1
2
3
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tb2N0YWwtZXNjYXBlOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSBcIkNvcHlyaWdodCBcXHUwMEE5XCI7ICAgLy8gdW5pY29kZVxuXG5jb25zdCBidXogPSBcIkNvcHlyaWdodCBcXHhBOVwiOyAgICAgLy8gaGV4YWRlY2ltYWwifQ==)

```
/*eslint no-octal-escape: "error"*/

const foo = "Copyright \u00A9";   // unicode

const buz = "Copyright \xA9";     // hexadecimal
1
2
3
4
5
```

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-octal-escape.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-octal-escape.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-octal-escape.md
                    
                
                )
