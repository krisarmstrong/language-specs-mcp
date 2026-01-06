# no-extra-label

Disallow unnecessary labels

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

If a loop contains no nested loops or switches, labeling the loop is unnecessary.

```
A: while (a) {
    break A;
}
1
2
3
```

Copy code to clipboard

You can achieve the same result by removing the label and using `break` or `continue` without a label. Probably those labels would confuse developers because they expect labels to jump to further.

## Rule Details

This rule is aimed at eliminating unnecessary labels.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtbGFiZWw6IFwiZXJyb3JcIiovXG5cbkE6IHdoaWxlIChhKSB7XG4gICAgYnJlYWsgQTtcbn1cblxuQjogZm9yIChsZXQgaSA9IDA7IGkgPCAxMDsgKytpKSB7XG4gICAgYnJlYWsgQjtcbn1cblxuQzogc3dpdGNoIChhKSB7XG4gICAgY2FzZSAwOlxuICAgICAgICBicmVhayBDO1xufSJ9)

```
/*eslint no-extra-label: "error"*/

A: while (a) {
    break A;
}

B: for (let i = 0; i < 10; ++i) {
    break B;
}

C: switch (a) {
    case 0:
        break C;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtbGFiZWw6IFwiZXJyb3JcIiovXG5cbndoaWxlIChhKSB7XG4gICAgYnJlYWs7XG59XG5cbmZvciAobGV0IGkgPSAwOyBpIDwgMTA7ICsraSkge1xuICAgIGJyZWFrO1xufVxuXG5zd2l0Y2ggKGEpIHtcbiAgICBjYXNlIDA6XG4gICAgICAgIGJyZWFrO1xufVxuXG5BOiB7XG4gICAgYnJlYWsgQTtcbn1cblxuQjogd2hpbGUgKGEpIHtcbiAgICB3aGlsZSAoYikge1xuICAgICAgICBicmVhayBCO1xuICAgIH1cbn1cblxuQzogc3dpdGNoIChhKSB7XG4gICAgY2FzZSAwOlxuICAgICAgICB3aGlsZSAoYikge1xuICAgICAgICAgICAgYnJlYWsgQztcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbn0ifQ==)

```
/*eslint no-extra-label: "error"*/

while (a) {
    break;
}

for (let i = 0; i < 10; ++i) {
    break;
}

switch (a) {
    case 0:
        break;
}

A: {
    break A;
}

B: while (a) {
    while (b) {
        break B;
    }
}

C: switch (a) {
    case 0:
        while (b) {
            break C;
        }
        break;
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

## When Not To Use It

If you don’t want to be notified about usage of labels, then it’s safe to disable this rule.

## Related Rules

- [no-labels](/docs/latest/rules/no-labels)
- [no-label-var](/docs/latest/rules/no-label-var)
- [no-unused-labels](/docs/latest/rules/no-unused-labels)

## Version

This rule was introduced in ESLint v2.0.0-rc.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-extra-label.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-extra-label.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-extra-label.md
                    
                
                )
