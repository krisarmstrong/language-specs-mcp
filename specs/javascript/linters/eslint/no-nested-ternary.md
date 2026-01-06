# no-nested-ternary

Disallow nested ternary expressions

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Resources](#resources)

Nesting ternary expressions can make code more difficult to understand.

```
const foo = bar ? baz : qux === quxx ? bing : bam;
1
```

Copy code to clipboard

## Rule Details

The `no-nested-ternary` rule disallows nested ternary expressions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmVzdGVkLXRlcm5hcnk6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHRoaW5nID0gZm9vID8gYmFyIDogYmF6ID09PSBxdXggPyBxdXh4IDogZm9vYmFyO1xuXG5mb28gPyBiYXogPT09IHF1eCA/IHF1eHgoKSA6IGZvb2JhcigpIDogYmFyKCk7In0=)

```
/*eslint no-nested-ternary: "error"*/

const thing = foo ? bar : baz === qux ? quxx : foobar;

foo ? baz === qux ? quxx() : foobar() : bar();
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbmVzdGVkLXRlcm5hcnk6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHRoaW5nID0gZm9vID8gYmFyIDogZm9vYmFyO1xuXG5sZXQgb3RoZXJUaGluZztcblxuaWYgKGZvbykge1xuICBvdGhlclRoaW5nID0gYmFyO1xufSBlbHNlIGlmIChiYXogPT09IHF1eCkge1xuICBvdGhlclRoaW5nID0gcXV4eDtcbn0gZWxzZSB7XG4gIG90aGVyVGhpbmcgPSBmb29iYXI7XG59In0=)

```
/*eslint no-nested-ternary: "error"*/

const thing = foo ? bar : foobar;

let otherThing;

if (foo) {
  otherThing = bar;
} else if (baz === qux) {
  otherThing = quxx;
} else {
  otherThing = foobar;
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
```

## Related Rules

- [no-ternary](/docs/latest/rules/no-ternary)
- [no-unneeded-ternary](/docs/latest/rules/no-unneeded-ternary)

## Version

This rule was introduced in ESLint v0.2.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-nested-ternary.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-nested-ternary.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-nested-ternary.md
                    
                
                )
