# no-param-reassign

Disallow reassigning function parameters

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [props](#props)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Assignment to variables declared as function parameters can be misleading and lead to confusing behavior, as modifying function parameters will also mutate the `arguments` object when not in `strict` mode (see [When Not To Use It](#when-not-to-use-it) below). Often, assignment to function parameters is unintended and indicative of a mistake or programmer error.

This rule can be also configured to fail when function parameters are modified. Side effects on parameters can cause counter-intuitive execution flow and make errors difficult to track down.

## Rule Details

This rule aims to prevent unintended behavior caused by modification or reassignment of function parameters.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGFyYW0tcmVhc3NpZ246IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGJhciA9IDEzO1xufVxuXG5jb25zdCBmb28xID0gZnVuY3Rpb24oYmFyKSB7XG4gICAgYmFyKys7XG59XG5cbmNvbnN0IGZvbzIgPSBmdW5jdGlvbihiYXIpIHtcbiAgICBmb3IgKGJhciBpbiBiYXopIHt9XG59XG5cbmNvbnN0IGZvbzMgPSBmdW5jdGlvbihiYXIpIHtcbiAgICBmb3IgKGJhciBvZiBiYXopIHt9XG59In0=)

```
/*eslint no-param-reassign: "error"*/

const foo = function(bar) {
    bar = 13;
}

const foo1 = function(bar) {
    bar++;
}

const foo2 = function(bar) {
    for (bar in baz) {}
}

const foo3 = function(bar) {
    for (bar of baz) {}
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGFyYW0tcmVhc3NpZ246IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGNvbnN0IGJheiA9IGJhcjtcbn0ifQ==)

```
/*eslint no-param-reassign: "error"*/

const foo = function(bar) {
    const baz = bar;
}
1
2
3
4
5
```

## Options

This rule takes one option, an object, with a boolean property `"props"`, and arrays `"ignorePropertyModificationsFor"` and `"ignorePropertyModificationsForRegex"`. `"props"` is `false` by default. If `"props"` is set to `true`, this rule warns against the modification of parameter properties unless they’re included in `"ignorePropertyModificationsFor"` or `"ignorePropertyModificationsForRegex"`, which is an empty array by default.

### props

Examples of correct code for the default `{ "props": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGFyYW0tcmVhc3NpZ246IFtcImVycm9yXCIsIHsgXCJwcm9wc1wiOiBmYWxzZSB9XSovXG5cbmNvbnN0IGZvbyA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGJhci5wcm9wID0gXCJ2YWx1ZVwiO1xufVxuXG5jb25zdCBmb28xID0gZnVuY3Rpb24oYmFyKSB7XG4gICAgZGVsZXRlIGJhci5hYWE7XG59XG5cbmNvbnN0IGZvbzIgPSBmdW5jdGlvbihiYXIpIHtcbiAgICBiYXIuYWFhKys7XG59XG5cbmNvbnN0IGZvbzMgPSBmdW5jdGlvbihiYXIpIHtcbiAgICBmb3IgKGJhci5hYWEgaW4gYmF6KSB7fVxufVxuXG5jb25zdCBmb280ID0gZnVuY3Rpb24oYmFyKSB7XG4gICAgZm9yIChiYXIuYWFhIG9mIGJheikge31cbn0ifQ==)

```
/*eslint no-param-reassign: ["error", { "props": false }]*/

const foo = function(bar) {
    bar.prop = "value";
}

const foo1 = function(bar) {
    delete bar.aaa;
}

const foo2 = function(bar) {
    bar.aaa++;
}

const foo3 = function(bar) {
    for (bar.aaa in baz) {}
}

const foo4 = function(bar) {
    for (bar.aaa of baz) {}
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

Examples of incorrect code for the `{ "props": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGFyYW0tcmVhc3NpZ246IFtcImVycm9yXCIsIHsgXCJwcm9wc1wiOiB0cnVlIH1dKi9cblxuY29uc3QgZm9vID0gZnVuY3Rpb24oYmFyKSB7XG4gICAgYmFyLnByb3AgPSBcInZhbHVlXCI7XG59XG5cbmNvbnN0IGZvbzEgPSBmdW5jdGlvbihiYXIpIHtcbiAgICBkZWxldGUgYmFyLmFhYTtcbn1cblxuY29uc3QgZm9vMiA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGJhci5hYWErKztcbn1cblxuY29uc3QgZm9vMyA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGZvciAoYmFyLmFhYSBpbiBiYXopIHt9XG59XG5cbmNvbnN0IGZvbzQgPSBmdW5jdGlvbihiYXIpIHtcbiAgICBmb3IgKGJhci5hYWEgb2YgYmF6KSB7fVxufSJ9)

