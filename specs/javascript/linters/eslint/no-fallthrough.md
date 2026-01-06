# no-fallthrough

Disallow fallthrough of `case` statements

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [commentPattern](#commentpattern)
  2. [allowEmptyCase](#allowemptycase)
  3. [reportUnusedFallthroughComment](#reportunusedfallthroughcomment)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

The `switch` statement in JavaScript is one of the more error-prone constructs of the language thanks in part to the ability to “fall through” from one `case` to the next. For example:

```
switch(foo) {
    case 1:
        doSomething();

    case 2:
        doSomethingElse();
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

In this example, if `foo` is `1`, then execution will flow through both cases, as the first falls through to the second. You can prevent this by using `break`, as in this example:

```
switch(foo) {
    case 1:
        doSomething();
        break;

    case 2:
        doSomethingElse();
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

That works fine when you don’t want a fallthrough, but what if the fallthrough is intentional, there is no way to indicate that in the language. It’s considered a best practice to always indicate when a fallthrough is intentional using a comment which matches the `/falls?\s?through/i` regular expression but isn’t a directive:

```
switch(foo) {
    case 1:
        doSomething();
        // falls through

    case 2:
        doSomethingElse();
}

switch(foo) {
    case 1:
        doSomething();
        // fall through

    case 2:
        doSomethingElse();
}

switch(foo) {
    case 1:
        doSomething();
        // fallsthrough

    case 2:
        doSomethingElse();
}

switch(foo) {
    case 1: {
        doSomething();
        // falls through
    }

    case 2: {
        doSomethingElse();
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

Copy code to clipboard

In this example, there is no confusion as to the expected behavior. It is clear that the first case is meant to fall through to the second case.

## Rule Details

This rule is aimed at eliminating unintentional fallthrough of one case to the other. As such, it flags any fallthrough scenarios that are not marked by a comment.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZmFsbHRocm91Z2g6IFwiZXJyb3JcIiovXG5cbnN3aXRjaChmb28pIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIGRvU29tZXRoaW5nKCk7XG5cbiAgICBjYXNlIDI6XG4gICAgICAgIGRvU29tZXRoaW5nKCk7XG59In0=)

```
/*eslint no-fallthrough: "error"*/

switch(foo) {
    case 1:
        doSomething();

    case 2:
        doSomething();
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZmFsbHRocm91Z2g6IFwiZXJyb3JcIiovXG5cbnN3aXRjaChmb28pIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIGRvU29tZXRoaW5nKCk7XG4gICAgICAgIGJyZWFrO1xuXG4gICAgY2FzZSAyOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xufVxuXG5mdW5jdGlvbiBiYXIoZm9vKSB7XG4gICAgc3dpdGNoKGZvbykge1xuICAgICAgICBjYXNlIDE6XG4gICAgICAgICAgICBkb1NvbWV0aGluZygpO1xuICAgICAgICAgICAgcmV0dXJuO1xuXG4gICAgICAgIGNhc2UgMjpcbiAgICAgICAgICAgIGRvU29tZXRoaW5nKCk7XG4gICAgfVxufVxuXG5zd2l0Y2goZm9vKSB7XG4gICAgY2FzZSAxOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xuICAgICAgICB0aHJvdyBuZXcgRXJyb3IoXCJCb28hXCIpO1xuXG4gICAgY2FzZSAyOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xufVxuXG5zd2l0Y2goZm9vKSB7XG4gICAgY2FzZSAxOlxuICAgIGNhc2UgMjpcbiAgICAgICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuc3dpdGNoKGZvbykge1xuICAgIGNhc2UgMTogY2FzZSAyOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xufVxuXG5zd2l0Y2goZm9vKSB7XG4gICAgY2FzZSAxOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xuICAgICAgICAvLyBmYWxscyB0aHJvdWdoXG5cbiAgICBjYXNlIDI6XG4gICAgICAgIGRvU29tZXRoaW5nKCk7XG59XG5cbnN3aXRjaChmb28pIHtcbiAgICBjYXNlIDE6IHtcbiAgICAgICAgZG9Tb21ldGhpbmcoKTtcbiAgICAgICAgLy8gZmFsbHMgdGhyb3VnaFxuICAgIH1cblxuICAgIGNhc2UgMjoge1xuICAgICAgICBkb1NvbWV0aGluZ0Vsc2UoKTtcbiAgICB9XG59In0=)

```
/*eslint no-fallthrough: "error"*/

switch(foo) {
    case 1:
        doSomething();
        break;

    case 2:
        doSomething();
}

function bar(foo) {
    switch(foo) {
        case 1:
            doSomething();
            return;

        case 2:
            doSomething();
    }
}

switch(foo) {
    case 1:
        doSomething();
        throw new Error("Boo!");

    case 2:
        doSomething();
}

switch(foo) {
    case 1:
    case 2:
        doSomething();
}

switch(foo) {
    case 1: case 2:
        doSomething();
}

switch(foo) {
    case 1:
        doSomething();
        // falls through

    case 2:
        doSomething();
}

switch(foo) {
    case 1: {
        doSomething();
        // falls through
    }

    case 2: {
        doSomethingElse();
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
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```

Note that the last `case` statement in these examples does not cause a warning because there is nothing to fall through into.

## Options

This rule has an object option:

- 

Set the `commentPattern` option to a regular expression string to change the test for intentional fallthrough comment. If the fallthrough comment matches a directive, that takes precedence over `commentPattern`.

- 

Set the `allowEmptyCase` option to `true` to allow empty cases regardless of the layout. By default, this rule does not require a fallthrough comment after an empty `case` only if the empty `case` and the next `case` are on the same line or on consecutive lines.

- 

Set the `reportUnusedFallthroughComment` option to `true` to prohibit a fallthrough comment from being present if the case cannot fallthrough due to being unreachable. This is mostly intended to help avoid misleading comments occurring as a result of refactoring.

### commentPattern

Examples of correct code for the `{ "commentPattern": "break[\\s\\w]*omitted" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZmFsbHRocm91Z2g6IFtcImVycm9yXCIsIHsgXCJjb21tZW50UGF0dGVyblwiOiBcImJyZWFrW1xcXFxzXFxcXHddKm9taXR0ZWRcIiB9XSovXG5cbnN3aXRjaChmb28pIHtcbiAgICBjYXNlIDE6XG4gICAgICAgIGRvU29tZXRoaW5nKCk7XG4gICAgICAgIC8vIGJyZWFrIG9taXR0ZWRcblxuICAgIGNhc2UgMjpcbiAgICAgICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuc3dpdGNoKGZvbykge1xuICAgIGNhc2UgMTpcbiAgICAgICAgZG9Tb21ldGhpbmcoKTtcbiAgICAgICAgLy8gY2F1dGlvbjogYnJlYWsgaXMgb21pdHRlZCBpbnRlbnRpb25hbGx5XG5cbiAgICBkZWZhdWx0OlxuICAgICAgICBkb1NvbWV0aGluZygpO1xufSJ9)

```
/*eslint no-fallthrough: ["error", { "commentPattern": "break[\\s\\w]*omitted" }]*/

switch(foo) {
    case 1:
        doSomething();
        // break omitted

    case 2:
        doSomething();
}

switch(foo) {
    case 1:
        doSomething();
        // caution: break is omitted intentionally

    default:
        doSomething();
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

### allowEmptyCase

Examples of correct code for the `{ "allowEmptyCase": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWZhbGx0aHJvdWdoOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dFbXB0eUNhc2VcIjogdHJ1ZSB9XSAqL1xuXG5zd2l0Y2goZm9vKXtcbiAgICBjYXNlIDE6XG5cbiAgICBjYXNlIDI6IGRvU29tZXRoaW5nKCk7XG59XG5cbnN3aXRjaChmb28pe1xuICAgIGNhc2UgMTpcbiAgICAvKlxuICAgIFB1dCBhIG1lc3NhZ2UgaGVyZSBcbiAgICAqL1xuICAgIGNhc2UgMjogZG9Tb21ldGhpbmcoKTtcbn1cbiJ9)

```
/* eslint no-fallthrough: ["error", { "allowEmptyCase": true }] */

switch(foo){
    case 1:

    case 2: doSomething();
}

switch(foo){
    case 1:
    /*
    Put a message here 
    */
    case 2: doSomething();
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
```

### reportUnusedFallthroughComment

Examples of incorrect code for the `{ "reportUnusedFallthroughComment": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWZhbGx0aHJvdWdoOiBbXCJlcnJvclwiLCB7IFwicmVwb3J0VW51c2VkRmFsbHRocm91Z2hDb21tZW50XCI6IHRydWUgfV0gKi9cblxuc3dpdGNoKGZvbyl7XG4gICAgY2FzZSAxOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xuICAgICAgICBicmVhaztcbiAgICAvLyBmYWxscyB0aHJvdWdoXG4gICAgY2FzZSAyOiBkb1NvbWV0aGluZygpO1xufVxuXG5mdW5jdGlvbiBmKCkge1xuICAgIHN3aXRjaChmb28pe1xuICAgICAgICBjYXNlIDE6XG4gICAgICAgICAgICBpZiAoYSkge1xuICAgICAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcigpO1xuICAgICAgICAgICAgfSBlbHNlIGlmIChiKSB7XG4gICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICAgIH1cbiAgICAgICAgLy8gZmFsbHMgdGhyb3VnaFxuICAgICAgICBjYXNlIDI6XG4gICAgICAgICAgICBicmVhaztcbiAgICB9XG59In0=)

```
/* eslint no-fallthrough: ["error", { "reportUnusedFallthroughComment": true }] */

switch(foo){
    case 1:
        doSomething();
        break;
    // falls through
    case 2: doSomething();
}

function f() {
    switch(foo){
        case 1:
            if (a) {
                throw new Error();
            } else if (b) {
                break;
            } else {
                return;
            }
        // falls through
        case 2:
            break;
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
20
21
22
23
24
25
```

Examples of correct code for the `{ "reportUnusedFallthroughComment": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWZhbGx0aHJvdWdoOiBbXCJlcnJvclwiLCB7IFwicmVwb3J0VW51c2VkRmFsbHRocm91Z2hDb21tZW50XCI6IHRydWUgfV0gKi9cblxuc3dpdGNoKGZvbyl7XG4gICAgY2FzZSAxOlxuICAgICAgICBkb1NvbWV0aGluZygpO1xuICAgICAgICBicmVhaztcbiAgICAvLyBqdXN0IGEgY29tbWVudFxuICAgIGNhc2UgMjogZG9Tb21ldGhpbmcoKTtcbn0ifQ==)

```
/* eslint no-fallthrough: ["error", { "reportUnusedFallthroughComment": true }] */

switch(foo){
    case 1:
        doSomething();
        break;
    // just a comment
    case 2: doSomething();
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

## When Not To Use It

If you don’t want to enforce that each `case` statement should end with a `throw`, `return`, `break`, or comment, then you can safely turn this rule off.

## Related Rules

- [default-case](/docs/latest/rules/default-case)

## Version

This rule was introduced in ESLint v0.0.7.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-fallthrough.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-fallthrough.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-fallthrough.md
                    
                
                )
