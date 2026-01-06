# no-inline-comments

Disallow inline comments after code

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)

  1. [JSX exception](#jsx-exception)

2. [Options](#options)

  1. [ignorePattern](#ignorepattern)

3. [Version](#version)
4. [Resources](#resources)

Some style guides disallow comments on the same line as code. Code can become difficult to read if comments immediately follow the code on the same line. On the other hand, it is sometimes faster and more obvious to put comments immediately following code.

## Rule Details

This rule disallows comments on the same line as code.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW5saW5lLWNvbW1lbnRzOiBcImVycm9yXCIqL1xuXG5jb25zdCBhID0gMTsgLy8gZGVjbGFyaW5nIGEgdG8gMVxuXG5mdW5jdGlvbiBnZXRSYW5kb21OdW1iZXIoKXtcbiAgICByZXR1cm4gNDsgLy8gY2hvc2VuIGJ5IGZhaXIgZGljZSByb2xsLlxuICAgICAgICAgICAgICAvLyBndWFyYW50ZWVkIHRvIGJlIHJhbmRvbS5cbn1cblxuLyogQSBibG9jayBjb21tZW50IGJlZm9yZSBjb2RlICovIGNvbnN0IGIgPSAyO1xuXG5jb25zdCBjID0gMzsgLyogQSBibG9jayBjb21tZW50IGFmdGVyIGNvZGUgKi8ifQ==)

```
/*eslint no-inline-comments: "error"*/

const a = 1; // declaring a to 1

function getRandomNumber(){
    return 4; // chosen by fair dice roll.
              // guaranteed to be random.
}

/* A block comment before code */ const b = 2;

const c = 3; /* A block comment after code */
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW5saW5lLWNvbW1lbnRzOiBcImVycm9yXCIqL1xuXG4vLyBUaGlzIGlzIGEgY29tbWVudCBhYm92ZSBhIGxpbmUgb2YgY29kZVxuY29uc3QgZm9vID0gNTtcblxuY29uc3QgYmFyID0gNTtcbi8vVGhpcyBpcyBhIGNvbW1lbnQgYmVsb3cgYSBsaW5lIG9mIGNvZGUifQ==)

```
/*eslint no-inline-comments: "error"*/

// This is a comment above a line of code
const foo = 5;

const bar = 5;
//This is a comment below a line of code
1
2
3
4
5
6
7
```

### JSX exception

Comments inside the curly braces in JSX are allowed to be on the same line as the braces, but only if they are not on the same line with other code, and the braces do not enclose an actual expression.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXJPcHRpb25zIjp7ImVjbWFGZWF0dXJlcyI6eyJqc3giOnRydWV9fX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5saW5lLWNvbW1lbnRzOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSA8ZGl2PnsgLyogT24gdGhlIHNhbWUgbGluZSB3aXRoIG90aGVyIGNvZGUgKi8gfTxoMT5Tb21lIGhlYWRpbmc8L2gxPjwvZGl2PjtcblxuY29uc3QgYmFyID0gKFxuICAgIDxkaXY+XG4gICAgeyAgIC8vIFRoZXNlIGJyYWNlcyBhcmUgbm90IGp1c3QgZm9yIHRoZSBjb21tZW50LCBzbyBpdCBjYW4ndCBiZSBvbiB0aGUgc2FtZSBsaW5lXG4gICAgICAgIGJhelxuICAgIH1cbiAgICA8L2Rpdj5cbik7In0=)

```
/*eslint no-inline-comments: "error"*/

const foo = <div>{ /* On the same line with other code */ }<h1>Some heading</h1></div>;

const bar = (
    <div>
    {   // These braces are not just for the comment, so it can't be on the same line
        baz
    }
    </div>
);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXJPcHRpb25zIjp7ImVjbWFGZWF0dXJlcyI6eyJqc3giOnRydWV9fX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5saW5lLWNvbW1lbnRzOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSAoXG4gICAgPGRpdj5cbiAgICAgIHsvKiBUaGVzZSBicmFjZXMgYXJlIGp1c3QgZm9yIHRoaXMgY29tbWVudCBhbmQgdGhlcmUgaXMgbm90aGluZyBlbHNlIG9uIHRoaXMgbGluZSAqL31cbiAgICAgIDxoMT5Tb21lIGhlYWRpbmc8L2gxPlxuICAgIDwvZGl2PlxuKVxuXG5jb25zdCBiYXIgPSAoXG4gICAgPGRpdj5cbiAgICB7XG4gICAgICAgIC8vIFRoZXJlIGlzIG5vdGhpbmcgZWxzZSBvbiB0aGlzIGxpbmVcbiAgICAgICAgYmF6XG4gICAgfVxuICAgIDwvZGl2PlxuKTtcblxuY29uc3QgcXV1eCA9IChcbiAgICA8ZGl2PlxuICAgICAgey8qXG4gICAgICAgIE11bHRpbGluZVxuICAgICAgICBjb21tZW50XG4gICAgICAqL31cbiAgICAgIDxoMT5Tb21lIGhlYWRpbmc8L2gxPlxuICAgIDwvZGl2PlxuKSJ9)

```
/*eslint no-inline-comments: "error"*/

const foo = (
    <div>
      {/* These braces are just for this comment and there is nothing else on this line */}
      <h1>Some heading</h1>
    </div>
)

const bar = (
    <div>
    {
        // There is nothing else on this line
        baz
    }
    </div>
);

const quux = (
    <div>
      {/*
        Multiline
        comment
      */}
      <h1>Some heading</h1>
    </div>
)
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
20
21
22
23
24
25
26
27
```

## Options

### ignorePattern

To make this rule ignore specific comments, set the `ignorePattern` option to a string pattern that will be passed to the [RegExp constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp).

Examples of correct code for the `ignorePattern` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW5saW5lLWNvbW1lbnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlUGF0dGVyblwiOiBcIndlYnBhY2tDaHVua05hbWU6XFxcXHMuK1wiIH1dKi9cblxuaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwibXktY2h1bmstbmFtZVwiICovICcuL2xvY2FsZS9lbicpOyJ9)

```
/*eslint no-inline-comments: ["error", { "ignorePattern": "webpackChunkName:\\s.+" }]*/

import(/* webpackChunkName: "my-chunk-name" */ './locale/en');
1
2
3
```

Examples of incorrect code for the `ignorePattern` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW5saW5lLWNvbW1lbnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlUGF0dGVyblwiOiBcInNvbWV0aGluZ1wiIH1dICovXG5cbmNvbnN0IGZvbyA9IDQ7IC8vIG90aGVyIHRoaW5nIn0=)

```
/*eslint no-inline-comments: ["error", { "ignorePattern": "something" }] */

const foo = 4; // other thing
1
2
3
```

## Version

This rule was introduced in ESLint v0.10.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-inline-comments.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-inline-comments.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-inline-comments.md
                    
                
                )
