# no-unexpected-multiline

Disallow confusing multiline expressions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Semicolons are usually optional in JavaScript, because of automatic semicolon insertion (ASI). You can require or disallow semicolons with the [semi](./semi) rule.

The rules for ASI are relatively straightforward: As once described by Isaac Schlueter, a newline character always ends a statement, just like a semicolon, except where one of the following is true:

- The statement has an unclosed paren, array literal, or object literal or ends in some other way that is not a valid way to end a statement. (For instance, ending with `.` or `,`.)
- The line is `--` or `++` (in which case it will decrement/increment the next token.)
- It is a `for()`, `while()`, `do`, `if()`, or `else`, and there is no `{`
- The next line starts with `[`, `(`, `+`, `*`, `/`, `-`, `,`, `.`, or some other binary operator that can only be found between two tokens in a single expression.

In the exceptions where a newline does not end a statement, a typing mistake to omit a semicolon causes two unrelated consecutive lines to be interpreted as one expression. Especially for a coding style without semicolons, readers might overlook the mistake. Although syntactically correct, the code might throw exceptions when it is executed.

## Rule Details

This rule disallows confusing multiline expressions where a newline looks like it is ending a statement, but is not.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5leHBlY3RlZC1tdWx0aWxpbmU6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IGJhclxuKDEgfHwgMikuYmF6KCk7XG5cbmNvbnN0IGhlbGxvID0gJ3dvcmxkJ1xuWzEsIDIsIDNdLmZvckVhY2goYWRkTnVtYmVyKTtcblxuY29uc3QgeCA9IGZ1bmN0aW9uKCkge31cbmBoZWxsb2BcblxuY29uc3QgeSA9IGZ1bmN0aW9uKCkge31cbnlcbmBoZWxsb2BcblxuY29uc3QgeiA9IGZvb1xuL3JlZ2V4L2cudGVzdChiYXIpIn0=)

```
/*eslint no-unexpected-multiline: "error"*/

const foo = bar
(1 || 2).baz();

const hello = 'world'
[1, 2, 3].forEach(addNumber);

const x = function() {}
`hello`

const y = function() {}
y
`hello`

const z = foo
/regex/g.test(bar)
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
14
15
16
17
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5leHBlY3RlZC1tdWx0aWxpbmU6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IGJhcjtcbigxIHx8IDIpLmJheigpO1xuXG5jb25zdCBiYXogPSBiYXJcbjsoMSB8fCAyKS5iYXooKVxuXG5jb25zdCBoZWxsbyA9ICd3b3JsZCc7XG5bMSwgMiwgM10uZm9yRWFjaChhZGROdW1iZXIpO1xuXG5jb25zdCBoaSA9ICd3b3JsZCdcbnZvaWQgWzEsIDIsIDNdLmZvckVhY2goYWRkTnVtYmVyKTtcblxuY29uc3QgeCA9IGZ1bmN0aW9uKCkge307XG5gaGVsbG9gXG5cbmNvbnN0IHRhZyA9IGZ1bmN0aW9uKCkge31cbnRhZyBgaGVsbG9gIn0=)

```
/*eslint no-unexpected-multiline: "error"*/

const foo = bar;
(1 || 2).baz();

const baz = bar
;(1 || 2).baz()

const hello = 'world';
[1, 2, 3].forEach(addNumber);

const hi = 'world'
void [1, 2, 3].forEach(addNumber);

const x = function() {};
`hello`

const tag = function() {}
tag `hello`
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
14
15
16
17
18
19
```

## When Not To Use It

You can turn this rule off if you are confident that you will not accidentally introduce code like this.

Note that the patterns considered problems are not flagged by the [semi](semi) rule.

## Related Rules

- [func-call-spacing](/docs/latest/rules/func-call-spacing)
- [semi](/docs/latest/rules/semi)
- [space-unary-ops](/docs/latest/rules/space-unary-ops)

## Version

This rule was introduced in ESLint v0.24.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unexpected-multiline.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unexpected-multiline.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unexpected-multiline.md
                    
                
                )
