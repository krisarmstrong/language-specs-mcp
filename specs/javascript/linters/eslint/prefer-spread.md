# prefer-spread

Require spread operators instead of `.apply()`

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [Known Limitations](#known-limitations)
4. [When Not To Use It](#when-not-to-use-it)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Resources](#resources)

Before ES2015, one must use `Function.prototype.apply()` to call variadic functions.

```
const args = [1, 2, 3, 4];
Math.max.apply(Math, args);
1
2
```

Copy code to clipboard

In ES2015, one can use spread syntax to call variadic functions.

```
const args = [1, 2, 3, 4];
Math.max(...args);
1
2
```

Copy code to clipboard

## Rule Details

This rule is aimed to flag usage of `Function.prototype.apply()` in situations where spread syntax could be used instead.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXNwcmVhZDogXCJlcnJvclwiKi9cblxuZm9vLmFwcGx5KHVuZGVmaW5lZCwgYXJncyk7XG5mb28uYXBwbHkobnVsbCwgYXJncyk7XG5vYmouZm9vLmFwcGx5KG9iaiwgYXJncyk7In0=)

```
/*eslint prefer-spread: "error"*/

foo.apply(undefined, args);
foo.apply(null, args);
obj.foo.apply(obj, args);
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXNwcmVhZDogXCJlcnJvclwiKi9cblxuLy8gVXNpbmcgc3ByZWFkIHN5bnRheFxuZm9vKC4uLmFyZ3MpO1xub2JqLmZvbyguLi5hcmdzKTtcblxuLy8gVGhlIGB0aGlzYCBiaW5kaW5nIGlzIGRpZmZlcmVudC5cbmZvby5hcHBseShvYmosIGFyZ3MpO1xub2JqLmZvby5hcHBseShudWxsLCBhcmdzKTtcbm9iai5mb28uYXBwbHkob3RoZXJPYmosIGFyZ3MpO1xuXG4vLyBUaGUgYXJndW1lbnQgbGlzdCBpcyBub3QgdmFyaWFkaWMuXG4vLyBUaG9zZSBhcmUgd2FybmVkIGJ5IHRoZSBgbm8tdXNlbGVzcy1jYWxsYCBydWxlLlxuZm9vLmFwcGx5KHVuZGVmaW5lZCwgWzEsIDIsIDNdKTtcbmZvby5hcHBseShudWxsLCBbMSwgMiwgM10pO1xub2JqLmZvby5hcHBseShvYmosIFsxLCAyLCAzXSk7In0=)

```
/*eslint prefer-spread: "error"*/

// Using spread syntax
foo(...args);
obj.foo(...args);

// The `this` binding is different.
foo.apply(obj, args);
obj.foo.apply(null, args);
obj.foo.apply(otherObj, args);

// The argument list is not variadic.
// Those are warned by the `no-useless-call` rule.
foo.apply(undefined, [1, 2, 3]);
foo.apply(null, [1, 2, 3]);
obj.foo.apply(obj, [1, 2, 3]);
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
```

## Known Limitations

This rule analyzes code statically to check whether or not the `this` argument is changed. So, if the `this` argument is computed in a dynamic expression, this rule cannot detect a violation.

```
/*eslint prefer-spread: "error"*/

// This warns.
a[i++].foo.apply(a[i++], args);

// This does not warn.
a[++i].foo.apply(a[i], args);
1
2
3
4
5
6
7
```

Copy code to clipboard

## When Not To Use It

This rule should not be used in ES3/5 environments.

In ES2015 (ES6) or later, if you don’t want to be notified about `Function.prototype.apply()` callings, you can safely disable this rule.

## Related Rules

- [no-useless-call](/docs/latest/rules/no-useless-call)

## Version

This rule was introduced in ESLint v1.0.0-rc-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-spread.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-spread.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-spread.md
                    
                
                )
