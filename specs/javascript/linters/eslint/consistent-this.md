# consistent-this

Enforce consistent naming when capturing the current execution context

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

It is often necessary to capture the current execution context in order to make it available subsequently. A prominent example of this are jQuery callbacks:

```
const that = this;
jQuery('li').click(function (event) {
    // here, "this" is the HTMLElement where the click event occurred
    that.setFoo(42);
});
1
2
3
4
5
```

Copy code to clipboard

There are many commonly used aliases for `this` such as `that`, `self` or `me`. It is desirable to ensure that whichever alias the team agrees upon is used consistently throughout the application.

## Rule Details

This rule enforces two things about variables with the designated alias names for `this`:

- If a variable with a designated name is declared, it must be either initialized (in the declaration) or assigned (in the same scope as the declaration) the value `this`.
- If a variable is initialized or assigned the value `this`, the name of the variable must be a designated alias.

## Options

This rule has one or more string options:

- designated alias names for `this` (default `"that"`)

Examples of incorrect code for this rule with the default `"that"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC10aGlzOiBbXCJlcnJvclwiLCBcInRoYXRcIl0qL1xuXG5sZXQgdGhhdCA9IDQyO1xuXG5sZXQgc2VsZiA9IHRoaXM7XG5cbnRoYXQgPSA0Mjtcblxuc2VsZiA9IHRoaXM7In0=)

```
/*eslint consistent-this: ["error", "that"]*/

let that = 42;

let self = this;

that = 42;

self = this;
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

Examples of correct code for this rule with the default `"that"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC10aGlzOiBbXCJlcnJvclwiLCBcInRoYXRcIl0qL1xuXG5sZXQgdGhhdCA9IHRoaXM7XG5cbmNvbnN0IHNlbGYgPSA0MjtcblxubGV0IGZvbztcblxudGhhdCA9IHRoaXM7XG5cbmZvby5iYXIgPSB0aGlzOyJ9)

```
/*eslint consistent-this: ["error", "that"]*/

let that = this;

const self = 42;

let foo;

that = this;

foo.bar = this;
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

Examples of incorrect code for this rule with the default `"that"` option, if the variable is not initialized:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC10aGlzOiBbXCJlcnJvclwiLCBcInRoYXRcIl0qL1xuXG5sZXQgdGhhdDtcbmZ1bmN0aW9uIGYoKSB7XG4gICAgdGhhdCA9IHRoaXM7XG59In0=)

```
/*eslint consistent-this: ["error", "that"]*/

let that;
function f() {
    that = this;
}
1
2
3
4
5
6
```

Examples of correct code for this rule with the default `"that"` option, if the variable is not initialized:

Declaring a variable `that` and assigning `this` to it.

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC10aGlzOiBbXCJlcnJvclwiLCBcInRoYXRcIl0qL1xuXG5sZXQgdGhhdDtcbnRoYXQgPSB0aGlzOyJ9)

```
/*eslint consistent-this: ["error", "that"]*/

let that;
that = this;
1
2
3
4
```

Declaring two variables, `foo` and `that`, with `foo` initialized, and then assigning `this` to `that`.

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC10aGlzOiBbXCJlcnJvclwiLCBcInRoYXRcIl0qL1xuXG5sZXQgZm9vID0gNDIsIHRoYXQ7XG50aGF0ID0gdGhpczsifQ==)

```
/*eslint consistent-this: ["error", "that"]*/

let foo = 42, that;
that = this;
1
2
3
4
```

## When Not To Use It

If you need to capture nested context, `consistent-this` is going to be problematic. Code of that nature is usually difficult to read and maintain and you should consider refactoring it.

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/consistent-this.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/consistent-this.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/consistent-this.md
                    
                
                )
