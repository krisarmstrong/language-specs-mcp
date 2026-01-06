# no-dupe-else-if

Disallow duplicate conditions in if-else-if chains

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

`if-else-if` chains are commonly used when there is a need to execute only one branch (or at most one branch) out of several possible branches, based on certain conditions.

```
if (a) {
    foo();
} else if (b) {
    bar();
} else if (c) {
    baz();
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

Two identical test conditions in the same chain are almost always a mistake in the code. Unless there are side effects in the expressions, a duplicate will evaluate to the same `true` or `false` value as the identical expression earlier in the chain, meaning that its branch can never execute.

```
if (a) {
    foo();
} else if (b) {
    bar();
} else if (b) {
    baz();
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

In the above example, `baz()` can never execute. Obviously, `baz()` could be executed only when `b` evaluates to `true`, but in that case `bar()` would be executed instead, since it’s earlier in the chain.

## Rule Details

This rule disallows duplicate conditions in the same `if-else-if` chain.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1lbHNlLWlmOiBcImVycm9yXCIqL1xuXG5pZiAoaXNTb21ldGhpbmcoeCkpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoaXNTb21ldGhpbmcoeCkpIHtcbiAgICBiYXIoKTtcbn1cblxuaWYgKGEpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoYikge1xuICAgIGJhcigpO1xufSBlbHNlIGlmIChjICYmIGQpIHtcbiAgICBiYXooKTtcbn0gZWxzZSBpZiAoYyAmJiBkKSB7XG4gICAgcXV1eCgpO1xufSBlbHNlIHtcbiAgICBxdXV1eCgpO1xufVxuXG5pZiAobiA9PT0gMSkge1xuICAgIGZvbygpO1xufSBlbHNlIGlmIChuID09PSAyKSB7XG4gICAgYmFyKCk7XG59IGVsc2UgaWYgKG4gPT09IDMpIHtcbiAgICBiYXooKTtcbn0gZWxzZSBpZiAobiA9PT0gMikge1xuICAgIHF1dXgoKTtcbn0gZWxzZSBpZiAobiA9PT0gNSkge1xuICAgIHF1dXV4KCk7XG59In0=)

```
/*eslint no-dupe-else-if: "error"*/

if (isSomething(x)) {
    foo();
} else if (isSomething(x)) {
    bar();
}

if (a) {
    foo();
} else if (b) {
    bar();
} else if (c && d) {
    baz();
} else if (c && d) {
    quux();
} else {
    quuux();
}

if (n === 1) {
    foo();
} else if (n === 2) {
    bar();
} else if (n === 3) {
    baz();
} else if (n === 2) {
    quux();
} else if (n === 5) {
    quuux();
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1lbHNlLWlmOiBcImVycm9yXCIqL1xuXG5pZiAoaXNTb21ldGhpbmcoeCkpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoaXNTb21ldGhpbmdFbHNlKHgpKSB7XG4gICAgYmFyKCk7XG59XG5cbmlmIChhKSB7XG4gICAgZm9vKCk7XG59IGVsc2UgaWYgKGIpIHtcbiAgICBiYXIoKTtcbn0gZWxzZSBpZiAoYyAmJiBkKSB7XG4gICAgYmF6KCk7XG59IGVsc2UgaWYgKGMgJiYgZSkge1xuICAgIHF1dXgoKTtcbn0gZWxzZSB7XG4gICAgcXV1dXgoKTtcbn1cblxuaWYgKG4gPT09IDEpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAobiA9PT0gMikge1xuICAgIGJhcigpO1xufSBlbHNlIGlmIChuID09PSAzKSB7XG4gICAgYmF6KCk7XG59IGVsc2UgaWYgKG4gPT09IDQpIHtcbiAgICBxdXV4KCk7XG59IGVsc2UgaWYgKG4gPT09IDUpIHtcbiAgICBxdXV1eCgpO1xufSJ9)

```
/*eslint no-dupe-else-if: "error"*/

if (isSomething(x)) {
    foo();
} else if (isSomethingElse(x)) {
    bar();
}

if (a) {
    foo();
} else if (b) {
    bar();
} else if (c && d) {
    baz();
} else if (c && e) {
    quux();
} else {
    quuux();
}

if (n === 1) {
    foo();
} else if (n === 2) {
    bar();
} else if (n === 3) {
    baz();
} else if (n === 4) {
    quux();
} else if (n === 5) {
    quuux();
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
```

This rule can also detect some cases where the conditions are not identical, but the branch can never execute due to the logic of `||` and `&&` operators.

Examples of additional incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1lbHNlLWlmOiBcImVycm9yXCIqL1xuXG5pZiAoYSB8fCBiKSB7XG4gICAgZm9vKCk7XG59IGVsc2UgaWYgKGEpIHtcbiAgICBiYXIoKTtcbn1cblxuaWYgKGEpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoYikge1xuICAgIGJhcigpO1xufSBlbHNlIGlmIChhIHx8IGIpIHtcbiAgICBiYXooKTtcbn1cblxuaWYgKGEpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoYSAmJiBiKSB7XG4gICAgYmFyKCk7XG59XG5cbmlmIChhICYmIGIpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoYSAmJiBiICYmIGMpIHtcbiAgICBiYXIoKTtcbn1cblxuaWYgKGEgfHwgYikge1xuICAgIGZvbygpO1xufSBlbHNlIGlmIChiICYmIGMpIHtcbiAgICBiYXIoKTtcbn1cblxuaWYgKGEpIHtcbiAgICBmb28oKTtcbn0gZWxzZSBpZiAoYiAmJiBjKSB7XG4gICAgYmFyKCk7XG59IGVsc2UgaWYgKGQgJiYgKGMgJiYgZSAmJiBiIHx8IGEpKSB7XG4gICAgYmF6KCk7XG59In0=)

```
/*eslint no-dupe-else-if: "error"*/

if (a || b) {
    foo();
} else if (a) {
    bar();
}

if (a) {
    foo();
} else if (b) {
    bar();
} else if (a || b) {
    baz();
}

if (a) {
    foo();
} else if (a && b) {
    bar();
}

if (a && b) {
    foo();
} else if (a && b && c) {
    bar();
}

if (a || b) {
    foo();
} else if (b && c) {
    bar();
}

if (a) {
    foo();
} else if (b && c) {
    bar();
} else if (d && (c && e && b || a)) {
    baz();
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
```

Please note that this rule does not compare conditions from the chain with conditions inside statements, and will not warn in the cases such as follows:

```
if (a) {
    if (a) {
        foo();
    }
}

if (a) {
    foo();
} else {
    if (a) {
        bar();
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
```

Copy code to clipboard

## When Not To Use It

In rare cases where you really need identical test conditions in the same chain, which necessarily means that the expressions in the chain are causing and relying on side effects, you will have to turn this rule off.

## Related Rules

- [no-duplicate-case](/docs/latest/rules/no-duplicate-case)
- [no-lonely-if](/docs/latest/rules/no-lonely-if)

## Version

This rule was introduced in ESLint v6.7.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-dupe-else-if.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-dupe-else-if.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-dupe-else-if.md
                    
                
                )
