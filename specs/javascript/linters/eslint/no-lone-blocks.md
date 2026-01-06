# no-lone-blocks

Disallow unnecessary nested blocks

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

In JavaScript, prior to ES6, standalone code blocks delimited by curly braces do not create a new scope and have no use. For example, these curly braces do nothing to `foo`:

```
{
    var foo = bar();
}
1
2
3
```

Copy code to clipboard

In ES6, code blocks may create a new scope if a block-level binding (`let` and `const`), a class declaration or a function declaration (in strict mode) are present. A block is not considered redundant in these cases.

## Rule Details

This rule aims to eliminate unnecessary and potentially confusing blocks at the top level of a script or within other blocks.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9uZS1ibG9ja3M6IFwiZXJyb3JcIiovXG5cbnt9XG5cbmlmIChmb28pIHtcbiAgICBiYXIoKTtcbiAgICB7XG4gICAgICAgIGJheigpO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gYmFyKCkge1xuICAgIHtcbiAgICAgICAgYmF6KCk7XG4gICAgfVxufVxuXG57XG4gICAgZnVuY3Rpb24gZm9vKCkge31cbn1cblxue1xuICAgIGFMYWJlbDoge1xuICAgIH1cbn1cblxuY2xhc3MgQyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAge1xuICAgICAgICAgICAgZm9vKCk7XG4gICAgICAgIH1cbiAgICB9XG59In0=)

```
/*eslint no-lone-blocks: "error"*/

{}

if (foo) {
    bar();
    {
        baz();
    }
}

function bar() {
    {
        baz();
    }
}

{
    function foo() {}
}

{
    aLabel: {
    }
}

class C {
    static {
        {
            foo();
        }
    }
}
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
28
29
30
31
32
33
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9uZS1ibG9ja3M6IFwiZXJyb3JcIiovXG5cbndoaWxlIChmb28pIHtcbiAgICBiYXIoKTtcbn1cblxuaWYgKGZvbykge1xuICAgIGlmIChiYXIpIHtcbiAgICAgICAgYmF6KCk7XG4gICAgfVxufVxuXG5mdW5jdGlvbiBiYXIoKSB7XG4gICAgYmF6KCk7XG59XG5cbntcbiAgICBsZXQgeCA9IDE7XG59XG5cbntcbiAgICBjb25zdCB5ID0gMTtcbn1cblxue1xuICAgIGNsYXNzIEZvbyB7fVxufVxuXG5hTGFiZWw6IHtcbn1cblxuY2xhc3MgQyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgbGJsOiB7XG4gICAgICAgICAgICBpZiAoc29tZXRoaW5nKSB7XG4gICAgICAgICAgICAgICAgYnJlYWsgbGJsO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICBmb28oKTtcbiAgICAgICAgfVxuICAgIH1cbn0ifQ==)

```
/*eslint no-lone-blocks: "error"*/

while (foo) {
    bar();
}

if (foo) {
    if (bar) {
        baz();
    }
}

function bar() {
    baz();
}

{
    let x = 1;
}

{
    const y = 1;
}

{
    class Foo {}
}

aLabel: {
}

class C {
    static {
        lbl: {
            if (something) {
                break lbl;
            }

            foo();
        }
    }
}
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
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
```

Examples of correct code for this rule with ES6 environment and strict mode via `"parserOptions": { "sourceType": "module" }` in the ESLint configuration or `"use strict"` directive in the code:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9uZS1ibG9ja3M6IFwiZXJyb3JcIiovXG5cblwidXNlIHN0cmljdFwiO1xuXG57XG4gICAgZnVuY3Rpb24gZm9vKCkge31cbn0ifQ==)

```
/*eslint no-lone-blocks: "error"*/

"use strict";

{
    function foo() {}
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

This rule was introduced in ESLint v0.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-lone-blocks.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-lone-blocks.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-lone-blocks.md
                    
                
                )
