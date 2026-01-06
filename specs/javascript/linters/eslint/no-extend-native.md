# no-extend-native

Disallow extending native types

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [exceptions](#exceptions)

3. [Known Limitations](#known-limitations)
4. [When Not To Use It](#when-not-to-use-it)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Resources](#resources)

In JavaScript, you can extend any object, including builtin or “native” objects. Sometimes people change the behavior of these native objects in ways that break the assumptions made about them in other parts of the code.

For example here we are overriding a builtin method that will then affect all Objects, even other builtins.

```
// seems harmless
Object.prototype.extra = 55;

// loop through some userIds
const users = {
    "123": "Stan",
    "456": "David"
};

// not what you'd expect
for (const id in users) {
    console.log(id); // "123", "456", "extra"
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

Copy code to clipboard

A common suggestion to avoid this problem would be to wrap the inside of the `for` loop with `users.hasOwnProperty(id)`. However, if this rule is strictly enforced throughout your codebase you won’t need to take that step.

## Rule Details

Disallows directly modifying the prototype of builtin objects.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0ZW5kLW5hdGl2ZTogXCJlcnJvclwiKi9cblxuT2JqZWN0LnByb3RvdHlwZS5hID0gXCJhXCI7XG5PYmplY3QuZGVmaW5lUHJvcGVydHkoQXJyYXkucHJvdG90eXBlLCBcInRpbWVzXCIsIHsgdmFsdWU6IDk5OSB9KTsifQ==)

```
/*eslint no-extend-native: "error"*/

Object.prototype.a = "a";
Object.defineProperty(Array.prototype, "times", { value: 999 });
1
2
3
4
```

## Options

This rule accepts an `exceptions` option, which can be used to specify a list of builtins for which extensions will be allowed.

### exceptions

Examples of correct code for the sample `{ "exceptions": ["Object"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0ZW5kLW5hdGl2ZTogW1wiZXJyb3JcIiwgeyBcImV4Y2VwdGlvbnNcIjogW1wiT2JqZWN0XCJdIH1dKi9cblxuT2JqZWN0LnByb3RvdHlwZS5hID0gXCJhXCI7In0=)

```
/*eslint no-extend-native: ["error", { "exceptions": ["Object"] }]*/

Object.prototype.a = "a";
1
2
3
```

## Known Limitations

This rule does not report any of the following less obvious approaches to modify the prototype of builtin objects:

```
const x = Object;
x.prototype.thing = a;

eval("Array.prototype.forEach = 'muhahaha'");

with(Array) {
    prototype.thing = 'thing';
};

window.Function.prototype.bind = 'tight';
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

## When Not To Use It

You may want to disable this rule when working with polyfills that try to patch older versions of JavaScript with the latest spec, such as those that might `Function.prototype.bind` or `Array.prototype.forEach` in a future-friendly way.

## Related Rules

- [no-global-assign](/docs/latest/rules/no-global-assign)

## Version

This rule was introduced in ESLint v0.1.4.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-extend-native.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-extend-native.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-extend-native.md
                    
                
                )
