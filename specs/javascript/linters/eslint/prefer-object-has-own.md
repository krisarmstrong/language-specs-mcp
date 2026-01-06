# prefer-object-has-own

Disallow use of `Object.prototype.hasOwnProperty.call()` and prefer use of `Object.hasOwn()`

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

It is very common to write code like:

```
if (Object.prototype.hasOwnProperty.call(object, "foo")) {
  console.log("has property foo");
}
1
2
3
```

Copy code to clipboard

This is a common practice because methods on `Object.prototype` can sometimes be unavailable or redefined (see the [no-prototype-builtins](no-prototype-builtins) rule).

Introduced in ES2022, `Object.hasOwn()` is a shorter alternative to `Object.prototype.hasOwnProperty.call()`:

```
if (Object.hasOwn(object, "foo")) {
  console.log("has property foo")
}
1
2
3
```

Copy code to clipboard

## Rule Details

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW9iamVjdC1oYXMtb3duOiBcImVycm9yXCIqL1xuXG5PYmplY3QucHJvdG90eXBlLmhhc093blByb3BlcnR5LmNhbGwob2JqLCBcImFcIik7XG5cbk9iamVjdC5oYXNPd25Qcm9wZXJ0eS5jYWxsKG9iaiwgXCJhXCIpO1xuXG4oe30pLmhhc093blByb3BlcnR5LmNhbGwob2JqLCBcImFcIik7XG5cbmNvbnN0IGhhc1Byb3BlcnR5ID0gT2JqZWN0LnByb3RvdHlwZS5oYXNPd25Qcm9wZXJ0eS5jYWxsKG9iamVjdCwgcHJvcGVydHkpOyJ9)

```
/*eslint prefer-object-has-own: "error"*/

Object.prototype.hasOwnProperty.call(obj, "a");

Object.hasOwnProperty.call(obj, "a");

({}).hasOwnProperty.call(obj, "a");

const hasProperty = Object.prototype.hasOwnProperty.call(object, property);
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW9iamVjdC1oYXMtb3duOiBcImVycm9yXCIqL1xuXG5PYmplY3QuaGFzT3duKG9iaiwgXCJhXCIpO1xuXG5jb25zdCBoYXNQcm9wZXJ0eSA9IE9iamVjdC5oYXNPd24ob2JqZWN0LCBwcm9wZXJ0eSk7In0=)

```
/*eslint prefer-object-has-own: "error"*/

Object.hasOwn(obj, "a");

const hasProperty = Object.hasOwn(object, property);
1
2
3
4
5
```

## When Not To Use It

This rule should not be used unless ES2022 is supported in your codebase.

## Version

This rule was introduced in ESLint v8.5.0.

## Further Reading

[Object.hasOwn() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-object-has-own.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-object-has-own.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-object-has-own.md
                    
                
                )
