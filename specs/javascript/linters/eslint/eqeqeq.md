# eqeqeq

Require the use of `===` and `!==`

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [smart](#smart)
  3. [allow-null](#allow-null)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

It is considered good practice to use the type-safe equality operators `===` and `!==` instead of their regular counterparts `==` and `!=`.

The reason for this is that `==` and `!=` do type coercion which follows the rather obscure [Abstract Equality Comparison Algorithm](https://www.ecma-international.org/ecma-262/5.1/#sec-11.9.3). For instance, the following statements are all considered `true`:

- `[] == false`
- `[] == ![]`
- `3 == "03"`

If one of those occurs in an innocent-looking statement such as `a == b` the actual problem is very difficult to spot.

## Rule Details

This rule is aimed at eliminating the type-unsafe equality operators.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZXFlcWVxOiBcImVycm9yXCIqL1xuXG5pZiAoeCA9PSA0MikgeyB9XG5cbmlmIChcIlwiID09IHRleHQpIHsgfVxuXG5pZiAob2JqLmdldFN0dWZmKCkgIT0gdW5kZWZpbmVkKSB7IH0ifQ==)

```
/*eslint eqeqeq: "error"*/

if (x == 42) { }

if ("" == text) { }

if (obj.getStuff() != undefined) { }
1
2
3
4
5
6
7
```

The `--fix` option on the command line automatically fixes some problems reported by this rule. A problem is only fixed if one of the operands is a `typeof` expression, or if both operands are literals with the same type.

## Options

### always

The `"always"` option (default) enforces the use of `===` and `!==` in every situation (except when you opt-in to more specific handling of `null` [see below]).

Examples of incorrect code for the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZXFlcWVxOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiXSovXG5cbmEgPT0gYlxuZm9vID09IHRydWVcbmJhbmFuYXMgIT0gMVxudmFsdWUgPT0gdW5kZWZpbmVkXG50eXBlb2YgZm9vID09ICd1bmRlZmluZWQnXG4naGVsbG8nICE9ICd3b3JsZCdcbjAgPT0gMFxudHJ1ZSA9PSB0cnVlXG5mb28gPT0gbnVsbFxuIn0=)

```
/*eslint eqeqeq: ["error", "always"]*/

a == b
foo == true
bananas != 1
value == undefined
typeof foo == 'undefined'
'hello' != 'world'
0 == 0
true == true
foo == null

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

Examples of correct code for the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZXFlcWVxOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiXSovXG5cbmEgPT09IGJcbmZvbyA9PT0gdHJ1ZVxuYmFuYW5hcyAhPT0gMVxudmFsdWUgPT09IHVuZGVmaW5lZFxudHlwZW9mIGZvbyA9PT0gJ3VuZGVmaW5lZCdcbidoZWxsbycgIT09ICd3b3JsZCdcbjAgPT09IDBcbnRydWUgPT09IHRydWVcbmZvbyA9PT0gbnVsbFxuIn0=)

```
/*eslint eqeqeq: ["error", "always"]*/

a === b
foo === true
bananas !== 1
value === undefined
typeof foo === 'undefined'
'hello' !== 'world'
0 === 0
true === true
foo === null

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

This rule optionally takes a second argument, which should be an object with the following supported properties:

- `"null"`: Customize how this rule treats `null` literals. Possible values: 

  - `always` (default) - Always use `===` or `!==`.
  - `never` - Never use `===` or `!==` with `null`.
  - `ignore` - Do not apply this rule to `null`.

### smart

The `"smart"` option enforces the use of `===` and `!==` except for these cases:

- Comparing two literal values.
- Evaluating the value of `typeof`.
- Comparing against `null`.

Examples of incorrect code for the `"smart"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZXFlcWVxOiBbXCJlcnJvclwiLCBcInNtYXJ0XCJdKi9cblxuLy8gY29tcGFyaW5nIHR3byB2YXJpYWJsZXMgcmVxdWlyZXMgPT09XG5hID09IGJcblxuLy8gb25seSBvbmUgc2lkZSBpcyBhIGxpdGVyYWxcbmZvbyA9PSB0cnVlXG5iYW5hbmFzICE9IDFcblxuLy8gY29tcGFyaW5nIHRvIHVuZGVmaW5lZCByZXF1aXJlcyA9PT1cbnZhbHVlID09IHVuZGVmaW5lZCJ9)

```
/*eslint eqeqeq: ["error", "smart"]*/

// comparing two variables requires ===
a == b

// only one side is a literal
foo == true
bananas != 1

// comparing to undefined requires ===
value == undefined
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

Examples of correct code for the `"smart"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZXFlcWVxOiBbXCJlcnJvclwiLCBcInNtYXJ0XCJdKi9cblxudHlwZW9mIGZvbyA9PSAndW5kZWZpbmVkJ1xuJ2hlbGxvJyAhPSAnd29ybGQnXG4wID09IDBcbnRydWUgPT0gdHJ1ZVxuZm9vID09IG51bGwifQ==)

```
/*eslint eqeqeq: ["error", "smart"]*/

typeof foo == 'undefined'
'hello' != 'world'
0 == 0
true == true
foo == null
1
2
3
4
5
6
7
```

### allow-null

Deprecated: Instead of using this option use `"always"` and pass a `"null"` option property with value `"ignore"`. This will tell ESLint to always enforce strict equality except when comparing with the `null` literal.

```
["error", "always", {"null": "ignore"}]
1
```

Copy code to clipboard

## When Not To Use It

If you don’t want to enforce a style for using equality operators, then it’s safe to disable this rule.

## Version

This rule was introduced in ESLint v0.0.2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/eqeqeq.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/eqeqeq.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/eqeqeq.md
                    
                
                )
