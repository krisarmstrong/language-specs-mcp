# no-ternary

Disallow ternary operators

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Resources](#resources)

The ternary operator is used to conditionally assign a value to a variable. Some believe that the use of ternary operators leads to unclear code.

```
const foo = isBar ? baz : qux;
1
```

Copy code to clipboard

## Rule Details

This rule disallows ternary operators.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGVybmFyeTogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0gaXNCYXIgPyBiYXogOiBxdXg7XG5cbmZ1bmN0aW9uIHF1dXgoKSB7XG4gIHJldHVybiBmb28gPyBiYXIoKSA6IGJheigpO1xufSJ9)

```
/*eslint no-ternary: "error"*/

const foo = isBar ? baz : qux;

function quux() {
  return foo ? bar() : baz();
}
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGVybmFyeTogXCJlcnJvclwiKi9cblxubGV0IGZvbztcblxuaWYgKGlzQmFyKSB7XG4gICAgZm9vID0gYmF6O1xufSBlbHNlIHtcbiAgICBmb28gPSBxdXg7XG59XG5cbmZ1bmN0aW9uIHF1dXgoKSB7XG4gICAgaWYgKGZvbykge1xuICAgICAgICByZXR1cm4gYmFyKCk7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgcmV0dXJuIGJheigpO1xuICAgIH1cbn0ifQ==)

```
/*eslint no-ternary: "error"*/

let foo;

if (isBar) {
    foo = baz;
} else {
    foo = qux;
}

function quux() {
    if (foo) {
        return bar();
    } else {
        return baz();
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

## Related Rules

- [no-nested-ternary](/docs/latest/rules/no-nested-ternary)
- [no-unneeded-ternary](/docs/latest/rules/no-unneeded-ternary)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-ternary.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-ternary.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-ternary.md
                    
                
                )
