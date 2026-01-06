# for-direction

Enforce `for` loop update clause moving the counter in the right direction

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

A `for` loop with a stop condition that can never be reached, such as one with a counter that moves in the wrong direction, will run infinitely. While there are occasions when an infinite loop is intended, the convention is to construct such loops as `while` loops. More typically, an infinite `for` loop is a bug.

## Rule Details

This rule forbids `for` loops where the counter variable changes in such a way that the stop condition will never be met. For example, if the counter variable is increasing (i.e. `i++`) and the stop condition tests that the counter is greater than zero (`i >= 0`) then the loop will never exit.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZm9yLWRpcmVjdGlvbjogXCJlcnJvclwiKi9cbmZvciAobGV0IGkgPSAwOyBpIDwgMTA7IGktLSkge1xufVxuXG5mb3IgKGxldCBpID0gMTA7IGkgPj0gMDsgaSsrKSB7XG59XG5cbmZvciAobGV0IGkgPSAwOyBpID4gMTA7IGkrKykge1xufVxuXG5mb3IgKGxldCBpID0gMDsgMTAgPiBpOyBpLS0pIHtcbn1cblxuY29uc3QgbiA9IC0yO1xuZm9yIChsZXQgaSA9IDA7IGkgPCAxMDsgaSArPSBuKSB7XG59In0=)

```
/*eslint for-direction: "error"*/
for (let i = 0; i < 10; i--) {
}

for (let i = 10; i >= 0; i++) {
}

for (let i = 0; i > 10; i++) {
}

for (let i = 0; 10 > i; i--) {
}

const n = -2;
for (let i = 0; i < 10; i += n) {
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZm9yLWRpcmVjdGlvbjogXCJlcnJvclwiKi9cbmZvciAobGV0IGkgPSAwOyBpIDwgMTA7IGkrKykge1xufVxuXG5mb3IgKGxldCBpID0gMDsgMTAgPiBpOyBpKyspIHsgLy8gd2l0aCBjb3VudGVyIFwiaVwiIG9uIHRoZSByaWdodFxufVxuXG5mb3IgKGxldCBpID0gMTA7IGkgPj0gMDsgaSArPSB0aGlzLnN0ZXApIHsgLy8gZGlyZWN0aW9uIHVua25vd25cbn1cblxuZm9yIChsZXQgaSA9IE1JTjsgaSA8PSBNQVg7IGkgLT0gMCkgeyAvLyBub3QgaW5jcmVhc2luZyBvciBkZWNyZWFzaW5nXG59In0=)

```
/*eslint for-direction: "error"*/
for (let i = 0; i < 10; i++) {
}

for (let i = 0; 10 > i; i++) { // with counter "i" on the right
}

for (let i = 10; i >= 0; i += this.step) { // direction unknown
}

for (let i = MIN; i <= MAX; i -= 0) { // not increasing or decreasing
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

## Version

This rule was introduced in ESLint v4.0.0-beta.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/for-direction.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/for-direction.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/for-direction.md
                    
                
                )
