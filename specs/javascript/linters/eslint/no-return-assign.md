# no-return-assign

Disallow assignment operators in `return` statements

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [except-parens](#except-parens)
  2. [always](#always)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

One of the interesting, and sometimes confusing, aspects of JavaScript is that assignment can happen at almost any point. Because of this, an errant equals sign can end up causing assignment when the true intent was to do a comparison. This is especially true when using a `return` statement. For example:

```
function doSomething() {
    return foo = bar + 2;
}
1
2
3
```

Copy code to clipboard

It is difficult to tell the intent of the `return` statement here. It’s possible that the function is meant to return the result of `bar + 2`, but then why is it assigning to `foo`? It’s also possible that the intent was to use a comparison operator such as `==` and that this code is an error.

Because of this ambiguity, it’s considered a best practice to not use assignment in `return` statements.

## Rule Details

This rule aims to eliminate assignments from `return` statements. As such, it will warn whenever an assignment is found as part of `return`.

## Options

The rule takes one option, a string, which must contain one of the following values:

- `except-parens` (default): Disallow assignments unless they are enclosed in parentheses.
- `always`: Disallow all assignments.

### except-parens

This is the default option. It disallows assignments unless they are enclosed in parentheses.

Examples of incorrect code for the default `"except-parens"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmV0dXJuLWFzc2lnbjogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7XG4gICAgcmV0dXJuIGZvbyA9IGJhciArIDI7XG59XG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nRWxzZSgpIHtcbiAgICByZXR1cm4gZm9vICs9IDI7XG59XG5cbmNvbnN0IGZvbyA9IChhLCBiKSA9PiBhID0gYlxuXG5jb25zdCBiYXIgPSAoYSwgYiwgYykgPT4gKGEgPSBiLCBjID09IGIpXG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nTW9yZSgpIHtcbiAgICByZXR1cm4gZm9vID0gYmFyICYmIGZvbyA+IDA7XG59In0=)

```
/*eslint no-return-assign: "error"*/

function doSomething() {
    return foo = bar + 2;
}

function doSomethingElse() {
    return foo += 2;
}

const foo = (a, b) => a = b

const bar = (a, b, c) => (a = b, c == b)

function doSomethingMore() {
    return foo = bar && foo > 0;
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
```

Examples of correct code for the default `"except-parens"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmV0dXJuLWFzc2lnbjogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7XG4gICAgcmV0dXJuIGZvbyA9PSBiYXIgKyAyO1xufVxuXG5mdW5jdGlvbiBkb1NvbWV0aGluZ0Vsc2UoKSB7XG4gICAgcmV0dXJuIGZvbyA9PT0gYmFyICsgMjtcbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmdNb3JlKCkge1xuICAgIHJldHVybiAoZm9vID0gYmFyICsgMik7XG59XG5cbmNvbnN0IGZvbyA9IChhLCBiKSA9PiAoYSA9IGIpXG5cbmNvbnN0IGJhciA9IChhLCBiLCBjKSA9PiAoKGEgPSBiKSwgYyA9PSBiKVxuXG5mdW5jdGlvbiBkb0Fub3RoZXJUaGluZygpIHtcbiAgICByZXR1cm4gKGZvbyA9IGJhcikgJiYgZm9vID4gMDtcbn0ifQ==)

```
/*eslint no-return-assign: "error"*/

function doSomething() {
    return foo == bar + 2;
}

function doSomethingElse() {
    return foo === bar + 2;
}

function doSomethingMore() {
    return (foo = bar + 2);
}

const foo = (a, b) => (a = b)

const bar = (a, b, c) => ((a = b), c == b)

function doAnotherThing() {
    return (foo = bar) && foo > 0;
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
```

### always

This option disallows all assignments in `return` statements. All assignments are treated as problems.

Examples of incorrect code for the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmV0dXJuLWFzc2lnbjogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5mdW5jdGlvbiBkb1NvbWV0aGluZygpIHtcbiAgICByZXR1cm4gZm9vID0gYmFyICsgMjtcbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkge1xuICAgIHJldHVybiBmb28gKz0gMjtcbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmdNb3JlKCkge1xuICAgIHJldHVybiAoZm9vID0gYmFyICsgMik7XG59In0=)

```
/*eslint no-return-assign: ["error", "always"]*/

function doSomething() {
    return foo = bar + 2;
}

function doSomethingElse() {
    return foo += 2;
}

function doSomethingMore() {
    return (foo = bar + 2);
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
```

Examples of correct code for the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmV0dXJuLWFzc2lnbjogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5mdW5jdGlvbiBkb1NvbWV0aGluZygpIHtcbiAgICByZXR1cm4gZm9vID09IGJhciArIDI7XG59XG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nRWxzZSgpIHtcbiAgICByZXR1cm4gZm9vID09PSBiYXIgKyAyO1xufSJ9)

```
/*eslint no-return-assign: ["error", "always"]*/

function doSomething() {
    return foo == bar + 2;
}

function doSomethingElse() {
    return foo === bar + 2;
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
```

## When Not To Use It

If you want to allow the use of assignment operators in a `return` statement, then you can safely disable this rule.

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-return-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-return-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-return-assign.md
                    
                
                )
