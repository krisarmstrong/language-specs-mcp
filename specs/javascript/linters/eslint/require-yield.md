# require-yield

Require generator functions to contain `yield`

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

## Rule Details

This rule generates warnings for generator functions that do not have the `yield` keyword.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS15aWVsZDogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24qIGZvbygpIHtcbiAgcmV0dXJuIDEwO1xufSJ9)

```
/*eslint require-yield: "error"*/

function* foo() {
  return 10;
}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS15aWVsZDogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24qIGZvbygpIHtcbiAgeWllbGQgNTtcbiAgcmV0dXJuIDEwO1xufVxuXG5mdW5jdGlvbiBiYXIoKSB7XG4gIHJldHVybiAxMDtcbn1cblxuLy8gVGhpcyBydWxlIGRvZXMgbm90IHdhcm4gb24gZW1wdHkgZ2VuZXJhdG9yIGZ1bmN0aW9ucy5cbmZ1bmN0aW9uKiBiYXooKSB7IH0ifQ==)

```
/*eslint require-yield: "error"*/

function* foo() {
  yield 5;
  return 10;
}

function bar() {
  return 10;
}

// This rule does not warn on empty generator functions.
function* baz() { }
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

## When Not To Use It

If you don’t want to notify generator functions that have no `yield` expression, then it’s safe to disable this rule.

## Related Rules

- [require-await](/docs/latest/rules/require-await)

## Version

This rule was introduced in ESLint v1.0.0-rc-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/require-yield.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/require-yield.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/require-yield.md
                    
                
                )
