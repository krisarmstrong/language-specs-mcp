# no-cond-assign

Disallow assignment operators in conditional expressions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [except-parens](#except-parens)
  2. [always](#always)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

In conditional statements, it is very easy to mistype a comparison operator (such as `==`) as an assignment operator (such as `=`). For example:

```
// Check the user's job title
if (user.jobTitle = "manager") {
    // user.jobTitle is now incorrect
}
1
2
3
4
```

Copy code to clipboard

There are valid reasons to use assignment operators in conditional statements. However, it can be difficult to tell whether a specific assignment was intentional.

## Rule Details

This rule disallows ambiguous assignment operators in test conditions of `if`, `for`, `while`, and `do...while` statements.

## Options

This rule has a string option:

- `"except-parens"` (default) allows assignments in test conditions only if they are enclosed in parentheses (for example, to allow reassigning a variable in the test of a `while` or `do...while` loop).
- `"always"` disallows all assignments in test conditions.

### except-parens

Examples of incorrect code for this rule with the default `"except-parens"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uZC1hc3NpZ246IFwiZXJyb3JcIiovXG5cbi8vIFVuaW50ZW50aW9uYWwgYXNzaWdubWVudFxubGV0IHg7XG5pZiAoeCA9IDApIHtcbiAgICBjb25zdCBiID0gMTtcbn1cblxuLy8gUHJhY3RpY2FsIGV4YW1wbGUgdGhhdCBpcyBzaW1pbGFyIHRvIGFuIGVycm9yXG5jb25zdCBzZXRIZWlnaHQgPSBmdW5jdGlvbiAoc29tZU5vZGUpIHtcbiAgICBkbyB7XG4gICAgICAgIHNvbWVOb2RlLmhlaWdodCA9IFwiMTAwcHhcIjtcbiAgICB9IHdoaWxlIChzb21lTm9kZSA9IHNvbWVOb2RlLnBhcmVudE5vZGUpO1xufSJ9)

```
/*eslint no-cond-assign: "error"*/

// Unintentional assignment
let x;
if (x = 0) {
    const b = 1;
}

// Practical example that is similar to an error
const setHeight = function (someNode) {
    do {
        someNode.height = "100px";
    } while (someNode = someNode.parentNode);
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
```

Examples of correct code for this rule with the default `"except-parens"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uZC1hc3NpZ246IFwiZXJyb3JcIiovXG5cbi8vIEFzc2lnbm1lbnQgcmVwbGFjZWQgYnkgY29tcGFyaXNvblxubGV0IHg7XG5pZiAoeCA9PT0gMCkge1xuICAgIGNvbnN0IGIgPSAxO1xufVxuXG4vLyBQcmFjdGljYWwgZXhhbXBsZSB0aGF0IHdyYXBzIHRoZSBhc3NpZ25tZW50IGluIHBhcmVudGhlc2VzXG5jb25zdCBzZXRIZWlnaHQgPSBmdW5jdGlvbiAoc29tZU5vZGUpIHtcbiAgICBkbyB7XG4gICAgICAgIHNvbWVOb2RlLmhlaWdodCA9IFwiMTAwcHhcIjtcbiAgICB9IHdoaWxlICgoc29tZU5vZGUgPSBzb21lTm9kZS5wYXJlbnROb2RlKSk7XG59XG5cbi8vIFByYWN0aWNhbCBleGFtcGxlIHRoYXQgd3JhcHMgdGhlIGFzc2lnbm1lbnQgYW5kIHRlc3RzIGZvciAnbnVsbCdcbmNvbnN0IHNldF9oZWlnaHQgPSBmdW5jdGlvbiAoc29tZU5vZGUpIHtcbiAgICBkbyB7XG4gICAgICAgIHNvbWVOb2RlLmhlaWdodCA9IFwiMTAwcHhcIjtcbiAgICB9IHdoaWxlICgoc29tZU5vZGUgPSBzb21lTm9kZS5wYXJlbnROb2RlKSAhPT0gbnVsbCk7XG59In0=)

```
/*eslint no-cond-assign: "error"*/

// Assignment replaced by comparison
let x;
if (x === 0) {
    const b = 1;
}

// Practical example that wraps the assignment in parentheses
const setHeight = function (someNode) {
    do {
        someNode.height = "100px";
    } while ((someNode = someNode.parentNode));
}

// Practical example that wraps the assignment and tests for 'null'
const set_height = function (someNode) {
    do {
        someNode.height = "100px";
    } while ((someNode = someNode.parentNode) !== null);
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

Examples of incorrect code for this rule with the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uZC1hc3NpZ246IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxuLy8gVW5pbnRlbnRpb25hbCBhc3NpZ25tZW50XG5sZXQgeDtcbmlmICh4ID0gMCkge1xuICAgIGNvbnN0IGIgPSAxO1xufVxuXG4vLyBQcmFjdGljYWwgZXhhbXBsZSB0aGF0IGlzIHNpbWlsYXIgdG8gYW4gZXJyb3JcbmNvbnN0IHNldEhlaWdodCA9IGZ1bmN0aW9uIChzb21lTm9kZSkge1xuICAgIGRvIHtcbiAgICAgICAgc29tZU5vZGUuaGVpZ2h0ID0gXCIxMDBweFwiO1xuICAgIH0gd2hpbGUgKHNvbWVOb2RlID0gc29tZU5vZGUucGFyZW50Tm9kZSk7XG59XG5cbi8vIFByYWN0aWNhbCBleGFtcGxlIHRoYXQgd3JhcHMgdGhlIGFzc2lnbm1lbnQgaW4gcGFyZW50aGVzZXNcbmNvbnN0IHNldF9oZWlnaHQgPSBmdW5jdGlvbiAoc29tZU5vZGUpIHtcbiAgICBkbyB7XG4gICAgICAgIHNvbWVOb2RlLmhlaWdodCA9IFwiMTAwcHhcIjtcbiAgICB9IHdoaWxlICgoc29tZU5vZGUgPSBzb21lTm9kZS5wYXJlbnROb2RlKSk7XG59XG5cbi8vIFByYWN0aWNhbCBleGFtcGxlIHRoYXQgd3JhcHMgdGhlIGFzc2lnbm1lbnQgYW5kIHRlc3RzIGZvciAnbnVsbCdcbmNvbnN0IGhlaWdodFNldHRlciA9IGZ1bmN0aW9uIChzb21lTm9kZSkge1xuICAgIGRvIHtcbiAgICAgICAgc29tZU5vZGUuaGVpZ2h0ID0gXCIxMDBweFwiO1xuICAgIH0gd2hpbGUgKChzb21lTm9kZSA9IHNvbWVOb2RlLnBhcmVudE5vZGUpICE9PSBudWxsKTtcbn0ifQ==)

```
/*eslint no-cond-assign: ["error", "always"]*/

// Unintentional assignment
let x;
if (x = 0) {
    const b = 1;
}

// Practical example that is similar to an error
const setHeight = function (someNode) {
    do {
        someNode.height = "100px";
    } while (someNode = someNode.parentNode);
}

// Practical example that wraps the assignment in parentheses
const set_height = function (someNode) {
    do {
        someNode.height = "100px";
    } while ((someNode = someNode.parentNode));
}

// Practical example that wraps the assignment and tests for 'null'
const heightSetter = function (someNode) {
    do {
        someNode.height = "100px";
    } while ((someNode = someNode.parentNode) !== null);
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
```

Examples of correct code for this rule with the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uZC1hc3NpZ246IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxuLy8gQXNzaWdubWVudCByZXBsYWNlZCBieSBjb21wYXJpc29uXG5sZXQgeDtcbmlmICh4ID09PSAwKSB7XG4gICAgY29uc3QgYiA9IDE7XG59In0=)

```
/*eslint no-cond-assign: ["error", "always"]*/

// Assignment replaced by comparison
let x;
if (x === 0) {
    const b = 1;
}
1
2
3
4
5
6
7
```

## Related Rules

- [no-extra-parens](/docs/latest/rules/no-extra-parens)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-cond-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-cond-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-cond-assign.md
                    
                
                )
