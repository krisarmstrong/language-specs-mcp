# no-lonely-if

Disallow `if` statements as the only statement in `else` blocks

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

If an `if` statement is the only statement in the `else` block, it is often clearer to use an `else if` form.

```
if (foo) {
    // ...
} else {
    if (bar) {
        // ...
    }
}
1
2
3
4
5
6
7
```

Copy code to clipboard

should be rewritten as

```
if (foo) {
    // ...
} else if (bar) {
    // ...
}
1
2
3
4
5
```

Copy code to clipboard

## Rule Details

This rule disallows `if` statements as the only statement in `else` blocks.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9uZWx5LWlmOiBcImVycm9yXCIqL1xuXG5pZiAoY29uZGl0aW9uKSB7XG4gICAgLy8gLi4uXG59IGVsc2Uge1xuICAgIGlmIChhbm90aGVyQ29uZGl0aW9uKSB7XG4gICAgICAgIC8vIC4uLlxuICAgIH1cbn1cblxuaWYgKGNvbmRpdGlvbikge1xuICAgIC8vIC4uLlxufSBlbHNlIHtcbiAgICBpZiAoYW5vdGhlckNvbmRpdGlvbikge1xuICAgICAgICAvLyAuLi5cbiAgICB9IGVsc2Uge1xuICAgICAgICAvLyAuLi5cbiAgICB9XG59In0=)

```
/*eslint no-lonely-if: "error"*/

if (condition) {
    // ...
} else {
    if (anotherCondition) {
        // ...
    }
}

if (condition) {
    // ...
} else {
    if (anotherCondition) {
        // ...
    } else {
        // ...
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9uZWx5LWlmOiBcImVycm9yXCIqL1xuXG5pZiAoY29uZGl0aW9uKSB7XG4gICAgLy8gLi4uXG59IGVsc2UgaWYgKGFub3RoZXJDb25kaXRpb24pIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKGNvbmRpdGlvbikge1xuICAgIC8vIC4uLlxufSBlbHNlIGlmIChhbm90aGVyQ29uZGl0aW9uKSB7XG4gICAgLy8gLi4uXG59IGVsc2Uge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoY29uZGl0aW9uKSB7XG4gICAgLy8gLi4uXG59IGVsc2Uge1xuICAgIGlmIChhbm90aGVyQ29uZGl0aW9uKSB7XG4gICAgICAgIC8vIC4uLlxuICAgIH1cbiAgICBkb1NvbWV0aGluZygpO1xufSJ9)

```
/*eslint no-lonely-if: "error"*/

if (condition) {
    // ...
} else if (anotherCondition) {
    // ...
}

if (condition) {
    // ...
} else if (anotherCondition) {
    // ...
} else {
    // ...
}

if (condition) {
    // ...
} else {
    if (anotherCondition) {
        // ...
    }
    doSomething();
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
```

## When Not To Use It

Disable this rule if the code is clearer without requiring the `else if` form.

## Version

This rule was introduced in ESLint v0.6.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-lonely-if.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-lonely-if.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-lonely-if.md
                    
                
                )
