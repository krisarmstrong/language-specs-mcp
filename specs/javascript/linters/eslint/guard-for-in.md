# guard-for-in

Require `for-in` loops to include an `if` statement

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Looping over objects with a `for in` loop will include properties that are inherited through the prototype chain. This behavior can lead to unexpected items in your for loop.

```
for (key in foo) {
    doSomething(key);
}
1
2
3
```

Copy code to clipboard

For codebases that do not support ES2022, `Object.prototype.hasOwnProperty.call(foo, key)` can be used as a check that the property is not inherited.

For codebases that do support ES2022, `Object.hasOwn(foo, key)` can be used as a shorter alternative; see [prefer-object-has-own](prefer-object-has-own).

Note that simply checking `foo.hasOwnProperty(key)` is likely to cause an error in some cases; see [no-prototype-builtins](no-prototype-builtins).

## Rule Details

This rule is aimed at preventing unexpected behavior that could arise from using a `for in` loop without filtering the results in the loop. As such, it will warn when `for in` loops do not filter their results with an `if` statement.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3VhcmQtZm9yLWluOiBcImVycm9yXCIqL1xuXG5mb3IgKGtleSBpbiBmb28pIHtcbiAgICBkb1NvbWV0aGluZyhrZXkpO1xufSJ9)

```
/*eslint guard-for-in: "error"*/

for (key in foo) {
    doSomething(key);
}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3VhcmQtZm9yLWluOiBcImVycm9yXCIqL1xuXG5mb3IgKGtleSBpbiBmb28pIHtcbiAgICBpZiAoT2JqZWN0Lmhhc093bihmb28sIGtleSkpIHtcbiAgICAgICAgZG9Tb21ldGhpbmcoa2V5KTtcbiAgICB9XG59XG5cbmZvciAoa2V5IGluIGZvbykge1xuICAgIGlmIChPYmplY3QucHJvdG90eXBlLmhhc093blByb3BlcnR5LmNhbGwoZm9vLCBrZXkpKSB7XG4gICAgICAgIGRvU29tZXRoaW5nKGtleSk7XG4gICAgfVxufVxuXG5mb3IgKGtleSBpbiBmb28pIHtcbiAgICBpZiAoe30uaGFzT3duUHJvcGVydHkuY2FsbChmb28sIGtleSkpIHtcbiAgICAgICAgZG9Tb21ldGhpbmcoa2V5KTtcbiAgICB9XG59In0=)

```
/*eslint guard-for-in: "error"*/

for (key in foo) {
    if (Object.hasOwn(foo, key)) {
        doSomething(key);
    }
}

for (key in foo) {
    if (Object.prototype.hasOwnProperty.call(foo, key)) {
        doSomething(key);
    }
}

for (key in foo) {
    if ({}.hasOwnProperty.call(foo, key)) {
        doSomething(key);
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
15
16
17
18
19
```

## Related Rules

- [prefer-object-has-own](/docs/latest/rules/prefer-object-has-own)
- [no-prototype-builtins](/docs/latest/rules/no-prototype-builtins)

## Version

This rule was introduced in ESLint v0.0.6.

## Further Reading

[Exploring JavaScript for-in loops](https://javascriptweblog.wordpress.com/2011/01/04/exploring-javascript-for-in-loops/)
 javascriptweblog.wordpress.com[The pitfalls of using objects as maps in JavaScript](https://2ality.com/2012/01/objects-as-maps.html)
 2ality.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/guard-for-in.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/guard-for-in.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/guard-for-in.md
                    
                
                )
