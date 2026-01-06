# func-name-matching

Require function names to match the name of the variable or property to which they are assigned

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [considerPropertyDescriptor](#considerpropertydescriptor)
  2. [includeCommonJSModuleExports](#includecommonjsmoduleexports)

3. [When Not To Use It](#when-not-to-use-it)
4. [Compatibility](#compatibility)
5. [Version](#version)
6. [Resources](#resources)

## Rule Details

This rule requires function names to match the name of the variable or property to which they are assigned. The rule will ignore property assignments where the property name is a literal that is not a valid identifier in the ECMAScript version specified in your configuration (default ES5).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBcImVycm9yXCIqL1xuXG5sZXQgZm9vID0gZnVuY3Rpb24gYmFyKCkge307XG5mb28gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbmNvbnN0IG9iaiA9IHtmb286IGZ1bmN0aW9uIGJhcigpIHt9fTtcbm9iai5mb28gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbm9ialsnZm9vJ10gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbih7Wydmb28nXTogZnVuY3Rpb24gYmFyKCkge319KTtcblxuY2xhc3MgQyB7XG4gICAgZm9vID0gZnVuY3Rpb24gYmFyKCkge307XG59In0=)

```
/*eslint func-name-matching: "error"*/

let foo = function bar() {};
foo = function bar() {};
const obj = {foo: function bar() {}};
obj.foo = function bar() {};
obj['foo'] = function bar() {};
({['foo']: function bar() {}});

class C {
    foo = function bar() {};
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
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdICovXG5cbmxldCBmb28gPSBmdW5jdGlvbiBmb28oKSB7fTtcbmZvbyA9IGZ1bmN0aW9uIGZvbygpIHt9O1xuY29uc3Qgb2JqID0ge2ZvbzogZnVuY3Rpb24gZm9vKCkge319O1xub2JqLmZvbyA9IGZ1bmN0aW9uIGZvbygpIHt9O1xub2JqWydmb28nXSA9IGZ1bmN0aW9uIGZvbygpIHt9O1xuKHtbJ2ZvbyddOiBmdW5jdGlvbiBmb28oKSB7fX0pO1xuXG5jbGFzcyBDIHtcbiAgICBmb28gPSBmdW5jdGlvbiBmb28oKSB7fTtcbn0ifQ==)

```
/*eslint func-name-matching: ["error", "never"] */

let foo = function foo() {};
foo = function foo() {};
const obj = {foo: function foo() {}};
obj.foo = function foo() {};
obj['foo'] = function foo() {};
({['foo']: function foo() {}});

class C {
    foo = function foo() {};
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBcImVycm9yXCIqL1xuLy8gZXF1aXZhbGVudCB0byAvKmVzbGludCBmdW5jLW5hbWUtbWF0Y2hpbmc6IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxuY29uc3QgZm9vID0gZnVuY3Rpb24gZm9vKCkge307XG5jb25zdCBmb28xID0gZnVuY3Rpb24oKSB7fTtcbmNvbnN0IGZvbzIgPSAoKSA9PiB7fTtcbmZvbyA9IGZ1bmN0aW9uIGZvbygpIHt9O1xuXG5jb25zdCBvYmogPSB7Zm9vOiBmdW5jdGlvbiBmb28oKSB7fX07XG5vYmouZm9vID0gZnVuY3Rpb24gZm9vKCkge307XG5vYmpbJ2ZvbyddID0gZnVuY3Rpb24gZm9vKCkge307XG5vYmpbJ2Zvby8vYmFyJ10gPSBmdW5jdGlvbiBmb28oKSB7fTtcbm9ialtmb29dID0gZnVuY3Rpb24gYmFyKCkge307XG5cbmNvbnN0IG9iajEgPSB7W2Zvb106IGZ1bmN0aW9uIGJhcigpIHt9fTtcbmNvbnN0IG9iajIgPSB7J2Zvby8vYmFyJzogZnVuY3Rpb24gZm9vKCkge319O1xuY29uc3Qgb2JqMyA9IHtmb286IGZ1bmN0aW9uKCkge319O1xuXG5vYmpbJ3gnICsgMl0gPSBmdW5jdGlvbiBiYXIoKXt9O1xuY29uc3QgWyBiYXIgXSA9IFsgZnVuY3Rpb24gYmFyKCl7fSBdO1xuKHtbZm9vXTogZnVuY3Rpb24gYmFyKCkge319KVxuXG5jbGFzcyBDIHtcbiAgICBmb28gPSBmdW5jdGlvbiBmb28oKSB7fTtcbiAgICBiYXogPSBmdW5jdGlvbigpIHt9O1xufVxuXG4vLyBwcml2YXRlIG5hbWVzIGFyZSBpZ25vcmVkXG5jbGFzcyBEIHtcbiAgICAjZm9vID0gZnVuY3Rpb24gZm9vKCkge307XG4gICAgI2JhciA9IGZ1bmN0aW9uIGZvbygpIHt9O1xuICAgIGJheigpIHtcbiAgICAgICAgdGhpcy4jZm9vID0gZnVuY3Rpb24gZm9vKCkge307XG4gICAgICAgIHRoaXMuI2ZvbyA9IGZ1bmN0aW9uIGJhcigpIHt9O1xuICAgIH1cbn1cblxubW9kdWxlLmV4cG9ydHMgPSBmdW5jdGlvbiBmb28obmFtZSkge307XG5tb2R1bGVbJ2V4cG9ydHMnXSA9IGZ1bmN0aW9uIGZvbyhuYW1lKSB7fTsifQ==)

```
/*eslint func-name-matching: "error"*/
// equivalent to /*eslint func-name-matching: ["error", "always"]*/

const foo = function foo() {};
const foo1 = function() {};
const foo2 = () => {};
foo = function foo() {};

const obj = {foo: function foo() {}};
obj.foo = function foo() {};
obj['foo'] = function foo() {};
obj['foo//bar'] = function foo() {};
obj[foo] = function bar() {};

const obj1 = {[foo]: function bar() {}};
const obj2 = {'foo//bar': function foo() {}};
const obj3 = {foo: function() {}};

obj['x' + 2] = function bar(){};
const [ bar ] = [ function bar(){} ];
({[foo]: function bar() {}})

class C {
    foo = function foo() {};
    baz = function() {};
}

// private names are ignored
class D {
    #foo = function foo() {};
    #bar = function foo() {};
    baz() {
        this.#foo = function foo() {};
        this.#foo = function bar() {};
    }
}

module.exports = function foo(name) {};
module['exports'] = function foo(name) {};
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
26
27
28
29
30
31
32
33
34
35
36
37
38
39
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdICovXG5cbmxldCBmb28gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbmNvbnN0IGZvbzEgPSBmdW5jdGlvbigpIHt9O1xuY29uc3QgZm9vMiA9ICgpID0+IHt9O1xuZm9vID0gZnVuY3Rpb24gYmFyKCkge307XG5cbmNvbnN0IG9iaiA9IHtmb286IGZ1bmN0aW9uIGJhcigpIHt9fTtcbm9iai5mb28gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbm9ialsnZm9vJ10gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbm9ialsnZm9vLy9iYXInXSA9IGZ1bmN0aW9uIGZvbygpIHt9O1xub2JqW2Zvb10gPSBmdW5jdGlvbiBmb28oKSB7fTtcblxuY29uc3Qgb2JqMSA9IHtmb286IGZ1bmN0aW9uIGJhcigpIHt9fTtcbmNvbnN0IG9iajIgPSB7W2Zvb106IGZ1bmN0aW9uIGZvbygpIHt9fTtcbmNvbnN0IG9iajMgPSB7J2Zvby8vYmFyJzogZnVuY3Rpb24gZm9vKCkge319O1xuY29uc3Qgb2JqNCA9IHtmb286IGZ1bmN0aW9uKCkge319O1xuXG5vYmpbJ3gnICsgMl0gPSBmdW5jdGlvbiBiYXIoKXt9O1xuY29uc3QgWyBiYXIgXSA9IFsgZnVuY3Rpb24gYmFyKCl7fSBdO1xuKHtbZm9vXTogZnVuY3Rpb24gYmFyKCkge319KVxuXG5jbGFzcyBDIHtcbiAgICBmb28gPSBmdW5jdGlvbiBiYXIoKSB7fTtcbiAgICBiYXogPSBmdW5jdGlvbigpIHt9O1xufVxuXG4vLyBwcml2YXRlIG5hbWVzIGFyZSBpZ25vcmVkXG5jbGFzcyBEIHtcbiAgICAjZm9vID0gZnVuY3Rpb24gZm9vKCkge307XG4gICAgI2JhciA9IGZ1bmN0aW9uIGZvbygpIHt9O1xuICAgIGJheigpIHtcbiAgICAgICAgdGhpcy4jZm9vID0gZnVuY3Rpb24gZm9vKCkge307XG4gICAgICAgIHRoaXMuI2ZvbyA9IGZ1bmN0aW9uIGJhcigpIHt9O1xuICAgIH1cbn1cblxubW9kdWxlLmV4cG9ydHMgPSBmdW5jdGlvbiBmb28obmFtZSkge307XG5tb2R1bGVbJ2V4cG9ydHMnXSA9IGZ1bmN0aW9uIGZvbyhuYW1lKSB7fTsifQ==)

```
/*eslint func-name-matching: ["error", "never"] */

let foo = function bar() {};
const foo1 = function() {};
const foo2 = () => {};
foo = function bar() {};

const obj = {foo: function bar() {}};
obj.foo = function bar() {};
obj['foo'] = function bar() {};
obj['foo//bar'] = function foo() {};
obj[foo] = function foo() {};

const obj1 = {foo: function bar() {}};
const obj2 = {[foo]: function foo() {}};
const obj3 = {'foo//bar': function foo() {}};
const obj4 = {foo: function() {}};

obj['x' + 2] = function bar(){};
const [ bar ] = [ function bar(){} ];
({[foo]: function bar() {}})

class C {
    foo = function bar() {};
    baz = function() {};
}

// private names are ignored
class D {
    #foo = function foo() {};
    #bar = function foo() {};
    baz() {
        this.#foo = function foo() {};
        this.#foo = function bar() {};
    }
}

module.exports = function foo(name) {};
module['exports'] = function foo(name) {};
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
26
27
28
29
30
31
32
33
34
35
36
37
38
39
```

## Options

This rule takes an optional string of `"always"` or `"never"` (when omitted, it defaults to `"always"`), and an optional options object with two properties `considerPropertyDescriptor` and `includeCommonJSModuleExports`.

### considerPropertyDescriptor

A boolean value that defaults to `false`. If `considerPropertyDescriptor` is set to true, the check will take into account the use of `Object.create`, `Object.defineProperty`, `Object.defineProperties`, and `Reflect.defineProperty`.

Examples of correct code for the `{ considerPropertyDescriptor: true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBbXCJlcnJvclwiLCB7IFwiY29uc2lkZXJQcm9wZXJ0eURlc2NyaXB0b3JcIjogdHJ1ZSB9XSovXG4vLyBlcXVpdmFsZW50IHRvIC8qZXNsaW50IGZ1bmMtbmFtZS1tYXRjaGluZzogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImNvbnNpZGVyUHJvcGVydHlEZXNjcmlwdG9yXCI6IHRydWUgfV0qL1xuY29uc3Qgb2JqID0ge307XG5PYmplY3QuY3JlYXRlKG9iaiwge2Zvbzp7dmFsdWU6IGZ1bmN0aW9uIGZvbygpIHt9fX0pO1xuT2JqZWN0LmRlZmluZVByb3BlcnR5KG9iaiwgJ2JhcicsIHt2YWx1ZTogZnVuY3Rpb24gYmFyKCkge319KTtcbk9iamVjdC5kZWZpbmVQcm9wZXJ0aWVzKG9iaiwge2Jhejp7dmFsdWU6IGZ1bmN0aW9uIGJheigpIHt9IH19KTtcblJlZmxlY3QuZGVmaW5lUHJvcGVydHkob2JqLCAnZm9vJywge3ZhbHVlOiBmdW5jdGlvbiBmb28oKSB7fX0pOyJ9)

```
/*eslint func-name-matching: ["error", { "considerPropertyDescriptor": true }]*/
// equivalent to /*eslint func-name-matching: ["error", "always", { "considerPropertyDescriptor": true }]*/
const obj = {};
Object.create(obj, {foo:{value: function foo() {}}});
Object.defineProperty(obj, 'bar', {value: function bar() {}});
Object.defineProperties(obj, {baz:{value: function baz() {} }});
Reflect.defineProperty(obj, 'foo', {value: function foo() {}});
1
2
3
4
5
6
7
```

Examples of incorrect code for the `{ considerPropertyDescriptor: true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBbXCJlcnJvclwiLCB7IFwiY29uc2lkZXJQcm9wZXJ0eURlc2NyaXB0b3JcIjogdHJ1ZSB9XSovXG4vLyBlcXVpdmFsZW50IHRvIC8qZXNsaW50IGZ1bmMtbmFtZS1tYXRjaGluZzogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImNvbnNpZGVyUHJvcGVydHlEZXNjcmlwdG9yXCI6IHRydWUgfV0qL1xuY29uc3Qgb2JqID0ge307XG5PYmplY3QuY3JlYXRlKG9iaiwge2Zvbzp7dmFsdWU6IGZ1bmN0aW9uIGJhcigpIHt9fX0pO1xuT2JqZWN0LmRlZmluZVByb3BlcnR5KG9iaiwgJ2JhcicsIHt2YWx1ZTogZnVuY3Rpb24gYmF6KCkge319KTtcbk9iamVjdC5kZWZpbmVQcm9wZXJ0aWVzKG9iaiwge2Jhejp7dmFsdWU6IGZ1bmN0aW9uIGZvbygpIHt9IH19KTtcblJlZmxlY3QuZGVmaW5lUHJvcGVydHkob2JqLCAnZm9vJywge3ZhbHVlOiBmdW5jdGlvbiB2YWx1ZSgpIHt9fSk7In0=)

```
/*eslint func-name-matching: ["error", { "considerPropertyDescriptor": true }]*/
// equivalent to /*eslint func-name-matching: ["error", "always", { "considerPropertyDescriptor": true }]*/
const obj = {};
Object.create(obj, {foo:{value: function bar() {}}});
Object.defineProperty(obj, 'bar', {value: function baz() {}});
Object.defineProperties(obj, {baz:{value: function foo() {} }});
Reflect.defineProperty(obj, 'foo', {value: function value() {}});
1
2
3
4
5
6
7
```

### includeCommonJSModuleExports

A boolean value that defaults to `false`. If `includeCommonJSModuleExports` is set to true, `module.exports` and `module["exports"]` will be checked by this rule.

Examples of incorrect code for the `{ includeCommonJSModuleExports: true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBbXCJlcnJvclwiLCB7IFwiaW5jbHVkZUNvbW1vbkpTTW9kdWxlRXhwb3J0c1wiOiB0cnVlIH1dKi9cbi8vIGVxdWl2YWxlbnQgdG8gLyplc2xpbnQgZnVuYy1uYW1lLW1hdGNoaW5nOiBbXCJlcnJvclwiLCBcImFsd2F5c1wiLCB7IFwiaW5jbHVkZUNvbW1vbkpTTW9kdWxlRXhwb3J0c1wiOiB0cnVlIH1dKi9cblxubW9kdWxlLmV4cG9ydHMgPSBmdW5jdGlvbiBmb28obmFtZSkge307XG5tb2R1bGVbJ2V4cG9ydHMnXSA9IGZ1bmN0aW9uIGZvbyhuYW1lKSB7fTsifQ==)

```
/*eslint func-name-matching: ["error", { "includeCommonJSModuleExports": true }]*/
// equivalent to /*eslint func-name-matching: ["error", "always", { "includeCommonJSModuleExports": true }]*/

module.exports = function foo(name) {};
module['exports'] = function foo(name) {};
1
2
3
4
5
```

## When Not To Use It

Do not use this rule if you want to allow named functions to have different names from the variable or property to which they are assigned.

## Compatibility

- JSCS: [requireMatchingFunctionName](https://jscs-dev.github.io/rule/requireMatchingFunctionName)

## Version

This rule was introduced in ESLint v3.8.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/func-name-matching.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/func-name-matching.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/func-name-matching.md
                    
                
                )
