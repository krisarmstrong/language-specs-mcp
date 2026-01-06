# no-global-assign

Disallow assignments to native objects or read-only global variables

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

JavaScript environments contain a number of built-in global variables, such as `window` in browsers and `process` in Node.js. In almost all cases, you don’t want to assign a value to these global variables as doing so could result in losing access to important functionality. For example, you probably don’t want to do this in browser code:

```
window = {};
1
```

Copy code to clipboard

While examples such as `window` are obvious, there are often hundreds of built-in global objects provided by JavaScript environments. It can be hard to know if you’re assigning to a global variable or not.

## Rule Details

This rule disallows modifications to read-only global variables.

ESLint has the capability to configure global variables as read-only.

See also: [Specifying Globals](../use/configure#specifying-globals)

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZ2xvYmFsLWFzc2lnbjogXCJlcnJvclwiKi9cblxuT2JqZWN0ID0gbnVsbFxudW5kZWZpbmVkID0gMSJ9)

```
/*eslint no-global-assign: "error"*/

Object = null
undefined = 1
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZ2xvYmFsLWFzc2lnbjogXCJlcnJvclwiKi9cbi8qZ2xvYmFsIHdpbmRvdzpyZWFkb25seSovXG5cbndpbmRvdyA9IHt9In0=)

```
/*eslint no-global-assign: "error"*/
/*global window:readonly*/

window = {}
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZ2xvYmFsLWFzc2lnbjogXCJlcnJvclwiKi9cblxuYSA9IDFcbmxldCBiID0gMVxuYiA9IDIifQ==)

```
/*eslint no-global-assign: "error"*/

a = 1
let b = 1
b = 2
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZ2xvYmFsLWFzc2lnbjogXCJlcnJvclwiKi9cbi8qZ2xvYmFsIG9ubG9hZDp3cml0YWJsZSovXG5cbm9ubG9hZCA9IGZ1bmN0aW9uKCkge30ifQ==)

```
/*eslint no-global-assign: "error"*/
/*global onload:writable*/

onload = function() {}
1
2
3
4
```

## Options

This rule accepts an `exceptions` option, which can be used to specify a list of builtins for which reassignments will be allowed:

```
{
    "rules": {
        "no-global-assign": ["error", {"exceptions": ["Object"]}]
    }
}
1
2
3
4
5
```

Copy code to clipboard

## When Not To Use It

If you are trying to override one of the native objects.

## Related Rules

- [no-extend-native](/docs/latest/rules/no-extend-native)
- [no-redeclare](/docs/latest/rules/no-redeclare)
- [no-shadow](/docs/latest/rules/no-shadow)

## Version

This rule was introduced in ESLint v3.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-global-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-global-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-global-assign.md
                    
                
                )
