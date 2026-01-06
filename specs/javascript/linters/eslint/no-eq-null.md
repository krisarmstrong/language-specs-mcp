# no-eq-null

Disallow `null` comparisons without type-checking operators

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Compatibility](#compatibility)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Comparing to `null` without a type-checking operator (`==` or `!=`), can have unintended results as the comparison will evaluate to `true` when comparing to not just a `null`, but also an `undefined` value.

```
if (foo == null) {
  bar();
}
1
2
3
```

Copy code to clipboard

## Rule Details

The `no-eq-null` rule aims reduce potential bug and unwanted behavior by ensuring that comparisons to `null` only match `null`, and not also `undefined`. As such it will flag comparisons to `null` when using `==` and `!=`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXEtbnVsbDogXCJlcnJvclwiKi9cblxuaWYgKGZvbyA9PSBudWxsKSB7XG4gIGJhcigpO1xufVxuXG53aGlsZSAocXV4ICE9IG51bGwpIHtcbiAgYmF6KCk7XG59In0=)

```
/*eslint no-eq-null: "error"*/

if (foo == null) {
  bar();
}

while (qux != null) {
  baz();
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXEtbnVsbDogXCJlcnJvclwiKi9cblxuaWYgKGZvbyA9PT0gbnVsbCkge1xuICBiYXIoKTtcbn1cblxud2hpbGUgKHF1eCAhPT0gbnVsbCkge1xuICBiYXooKTtcbn0ifQ==)

```
/*eslint no-eq-null: "error"*/

if (foo === null) {
  bar();
}

while (qux !== null) {
  baz();
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

## When Not To Use It

If you want to enforce type-checking operations in general, use the more powerful [eqeqeq](./eqeqeq) instead.

## Compatibility

- JSHint: This rule corresponds to `eqnull` rule of JSHint.

## Related Rules

- [eqeqeq](/docs/latest/rules/eqeqeq)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-eq-null.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-eq-null.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-eq-null.md
                    
                
                )
