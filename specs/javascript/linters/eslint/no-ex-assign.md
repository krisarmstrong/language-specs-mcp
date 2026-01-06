# no-ex-assign

Disallow reassigning exceptions in `catch` clauses

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Further Reading](#further-reading)
4. [Resources](#resources)

If a `catch` clause in a `try` statement accidentally (or purposely) assigns another value to the exception parameter, it is impossible to refer to the error from that point on. Since there is no `arguments` object to offer alternative access to this data, assignment of the parameter is absolutely destructive.

## Rule Details

This rule disallows reassigning exceptions in `catch` clauses.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXgtYXNzaWduOiBcImVycm9yXCIqL1xuXG50cnkge1xuICAgIC8vIGNvZGVcbn0gY2F0Y2ggKGUpIHtcbiAgICBlID0gMTA7XG59In0=)

```
/*eslint no-ex-assign: "error"*/

try {
    // code
} catch (e) {
    e = 10;
}
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXgtYXNzaWduOiBcImVycm9yXCIqL1xuXG50cnkge1xuICAgIC8vIGNvZGVcbn0gY2F0Y2ggKGUpIHtcbiAgICBjb25zdCBmb28gPSAxMDtcbn0ifQ==)

```
/*eslint no-ex-assign: "error"*/

try {
    // code
} catch (e) {
    const foo = 10;
}
1
2
3
4
5
6
7
```

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[The](https://bocoup.com/blog/the-catch-with-try-catch)
 bocoup.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-ex-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-ex-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-ex-assign.md
                    
                
                )
