# no-useless-assignment

Disallow variable assignments when the value is not used

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

[Wikipedia describes a “dead store”](https://en.wikipedia.org/wiki/Dead_store) as follows:

In computer programming, a local variable that is assigned a value but is not read by any subsequent instruction is referred to as a dead store.

“Dead stores” waste processing and memory, so it is better to remove unnecessary assignments to variables.

Also, if the author intended the variable to be used, there is likely a mistake around the dead store. For example,

- you should have used a stored value but forgot to do so.
- you made a mistake in the name of the variable to be stored.

```
let id = "x1234";    // this is a "dead store" - this value ("x1234") is never read

id = generateId();

doSomethingWith(id);
1
2
3
4
5
```

Copy code to clipboard

## Rule Details

This rule aims to report variable assignments when the value is not used.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXVzZWxlc3MtYXNzaWdubWVudDogXCJlcnJvclwiICovXG5cbmZ1bmN0aW9uIGZuMSgpIHtcbiAgICBsZXQgdiA9ICd1c2VkJztcbiAgICBkb1NvbWV0aGluZyh2KTtcbiAgICB2ID0gJ3VudXNlZCc7XG59XG5cbmZ1bmN0aW9uIGZuMigpIHtcbiAgICBsZXQgdiA9ICd1c2VkJztcbiAgICBpZiAoY29uZGl0aW9uKSB7XG4gICAgICAgIHYgPSAndW51c2VkJztcbiAgICAgICAgcmV0dXJuXG4gICAgfVxuICAgIGRvU29tZXRoaW5nKHYpO1xufVxuXG5mdW5jdGlvbiBmbjMoKSB7XG4gICAgbGV0IHYgPSAndXNlZCc7XG4gICAgaWYgKGNvbmRpdGlvbikge1xuICAgICAgICBkb1NvbWV0aGluZyh2KTtcbiAgICB9IGVsc2Uge1xuICAgICAgICB2ID0gJ3VudXNlZCc7XG4gICAgfVxufVxuXG5mdW5jdGlvbiBmbjQoKSB7XG4gICAgbGV0IHYgPSAndW51c2VkJztcbiAgICBpZiAoY29uZGl0aW9uKSB7XG4gICAgICAgIHYgPSAndXNlZCc7XG4gICAgICAgIGRvU29tZXRoaW5nKHYpO1xuICAgICAgICByZXR1cm5cbiAgICB9XG59XG5cbmZ1bmN0aW9uIGZuNSgpIHtcbiAgICBsZXQgdiA9ICd1c2VkJztcbiAgICBpZiAoY29uZGl0aW9uKSB7XG4gICAgICAgIGxldCB2ID0gJ3VzZWQnO1xuICAgICAgICBjb25zb2xlLmxvZyh2KTtcbiAgICAgICAgdiA9ICd1bnVzZWQnO1xuICAgIH1cbiAgICBjb25zb2xlLmxvZyh2KTtcbn0ifQ==)

```
/* eslint no-useless-assignment: "error" */

function fn1() {
    let v = 'used';
    doSomething(v);
    v = 'unused';
}

function fn2() {
    let v = 'used';
    if (condition) {
        v = 'unused';
        return
    }
    doSomething(v);
}

function fn3() {
    let v = 'used';
    if (condition) {
        doSomething(v);
    } else {
        v = 'unused';
    }
}

function fn4() {
    let v = 'unused';
    if (condition) {
        v = 'used';
        doSomething(v);
        return
    }
}

function fn5() {
    let v = 'used';
    if (condition) {
        let v = 'used';
        console.log(v);
        v = 'unused';
    }
    console.log(v);
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
35
36
37
38
39
40
41
42
43
44
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXVzZWxlc3MtYXNzaWdubWVudDogXCJlcnJvclwiICovXG5cbmZ1bmN0aW9uIGZuMSgpIHtcbiAgICBsZXQgdiA9ICd1c2VkJztcbiAgICBkb1NvbWV0aGluZyh2KTtcbiAgICB2ID0gJ3VzZWQtMic7XG4gICAgZG9Tb21ldGhpbmcodik7XG59XG5cbmZ1bmN0aW9uIGZuMigpIHtcbiAgICBsZXQgdiA9ICd1c2VkJztcbiAgICBpZiAoY29uZGl0aW9uKSB7XG4gICAgICAgIHYgPSAndXNlZC0yJztcbiAgICAgICAgZG9Tb21ldGhpbmcodik7XG4gICAgICAgIHJldHVyblxuICAgIH1cbiAgICBkb1NvbWV0aGluZyh2KTtcbn1cblxuZnVuY3Rpb24gZm4zKCkge1xuICAgIGxldCB2ID0gJ3VzZWQnO1xuICAgIGlmIChjb25kaXRpb24pIHtcbiAgICAgICAgZG9Tb21ldGhpbmcodik7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgdiA9ICd1c2VkLTInO1xuICAgICAgICBkb1NvbWV0aGluZyh2KTtcbiAgICB9XG59XG5cbmZ1bmN0aW9uIGZuNCgpIHtcbiAgICBsZXQgdiA9ICd1c2VkJztcbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IDEwOyBpKyspIHtcbiAgICAgICAgZG9Tb21ldGhpbmcodik7XG4gICAgICAgIHYgPSAndXNlZCBpbiBuZXh0IGl0ZXJhdGlvbic7XG4gICAgfVxufSJ9)

```
/* eslint no-useless-assignment: "error" */

