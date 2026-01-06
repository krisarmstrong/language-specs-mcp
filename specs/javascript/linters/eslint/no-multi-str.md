# no-multi-str

Disallow multiline strings

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

It’s possible to create multiline strings in JavaScript by using a slash before a newline, such as:

```
const x = "Line 1 \
         Line 2";
1
2
```

Copy code to clipboard

Some consider this to be a bad practice as it was an undocumented feature of JavaScript that was only formalized later.

## Rule Details

This rule is aimed at preventing the use of multiline strings.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbXVsdGktc3RyOiBcImVycm9yXCIqL1xuXG5jb25zdCB4ID0gXCJzb21lIHZlcnkgXFxcbmxvbmcgdGV4dFwiOyJ9)

```
/*eslint no-multi-str: "error"*/

const x = "some very \
long text";
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbXVsdGktc3RyOiBcImVycm9yXCIqL1xuXG5jb25zdCB4ID0gXCJzb21lIHZlcnkgbG9uZyB0ZXh0XCI7XG5cbmNvbnN0IHkgPSBcInNvbWUgdmVyeSBcIiArXG4gICAgICAgIFwibG9uZyB0ZXh0XCI7In0=)

```
/*eslint no-multi-str: "error"*/

const x = "some very long text";

const y = "some very " +
        "long text";
1
2
3
4
5
6
```

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-multi-str.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-multi-str.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-multi-str.md
                    
                
                )
