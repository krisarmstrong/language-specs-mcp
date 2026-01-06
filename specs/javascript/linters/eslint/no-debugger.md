# no-debugger

Disallow the use of `debugger`

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

The `debugger` statement is used to tell the executing JavaScript environment to stop execution and start up a debugger at the current point in the code. This has fallen out of favor as a good practice with the advent of modern debugging and development tools. Production code should definitely not contain `debugger`, as it will cause the browser to stop executing code and open an appropriate debugger.

## Rule Details

This rule disallows `debugger` statements.

Example of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZGVidWdnZXI6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGlzVHJ1dGh5KHgpIHtcbiAgICBkZWJ1Z2dlcjtcbiAgICByZXR1cm4gQm9vbGVhbih4KTtcbn0ifQ==)

```
/*eslint no-debugger: "error"*/

function isTruthy(x) {
    debugger;
    return Boolean(x);
}
1
2
3
4
5
6
```

Example of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZGVidWdnZXI6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGlzVHJ1dGh5KHgpIHtcbiAgICByZXR1cm4gQm9vbGVhbih4KTsgLy8gc2V0IGEgYnJlYWtwb2ludCBhdCB0aGlzIGxpbmVcbn0ifQ==)

```
/*eslint no-debugger: "error"*/

function isTruthy(x) {
    return Boolean(x); // set a breakpoint at this line
}
1
2
3
4
5
```

## When Not To Use It

If your code is still very much in development and don’t want to worry about stripping `debugger` statements, then turn this rule off. You’ll generally want to turn it back on when testing code prior to deployment.

## Related Rules

- [no-alert](/docs/latest/rules/no-alert)
- [no-console](/docs/latest/rules/no-console)

## Version

This rule was introduced in ESLint v0.0.2.

## Further Reading

[debugger - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-debugger.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-debugger.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-debugger.md
                    
                
                )
