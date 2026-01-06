# logical-assignment-operators

Require or disallow logical assignment operator shorthand

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Options](#options)

    1. [always](#always)
    2. [never](#never)
    3. [enforceForIfStatements](#enforceforifstatements)

2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

ES2021 introduces the assignment operator shorthand for the logical operators `||`, `&&` and `??`. Before, this was only allowed for mathematical operations such as `+` or `*` (see the rule [operator-assignment](./operator-assignment)). The shorthand can be used if the assignment target and the left expression of a logical expression are the same. For example `a = a || b` can be shortened to `a ||= b`.

## Rule Details

This rule requires or disallows logical assignment operator shorthand.

### Options

This rule has a string and an object option. String option:

- `"always"` (default)
- `"never"`

Object option (only available if string option is set to `"always"`):

- `"enforceForIfStatements": false` (default) Do not check for equivalent `if` statements.
- `"enforceForIfStatements": true` Check for equivalent `if` statements.

#### always

This option checks for expressions that can be shortened using logical assignment operator. For example, `a = a || b` can be shortened to `a ||= b`. Expressions with associativity such as `a = a || b || c` are reported as being able to be shortened to `a ||= b || c` unless the evaluation order is explicitly defined using parentheses, such as `a = (a || b) || c`.

Examples of incorrect code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbG9naWNhbC1hc3NpZ25tZW50LW9wZXJhdG9yczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5hID0gYSB8fCBiXG5hID0gYSAmJiBiXG5hID0gYSA/PyBiXG5hIHx8IChhID0gYilcbmEgJiYgKGEgPSBiKVxuYSA/PyAoYSA9IGIpXG5hID0gYSB8fCBiIHx8IGNcbmEgPSBhICYmIGIgJiYgY1xuYSA9IGEgPz8gYiA/PyBjIn0=)

```
/*eslint logical-assignment-operators: ["error", "always"]*/

a = a || b
a = a && b
a = a ?? b
a || (a = b)
a && (a = b)
a ?? (a = b)
a = a || b || c
a = a && b && c
a = a ?? b ?? c
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

Examples of correct code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbG9naWNhbC1hc3NpZ25tZW50LW9wZXJhdG9yczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5hID0gYlxuYSArPSBiXG5hIHx8PSBiXG5hID0gYiB8fCBjXG5hIHx8IChiID0gYylcblxuaWYgKGEpIGEgPSBiXG5cbmEgPSAoYSB8fCBiKSB8fCBjIn0=)

```
/*eslint logical-assignment-operators: ["error", "always"]*/

a = b
a += b
a ||= b
a = b || c
a || (b = c)

if (a) a = b

a = (a || b) || c
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

#### never

Examples of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbG9naWNhbC1hc3NpZ25tZW50LW9wZXJhdG9yczogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbmEgfHw9IGJcbmEgJiY9IGJcbmEgPz89IGIifQ==)

```
/*eslint logical-assignment-operators: ["error", "never"]*/

a ||= b
a &&= b
a ??= b
1
2
3
4
5
```

Examples of correct code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbG9naWNhbC1hc3NpZ25tZW50LW9wZXJhdG9yczogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbmEgPSBhIHx8IGJcbmEgPSBhICYmIGJcbmEgPSBhID8/IGIifQ==)

```
/*eslint logical-assignment-operators: ["error", "never"]*/

a = a || b
a = a && b
a = a ?? b
1
2
3
4
5
```

#### enforceForIfStatements

This option checks for additional patterns with if statements which could be expressed with the logical assignment operator.

Examples of incorrect code for this rule with the `["always", { enforceForIfStatements: true }]` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbG9naWNhbC1hc3NpZ25tZW50LW9wZXJhdG9yczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBlbmZvcmNlRm9ySWZTdGF0ZW1lbnRzOiB0cnVlIH1dKi9cblxuaWYgKGEpIGEgPSBiIC8vIDw9PiBhICYmPSBiXG5pZiAoIWEpIGEgPSBiIC8vIDw9PiBhIHx8PSBiXG5cbmlmIChhID09IG51bGwpIGEgPSBiIC8vIDw9PiBhID8/PSBiXG5pZiAoYSA9PT0gbnVsbCB8fCBhID09PSB1bmRlZmluZWQpIGEgPSBiIC8vIDw9PiBhID8/PSBiIn0=)

```
/*eslint logical-assignment-operators: ["error", "always", { enforceForIfStatements: true }]*/

if (a) a = b // <=> a &&= b
if (!a) a = b // <=> a ||= b

if (a == null) a = b // <=> a ??= b
if (a === null || a === undefined) a = b // <=> a ??= b
1
2
3
4
5
6
7
```

Examples of correct code for this rule with the `["always", { enforceForIfStatements: true }]` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbG9naWNhbC1hc3NpZ25tZW50LW9wZXJhdG9yczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBlbmZvcmNlRm9ySWZTdGF0ZW1lbnRzOiB0cnVlIH1dKi9cblxuaWYgKGEpIGIgPSBjXG5pZiAoYSA9PT0gMCkgYSA9IGIifQ==)

```
/*eslint logical-assignment-operators: ["error", "always", { enforceForIfStatements: true }]*/

if (a) b = c
if (a === 0) a = b
1
2
3
4
```

## When Not To Use It

Use of logical operator assignment shorthand is a stylistic choice. Leaving this rule turned off would allow developers to choose which style is more readable on a case-by-case basis.

## Version

This rule was introduced in ESLint v8.24.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/logical-assignment-operators.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/logical-assignment-operators.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/logical-assignment-operators.md
                    
                
                )
