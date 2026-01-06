# max-statements

Enforce a maximum number of statements allowed in function blocks

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [max](#max)
  2. [ignoreTopLevelFunctions](#ignoretoplevelfunctions)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

The `max-statements` rule allows you to specify the maximum number of statements allowed in a function.

```
function foo() {
  const bar = 1; // one statement
  const baz = 2; // two statements
  const qux = 3; // three statements
}
1
2
3
4
5
```

Copy code to clipboard

## Rule Details

This rule enforces a maximum number of statements allowed in function blocks.

## Options

This rule has a number or object option:

- `"max"` (default `10`) enforces a maximum number of statements allows in function blocks

Deprecated: The object property `maximum` is deprecated; please use the object property `max` instead.

This rule has an object option:

- `"ignoreTopLevelFunctions": true` ignores top-level functions

### max

Examples of incorrect code for this rule with the default `{ "max": 10 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LXN0YXRlbWVudHM6IFtcImVycm9yXCIsIDEwXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgY29uc3QgZm9vMSA9IDE7XG4gIGNvbnN0IGZvbzIgPSAyO1xuICBjb25zdCBmb28zID0gMztcbiAgY29uc3QgZm9vNCA9IDQ7XG4gIGNvbnN0IGZvbzUgPSA1O1xuICBjb25zdCBmb282ID0gNjtcbiAgY29uc3QgZm9vNyA9IDc7XG4gIGNvbnN0IGZvbzggPSA4O1xuICBjb25zdCBmb285ID0gOTtcbiAgY29uc3QgZm9vMTAgPSAxMDtcblxuICBjb25zdCBmb28xMSA9IDExOyAvLyBUb28gbWFueS5cbn1cblxuY29uc3QgYmFyID0gKCkgPT4ge1xuICBjb25zdCBmb28xID0gMTtcbiAgY29uc3QgZm9vMiA9IDI7XG4gIGNvbnN0IGZvbzMgPSAzO1xuICBjb25zdCBmb280ID0gNDtcbiAgY29uc3QgZm9vNSA9IDU7XG4gIGNvbnN0IGZvbzYgPSA2O1xuICBjb25zdCBmb283ID0gNztcbiAgY29uc3QgZm9vOCA9IDg7XG4gIGNvbnN0IGZvbzkgPSA5O1xuICBjb25zdCBmb28xMCA9IDEwO1xuXG4gIGNvbnN0IGZvbzExID0gMTE7IC8vIFRvbyBtYW55LlxufTsifQ==)

```
/*eslint max-statements: ["error", 10]*/

function foo() {
  const foo1 = 1;
  const foo2 = 2;
  const foo3 = 3;
  const foo4 = 4;
  const foo5 = 5;
  const foo6 = 6;
  const foo7 = 7;
  const foo8 = 8;
  const foo9 = 9;
  const foo10 = 10;

  const foo11 = 11; // Too many.
}

const bar = () => {
  const foo1 = 1;
  const foo2 = 2;
  const foo3 = 3;
  const foo4 = 4;
  const foo5 = 5;
  const foo6 = 6;
  const foo7 = 7;
  const foo8 = 8;
  const foo9 = 9;
  const foo10 = 10;

  const foo11 = 11; // Too many.
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

Examples of correct code for this rule with the default `{ "max": 10 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LXN0YXRlbWVudHM6IFtcImVycm9yXCIsIDEwXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgY29uc3QgZm9vMSA9IDE7XG4gIGNvbnN0IGZvbzIgPSAyO1xuICBjb25zdCBmb28zID0gMztcbiAgY29uc3QgZm9vNCA9IDQ7XG4gIGNvbnN0IGZvbzUgPSA1O1xuICBjb25zdCBmb282ID0gNjtcbiAgY29uc3QgZm9vNyA9IDc7XG4gIGNvbnN0IGZvbzggPSA4O1xuICBjb25zdCBmb285ID0gOTtcbiAgcmV0dXJuIGZ1bmN0aW9uICgpIHsgLy8gMTBcblxuICAgIC8vIFRoZSBudW1iZXIgb2Ygc3RhdGVtZW50cyBpbiB0aGUgaW5uZXIgZnVuY3Rpb24gZG9lcyBub3QgY291bnQgdG93YXJkIHRoZVxuICAgIC8vIHN0YXRlbWVudCBtYXhpbXVtLlxuXG4gICAgbGV0IGJhcjtcbiAgICBsZXQgYmF6O1xuICAgIHJldHVybiA0MjtcbiAgfTtcbn1cblxuY29uc3QgYmFyID0gKCkgPT4ge1xuICBjb25zdCBmb28xID0gMTtcbiAgY29uc3QgZm9vMiA9IDI7XG4gIGNvbnN0IGZvbzMgPSAzO1xuICBjb25zdCBmb280ID0gNDtcbiAgY29uc3QgZm9vNSA9IDU7XG4gIGNvbnN0IGZvbzYgPSA2O1xuICBjb25zdCBmb283ID0gNztcbiAgY29uc3QgZm9vOCA9IDg7XG4gIGNvbnN0IGZvbzkgPSA5O1xuICByZXR1cm4gZnVuY3Rpb24gKCkgeyAvLyAxMFxuXG4gICAgLy8gVGhlIG51bWJlciBvZiBzdGF0ZW1lbnRzIGluIHRoZSBpbm5lciBmdW5jdGlvbiBkb2VzIG5vdCBjb3VudCB0b3dhcmQgdGhlXG4gICAgLy8gc3RhdGVtZW50IG1heGltdW0uXG5cbiAgICBsZXQgYmFyO1xuICAgIGxldCBiYXo7XG4gICAgcmV0dXJuIDQyO1xuICB9O1xufSJ9)

```
/*eslint max-statements: ["error", 10]*/

function foo() {
  const foo1 = 1;
  const foo2 = 2;
  const foo3 = 3;
  const foo4 = 4;
  const foo5 = 5;
  const foo6 = 6;
  const foo7 = 7;
  const foo8 = 8;
  const foo9 = 9;
  return function () { // 10

    // The number of statements in the inner function does not count toward the
    // statement maximum.

    let bar;
    let baz;
    return 42;
  };
}

const bar = () => {
  const foo1 = 1;
  const foo2 = 2;
  const foo3 = 3;
  const foo4 = 4;
  const foo5 = 5;
  const foo6 = 6;
  const foo7 = 7;
  const foo8 = 8;
  const foo9 = 9;
  return function () { // 10

    // The number of statements in the inner function does not count toward the
    // statement maximum.

    let bar;
    let baz;
    return 42;
  };
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
```

Note that this rule does not apply to class static blocks, and that statements in class static blocks do not count as statements in the enclosing function.

Examples of correct code for this rule with `{ "max": 2 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LXN0YXRlbWVudHM6IFtcImVycm9yXCIsIDJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIGxldCBvbmU7XG4gICAgbGV0IHR3byA9IGNsYXNzIHtcbiAgICAgICAgc3RhdGljIHtcbiAgICAgICAgICAgIGxldCB0aHJlZTtcbiAgICAgICAgICAgIGxldCBmb3VyO1xuICAgICAgICAgICAgbGV0IGZpdmU7XG4gICAgICAgICAgICBpZiAoc2l4KSB7XG4gICAgICAgICAgICAgICAgbGV0IHNldmVuO1xuICAgICAgICAgICAgICAgIGxldCBlaWdodDtcbiAgICAgICAgICAgICAgICBsZXQgbmluZTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH07XG59In0=)

```
/*eslint max-statements: ["error", 2]*/

function foo() {
    let one;
    let two = class {
        static {
            let three;
            let four;
            let five;
            if (six) {
                let seven;
                let eight;
                let nine;
            }
        }
    };
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

### ignoreTopLevelFunctions

Examples of additional correct code for this rule with the `{ "max": 10 }, { "ignoreTopLevelFunctions": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LXN0YXRlbWVudHM6IFtcImVycm9yXCIsIDEwLCB7IFwiaWdub3JlVG9wTGV2ZWxGdW5jdGlvbnNcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgY29uc3QgZm9vMSA9IDE7XG4gIGNvbnN0IGZvbzIgPSAyO1xuICBjb25zdCBmb28zID0gMztcbiAgY29uc3QgZm9vNCA9IDQ7XG4gIGNvbnN0IGZvbzUgPSA1O1xuICBjb25zdCBmb282ID0gNjtcbiAgY29uc3QgZm9vNyA9IDc7XG4gIGNvbnN0IGZvbzggPSA4O1xuICBjb25zdCBmb285ID0gOTtcbiAgY29uc3QgZm9vMTAgPSAxMDtcbiAgY29uc3QgZm9vMTEgPSAxMTtcbn0ifQ==)

```
/*eslint max-statements: ["error", 10, { "ignoreTopLevelFunctions": true }]*/

function foo() {
  const foo1 = 1;
  const foo2 = 2;
  const foo3 = 3;
  const foo4 = 4;
  const foo5 = 5;
  const foo6 = 6;
  const foo7 = 7;
  const foo8 = 8;
  const foo9 = 9;
  const foo10 = 10;
  const foo11 = 11;
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
```

## Related Rules

- [complexity](/docs/latest/rules/complexity)
- [max-depth](/docs/latest/rules/max-depth)
- [max-len](/docs/latest/rules/max-len)
- [max-lines](/docs/latest/rules/max-lines)
- [max-lines-per-function](/docs/latest/rules/max-lines-per-function)
- [max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)
- [max-params](/docs/latest/rules/max-params)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-statements.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-statements.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-statements.md
                    
                
                )
