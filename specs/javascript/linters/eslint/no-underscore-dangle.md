# no-underscore-dangle

Disallow dangling underscores in identifiers

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allow](#allow)
  2. [allowAfterThis](#allowafterthis)
  3. [allowAfterSuper](#allowaftersuper)
  4. [allowAfterThisConstructor](#allowafterthisconstructor)
  5. [enforceInMethodNames](#enforceinmethodnames)
  6. [enforceInClassFields](#enforceinclassfields)
  7. [allowInArrayDestructuring](#allowinarraydestructuring)
  8. [allowInObjectDestructuring](#allowinobjectdestructuring)
  9. [allowFunctionParams](#allowfunctionparams)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

As far as naming conventions for identifiers go, dangling underscores may be the most polarizing in JavaScript. Dangling underscores are underscores at either the beginning or end of an identifier, such as:

```
let _foo;
1
```

Copy code to clipboard

There is a long history of marking “private” members with dangling underscores in JavaScript, beginning with SpiderMonkey adding nonstandard methods such as `__defineGetter__()`. Since that time, using a single underscore prefix has become the most popular convention for indicating a member is not part of the public interface of an object.

It is recommended to use the formal [private class features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields) introduced in ECMAScript 2022 for encapsulating private data and methods rather than relying on naming conventions.

Allowing dangling underscores in identifiers is purely a convention and has no effect on performance, readability, or complexity. They do not have the same encapsulation benefits as private class features, even with this rule enabled.

## Rule Details

This rule disallows dangling underscores in identifiers.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFwiZXJyb3JcIiovXG5cbmxldCBmb29fO1xuY29uc3QgX19wcm90b19fID0ge307XG5mb28uX2JhcigpOyJ9)

```
/*eslint no-underscore-dangle: "error"*/

let foo_;
const __proto__ = {};
foo._bar();
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFwiZXJyb3JcIiovXG5cbmNvbnN0IF8gPSByZXF1aXJlKCd1bmRlcnNjb3JlJyk7XG5jb25zdCBvYmogPSBfLmNvbnRhaW5zKGl0ZW1zLCBpdGVtKTtcbm9iai5fX3Byb3RvX18gPSB7fTtcbmNvbnN0IGZpbGUgPSBfX2ZpbGVuYW1lO1xuZnVuY3Rpb24gZm9vKF9iYXIpIHt9O1xuY29uc3QgYmFyID0geyBvbkNsaWNrKF9iYXIpIHt9IH07XG5jb25zdCBiYXogPSAoX2JhcikgPT4ge307In0=)

```
/*eslint no-underscore-dangle: "error"*/

const _ = require('underscore');
const obj = _.contains(items, item);
obj.__proto__ = {};
const file = __filename;
function foo(_bar) {};
const bar = { onClick(_bar) {} };
const baz = (_bar) => {};
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

## Options

This rule has an object option:

- `"allow"` allows specified identifiers to have dangling underscores
- `"allowAfterThis": false` (default) disallows dangling underscores in members of the `this` object
- `"allowAfterSuper": false` (default) disallows dangling underscores in members of the `super` object
- `"allowAfterThisConstructor": false` (default) disallows dangling underscores in members of the `this.constructor` object
- `"enforceInMethodNames": false` (default) allows dangling underscores in method names
- `"enforceInClassFields": false` (default) allows dangling underscores in es2022 class fields names
- `"allowInArrayDestructuring": true` (default) allows dangling underscores in variable names assigned by array destructuring
- `"allowInObjectDestructuring": true` (default) allows dangling underscores in variable names assigned by object destructuring
- `"allowFunctionParams": true` (default) allows dangling underscores in function parameter names

### allow

Examples of additional correct code for this rule with the `{ "allow": ["foo_", "_bar"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJmb29fXCIsIFwiX2JhclwiXSB9XSovXG5cbmxldCBmb29fO1xuZm9vLl9iYXIoKTsifQ==)

```
/*eslint no-underscore-dangle: ["error", { "allow": ["foo_", "_bar"] }]*/

let foo_;
foo._bar();
1
2
3
4
```

### allowAfterThis

Examples of correct code for this rule with the `{ "allowAfterThis": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0FmdGVyVGhpc1wiOiB0cnVlIH1dKi9cblxuY29uc3QgYSA9IHRoaXMuZm9vXztcbnRoaXMuX2JhcigpOyJ9)

```
/*eslint no-underscore-dangle: ["error", { "allowAfterThis": true }]*/

const a = this.foo_;
this._bar();
1
2
3
4
```

### allowAfterSuper

Examples of correct code for this rule with the `{ "allowAfterSuper": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0FmdGVyU3VwZXJcIjogdHJ1ZSB9XSovXG5cbmNsYXNzIEZvbyBleHRlbmRzIEJhciB7XG4gIGRvU29tZXRoaW5nKCkge1xuICAgIGNvbnN0IGEgPSBzdXBlci5mb29fO1xuICAgIHN1cGVyLl9iYXIoKTtcbiAgfVxufSJ9)

```
/*eslint no-underscore-dangle: ["error", { "allowAfterSuper": true }]*/

class Foo extends Bar {
  doSomething() {
    const a = super.foo_;
    super._bar();
  }
}
1
2
3
4
5
6
7
8
```

### allowAfterThisConstructor

Examples of correct code for this rule with the `{ "allowAfterThisConstructor": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0FmdGVyVGhpc0NvbnN0cnVjdG9yXCI6IHRydWUgfV0qL1xuXG5jb25zdCBhID0gdGhpcy5jb25zdHJ1Y3Rvci5mb29fO1xudGhpcy5jb25zdHJ1Y3Rvci5fYmFyKCk7In0=)

```
/*eslint no-underscore-dangle: ["error", { "allowAfterThisConstructor": true }]*/

const a = this.constructor.foo_;
this.constructor._bar();
1
2
3
4
```

### enforceInMethodNames

Examples of incorrect code for this rule with the `{ "enforceInMethodNames": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJlbmZvcmNlSW5NZXRob2ROYW1lc1wiOiB0cnVlIH1dKi9cblxuY2xhc3MgRm9vIHtcbiAgX2JhcigpIHt9XG59XG5cbmNsYXNzIEJhciB7XG4gIGJhcl8oKSB7fVxufVxuXG5jb25zdCBvMSA9IHtcbiAgX2JhcigpIHt9XG59O1xuXG5jb25zdCBvMiA9IHtcbiAgYmFyXygpIHt9XG59OyJ9)

```
/*eslint no-underscore-dangle: ["error", { "enforceInMethodNames": true }]*/

class Foo {
  _bar() {}
}

class Bar {
  bar_() {}
}

const o1 = {
  _bar() {}
};

const o2 = {
  bar_() {}
};
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
```

### enforceInClassFields

Examples of incorrect code for this rule with the `{ "enforceInClassFields": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJlbmZvcmNlSW5DbGFzc0ZpZWxkc1wiOiB0cnVlIH1dKi9cblxuY2xhc3MgRm9vIHtcbiAgICBfYmFyO1xufVxuXG5jbGFzcyBCYXIge1xuICAgIF9iYXIgPSAoKSA9PiB7fTtcbn1cblxuY2xhc3MgQmF6IHtcbiAgICBiYXJfO1xufVxuXG5jbGFzcyBRdXgge1xuICAgICNfYmFyO1xufVxuXG5jbGFzcyBGb29CYXIge1xuICAgICNiYXJfO1xufSJ9)

```
/*eslint no-underscore-dangle: ["error", { "enforceInClassFields": true }]*/

class Foo {
    _bar;
}

class Bar {
    _bar = () => {};
}

class Baz {
    bar_;
}

class Qux {
    #_bar;
}

class FooBar {
    #bar_;
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
14
15
16
17
18
19
20
21
```

### allowInArrayDestructuring

Examples of incorrect code for this rule with the `{ "allowInArrayDestructuring": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0luQXJyYXlEZXN0cnVjdHVyaW5nXCI6IGZhbHNlIH1dKi9cblxuY29uc3QgW19mb28sIF9iYXJdID0gbGlzdDtcbmNvbnN0IFtmb29fLCAuLi5fcXV4XSA9IGxpc3Q7XG5jb25zdCBbZm9vLCBbYmFyLCBfYmF6XV0gPSBsaXN0OyJ9)

```
/*eslint no-underscore-dangle: ["error", { "allowInArrayDestructuring": false }]*/

const [_foo, _bar] = list;
const [foo_, ..._qux] = list;
const [foo, [bar, _baz]] = list;
1
2
3
4
5
```

### allowInObjectDestructuring

Examples of incorrect code for this rule with the `{ "allowInObjectDestructuring": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0luT2JqZWN0RGVzdHJ1Y3R1cmluZ1wiOiBmYWxzZSB9XSovXG5cbmNvbnN0IHsgZm9vLCBiYXI6IF9iYXIgfSA9IGNvbGxlY3Rpb247XG5jb25zdCB7IHF1eCwgeHl6LCBfYmF6IH0gPSBjb2xsZWN0aW9uOyJ9)

```
/*eslint no-underscore-dangle: ["error", { "allowInObjectDestructuring": false }]*/

const { foo, bar: _bar } = collection;
const { qux, xyz, _baz } = collection;
1
2
3
4
```

Examples of correct code for this rule with the `{ "allowInObjectDestructuring": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0luT2JqZWN0RGVzdHJ1Y3R1cmluZ1wiOiBmYWxzZSB9XSovXG5cbmNvbnN0IHsgZm9vLCBiYXIsIF9iYXo6IHsgYSwgYiB9IH0gPSBjb2xsZWN0aW9uO1xuY29uc3QgeyBxdXgsIHh5eiwgX2JhejogYmF6IH0gPSBjb2xsZWN0aW9uOyJ9)

```
/*eslint no-underscore-dangle: ["error", { "allowInObjectDestructuring": false }]*/

const { foo, bar, _baz: { a, b } } = collection;
const { qux, xyz, _baz: baz } = collection;
1
2
3
4
```

### allowFunctionParams

Examples of incorrect code for this rule with the `{ "allowFunctionParams": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZXJzY29yZS1kYW5nbGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd0Z1bmN0aW9uUGFyYW1zXCI6IGZhbHNlIH1dKi9cblxuZnVuY3Rpb24gZm9vMSAoX2Jhcikge31cbmZ1bmN0aW9uIGZvbzIgKF9iYXIgPSAwKSB7fVxuZnVuY3Rpb24gZm9vMyAoLi4uX2Jhcikge31cblxuY29uc3QgZm9vNCA9IGZ1bmN0aW9uIG9uQ2xpY2sgKF9iYXIpIHt9XG5jb25zdCBmb281ID0gZnVuY3Rpb24gb25DbGljayAoX2JhciA9IDApIHt9XG5jb25zdCBmb282ID0gZnVuY3Rpb24gb25DbGljayAoLi4uX2Jhcikge31cblxuY29uc3QgZm9vNyA9IChfYmFyKSA9PiB7fTtcbmNvbnN0IGZvbzggPSAoX2JhciA9IDApID0+IHt9O1xuY29uc3QgZm9vOSA9ICguLi5fYmFyKSA9PiB7fTsifQ==)

```
/*eslint no-underscore-dangle: ["error", { "allowFunctionParams": false }]*/

function foo1 (_bar) {}
function foo2 (_bar = 0) {}
function foo3 (..._bar) {}

const foo4 = function onClick (_bar) {}
const foo5 = function onClick (_bar = 0) {}
const foo6 = function onClick (..._bar) {}

const foo7 = (_bar) => {};
const foo8 = (_bar = 0) => {};
const foo9 = (..._bar) => {};
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

## When Not To Use It

If you want to allow dangling underscores in identifiers, then you can safely turn this rule off.

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-underscore-dangle.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-underscore-dangle.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-underscore-dangle.md
                    
                
                )
