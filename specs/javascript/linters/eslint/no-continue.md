# no-continue

Disallow `continue` statements

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Compatibility](#compatibility)
3. [Version](#version)
4. [Resources](#resources)

The `continue` statement terminates execution of the statements in the current iteration of the current or labeled loop, and continues execution of the loop with the next iteration. When used incorrectly it makes code less testable, less readable and less maintainable. Structured control flow statements such as `if` should be used instead.

```
let sum = 0,
    i;

for(i = 0; i < 10; i++) {
    if(i >= 5) {
        continue;
    }

    sum += i;
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

## Rule Details

This rule disallows `continue` statements.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29udGludWU6IFwiZXJyb3JcIiovXG5cbmxldCBzdW0gPSAwLFxuICAgIGk7XG5cbmZvcihpID0gMDsgaSA8IDEwOyBpKyspIHtcbiAgICBpZihpID49IDUpIHtcbiAgICAgICAgY29udGludWU7XG4gICAgfVxuXG4gICAgc3VtICs9IGk7XG59In0=)

```
/*eslint no-continue: "error"*/

let sum = 0,
    i;

for(i = 0; i < 10; i++) {
    if(i >= 5) {
        continue;
    }

    sum += i;
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29udGludWU6IFwiZXJyb3JcIiovXG5cbmxldCBzdW0gPSAwLFxuICAgIGk7XG5cbmxhYmVsZWRMb29wOiBmb3IoaSA9IDA7IGkgPCAxMDsgaSsrKSB7XG4gICAgaWYoaSA+PSA1KSB7XG4gICAgICAgIGNvbnRpbnVlIGxhYmVsZWRMb29wO1xuICAgIH1cblxuICAgIHN1bSArPSBpO1xufSJ9)

```
/*eslint no-continue: "error"*/

let sum = 0,
    i;

labeledLoop: for(i = 0; i < 10; i++) {
    if(i >= 5) {
        continue labeledLoop;
    }

    sum += i;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29udGludWU6IFwiZXJyb3JcIiovXG5cbmxldCBzdW0gPSAwLFxuICAgIGk7XG5cbmZvcihpID0gMDsgaSA8IDEwOyBpKyspIHtcbiAgICBpZihpIDwgNSkge1xuICAgICAgIHN1bSArPSBpO1xuICAgIH1cbn0ifQ==)

```
/*eslint no-continue: "error"*/

let sum = 0,
    i;

for(i = 0; i < 10; i++) {
    if(i < 5) {
       sum += i;
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
```

## Compatibility

- JSLint: `continue`

## Version

This rule was introduced in ESLint v0.19.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-continue.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-continue.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-continue.md
                    
                
                )
