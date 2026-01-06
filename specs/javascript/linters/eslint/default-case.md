# default-case

Require `default` cases in `switch` statements

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [commentPattern](#commentpattern)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Some code conventions require that all `switch` statements have a `default` case, even if the default case is empty, such as:

```
switch (foo) {
    case 1:
        doSomething();
        break;

    case 2:
        doSomething();
        break;

    default:
    // do nothing
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

Copy code to clipboard

The thinking is that it’s better to always explicitly state what the default behavior should be so that it’s clear whether or not the developer forgot to include the default behavior by mistake.

Other code conventions allow you to skip the `default` case so long as there is a comment indicating the omission is intentional, such as:

```
switch (foo) {
    case 1:
        doSomething();
        break;

    case 2:
        doSomething();
        break;

    // no default
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
```

Copy code to clipboard

Once again, the intent here is to show that the developer intended for there to be no default behavior.

## Rule Details

This rule aims to require `default` case in `switch` statements. You may optionally include a `// no default` after the last `case` if there is no `default` case. The comment may be in any desired case, such as `// No Default`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZGVmYXVsdC1jYXNlOiBcImVycm9yXCIqL1xuXG5zd2l0Y2ggKGEpIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIC8qIGNvZGUgKi9cbiAgICAgICAgYnJlYWs7XG59XG4ifQ==)

```
/*eslint default-case: "error"*/

switch (a) {
    case 1:
        /* code */
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZGVmYXVsdC1jYXNlOiBcImVycm9yXCIqL1xuXG5zd2l0Y2ggKGEpIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIC8qIGNvZGUgKi9cbiAgICAgICAgYnJlYWs7XG5cbiAgICBkZWZhdWx0OlxuICAgICAgICAvKiBjb2RlICovXG4gICAgICAgIGJyZWFrO1xufVxuXG5zd2l0Y2ggKGEpIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIC8qIGNvZGUgKi9cbiAgICAgICAgYnJlYWs7XG5cbiAgICAvLyBubyBkZWZhdWx0XG59XG5cbnN3aXRjaCAoYSkge1xuICAgIGNhc2UgMTpcbiAgICAgICAgLyogY29kZSAqL1xuICAgICAgICBicmVhaztcblxuICAgIC8vIE5vIERlZmF1bHRcbn0ifQ==)

```
/*eslint default-case: "error"*/

switch (a) {
    case 1:
        /* code */
        break;

    default:
        /* code */
        break;
}

switch (a) {
    case 1:
        /* code */
        break;

    // no default
}

switch (a) {
    case 1:
        /* code */
        break;

    // No Default
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
```

## Options

This rule accepts a single options argument:

- Set the `commentPattern` option to a regular expression string to change the default `/^no default$/i` comment test pattern.

### commentPattern

Examples of correct code for the `{ "commentPattern": "^skip\\sdefault" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZGVmYXVsdC1jYXNlOiBbXCJlcnJvclwiLCB7IFwiY29tbWVudFBhdHRlcm5cIjogXCJec2tpcFxcXFxzZGVmYXVsdFwiIH1dKi9cblxuc3dpdGNoKGEpIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIC8qIGNvZGUgKi9cbiAgICAgICAgYnJlYWs7XG5cbiAgICAvLyBza2lwIGRlZmF1bHRcbn1cblxuc3dpdGNoKGEpIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIC8qIGNvZGUgKi9cbiAgICAgICAgYnJlYWs7XG5cbiAgICAvLyBza2lwIGRlZmF1bHQgY2FzZVxufSJ9)

```
/*eslint default-case: ["error", { "commentPattern": "^skip\\sdefault" }]*/

switch(a) {
    case 1:
        /* code */
        break;

    // skip default
}

switch(a) {
    case 1:
        /* code */
        break;

    // skip default case
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
```

## When Not To Use It

If you don’t want to enforce a `default` case for `switch` statements, you can safely disable this rule.

## Related Rules

- [no-fallthrough](/docs/latest/rules/no-fallthrough)

## Version

This rule was introduced in ESLint v0.6.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/default-case.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/default-case.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/default-case.md
                    
                
                )
