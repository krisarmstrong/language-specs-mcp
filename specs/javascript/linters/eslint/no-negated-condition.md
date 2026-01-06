# no-negated-condition

Disallow negated conditions

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

Negated conditions are more difficult to understand. Code can be made more readable by inverting the condition instead.

## Rule Details

This rule disallows negated conditions in either of the following:

- `if` statements which have an `else` branch
- ternary expressions

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmVnYXRlZC1jb25kaXRpb246IFwiZXJyb3JcIiovXG5cbmlmICghYSkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IGVsc2Uge1xuICAgIGRvU29tZXRoaW5nRWxzZSgpO1xufVxuXG5pZiAoYSAhPSBiKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0gZWxzZSB7XG4gICAgZG9Tb21ldGhpbmdFbHNlKCk7XG59XG5cbmlmIChhICE9PSBiKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0gZWxzZSB7XG4gICAgZG9Tb21ldGhpbmdFbHNlKCk7XG59XG5cbiFhID8gYyA6IGIifQ==)

```
/*eslint no-negated-condition: "error"*/

if (!a) {
    doSomething();
} else {
    doSomethingElse();
}

if (a != b) {
    doSomething();
} else {
    doSomethingElse();
}

if (a !== b) {
    doSomething();
} else {
    doSomethingElse();
}

!a ? c : b
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmVnYXRlZC1jb25kaXRpb246IFwiZXJyb3JcIiovXG5cbmlmICghYSkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59XG5cbmlmICghYSkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IGVsc2UgaWYgKGIpIHtcbiAgICBkb1NvbWV0aGluZygpO1xufVxuXG5pZiAoYSAhPSBiKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuYSA/IGIgOiBjIn0=)

```
/*eslint no-negated-condition: "error"*/

if (!a) {
    doSomething();
}

if (!a) {
    doSomething();
} else if (b) {
    doSomething();
}

if (a != b) {
    doSomething();
}

a ? b : c
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

## Version

This rule was introduced in ESLint v1.6.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-negated-condition.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-negated-condition.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-negated-condition.md
                    
                
                )
