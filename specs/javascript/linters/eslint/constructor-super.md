# constructor-super

Require `super()` calls in constructors

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Handled by TypeScript](#handled_by_typescript)
4. [Version](#version)
5. [Resources](#resources)

Constructors of derived classes must call `super()`. Constructors of non derived classes must not call `super()`. If this is not observed, the JavaScript engine will raise a runtime error.

This rule checks whether or not there is a valid `super()` call.

## Rule Details

This rule is aimed to flag invalid/missing `super()` calls.

This is a syntax error because there is no `extends` clause in the class:

```
class A {
    constructor() {
        super();
    }
}
1
2
3
4
5
```

Copy code to clipboard

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc3RydWN0b3Itc3VwZXI6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEEgZXh0ZW5kcyBCIHtcbiAgICBjb25zdHJ1Y3RvcigpIHsgfSAgLy8gV291bGQgdGhyb3cgYSBSZWZlcmVuY2VFcnJvci5cbn1cblxuLy8gQ2xhc3NlcyB3aGljaCBpbmhlcml0cyBmcm9tIGEgbm9uIGNvbnN0cnVjdG9yIGFyZSBhbHdheXMgcHJvYmxlbXMuXG5jbGFzcyBDIGV4dGVuZHMgbnVsbCB7XG4gICAgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIHN1cGVyKCk7ICAvLyBXb3VsZCB0aHJvdyBhIFR5cGVFcnJvci5cbiAgICB9XG59XG5cbmNsYXNzIEQgZXh0ZW5kcyBudWxsIHtcbiAgICBjb25zdHJ1Y3RvcigpIHsgfSAgLy8gV291bGQgdGhyb3cgYSBSZWZlcmVuY2VFcnJvci5cbn0ifQ==)

```
/*eslint constructor-super: "error"*/

class A extends B {
    constructor() { }  // Would throw a ReferenceError.
}

// Classes which inherits from a non constructor are always problems.
class C extends null {
    constructor() {
        super();  // Would throw a TypeError.
    }
}

class D extends null {
    constructor() { }  // Would throw a ReferenceError.
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc3RydWN0b3Itc3VwZXI6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEEge1xuICAgIGNvbnN0cnVjdG9yKCkgeyB9XG59XG5cbmNsYXNzIEIgZXh0ZW5kcyBDIHtcbiAgICBjb25zdHJ1Y3RvcigpIHtcbiAgICAgICAgc3VwZXIoKTtcbiAgICB9XG59In0=)

```
/*eslint constructor-super: "error"*/

class A {
    constructor() { }
}

class B extends C {
    constructor() {
        super();
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
```

## When Not To Use It

If you don’t want to be notified about invalid/missing `super()` callings in constructors, you can safely disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v0.24.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/constructor-super.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/constructor-super.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/constructor-super.md
                    
                
                )
