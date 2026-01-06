# default-case-last

Enforce `default` clauses in `switch` statements to be last

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

A `switch` statement can optionally have a `default` clause.

If present, it’s usually the last clause, but it doesn’t need to be. It is also allowed to put the `default` clause before all `case` clauses, or anywhere between. The behavior is mostly the same as if it was the last clause. The `default` block will be still executed only if there is no match in the `case` clauses (including those defined after the `default`), but there is also the ability to “fall through” from the `default` clause to the following clause in the list. However, such flow is not common and it would be confusing to the readers.

Even if there is no “fall through” logic, it’s still unexpected to see the `default` clause before or between the `case` clauses. By convention, it is expected to be the last clause.

If a `switch` statement should have a `default` clause, it’s considered a best practice to define it as the last clause.

## Rule Details

This rule enforces `default` clauses in `switch` statements to be last.

It applies only to `switch` statements that already have a `default` clause.

This rule does not enforce the existence of `default` clauses. See [default-case](default-case) if you also want to enforce the existence of `default` clauses in `switch` statements.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZGVmYXVsdC1jYXNlLWxhc3Q6IFwiZXJyb3JcIiovXG5cbnN3aXRjaCAoZm9vKSB7XG4gICAgZGVmYXVsdDpcbiAgICAgICAgYmFyKCk7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgXCJhXCI6XG4gICAgICAgIGJheigpO1xuICAgICAgICBicmVhaztcbn1cblxuc3dpdGNoIChmb28pIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIGJhcigpO1xuICAgICAgICBicmVhaztcbiAgICBkZWZhdWx0OlxuICAgICAgICBiYXooKTtcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSAyOlxuICAgICAgICBxdXV4KCk7XG4gICAgICAgIGJyZWFrO1xufVxuXG5zd2l0Y2ggKGZvbykge1xuICAgIGNhc2UgXCJ4XCI6XG4gICAgICAgIGJhcigpO1xuICAgICAgICBicmVhaztcbiAgICBkZWZhdWx0OlxuICAgIGNhc2UgXCJ5XCI6XG4gICAgICAgIGJheigpO1xuICAgICAgICBicmVhaztcbn1cblxuc3dpdGNoIChmb28pIHtcbiAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbiAgICBjYXNlIC0xOlxuICAgICAgICBiYXIoKTtcbiAgICAgICAgYnJlYWs7XG59XG5cbnN3aXRjaCAoZm9vKSB7XG4gIGRlZmF1bHQ6XG4gICAgZG9Tb21ldGhpbmdJZk5vdFplcm8oKTtcbiAgY2FzZSAwOlxuICAgIGRvU29tZXRoaW5nQW55d2F5KCk7XG59In0=)

```
/*eslint default-case-last: "error"*/

switch (foo) {
    default:
        bar();
        break;
    case "a":
        baz();
        break;
}

switch (foo) {
    case 1:
        bar();
        break;
    default:
        baz();
        break;
    case 2:
        quux();
        break;
}

switch (foo) {
    case "x":
        bar();
        break;
    default:
    case "y":
        baz();
        break;
}

switch (foo) {
    default:
        break;
    case -1:
        bar();
        break;
}

switch (foo) {
  default:
    doSomethingIfNotZero();
  case 0:
    doSomethingAnyway();
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
38
39
40
41
42
43
44
45
46
47
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZGVmYXVsdC1jYXNlLWxhc3Q6IFwiZXJyb3JcIiovXG5cbnN3aXRjaCAoZm9vKSB7XG4gICAgY2FzZSBcImFcIjpcbiAgICAgICAgYmF6KCk7XG4gICAgICAgIGJyZWFrO1xuICAgIGRlZmF1bHQ6XG4gICAgICAgIGJhcigpO1xuICAgICAgICBicmVhaztcbn1cblxuc3dpdGNoIChmb28pIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIGJhcigpO1xuICAgICAgICBicmVhaztcbiAgICBjYXNlIDI6XG4gICAgICAgIHF1dXgoKTtcbiAgICAgICAgYnJlYWs7XG4gICAgZGVmYXVsdDpcbiAgICAgICAgYmF6KCk7XG4gICAgICAgIGJyZWFrO1xufVxuXG5zd2l0Y2ggKGZvbykge1xuICAgIGNhc2UgXCJ4XCI6XG4gICAgICAgIGJhcigpO1xuICAgICAgICBicmVhaztcbiAgICBjYXNlIFwieVwiOlxuICAgIGRlZmF1bHQ6XG4gICAgICAgIGJheigpO1xuICAgICAgICBicmVhaztcbn1cblxuc3dpdGNoIChmb28pIHtcbiAgICBjYXNlIC0xOlxuICAgICAgICBiYXIoKTtcbiAgICAgICAgYnJlYWs7XG59XG5cbmlmIChmb28gIT09IDApIHtcbiAgICBkb1NvbWV0aGluZ0lmTm90WmVybygpO1xufVxuZG9Tb21ldGhpbmdBbnl3YXkoKTsifQ==)

```
/*eslint default-case-last: "error"*/

switch (foo) {
    case "a":
        baz();
        break;
    default:
        bar();
        break;
}

switch (foo) {
    case 1:
        bar();
        break;
    case 2:
        quux();
        break;
    default:
        baz();
        break;
}

switch (foo) {
    case "x":
        bar();
        break;
    case "y":
    default:
        baz();
        break;
}

switch (foo) {
    case -1:
        bar();
        break;
}

if (foo !== 0) {
    doSomethingIfNotZero();
}
doSomethingAnyway();
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
38
39
40
41
42
43
```

## Related Rules

- [default-case](/docs/latest/rules/default-case)

## Version

This rule was introduced in ESLint v7.0.0-alpha.0.

## Further Reading

[switch - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/default-case-last.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/default-case-last.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/default-case-last.md
                    
                
                )
