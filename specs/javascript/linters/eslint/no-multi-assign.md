# no-multi-assign

Disallow use of chained assignment expressions

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [ignoreNonDeclaration](#ignorenondeclaration)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Chaining the assignment of variables can lead to unexpected results and be difficult to read.

```
(function() {
    const foo = bar = 0; // Did you mean `foo = bar == 0`?
    bar = 1;             // This will not fail since `bar` is not constant.
})();
console.log(bar);        // This will output 1 since `bar` is not scoped.
1
2
3
4
5
```

Copy code to clipboard

## Rule Details

This rule disallows using multiple assignments within a single statement.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbXVsdGktYXNzaWduOiBcImVycm9yXCIqL1xuXG5sZXQgYSA9IGIgPSBjID0gNTtcblxuY29uc3QgZm9vID0gYmFyID0gXCJiYXpcIjtcblxubGV0IGQgPVxuICAgIGUgPVxuICAgIGM7XG5cbmNsYXNzIEZvbyB7XG4gICAgYSA9IGIgPSAxMDtcbn1cblxuYSA9IGIgPSBcInF1dXhcIjsifQ==)

```
/*eslint no-multi-assign: "error"*/

let a = b = c = 5;

const foo = bar = "baz";

let d =
    e =
    c;

class Foo {
    a = b = 10;
}

a = b = "quux";
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbXVsdGktYXNzaWduOiBcImVycm9yXCIqL1xuXG5sZXQgYSA9IDU7XG5sZXQgYiA9IDU7XG5jb25zdCBjID0gNTtcblxuY29uc3QgZm9vID0gXCJiYXpcIjtcbmNvbnN0IGJhciA9IFwiYmF6XCI7XG5cbmxldCBkID0gYztcbmxldCBlID0gYztcblxuY2xhc3MgRm9vIHtcbiAgICBhID0gMTA7XG4gICAgYiA9IDEwO1xufVxuXG5hID0gXCJxdXV4XCI7XG5iID0gXCJxdXV4XCI7In0=)

```
/*eslint no-multi-assign: "error"*/

let a = 5;
let b = 5;
const c = 5;

const foo = "baz";
const bar = "baz";

let d = c;
let e = c;

class Foo {
    a = 10;
    b = 10;
}

a = "quux";
b = "quux";
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

## Options

This rule has an object option:

- `"ignoreNonDeclaration"`: When set to `true`, the rule allows chains that don’t include initializing a variable in a declaration or initializing a class field. Default is `false`.

### ignoreNonDeclaration

Examples of correct code for the `{ "ignoreNonDeclaration": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbXVsdGktYXNzaWduOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTm9uRGVjbGFyYXRpb25cIjogdHJ1ZSB9XSovXG5cbmxldCBhO1xubGV0IGI7XG5hID0gYiA9IFwiYmF6XCI7XG5cbmNvbnN0IHggPSB7fTtcbmNvbnN0IHkgPSB7fTtcbngub25lID0geS5vbmUgPSAxOyJ9)

```
/*eslint no-multi-assign: ["error", { "ignoreNonDeclaration": true }]*/

let a;
let b;
a = b = "baz";

const x = {};
const y = {};
x.one = y.one = 1;
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

Examples of incorrect code for the `{ "ignoreNonDeclaration": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbXVsdGktYXNzaWduOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTm9uRGVjbGFyYXRpb25cIjogdHJ1ZSB9XSovXG5cbmxldCBhID0gYiA9IFwiYmF6XCI7XG5cbmNvbnN0IGZvbyA9IGJhciA9IDE7XG5cbmNsYXNzIEZvbyB7XG4gICAgYSA9IGIgPSAxMDtcbn0ifQ==)

```
/*eslint no-multi-assign: ["error", { "ignoreNonDeclaration": true }]*/

let a = b = "baz";

const foo = bar = 1;

class Foo {
    a = b = 10;
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
```

## Related Rules

- [max-statements-per-line](/docs/latest/rules/max-statements-per-line)

## Version

This rule was introduced in ESLint v3.14.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-multi-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-multi-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-multi-assign.md
                    
                
                )
