# no-unreachable

Disallow unreachable code after `return`, `throw`, `continue`, and `break` statements

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Handled by TypeScript](#handled_by_typescript)
3. [Version](#version)
4. [Resources](#resources)

Because the `return`, `throw`, `continue`, and `break` statements unconditionally exit a block of code, any statements after them cannot be executed. Unreachable statements are usually a mistake.

```
function fn() {
    x = 1;
    return x;
    x = 3; // this will never execute
}
1
2
3
4
5
```

Copy code to clipboard

Another kind of mistake is defining instance fields in a subclass whose constructor doesn’t call `super()`. Instance fields of a subclass are only added to the instance after `super()`. If there are no `super()` calls, their definitions are never applied and therefore are unreachable code.

```
class C extends B {
    #x; // this will never be added to instances

    constructor() {
        return {};
    }
}
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

This rule disallows unreachable code after `return`, `throw`, `continue`, and `break` statements. This rule also flags definitions of instance fields in subclasses whose constructors don’t have `super()` calls.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGU6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICByZXR1cm4gdHJ1ZTtcbiAgICBjb25zb2xlLmxvZyhcImRvbmVcIik7XG59XG5cbmZ1bmN0aW9uIGJhcigpIHtcbiAgICB0aHJvdyBuZXcgRXJyb3IoXCJPb3BzIVwiKTtcbiAgICBjb25zb2xlLmxvZyhcImRvbmVcIik7XG59XG5cbndoaWxlKHZhbHVlKSB7XG4gICAgYnJlYWs7XG4gICAgY29uc29sZS5sb2coXCJkb25lXCIpO1xufVxuXG50aHJvdyBuZXcgRXJyb3IoXCJPb3BzIVwiKTtcbmNvbnNvbGUubG9nKFwiZG9uZVwiKTtcblxuZnVuY3Rpb24gYmF6KCkge1xuICAgIGlmIChNYXRoLnJhbmRvbSgpIDwgMC41KSB7XG4gICAgICAgIHJldHVybjtcbiAgICB9IGVsc2Uge1xuICAgICAgICB0aHJvdyBuZXcgRXJyb3IoKTtcbiAgICB9XG4gICAgY29uc29sZS5sb2coXCJkb25lXCIpO1xufVxuXG5mb3IgKDs7KSB7fVxuY29uc29sZS5sb2coXCJkb25lXCIpOyJ9)

```
/*eslint no-unreachable: "error"*/

function foo() {
    return true;
    console.log("done");
}

function bar() {
    throw new Error("Oops!");
    console.log("done");
}

while(value) {
    break;
    console.log("done");
}

throw new Error("Oops!");
console.log("done");

function baz() {
    if (Math.random() < 0.5) {
        return;
    } else {
        throw new Error();
    }
    console.log("done");
}

for (;;) {}
console.log("done");
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

Examples of correct code for this rule, because of JavaScript function and variable hoisting:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGU6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICByZXR1cm4gYmFyKCk7XG4gICAgZnVuY3Rpb24gYmFyKCkge1xuICAgICAgICByZXR1cm4gMTtcbiAgICB9XG59XG5cbmZ1bmN0aW9uIGJhcigpIHtcbiAgICByZXR1cm4geDtcbiAgICB2YXIgeDtcbn1cblxuc3dpdGNoIChmb28pIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIGJyZWFrO1xuICAgICAgICB2YXIgeDtcbn0ifQ==)

```
/*eslint no-unreachable: "error"*/

function foo() {
    return bar();
    function bar() {
        return 1;
    }
}

function bar() {
    return x;
    var x;
}

switch (foo) {
    case 1:
        break;
        var x;
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
```

Examples of additional incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGU6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEMgZXh0ZW5kcyBCIHtcbiAgICAjeDsgLy8gdW5yZWFjaGFibGVcbiAgICAjeSA9IDE7IC8vIHVucmVhY2hhYmxlXG4gICAgYTsgLy8gdW5yZWFjaGFibGVcbiAgICBiID0gMTsgLy8gdW5yZWFjaGFibGVcblxuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICByZXR1cm4ge307XG4gICAgfVxufSJ9)

```
/*eslint no-unreachable: "error"*/

class C extends B {
    #x; // unreachable
    #y = 1; // unreachable
    a; // unreachable
    b = 1; // unreachable

    constructor() {
        return {};
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
```

Examples of additional correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGU6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEQgZXh0ZW5kcyBCIHtcbiAgICAjeDtcbiAgICAjeSA9IDE7XG4gICAgYTtcbiAgICBiID0gMTtcblxuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICBzdXBlcigpO1xuICAgIH1cbn1cblxuY2xhc3MgRSBleHRlbmRzIEIge1xuICAgICN4O1xuICAgICN5ID0gMTtcbiAgICBhO1xuICAgIGIgPSAxO1xuXG4gICAgLy8gaW1wbGljaXQgY29uc3RydWN0b3IgYWx3YXlzIGNhbGxzIGBzdXBlcigpYFxufVxuXG5jbGFzcyBGIGV4dGVuZHMgQiB7XG4gICAgc3RhdGljICN4O1xuICAgIHN0YXRpYyAjeSA9IDE7XG4gICAgc3RhdGljIGE7XG4gICAgc3RhdGljIGIgPSAxO1xuXG4gICAgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIHJldHVybiB7fTtcbiAgICB9XG59In0=)

```
/*eslint no-unreachable: "error"*/

class D extends B {
    #x;
    #y = 1;
    a;
    b = 1;

    constructor() {
        super();
    }
}

class E extends B {
    #x;
    #y = 1;
    a;
    b = 1;

    // implicit constructor always calls `super()`
}

class F extends B {
    static #x;
    static #y = 1;
    static a;
    static b = 1;

    constructor() {
        return {};
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
```

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

TypeScript must be configured with [allowUnreachableCode: false](https://www.typescriptlang.org/tsconfig#allowUnreachableCode) for it to consider unreachable code an error.

## Version

This rule was introduced in ESLint v0.0.6.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unreachable.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unreachable.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unreachable.md
                    
                
                )
