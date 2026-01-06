# operator-assignment

Require or disallow assignment operator shorthand where possible

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [never](#never)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

JavaScript provides shorthand operators that combine variable assignment and some simple mathematical operations. For example, `x = x + 4` can be shortened to `x += 4`. The supported shorthand forms are as follows:

```
 Shorthand | Separate
-----------|------------
 x += y    | x = x + y
 x -= y    | x = x - y
 x *= y    | x = x * y
 x /= y    | x = x / y
 x %= y    | x = x % y
 x **= y   | x = x ** y
 x <<= y   | x = x << y
 x >>= y   | x = x >> y
 x >>>= y  | x = x >>> y
 x &= y    | x = x & y
 x ^= y    | x = x ^ y
 x |= y    | x = x | y
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
```

Copy code to clipboard

## Rule Details

This rule requires or disallows assignment operator shorthand where possible.

The rule applies to the operators listed in the above table. It does not report the logical assignment operators `&&=`, `||=`, and `??=` because their short-circuiting behavior is different from the other assignment operators.

## Options

This rule has a single string option:

- `"always"` (default) requires assignment operator shorthand where possible
- `"never"` disallows assignment operator shorthand

### always

Examples of incorrect code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb3BlcmF0b3ItYXNzaWdubWVudDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG54ID0geCArIHk7XG54ID0geSAqIHg7XG54WzBdID0geFswXSAvIHk7XG54LnkgPSB4LnkgPDwgejsifQ==)

```
/*eslint operator-assignment: ["error", "always"]*/

x = x + y;
x = y * x;
x[0] = x[0] / y;
x.y = x.y << z;
1
2
3
4
5
6
```

Examples of correct code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb3BlcmF0b3ItYXNzaWdubWVudDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG54ID0geTtcbnggKz0geTtcbnggPSB5ICogejtcbnggPSAoeCAqIHkpICogejtcbnhbMF0gLz0geTtcbnhbZm9vKCldID0geFtmb28oKV0gJSAyO1xueCA9IHkgKyB4OyAvLyBgK2AgaXMgbm90IGFsd2F5cyBjb21tdXRhdGl2ZSAoZS5nLiB4ID0gXCJhYmNcIikifQ==)

```
/*eslint operator-assignment: ["error", "always"]*/

x = y;
x += y;
x = y * z;
x = (x * y) * z;
x[0] /= y;
x[foo()] = x[foo()] % 2;
x = y + x; // `+` is not always commutative (e.g. x = "abc")
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

### never

Examples of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb3BlcmF0b3ItYXNzaWdubWVudDogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbnggKj0geTtcbnggXj0gKHkgKyB6KSAvIGZvbygpOyJ9)

```
/*eslint operator-assignment: ["error", "never"]*/

x *= y;
x ^= (y + z) / foo();
1
2
3
4
```

Examples of correct code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb3BlcmF0b3ItYXNzaWdubWVudDogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbnggPSB4ICsgeTtcbngueSA9IHgueSAvIGEuYjsifQ==)

```
/*eslint operator-assignment: ["error", "never"]*/

x = x + y;
x.y = x.y / a.b;
1
2
3
4
```

## When Not To Use It

Use of operator assignment shorthand is a stylistic choice. Leaving this rule turned off would allow developers to choose which style is more readable on a case-by-case basis.

## Version

This rule was introduced in ESLint v0.10.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/operator-assignment.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/operator-assignment.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/operator-assignment.md
                    
                
                )
