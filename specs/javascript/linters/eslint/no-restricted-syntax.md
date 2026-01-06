# no-restricted-syntax

Disallow specified syntax

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

JavaScript has a lot of language features, and not everyone likes all of them. As a result, some projects choose to disallow the use of certain language features altogether. For instance, you might decide to disallow the use of `try-catch` or `class`, or you might decide to disallow the use of the `in` operator.

Rather than creating separate rules for every language feature you want to turn off, this rule allows you to configure the syntax elements you want to restrict use of. For the JavaScript language, these elements are represented by their [ESTree](https://github.com/estree/estree) node types. For example, a function declaration is represented by `FunctionDeclaration` and the `with` statement is represented by `WithStatement`. You may use [Code Explorer](https://explorer.eslint.org) to determine the nodes that represent your code.

You can also specify [AST selectors](../extend/selectors) to restrict, allowing much more precise control over syntax patterns.

Note: This rule can be used with any language you lint using ESLint. To see what type of nodes your code in another language consists of, you can use:

- [typescript-eslint Playground](https://typescript-eslint.io/play) if you’re using ESLint with `typescript-eslint`.
- [ESLint Code Explorer](https://explorer.eslint.org/) if you’re using ESLint to lint JavaScript, JSON, Markdown, or CSS.

## Rule Details

This rule disallows specified (that is, user-defined) syntax.

## Options

This rule takes a list of strings, where each string is an AST selector:

```
{
    "rules": {
        "no-restricted-syntax": ["error", "FunctionExpression", "WithStatement", "BinaryExpression[operator='in']"]
    }
}
1
2
3
4
5
```

Copy code to clipboard

Alternatively, the rule also accepts objects, where the selector and an optional custom message are specified:

```
{
    "rules": {
        "no-restricted-syntax": [
            "error",
            {
                "selector": "FunctionExpression",
                "message": "Function expressions are not allowed."
            },
            {
                "selector": "CallExpression[callee.name='setTimeout'][arguments.length!=2]",
                "message": "setTimeout must always be invoked with two arguments."
            }
        ]
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
```

Copy code to clipboard

If a custom message is specified with the `message` property, ESLint will use that message when reporting occurrences of the syntax specified in the `selector` property.

The string and object formats can be freely mixed in the configuration as needed.

Examples of incorrect code for this rule with the `"FunctionExpression", "WithStatement", BinaryExpression[operator='in']` options:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtc3ludGF4OiBbXCJlcnJvclwiLCBcIkZ1bmN0aW9uRXhwcmVzc2lvblwiLCBcIldpdGhTdGF0ZW1lbnRcIiwgXCJCaW5hcnlFeHByZXNzaW9uW29wZXJhdG9yPSdpbiddXCJdICovXG5cbndpdGggKG1lKSB7XG4gICAgZG9udE1lc3MoKTtcbn1cblxuY29uc3QgZG9Tb21ldGhpbmcgPSBmdW5jdGlvbiAoKSB7fTtcblxuZm9vIGluIGJhcjsifQ==)

```
/* eslint no-restricted-syntax: ["error", "FunctionExpression", "WithStatement", "BinaryExpression[operator='in']"] */

with (me) {
    dontMess();
}

const doSomething = function () {};

foo in bar;
1
2
3
4
5
6
7
8
9
```

Examples of correct code for this rule with the `"FunctionExpression", "WithStatement", BinaryExpression[operator='in']` options:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtc3ludGF4OiBbXCJlcnJvclwiLCBcIkZ1bmN0aW9uRXhwcmVzc2lvblwiLCBcIldpdGhTdGF0ZW1lbnRcIiwgXCJCaW5hcnlFeHByZXNzaW9uW29wZXJhdG9yPSdpbiddXCJdICovXG5cbm1lLmRvbnRNZXNzKCk7XG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nKCkge307XG5cbmZvbyBpbnN0YW5jZW9mIGJhcjsifQ==)

```
/* eslint no-restricted-syntax: ["error", "FunctionExpression", "WithStatement", "BinaryExpression[operator='in']"] */

me.dontMess();

function doSomething() {};

foo instanceof bar;
1
2
3
4
5
6
7
```

## When Not To Use It

If you don’t want to restrict your code from using any JavaScript features or syntax, you should not use this rule.

## Related Rules

- [no-alert](/docs/latest/rules/no-alert)
- [no-console](/docs/latest/rules/no-console)
- [no-debugger](/docs/latest/rules/no-debugger)
- [no-restricted-properties](/docs/latest/rules/no-restricted-properties)

## Version

This rule was introduced in ESLint v1.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-restricted-syntax.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-restricted-syntax.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-restricted-syntax.md
                    
                
                )
