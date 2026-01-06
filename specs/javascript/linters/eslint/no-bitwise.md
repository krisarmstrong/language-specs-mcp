# no-bitwise

Disallow bitwise operators

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allow](#allow)
  2. [int32Hint](#int32hint)

3. [Version](#version)
4. [Resources](#resources)

The use of bitwise operators in JavaScript is very rare and often `&` or `|` is simply a mistyped `&&` or `||`, which will lead to unexpected behavior.

```
const x = y | z;
1
```

Copy code to clipboard

## Rule Details

This rule disallows bitwise operators.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYml0d2lzZTogXCJlcnJvclwiKi9cblxubGV0IHggPSB5IHwgejtcblxuY29uc3QgeDEgPSB5ICYgejtcblxuY29uc3QgeDIgPSB5IF4gejtcblxuY29uc3QgeDMgPSB+IHo7XG5cbmNvbnN0IHg0ID0geSA8PCB6O1xuXG5jb25zdCB4NSA9IHkgPj4gejtcblxuY29uc3QgeDYgPSB5ID4+PiB6O1xuXG54IHw9IHk7XG5cbnggJj0geTtcblxueCBePSB5O1xuXG54IDw8PSB5O1xuXG54ID4+PSB5O1xuXG54ID4+Pj0geTsifQ==)

```
/*eslint no-bitwise: "error"*/

let x = y | z;

const x1 = y & z;

const x2 = y ^ z;

const x3 = ~ z;

const x4 = y << z;

const x5 = y >> z;

const x6 = y >>> z;

x |= y;

x &= y;

x ^= y;

x <<= y;

x >>= y;

x >>>= y;
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYml0d2lzZTogXCJlcnJvclwiKi9cblxubGV0IHggPSB5IHx8IHo7XG5cbmNvbnN0IHgxID0geSAmJiB6O1xuXG5jb25zdCB4MiA9IHkgPiB6O1xuXG5jb25zdCB4MyA9IHkgPCB6O1xuXG54ICs9IHk7In0=)

```
/*eslint no-bitwise: "error"*/

let x = y || z;

const x1 = y && z;

const x2 = y > z;

const x3 = y < z;

x += y;
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

## Options

This rule has an object option:

- `"allow"`: Allows a list of bitwise operators to be used as exceptions.
- `"int32Hint"`: Allows the use of bitwise OR in `|0` pattern for type casting.

### allow

Examples of correct code for this rule with the `{ "allow": ["~"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYml0d2lzZTogW1wiZXJyb3JcIiwgeyBcImFsbG93XCI6IFtcIn5cIl0gfV0gKi9cblxuflsxLDIsM10uaW5kZXhPZigxKSA9PT0gLTE7In0=)

```
/*eslint no-bitwise: ["error", { "allow": ["~"] }] */

~[1,2,3].indexOf(1) === -1;
1
2
3
```

### int32Hint

Examples of correct code for this rule with the `{ "int32Hint": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYml0d2lzZTogW1wiZXJyb3JcIiwgeyBcImludDMySGludFwiOiB0cnVlIH1dICovXG5cbmNvbnN0IGIgPSBhfDA7In0=)

```
/*eslint no-bitwise: ["error", { "int32Hint": true }] */

const b = a|0;
1
2
3
```

## Version

This rule was introduced in ESLint v0.0.2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-bitwise.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-bitwise.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-bitwise.md
                    
                
                )