function fn1() {
    let v = 'used';
    doSomething(v);
    v = 'used-2';
    doSomething(v);
}

function fn2() {
    let v = 'used';
    if (condition) {
        v = 'used-2';
        doSomething(v);
        return
    }
    doSomething(v);
}

function fn3() {
    let v = 'used';
    if (condition) {
        doSomething(v);
    } else {
        v = 'used-2';
        doSomething(v);
    }
}

function fn4() {
    let v = 'used';
    for (let i = 0; i < 10; i++) {
        doSomething(v);
        v = 'used in next iteration';
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
35
36
```

This rule will not report variables that are never read. Because it’s clearly an unused variable. If you want it reported, please enable the [no-unused-vars](./no-unused-vars) rule.

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXVzZWxlc3MtYXNzaWdubWVudDogXCJlcnJvclwiICovXG5cbmZ1bmN0aW9uIGZuKCkge1xuICAgIGxldCB2ID0gJ3VudXNlZCc7XG4gICAgdiA9ICd1bnVzZWQtMidcbiAgICBkb1NvbWV0aGluZygpO1xufSJ9)

```
/* eslint no-useless-assignment: "error" */

function fn() {
    let v = 'unused';
    v = 'unused-2'
    doSomething();
}
1
2
3
4
5
6
7
```

## Known Limitations

This rule does not report certain variable reassignments when they occur inside the `try` block. This is intentional because such assignments may still be observed within the corresponding `catch` block or after the `try-catch` structure, due to potential early exits or error handling logic.

```
function foo() {
    let bar;
    try {
        bar = 2;
        unsafeFn();
        return { error: undefined };
    } catch {
        return { bar }; // `bar` is observed in the catch block
    }
}   
function unsafeFn() {
    throw new Error();
}

function foo() {
    let bar;
    try {
        bar = 2; // This assignment is relevant if unsafeFn() throws an error
        unsafeFn();
        bar = 4;
    } catch {
        // Error handling
    }
    return bar;
}   
function unsafeFn() {
    throw new Error();
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

Copy code to clipboard

## When Not To Use It

If you don’t want to be notified about values that are never read, you can safely disable this rule.

## Related Rules

- [no-unused-vars](/docs/latest/rules/no-unused-vars)

## Version

This rule was introduced in ESLint v9.0.0-alpha.1.

## Further Reading

[Dead store - Wikipedia](https://en.wikipedia.org/wiki/Dead_store)
 en.wikipedia.org[JavaScript static code analysis: Unused assignments should be removed](https://rules.sonarsource.com/javascript/RSPEC-1854/)
 rules.sonarsource.com[CWE - CWE-563: Assignment to Variable without Use (4.13)](https://cwe.mitre.org/data/definitions/563.html)
 cwe.mitre.org[MSC13-C. Detect and remove unused values - SEI CERT C Coding Standard - Confluence](https://wiki.sei.cmu.edu/confluence/display/c/MSC13-C.+Detect+and+remove+unused+values)
 wiki.sei.cmu.edu[MSC56-J. Detect and remove superfluous code and values - SEI CERT Oracle Coding Standard for Java - Confluence](https://wiki.sei.cmu.edu/confluence/display/java/MSC56-J.+Detect+and+remove+superfluous+code+and+values)
 wiki.sei.cmu.edu

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-assignment.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-assignment.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-assignment.md
                    
                
                )
