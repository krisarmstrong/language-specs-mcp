# no-class-assign

Disallow reassigning class members

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Handled by TypeScript](#handled_by_typescript)
4. [Version](#version)
5. [Resources](#resources)

`ClassDeclaration` creates a variable, and we can modify the variable.

```
class A { }
A = 0;
1
2
```

Copy code to clipboard

But the modification is a mistake in most cases.

## Rule Details

This rule is aimed to flag modifying variables of class declarations.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiBcImVycm9yXCIqL1xuXG5jbGFzcyBBIHsgfVxuQSA9IDA7In0=)

```
/*eslint no-class-assign: "error"*/

class A { }
A = 0;
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiBcImVycm9yXCIqL1xuXG5BID0gMDtcbmNsYXNzIEEgeyB9In0=)

```
/*eslint no-class-assign: "error"*/

A = 0;
class A { }
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiBcImVycm9yXCIqL1xuXG5jbGFzcyBBIHtcbiAgICBiKCkge1xuICAgICAgICBBID0gMDtcbiAgICB9XG59In0=)

```
/*eslint no-class-assign: "error"*/

class A {
    b() {
        A = 0;
    }
}
1
2
3
4
5
6
7
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiBcImVycm9yXCIqL1xuXG5sZXQgQSA9IGNsYXNzIEEge1xuICAgIGIoKSB7XG4gICAgICAgIEEgPSAwO1xuICAgICAgICAvLyBgbGV0IEFgIGlzIHNoYWRvd2VkIGJ5IHRoZSBjbGFzcyBuYW1lLlxuICAgIH1cbn0ifQ==)

```
/*eslint no-class-assign: "error"*/

let A = class A {
    b() {
        A = 0;
        // `let A` is shadowed by the class name.
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiBcImVycm9yXCIqL1xuXG5sZXQgQSA9IGNsYXNzIEEgeyB9XG5BID0gMDsgLy8gQSBpcyBhIHZhcmlhYmxlLiJ9)

```
/*eslint no-class-assign: "error"*/

let A = class A { }
A = 0; // A is a variable.
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiBcImVycm9yXCIqL1xuXG5sZXQgQSA9IGNsYXNzIHtcbiAgICBiKCkge1xuICAgICAgICBBID0gMDsgLy8gQSBpcyBhIHZhcmlhYmxlLlxuICAgIH1cbn0ifQ==)

```
/*eslint no-class-assign: "error"*/

let A = class {
    b() {
        A = 0; // A is a variable.
    }
}
1
2
3
4
5
6
7
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2xhc3MtYXNzaWduOiAyKi9cblxuY2xhc3MgQSB7XG4gICAgYihBKSB7XG4gICAgICAgIEEgPSAwOyAvLyBBIGlzIGEgcGFyYW1ldGVyLlxuICAgIH1cbn0ifQ==)

```
/*eslint no-class-assign: 2*/

class A {
    b(A) {
        A = 0; // A is a parameter.
    }
}
1
2
3
4
5
6
7
```

## When Not To Use It

If you don’t want to be notified about modifying variables of class declarations, you can safely disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v1.0.0-rc-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-class-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-class-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-class-assign.md
                    
                
                )
