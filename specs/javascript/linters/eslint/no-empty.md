# no-empty

Disallow empty block statements

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowEmptyCatch](#allowemptycatch)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Empty block statements, while not technically errors, usually occur due to refactoring that wasn’t completed. They can cause confusion when reading code.

## Rule Details

This rule disallows empty block statements. This rule ignores block statements which contain a comment (for example, in an empty `catch` or `finally` block of a `try` statement to indicate that execution should continue regardless of errors).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHk6IFwiZXJyb3JcIiovXG5cbmlmIChmb28pIHtcbn1cblxud2hpbGUgKGZvbykge1xufVxuXG5zd2l0Y2goZm9vKSB7XG59XG5cbnRyeSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2goZXgpIHtcblxufSBmaW5hbGx5IHtcblxufSJ9)

```
/*eslint no-empty: "error"*/

if (foo) {
}

while (foo) {
}

switch(foo) {
}

try {
    doSomething();
} catch(ex) {

} finally {

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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHk6IFwiZXJyb3JcIiovXG5cbmlmIChmb28pIHtcbiAgICAvLyBlbXB0eVxufVxuXG53aGlsZSAoZm9vKSB7XG4gICAgLyogZW1wdHkgKi9cbn1cblxuc3dpdGNoKGZvbykge1xuICAgIC8qIGVtcHR5ICovXG59XG5cbnRyeSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2ggKGV4KSB7XG4gICAgLy8gY29udGludWUgcmVnYXJkbGVzcyBvZiBlcnJvclxufVxuXG50cnkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IGZpbmFsbHkge1xuICAgIC8qIGNvbnRpbnVlIHJlZ2FyZGxlc3Mgb2YgZXJyb3IgKi9cbn0ifQ==)

```
/*eslint no-empty: "error"*/

if (foo) {
    // empty
}

while (foo) {
    /* empty */
}

switch(foo) {
    /* empty */
}

try {
    doSomething();
} catch (ex) {
    // continue regardless of error
}

try {
    doSomething();
} finally {
    /* continue regardless of error */
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

## Options

This rule has an object option for exceptions:

- `"allowEmptyCatch": true` allows empty `catch` clauses (that is, which do not contain a comment)

### allowEmptyCatch

Examples of additional correct code for this rule with the `{ "allowEmptyCatch": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWVtcHR5OiBbXCJlcnJvclwiLCB7IFwiYWxsb3dFbXB0eUNhdGNoXCI6IHRydWUgfV0gKi9cbnRyeSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2ggKGV4KSB7fVxuXG50cnkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59XG5jYXRjaCAoZXgpIHt9XG5maW5hbGx5IHtcbiAgICAvKiBjb250aW51ZSByZWdhcmRsZXNzIG9mIGVycm9yICovXG59In0=)

```
/* eslint no-empty: ["error", { "allowEmptyCatch": true }] */
try {
    doSomething();
} catch (ex) {}

try {
    doSomething();
}
catch (ex) {}
finally {
    /* continue regardless of error */
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

## When Not To Use It

If you intentionally use empty block statements then you can disable this rule.

## Related Rules

- [no-empty-function](/docs/latest/rules/no-empty-function)

## Version

This rule was introduced in ESLint v0.0.2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-empty.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-empty.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-empty.md
                    
                
                )
