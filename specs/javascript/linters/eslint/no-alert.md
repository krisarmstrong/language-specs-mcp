# no-alert

Disallow the use of `alert`, `confirm`, and `prompt`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Resources](#resources)

JavaScript’s `alert`, `confirm`, and `prompt` functions are widely considered to be obtrusive as UI elements and should be replaced by a more appropriate custom UI implementation. Furthermore, `alert` is often used while debugging code, which should be removed before deployment to production.

```
alert("here!");
1
```

Copy code to clipboard

## Rule Details

This rule is aimed at catching debugging code that should be removed and popup UI elements that should be replaced with less obtrusive, custom UIs. As such, it will warn when it encounters `alert`, `prompt`, and `confirm` function calls which are not shadowed.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYWxlcnQ6IFwiZXJyb3JcIiovXG5cbmFsZXJ0KFwiaGVyZSFcIik7XG5cbmNvbmZpcm0oXCJBcmUgeW91IHN1cmU/XCIpO1xuXG5wcm9tcHQoXCJXaGF0J3MgeW91ciBuYW1lP1wiLCBcIkpvaG4gRG9lXCIpOyJ9)

```
/*eslint no-alert: "error"*/

alert("here!");

confirm("Are you sure?");

prompt("What's your name?", "John Doe");
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYWxlcnQ6IFwiZXJyb3JcIiovXG5cbmN1c3RvbUFsZXJ0KFwiU29tZXRoaW5nIGhhcHBlbmVkIVwiKTtcblxuY3VzdG9tQ29uZmlybShcIkFyZSB5b3Ugc3VyZT9cIik7XG5cbmN1c3RvbVByb21wdChcIldobyBhcmUgeW91P1wiKTtcblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIGNvbnN0IGFsZXJ0ID0gbXlDdXN0b21MaWIuY3VzdG9tQWxlcnQ7XG4gICAgYWxlcnQoKTtcbn0ifQ==)

```
/*eslint no-alert: "error"*/

customAlert("Something happened!");

customConfirm("Are you sure?");

customPrompt("Who are you?");

function foo() {
    const alert = myCustomLib.customAlert;
    alert();
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
```

## Related Rules

- [no-console](/docs/latest/rules/no-console)
- [no-debugger](/docs/latest/rules/no-debugger)

## Version

This rule was introduced in ESLint v0.0.5.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-alert.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-alert.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-alert.md
                    
                
                )
