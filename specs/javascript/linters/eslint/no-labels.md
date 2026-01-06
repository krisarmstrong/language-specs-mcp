# no-labels

Disallow labeled statements

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowLoop](#allowloop)
  2. [allowSwitch](#allowswitch)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Labeled statements in JavaScript are used in conjunction with `break` and `continue` to control flow around multiple loops. For example:

```
outer:
    while (true) {

        while (true) {
            break outer;
        }
    }
1
2
3
4
5
6
7
```

Copy code to clipboard

The `break outer` statement ensures that this code will not result in an infinite loop because control is returned to the next statement after the `outer` label was applied. If this statement was changed to be just `break`, control would flow back to the outer `while` statement and an infinite loop would result.

While convenient in some cases, labels tend to be used only rarely and are frowned upon by some as a remedial form of flow control that is more error prone and harder to understand.

## Rule Details

This rule aims to eliminate the use of labeled statements in JavaScript. It will warn whenever a labeled statement is encountered and whenever `break` or `continue` are used with a label.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbGFiZWxzOiBcImVycm9yXCIqL1xuXG5sYWJlbDpcbiAgICB3aGlsZSh0cnVlKSB7XG4gICAgICAgIC8vIC4uLlxuICAgIH1cblxubGFiZWw6XG4gICAgd2hpbGUodHJ1ZSkge1xuICAgICAgICBicmVhayBsYWJlbDtcbiAgICB9XG5cbmxhYmVsOlxuICAgIHdoaWxlKHRydWUpIHtcbiAgICAgICAgY29udGludWUgbGFiZWw7XG4gICAgfVxuXG5sYWJlbDpcbiAgICBzd2l0Y2ggKGEpIHtcbiAgICBjYXNlIDA6XG4gICAgICAgIGJyZWFrIGxhYmVsO1xuICAgIH1cblxubGFiZWw6XG4gICAge1xuICAgICAgICBicmVhayBsYWJlbDtcbiAgICB9XG5cbmxhYmVsOlxuICAgIGlmIChhKSB7XG4gICAgICAgIGJyZWFrIGxhYmVsO1xuICAgIH0ifQ==)

```
/*eslint no-labels: "error"*/

label:
    while(true) {
        // ...
    }

label:
    while(true) {
        break label;
    }

label:
    while(true) {
        continue label;
    }

label:
    switch (a) {
    case 0:
        break label;
    }

label:
    {
        break label;
    }

label:
    if (a) {
        break label;
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
20
21
22
23
24
25
26
27
28
29
30
31
32
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbGFiZWxzOiBcImVycm9yXCIqL1xuXG5jb25zdCBmID0ge1xuICAgIGxhYmVsOiBcImZvb1wiXG59O1xuXG53aGlsZSAodHJ1ZSkge1xuICAgIGJyZWFrO1xufVxuXG53aGlsZSAodHJ1ZSkge1xuICAgIGNvbnRpbnVlO1xufSJ9)

```
/*eslint no-labels: "error"*/

const f = {
    label: "foo"
};

while (true) {
    break;
}

while (true) {
    continue;
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
```

## Options

The options allow labels with loop or switch statements:

- `"allowLoop"` (`boolean`, default is `false`) - If this option was set `true`, this rule ignores labels which are sticking to loop statements.
- `"allowSwitch"` (`boolean`, default is `false`) - If this option was set `true`, this rule ignores labels which are sticking to switch statements.

Actually labeled statements in JavaScript can be used with other than loop and switch statements. However, this way is ultra rare, not well-known, so this would be confusing developers.

### allowLoop

Examples of correct code for the `{ "allowLoop": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbGFiZWxzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dMb29wXCI6IHRydWUgfV0qL1xuXG5sYWJlbDpcbiAgICB3aGlsZSAodHJ1ZSkge1xuICAgICAgICBicmVhayBsYWJlbDtcbiAgICB9In0=)

```
/*eslint no-labels: ["error", { "allowLoop": true }]*/

label:
    while (true) {
        break label;
    }
1
2
3
4
5
6
```

### allowSwitch

Examples of correct code for the `{ "allowSwitch": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbGFiZWxzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTd2l0Y2hcIjogdHJ1ZSB9XSovXG5cbmxhYmVsOlxuICAgIHN3aXRjaCAoYSkge1xuICAgICAgICBjYXNlIDA6XG4gICAgICAgICAgICBicmVhayBsYWJlbDtcbiAgICB9In0=)

```
/*eslint no-labels: ["error", { "allowSwitch": true }]*/

label:
    switch (a) {
        case 0:
            break label;
    }
1
2
3
4
5
6
7
```

## When Not To Use It

If you need to use labeled statements everywhere, then you can safely disable this rule.

## Related Rules

- [no-extra-label](/docs/latest/rules/no-extra-label)
- [no-label-var](/docs/latest/rules/no-label-var)
- [no-unused-labels](/docs/latest/rules/no-unused-labels)

## Version

This rule was introduced in ESLint v0.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-labels.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-labels.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-labels.md
                    
                
                )
