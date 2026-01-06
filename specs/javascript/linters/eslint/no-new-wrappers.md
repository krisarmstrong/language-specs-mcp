# no-new-wrappers

Disallow `new` operators with the `String`, `Number`, and `Boolean` objects

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

There are three primitive types in JavaScript that have wrapper objects: string, number, and boolean. These are represented by the constructors `String`, `Number`, and `Boolean`, respectively. The primitive wrapper types are used whenever one of these primitive values is read, providing them with object-like capabilities such as methods. Behind the scenes, an object of the associated wrapper type is created and then destroyed, which is why you can call methods on primitive values, such as:

```
const text = "Hello world".substring(2);
1
```

Copy code to clipboard

Behind the scenes in this example, a `String` object is constructed. The `substring()` method exists on `String.prototype` and so is accessible to the string instance.

It’s also possible to manually create a new wrapper instance:

```
const stringObject = new String("Hello world");
const numberObject = new Number(33);
const booleanObject = new Boolean(false);
1
2
3
```

Copy code to clipboard

Although possible, there aren’t any good reasons to use these primitive wrappers as constructors. They tend to confuse other developers more than anything else because they seem like they should act as primitives, but they do not. For example:

```
const stringObject = new String("Hello world");
console.log(typeof stringObject);       // "object"

const text = "Hello world";
console.log(typeof text);               // "string"

const booleanObject = new Boolean(false);
if (booleanObject) {    // all objects are truthy!
    console.log("This executes");
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
```

Copy code to clipboard

The first problem is that primitive wrapper objects are, in fact, objects. That means `typeof` will return `"object"` instead of `"string"`, `"number"`, or `"boolean"`. The second problem comes with boolean objects. Every object is truthy, that means an instance of `Boolean` always resolves to `true` even when its actual value is `false`.

For these reasons, it’s considered a best practice to avoid using primitive wrapper types with `new`.

## Rule Details

This rule aims to eliminate the use of `String`, `Number`, and `Boolean` with the `new` operator. As such, it warns whenever it sees `new String`, `new Number`, or `new Boolean`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3LXdyYXBwZXJzOiBcImVycm9yXCIqL1xuXG5jb25zdCBzdHJpbmdPYmplY3QgPSBuZXcgU3RyaW5nKFwiSGVsbG8gd29ybGRcIik7XG5jb25zdCBudW1iZXJPYmplY3QgPSBuZXcgTnVtYmVyKDMzKTtcbmNvbnN0IGJvb2xlYW5PYmplY3QgPSBuZXcgQm9vbGVhbihmYWxzZSk7XG5cbmNvbnN0IHN0cmluZ09iamVjdDIgPSBuZXcgU3RyaW5nO1xuY29uc3QgbnVtYmVyT2JqZWN0MiA9IG5ldyBOdW1iZXI7XG5jb25zdCBib29sZWFuT2JqZWN0MiA9IG5ldyBCb29sZWFuOyJ9)

```
/*eslint no-new-wrappers: "error"*/

const stringObject = new String("Hello world");
const numberObject = new Number(33);
const booleanObject = new Boolean(false);

const stringObject2 = new String;
const numberObject2 = new Number;
const booleanObject2 = new Boolean;
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmV3LXdyYXBwZXJzOiBcImVycm9yXCIqL1xuXG5jb25zdCB0ZXh0ID0gU3RyaW5nKHNvbWVWYWx1ZSk7XG5jb25zdCBudW0gPSBOdW1iZXIoc29tZVZhbHVlKTtcblxuY29uc3Qgb2JqZWN0ID0gbmV3IE15U3RyaW5nKCk7In0=)

```
/*eslint no-new-wrappers: "error"*/

const text = String(someValue);
const num = Number(someValue);

const object = new MyString();
1
2
3
4
5
6
```

## When Not To Use It

If you want to allow the use of primitive wrapper objects, then you can safely disable this rule.

## Related Rules

- [no-array-constructor](/docs/latest/rules/no-array-constructor)
- [no-object-constructor](/docs/latest/rules/no-object-constructor)

## Version

This rule was introduced in ESLint v0.0.6.

## Further Reading

[Unsupported Browser](https://www.inkling.com/read/javascript-definitive-guide-david-flanagan-6th/chapter-3/wrapper-objects)
 www.inkling.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-new-wrappers.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-new-wrappers.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-new-wrappers.md
                    
                
                )
