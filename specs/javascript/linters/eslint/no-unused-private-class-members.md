# no-unused-private-class-members

Disallow unused private class members

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

Private class members that are declared and not used anywhere in the code are most likely an error due to incomplete refactoring. Such class members take up space in the code and can lead to confusion by readers.

## Rule Details

This rule reports unused private class members.

- A private field or method is considered to be unused if its value is never read.
- A private accessor is considered to be unused if it is never accessed (read or write).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXByaXZhdGUtY2xhc3MtbWVtYmVyczogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7XG4gICAgI3VudXNlZE1lbWJlciA9IDU7XG59XG5cbmNsYXNzIEIge1xuICAgICN1c2VkT25seUluV3JpdGUgPSA1O1xuICAgIG1ldGhvZCgpIHtcbiAgICAgICAgdGhpcy4jdXNlZE9ubHlJbldyaXRlID0gNDI7XG4gICAgfVxufVxuXG5jbGFzcyBDIHtcbiAgICAjdXNlZE9ubHlUb1VwZGF0ZUl0c2VsZiA9IDU7XG4gICAgbWV0aG9kKCkge1xuICAgICAgICB0aGlzLiN1c2VkT25seVRvVXBkYXRlSXRzZWxmKys7XG4gICAgfVxufVxuXG5jbGFzcyBEIHtcbiAgICAjdW51c2VkTWV0aG9kKCkge31cbn1cblxuY2xhc3MgRSB7XG4gICAgZ2V0ICN1bnVzZWRBY2Nlc3NvcigpIHt9XG4gICAgc2V0ICN1bnVzZWRBY2Nlc3Nvcih2YWx1ZSkge31cbn0ifQ==)

```
/*eslint no-unused-private-class-members: "error"*/

class A {
    #unusedMember = 5;
}

class B {
    #usedOnlyInWrite = 5;
    method() {
        this.#usedOnlyInWrite = 42;
    }
}

class C {
    #usedOnlyToUpdateItself = 5;
    method() {
        this.#usedOnlyToUpdateItself++;
    }
}

class D {
    #unusedMethod() {}
}

class E {
    get #unusedAccessor() {}
    set #unusedAccessor(value) {}
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXByaXZhdGUtY2xhc3MtbWVtYmVyczogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7XG4gICAgI3VzZWRNZW1iZXIgPSA0MjtcbiAgICBtZXRob2QoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLiN1c2VkTWVtYmVyO1xuICAgIH1cbn1cblxuY2xhc3MgQiB7XG4gICAgI3VzZWRNZXRob2QoKSB7XG4gICAgICAgIHJldHVybiA0MjtcbiAgICB9XG4gICAgYW5vdGhlck1ldGhvZCgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMuI3VzZWRNZXRob2QoKTtcbiAgICB9XG59XG5cbmNsYXNzIEMge1xuICAgIGdldCAjdXNlZEFjY2Vzc29yKCkge31cbiAgICBzZXQgI3VzZWRBY2Nlc3Nvcih2YWx1ZSkge31cbiAgICBcbiAgICBtZXRob2QoKSB7XG4gICAgICAgIHRoaXMuI3VzZWRBY2Nlc3NvciA9IDQyO1xuICAgIH1cbn0ifQ==)

```
/*eslint no-unused-private-class-members: "error"*/

class A {
    #usedMember = 42;
    method() {
        return this.#usedMember;
    }
}

class B {
    #usedMethod() {
        return 42;
    }
    anotherMethod() {
        return this.#usedMethod();
    }
}

class C {
    get #usedAccessor() {}
    set #usedAccessor(value) {}
    
    method() {
        this.#usedAccessor = 42;
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
```

## When Not To Use It

If you don’t want to be notified about unused private class members, you can safely turn this rule off.

## Version

This rule was introduced in ESLint v8.1.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unused-private-class-members.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unused-private-class-members.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unused-private-class-members.md
                    
                
                )
