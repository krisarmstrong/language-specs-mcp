# no-constructor-return

Disallow returning value from constructor

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

In JavaScript, returning a value in the constructor of a class may be a mistake. Forbidding this pattern prevents mistakes resulting from unfamiliarity with the language or a copy-paste error.

## Rule Details

This rule disallows return statements in the constructor of a class. Note that returning nothing is allowed.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RydWN0b3ItcmV0dXJuOiBcImVycm9yXCIqL1xuXG5jbGFzcyBBIHtcbiAgICBjb25zdHJ1Y3RvcihhKSB7XG4gICAgICAgIHRoaXMuYSA9IGE7XG4gICAgICAgIHJldHVybiBhO1xuICAgIH1cbn1cblxuY2xhc3MgQiB7XG4gICAgY29uc3RydWN0b3IoZikge1xuICAgICAgICBpZiAoIWYpIHtcbiAgICAgICAgICAgIHJldHVybiAnZmFsc3knO1xuICAgICAgICB9XG4gICAgfVxufSJ9)

```
/*eslint no-constructor-return: "error"*/

class A {
    constructor(a) {
        this.a = a;
        return a;
    }
}

class B {
    constructor(f) {
        if (!f) {
            return 'falsy';
        }
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RydWN0b3ItcmV0dXJuOiBcImVycm9yXCIqL1xuXG5jbGFzcyBDIHtcbiAgICBjb25zdHJ1Y3RvcihjKSB7XG4gICAgICAgIHRoaXMuYyA9IGM7XG4gICAgfVxufVxuXG5jbGFzcyBEIHtcbiAgICBjb25zdHJ1Y3RvcihmKSB7XG4gICAgICAgIGlmICghZikge1xuICAgICAgICAgICAgcmV0dXJuOyAgLy8gRmxvdyBjb250cm9sLlxuICAgICAgICB9XG5cbiAgICAgICAgZigpO1xuICAgIH1cbn1cblxuY2xhc3MgRSB7XG4gICAgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIHJldHVybjtcbiAgICB9XG59XG4ifQ==)

```
/*eslint no-constructor-return: "error"*/

class C {
    constructor(c) {
        this.c = c;
    }
}

class D {
    constructor(f) {
        if (!f) {
            return;  // Flow control.
        }

        f();
    }
}

class E {
    constructor() {
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
```

## Version

This rule was introduced in ESLint v6.7.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-constructor-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-constructor-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-constructor-return.md
                    
                
                )
