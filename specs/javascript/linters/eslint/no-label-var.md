# no-label-var

Disallow labels that share a name with a variable

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

## Rule Details

This rule aims to create clearer code by disallowing the bad practice of creating a label that shares a name with a variable that is in scope.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbGFiZWwtdmFyOiBcImVycm9yXCIqL1xuXG52YXIgeCA9IGZvbztcbmZ1bmN0aW9uIGJhcigpIHtcbng6XG4gIGZvciAoOzspIHtcbiAgICBicmVhayB4O1xuICB9XG59In0=)

```
/*eslint no-label-var: "error"*/

var x = foo;
function bar() {
x:
  for (;;) {
    break x;
  }
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbGFiZWwtdmFyOiBcImVycm9yXCIqL1xuXG4vLyBUaGUgdmFyaWFibGUgdGhhdCBoYXMgdGhlIHNhbWUgbmFtZSBhcyB0aGUgbGFiZWwgaXMgbm90IGluIHNjb3BlLlxuXG5mdW5jdGlvbiBmb28oKSB7XG4gIHZhciBxID0gdDtcbn1cblxuZnVuY3Rpb24gYmFyKCkge1xucTpcbiAgZm9yKDs7KSB7XG4gICAgYnJlYWsgcTtcbiAgfVxufSJ9)

```
/*eslint no-label-var: "error"*/

// The variable that has the same name as the label is not in scope.

function foo() {
  var q = t;
}

function bar() {
q:
  for(;;) {
    break q;
  }
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
```

## When Not To Use It

If you don’t want to be notified about usage of labels, then it’s safe to disable this rule.

## Related Rules

- [no-extra-label](/docs/latest/rules/no-extra-label)
- [no-labels](/docs/latest/rules/no-labels)
- [no-unused-labels](/docs/latest/rules/no-unused-labels)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-label-var.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-label-var.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-label-var.md
                    
                
                )
