# prefer-regex-literals

Disallow use of the `RegExp` constructor in favor of regular expression literals

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [disallowRedundantWrapping](#disallowredundantwrapping)

3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

There are two ways to create a regular expression:

- Regular expression literals, e.g., `/abc/u`.
- The `RegExp` constructor function, e.g., `new RegExp("abc", "u")` or `RegExp("abc", "u")`.

The constructor function is particularly useful when you want to dynamically generate the pattern, because it takes string arguments.

When using the constructor function with string literals, don’t forget that the string escaping rules still apply. If you want to put a backslash in the pattern, you need to escape it in the string literal. Thus, the following are equivalent:

```
new RegExp("^\\d\\.$");

/^\d\.$/;

// matches "0.", "1.", "2." ... "9."
1
2
3
4
5
```

Copy code to clipboard

In the above example, the regular expression literal is easier to read and reason about. Also, it’s a common mistake to omit the extra `\` in the string literal, which would produce a completely different regular expression:

```
new RegExp("^\d\.$");

// equivalent to /^d.$/, matches "d1", "d2", "da", "db" ...
1
2
3
```

Copy code to clipboard

When a regular expression is known in advance, it is considered a best practice to avoid the string literal notation on top of the regular expression notation, and use regular expression literals instead of the constructor function.

## Rule Details

This rule disallows the use of the `RegExp` constructor function with string literals as its arguments.

This rule also disallows the use of the `RegExp` constructor function with template literals without expressions and `String.raw` tagged template literals without expressions.

The rule does not disallow all use of the `RegExp` constructor. It should be still used for dynamically generated regular expressions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXJlZ2V4LWxpdGVyYWxzOiBcImVycm9yXCIqL1xuXG5uZXcgUmVnRXhwKFwiYWJjXCIpO1xuXG5uZXcgUmVnRXhwKFwiYWJjXCIsIFwidVwiKTtcblxuUmVnRXhwKFwiYWJjXCIpO1xuXG5SZWdFeHAoXCJhYmNcIiwgXCJ1XCIpO1xuXG5uZXcgUmVnRXhwKFwiXFxcXGRcXFxcZFxcXFwuXFxcXGRcXFxcZFxcXFwuXFxcXGRcXFxcZFxcXFxkXFxcXGRcIik7XG5cblJlZ0V4cChgXlxcXFxkXFxcXC4kYCk7XG5cbm5ldyBSZWdFeHAoU3RyaW5nLnJhd2BeXFxkXFwuJGApOyJ9)

```
/*eslint prefer-regex-literals: "error"*/

new RegExp("abc");

new RegExp("abc", "u");

RegExp("abc");

RegExp("abc", "u");

new RegExp("\\d\\d\\.\\d\\d\\.\\d\\d\\d\\d");

RegExp(`^\\d\\.$`);

new RegExp(String.raw`^\d\.$`);
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXJlZ2V4LWxpdGVyYWxzOiBcImVycm9yXCIqL1xuXG4vYWJjLztcblxuL2FiYy91O1xuXG4vXFxkXFxkXFwuXFxkXFxkXFwuXFxkXFxkXFxkXFxkLztcblxuL15cXGRcXC4kLztcblxuLy8gUmVnRXhwIGNvbnN0cnVjdG9yIGlzIGFsbG93ZWQgZm9yIGR5bmFtaWNhbGx5IGdlbmVyYXRlZCByZWd1bGFyIGV4cHJlc3Npb25zXG5cbm5ldyBSZWdFeHAocGF0dGVybik7XG5cblJlZ0V4cChcImFiY1wiLCBmbGFncyk7XG5cbm5ldyBSZWdFeHAocHJlZml4ICsgXCJhYmNcIik7XG5cblJlZ0V4cChgJHtwcmVmaXh9YWJjYCk7XG5cbm5ldyBSZWdFeHAoU3RyaW5nLnJhd2BeXFxkXFwuICR7c3VmZml4fWApOyJ9)

```
/*eslint prefer-regex-literals: "error"*/

/abc/;

/abc/u;

/\d\d\.\d\d\.\d\d\d\d/;

/^\d\.$/;

// RegExp constructor is allowed for dynamically generated regular expressions

new RegExp(pattern);

RegExp("abc", flags);

new RegExp(prefix + "abc");

RegExp(`${prefix}abc`);

new RegExp(String.raw`^\d\. ${suffix}`);
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
```

## Options

This rule has an object option:

- `disallowRedundantWrapping` set to `true` additionally checks for unnecessarily wrapped regex literals (Default `false`).

### disallowRedundantWrapping

By default, this rule doesn’t check when a regex literal is unnecessarily wrapped in a `RegExp` constructor call. When the option `disallowRedundantWrapping` is set to `true`, the rule will also disallow such unnecessary patterns.

Examples of `incorrect` code for `{ "disallowRedundantWrapping": true }`

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXJlZ2V4LWxpdGVyYWxzOiBbXCJlcnJvclwiLCB7XCJkaXNhbGxvd1JlZHVuZGFudFdyYXBwaW5nXCI6IHRydWV9XSovXG5cbm5ldyBSZWdFeHAoL2FiYy8pO1xuXG5uZXcgUmVnRXhwKC9hYmMvLCAndScpOyJ9)

```
/*eslint prefer-regex-literals: ["error", {"disallowRedundantWrapping": true}]*/

new RegExp(/abc/);

new RegExp(/abc/, 'u');
1
2
3
4
5
```

Examples of `correct` code for `{ "disallowRedundantWrapping": true }`

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXJlZ2V4LWxpdGVyYWxzOiBbXCJlcnJvclwiLCB7XCJkaXNhbGxvd1JlZHVuZGFudFdyYXBwaW5nXCI6IHRydWV9XSovXG5cbi9hYmMvO1xuXG4vYWJjL3U7XG5cbm5ldyBSZWdFeHAoL2FiYy8sIGZsYWdzKTsifQ==)

```
/*eslint prefer-regex-literals: ["error", {"disallowRedundantWrapping": true}]*/

/abc/;

/abc/u;

new RegExp(/abc/, flags);
1
2
3
4
5
6
7
```

## Version

This rule was introduced in ESLint v6.4.0.

## Further Reading

[Regular expressions - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
 developer.mozilla.org[RegExp - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-regex-literals.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-regex-literals.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-regex-literals.md
                    
                
                )
