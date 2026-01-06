# no-self-compare

Disallow comparisons where both sides are exactly the same

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [Version](#version)
4. [Resources](#resources)

Comparing a variable against itself is usually an error, either a typo or refactoring error. It is confusing to the reader and may potentially introduce a runtime error.

The only time you would compare a variable against itself is when you are testing for `NaN`. However, it is far more appropriate to use `typeof x === 'number' && isNaN(x)` or the [Number.isNaN ES2015 function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN) for that use case rather than leaving the reader of the code to determine the intent of self comparison.

## Rule Details

This error is raised to highlight a potentially confusing and potentially pointless piece of code. There are almost no situations in which you would need to compare something to itself.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VsZi1jb21wYXJlOiBcImVycm9yXCIqL1xuXG5sZXQgeCA9IDEwO1xuaWYgKHggPT09IHgpIHtcbiAgICB4ID0gMjA7XG59In0=)

```
/*eslint no-self-compare: "error"*/

let x = 10;
if (x === x) {
    x = 20;
}
1
2
3
4
5
6
```

## Known Limitations

This rule works by directly comparing the tokens on both sides of the operator. It flags them as problematic if they are structurally identical. However, it doesn’t consider possible side effects or that functions may return different objects even when called with the same arguments. As a result, it can produce false positives in some cases, such as:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VsZi1jb21wYXJlOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBwYXJzZURhdGUoZGF0ZVN0cikge1xuICByZXR1cm4gbmV3IERhdGUoZGF0ZVN0cik7XG59XG5cbmlmIChwYXJzZURhdGUoJ0RlY2VtYmVyIDE3LCAxOTk1IDAzOjI0OjAwJykgPT09IHBhcnNlRGF0ZSgnRGVjZW1iZXIgMTcsIDE5OTUgMDM6MjQ6MDAnKSkge1xuICAvLyBkbyBzb21ldGhpbmdcbn1cblxubGV0IGNvdW50ZXIgPSAwO1xuZnVuY3Rpb24gaW5jcmVtZW50VW5sZXNzUmVhY2hlZE1heGltdW0oKSB7XG4gIHJldHVybiBNYXRoLm1pbihjb3VudGVyICs9IDEsIDEwKTtcbn1cblxuaWYgKGluY3JlbWVudFVubGVzc1JlYWNoZWRNYXhpbXVtKCkgPT09IGluY3JlbWVudFVubGVzc1JlYWNoZWRNYXhpbXVtKCkpIHtcbiAgLy8gLi4uXG59In0=)

```
/*eslint no-self-compare: "error"*/

function parseDate(dateStr) {
  return new Date(dateStr);
}

if (parseDate('December 17, 1995 03:24:00') === parseDate('December 17, 1995 03:24:00')) {
  // do something
}

let counter = 0;
function incrementUnlessReachedMaximum() {
  return Math.min(counter += 1, 10);
}

if (incrementUnlessReachedMaximum() === incrementUnlessReachedMaximum()) {
  // ...
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
17
18
```

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-self-compare.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-self-compare.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-self-compare.md
                    
                
                )
