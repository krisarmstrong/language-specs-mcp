# max-lines-per-function

Enforce a maximum number of lines of code in a function

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Why not use max-statements or other complexity measurement rules instead?](#why-not-use-max-statements-or-other-complexity-measurement-rules-instead)

2. [Options](#options)

  1. [code](#code)
  2. [skipBlankLines](#skipblanklines)
  3. [skipComments](#skipcomments)
  4. [IIFEs](#iifes)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Some people consider large functions a code smell. Large functions tend to do a lot of things and can make it hard following what’s going on. Many coding style guides dictate a limit of the number of lines that a function can comprise of. This rule can help enforce that style.

## Rule Details

This rule enforces a maximum number of lines per function, in order to aid in maintainability and reduce complexity.

### Why not use `max-statements` or other complexity measurement rules instead?

Nested long method chains like the below example are often broken onto separate lines for readability:

```
function() {
    return m("div", [
        m("table", {className: "table table-striped latest-data"}, [
            m("tbody",
                data.map(function(db) {
                    return m("tr", {key: db.dbname}, [
                        m("td", {className: "dbname"}, db.dbname),
                        m("td", {className: "query-count"},  [
                            m("span", {className: db.lastSample.countClassName}, db.lastSample.nbQueries)
                        ])
                    ])
                })
            )
        ])
    ])
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
```

Copy code to clipboard

- `max-statements` will only report this as 1 statement, despite being 16 lines of code.
- `complexity` will only report a complexity of 1
- `max-nested-callbacks` will only report 1
- `max-depth` will report a depth of 0

## Options

This rule has the following options that can be specified using an object:

- 

`"max"` (default `50`) enforces a maximum number of lines in a function.

- 

`"skipBlankLines"` (default `false`) ignore lines made up purely of whitespace.

- 

`"skipComments"` (default `false`) ignore lines containing just comments.

- 

`"IIFEs"` (default `false`) include any code included in IIFEs.

Alternatively, you may specify a single integer for the `max` option:

```
"max-lines-per-function": ["error", 20]
1
```

Copy code to clipboard

is equivalent to

```
"max-lines-per-function": ["error", { "max": 20 }]
1
```

Copy code to clipboard

### code

Examples of incorrect code for this rule with a particular max value:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwgMl0qL1xuZnVuY3Rpb24gZm9vKCkge1xuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", 2]*/
function foo() {
    const x = 0;
}
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwgM10qL1xuZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIGEgY29tbWVudFxuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", 3]*/
function foo() {
    // a comment
    const x = 0;
}
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwgNF0qL1xuZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIGEgY29tbWVudCBmb2xsb3dlZCBieSBhIGJsYW5rIGxpbmVcblxuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", 4]*/
function foo() {
    // a comment followed by a blank line

    const x = 0;
}
1
2
3
4
5
6
```

Examples of correct code for this rule with a particular max value:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwgM10qL1xuZnVuY3Rpb24gZm9vKCkge1xuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", 3]*/
function foo() {
    const x = 0;
}
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwgNF0qL1xuZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIGEgY29tbWVudFxuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", 4]*/
function foo() {
    // a comment
    const x = 0;
}
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwgNV0qL1xuZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIGEgY29tbWVudCBmb2xsb3dlZCBieSBhIGJsYW5rIGxpbmVcblxuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", 5]*/
function foo() {
    // a comment followed by a blank line

    const x = 0;
}
1
2
3
4
5
6
```

### skipBlankLines

Examples of incorrect code for this rule with the `{ "skipBlankLines": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwge1wibWF4XCI6IDIsIFwic2tpcEJsYW5rTGluZXNcIjogdHJ1ZX1dKi9cbmZ1bmN0aW9uIGZvbygpIHtcblxuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", {"max": 2, "skipBlankLines": true}]*/
function foo() {

    const x = 0;
}
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "skipBlankLines": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwge1wibWF4XCI6IDMsIFwic2tpcEJsYW5rTGluZXNcIjogdHJ1ZX1dKi9cbmZ1bmN0aW9uIGZvbygpIHtcblxuICAgIGNvbnN0IHggPSAwO1xufSJ9)

```
/*eslint max-lines-per-function: ["error", {"max": 3, "skipBlankLines": true}]*/
function foo() {

    const x = 0;
}
1
2
3
4
5
```

### skipComments

Examples of incorrect code for this rule with the `{ "skipComments": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwge1wibWF4XCI6IDIsIFwic2tpcENvbW1lbnRzXCI6IHRydWV9XSovXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgLy8gYSBjb21tZW50XG4gICAgY29uc3QgeCA9IDA7XG59In0=)

```
/*eslint max-lines-per-function: ["error", {"max": 2, "skipComments": true}]*/
function foo() {
    // a comment
    const x = 0;
}
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "skipComments": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwge1wibWF4XCI6IDMsIFwic2tpcENvbW1lbnRzXCI6IHRydWV9XSovXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgLy8gYSBjb21tZW50XG4gICAgY29uc3QgeCA9IDA7XG59In0=)

```
/*eslint max-lines-per-function: ["error", {"max": 3, "skipComments": true}]*/
function foo() {
    // a comment
    const x = 0;
}
1
2
3
4
5
```

### IIFEs

Examples of incorrect code for this rule with the `{ "IIFEs": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwge1wibWF4XCI6IDIsIFwiSUlGRXNcIjogdHJ1ZX1dKi9cbihmdW5jdGlvbigpe1xuICAgIGNvbnN0IHggPSAwO1xufSgpKTtcblxuKCgpID0+IHtcbiAgICBjb25zdCB4ID0gMDtcbn0pKCk7In0=)

```
/*eslint max-lines-per-function: ["error", {"max": 2, "IIFEs": true}]*/
(function(){
    const x = 0;
}());

(() => {
    const x = 0;
})();
1
2
3
4
5
6
7
8
```

Examples of correct code for this rule with the `{ "IIFEs": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzLXBlci1mdW5jdGlvbjogW1wiZXJyb3JcIiwge1wibWF4XCI6IDMsIFwiSUlGRXNcIjogdHJ1ZX1dKi9cbihmdW5jdGlvbigpe1xuICAgIGNvbnN0IHggPSAwO1xufSgpKTtcblxuKCgpID0+IHtcbiAgICBjb25zdCB4ID0gMDtcbn0pKCk7In0=)

```
/*eslint max-lines-per-function: ["error", {"max": 3, "IIFEs": true}]*/
(function(){
    const x = 0;
}());

(() => {
    const x = 0;
})();
1
2
3
4
5
6
7
8
```

## When Not To Use It

You can turn this rule off if you are not concerned with the number of lines in your functions.

## Related Rules

- [complexity](/docs/latest/rules/complexity)
- [max-depth](/docs/latest/rules/max-depth)
- [max-lines](/docs/latest/rules/max-lines)
- [max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)
- [max-params](/docs/latest/rules/max-params)
- [max-statements](/docs/latest/rules/max-statements)
- [max-statements-per-line](/docs/latest/rules/max-statements-per-line)

## Version

This rule was introduced in ESLint v5.0.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-lines-per-function.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-lines-per-function.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-lines-per-function.md
                    
                
                )
