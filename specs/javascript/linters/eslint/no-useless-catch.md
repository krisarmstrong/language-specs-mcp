# no-useless-catch

Disallow unnecessary `catch` clauses

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

A `catch` clause that only rethrows the original error is redundant, and has no effect on the runtime behavior of the program. These redundant clauses can be a source of confusion and code bloat, so it’s better to disallow these unnecessary `catch` clauses.

## Rule Details

This rule reports `catch` clauses that only `throw` the caught error.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jYXRjaDogXCJlcnJvclwiKi9cblxudHJ5IHtcbiAgZG9Tb21ldGhpbmdUaGF0TWlnaHRUaHJvdygpO1xufSBjYXRjaCAoZSkge1xuICB0aHJvdyBlO1xufVxuXG50cnkge1xuICBkb1NvbWV0aGluZ1RoYXRNaWdodFRocm93KCk7XG59IGNhdGNoIChlKSB7XG4gIHRocm93IGU7XG59IGZpbmFsbHkge1xuICBjbGVhblVwKCk7XG59In0=)

```
/*eslint no-useless-catch: "error"*/

try {
  doSomethingThatMightThrow();
} catch (e) {
  throw e;
}

try {
  doSomethingThatMightThrow();
} catch (e) {
  throw e;
} finally {
  cleanUp();
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jYXRjaDogXCJlcnJvclwiKi9cblxudHJ5IHtcbiAgZG9Tb21ldGhpbmdUaGF0TWlnaHRUaHJvdygpO1xufSBjYXRjaCAoZSkge1xuICBkb1NvbWV0aGluZ0JlZm9yZVJldGhyb3coKTtcbiAgdGhyb3cgZTtcbn1cblxudHJ5IHtcbiAgZG9Tb21ldGhpbmdUaGF0TWlnaHRUaHJvdygpO1xufSBjYXRjaCAoZSkge1xuICBoYW5kbGVFcnJvcihlKTtcbn1cblxudHJ5IHtcbiAgZG9Tb21ldGhpbmdUaGF0TWlnaHRUaHJvdygpO1xufSBmaW5hbGx5IHtcbiAgY2xlYW5VcCgpO1xufSJ9)

```
/*eslint no-useless-catch: "error"*/

try {
  doSomethingThatMightThrow();
} catch (e) {
  doSomethingBeforeRethrow();
  throw e;
}

try {
  doSomethingThatMightThrow();
} catch (e) {
  handleError(e);
}

try {
  doSomethingThatMightThrow();
} finally {
  cleanUp();
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
```

## When Not To Use It

If you don’t want to be notified about unnecessary catch clauses, you can safely disable this rule.

## Version

This rule was introduced in ESLint v5.11.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-catch.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-catch.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-catch.md
                    
                
                )