```
/*eslint no-param-reassign: ["error", { "props": true }]*/

const foo = function(bar) {
    bar.prop = "value";
}

const foo1 = function(bar) {
    delete bar.aaa;
}

const foo2 = function(bar) {
    bar.aaa++;
}

const foo3 = function(bar) {
    for (bar.aaa in baz) {}
}

const foo4 = function(bar) {
    for (bar.aaa of baz) {}
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

Examples of correct code for the `{ "props": true }` option with `"ignorePropertyModificationsFor"` set:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGFyYW0tcmVhc3NpZ246IFtcImVycm9yXCIsIHsgXCJwcm9wc1wiOiB0cnVlLCBcImlnbm9yZVByb3BlcnR5TW9kaWZpY2F0aW9uc0ZvclwiOiBbXCJiYXJcIl0gfV0qL1xuXG5jb25zdCBmb28gPSBmdW5jdGlvbihiYXIpIHtcbiAgICBiYXIucHJvcCA9IFwidmFsdWVcIjtcbn1cblxuY29uc3QgZm9vMSA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGRlbGV0ZSBiYXIuYWFhO1xufVxuXG5jb25zdCBmb28yID0gZnVuY3Rpb24oYmFyKSB7XG4gICAgYmFyLmFhYSsrO1xufVxuXG5jb25zdCBmb28zID0gZnVuY3Rpb24oYmFyKSB7XG4gICAgZm9yIChiYXIuYWFhIGluIGJheikge31cbn1cblxuY29uc3QgZm9vNCA9IGZ1bmN0aW9uKGJhcikge1xuICAgIGZvciAoYmFyLmFhYSBvZiBiYXopIHt9XG59In0=)

```
/*eslint no-param-reassign: ["error", { "props": true, "ignorePropertyModificationsFor": ["bar"] }]*/

const foo = function(bar) {
    bar.prop = "value";
}

const foo1 = function(bar) {
    delete bar.aaa;
}

const foo2 = function(bar) {
    bar.aaa++;
}

const foo3 = function(bar) {
    for (bar.aaa in baz) {}
}

const foo4 = function(bar) {
    for (bar.aaa of baz) {}
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

Examples of correct code for the `{ "props": true }` option with `"ignorePropertyModificationsForRegex"` set:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGFyYW0tcmVhc3NpZ246IFtcImVycm9yXCIsIHsgXCJwcm9wc1wiOiB0cnVlLCBcImlnbm9yZVByb3BlcnR5TW9kaWZpY2F0aW9uc0ZvclJlZ2V4XCI6IFtcIl5iYXJcIl0gfV0qL1xuXG5jb25zdCBmb28gPSBmdW5jdGlvbihiYXJWYXIpIHtcbiAgICBiYXJWYXIucHJvcCA9IFwidmFsdWVcIjtcbn1cblxuY29uc3QgZm9vMSA9IGZ1bmN0aW9uKGJhcnJpdG8pIHtcbiAgICBkZWxldGUgYmFycml0by5hYWE7XG59XG5cbmNvbnN0IGZvbzIgPSBmdW5jdGlvbihiYXJfKSB7XG4gICAgYmFyXy5hYWErKztcbn1cblxuY29uc3QgZm9vMyA9IGZ1bmN0aW9uKGJhckJheikge1xuICAgIGZvciAoYmFyQmF6LmFhYSBpbiBiYXopIHt9XG59XG5cbmNvbnN0IGZvbzQgPSBmdW5jdGlvbihiYXJCYXopIHtcbiAgICBmb3IgKGJhckJhei5hYWEgb2YgYmF6KSB7fVxufSJ9)

```
/*eslint no-param-reassign: ["error", { "props": true, "ignorePropertyModificationsForRegex": ["^bar"] }]*/

const foo = function(barVar) {
    barVar.prop = "value";
}

const foo1 = function(barrito) {
    delete barrito.aaa;
}

const foo2 = function(bar_) {
    bar_.aaa++;
}

const foo3 = function(barBaz) {
    for (barBaz.aaa in baz) {}
}

const foo4 = function(barBaz) {
    for (barBaz.aaa of baz) {}
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

## When Not To Use It

If you want to allow assignment to function parameters, then you can safely disable this rule.

`strict` mode code doesn’t sync indices of the arguments object with each parameter binding. Therefore, this rule is not necessary to protect against arguments object mutation in ESM modules or other `strict` mode functions.

## Version

This rule was introduced in ESLint v0.18.0.

## Further Reading

[JavaScript: Don’t Reassign Your Function Arguments](https://spin.atomicobject.com/2011/04/10/javascript-don-t-reassign-your-function-arguments/)
 spin.atomicobject.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-param-reassign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-param-reassign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-param-reassign.md
                    
                
                )
