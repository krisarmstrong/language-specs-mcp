# no-duplicate-case

Disallow duplicate case labels

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

If a `switch` statement has duplicate test expressions in `case` clauses, it is likely that a programmer copied a `case` clause but forgot to change the test expression.

## Rule Details

This rule disallows duplicate test expressions in `case` clauses of `switch` statements.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWNhc2U6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSAxLFxuICAgIG9uZSA9IDE7XG5cbnN3aXRjaCAoYSkge1xuICAgIGNhc2UgMTpcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSAyOlxuICAgICAgICBicmVhaztcbiAgICBjYXNlIDE6ICAgICAgICAgLy8gZHVwbGljYXRlIHRlc3QgZXhwcmVzc2lvblxuICAgICAgICBicmVhaztcbiAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbn1cblxuc3dpdGNoIChhKSB7XG4gICAgY2FzZSBvbmU6XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgMjpcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSBvbmU6ICAgICAgICAgLy8gZHVwbGljYXRlIHRlc3QgZXhwcmVzc2lvblxuICAgICAgICBicmVhaztcbiAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbn1cblxuc3dpdGNoIChhKSB7XG4gICAgY2FzZSBcIjFcIjpcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSBcIjJcIjpcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSBcIjFcIjogICAgICAgICAvLyBkdXBsaWNhdGUgdGVzdCBleHByZXNzaW9uXG4gICAgICAgIGJyZWFrO1xuICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xufSJ9)

```
/*eslint no-duplicate-case: "error"*/

const a = 1,
    one = 1;

switch (a) {
    case 1:
        break;
    case 2:
        break;
    case 1:         // duplicate test expression
        break;
    default:
        break;
}

switch (a) {
    case one:
        break;
    case 2:
        break;
    case one:         // duplicate test expression
        break;
    default:
        break;
}

switch (a) {
    case "1":
        break;
    case "2":
        break;
    case "1":         // duplicate test expression
        break;
    default:
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
33
34
35
36
37
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWNhc2U6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSAxLFxuICAgIG9uZSA9IDE7XG5cbnN3aXRjaCAoYSkge1xuICAgIGNhc2UgMTpcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSAyOlxuICAgICAgICBicmVhaztcbiAgICBjYXNlIDM6XG4gICAgICAgIGJyZWFrO1xuICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xufVxuXG5zd2l0Y2ggKGEpIHtcbiAgICBjYXNlIG9uZTpcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSAyOlxuICAgICAgICBicmVhaztcbiAgICBjYXNlIDM6XG4gICAgICAgIGJyZWFrO1xuICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xufVxuXG5zd2l0Y2ggKGEpIHtcbiAgICBjYXNlIFwiMVwiOlxuICAgICAgICBicmVhaztcbiAgICBjYXNlIFwiMlwiOlxuICAgICAgICBicmVhaztcbiAgICBjYXNlIFwiM1wiOlxuICAgICAgICBicmVhaztcbiAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbn0ifQ==)

```
/*eslint no-duplicate-case: "error"*/

const a = 1,
    one = 1;

switch (a) {
    case 1:
        break;
    case 2:
        break;
    case 3:
        break;
    default:
        break;
}

switch (a) {
    case one:
        break;
    case 2:
        break;
    case 3:
        break;
    default:
        break;
}

switch (a) {
    case "1":
        break;
    case "2":
        break;
    case "3":
        break;
    default:
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
33
34
35
36
37
```

## When Not To Use It

In rare cases where identical test expressions in `case` clauses produce different values, which necessarily means that the expressions are causing and relying on side effects, you will have to disable this rule.

```
switch (a) {
    case i++:
        foo();
        break;
    case i++: // eslint-disable-line no-duplicate-case
        bar();
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
```

Copy code to clipboard

## Version

This rule was introduced in ESLint v0.17.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-duplicate-case.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-duplicate-case.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-duplicate-case.md
                    
                
                )
