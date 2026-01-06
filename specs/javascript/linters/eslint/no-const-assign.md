# no-const-assign

Disallow reassigning `const`, `using`, and `await using` variables

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Handled by TypeScript](#handled_by_typescript)
4. [Version](#version)
5. [Resources](#resources)

Constant bindings cannot be modified. An attempt to modify a constant binding will raise a runtime error.

## Rule Details

This rule is aimed to flag modifying variables that are declared using `const`, `using`, or `await using` keywords.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5jb25zdCBhID0gMDtcbmEgPSAxOyJ9)

```
/*eslint no-const-assign: "error"*/

const a = 0;
a = 1;
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5jb25zdCBhID0gMDtcbmEgKz0gMTsifQ==)

```
/*eslint no-const-assign: "error"*/

const a = 0;
a += 1;
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5jb25zdCBhID0gMDtcbisrYTsifQ==)

```
/*eslint no-const-assign: "error"*/

const a = 0;
++a;
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5pZiAoZm9vKSB7XG5cdHVzaW5nIGEgPSBnZXRTb21ldGhpbmcoKTtcblx0YSA9IHNvbWV0aGluZ0Vsc2U7XG59XG5cbmlmIChiYXIpIHtcblx0YXdhaXQgdXNpbmcgYSA9IGdldFNvbWV0aGluZygpO1xuXHRhID0gc29tZXRoaW5nRWxzZTtcbn0ifQ==)

```
/*eslint no-const-assign: "error"*/

if (foo) {
	using a = getSomething();
	a = somethingElse;
}

if (bar) {
	await using a = getSomething();
	a = somethingElse;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5jb25zdCBhID0gMDtcbmNvbnNvbGUubG9nKGEpOyJ9)

```
/*eslint no-const-assign: "error"*/

const a = 0;
console.log(a);
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5pZiAoZm9vKSB7XG5cdHVzaW5nIGEgPSBnZXRTb21ldGhpbmcoKTtcblx0YS5leGVjdXRlKCk7XG59XG5cbmlmIChiYXIpIHtcblx0YXdhaXQgdXNpbmcgYSA9IGdldFNvbWV0aGluZygpO1xuXHRhLmV4ZWN1dGUoKTtcbn0ifQ==)

```
/*eslint no-const-assign: "error"*/

if (foo) {
	using a = getSomething();
	a.execute();
}

if (bar) {
	await using a = getSomething();
	a.execute();
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5mb3IgKGNvbnN0IGEgaW4gWzEsIDIsIDNdKSB7IC8vIGBhYCBpcyByZS1kZWZpbmVkIChub3QgbW9kaWZpZWQpIG9uIGVhY2ggbG9vcCBzdGVwLlxuICAgIGNvbnNvbGUubG9nKGEpO1xufSJ9)

```
/*eslint no-const-assign: "error"*/

for (const a in [1, 2, 3]) { // `a` is re-defined (not modified) on each loop step.
    console.log(a);
}
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3QtYXNzaWduOiBcImVycm9yXCIqL1xuXG5mb3IgKGNvbnN0IGEgb2YgWzEsIDIsIDNdKSB7IC8vIGBhYCBpcyByZS1kZWZpbmVkIChub3QgbW9kaWZpZWQpIG9uIGVhY2ggbG9vcCBzdGVwLlxuICAgIGNvbnNvbGUubG9nKGEpO1xufSJ9)

```
/*eslint no-const-assign: "error"*/

for (const a of [1, 2, 3]) { // `a` is re-defined (not modified) on each loop step.
    console.log(a);
}
1
2
3
4
5
```

## When Not To Use It

If you don’t want to be notified about modifying variables that are declared using `const`, `using`, and `await using` keywords, you can safely disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v1.0.0-rc-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-const-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-const-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-const-assign.md
                    
                
                )
