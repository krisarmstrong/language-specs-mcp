# capitalized-comments

Enforce or disallow capitalization of the first letter of a comment

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Options](#options)

    1. ["always"](#always)
    2. ["never"](#never)
    3. [ignorePattern](#ignorepattern)
    4. [ignoreInlineComments](#ignoreinlinecomments)
    5. [ignoreConsecutiveComments](#ignoreconsecutivecomments)

  2. [Using Different Options for Line and Block Comments](#using-different-options-for-line-and-block-comments)

2. [When Not To Use It](#when-not-to-use-it)
3. [Compatibility](#compatibility)
4. [Version](#version)
5. [Resources](#resources)

Comments are useful for leaving information for future developers. In order for that information to be useful and not distracting, it is sometimes desirable for comments to follow a particular style. One element of comment formatting styles is whether the first word of a comment should be capitalized or lowercase.

In general, no comment style is any more or less valid than any others, but many developers would agree that a consistent style can improve a project’s maintainability.

## Rule Details

This rule aims to enforce a consistent style of comments across your codebase, specifically by either requiring or disallowing a capitalized letter as the first word character in a comment. This rule will not issue warnings when non-cased letters are used.

By default, this rule will require a non-lowercase letter at the beginning of comments.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiXSAqL1xuXG4vLyBsb3dlcmNhc2UgY29tbWVudFxuIn0=)

```
/* eslint capitalized-comments: ["error"] */

// lowercase comment

1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBlcnJvciAqL1xuXG4vLyBDYXBpdGFsaXplZCBjb21tZW50XG5cbi8vIDEuIE5vbi1sZXR0ZXIgYXQgYmVnaW5uaW5nIG9mIGNvbW1lbnRcblxuLy8g5LiIIE5vbi1MYXRpbiBjaGFyYWN0ZXIgYXQgYmVnaW5uaW5nIG9mIGNvbW1lbnRcblxuLyogaXN0YW5idWwgaWdub3JlIG5leHQgKi9cbi8qIGpzY3M6ZW5hYmxlICovXG4vKiBqc2hpbnQgYXNpOnRydWUgKi9cbi8qIGdsb2JhbCBmb28gKi9cbi8qIGdsb2JhbHMgZm9vICovXG4vKiBleHBvcnRlZCBteVZhciAqL1xuLy8gaHR0cHM6Ly9naXRodWIuY29tXG5cbi8qIGVzbGludCBzZW1pOjIgKi9cbi8qIGVzbGludC1kaXNhYmxlICovXG5mb29cbi8qIGVzbGludC1lbmFibGUgKi9cbi8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZVxuYmF6XG5iYXIgLy8gZXNsaW50LWRpc2FibGUtbGluZVxuIn0=)

```
/* eslint capitalized-comments: error */

// Capitalized comment

// 1. Non-letter at beginning of comment

// 丈 Non-Latin character at beginning of comment

/* istanbul ignore next */
/* jscs:enable */
/* jshint asi:true */
/* global foo */
/* globals foo */
/* exported myVar */
// https://github.com

/* eslint semi:2 */
/* eslint-disable */
foo
/* eslint-enable */
// eslint-disable-next-line
baz
bar // eslint-disable-line

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

### Options

This rule has two options: a string value `"always"` or `"never"` which determines whether capitalization of the first word of a comment should be required or forbidden, and optionally an object containing more configuration parameters for the rule.

Here are the supported object options:

- `ignorePattern`: A string representing a regular expression pattern of words that should be ignored by this rule. If the first word of a comment matches the pattern, this rule will not report that comment. 

  - Note that the following words are always ignored by this rule: `["jscs", "jshint", "eslint", "istanbul", "global", "globals", "exported"]`.

- `ignoreInlineComments`: If this is `true`, the rule will not report on comments in the middle of code. By default, this is `false`.
- `ignoreConsecutiveComments`: If this is `true`, the rule will not report on a comment which violates the rule, as long as the comment immediately follows another comment. By default, this is `false`.

Here is an example configuration:

```
{
    "capitalized-comments": [
        "error",
        "always",
        {
            "ignorePattern": "pragma|ignored",
            "ignoreInlineComments": true
        }
    ]
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
```

Copy code to clipboard

#### `"always"`

Using the `"always"` option means that this rule will report any comments which start with a lowercase letter. This is the default configuration for this rule.

Note that configuration comments and comments which start with URLs are never reported.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiXSAqL1xuXG4vLyBsb3dlcmNhc2UgY29tbWVudFxuIn0=)

```
/* eslint capitalized-comments: ["error", "always"] */

// lowercase comment

1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiXSAqL1xuXG4vLyBDYXBpdGFsaXplZCBjb21tZW50XG5cbi8vIDEuIE5vbi1sZXR0ZXIgYXQgYmVnaW5uaW5nIG9mIGNvbW1lbnRcblxuLy8g5LiIIE5vbi1MYXRpbiBjaGFyYWN0ZXIgYXQgYmVnaW5uaW5nIG9mIGNvbW1lbnRcblxuLyogaXN0YW5idWwgaWdub3JlIG5leHQgKi9cbi8qIGpzY3M6ZW5hYmxlICovXG4vKiBqc2hpbnQgYXNpOnRydWUgKi9cbi8qIGdsb2JhbCBmb28gKi9cbi8qIGdsb2JhbHMgZm9vICovXG4vKiBleHBvcnRlZCBteVZhciAqL1xuLy8gaHR0cHM6Ly9naXRodWIuY29tXG5cbi8qIGVzbGludCBzZW1pOjIgKi9cbi8qIGVzbGludC1kaXNhYmxlICovXG5mb29cbi8qIGVzbGludC1lbmFibGUgKi9cbi8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZVxuYmF6XG5iYXIgLy8gZXNsaW50LWRpc2FibGUtbGluZVxuIn0=)

```
/* eslint capitalized-comments: ["error", "always"] */

// Capitalized comment

// 1. Non-letter at beginning of comment

// 丈 Non-Latin character at beginning of comment

/* istanbul ignore next */
/* jscs:enable */
/* jshint asi:true */
/* global foo */
/* globals foo */
/* exported myVar */
// https://github.com

/* eslint semi:2 */
/* eslint-disable */
foo
/* eslint-enable */
// eslint-disable-next-line
baz
bar // eslint-disable-line

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

#### `"never"`

Using the `"never"` option means that this rule will report any comments which start with an uppercase letter.

Examples of incorrect code with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdICovXG5cbi8vIENhcGl0YWxpemVkIGNvbW1lbnRcbiJ9)

```
/* eslint capitalized-comments: ["error", "never"] */

// Capitalized comment

1
2
3
4
```

Examples of correct code with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdICovXG5cbi8vIGxvd2VyY2FzZSBjb21tZW50XG5cbi8vIDEuIE5vbi1sZXR0ZXIgYXQgYmVnaW5uaW5nIG9mIGNvbW1lbnRcblxuLy8g5LiIIE5vbi1MYXRpbiBjaGFyYWN0ZXIgYXQgYmVnaW5uaW5nIG9mIGNvbW1lbnRcbiJ9)

```
/* eslint capitalized-comments: ["error", "never"] */

// lowercase comment

// 1. Non-letter at beginning of comment

// 丈 Non-Latin character at beginning of comment

1
2
3
4
5
6
7
8
```

#### `ignorePattern`

The `ignorePattern` object takes a string value, which is used as a regular expression applied to the first word of a comment.

Examples of correct code with the `"ignorePattern"` option set to `"pragma"`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiaWdub3JlUGF0dGVyblwiOiBcInByYWdtYVwiIH1dICovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICAvKiBwcmFnbWEgd3JhcCh0cnVlKSAqL1xufVxuIn0=)

```
/* eslint capitalized-comments: ["error", "always", { "ignorePattern": "pragma" }] */

function foo() {
    /* pragma wrap(true) */
}

1
2
3
4
5
6
```

#### `ignoreInlineComments`

Setting the `ignoreInlineComments` option to `true` means that comments in the middle of code (with a token on the same line as the beginning of the comment, and another token on the same line as the end of the comment) will not be reported by this rule.

Examples of correct code with the `"ignoreInlineComments"` option set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiaWdub3JlSW5saW5lQ29tbWVudHNcIjogdHJ1ZSB9XSAqL1xuXG5mdW5jdGlvbiBmb28oLyogaWdub3JlZCAqLyBhKSB7XG59XG4ifQ==)

```
/* eslint capitalized-comments: ["error", "always", { "ignoreInlineComments": true }] */

function foo(/* ignored */ a) {
}

1
2
3
4
5
```

#### `ignoreConsecutiveComments`

If the `ignoreConsecutiveComments` option is set to `true`, then comments which otherwise violate the rule will not be reported as long as they immediately follow another comment. This can be applied more than once.

Examples of correct code with `ignoreConsecutiveComments` set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiaWdub3JlQ29uc2VjdXRpdmVDb21tZW50c1wiOiB0cnVlIH1dICovXG5cbmZvbygpO1xuLy8gVGhpcyBjb21tZW50IGlzIHZhbGlkIHNpbmNlIGl0IGhhcyB0aGUgY29ycmVjdCBjYXBpdGFsaXphdGlvbi5cbi8vIHRoaXMgY29tbWVudCBpcyBpZ25vcmVkIHNpbmNlIGl0IGZvbGxvd3MgYW5vdGhlciBjb21tZW50LFxuLy8gYW5kIHRoaXMgb25lIGFzIHdlbGwgYmVjYXVzZSBpdCBmb2xsb3dzIHlldCBhbm90aGVyIGNvbW1lbnQuXG5cbmJhcigpO1xuLyogSGVyZSBpcyBhIGJsb2NrIGNvbW1lbnQgd2hpY2ggaGFzIHRoZSBjb3JyZWN0IGNhcGl0YWxpemF0aW9uLCAqL1xuLyogYnV0IHRoaXMgb25lIGlzIGlnbm9yZWQgZHVlIHRvIGJlaW5nIGNvbnNlY3V0aXZlOyAqL1xuLypcbiAqIGluIGZhY3QsIGV2ZW4gaWYgYW55IG9mIHRoZXNlIGFyZSBtdWx0aS1saW5lLCB0aGF0IGlzIGZpbmUgdG9vLlxuICovIn0=)

```
/* eslint capitalized-comments: ["error", "always", { "ignoreConsecutiveComments": true }] */

foo();
// This comment is valid since it has the correct capitalization.
// this comment is ignored since it follows another comment,
// and this one as well because it follows yet another comment.

bar();
/* Here is a block comment which has the correct capitalization, */
/* but this one is ignored due to being consecutive; */
/*
 * in fact, even if any of these are multi-line, that is fine too.
 */
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
```

Examples of incorrect code with `ignoreConsecutiveComments` set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiaWdub3JlQ29uc2VjdXRpdmVDb21tZW50c1wiOiB0cnVlIH1dICovXG5cbmZvbygpO1xuLy8gdGhpcyBjb21tZW50IGlzIGludmFsaWQsIGJ1dCBvbmx5IG9uIHRoaXMgbGluZS5cbi8vIHRoaXMgY29tbWVudCBkb2VzIE5PVCBnZXQgcmVwb3J0ZWQsIHNpbmNlIGl0IGlzIGEgY29uc2VjdXRpdmUgY29tbWVudC4ifQ==)

```
/* eslint capitalized-comments: ["error", "always", { "ignoreConsecutiveComments": true }] */

foo();
// this comment is invalid, but only on this line.
// this comment does NOT get reported, since it is a consecutive comment.
1
2
3
4
5
```

### Using Different Options for Line and Block Comments

If you wish to have a different configuration for line comments and block comments, you can do so by using two different object configurations (note that the capitalization option will be enforced consistently for line and block comments):

```
{
    "capitalized-comments": [
        "error",
        "always",
        {
            "line": {
                "ignorePattern": "pragma|ignored",
            },
            "block": {
                "ignoreInlineComments": true,
                "ignorePattern": "ignored"
            }
        }
    ]
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

Examples of incorrect code with different line and block comment configuration:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiYmxvY2tcIjogeyBcImlnbm9yZVBhdHRlcm5cIjogXCJibG9ja2lnbm9yZVwiIH0gfV0gKi9cblxuLy8gY2FwaXRhbGl6ZWQgbGluZSBjb21tZW50LCB0aGlzIGlzIGluY29ycmVjdCwgYmxvY2tpZ25vcmUgZG9lcyBub3QgaGVscCBoZXJlXG4vKiBsb3dlcmNhc2VkIGJsb2NrIGNvbW1lbnQsIHRoaXMgaXMgaW5jb3JyZWN0IHRvbyAqL1xuIn0=)

```
/* eslint capitalized-comments: ["error", "always", { "block": { "ignorePattern": "blockignore" } }] */

// capitalized line comment, this is incorrect, blockignore does not help here
/* lowercased block comment, this is incorrect too */

1
2
3
4
5
```

Examples of correct code with different line and block comment configuration:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGNhcGl0YWxpemVkLWNvbW1lbnRzOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiYmxvY2tcIjogeyBcImlnbm9yZVBhdHRlcm5cIjogXCJibG9ja2lnbm9yZVwiIH0gfV0gKi9cblxuLy8gVXBwZXJjYXNlIGxpbmUgY29tbWVudCwgdGhpcyBpcyBjb3JyZWN0XG4vKiBibG9ja2lnbm9yZSBsb3dlcmNhc2UgYmxvY2sgY29tbWVudCwgdGhpcyBpcyBjb3JyZWN0IGR1ZSB0byBpZ25vcmVQYXR0ZXJuICovXG4ifQ==)

```
/* eslint capitalized-comments: ["error", "always", { "block": { "ignorePattern": "blockignore" } }] */

// Uppercase line comment, this is correct
/* blockignore lowercase block comment, this is correct due to ignorePattern */

1
2
3
4
5
```

## When Not To Use It

This rule can be disabled if you do not care about the grammatical style of comments in your codebase.

## Compatibility

- JSCS: [requireCapitalizedComments](https://jscs-dev.github.io/rule/requireCapitalizedComments)
- JSCS: [disallowCapitalizedComments](https://jscs-dev.github.io/rule/disallowCapitalizedComments)

## Version

This rule was introduced in ESLint v3.11.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/capitalized-comments.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/capitalized-comments.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/capitalized-comments.md
                    
                
                )
