# one-var

Enforce variables to be declared either together or separately in functions

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [never](#never)
  3. [consecutive](#consecutive)
  4. [var, let, const, using, and awaitUsing](#var-let-const-using-and-awaitusing)
  5. [initialized and uninitialized](#initialized-and-uninitialized)

3. [Compatibility](#compatibility)
4. [Version](#version)
5. [Resources](#resources)

Variables can be declared at any point in JavaScript code using `var`, `let`, `const`, `using`, or `await using`. There are many styles and preferences related to the declaration of variables, and one of those is deciding on how many variable declarations should be allowed in a single function.

There are two schools of thought in this regard:

1. There should be just one variable declaration for all variables in the function. That declaration typically appears at the top of the function.
2. You should use one variable declaration for each variable you want to define.

For instance:

```
// one variable declaration per function
function foo() {
    var bar, baz;
}

// multiple variable declarations per function
function foo() {
    var bar;
    var baz;
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

The single-declaration school of thought is based in pre-ECMAScript 6 behaviors, where there was no such thing as block scope, only function scope. Since all `var` statements are hoisted to the top of the function anyway, some believe that declaring all variables in a single declaration at the top of the function removes confusion around scoping rules.

## Rule Details

This rule enforces variables to be declared either together or separately per function ( for `var`) or block (for `let`, `const`, `using`, and `await using`) scope.

## Options

This rule has one option, which can be a string option or an object option.

String option:

- `"always"` (default) requires one variable declaration per scope
- `"never"` requires multiple variable declarations per scope
- `"consecutive"` allows multiple variable declarations per scope but requires consecutive variable declarations to be combined into a single declaration

Object option:

- `"var": "always"` requires one `var` declaration per function
- `"var": "never"` requires multiple `var` declarations per function
- `"var": "consecutive"` requires consecutive `var` declarations to be a single declaration
- `"let": "always"` requires one `let` declaration per block
- `"let": "never"` requires multiple `let` declarations per block
- `"let": "consecutive"` requires consecutive `let` declarations to be a single declaration
- `"const": "always"` requires one `const` declaration per block
- `"const": "never"` requires multiple `const` declarations per block
- `"const": "consecutive"` requires consecutive `const` declarations to be a single declaration
- `"using": "always"` requires one `using` declaration per block
- `"using": "never"` requires multiple `using` declarations per block
- `"using": "consecutive"` requires consecutive `using` declarations to be a single declaration
- `"awaitUsing": "always"` requires one `await using` declaration per block
- `"awaitUsing": "never"` requires multiple `await using` declarations per block
- `"awaitUsing": "consecutive"` requires consecutive `await using` declarations to be a single declaration
- `"separateRequires": true` enforces `requires` to be separate from declarations

Alternate object option:

- `"initialized": "always"` requires one variable declaration for initialized variables per scope
- `"initialized": "never"` requires multiple variable declarations for initialized variables per scope
- `"initialized": "consecutive"` requires consecutive variable declarations for initialized variables to be a single declaration
- `"uninitialized": "always"` requires one variable declaration for uninitialized variables per scope
- `"uninitialized": "never"` requires multiple variable declarations for uninitialized variables per scope
- `"uninitialized": "consecutive"` requires consecutive variable declarations for uninitialized variables to be a single declaration

### always

Examples of incorrect code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5mdW5jdGlvbiBmb28xKCkge1xuICAgIHZhciBiYXI7XG4gICAgdmFyIGJhejtcbiAgICBsZXQgcXV4O1xuICAgIGxldCBub3JmO1xufVxuXG5mdW5jdGlvbiBmb28yKCl7XG4gICAgY29uc3QgYmFyID0gZmFsc2U7XG4gICAgY29uc3QgYmF6ID0gdHJ1ZTtcbiAgICBsZXQgcXV4O1xuICAgIGxldCBub3JmO1xufVxuXG5mdW5jdGlvbiBmb28zKCkge1xuICAgIHZhciBiYXI7XG5cbiAgICBpZiAoYmF6KSB7XG4gICAgICAgIHZhciBxdXggPSB0cnVlO1xuICAgIH1cbn1cblxuY2xhc3MgQyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgdmFyIGZvbztcbiAgICAgICAgdmFyIGJhcjtcbiAgICB9XG5cbiAgICBzdGF0aWMge1xuICAgICAgICB2YXIgZm9vO1xuICAgICAgICBpZiAoYmFyKSB7XG4gICAgICAgICAgICB2YXIgYmF6ID0gdHJ1ZTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIHN0YXRpYyB7XG4gICAgICAgIGxldCBmb287XG4gICAgICAgIGxldCBiYXI7XG4gICAgfVxufSJ9)

```
/*eslint one-var: ["error", "always"]*/

function foo1() {
    var bar;
    var baz;
    let qux;
    let norf;
}

function foo2(){
    const bar = false;
    const baz = true;
    let qux;
    let norf;
}

function foo3() {
    var bar;

    if (baz) {
        var qux = true;
    }
}

class C {
    static {
        var foo;
        var bar;
    }

    static {
        var foo;
        if (bar) {
            var baz = true;
        }
    }

    static {
        let foo;
        let bar;
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
40
41
42
```

Examples of correct code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5mdW5jdGlvbiBmb28xKCkge1xuICAgIHZhciBiYXIsXG4gICAgICAgIGJhejtcbiAgICBsZXQgcXV4LFxuICAgICAgICBub3JmO1xufVxuXG5mdW5jdGlvbiBmb28yKCl7XG4gICAgY29uc3QgYmFyID0gdHJ1ZSxcbiAgICAgICAgYmF6ID0gZmFsc2U7XG4gICAgbGV0IHF1eCxcbiAgICAgICAgbm9yZjtcbn1cblxuZnVuY3Rpb24gZm9vMygpIHtcbiAgICB2YXIgYmFyLFxuICAgICAgICBxdXg7XG5cbiAgICBpZiAoYmF6KSB7XG4gICAgICAgIHF1eCA9IHRydWU7XG4gICAgfVxufVxuXG5mdW5jdGlvbiBmb280KCl7XG4gICAgbGV0IGJhcjtcblxuICAgIGlmIChiYXopIHtcbiAgICAgICAgbGV0IHF1eDtcbiAgICB9XG59XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIHZhciBmb28sIGJhcjtcbiAgICB9XG5cbiAgICBzdGF0aWMge1xuICAgICAgICB2YXIgZm9vLCBiYXo7XG4gICAgICAgIGlmIChiYXIpIHtcbiAgICAgICAgICAgIGJheiA9IHRydWU7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICBzdGF0aWMge1xuICAgICAgICBsZXQgZm9vLCBiYXI7XG4gICAgfVxuXG4gICAgc3RhdGljIHtcbiAgICAgICAgbGV0IGZvbztcbiAgICAgICAgaWYgKGJhcikge1xuICAgICAgICAgICAgbGV0IGJhejtcbiAgICAgICAgfVxuICAgIH1cbn0ifQ==)

```
/*eslint one-var: ["error", "always"]*/

function foo1() {
    var bar,
        baz;
    let qux,
        norf;
}

function foo2(){
    const bar = true,
        baz = false;
    let qux,
        norf;
}

function foo3() {
    var bar,
        qux;

    if (baz) {
        qux = true;
    }
}

function foo4(){
    let bar;

    if (baz) {
        let qux;
    }
}

class C {
    static {
        var foo, bar;
    }

    static {
        var foo, baz;
        if (bar) {
            baz = true;
        }
    }

    static {
        let foo, bar;
    }

    static {
        let foo;
        if (bar) {
            let baz;
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
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
```

### never

Examples of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgdmFyIGJhcixcbiAgICAgICAgYmF6O1xuICAgIGNvbnN0IHF1eCA9IHRydWUsXG4gICAgICAgIGZvb2JhciA9IGZhbHNlO1xufVxuXG5mdW5jdGlvbiBmb28yKCkge1xuICAgIHZhciBiYXIsXG4gICAgICAgIHF1eDtcblxuICAgIGlmIChiYXopIHtcbiAgICAgICAgcXV4ID0gdHJ1ZTtcbiAgICB9XG59XG5cbmZ1bmN0aW9uIGZvbzMoKXtcbiAgICBsZXQgYmFyID0gdHJ1ZSxcbiAgICAgICAgYmF6ID0gZmFsc2U7XG59XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIHZhciBmb28sIGJhcjtcbiAgICAgICAgbGV0IGJheiwgcXV4O1xuICAgIH1cbn0ifQ==)

```
/*eslint one-var: ["error", "never"]*/

function foo1() {
    var bar,
        baz;
    const qux = true,
        foobar = false;
}

function foo2() {
    var bar,
        qux;

    if (baz) {
        qux = true;
    }
}

function foo3(){
    let bar = true,
        baz = false;
}

class C {
    static {
        var foo, bar;
        let baz, qux;
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
28
29
```

Examples of correct code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgdmFyIGJhcjtcbiAgICB2YXIgYmF6O1xufVxuXG5mdW5jdGlvbiBmb28yKCkge1xuICAgIHZhciBiYXI7XG5cbiAgICBpZiAoYmF6KSB7XG4gICAgICAgIHZhciBxdXggPSB0cnVlO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gZm9vMygpIHtcbiAgICBsZXQgYmFyO1xuXG4gICAgaWYgKGJheikge1xuICAgICAgICBsZXQgcXV4ID0gdHJ1ZTtcbiAgICB9XG59XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIHZhciBmb287XG4gICAgICAgIHZhciBiYXI7XG4gICAgICAgIGxldCBiYXo7XG4gICAgICAgIGxldCBxdXg7XG4gICAgfVxufVxuXG4vLyBkZWNsYXJhdGlvbnMgd2l0aCBtdWx0aXBsZSB2YXJpYWJsZXMgYXJlIGFsbG93ZWQgaW4gZm9yLWxvb3AgaW5pdGlhbGl6ZXJzXG5mb3IgKHZhciBpID0gMCwgbGVuID0gYXJyLmxlbmd0aDsgaSA8IGxlbjsgaSsrKSB7XG4gICAgZG9Tb21ldGhpbmcoYXJyW2ldKTtcbn0ifQ==)

```
/*eslint one-var: ["error", "never"]*/

function foo1() {
    var bar;
    var baz;
}

function foo2() {
    var bar;

    if (baz) {
        var qux = true;
    }
}

function foo3() {
    let bar;

    if (baz) {
        let qux = true;
    }
}

class C {
    static {
        var foo;
        var bar;
        let baz;
        let qux;
    }
}

// declarations with multiple variables are allowed in for-loop initializers
for (var i = 0, len = arr.length; i < len; i++) {
    doSomething(arr[i]);
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
28
29
30
31
32
33
34
35
36
```

### consecutive

Examples of incorrect code for this rule with the `"consecutive"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgXCJjb25zZWN1dGl2ZVwiXSovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgdmFyIGJhcjtcbiAgICB2YXIgYmF6O1xufVxuXG5mdW5jdGlvbiBmb28yKCl7XG4gICAgdmFyIGJhciA9IDE7XG4gICAgdmFyIGJheiA9IDI7XG5cbiAgICBxdXgoKTtcblxuICAgIHZhciBxdXggPSAzO1xuICAgIHZhciBxdXV4O1xufVxuXG5jbGFzcyBDIHtcbiAgICBzdGF0aWMge1xuICAgICAgICB2YXIgZm9vO1xuICAgICAgICB2YXIgYmFyO1xuICAgICAgICBsZXQgYmF6O1xuICAgICAgICBsZXQgcXV4O1xuICAgIH1cbn0ifQ==)

```
/*eslint one-var: ["error", "consecutive"]*/

function foo1() {
    var bar;
    var baz;
}

function foo2(){
    var bar = 1;
    var baz = 2;

    qux();

    var qux = 3;
    var quux;
}

class C {
    static {
        var foo;
        var bar;
        let baz;
        let qux;
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
```

Examples of correct code for this rule with the `"consecutive"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgXCJjb25zZWN1dGl2ZVwiXSovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgdmFyIGJhcixcbiAgICAgICAgYmF6O1xufVxuXG5mdW5jdGlvbiBmb28yKCl7XG4gICAgdmFyIGJhciA9IDEsXG4gICAgICAgIGJheiA9IDI7XG5cbiAgICBxdXgoKTtcblxuICAgIHZhciBxdXggPSAzLFxuICAgICAgICBxdXV4O1xufVxuXG5jbGFzcyBDIHtcbiAgICBzdGF0aWMge1xuICAgICAgICB2YXIgZm9vLCBiYXI7XG4gICAgICAgIGxldCBiYXosIHF1eDtcbiAgICAgICAgZG9Tb21ldGhpbmcoKTtcbiAgICAgICAgbGV0IHF1dXg7XG4gICAgICAgIHZhciBxdXV1eDtcbiAgICB9XG59In0=)

```
/*eslint one-var: ["error", "consecutive"]*/

function foo1() {
    var bar,
        baz;
}

function foo2(){
    var bar = 1,
        baz = 2;

    qux();

    var qux = 3,
        quux;
}

class C {
    static {
        var foo, bar;
        let baz, qux;
        doSomething();
        let quux;
        var quuux;
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
```

### var, let, const, using, and awaitUsing

Examples of incorrect code for this rule with the `{ var: "always", let: "never", const: "never", using: "never", awaitUsing: "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwiYWx3YXlzXCIsIGxldDogXCJuZXZlclwiLCBjb25zdDogXCJuZXZlclwiLCB1c2luZzogXCJuZXZlclwiLCBhd2FpdFVzaW5nOiBcIm5ldmVyXCIgfV0qL1xuXG5mdW5jdGlvbiBmb28xKCkge1xuICAgIHZhciBiYXI7XG4gICAgdmFyIGJhejtcbiAgICBsZXQgcXV4LFxuICAgICAgICBub3JmO1xufVxuXG5mdW5jdGlvbiBmb28yKCkge1xuICAgIGNvbnN0IGJhciA9IDEsXG4gICAgICAgICAgYmF6ID0gMjtcbiAgICBsZXQgcXV4LFxuICAgICAgICBub3JmO1xufVxuXG5hc3luYyBmdW5jdGlvbiBmb28zKCkge1xuICAgIHVzaW5nIGJhciA9IDEsXG4gICAgICAgICAgYmF6ID0gMjtcbiAgICBhd2FpdCB1c2luZyBxdXggPSAzLFxuICAgICAgICAgICAgICAgIG5vcmYgPSA0O1xufSJ9)

```
/*eslint one-var: ["error", { var: "always", let: "never", const: "never", using: "never", awaitUsing: "never" }]*/

function foo1() {
    var bar;
    var baz;
    let qux,
        norf;
}

function foo2() {
    const bar = 1,
          baz = 2;
    let qux,
        norf;
}

async function foo3() {
    using bar = 1,
          baz = 2;
    await using qux = 3,
                norf = 4;
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

Examples of correct code for this rule with the `{ var: "always", let: "never", const: "never", using: "never", awaitUsing: "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwiYWx3YXlzXCIsIGxldDogXCJuZXZlclwiLCBjb25zdDogXCJuZXZlclwiLCB1c2luZzogXCJuZXZlclwiLCBhd2FpdFVzaW5nOiBcIm5ldmVyXCIgfV0qL1xuXG5mdW5jdGlvbiBmb28xKCkge1xuICAgIHZhciBiYXIsXG4gICAgICAgIGJhejtcbiAgICBsZXQgcXV4O1xuICAgIGxldCBub3JmO1xufVxuXG5mdW5jdGlvbiBmb28yKCkge1xuICAgIGNvbnN0IGJhciA9IDE7XG4gICAgY29uc3QgYmF6ID0gMjtcbiAgICBsZXQgcXV4O1xuICAgIGxldCBub3JmO1xufVxuXG5hc3luYyBmdW5jdGlvbiBmb28zKCkge1xuICAgIHVzaW5nIGJhciA9IDE7XG4gICAgdXNpbmcgYmF6ID0gMjtcbiAgICBhd2FpdCB1c2luZyBxdXggPSAzO1xuICAgIGF3YWl0IHVzaW5nIG5vcmYgPSA0O1xufSJ9)

```
/*eslint one-var: ["error", { var: "always", let: "never", const: "never", using: "never", awaitUsing: "never" }]*/

function foo1() {
    var bar,
        baz;
    let qux;
    let norf;
}

function foo2() {
    const bar = 1;
    const baz = 2;
    let qux;
    let norf;
}

async function foo3() {
    using bar = 1;
    using baz = 2;
    await using qux = 3;
    await using norf = 4;
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

Examples of incorrect code for this rule with the `{ var: "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwibmV2ZXJcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYmFyLFxuICAgICAgICBiYXo7XG59In0=)

```
/*eslint one-var: ["error", { var: "never" }]*/

function foo() {
    var bar,
        baz;
}
1
2
3
4
5
6
```

Examples of correct code for this rule with the `{ var: "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwibmV2ZXJcIiB9XSovXG5cbmFzeW5jIGZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYmFyO1xuICAgIHZhciBiYXo7XG5cbiAgICAvLyBgY29uc3RgLCBgbGV0YCwgYHVzaW5nYCBhbmQgYGF3YWl0IHVzaW5nYCBkZWNsYXJhdGlvbnMgYXJlIGlnbm9yZWQgaWYgdGhleSBhcmUgbm90IHNwZWNpZmllZFxuICAgIGNvbnN0IGZvb2JhciA9IDE7XG4gICAgY29uc3QgZm9vYmF6ID0gMjtcbiAgICBjb25zdCBiYXJmb28gPSAxLCBiYXpmb28gPSAyO1xuICAgIGxldCBxdXg7XG4gICAgbGV0IG5vcmY7XG4gICAgbGV0IGZvb3F1eCwgZm9vbm9yZjtcbiAgICB1c2luZyBmb29iYXJmb28gPSAxO1xuICAgIHVzaW5nIGZvb2JhemZvbyA9IDI7XG4gICAgdXNpbmcgYmF6YmFyZm9vID0gMSwgYmF6Zm9vYmFyID0gMjtcbiAgICBhd2FpdCB1c2luZyBmb29iYXJiYXogPSAxO1xuICAgIGF3YWl0IHVzaW5nIGZvb2JhenF1eCA9IDI7XG4gICAgYXdhaXQgdXNpbmcgYmF6YmFycXV4ID0gMSwgYmF6Zm9vcXV4ID0gMjtcbn0ifQ==)

```
/*eslint one-var: ["error", { var: "never" }]*/

async function foo() {
    var bar;
    var baz;

    // `const`, `let`, `using` and `await using` declarations are ignored if they are not specified
    const foobar = 1;
    const foobaz = 2;
    const barfoo = 1, bazfoo = 2;
    let qux;
    let norf;
    let fooqux, foonorf;
    using foobarfoo = 1;
    using foobazfoo = 2;
    using bazbarfoo = 1, bazfoobar = 2;
    await using foobarbaz = 1;
    await using foobazqux = 2;
    await using bazbarqux = 1, bazfooqux = 2;
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

Examples of incorrect code for this rule with the `{ separateRequires: true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBzZXBhcmF0ZVJlcXVpcmVzOiB0cnVlLCB2YXI6IFwiYWx3YXlzXCIgfV0qL1xuXG52YXIgZm9vID0gcmVxdWlyZShcImZvb1wiKSxcbiAgICBiYXIgPSBcImJhclwiOyJ9)

```
/*eslint one-var: ["error", { separateRequires: true, var: "always" }]*/

var foo = require("foo"),
    bar = "bar";
1
2
3
4
```

Examples of correct code for this rule with the `{ separateRequires: true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBzZXBhcmF0ZVJlcXVpcmVzOiB0cnVlLCB2YXI6IFwiYWx3YXlzXCIgfV0qL1xuXG52YXIgZm9vID0gcmVxdWlyZShcImZvb1wiKTtcbnZhciBiYXIgPSBcImJhclwiOyJ9)

```
/*eslint one-var: ["error", { separateRequires: true, var: "always" }]*/

var foo = require("foo");
var bar = "bar";
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBzZXBhcmF0ZVJlcXVpcmVzOiB0cnVlLCB2YXI6IFwiYWx3YXlzXCIgfV0qL1xuXG52YXIgZm9vID0gcmVxdWlyZShcImZvb1wiKSxcbiAgICBiYXIgPSByZXF1aXJlKFwiYmFyXCIpOyJ9)

```
/*eslint one-var: ["error", { separateRequires: true, var: "always" }]*/

var foo = require("foo"),
    bar = require("bar");
1
2
3
4
```

Examples of incorrect code for this rule with the `{ var: "never", let: "consecutive", const: "consecutive", using: "consecutive", awaitUsing: "consecutive" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwibmV2ZXJcIiwgbGV0OiBcImNvbnNlY3V0aXZlXCIsIGNvbnN0OiBcImNvbnNlY3V0aXZlXCIsIHVzaW5nOiBcImNvbnNlY3V0aXZlXCIsIGF3YWl0VXNpbmc6IFwiY29uc2VjdXRpdmVcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgbGV0IGEsXG4gICAgICAgIGI7XG4gICAgbGV0IGM7XG5cbiAgICB2YXIgZCxcbiAgICAgICAgZTtcbn1cblxuZnVuY3Rpb24gZm9vMigpIHtcbiAgICBjb25zdCBhID0gMSxcbiAgICAgICAgYiA9IDI7XG4gICAgY29uc3QgYyA9IDM7XG5cbiAgICB2YXIgZCxcbiAgICAgICAgZTtcbn1cblxuZnVuY3Rpb24gZm9vMygpIHtcbiAgICB1c2luZyBhID0gMSxcbiAgICAgICAgYiA9IDI7XG4gICAgdXNpbmcgYyA9IDM7XG5cbiAgICB2YXIgZCxcbiAgICAgICAgZTtcbn1cblxuYXN5bmMgZnVuY3Rpb24gZm9vNCgpIHtcbiAgICBhd2FpdCB1c2luZyBhID0gMSxcbiAgICAgICAgYiA9IDI7XG4gICAgYXdhaXQgdXNpbmcgYyA9IDM7XG5cbiAgICB2YXIgZCxcbiAgICAgICAgZTtcbn0ifQ==)

```
/*eslint one-var: ["error", { var: "never", let: "consecutive", const: "consecutive", using: "consecutive", awaitUsing: "consecutive" }]*/

function foo1() {
    let a,
        b;
    let c;

    var d,
        e;
}

function foo2() {
    const a = 1,
        b = 2;
    const c = 3;

    var d,
        e;
}

function foo3() {
    using a = 1,
        b = 2;
    using c = 3;

    var d,
        e;
}

async function foo4() {
    await using a = 1,
        b = 2;
    await using c = 3;

    var d,
        e;
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
```

Examples of correct code for this rule with the `{ var: "never", let: "consecutive", const: "consecutive", using: "consecutive", awaitUsing: "consecutive" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwibmV2ZXJcIiwgbGV0OiBcImNvbnNlY3V0aXZlXCIsIGNvbnN0OiBcImNvbnNlY3V0aXZlXCIsIHVzaW5nOiBcImNvbnNlY3V0aXZlXCIsIGF3YWl0VXNpbmc6IFwiY29uc2VjdXRpdmVcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgbGV0IGEsXG4gICAgICAgIGI7XG5cbiAgICB2YXIgZDtcbiAgICB2YXIgZTtcblxuICAgIGxldCBmO1xufVxuXG5mdW5jdGlvbiBmb28yKCkge1xuICAgIGNvbnN0IGEgPSAxLFxuICAgICAgICAgIGIgPSAyO1xuXG4gICAgdmFyIGM7XG4gICAgdmFyIGQ7XG5cbiAgICBjb25zdCBlID0gMztcbn1cblxuZnVuY3Rpb24gZm9vMygpIHtcbiAgICB1c2luZyBhID0gMSxcbiAgICAgICAgICBiID0gMjtcblxuICAgIHZhciBjO1xuICAgIHZhciBkO1xuXG4gICAgdXNpbmcgZSA9IDM7XG59XG5cbmFzeW5jIGZ1bmN0aW9uIGZvbzQoKSB7XG4gICAgYXdhaXQgdXNpbmcgYSA9IDEsXG4gICAgICAgICAgYiA9IDI7XG5cbiAgICB2YXIgYztcbiAgICB2YXIgZDtcblxuICAgIGF3YWl0IHVzaW5nIGUgPSAzO1xufSJ9)

```
/*eslint one-var: ["error", { var: "never", let: "consecutive", const: "consecutive", using: "consecutive", awaitUsing: "consecutive" }]*/

function foo1() {
    let a,
        b;

    var d;
    var e;

    let f;
}

function foo2() {
    const a = 1,
          b = 2;

    var c;
    var d;

    const e = 3;
}

function foo3() {
    using a = 1,
          b = 2;

    var c;
    var d;

    using e = 3;
}

async function foo4() {
    await using a = 1,
          b = 2;

    var c;
    var d;

    await using e = 3;
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
40
41
```

Examples of incorrect code for this rule with the `{ var: "consecutive" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwiY29uc2VjdXRpdmVcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYTtcbiAgICB2YXIgYjtcbn0ifQ==)

```
/*eslint one-var: ["error", { var: "consecutive" }]*/

function foo() {
    var a;
    var b;
}
1
2
3
4
5
6
```

Examples of correct code for this rule with the `{ var: "consecutive" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyB2YXI6IFwiY29uc2VjdXRpdmVcIiB9XSovXG5cbmFzeW5jIGZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYSxcbiAgICAgICAgYjtcbiBcbiAgICAvLyBgY29uc3RgLCBgbGV0YCwgYHVzaW5nYCwgYW5kIGBhd2FpdCB1c2luZ2AgZGVjbGFyYXRpb25zIGFyZSBpZ25vcmVkIGlmIHRoZXkgYXJlIG5vdCBzcGVjaWZpZWRcbiAgICBjb25zdCBjID0gMTtcbiAgICBjb25zdCBkID0gMjtcbiAgICBsZXQgZTtcbiAgICBsZXQgZjtcbiAgICB1c2luZyBnID0gMztcbiAgICB1c2luZyBoID0gNDtcbiAgICBhd2FpdCB1c2luZyBpID0gNTtcbiAgICBhd2FpdCB1c2luZyBqID0gNjtcbn0ifQ==)

```
/*eslint one-var: ["error", { var: "consecutive" }]*/

async function foo() {
    var a,
        b;
 
    // `const`, `let`, `using`, and `await using` declarations are ignored if they are not specified
    const c = 1;
    const d = 2;
    let e;
    let f;
    using g = 3;
    using h = 4;
    await using i = 5;
    await using j = 6;
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
```

### initialized and uninitialized

Examples of incorrect code for this rule with the `{ "initialized": "always", "uninitialized": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwiYWx3YXlzXCIsIFwidW5pbml0aWFsaXplZFwiOiBcIm5ldmVyXCIgfV0qL1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgdmFyIGEsIGIsIGM7XG4gICAgdmFyIGZvbyA9IHRydWU7XG4gICAgdmFyIGJhciA9IGZhbHNlO1xufSJ9)

```
/*eslint one-var: ["error", { "initialized": "always", "uninitialized": "never" }]*/

function foo() {
    var a, b, c;
    var foo = true;
    var bar = false;
}
1
2
3
4
5
6
7
```

Examples of correct code for this rule with the `{ "initialized": "always", "uninitialized": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwiYWx3YXlzXCIsIFwidW5pbml0aWFsaXplZFwiOiBcIm5ldmVyXCIgfV0qL1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgdmFyIGE7XG4gICAgdmFyIGI7XG4gICAgdmFyIGM7XG4gICAgdmFyIGZvbyA9IHRydWUsXG4gICAgICAgIGJhciA9IGZhbHNlO1xufVxuXG5mb3IgKGxldCB6IG9mIGZvbykge1xuICAgIGRvU29tZXRoaW5nKHopO1xufVxuXG5sZXQgejtcbmZvciAoeiBvZiBmb28pIHtcbiAgICBkb1NvbWV0aGluZyh6KTtcbn0ifQ==)

```
/*eslint one-var: ["error", { "initialized": "always", "uninitialized": "never" }]*/

function foo() {
    var a;
    var b;
    var c;
    var foo = true,
        bar = false;
}

for (let z of foo) {
    doSomething(z);
}

let z;
for (z of foo) {
    doSomething(z);
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
```

Examples of incorrect code for this rule with the `{ "initialized": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwibmV2ZXJcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgZm9vID0gdHJ1ZSxcbiAgICAgICAgYmFyID0gZmFsc2U7XG59In0=)

```
/*eslint one-var: ["error", { "initialized": "never" }]*/

function foo() {
    var foo = true,
        bar = false;
}
1
2
3
4
5
6
```

Examples of correct code for this rule with the `{ "initialized": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwibmV2ZXJcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgZm9vID0gdHJ1ZTtcbiAgICB2YXIgYmFyID0gZmFsc2U7XG4gICAgdmFyIGEsIGIsIGM7IC8vIFVuaW5pdGlhbGl6ZWQgdmFyaWFibGVzIGFyZSBpZ25vcmVkXG59In0=)

```
/*eslint one-var: ["error", { "initialized": "never" }]*/

function foo() {
    var foo = true;
    var bar = false;
    var a, b, c; // Uninitialized variables are ignored
}
1
2
3
4
5
6
7
```

Examples of incorrect code for this rule with the `{ "initialized": "consecutive", "uninitialized": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwiY29uc2VjdXRpdmVcIiwgXCJ1bmluaXRpYWxpemVkXCI6IFwibmV2ZXJcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYSA9IDE7XG4gICAgdmFyIGIgPSAyO1xuICAgIHZhciBjLFxuICAgICAgICBkO1xuICAgIHZhciBlID0gMztcbiAgICB2YXIgZiA9IDQ7XG59In0=)

```
/*eslint one-var: ["error", { "initialized": "consecutive", "uninitialized": "never" }]*/

function foo() {
    var a = 1;
    var b = 2;
    var c,
        d;
    var e = 3;
    var f = 4;
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

Examples of correct code for this rule with the `{ "initialized": "consecutive", "uninitialized": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwiY29uc2VjdXRpdmVcIiwgXCJ1bmluaXRpYWxpemVkXCI6IFwibmV2ZXJcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYSA9IDEsXG4gICAgICAgIGIgPSAyO1xuICAgIHZhciBjO1xuICAgIHZhciBkO1xuICAgIHZhciBlID0gMyxcbiAgICAgICAgZiA9IDQ7XG59In0=)

```
/*eslint one-var: ["error", { "initialized": "consecutive", "uninitialized": "never" }]*/

function foo() {
    var a = 1,
        b = 2;
    var c;
    var d;
    var e = 3,
        f = 4;
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

Examples of incorrect code for this rule with the `{ "initialized": "consecutive" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwiY29uc2VjdXRpdmVcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYSA9IDE7XG4gICAgdmFyIGIgPSAyO1xuXG4gICAgZm9vKCk7XG5cbiAgICB2YXIgYyA9IDM7XG4gICAgdmFyIGQgPSA0O1xufSJ9)

```
/*eslint one-var: ["error", { "initialized": "consecutive" }]*/

function foo() {
    var a = 1;
    var b = 2;

    foo();

    var c = 3;
    var d = 4;
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
```

Examples of correct code for this rule with the `{ "initialized": "consecutive" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb25lLXZhcjogW1wiZXJyb3JcIiwgeyBcImluaXRpYWxpemVkXCI6IFwiY29uc2VjdXRpdmVcIiB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICB2YXIgYSA9IDEsXG4gICAgICAgIGIgPSAyO1xuXG4gICAgZm9vKCk7XG5cbiAgICB2YXIgYyA9IDMsXG4gICAgICAgIGQgPSA0O1xufSJ9)

```
/*eslint one-var: ["error", { "initialized": "consecutive" }]*/

function foo() {
    var a = 1,
        b = 2;

    foo();

    var c = 3,
        d = 4;
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
```

## Compatibility

- JSHint: This rule maps to the `onevar` JSHint rule, but allows `let` and `const` to be configured separately.
- JSCS: This rule roughly maps to [disallowMultipleVarDecl](https://jscs-dev.github.io/rule/disallowMultipleVarDecl).
- JSCS: This rule option `separateRequires` roughly maps to [requireMultipleVarDecl](https://jscs-dev.github.io/rule/requireMultipleVarDecl).

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/one-var.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/one-var.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/one-var.md
                    
                
                )
