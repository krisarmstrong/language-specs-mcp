# id-length

Enforce minimum and maximum identifier lengths

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [min](#min)
  2. [max](#max)
  3. [properties](#properties)
  4. [exceptions](#exceptions)
  5. [exceptionPatterns](#exceptionpatterns)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Very short identifier names like `e`, `x`, `_t` or very long ones like `hashGeneratorResultOutputContainerObject` can make code harder to read and potentially less maintainable. To prevent this, one may enforce a minimum and/or maximum identifier length.

```
const x = 5; // too short; difficult to understand its purpose without context
1
```

Copy code to clipboard

## Rule Details

This rule enforces a minimum and/or maximum identifier length convention.

This rule counts [graphemes](https://unicode.org/reports/tr29/#Default_Grapheme_Cluster_Table) instead of using [String length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length).

## Options

Examples of incorrect code for this rule with the default options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBcImVycm9yXCIqLyAgICAgLy8gZGVmYXVsdCBpcyBtaW5pbXVtIDItY2hhcnMgKHsgXCJtaW5cIjogMiB9KVxuXG5jb25zdCB4ID0gNTtcbm9iai5lID0gZG9jdW1lbnQuYm9keTtcbmNvbnN0IGZvbyA9IGZ1bmN0aW9uIChlKSB7IH07XG50cnkge1xuICAgIGRhbmdlcm91c1N0dWZmKCk7XG59IGNhdGNoIChlKSB7XG4gICAgLy8gaWdub3JlIGFzIG1hbnkgZG9cbn1cbmNvbnN0IG15T2JqID0geyBhOiAxIH07XG4oYSkgPT4geyBhICogYSB9O1xuY2xhc3MgeSB7IH1cbmNsYXNzIEZvbyB7IHgoKSB7fSB9XG5jbGFzcyBCYXIgeyAjeCgpIHt9IH1cbmNsYXNzIEJheiB7IHggPSAxIH1cbmNsYXNzIFF1eCB7ICN4ID0gMSB9XG5mdW5jdGlvbiBiYXIoLi4ueCkgeyB9XG5mdW5jdGlvbiBiYXooW3hdKSB7IH1cbmNvbnN0IFt6XSA9IGFycjtcbmNvbnN0IHsgcHJvcDogW2ldfSA9IHt9O1xuZnVuY3Rpb24gcXV4KHt4fSkgeyB9XG5jb25zdCB7IGogfSA9IHt9O1xuY29uc3QgeyBwcm9wOiBhfSA9IHt9O1xuKHsgcHJvcDogb2JqLnggfSA9IHt9KTsifQ==)

```
/*eslint id-length: "error"*/     // default is minimum 2-chars ({ "min": 2 })

const x = 5;
obj.e = document.body;
const foo = function (e) { };
try {
    dangerousStuff();
} catch (e) {
    // ignore as many do
}
const myObj = { a: 1 };
(a) => { a * a };
class y { }
class Foo { x() {} }
class Bar { #x() {} }
class Baz { x = 1 }
class Qux { #x = 1 }
function bar(...x) { }
function baz([x]) { }
const [z] = arr;
const { prop: [i]} = {};
function qux({x}) { }
const { j } = {};
const { prop: a} = {};
({ prop: obj.x } = {});
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

Examples of correct code for this rule with the default options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBcImVycm9yXCIqLyAgICAgLy8gZGVmYXVsdCBpcyBtaW5pbXVtIDItY2hhcnMgKHsgXCJtaW5cIjogMiB9KVxuXG5jb25zdCBudW0gPSA1O1xuZnVuY3Rpb24gX2YoKSB7IHJldHVybiA0MjsgfVxuZnVuY3Rpb24gX2Z1bmMoKSB7IHJldHVybiA0MjsgfVxub2JqLmVsID0gZG9jdW1lbnQuYm9keTtcbmNvbnN0IGZvbyA9IGZ1bmN0aW9uIChldnQpIHsgLyogZG8gc3R1ZmYgKi8gfTtcbnRyeSB7XG4gICAgZGFuZ2Vyb3VzU3R1ZmYoKTtcbn0gY2F0Y2ggKGVycm9yKSB7XG4gICAgLy8gaWdub3JlIGFzIG1hbnkgZG9cbn1cbmNvbnN0IG15T2JqID0geyBhcHBsZTogMSB9O1xuKG51bSkgPT4geyBudW0gKiBudW0gfTtcbmZ1bmN0aW9uIGJhcihudW0gPSAwKSB7IH1cbmNsYXNzIE15Q2xhc3MgeyB9XG5jbGFzcyBGb28geyBtZXRob2QoKSB7fSB9XG5jbGFzcyBCYXIgeyAjbWV0aG9kKCkge30gfVxuY2xhc3MgQmF6IHsgZmllbGQgPSAxIH1cbmNsYXNzIFF1eCB7ICNmaWVsZCA9IDEgfVxuZnVuY3Rpb24gYmF6KC4uLmFyZ3MpIHsgfVxuZnVuY3Rpb24gcXV4KFtsb25nTmFtZV0pIHsgfVxuY29uc3QgeyBwcm9wIH0gPSB7fTtcbmNvbnN0IHsgcHJvcDogW25hbWVdIH0gPSB7fTtcbmNvbnN0IFtsb25nTmFtZV0gPSBhcnI7XG5mdW5jdGlvbiBmb29iYXIoeyBwcm9wIH0pIHsgfVxuZnVuY3Rpb24gZm9vYmF6KHsgYTogcHJvcCB9KSB7IH1cbmNvbnN0IHsgYTogcHJvcGVydHkgfSA9IHt9O1xuKHsgcHJvcDogb2JqLmxvbmdOYW1lIH0gPSB7fSk7XG5jb25zdCBkYXRhID0geyBcInhcIjogMSB9OyAgLy8gZXhjdXNlZCBiZWNhdXNlIG9mIHF1b3Rlc1xuZGF0YVtcInlcIl0gPSAzOyAgLy8gZXhjdXNlZCBiZWNhdXNlIG9mIGNhbGN1bGF0ZWQgcHJvcGVydHkgYWNjZXNzIn0=)

```
/*eslint id-length: "error"*/     // default is minimum 2-chars ({ "min": 2 })

const num = 5;
function _f() { return 42; }
function _func() { return 42; }
obj.el = document.body;
const foo = function (evt) { /* do stuff */ };
try {
    dangerousStuff();
} catch (error) {
    // ignore as many do
}
const myObj = { apple: 1 };
(num) => { num * num };
function bar(num = 0) { }
class MyClass { }
class Foo { method() {} }
class Bar { #method() {} }
class Baz { field = 1 }
class Qux { #field = 1 }
function baz(...args) { }
function qux([longName]) { }
const { prop } = {};
const { prop: [name] } = {};
const [longName] = arr;
function foobar({ prop }) { }
function foobaz({ a: prop }) { }
const { a: property } = {};
({ prop: obj.longName } = {});
const data = { "x": 1 };  // excused because of quotes
data["y"] = 3;  // excused because of calculated property access
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
```

This rule has an object option:

- `"min"` (default: `2`) enforces a minimum identifier length
- `"max"` (default: `Infinity`) enforces a maximum identifier length
- `"properties": always` (default) enforces identifier length convention for property names
- `"properties": never` ignores identifier length convention for property names
- `"exceptions"` allows an array of specified identifier names
- `"exceptionPatterns"` array of strings representing regular expression patterns, allows identifiers that match any of the patterns.

### min

Examples of incorrect code for this rule with the `{ "min": 4 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwibWluXCI6IDQgfV0qL1xuXG5jb25zdCB2YWwgPSA1O1xub2JqLmUgPSBkb2N1bWVudC5ib2R5O1xuZnVuY3Rpb24gZm9vIChlKSB7IH07XG50cnkge1xuICAgIGRhbmdlcm91c1N0dWZmKCk7XG59IGNhdGNoIChlKSB7XG4gICAgLy8gaWdub3JlIGFzIG1hbnkgZG9cbn1cbmNvbnN0IG15T2JqID0geyBhOiAxIH07XG4odmFsKSA9PiB7IHZhbCAqIHZhbCB9O1xuY2xhc3MgeSB7IH1cbmNsYXNzIEZvbyB7IHgoKSB7fSB9XG5mdW5jdGlvbiBiYXIoLi4ueCkgeyB9XG5jb25zdCB7IHggfSA9IHt9O1xuY29uc3QgeyBwcm9wOiBhfSA9IHt9O1xuY29uc3QgW2ldID0gYXJyO1xuY29uc3QgeyBwcm9wOiBbbnVtXX0gPSB7fTtcbih7IHByb3A6IG9iai54IH0gPSB7fSk7In0=)

```
/*eslint id-length: ["error", { "min": 4 }]*/

const val = 5;
obj.e = document.body;
function foo (e) { };
try {
    dangerousStuff();
} catch (e) {
    // ignore as many do
}
const myObj = { a: 1 };
(val) => { val * val };
class y { }
class Foo { x() {} }
function bar(...x) { }
const { x } = {};
const { prop: a} = {};
const [i] = arr;
const { prop: [num]} = {};
({ prop: obj.x } = {});
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
```

Examples of correct code for this rule with the `{ "min": 4 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwibWluXCI6IDQgfV0qL1xuXG5jb25zdCB2YWx1ZSA9IDU7XG5mdW5jdGlvbiBmdW5jKCkgeyByZXR1cm4gNDI7IH1cbm9iamVjdC5lbGVtZW50ID0gZG9jdW1lbnQuYm9keTtcbmNvbnN0IGZvb2JhciA9IGZ1bmN0aW9uIChldmVudCkgeyAvKiBkbyBzdHVmZiAqLyB9O1xudHJ5IHtcbiAgICBkYW5nZXJvdXNTdHVmZigpO1xufSBjYXRjaCAoZXJyb3IpIHtcbiAgICAvLyBpZ25vcmUgYXMgbWFueSBkb1xufVxuY29uc3QgbXlPYmogPSB7IGFwcGxlOiAxIH07XG4odmFsdWUpID0+IHsgdmFsdWUgKiB2YWx1ZSB9O1xuZnVuY3Rpb24gZm9vYmF6KHZhbHVlID0gMCkgeyB9XG5jbGFzcyBNeUNsYXNzIHsgfVxuY2xhc3MgRm9vYmFyIHsgbWV0aG9kKCkge30gfVxuZnVuY3Rpb24gYmFyYmF6KC4uLmFyZ3MpIHsgfVxuY29uc3QgeyBwcm9wIH0gPSB7fTtcbmNvbnN0IFtsb25nTmFtZV0gPSBmb287XG5jb25zdCB7IGE6IFtuYW1lXSB9ID0ge307XG5jb25zdCB7IGE6IHJlY29yZCB9ID0ge307XG4oeyBwcm9wOiBvYmplY3QubmFtZSB9ID0ge30pO1xuY29uc3QgZGF0YSA9IHsgXCJ4XCI6IDEgfTsgIC8vIGV4Y3VzZWQgYmVjYXVzZSBvZiBxdW90ZXNcbmRhdGFbXCJ5XCJdID0gMzsgIC8vIGV4Y3VzZWQgYmVjYXVzZSBvZiBjYWxjdWxhdGVkIHByb3BlcnR5IGFjY2VzcyJ9)

```
/*eslint id-length: ["error", { "min": 4 }]*/

const value = 5;
function func() { return 42; }
object.element = document.body;
const foobar = function (event) { /* do stuff */ };
try {
    dangerousStuff();
} catch (error) {
    // ignore as many do
}
const myObj = { apple: 1 };
(value) => { value * value };
function foobaz(value = 0) { }
class MyClass { }
class Foobar { method() {} }
function barbaz(...args) { }
const { prop } = {};
const [longName] = foo;
const { a: [name] } = {};
const { a: record } = {};
({ prop: object.name } = {});
const data = { "x": 1 };  // excused because of quotes
data["y"] = 3;  // excused because of calculated property access
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
```

### max

Examples of incorrect code for this rule with the `{ "max": 10 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwibWF4XCI6IDEwIH1dKi9cblxuY29uc3QgcmVhbGx5TG9uZ1Zhck5hbWUgPSA1O1xuZnVuY3Rpb24gcmVhbGx5TG9uZ0Z1bmNOYW1lKCkgeyByZXR1cm4gNDI7IH1cbm9iai5yZWFsbHlMb25nUHJvcE5hbWUgPSBkb2N1bWVudC5ib2R5O1xuY29uc3QgZm9vID0gZnVuY3Rpb24gKHJlYWxseUxvbmdBcmdOYW1lKSB7IC8qIGRvIHN0dWZmICovIH07XG50cnkge1xuICAgIGRhbmdlcm91c1N0dWZmKCk7XG59IGNhdGNoIChyZWFsbHlMb25nRXJyb3JOYW1lKSB7XG4gICAgLy8gaWdub3JlIGFzIG1hbnkgZG9cbn1cbihyZWFsbHlMb25nQXJnTmFtZSkgPT4geyByZXR1cm4gIXJlYWxseUxvbmdBcmdOYW1lOyB9O1xuY29uc3QgW3JlYWxseUxvbmdGaXJzdEVsZW1lbnROYW1lXSA9IGFycjsifQ==)

```
/*eslint id-length: ["error", { "max": 10 }]*/

const reallyLongVarName = 5;
function reallyLongFuncName() { return 42; }
obj.reallyLongPropName = document.body;
const foo = function (reallyLongArgName) { /* do stuff */ };
try {
    dangerousStuff();
} catch (reallyLongErrorName) {
    // ignore as many do
}
(reallyLongArgName) => { return !reallyLongArgName; };
const [reallyLongFirstElementName] = arr;
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

Examples of correct code for this rule with the `{ "max": 10 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwibWF4XCI6IDEwIH1dKi9cblxuY29uc3QgdmFyTmFtZSA9IDU7XG5mdW5jdGlvbiBmdW5jTmFtZSgpIHsgcmV0dXJuIDQyOyB9XG5vYmoucHJvcE5hbWUgPSBkb2N1bWVudC5ib2R5O1xuY29uc3QgZm9vID0gZnVuY3Rpb24gKGFyZykgeyAvKiBkbyBzdHVmZiAqLyB9O1xudHJ5IHtcbiAgICBkYW5nZXJvdXNTdHVmZigpO1xufSBjYXRjaCAoZXJyb3IpIHtcbiAgICAvLyBpZ25vcmUgYXMgbWFueSBkb1xufVxuKGFyZykgPT4geyByZXR1cm4gIWFyZzsgfTtcbmNvbnN0IFtmaXJzdF0gPSBhcnI7In0=)

```
/*eslint id-length: ["error", { "max": 10 }]*/

const varName = 5;
function funcName() { return 42; }
obj.propName = document.body;
const foo = function (arg) { /* do stuff */ };
try {
    dangerousStuff();
} catch (error) {
    // ignore as many do
}
(arg) => { return !arg; };
const [first] = arr;
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

### properties

Examples of correct code for this rule with the `{ "properties": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwicHJvcGVydGllc1wiOiBcIm5ldmVyXCIgfV0qL1xuXG5jb25zdCBteU9iaiA9IHsgYTogMSB9O1xuKHsgYTogb2JqLngueS56IH0gPSB7fSk7XG4oeyBwcm9wOiBvYmouaSB9ID0ge30pOyJ9)

```
/*eslint id-length: ["error", { "properties": "never" }]*/

const myObj = { a: 1 };
({ a: obj.x.y.z } = {});
({ prop: obj.i } = {});
1
2
3
4
5
```

### exceptions

Examples of additional correct code for this rule with the `{ "exceptions": ["x", "y", "z", "ζ"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwiZXhjZXB0aW9uc1wiOiBbXCJ4XCIsIFwieVwiLCBcInpcIiwgXCLOtlwiLCBcImlcIl0gfV0qL1xuXG5jb25zdCB4ID0gNTtcbmZ1bmN0aW9uIHkoKSB7IHJldHVybiA0MjsgfVxub2JqLnggPSBkb2N1bWVudC5ib2R5O1xuY29uc3QgZm9vID0gZnVuY3Rpb24gKHgpIHsgLyogZG8gc3R1ZmYgKi8gfTtcbnRyeSB7XG4gICAgZGFuZ2Vyb3VzU3R1ZmYoKTtcbn0gY2F0Y2ggKHgpIHtcbiAgICAvLyBpZ25vcmUgYXMgbWFueSBkb1xufVxuKHgpID0+IHsgcmV0dXJuIHggKiB4OyB9O1xuY29uc3QgW2ldID0gYXJyO1xuY29uc3QgeyB6IH0gPSBmb287XG5jb25zdCB7IGE6IM62IH0gPSBmb287In0=)

```
/*eslint id-length: ["error", { "exceptions": ["x", "y", "z", "ζ", "i"] }]*/

const x = 5;
function y() { return 42; }
obj.x = document.body;
const foo = function (x) { /* do stuff */ };
try {
    dangerousStuff();
} catch (x) {
    // ignore as many do
}
(x) => { return x * x; };
const [i] = arr;
const { z } = foo;
const { a: ζ } = foo;
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

### exceptionPatterns

Examples of additional correct code for this rule with the `{ "exceptionPatterns": ["E|S", "[x-z]"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbGVuZ3RoOiBbXCJlcnJvclwiLCB7IFwiZXhjZXB0aW9uUGF0dGVybnNcIjogW1wiRXxTfFhcIiwgXCJbeC16XVwiXSB9XSovXG5cbmNvbnN0IEUgPSA1O1xuZnVuY3Rpb24gUygpIHsgcmV0dXJuIDQyOyB9XG5vYmoueCA9IGRvY3VtZW50LmJvZHk7XG5jb25zdCBmb28gPSBmdW5jdGlvbiAoeCkgeyAvKiBkbyBzdHVmZiAqLyB9O1xudHJ5IHtcbiAgICBkYW5nZXJvdXNTdHVmZigpO1xufSBjYXRjaCAoeCkge1xuICAgIC8vIGlnbm9yZSBhcyBtYW55IGRvXG59XG4oeSkgPT4ge3JldHVybiAgeSAqIHl9O1xuY29uc3QgW1hdID0gYXJyO1xuY29uc3QgeyB5IH0gPSBmb287XG5jb25zdCB7IGE6IHogfSA9IGZvbzsifQ==)

```
/*eslint id-length: ["error", { "exceptionPatterns": ["E|S|X", "[x-z]"] }]*/

const E = 5;
function S() { return 42; }
obj.x = document.body;
const foo = function (x) { /* do stuff */ };
try {
    dangerousStuff();
} catch (x) {
    // ignore as many do
}
(y) => {return  y * y};
const [X] = arr;
const { y } = foo;
const { a: z } = foo;
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

## Related Rules

- [max-len](/docs/latest/rules/max-len)
- [new-cap](/docs/latest/rules/new-cap)
- [func-names](/docs/latest/rules/func-names)
- [camelcase](/docs/latest/rules/camelcase)

## Version

This rule was introduced in ESLint v1.0.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/id-length.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/id-length.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/id-length.md
                    
                
                )
