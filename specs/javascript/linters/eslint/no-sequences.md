# no-sequences

Disallow comma operators

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Note about arrow function bodies](#note-about-arrow-function-bodies)

2. [Options](#options)

  1. [allowInParentheses](#allowinparentheses)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

The comma operator includes multiple expressions where only one is expected. It evaluates each operand from left to right and returns the value of the last operand. However, this frequently obscures side effects, and its use is often an accident. Here are some examples of sequences:

```
let a = (3, 5); // a = 5

a = b += 5, a + b;

while (a = next(), a && a.length);

(0, eval)("doSomething();");
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

This rule forbids the use of the comma operator, with the following exceptions:

- In the initialization or update portions of a `for` statement.
- By default, if the expression sequence is explicitly wrapped in parentheses. This exception can be removed with the `allowInParentheses` option.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VxdWVuY2VzOiBcImVycm9yXCIqL1xuXG5mb28gPSBkb1NvbWV0aGluZygpLCB2YWw7XG5cbjAsIGV2YWwoXCJkb1NvbWV0aGluZygpO1wiKTtcblxuZG8ge30gd2hpbGUgKGRvU29tZXRoaW5nKCksICEhdGVzdCk7XG5cbmZvciAoOyBkb1NvbWV0aGluZygpLCAhIXRlc3Q7ICk7XG5cbmlmIChkb1NvbWV0aGluZygpLCAhIXRlc3QpO1xuXG5zd2l0Y2ggKHZhbCA9IGZvbygpLCB2YWwpIHt9XG5cbndoaWxlICh2YWwgPSBmb28oKSwgdmFsIDwgNDIpO1xuXG53aXRoIChkb1NvbWV0aGluZygpLCB2YWwpIHt9In0=)

```
/*eslint no-sequences: "error"*/

foo = doSomething(), val;

0, eval("doSomething();");

do {} while (doSomething(), !!test);

for (; doSomething(), !!test; );

if (doSomething(), !!test);

switch (val = foo(), val) {}

while (val = foo(), val < 42);

with (doSomething(), val) {}
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

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VxdWVuY2VzOiBcImVycm9yXCIqL1xuXG5mb28gPSAoZG9Tb21ldGhpbmcoKSwgdmFsKTtcblxuKDAsIGV2YWwpKFwiZG9Tb21ldGhpbmcoKTtcIik7XG5cbmRvIHt9IHdoaWxlICgoZG9Tb21ldGhpbmcoKSwgISF0ZXN0KSk7XG5cbmZvciAoaSA9IDAsIGogPSAxMDsgaSA8IGo7IGkrKywgai0tKTtcblxuaWYgKChkb1NvbWV0aGluZygpLCAhIXRlc3QpKTtcblxuc3dpdGNoICgodmFsID0gZm9vKCksIHZhbCkpIHt9XG5cbndoaWxlICgodmFsID0gZm9vKCksIHZhbCA8IDQyKSk7XG5cbndpdGggKChkb1NvbWV0aGluZygpLCB2YWwpKSB7fSJ9)

```
/*eslint no-sequences: "error"*/

foo = (doSomething(), val);

(0, eval)("doSomething();");

do {} while ((doSomething(), !!test));

for (i = 0, j = 10; i < j; i++, j--);

if ((doSomething(), !!test));

switch ((val = foo(), val)) {}

while ((val = foo(), val < 42));

with ((doSomething(), val)) {}
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

### Note about arrow function bodies

If an arrow function body is a statement rather than a block, and that statement contains a sequence, you need to use double parentheses around the statement to indicate that the sequence is intentional.

Examples of incorrect code for arrow functions:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VxdWVuY2VzOiBcImVycm9yXCIqL1xuY29uc3QgZm9vID0gKHZhbCkgPT4gKGNvbnNvbGUubG9nKCdiYXInKSwgdmFsKTtcblxuY29uc3QgYmF6ID0gKCkgPT4gKChiYXIgPSAxMjMpLCAxMCk7XG5cbmNvbnN0IHF1eCA9ICgpID0+IHsgcmV0dXJuIChiYXIgPSAxMjMpLCAxMCB9In0=)

```
/*eslint no-sequences: "error"*/
const foo = (val) => (console.log('bar'), val);

const baz = () => ((bar = 123), 10);

const qux = () => { return (bar = 123), 10 }
1
2
3
4
5
6
```

Examples of correct code for arrow functions:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VxdWVuY2VzOiBcImVycm9yXCIqL1xuY29uc3QgZm9vID0gKHZhbCkgPT4gKChjb25zb2xlLmxvZygnYmFyJyksIHZhbCkpO1xuXG5jb25zdCBiYXogPSAoKSA9PiAoKChiYXIgPSAxMjMpLCAxMCkpO1xuXG5jb25zdCBxdXggPSAoKSA9PiB7IHJldHVybiAoKGJhciA9IDEyMyksIDEwKSB9In0=)

```
/*eslint no-sequences: "error"*/
const foo = (val) => ((console.log('bar'), val));

const baz = () => (((bar = 123), 10));

const qux = () => { return ((bar = 123), 10) }
1
2
3
4
5
6
```

## Options

This rule takes one option, an object, with the following properties:

- `"allowInParentheses"`: If set to `true` (default), this rule allows expression sequences that are explicitly wrapped in parentheses.

### allowInParentheses

Examples of incorrect code for this rule with the `{ "allowInParentheses": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VxdWVuY2VzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dJblBhcmVudGhlc2VzXCI6IGZhbHNlIH1dKi9cblxuZm9vID0gKGRvU29tZXRoaW5nKCksIHZhbCk7XG5cbigwLCBldmFsKShcImRvU29tZXRoaW5nKCk7XCIpO1xuXG5kbyB7fSB3aGlsZSAoKGRvU29tZXRoaW5nKCksICEhdGVzdCkpO1xuXG5mb3IgKDsgKGRvU29tZXRoaW5nKCksICEhdGVzdCk7ICk7XG5cbmlmICgoZG9Tb21ldGhpbmcoKSwgISF0ZXN0KSk7XG5cbnN3aXRjaCAoKHZhbCA9IGZvbygpLCB2YWwpKSB7fVxuXG53aGlsZSAoKHZhbCA9IGZvbygpLCB2YWwgPCA0MikpO1xuXG53aXRoICgoZG9Tb21ldGhpbmcoKSwgdmFsKSkge31cblxuY29uc3QgZm9vID0gKHZhbCkgPT4gKChjb25zb2xlLmxvZygnYmFyJyksIHZhbCkpOyJ9)

```
/*eslint no-sequences: ["error", { "allowInParentheses": false }]*/

foo = (doSomething(), val);

(0, eval)("doSomething();");

do {} while ((doSomething(), !!test));

for (; (doSomething(), !!test); );

if ((doSomething(), !!test));

switch ((val = foo(), val)) {}

while ((val = foo(), val < 42));

with ((doSomething(), val)) {}

const foo = (val) => ((console.log('bar'), val));
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

Examples of correct code for this rule with the `{ "allowInParentheses": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VxdWVuY2VzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dJblBhcmVudGhlc2VzXCI6IGZhbHNlIH1dKi9cblxuZm9yIChpID0gMCwgaiA9IDEwOyBpIDwgajsgaSsrLCBqLS0pOyJ9)

```
/*eslint no-sequences: ["error", { "allowInParentheses": false }]*/

for (i = 0, j = 10; i < j; i++, j--);
1
2
3
```

## When Not To Use It

Disable this rule if sequence expressions with the comma operator are acceptable. Another case is where you might want to report all usages of the comma operator, even in a `for` loop. You can achieve this using rule `no-restricted-syntax`:

```
{
    "rules": {
        "no-restricted-syntax": ["error", "SequenceExpression"]
    }
}
1
2
3
4
5
```

Copy code to clipboard

## Version

This rule was introduced in ESLint v0.5.1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-sequences.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-sequences.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-sequences.md
                    
                
                )
