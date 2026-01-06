# no-compare-neg-zero

Disallow comparing against `-0`

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

## Rule Details

The rule should warn against code that tries to compare against `-0`, since that will not work as intended. That is, code like `x === -0` will pass for both `+0` and `-0`. The author probably intended `Object.is(x, -0)`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWNvbXBhcmUtbmVnLXplcm86IFwiZXJyb3JcIiAqL1xuXG5pZiAoeCA9PT0gLTApIHtcbiAgICAvLyBkb1NvbWV0aGluZygpLi4uXG59In0=)

```
/* eslint no-compare-neg-zero: "error" */

if (x === -0) {
    // doSomething()...
}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWNvbXBhcmUtbmVnLXplcm86IFwiZXJyb3JcIiAqL1xuXG5pZiAoeCA9PT0gMCkge1xuICAgIC8vIGRvU29tZXRoaW5nKCkuLi5cbn0ifQ==)

```
/* eslint no-compare-neg-zero: "error" */

if (x === 0) {
    // doSomething()...
}
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWNvbXBhcmUtbmVnLXplcm86IFwiZXJyb3JcIiAqL1xuXG5pZiAoT2JqZWN0LmlzKHgsIC0wKSkge1xuICAgIC8vIGRvU29tZXRoaW5nKCkuLi5cbn0ifQ==)

```
/* eslint no-compare-neg-zero: "error" */

if (Object.is(x, -0)) {
    // doSomething()...
}
1
2
3
4
5
```

## Version

This rule was introduced in ESLint v3.17.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-compare-neg-zero.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-compare-neg-zero.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-compare-neg-zero.md
                    
                
                )
