# no-self-assign

Disallow assignments where both sides are exactly the same

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [props](#props)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

Self assignments have no effect, so probably those are an error due to incomplete refactoring. Those indicate that what you should do is still remaining.

```
foo = foo;
[bar, baz] = [bar, qiz];
1
2
```

Copy code to clipboard

## Rule Details

This rule is aimed at eliminating self assignments.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VsZi1hc3NpZ246IFwiZXJyb3JcIiovXG5cbmZvbyA9IGZvbztcblxuW2EsIGJdID0gW2EsIGJdO1xuXG5bYSwgLi4uYl0gPSBbeCwgLi4uYl07XG5cbih7YSwgYn0gPSB7YSwgeH0pO1xuXG5mb28gJiY9IGZvbztcbmZvbyB8fD0gZm9vO1xuZm9vID8/PSBmb287In0=)

```
/*eslint no-self-assign: "error"*/

foo = foo;

[a, b] = [a, b];

[a, ...b] = [x, ...b];

({a, b} = {a, x});

foo &&= foo;
foo ||= foo;
foo ??= foo;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VsZi1hc3NpZ246IFwiZXJyb3JcIiovXG5cbmZvbyA9IGJhcjtcblthLCBiXSA9IFtiLCBhXTtcblxuLy8gVGhpcyBwYXR0ZXJuIGlzIHdhcm5lZCBieSB0aGUgYG5vLXVzZS1iZWZvcmUtZGVmaW5lYCBydWxlLlxubGV0IGZvbyA9IGZvbztcblxuLy8gVGhlIGRlZmF1bHQgdmFsdWVzIGhhdmUgYW4gZWZmZWN0LlxuW2ZvbyA9IDFdID0gW2Zvb107XG5cbi8vIG5vbi1zZWxmLWFzc2lnbm1lbnRzIHdpdGggcHJvcGVydGllcy5cbm9iai5hID0gb2JqLmI7XG5vYmouYS5iID0gb2JqLmMuYjtcbm9iai5hLmIgPSBvYmouYS5jO1xub2JqW2FdID0gb2JqW1wiYVwiXTtcblxuLy8gVGhpcyBpZ25vcmVzIGlmIHRoZXJlIGlzIGEgZnVuY3Rpb24gY2FsbC5cbm9iai5hKCkuYiA9IG9iai5hKCkuYjtcbmEoKS5iID0gYSgpLmI7XG5cbi8vIGAmPWAgYW5kIGB8PWAgaGF2ZSBhbiBlZmZlY3Qgb24gbm9uLWludGVnZXJzLlxuZm9vICY9IGZvbztcbmZvbyB8PSBmb287XG5cbi8vIEtub3duIGxpbWl0YXRpb246IHRoaXMgZG9lcyBub3Qgc3VwcG9ydCBjb21wdXRlZCBwcm9wZXJ0aWVzIGV4Y2VwdCBzaW5nbGUgbGl0ZXJhbCBvciBzaW5nbGUgaWRlbnRpZmllci5cbm9ialthICsgYl0gPSBvYmpbYSArIGJdO1xub2JqW1wiYVwiICsgXCJiXCJdID0gb2JqW1wiYVwiICsgXCJiXCJdOyJ9)

```
/*eslint no-self-assign: "error"*/

foo = bar;
[a, b] = [b, a];

// This pattern is warned by the `no-use-before-define` rule.
let foo = foo;

// The default values have an effect.
[foo = 1] = [foo];

// non-self-assignments with properties.
obj.a = obj.b;
obj.a.b = obj.c.b;
obj.a.b = obj.a.c;
obj[a] = obj["a"];

// This ignores if there is a function call.
obj.a().b = obj.a().b;
a().b = a().b;

// `&=` and `|=` have an effect on non-integers.
foo &= foo;
foo |= foo;

// Known limitation: this does not support computed properties except single literal or single identifier.
obj[a + b] = obj[a + b];
obj["a" + "b"] = obj["a" + "b"];
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
20
21
22
23
24
25
26
27
28
```

## Options

This rule has the option to check properties as well.

```
{
    "no-self-assign": ["error", {"props": true}]
}
1
2
3
```

Copy code to clipboard

- `props` - if this is `true`, `no-self-assign` rule warns self-assignments of properties. Default is `true`.

### props

Examples of correct code with the `{ "props": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2VsZi1hc3NpZ246IFtcImVycm9yXCIsIHtcInByb3BzXCI6IGZhbHNlfV0qL1xuXG4vLyBzZWxmLWFzc2lnbm1lbnRzIHdpdGggcHJvcGVydGllcy5cbm9iai5hID0gb2JqLmE7XG5vYmouYS5iID0gb2JqLmEuYjtcbm9ialtcImFcIl0gPSBvYmpbXCJhXCJdO1xub2JqW2FdID0gb2JqW2FdOyJ9)

```
/*eslint no-self-assign: ["error", {"props": false}]*/

// self-assignments with properties.
obj.a = obj.a;
obj.a.b = obj.a.b;
obj["a"] = obj["a"];
obj[a] = obj[a];
1
2
3
4
5
6
7
```

## When Not To Use It

If you don’t want to notify about self assignments, then it’s safe to disable this rule.

## Version

This rule was introduced in ESLint v2.0.0-rc.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-self-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-self-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-self-assign.md
                    
                
                )
