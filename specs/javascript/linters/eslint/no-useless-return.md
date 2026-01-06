# no-useless-return

Disallow redundant return statements

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

A `return;` statement with nothing after it is redundant, and has no effect on the runtime behavior of a function. This can be confusing, so it’s better to disallow these redundant statements.

## Rule Details

This rule aims to report redundant `return` statements.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXVzZWxlc3MtcmV0dXJuOiBcImVycm9yXCIgKi9cblxuY29uc3QgZm9vID0gZnVuY3Rpb24oKSB7IHJldHVybjsgfVxuXG5jb25zdCBiYXIgPSBmdW5jdGlvbigpIHtcbiAgZG9Tb21ldGhpbmcoKTtcbiAgcmV0dXJuO1xufVxuXG5jb25zdCBiYXogPSBmdW5jdGlvbigpIHtcbiAgaWYgKGNvbmRpdGlvbikge1xuICAgIHF1eCgpO1xuICAgIHJldHVybjtcbiAgfSBlbHNlIHtcbiAgICBxdXV4KCk7XG4gIH1cbn1cblxuY29uc3QgaXRlbSA9IGZ1bmN0aW9uKCkge1xuICBzd2l0Y2ggKGJhcikge1xuICAgIGNhc2UgMTpcbiAgICAgIGRvU29tZXRoaW5nKCk7XG4gICAgZGVmYXVsdDpcbiAgICAgIGRvU29tZXRoaW5nRWxzZSgpO1xuICAgICAgcmV0dXJuO1xuICB9XG59XG4ifQ==)

```
/* eslint no-useless-return: "error" */

const foo = function() { return; }

const bar = function() {
  doSomething();
  return;
}

const baz = function() {
  if (condition) {
    qux();
    return;
  } else {
    quux();
  }
}

const item = function() {
  switch (bar) {
    case 1:
      doSomething();
    default:
      doSomethingElse();
      return;
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXVzZWxlc3MtcmV0dXJuOiBcImVycm9yXCIgKi9cblxuY29uc3QgZm9vID0gZnVuY3Rpb24oKSB7IHJldHVybiA1OyB9XG5cbmNvbnN0IGJhciA9IGZ1bmN0aW9uKCkge1xuICByZXR1cm4gZG9Tb21ldGhpbmcoKTtcbn1cblxuY29uc3QgYmF6ID0gZnVuY3Rpb24oKSB7XG4gIGlmIChjb25kaXRpb24pIHtcbiAgICBxdXgoKTtcbiAgICByZXR1cm47XG4gIH0gZWxzZSB7XG4gICAgcXV1eCgpO1xuICB9XG4gIHF1eCgpO1xufVxuXG5jb25zdCBpdGVtID0gZnVuY3Rpb24oKSB7XG4gIHN3aXRjaCAoYmFyKSB7XG4gICAgY2FzZSAxOlxuICAgICAgZG9Tb21ldGhpbmcoKTtcbiAgICAgIHJldHVybjtcbiAgICBkZWZhdWx0OlxuICAgICAgZG9Tb21ldGhpbmdFbHNlKCk7XG4gIH1cbn1cblxuY29uc3QgZnVuYyA9IGZ1bmN0aW9uKCkge1xuICBmb3IgKGNvbnN0IGZvbyBvZiBiYXIpIHtcbiAgICByZXR1cm47XG4gIH1cbn1cbiJ9)

```
/* eslint no-useless-return: "error" */

const foo = function() { return 5; }

const bar = function() {
  return doSomething();
}

const baz = function() {
  if (condition) {
    qux();
    return;
  } else {
    quux();
  }
  qux();
}

const item = function() {
  switch (bar) {
    case 1:
      doSomething();
      return;
    default:
      doSomethingElse();
  }
}

const func = function() {
  for (const foo of bar) {
    return;
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
```

## When Not To Use It

If you don’t care about disallowing redundant return statements, you can turn off this rule.

## Version

This rule was introduced in ESLint v3.9.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-return.md
                    
                
                )
