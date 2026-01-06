# no-loss-of-precision

Disallow literal numbers that lose precision

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

This rule would disallow the use of number literals that lose precision at runtime when converted to a JS `Number` due to 64-bit floating-point rounding.

## Rule Details

In JS, `Number`s are stored as double-precision floating-point numbers according to the [IEEE 754 standard](https://en.wikipedia.org/wiki/IEEE_754). Because of this, numbers can only retain accuracy up to a certain amount of digits. If the programmer enters additional digits, those digits will be lost in the conversion to the `Number` type and will result in unexpected behavior.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9zcy1vZi1wcmVjaXNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSA5MDA3MTk5MjU0NzQwOTkzXG5jb25zdCBiID0gNTEyMzAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMVxuY29uc3QgYyA9IDEyMzAwMDAwMDAwMDAwMDAwMDAwMDAwMDAuMFxuY29uc3QgZCA9IC4xMjMwMDAwMDAwMDAwMDAwMDAwMDAwMDAwXG5jb25zdCBlID0gMFgyMDAwMDAwMDAwMDAwMVxuY29uc3QgZiA9IDBYMl8wMDAwMDAwMDBfMDAwMTsifQ==)

```
/*eslint no-loss-of-precision: "error"*/

const a = 9007199254740993
const b = 5123000000000000000000000000001
const c = 1230000000000000000000000.0
const d = .1230000000000000000000000
const e = 0X20000000000001
const f = 0X2_000000000_0001;
1
2
3
4
5
6
7
8
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9zcy1vZi1wcmVjaXNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSAxMjM0NVxuY29uc3QgYiA9IDEyMy40NTZcbmNvbnN0IGMgPSAxMjNlMzRcbmNvbnN0IGQgPSAxMjMwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMFxuY29uc3QgZSA9IDB4MUZGRkZGRkZGRkZGRkZcbmNvbnN0IGYgPSA5MDA3MTk5MjU0NzQwOTkxXG5jb25zdCBnID0gOTAwN18xOTkyNTQ3NDA5XzkxIn0=)

```
/*eslint no-loss-of-precision: "error"*/

const a = 12345
const b = 123.456
const c = 123e34
const d = 12300000000000000000000000
const e = 0x1FFFFFFFFFFFFF
const f = 9007199254740991
const g = 9007_1992547409_91
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

## Version

This rule was introduced in ESLint v7.1.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-loss-of-precision.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-loss-of-precision.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-loss-of-precision.md
                    
                
                )
