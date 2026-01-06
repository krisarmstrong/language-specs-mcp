# no-script-url

Disallow `javascript:` URLs

## Table of Contents

1. [Rule Details](#rule-details)
2. [Compatibility](#compatibility)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Using `javascript:` URLs is considered by some as a form of `eval`. Code passed in `javascript:` URLs has to be parsed and evaluated by the browser in the same way that `eval` is processed.

## Rule Details

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2NyaXB0LXVybDogXCJlcnJvclwiKi9cblxubG9jYXRpb24uaHJlZiA9IFwiamF2YXNjcmlwdDp2b2lkKDApXCI7XG5cbmxvY2F0aW9uLmhyZWYgPSBgamF2YXNjcmlwdDp2b2lkKDApYDsifQ==)

```
/*eslint no-script-url: "error"*/

location.href = "javascript:void(0)";

location.href = `javascript:void(0)`;
1
2
3
4
5
```

## Compatibility

- JSHint: This rule corresponds to `scripturl` rule of JSHint.

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[What is the matter with script-targeted URLs?](https://stackoverflow.com/questions/13497971/what-is-the-matter-with-script-targeted-urls)
 stackoverflow.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-script-url.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-script-url.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-script-url.md
                    
                
                )
