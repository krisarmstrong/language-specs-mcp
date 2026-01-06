# no-extra-bind

Disallow unnecessary calls to `.bind()`

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

The `bind()` method is used to create functions with specific `this` values and, optionally, binds arguments to specific values. When used to specify the value of `this`, it’s important that the function actually uses `this` in its function body. For example:

```
const boundGetName = (function getName() {
    return this.name;
}).bind({ name: "ESLint" });

console.log(boundGetName());      // "ESLint"
1
2
3
4
5
```

Copy code to clipboard

This code is an example of a good use of `bind()` for setting the value of `this`.

Sometimes during the course of code maintenance, the `this` value is removed from the function body. In that case, you can end up with a call to `bind()` that doesn’t accomplish anything:

```
// useless bind
const boundGetName = (function getName() {
    return "ESLint";
}).bind({ name: "ESLint" });

console.log(boundGetName());      // "ESLint"
1
2
3
4
5
6
```

Copy code to clipboard

In this code, the reference to `this` has been removed but `bind()` is still used. In this case, the `bind()` is unnecessary overhead (and a performance hit) and can be safely removed.

## Rule Details

This rule is aimed at avoiding the unnecessary use of `bind()` and as such will warn whenever an immediately-invoked function expression (IIFE) is using `bind()` and doesn’t have an appropriate `this` value. This rule won’t flag usage of `bind()` that includes function argument binding.

Note: Arrow functions can never have their `this` value set using `bind()`. This rule flags all uses of `bind()` with arrow functions as a problem

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtYmluZDogXCJlcnJvclwiKi9cblxuY29uc3QgeCA9IGZ1bmN0aW9uICgpIHtcbiAgICBmb28oKTtcbn0uYmluZChiYXIpO1xuXG5jb25zdCB5ID0gKCgpID0+IHtcbiAgICBmb28oKTtcbn0pLmJpbmQoYmFyKTtcblxuY29uc3QgeiA9ICgoKSA9PiB7XG4gICAgdGhpcy5mb28oKTtcbn0pLmJpbmQoYmFyKTtcblxuY29uc3QgYSA9IGZ1bmN0aW9uICgpIHtcbiAgICAoZnVuY3Rpb24gKCkge1xuICAgICAgdGhpcy5mb28oKTtcbiAgICB9KCkpO1xufS5iaW5kKGJhcik7XG5cbmNvbnN0IGIgPSBmdW5jdGlvbiAoKSB7XG4gICAgZnVuY3Rpb24gZm9vKCkge1xuICAgICAgdGhpcy5iYXIoKTtcbiAgICB9XG59LmJpbmQoYmF6KTsifQ==)

```
/*eslint no-extra-bind: "error"*/

const x = function () {
    foo();
}.bind(bar);

const y = (() => {
    foo();
}).bind(bar);

const z = (() => {
    this.foo();
}).bind(bar);

const a = function () {
    (function () {
      this.foo();
    }());
}.bind(bar);

const b = function () {
    function foo() {
      this.bar();
    }
}.bind(baz);
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
22
23
24
25
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtYmluZDogXCJlcnJvclwiKi9cblxuY29uc3QgeCA9IGZ1bmN0aW9uICgpIHtcbiAgICB0aGlzLmZvbygpO1xufS5iaW5kKGJhcik7XG5cbmNvbnN0IHkgPSBmdW5jdGlvbiAoYSkge1xuICAgIHJldHVybiBhICsgMTtcbn0uYmluZChmb28sIGJhcik7In0=)

```
/*eslint no-extra-bind: "error"*/

const x = function () {
    this.foo();
}.bind(bar);

const y = function (a) {
    return a + 1;
}.bind(foo, bar);
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

If you are not concerned about unnecessary calls to `bind()`, you can safely disable this rule.

## Version

This rule was introduced in ESLint v0.8.0.

## Further Reading

[Function.prototype.bind() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
 developer.mozilla.org[Understanding JavaScript Bind () — Smashing Magazine](https://www.smashingmagazine.com/2014/01/understanding-javascript-function-prototype-bind/)
 www.smashingmagazine.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-extra-bind.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-extra-bind.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-extra-bind.md
                    
                
                )
