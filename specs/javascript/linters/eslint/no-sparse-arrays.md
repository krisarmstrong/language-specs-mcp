# no-sparse-arrays

Disallow sparse arrays

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Sparse arrays contain empty slots, most frequently due to multiple commas being used in an array literal, such as:

```
const items = [,,];
1
```

Copy code to clipboard

While the `items` array in this example has a `length` of 2, there are actually no values in `items[0]` or `items[1]`. The fact that the array literal is valid with only commas inside, coupled with the `length` being set and actual item values not being set, make sparse arrays confusing for many developers. Consider the following:

```
const colors = [ "red",, "blue" ];
1
```

Copy code to clipboard

In this example, the `colors` array has a `length` of 3. But did the developer intend for there to be an empty spot in the middle of the array? Or is it a typo?

The confusion around sparse arrays defined in this manner is enough that it’s recommended to avoid using them unless you are certain that they are useful in your code.

## Rule Details

This rule disallows sparse array literals which have “holes” where commas are not preceded by elements. It does not apply to a trailing comma following the last element.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc3BhcnNlLWFycmF5czogXCJlcnJvclwiKi9cblxuY29uc3QgaXRlbXMgPSBbLF07XG5jb25zdCBjb2xvcnMgPSBbIFwicmVkXCIsLCBcImJsdWVcIiBdOyJ9)

```
/*eslint no-sparse-arrays: "error"*/

const items = [,];
const colors = [ "red",, "blue" ];
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc3BhcnNlLWFycmF5czogXCJlcnJvclwiKi9cblxuY29uc3QgaXRlbXMgPSBbXTtcbmNvbnN0IGFyciA9IG5ldyBBcnJheSgyMyk7XG5cbi8vIHRyYWlsaW5nIGNvbW1hIChhZnRlciB0aGUgbGFzdCBlbGVtZW50KSBpcyBub3QgYSBwcm9ibGVtXG5jb25zdCBjb2xvcnMgPSBbIFwicmVkXCIsIFwiYmx1ZVwiLCBdOyJ9)

```
/*eslint no-sparse-arrays: "error"*/

const items = [];
const arr = new Array(23);

// trailing comma (after the last element) is not a problem
const colors = [ "red", "blue", ];
1
2
3
4
5
6
7
```

## When Not To Use It

If you want to use sparse arrays, then it is safe to disable this rule.

## Version

This rule was introduced in ESLint v0.4.0.

## Further Reading

[Inconsistent array literals](https://www.nczonline.net/blog/2007/09/09/inconsistent-array-literals/)
 www.nczonline.net

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-sparse-arrays.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-sparse-arrays.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-sparse-arrays.md
                    
                
                )
