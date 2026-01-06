# no-prototype-builtins

Disallow calling some `Object.prototype` methods directly on objects

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

In ECMAScript 5.1, `Object.create` was added, which enables the creation of objects with a specified `[[Prototype]]`. `Object.create(null)` is a common pattern used to create objects that will be used as a Map. This can lead to errors when it is assumed that objects will have properties from `Object.prototype`. This rule prevents calling some `Object.prototype` methods directly from an object.

Additionally, objects can have properties that shadow the builtins on `Object.prototype`, potentially causing unintended behavior or denial-of-service security vulnerabilities. For example, it would be unsafe for a webserver to parse JSON input from a client and call `hasOwnProperty` directly on the resulting object, because a malicious client could send a JSON value like `{"hasOwnProperty": 1}` and cause the server to crash.

To avoid subtle bugs like this, it’s better to always call these methods from `Object.prototype`. For example, `foo.hasOwnProperty("bar")` should be replaced with `Object.prototype.hasOwnProperty.call(foo, "bar")`.

## Rule Details

This rule disallows calling some `Object.prototype` methods directly on object instances.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvdG90eXBlLWJ1aWx0aW5zOiBcImVycm9yXCIqL1xuXG5jb25zdCBoYXNCYXJQcm9wZXJ0eSA9IGZvby5oYXNPd25Qcm9wZXJ0eShcImJhclwiKTtcblxuY29uc3QgaXNQcm90b3R5cGVPZkJhciA9IGZvby5pc1Byb3RvdHlwZU9mKGJhcik7XG5cbmNvbnN0IGJhcklzRW51bWVyYWJsZSA9IGZvby5wcm9wZXJ0eUlzRW51bWVyYWJsZShcImJhclwiKTsifQ==)

```
/*eslint no-prototype-builtins: "error"*/

const hasBarProperty = foo.hasOwnProperty("bar");

const isPrototypeOfBar = foo.isPrototypeOf(bar);

const barIsEnumerable = foo.propertyIsEnumerable("bar");
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvdG90eXBlLWJ1aWx0aW5zOiBcImVycm9yXCIqL1xuXG5jb25zdCBoYXNCYXJQcm9wZXJ0eSA9IE9iamVjdC5wcm90b3R5cGUuaGFzT3duUHJvcGVydHkuY2FsbChmb28sIFwiYmFyXCIpO1xuXG5jb25zdCBpc1Byb3RvdHlwZU9mQmFyID0gT2JqZWN0LnByb3RvdHlwZS5pc1Byb3RvdHlwZU9mLmNhbGwoZm9vLCBiYXIpO1xuXG5jb25zdCBiYXJJc0VudW1lcmFibGUgPSB7fS5wcm9wZXJ0eUlzRW51bWVyYWJsZS5jYWxsKGZvbywgXCJiYXJcIik7In0=)

```
/*eslint no-prototype-builtins: "error"*/

const hasBarProperty = Object.prototype.hasOwnProperty.call(foo, "bar");

const isPrototypeOfBar = Object.prototype.isPrototypeOf.call(foo, bar);

const barIsEnumerable = {}.propertyIsEnumerable.call(foo, "bar");
1
2
3
4
5
6
7
```

## When Not To Use It

You may want to turn this rule off if your code only touches objects with hardcoded keys, and you will never use an object that shadows an `Object.prototype` method or which does not inherit from `Object.prototype`.

## Version

This rule was introduced in ESLint v2.11.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-prototype-builtins.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-prototype-builtins.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-prototype-builtins.md
                    
                
                )
