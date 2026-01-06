# no-inner-declarations

Disallow variable or `function` declarations in nested blocks

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [functions](#functions)
  2. [both](#both)
  3. [blockScopedFunctions](#blockscopedfunctions)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

In JavaScript, prior to ES6, a function declaration is only allowed in the first level of a program or the body of another function, though parsers sometimes [erroneously accept them elsewhere](https://code.google.com/p/esprima/issues/detail?id=422). This only applies to function declarations; named or anonymous function expressions can occur anywhere an expression is permitted.

```
// Good
function doSomething() { }

// Bad
if (test) {
    function doSomethingElse () { }
}

function anotherThing() {
    var fn;

    if (test) {

        // Good
        fn = function expression() { };

        // Bad
        function declaration() { }
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

Copy code to clipboard

In ES6, [block-level functions](https://leanpub.com/understandinges6/read#leanpub-auto-block-level-functions) (functions declared inside a block) are limited to the scope of the block they are declared in and outside of the block scope they can’t be accessed and called, but only when the code is in strict mode (code with `"use strict"` tag or ESM modules). In non-strict mode, they can be accessed and called outside of the block scope.

```
"use strict";

if (test) {
    function doSomething () { }

    doSomething(); // no error
}

doSomething(); // error
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

Copy code to clipboard

A variable declaration is permitted anywhere a statement can go, even nested deeply inside other blocks. This is often undesirable due to variable hoisting, and moving declarations to the root of the program or function body can increase clarity. Note that [block bindings](https://leanpub.com/understandinges6/read#leanpub-auto-block-bindings) (`let`, `const`) are not hoisted and therefore they are not affected by this rule.

```
// Good
var foo = 42;

// Good
if (foo) {
    let bar1;
}

// Bad
while (test) {
    var bar2;
}

function doSomething() {
    // Good
    var baz = true;

    // Bad
    if (baz) {
        var quux;
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
```

Copy code to clipboard

## Rule Details

This rule requires that function declarations and, optionally, variable declarations be in the root of a program, or in the root of the body of a function, or in the root of the body of a class static block.

## Options

This rule has a string and an object option:

- `"functions"` (default) disallows `function` declarations in nested blocks
- `"both"` disallows `function` and `var` declarations in nested blocks
- `{ blockScopedFunctions: "allow" }` (default) this option allows `function` declarations in nested blocks when code is in strict mode (code with `"use strict"` tag or ESM modules) and `languageOptions.ecmaVersion` is set to `2015` or above. This option can be disabled by setting it to `"disallow"`.

### functions

Examples of incorrect code for this rule with the default `"functions"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5uZXItZGVjbGFyYXRpb25zOiBcImVycm9yXCIqL1xuXG4vLyBzY3JpcHQsIG5vbi1zdHJpY3QgY29kZVxuXG5pZiAodGVzdCkge1xuICAgIGZ1bmN0aW9uIGRvU29tZXRoaW5nKCkgeyB9XG59XG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nRWxzZSgpIHtcbiAgICBpZiAodGVzdCkge1xuICAgICAgICBmdW5jdGlvbiBkb0Fub3RoZXJUaGluZygpIHsgfVxuICAgIH1cbn1cblxuaWYgKGZvbykgZnVuY3Rpb24gZigpe30ifQ==)

```
/*eslint no-inner-declarations: "error"*/

// script, non-strict code

if (test) {
    function doSomething() { }
}

function doSomethingElse() {
    if (test) {
        function doAnotherThing() { }
    }
}

if (foo) function f(){}
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

Examples of correct code for this rule with the default `"functions"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5uZXItZGVjbGFyYXRpb25zOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBkb1NvbWV0aGluZygpIHsgfVxuXG5mdW5jdGlvbiBkb1NvbWV0aGluZ0Vsc2UoKSB7XG4gICAgZnVuY3Rpb24gZG9Bbm90aGVyVGhpbmcoKSB7IH1cbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkge1xuICAgIFwidXNlIHN0cmljdFwiO1xuXG4gICAgaWYgKHRlc3QpIHtcbiAgICAgICAgZnVuY3Rpb24gZG9Bbm90aGVyVGhpbmcoKSB7IH1cbiAgICB9XG59XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIGZ1bmN0aW9uIGRvU29tZXRoaW5nKCkgeyB9XG4gICAgfVxufVxuXG5pZiAodGVzdCkge1xuICAgIGFzeW5jQ2FsbChpZCwgZnVuY3Rpb24gKGVyciwgZGF0YSkgeyB9KTtcbn1cblxudmFyIGZuO1xuaWYgKHRlc3QpIHtcbiAgICBmbiA9IGZ1bmN0aW9uIGZuRXhwcmVzc2lvbigpIHsgfTtcbn1cblxuaWYgKGZvbykgdmFyIGE7In0=)

```
/*eslint no-inner-declarations: "error"*/

function doSomething() { }

function doSomethingElse() {
    function doAnotherThing() { }
}

function doSomethingElse() {
    "use strict";

    if (test) {
        function doAnotherThing() { }
    }
}

class C {
    static {
        function doSomething() { }
    }
}

if (test) {
    asyncCall(id, function (err, data) { });
}

var fn;
if (test) {
    fn = function fnExpression() { };
}

if (foo) var a;
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
```

### both

Examples of incorrect code for this rule with the `"both"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5uZXItZGVjbGFyYXRpb25zOiBbXCJlcnJvclwiLCBcImJvdGhcIl0qL1xuXG5pZiAodGVzdCkge1xuICAgIHZhciBmb28gPSA0Mjtcbn1cblxuZnVuY3Rpb24gZG9Bbm90aGVyVGhpbmcoKSB7XG4gICAgaWYgKHRlc3QpIHtcbiAgICAgICAgdmFyIGJhciA9IDgxO1xuICAgIH1cbn1cblxuaWYgKGZvbykgdmFyIGE7XG5cbmlmIChmb28pIGZ1bmN0aW9uIGYoKXt9XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIGlmICh0ZXN0KSB7XG4gICAgICAgICAgICB2YXIgc29tZXRoaW5nO1xuICAgICAgICB9XG4gICAgfVxufSJ9)

```
/*eslint no-inner-declarations: ["error", "both"]*/

if (test) {
    var foo = 42;
}

function doAnotherThing() {
    if (test) {
        var bar = 81;
    }
}

if (foo) var a;

if (foo) function f(){}

class C {
    static {
        if (test) {
            var something;
        }
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
```

Examples of correct code for this rule with the `"both"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5uZXItZGVjbGFyYXRpb25zOiBbXCJlcnJvclwiLCBcImJvdGhcIl0qL1xuXG52YXIgYmFyID0gNDI7XG5cbmlmICh0ZXN0KSB7XG4gICAgbGV0IGJheiA9IDQzO1xufVxuXG5mdW5jdGlvbiBkb0Fub3RoZXJUaGluZygpIHtcbiAgICB2YXIgYmF6ID0gODE7XG59XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIHZhciBzb21ldGhpbmc7XG4gICAgfVxufSJ9)

```
/*eslint no-inner-declarations: ["error", "both"]*/

var bar = 42;

if (test) {
    let baz = 43;
}

function doAnotherThing() {
    var baz = 81;
}

class C {
    static {
        var something;
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

### blockScopedFunctions

Example of incorrect code for this rule with `{ blockScopedFunctions: "disallow" }` option with `ecmaVersion: 2015`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0IiwiZWNtYVZlcnNpb24iOjIwMTV9fSwidGV4dCI6Ii8qZXNsaW50IG5vLWlubmVyLWRlY2xhcmF0aW9uczogW1wiZXJyb3JcIiwgXCJmdW5jdGlvbnNcIiwgeyBibG9ja1Njb3BlZEZ1bmN0aW9uczogXCJkaXNhbGxvd1wiIH1dKi9cblxuLy8gbm9uLXN0cmljdCBjb2RlXG5cbmlmICh0ZXN0KSB7XG4gICAgZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7IH1cbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7XG4gICAgaWYgKHRlc3QpIHtcbiAgICAgICAgZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkgeyB9XG4gICAgfVxufVxuXG4vLyBzdHJpY3QgY29kZVxuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgXCJ1c2Ugc3RyaWN0XCI7XG5cbiAgICBpZiAodGVzdCkge1xuICAgICAgICBmdW5jdGlvbiBiYXIoKSB7IH1cbiAgICB9XG59In0=)

```
/*eslint no-inner-declarations: ["error", "functions", { blockScopedFunctions: "disallow" }]*/

// non-strict code

if (test) {
    function doSomething() { }
}

function doSomething() {
    if (test) {
        function doSomethingElse() { }
    }
}

// strict code

function foo() {
    "use strict";

    if (test) {
        function bar() { }
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
```

Example of correct code for this rule with `{ blockScopedFunctions: "disallow" }` option with `ecmaVersion: 2015`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0IiwiZWNtYVZlcnNpb24iOjIwMTV9fSwidGV4dCI6Ii8qZXNsaW50IG5vLWlubmVyLWRlY2xhcmF0aW9uczogW1wiZXJyb3JcIiwgXCJmdW5jdGlvbnNcIiwgeyBibG9ja1Njb3BlZEZ1bmN0aW9uczogXCJkaXNhbGxvd1wiIH1dKi9cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7IH1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7XG4gICAgZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkgeyB9XG59In0=)

```
/*eslint no-inner-declarations: ["error", "functions", { blockScopedFunctions: "disallow" }]*/

function doSomething() { }

function doSomething() {
    function doSomethingElse() { }
}
1
2
3
4
5
6
7
```

Example of correct code for this rule with `{ blockScopedFunctions: "allow" }` option with `ecmaVersion: 2015`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0IiwiZWNtYVZlcnNpb24iOjIwMTV9fSwidGV4dCI6Ii8qZXNsaW50IG5vLWlubmVyLWRlY2xhcmF0aW9uczogW1wiZXJyb3JcIiwgXCJmdW5jdGlvbnNcIiwgeyBibG9ja1Njb3BlZEZ1bmN0aW9uczogXCJhbGxvd1wiIH1dKi9cblxuXCJ1c2Ugc3RyaWN0XCI7XG5cbmlmICh0ZXN0KSB7XG4gICAgZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7IH1cbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7XG4gICAgaWYgKHRlc3QpIHtcbiAgICAgICAgZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkgeyB9XG4gICAgfVxufVxuXG4vLyBPUlxuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgXCJ1c2Ugc3RyaWN0XCI7XG5cbiAgICBpZiAodGVzdCkge1xuICAgICAgICBmdW5jdGlvbiBiYXIoKSB7IH1cbiAgICB9XG59In0=)

```
/*eslint no-inner-declarations: ["error", "functions", { blockScopedFunctions: "allow" }]*/

"use strict";

if (test) {
    function doSomething() { }
}

function doSomething() {
    if (test) {
        function doSomethingElse() { }
    }
}

// OR

function foo() {
    "use strict";

    if (test) {
        function bar() { }
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
```

`ESM modules` and both `class` declarations and expressions are always in strict mode.

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW5uZXItZGVjbGFyYXRpb25zOiBbXCJlcnJvclwiLCBcImZ1bmN0aW9uc1wiLCB7IGJsb2NrU2NvcGVkRnVuY3Rpb25zOiBcImFsbG93XCIgfV0qL1xuXG5pZiAodGVzdCkge1xuICAgIGZ1bmN0aW9uIGRvU29tZXRoaW5nKCkgeyB9XG59XG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nRWxzZSgpIHtcbiAgICBpZiAodGVzdCkge1xuICAgICAgICBmdW5jdGlvbiBkb0Fub3RoZXJUaGluZygpIHsgfVxuICAgIH1cbn1cblxuY2xhc3MgU29tZSB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgaWYgKHRlc3QpIHtcbiAgICAgICAgICAgIGZ1bmN0aW9uIGRvU29tZXRoaW5nKCkgeyB9XG4gICAgICAgIH1cbiAgICB9XG59XG5cbmNvbnN0IEMgPSBjbGFzcyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgaWYgKHRlc3QpIHtcbiAgICAgICAgICAgIGZ1bmN0aW9uIGRvU29tZXRoaW5nKCkgeyB9XG4gICAgICAgIH1cbiAgICB9XG59In0=)

```
/*eslint no-inner-declarations: ["error", "functions", { blockScopedFunctions: "allow" }]*/

if (test) {
    function doSomething() { }
}

function doSomethingElse() {
    if (test) {
        function doAnotherThing() { }
    }
}

class Some {
    static {
        if (test) {
            function doSomething() { }
        }
    }
}

const C = class {
    static {
        if (test) {
            function doSomething() { }
        }
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
```

## When Not To Use It

By default, this rule disallows inner function declarations only in contexts where their behavior is unspecified and thus inconsistent (pre-ES6 environments) or legacy semantics apply (non-strict mode code). If your code targets pre-ES6 environments or is not in strict mode, you should enable this rule to prevent unexpected behavior.

In ES6+ environments, in strict mode code, the behavior of inner function declarations is well-defined and consistent - they are always block-scoped. If your code targets only ES6+ environments and is in strict mode (ES modules, or code with `"use strict"` directives) then there is no need to enable this rule unless you want to disallow inner functions as a stylistic choice, in which case you should enable this rule with the option `blockScopedFunctions: "disallow"`.

Disable checking variable declarations when using [block-scoped-var](block-scoped-var) or if declaring variables in nested blocks is acceptable despite hoisting.

## Version

This rule was introduced in ESLint v0.6.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-inner-declarations.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-inner-declarations.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-inner-declarations.md
                    
                
                )
