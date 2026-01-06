# no-octal

Disallow octal literals

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Compatibility](#compatibility)
3. [Version](#version)
4. [Resources](#resources)

Octal literals are numerals that begin with a leading zero, such as:

```
const num = 071;      // 57
1
```

Copy code to clipboard

Because the leading zero which identifies an octal literal has been a source of confusion and error in JavaScript code, ECMAScript 5 deprecates the use of octal numeric literals.

## Rule Details

The rule disallows octal literals.

If ESLint parses code in strict mode, the parser (instead of this rule) reports the error.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tb2N0YWw6IFwiZXJyb3JcIiovXG5cbmNvbnN0IG51bSA9IDA3MTtcbmNvbnN0IHJlc3VsdCA9IDUgKyAwNzsifQ==)

```
/*eslint no-octal: "error"*/

const num = 071;
const result = 5 + 07;
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tb2N0YWw6IFwiZXJyb3JcIiovXG5cbmNvbnN0IG51bSAgPSBcIjA3MVwiOyJ9)

```
/*eslint no-octal: "error"*/

const num  = "071";
1
2
3
```

## Compatibility

- JSHint: W115

## Version

This rule was introduced in ESLint v0.0.6.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-octal.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-octal.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-octal.md
                    
                
                )
