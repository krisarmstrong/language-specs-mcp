# no-div-regex

Disallow equal signs explicitly at the beginning of regular expressions

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Resources](#resources)

Characters `/=` at the beginning of a regular expression literal can be confused with a division assignment operator.

```
function bar() { return /=foo/; }
1
```

Copy code to clipboard

## Rule Details

This rule forbids equal signs (`=`) after the slash (`/`) at the beginning of a regular expression literal, because the characters `/=` can be confused with a division assignment operator.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZGl2LXJlZ2V4OiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBiYXIoKSB7IHJldHVybiAvPWZvby87IH0ifQ==)

```
/*eslint no-div-regex: "error"*/

function bar() { return /=foo/; }
1
2
3
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZGl2LXJlZ2V4OiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBiYXIoKSB7IHJldHVybiAvWz1dZm9vLzsgfSJ9)

```
/*eslint no-div-regex: "error"*/

function bar() { return /[=]foo/; }
1
2
3
```

## Related Rules

- [no-control-regex](/docs/latest/rules/no-control-regex)
- [no-regex-spaces](/docs/latest/rules/no-regex-spaces)

## Version

This rule was introduced in ESLint v0.1.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-div-regex.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-div-regex.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-div-regex.md
                    
                
                )
