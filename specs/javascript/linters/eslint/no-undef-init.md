# no-undef-init

Disallow initializing variables to `undefined`

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

In JavaScript, a variable that is declared and not initialized to any value automatically gets the value of `undefined`. For example:

```
var foo;

console.log(foo === undefined);     // true
1
2
3
```

Copy code to clipboard

It’s therefore unnecessary to initialize a variable to `undefined`, such as:

```
var foo = undefined;
1
```

Copy code to clipboard

It’s considered a best practice to avoid initializing variables to `undefined`.

## Rule Details

This rule aims to eliminate `var` and `let` variable declarations that initialize to `undefined`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWYtaW5pdDogXCJlcnJvclwiKi9cblxudmFyIGZvbyA9IHVuZGVmaW5lZDtcbmxldCBiYXIgPSB1bmRlZmluZWQ7In0=)

```
/*eslint no-undef-init: "error"*/

var foo = undefined;
let bar = undefined;
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWYtaW5pdDogXCJlcnJvclwiKi9cblxudmFyIGZvbztcbmxldCBiYXI7In0=)

```
/*eslint no-undef-init: "error"*/

var foo;
let bar;
1
2
3
4
```

Please note that this rule does not check `const` declarations, `using` declarations, `await using` declarations, destructuring patterns, function parameters, and class fields.

Examples of additional correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWYtaW5pdDogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0gdW5kZWZpbmVkO1xuXG51c2luZyBmb28xID0gdW5kZWZpbmVkO1xuXG5hd2FpdCB1c2luZyBmb28yID0gdW5kZWZpbmVkO1xuXG5sZXQgeyBiYXIgPSB1bmRlZmluZWQgfSA9IGJhejtcblxuW3F1dXggPSB1bmRlZmluZWRdID0gcXV1dXg7XG5cbihmb28gPSB1bmRlZmluZWQpID0+IHt9O1xuXG5jbGFzcyBGb28ge1xuICAgIGJhciA9IHVuZGVmaW5lZDtcbn0ifQ==)

```
/*eslint no-undef-init: "error"*/

const foo = undefined;

using foo1 = undefined;

await using foo2 = undefined;

let { bar = undefined } = baz;

[quux = undefined] = quuux;

(foo = undefined) => {};

class Foo {
    bar = undefined;
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

## When Not To Use It

There are situations where initializing to `undefined` behaves differently than omitting the initialization.

One such case is when a `var` declaration occurs inside of a loop. For example:

Example of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWYtaW5pdDogXCJlcnJvclwiKi9cblxuZm9yIChpID0gMDsgaSA8IDEwOyBpKyspIHtcbiAgICB2YXIgeCA9IHVuZGVmaW5lZDtcbiAgICBjb25zb2xlLmxvZyh4KTtcbiAgICB4ID0gaTtcbn0ifQ==)

```
/*eslint no-undef-init: "error"*/

for (i = 0; i < 10; i++) {
    var x = undefined;
    console.log(x);
    x = i;
}
1
2
3
4
5
6
7
```

In this case, the `var x` is hoisted out of the loop, effectively creating:

```
var x;

for (i = 0; i < 10; i++) {
    x = undefined;
    console.log(x);
    x = i;
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

If you were to remove the initialization, then the behavior of the loop changes:

```
for (i = 0; i < 10; i++) {
    var x;
    console.log(x);
    x = i;
}
1
2
3
4
5
```

Copy code to clipboard

This code is equivalent to:

```
var x;

for (i = 0; i < 10; i++) {
    console.log(x);
    x = i;
}
1
2
3
4
5
6
```

Copy code to clipboard

This produces a different outcome than defining `var x = undefined` in the loop, as `x` is no longer reset to `undefined` each time through the loop.

If you’re using such an initialization inside of a loop, then you should disable this rule.

Example of correct code for this rule, because it is disabled on a specific line:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWYtaW5pdDogXCJlcnJvclwiKi9cblxuZm9yIChpID0gMDsgaSA8IDEwOyBpKyspIHtcbiAgICB2YXIgeCA9IHVuZGVmaW5lZDsgLy8gZXNsaW50LWRpc2FibGUtbGluZSBuby11bmRlZi1pbml0XG4gICAgY29uc29sZS5sb2coeCk7XG4gICAgeCA9IGk7XG59In0=)

```
/*eslint no-undef-init: "error"*/

for (i = 0; i < 10; i++) {
    var x = undefined; // eslint-disable-line no-undef-init
    console.log(x);
    x = i;
}
1
2
3
4
5
6
7
```

Another such case is when a variable is redeclared using `var`. For example:

```
function foo() {
    var x = 1;
    console.log(x); // output: 1

    var x;
    console.log(x); // output: 1

    var x = undefined;
    console.log(x); // output: undefined
}

foo();
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

Copy code to clipboard

In this case, you can avoid redeclaration by changing it to an assignment (`x = undefined;`), or use an eslint disable comment on a specific line.

## Related Rules

- [no-undefined](/docs/latest/rules/no-undefined)
- [no-void](/docs/latest/rules/no-void)

## Version

This rule was introduced in ESLint v0.0.6.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-undef-init.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-undef-init.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-undef-init.md
                    
                
                )
