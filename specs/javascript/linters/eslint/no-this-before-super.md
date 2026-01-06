# no-this-before-super

Disallow `this`/`super` before calling `super()` in constructors

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Handled by TypeScript](#handled_by_typescript)
5. [Version](#version)
6. [Resources](#resources)

In the constructor of derived classes, if `this`/`super` are used before `super()` calls, it raises a reference error.

This rule checks `this`/`super` keywords in constructors, then reports those that are before `super()`.

## Rule Details

This rule is aimed to flag `this`/`super` keywords before `super()` callings.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGhpcy1iZWZvcmUtc3VwZXI6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEExIGV4dGVuZHMgQiB7XG4gICAgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIHRoaXMuYSA9IDA7XG4gICAgICAgIHN1cGVyKCk7XG4gICAgfVxufVxuXG5jbGFzcyBBMiBleHRlbmRzIEIge1xuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICB0aGlzLmZvbygpO1xuICAgICAgICBzdXBlcigpO1xuICAgIH1cbn1cblxuY2xhc3MgQTMgZXh0ZW5kcyBCIHtcbiAgICBjb25zdHJ1Y3RvcigpIHtcbiAgICAgICAgc3VwZXIuZm9vKCk7XG4gICAgICAgIHN1cGVyKCk7XG4gICAgfVxufVxuXG5jbGFzcyBBNCBleHRlbmRzIEIge1xuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICBzdXBlcih0aGlzLmZvbygpKTtcbiAgICB9XG59In0=)

```
/*eslint no-this-before-super: "error"*/

class A1 extends B {
    constructor() {
        this.a = 0;
        super();
    }
}

class A2 extends B {
    constructor() {
        this.foo();
        super();
    }
}

class A3 extends B {
    constructor() {
        super.foo();
        super();
    }
}

class A4 extends B {
    constructor() {
        super(this.foo());
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGhpcy1iZWZvcmUtc3VwZXI6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEExIHtcbiAgICBjb25zdHJ1Y3RvcigpIHtcbiAgICAgICAgdGhpcy5hID0gMDsgLy8gT0ssIHRoaXMgY2xhc3MgZG9lc24ndCBoYXZlIGFuIGBleHRlbmRzYCBjbGF1c2UuXG4gICAgfVxufVxuXG5jbGFzcyBBMiBleHRlbmRzIEIge1xuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICBzdXBlcigpO1xuICAgICAgICB0aGlzLmEgPSAwOyAvLyBPSywgdGhpcyBpcyBhZnRlciBgc3VwZXIoKWAuXG4gICAgfVxufVxuXG5jbGFzcyBBMyBleHRlbmRzIEIge1xuICAgIGZvbygpIHtcbiAgICAgICAgdGhpcy5hID0gMDsgLy8gT0suIHRoaXMgaXMgbm90IGluIGEgY29uc3RydWN0b3IuXG4gICAgfVxufSJ9)

```
/*eslint no-this-before-super: "error"*/

class A1 {
    constructor() {
        this.a = 0; // OK, this class doesn't have an `extends` clause.
    }
}

class A2 extends B {
    constructor() {
        super();
        this.a = 0; // OK, this is after `super()`.
    }
}

class A3 extends B {
    foo() {
        this.a = 0; // OK. this is not in a constructor.
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
```

## When Not To Use It

If you don’t want to be notified about using `this`/`super` before `super()` in constructors, you can safely disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v0.24.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-this-before-super.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-this-before-super.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-this-before-super.md
                    
                
                )
