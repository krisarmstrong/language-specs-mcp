# no-useless-constructor

Disallow unnecessary constructors

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

ES2015 provides a default class constructor if one is not specified. As such, it is unnecessary to provide an empty constructor or one that simply delegates into its parent class, as in the following examples:

```
class A {
    constructor () {
    }
}

class B extends A {
    constructor (value) {
      super(value);
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
```

Copy code to clipboard

## Rule Details

This rule flags class constructors that can be safely removed without changing how the class works.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb25zdHJ1Y3RvcjogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7XG4gICAgY29uc3RydWN0b3IgKCkge1xuICAgIH1cbn1cblxuY2xhc3MgQiBleHRlbmRzIEEge1xuICAgIGNvbnN0cnVjdG9yICguLi5hcmdzKSB7XG4gICAgICBzdXBlciguLi5hcmdzKTtcbiAgICB9XG59In0=)

```
/*eslint no-useless-constructor: "error"*/

class A {
    constructor () {
    }
}

class B extends A {
    constructor (...args) {
      super(...args);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb25zdHJ1Y3RvcjogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7IH1cblxuY2xhc3MgQiB7XG4gICAgY29uc3RydWN0b3IgKCkge1xuICAgICAgICBkb1NvbWV0aGluZygpO1xuICAgIH1cbn1cblxuY2xhc3MgQyBleHRlbmRzIEEge1xuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICBzdXBlcignZm9vJyk7XG4gICAgfVxufVxuXG5jbGFzcyBEIGV4dGVuZHMgQSB7XG4gICAgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIHN1cGVyKCk7XG4gICAgICAgIGRvU29tZXRoaW5nKCk7XG4gICAgfVxufSJ9)

```
/*eslint no-useless-constructor: "error"*/

class A { }

class B {
    constructor () {
        doSomething();
    }
}

class C extends A {
    constructor() {
        super('foo');
    }
}

class D extends A {
    constructor() {
        super();
        doSomething();
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
```

This rule additionally supports TypeScript type syntax.

Examples of incorrect TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgbm8tdXNlbGVzcy1jb25zdHJ1Y3RvcjogXCJlcnJvclwiICovXG5cbmNsYXNzIEEge1xuICAgIHB1YmxpYyBjb25zdHJ1Y3RvcigpIHt9XG59In0=)

```
/* eslint no-useless-constructor: "error" */

class A {
    public constructor() {}
}
1
2
3
4
5
```

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgbm8tdXNlbGVzcy1jb25zdHJ1Y3RvcjogXCJlcnJvclwiICovXG5cbmNsYXNzIEEge1xuICAgIHByb3RlY3RlZCBjb25zdHJ1Y3RvcigpIHt9XG59XG5cbmNsYXNzIEIgZXh0ZW5kcyBBIHtcbiAgICBwdWJsaWMgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIHN1cGVyKCk7XG4gICAgfVxufVxuXG5jbGFzcyBDIHtcbiAgICBjb25zdHJ1Y3RvcihAZGVjb3JhdGVkIHBhcmFtKSB7fVxufSJ9)

```
/* eslint no-useless-constructor: "error" */

class A {
    protected constructor() {}
}

class B extends A {
    public constructor() {
        super();
    }
}

class C {
    constructor(@decorated param) {}
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

## When Not To Use It

If you don’t want to be notified about unnecessary constructors, you can safely disable this rule.

## Version

This rule was introduced in ESLint v2.0.0-beta.1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-constructor.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-constructor.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-constructor.md
                    
                
                )
