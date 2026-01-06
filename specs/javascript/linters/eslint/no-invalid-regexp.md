# no-invalid-regexp

Disallow invalid regular expression strings in `RegExp` constructors

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowConstructorFlags](#allowconstructorflags)

3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

An invalid pattern in a regular expression literal is a `SyntaxError` when the code is parsed, but an invalid string in `RegExp` constructors throws a `SyntaxError` only when the code is executed.

## Rule Details

This rule disallows invalid regular expression strings in `RegExp` constructors.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC1yZWdleHA6IFwiZXJyb3JcIiovXG5cblJlZ0V4cCgnWycpXG5cblJlZ0V4cCgnLicsICd6JylcblxubmV3IFJlZ0V4cCgnXFxcXCcpIn0=)

```
/*eslint no-invalid-regexp: "error"*/

RegExp('[')

RegExp('.', 'z')

new RegExp('\\')
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC1yZWdleHA6IFwiZXJyb3JcIiovXG5cblJlZ0V4cCgnLicpXG5cbm5ldyBSZWdFeHBcblxudGhpcy5SZWdFeHAoJ1snKSJ9)

```
/*eslint no-invalid-regexp: "error"*/

RegExp('.')

new RegExp

this.RegExp('[')
1
2
3
4
5
6
7
```

Please note that this rule validates regular expressions per the latest ECMAScript specification, regardless of your parser settings.

If you want to allow additional constructor flags for any reason, you can specify them using the `allowConstructorFlags` option. These flags will then be ignored by the rule.

## Options

This rule has an object option for exceptions:

- `"allowConstructorFlags"` is a case-sensitive array of flags

### allowConstructorFlags

Examples of correct code for this rule with the `{ "allowConstructorFlags": ["a", "z"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC1yZWdleHA6IFtcImVycm9yXCIsIHsgXCJhbGxvd0NvbnN0cnVjdG9yRmxhZ3NcIjogW1wiYVwiLCBcInpcIl0gfV0qL1xuXG5uZXcgUmVnRXhwKCcuJywgJ2EnKVxuXG5uZXcgUmVnRXhwKCcuJywgJ2F6JykifQ==)

```
/*eslint no-invalid-regexp: ["error", { "allowConstructorFlags": ["a", "z"] }]*/

new RegExp('.', 'a')

new RegExp('.', 'az')
1
2
3
4
5
```

## Version

This rule was introduced in ESLint v0.1.4.

## Further Reading

[Annotated ES5](https://es5.github.io/#x7.8.5)
 es5.github.io

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-invalid-regexp.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-invalid-regexp.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-invalid-regexp.md
                    
                
                )
