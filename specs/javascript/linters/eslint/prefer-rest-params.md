# prefer-rest-params

Require rest parameters instead of `arguments`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

There are rest parameters in ES2015. We can use that feature for variadic functions instead of the `arguments` variable.

`arguments` does not have methods of `Array.prototype`, so it’s a bit of an inconvenience.

## Rule Details

This rule is aimed to flag usage of `arguments` variables.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXJlc3QtcGFyYW1zOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgY29uc29sZS5sb2coYXJndW1lbnRzKTtcbn1cblxuZnVuY3Rpb24gZm9vKGFjdGlvbikge1xuICAgIGNvbnN0IGFyZ3MgPSBBcnJheS5wcm90b3R5cGUuc2xpY2UuY2FsbChhcmd1bWVudHMsIDEpO1xuICAgIGFjdGlvbi5hcHBseShudWxsLCBhcmdzKTtcbn1cblxuZnVuY3Rpb24gZm9vKGFjdGlvbikge1xuICAgIGNvbnN0IGFyZ3MgPSBbXS5zbGljZS5jYWxsKGFyZ3VtZW50cywgMSk7XG4gICAgYWN0aW9uLmFwcGx5KG51bGwsIGFyZ3MpO1xufSJ9)

```
/*eslint prefer-rest-params: "error"*/

function foo() {
    console.log(arguments);
}

function foo(action) {
    const args = Array.prototype.slice.call(arguments, 1);
    action.apply(null, args);
}

function foo(action) {
    const args = [].slice.call(arguments, 1);
    action.apply(null, args);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXJlc3QtcGFyYW1zOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBmb28oLi4uYXJncykge1xuICAgIGNvbnNvbGUubG9nKGFyZ3MpO1xufVxuXG5mdW5jdGlvbiBmb28oYWN0aW9uLCAuLi5hcmdzKSB7XG4gICAgYWN0aW9uLmFwcGx5KG51bGwsIGFyZ3MpOyAvLyBvciBgYWN0aW9uKC4uLmFyZ3MpYCwgcmVsYXRlZCB0byB0aGUgYHByZWZlci1zcHJlYWRgIHJ1bGUuXG59XG5cbi8vIE5vdGU6IHRoZSBpbXBsaWNpdCBhcmd1bWVudHMgY2FuIGJlIG92ZXJ3cml0dGVuLlxuZnVuY3Rpb24gZm9vKGFyZ3VtZW50cykge1xuICAgIGNvbnNvbGUubG9nKGFyZ3VtZW50cyk7IC8vIFRoaXMgaXMgdGhlIGZpcnN0IGFyZ3VtZW50LlxufVxuZnVuY3Rpb24gZm9vKCkge1xuICAgIGNvbnN0IGFyZ3VtZW50cyA9IDA7XG4gICAgY29uc29sZS5sb2coYXJndW1lbnRzKTsgLy8gVGhpcyBpcyBhIGxvY2FsIHZhcmlhYmxlLlxufSJ9)

```
/*eslint prefer-rest-params: "error"*/

function foo(...args) {
    console.log(args);
}

function foo(action, ...args) {
    action.apply(null, args); // or `action(...args)`, related to the `prefer-spread` rule.
}

// Note: the implicit arguments can be overwritten.
function foo(arguments) {
    console.log(arguments); // This is the first argument.
}
function foo() {
    const arguments = 0;
    console.log(arguments); // This is a local variable.
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
```

## When Not To Use It

This rule should not be used in ES3/5 environments.

In ES2015 (ES6) or later, if you don’t want to be notified about `arguments` variables, then it’s safe to disable this rule.

## Related Rules

- [prefer-spread](/docs/latest/rules/prefer-spread)

## Version

This rule was introduced in ESLint v2.0.0-alpha-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-rest-params.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-rest-params.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-rest-params.md
                    
                
                )
