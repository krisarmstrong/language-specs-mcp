# no-obj-calls

Disallow calling global object properties as functions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Handled by TypeScript](#handled_by_typescript)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

ECMAScript provides several global objects that are intended to be used as-is. Some of these objects look as if they could be constructors due their capitalization (such as `Math` and `JSON`) but will throw an error if you try to execute them as functions.

The [ECMAScript 5 specification](https://es5.github.io/#x15.8) makes it clear that both `Math` and `JSON` cannot be invoked:

The Math object does not have a `[[Call]]` internal property; it is not possible to invoke the Math object as a function.

The [ECMAScript 2015 specification](https://www.ecma-international.org/ecma-262/6.0/index.html#sec-reflect-object) makes it clear that `Reflect` cannot be invoked:

The Reflect object also does not have a `[[Call]]` internal method; it is not possible to invoke the Reflect object as a function.

The [ECMAScript 2017 specification](https://www.ecma-international.org/ecma-262/8.0/index.html#sec-atomics-object) makes it clear that `Atomics` cannot be invoked:

The Atomics object does not have a `[[Call]]` internal method; it is not possible to invoke the Atomics object as a function.

And the [ECMAScript Internationalization API Specification](https://tc39.es/ecma402/#intl-object) makes it clear that `Intl` cannot be invoked:

The Intl object does not have a `[[Call]]` internal method; it is not possible to invoke the Intl object as a function.

## Rule Details

This rule disallows calling the `Math`, `JSON`, `Reflect`, `Atomics` and `Intl` objects as functions.

This rule also disallows using these objects as constructors with the `new` operator.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tb2JqLWNhbGxzOiBcImVycm9yXCIqL1xuXG5jb25zdCBtYXRoID0gTWF0aCgpO1xuXG5jb25zdCBuZXdNYXRoID0gbmV3IE1hdGgoKTtcblxuY29uc3QganNvbiA9IEpTT04oKTtcblxuY29uc3QgbmV3SlNPTiA9IG5ldyBKU09OKCk7XG5cbmNvbnN0IHJlZmxlY3QgPSBSZWZsZWN0KCk7XG5cbmNvbnN0IG5ld1JlZmxlY3QgPSBuZXcgUmVmbGVjdCgpO1xuXG5jb25zdCBhdG9taWNzID0gQXRvbWljcygpO1xuXG5jb25zdCBuZXdBdG9taWNzID0gbmV3IEF0b21pY3MoKTtcblxuY29uc3QgaW50bCA9IEludGwoKTtcblxuY29uc3QgbmV3SW50bCA9IG5ldyBJbnRsKCk7In0=)

```
/*eslint no-obj-calls: "error"*/

const math = Math();

const newMath = new Math();

const json = JSON();

const newJSON = new JSON();

const reflect = Reflect();

const newReflect = new Reflect();

const atomics = Atomics();

const newAtomics = new Atomics();

const intl = Intl();

const newIntl = new Intl();
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tb2JqLWNhbGxzOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBhcmVhKHIpIHtcbiAgICByZXR1cm4gTWF0aC5QSSAqIHIgKiByO1xufVxuXG5jb25zdCBvYmplY3QgPSBKU09OLnBhcnNlKFwie31cIik7XG5cbmNvbnN0IHZhbHVlID0gUmVmbGVjdC5nZXQoeyB4OiAxLCB5OiAyIH0sIFwieFwiKTtcblxuY29uc3QgZmlyc3QgPSBBdG9taWNzLmxvYWQoZm9vLCAwKTtcblxuY29uc3Qgc2VnbWVudGVyRnIgPSBuZXcgSW50bC5TZWdtZW50ZXIoXCJmclwiLCB7IGdyYW51bGFyaXR5OiBcIndvcmRcIiB9KTsifQ==)

```
/*eslint no-obj-calls: "error"*/

function area(r) {
    return Math.PI * r * r;
}

const object = JSON.parse("{}");

const value = Reflect.get({ x: 1, y: 2 }, "x");

const first = Atomics.load(foo, 0);

const segmenterFr = new Intl.Segmenter("fr", { granularity: "word" });
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

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[Annotated ES5](https://es5.github.io/#x15.8)
 es5.github.io

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-obj-calls.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-obj-calls.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-obj-calls.md
                    
                
                )
