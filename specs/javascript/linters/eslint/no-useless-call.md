# no-useless-call

Disallow unnecessary calls to `.call()` and `.apply()`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

The function invocation can be written by `Function.prototype.call()` and `Function.prototype.apply()`. But `Function.prototype.call()` and `Function.prototype.apply()` are slower than the normal function invocation.

## Rule Details

This rule is aimed to flag usage of `Function.prototype.call()` and `Function.prototype.apply()` that can be replaced with the normal function invocation.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jYWxsOiBcImVycm9yXCIqL1xuXG4vLyBUaGVzZSBhcmUgc2FtZSBhcyBgZm9vKDEsIDIsIDMpO2BcbmZvby5jYWxsKHVuZGVmaW5lZCwgMSwgMiwgMyk7XG5mb28uYXBwbHkodW5kZWZpbmVkLCBbMSwgMiwgM10pO1xuZm9vLmNhbGwobnVsbCwgMSwgMiwgMyk7XG5mb28uYXBwbHkobnVsbCwgWzEsIDIsIDNdKTtcblxuLy8gVGhlc2UgYXJlIHNhbWUgYXMgYG9iai5mb28oMSwgMiwgMyk7YFxub2JqLmZvby5jYWxsKG9iaiwgMSwgMiwgMyk7XG5vYmouZm9vLmFwcGx5KG9iaiwgWzEsIDIsIDNdKTsifQ==)

```
/*eslint no-useless-call: "error"*/

// These are same as `foo(1, 2, 3);`
foo.call(undefined, 1, 2, 3);
foo.apply(undefined, [1, 2, 3]);
foo.call(null, 1, 2, 3);
foo.apply(null, [1, 2, 3]);

// These are same as `obj.foo(1, 2, 3);`
obj.foo.call(obj, 1, 2, 3);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jYWxsOiBcImVycm9yXCIqL1xuXG4vLyBUaGUgYHRoaXNgIGJpbmRpbmcgaXMgZGlmZmVyZW50LlxuZm9vLmNhbGwob2JqLCAxLCAyLCAzKTtcbmZvby5hcHBseShvYmosIFsxLCAyLCAzXSk7XG5vYmouZm9vLmNhbGwobnVsbCwgMSwgMiwgMyk7XG5vYmouZm9vLmFwcGx5KG51bGwsIFsxLCAyLCAzXSk7XG5vYmouZm9vLmNhbGwob3RoZXJPYmosIDEsIDIsIDMpO1xub2JqLmZvby5hcHBseShvdGhlck9iaiwgWzEsIDIsIDNdKTtcblxuLy8gVGhlIGFyZ3VtZW50IGxpc3QgaXMgdmFyaWFkaWMuXG4vLyBUaG9zZSBhcmUgd2FybmVkIGJ5IHRoZSBgcHJlZmVyLXNwcmVhZGAgcnVsZS5cbmZvby5hcHBseSh1bmRlZmluZWQsIGFyZ3MpO1xuZm9vLmFwcGx5KG51bGwsIGFyZ3MpO1xub2JqLmZvby5hcHBseShvYmosIGFyZ3MpOyJ9)

```
/*eslint no-useless-call: "error"*/

// The `this` binding is different.
foo.call(obj, 1, 2, 3);
foo.apply(obj, [1, 2, 3]);
obj.foo.call(null, 1, 2, 3);
obj.foo.apply(null, [1, 2, 3]);
obj.foo.call(otherObj, 1, 2, 3);
obj.foo.apply(otherObj, [1, 2, 3]);

// The argument list is variadic.
// Those are warned by the `prefer-spread` rule.
foo.apply(undefined, args);
foo.apply(null, args);
obj.foo.apply(obj, args);
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

## Known Limitations

This rule compares code statically to check whether or not `thisArg` is changed. So if the code about `thisArg` is a dynamic expression, this rule cannot judge correctly.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jYWxsOiBcImVycm9yXCIqL1xuXG5hW2krK10uZm9vLmNhbGwoYVtpKytdLCAxLCAyLCAzKTsifQ==)

```
/*eslint no-useless-call: "error"*/

a[i++].foo.call(a[i++], 1, 2, 3);
1
2
3
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jYWxsOiBcImVycm9yXCIqL1xuXG5hWysraV0uZm9vLmNhbGwoYVtpXSwgMSwgMiwgMyk7In0=)

```
/*eslint no-useless-call: "error"*/

a[++i].foo.call(a[i], 1, 2, 3);
1
2
3
```

## When Not To Use It

If you don’t want to be notified about unnecessary `.call()` and `.apply()`, you can safely disable this rule.

## Related Rules

- [prefer-spread](/docs/latest/rules/prefer-spread)

## Version

This rule was introduced in ESLint v1.0.0-rc-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-call.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-call.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-call.md
                    
                
                )
