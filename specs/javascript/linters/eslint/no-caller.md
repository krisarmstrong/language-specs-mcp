# no-caller

Disallow the use of `arguments.caller` or `arguments.callee`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

The use of `arguments.caller` and `arguments.callee` make several code optimizations impossible. They have been deprecated in future versions of JavaScript and their use is forbidden in ECMAScript 5 while in strict mode.

```
function foo() {
    const callee = arguments.callee;
}
1
2
3
```

Copy code to clipboard

## Rule Details

This rule is aimed at discouraging the use of deprecated and sub-optimal code by disallowing the use of `arguments.caller` and `arguments.callee`. As such, it will warn when `arguments.caller` and `arguments.callee` are used.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2FsbGVyOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBmb28obikge1xuICAgIGlmIChuIDw9IDApIHtcbiAgICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGFyZ3VtZW50cy5jYWxsZWUobiAtIDEpO1xufVxuXG5bMSwyLDMsNCw1XS5tYXAoZnVuY3Rpb24obikge1xuICAgIHJldHVybiAhKG4gPiAxKSA/IDEgOiBhcmd1bWVudHMuY2FsbGVlKG4gLSAxKSAqIG47XG59KTsifQ==)

```
/*eslint no-caller: "error"*/

function foo(n) {
    if (n <= 0) {
        return;
    }

    arguments.callee(n - 1);
}

[1,2,3,4,5].map(function(n) {
    return !(n > 1) ? 1 : arguments.callee(n - 1) * n;
});
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2FsbGVyOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBmb28obikge1xuICAgIGlmIChuIDw9IDApIHtcbiAgICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGZvbyhuIC0gMSk7XG59XG5cblsxLDIsMyw0LDVdLm1hcChmdW5jdGlvbiBmYWN0b3JpYWwobikge1xuICAgIHJldHVybiAhKG4gPiAxKSA/IDEgOiBmYWN0b3JpYWwobiAtIDEpICogbjtcbn0pOyJ9)

```
/*eslint no-caller: "error"*/

function foo(n) {
    if (n <= 0) {
        return;
    }

    foo(n - 1);
}

[1,2,3,4,5].map(function factorial(n) {
    return !(n > 1) ? 1 : factorial(n - 1) * n;
});
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

## Version

This rule was introduced in ESLint v0.0.6.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-caller.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-caller.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-caller.md
                    
                
                )
