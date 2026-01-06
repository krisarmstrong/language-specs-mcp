# no-object-constructor

Disallow calls to the `Object` constructor without an argument

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Use of the `Object` constructor to construct a new empty object is generally discouraged in favor of object literal notation because of conciseness and because the `Object` global may be redefined. The exception is when the `Object` constructor is used to intentionally wrap a specified value which is passed as an argument.

## Rule Details

This rule disallows calling the `Object` constructor without an argument.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tb2JqZWN0LWNvbnN0cnVjdG9yOiBcImVycm9yXCIqL1xuXG5PYmplY3QoKTtcblxubmV3IE9iamVjdCgpOyJ9)

```
/*eslint no-object-constructor: "error"*/

Object();

new Object();
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tb2JqZWN0LWNvbnN0cnVjdG9yOiBcImVycm9yXCIqL1xuXG5PYmplY3QoXCJmb29cIik7XG5cbmNvbnN0IG9iaiA9IHsgYTogMSwgYjogMiB9O1xuXG5jb25zdCBpc09iamVjdCA9IHZhbHVlID0+IHZhbHVlID09PSBPYmplY3QodmFsdWUpO1xuXG5jb25zdCBjcmVhdGVPYmplY3QgPSBPYmplY3QgPT4gbmV3IE9iamVjdCgpOyJ9)

```
/*eslint no-object-constructor: "error"*/

Object("foo");

const obj = { a: 1, b: 2 };

const isObject = value => value === Object(value);

const createObject = Object => new Object();
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

If you wish to allow the use of the `Object` constructor, you can safely turn this rule off.

## Related Rules

- [no-array-constructor](/docs/latest/rules/no-array-constructor)
- [no-new-wrappers](/docs/latest/rules/no-new-wrappers)

## Version

This rule was introduced in ESLint v8.50.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-object-constructor.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-object-constructor.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-object-constructor.md
                    
                
                )
