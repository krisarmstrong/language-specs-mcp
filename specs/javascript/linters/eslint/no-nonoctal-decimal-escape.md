# no-nonoctal-decimal-escape

Disallow `\8` and `\9` escape sequences in string literals

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Although not being specified in the language until ECMAScript 2021, `\8` and `\9` escape sequences in string literals were allowed in most JavaScript engines, and treated as “useless” escapes:

```
"\8" === "8"; // true
"\9" === "9"; // true
1
2
```

Copy code to clipboard

Since ECMAScript 2021, these escape sequences are specified as [non-octal decimal escape sequences](https://tc39.es/ecma262/#prod-annexB-NonOctalDecimalEscapeSequence), retaining the same behavior.

Nevertheless, the ECMAScript specification treats `\8` and `\9` in string literals as a legacy feature. This syntax is optional if the ECMAScript host is not a web browser. Browsers still have to support it, but only in non-strict mode.

Regardless of your targeted environment, these escape sequences shouldn’t be used when writing new code.

## Rule Details

This rule disallows `\8` and `\9` escape sequences in string literals.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tbm9ub2N0YWwtZGVjaW1hbC1lc2NhcGU6IFwiZXJyb3JcIiovXG5cblwiXFw4XCI7XG5cblwiXFw5XCI7XG5cbmNvbnN0IGZvbyA9IFwid1xcOGxlc3NcIjtcblxuY29uc3QgYmFyID0gXCJEZWNlbWJlciAxXFw5XCI7XG5cbmNvbnN0IGJheiA9IFwiRG9uJ3QgdXNlIFxcOCBhbmQgXFw5IGVzY2FwZXMuXCI7XG5cbmNvbnN0IHF1dXggPSBcIlxcMFxcOFwiOyJ9)

```
/*eslint no-nonoctal-decimal-escape: "error"*/

"\8";

"\9";

const foo = "w\8less";

const bar = "December 1\9";

const baz = "Don't use \8 and \9 escapes.";

const quux = "\0\8";
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tbm9ub2N0YWwtZGVjaW1hbC1lc2NhcGU6IFwiZXJyb3JcIiovXG5cblwiOFwiO1xuXG5cIjlcIjtcblxuY29uc3QgZm9vID0gXCJ3OGxlc3NcIjtcblxuY29uc3QgYmFyID0gXCJEZWNlbWJlciAxOVwiO1xuXG5jb25zdCBiYXogPSBcIkRvbid0IHVzZSBcXFxcOCBhbmQgXFxcXDkgZXNjYXBlcy5cIjtcblxuY29uc3QgcXV1eCA9IFwiXFwwXFx1MDAzOFwiOyJ9)

```
/*eslint no-nonoctal-decimal-escape: "error"*/

"8";

"9";

const foo = "w8less";

const bar = "December 19";

const baz = "Don't use \\8 and \\9 escapes.";

const quux = "\0\u0038";
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

## Related Rules

- [no-octal-escape](/docs/latest/rules/no-octal-escape)

## Version

This rule was introduced in ESLint v7.14.0.

## Further Reading

[ECMAScript® 2023 Language Specification](https://tc39.es/ecma262/#prod-annexB-NonOctalDecimalEscapeSequence)
 tc39.es

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-nonoctal-decimal-escape.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-nonoctal-decimal-escape.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-nonoctal-decimal-escape.md
                    
                
                )
