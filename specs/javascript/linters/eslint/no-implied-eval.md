# no-implied-eval

Disallow the use of `eval()`-like methods

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

It’s considered a good practice to avoid using `eval()` in JavaScript. There are security and performance implications involved with doing so, which is why many linters (including ESLint) recommend disallowing `eval()`. However, there are some other ways to pass a string and have it interpreted as JavaScript code that have similar concerns.

The first is using `setTimeout()`, `setInterval()` or `execScript()` (Internet Explorer only), all of which can accept a string of JavaScript code as their first argument. For example:

```
setTimeout("alert('Hi!');", 100);
1
```

Copy code to clipboard

This is considered an implied `eval()` because a string of JavaScript code is passed in to be interpreted. The same can be done with `setInterval()` and `execScript()`. Both interpret the JavaScript code in the global scope. For both `setTimeout()` and `setInterval()`, the first argument can also be a function, and that is considered safer and is more performant:

```
setTimeout(function() {
    alert("Hi!");
}, 100);
1
2
3
```

Copy code to clipboard

The best practice is to always use a function for the first argument of `setTimeout()` and `setInterval()` (and avoid `execScript()`).

## Rule Details

This rule aims to eliminate implied `eval()` through the use of `setTimeout()`, `setInterval()` or `execScript()`. As such, it will warn when either function is used with a string as the first argument.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGllZC1ldmFsOiBcImVycm9yXCIqL1xuLypnbG9iYWwgd2luZG93LCBzZXRUaW1lb3V0LCBzZXRJbnRlcnZhbCwgZXhlY1NjcmlwdCovXG5cbnNldFRpbWVvdXQoXCJhbGVydCgnSGkhJyk7XCIsIDEwMCk7XG5cbnNldEludGVydmFsKFwiYWxlcnQoJ0hpIScpO1wiLCAxMDApO1xuXG5leGVjU2NyaXB0KFwiYWxlcnQoJ0hpIScpXCIpO1xuXG53aW5kb3cuc2V0VGltZW91dChcImNvdW50ID0gNVwiLCAxMCk7XG5cbndpbmRvdy5zZXRJbnRlcnZhbChcImZvbyA9IGJhclwiLCAxMCk7In0=)

```
/*eslint no-implied-eval: "error"*/
/*global window, setTimeout, setInterval, execScript*/

setTimeout("alert('Hi!');", 100);

setInterval("alert('Hi!');", 100);

execScript("alert('Hi!')");

window.setTimeout("count = 5", 10);

window.setInterval("foo = bar", 10);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGllZC1ldmFsOiBcImVycm9yXCIqL1xuLypnbG9iYWwgc2V0VGltZW91dCwgc2V0SW50ZXJ2YWwqL1xuXG5zZXRUaW1lb3V0KGZ1bmN0aW9uKCkge1xuICAgIGFsZXJ0KFwiSGkhXCIpO1xufSwgMTAwKTtcblxuc2V0SW50ZXJ2YWwoZnVuY3Rpb24oKSB7XG4gICAgYWxlcnQoXCJIaSFcIik7XG59LCAxMDApOyJ9)

```
/*eslint no-implied-eval: "error"*/
/*global setTimeout, setInterval*/

setTimeout(function() {
    alert("Hi!");
}, 100);

setInterval(function() {
    alert("Hi!");
}, 100);
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
```

## When Not To Use It

If you want to allow `setTimeout()` and `setInterval()` with string arguments, then you can safely disable this rule.

## Related Rules

- [no-eval](/docs/latest/rules/no-eval)

## Version

This rule was introduced in ESLint v0.0.7.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-implied-eval.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-implied-eval.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-implied-eval.md
                    
                
                )
