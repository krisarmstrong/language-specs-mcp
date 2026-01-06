# no-proto

Disallow the use of the `__proto__` property

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

`__proto__` property has been deprecated as of ECMAScript 3.1 and shouldn’t be used in the code. Use `Object.getPrototypeOf` and `Object.setPrototypeOf` instead.

## Rule Details

When an object is created with the `new` operator, `__proto__` is set to the original “prototype” property of the object’s constructor function. `Object.getPrototypeOf` is the preferred method of getting the object’s prototype. To change an object’s prototype, use `Object.setPrototypeOf`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvdG86IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSBvYmouX19wcm90b19fO1xuXG5jb25zdCBhMSA9IG9ialtcIl9fcHJvdG9fX1wiXTtcblxub2JqLl9fcHJvdG9fXyA9IGI7XG5cbm9ialtcIl9fcHJvdG9fX1wiXSA9IGI7In0=)

```
/*eslint no-proto: "error"*/

const a = obj.__proto__;

const a1 = obj["__proto__"];

obj.__proto__ = b;

obj["__proto__"] = b;
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvdG86IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSBPYmplY3QuZ2V0UHJvdG90eXBlT2Yob2JqKTtcblxuT2JqZWN0LnNldFByb3RvdHlwZU9mKG9iaiwgYik7XG5cbmNvbnN0IGMgPSB7IF9fcHJvdG9fXzogYSB9OyJ9)

```
/*eslint no-proto: "error"*/

const a = Object.getPrototypeOf(obj);

Object.setPrototypeOf(obj, b);

const c = { __proto__: a };
1
2
3
4
5
6
7
```

## When Not To Use It

You might want to turn this rule off if you need to support legacy browsers which implement the `__proto__` property but not `Object.getPrototypeOf` or `Object.setPrototypeOf`.

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[John Resig - Object.getPrototypeOf](https://johnresig.com/blog/objectgetprototypeof/)
 johnresig.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-proto.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-proto.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-proto.md
                    
                
                )
