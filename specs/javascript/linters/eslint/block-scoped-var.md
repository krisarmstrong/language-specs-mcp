# block-scoped-var

Enforce the use of variables within the scope they are defined

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Further Reading](#further-reading)
4. [Resources](#resources)

The `block-scoped-var` rule generates warnings when variables are used outside of the block in which they were defined. This emulates C-style block scope.

## Rule Details

This rule aims to reduce the usage of variables outside of their binding context and emulate traditional block scope from other languages. This is to help newcomers to the language avoid difficult bugs with variable hoisting.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYmxvY2stc2NvcGVkLXZhcjogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24gZG9JZigpIHtcbiAgICBpZiAodHJ1ZSkge1xuICAgICAgICB2YXIgYnVpbGQgPSB0cnVlO1xuICAgIH1cblxuICAgIGNvbnNvbGUubG9nKGJ1aWxkKTtcbn1cblxuZnVuY3Rpb24gZG9JZkVsc2UoKSB7XG4gICAgaWYgKHRydWUpIHtcbiAgICAgICAgdmFyIGJ1aWxkID0gdHJ1ZTtcbiAgICB9IGVsc2Uge1xuICAgICAgICB2YXIgYnVpbGQgPSBmYWxzZTtcbiAgICB9XG59XG5cbmZ1bmN0aW9uIGRvVHJ5Q2F0Y2goKSB7XG4gICAgdHJ5IHtcbiAgICAgICAgdmFyIGJ1aWxkID0gMTtcbiAgICB9IGNhdGNoIChlKSB7XG4gICAgICAgIHZhciBmID0gYnVpbGQ7XG4gICAgfVxufVxuXG5mdW5jdGlvbiBkb0ZvcigpIHtcbiAgICBmb3IgKHZhciB4ID0gMTsgeCA8IDEwOyB4KyspIHtcbiAgICAgICAgdmFyIHkgPSBmKHgpO1xuICAgIH1cbiAgICBjb25zb2xlLmxvZyh5KTtcbn1cblxuY2xhc3MgQyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgaWYgKHNvbWV0aGluZykge1xuICAgICAgICAgICAgdmFyIGJ1aWxkID0gdHJ1ZTtcbiAgICAgICAgfVxuICAgICAgICBidWlsZCA9IGZhbHNlO1xuICAgIH1cbn0ifQ==)

```
/*eslint block-scoped-var: "error"*/

function doIf() {
    if (true) {
        var build = true;
    }

    console.log(build);
}

function doIfElse() {
    if (true) {
        var build = true;
    } else {
        var build = false;
    }
}

function doTryCatch() {
    try {
        var build = 1;
    } catch (e) {
        var f = build;
    }
}

function doFor() {
    for (var x = 1; x < 10; x++) {
        var y = f(x);
    }
    console.log(y);
}

class C {
    static {
        if (something) {
            var build = true;
        }
        build = false;
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
37
38
39
40
41
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYmxvY2stc2NvcGVkLXZhcjogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24gZG9JZigpIHtcbiAgICB2YXIgYnVpbGQ7XG5cbiAgICBpZiAodHJ1ZSkge1xuICAgICAgICBidWlsZCA9IHRydWU7XG4gICAgfVxuXG4gICAgY29uc29sZS5sb2coYnVpbGQpO1xufVxuXG5mdW5jdGlvbiBkb0lmRWxzZSgpIHtcbiAgICB2YXIgYnVpbGQ7XG5cbiAgICBpZiAodHJ1ZSkge1xuICAgICAgICBidWlsZCA9IHRydWU7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgYnVpbGQgPSBmYWxzZTtcbiAgICB9XG59XG5cbmZ1bmN0aW9uIGRvVHJ5Q2F0Y2goKSB7XG4gICAgdmFyIGJ1aWxkO1xuICAgIHZhciBmO1xuXG4gICAgdHJ5IHtcbiAgICAgICAgYnVpbGQgPSAxO1xuICAgIH0gY2F0Y2ggKGUpIHtcbiAgICAgICAgZiA9IGJ1aWxkO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gZG9Gb3IoKSB7XG4gICAgZm9yICh2YXIgeCA9IDE7IHggPCAxMDsgeCsrKSB7XG4gICAgICAgIHZhciB5ID0gZih4KTtcbiAgICAgICAgY29uc29sZS5sb2coeSk7XG4gICAgfVxufVxuXG5jbGFzcyBDIHtcbiAgICBzdGF0aWMge1xuICAgICAgICB2YXIgYnVpbGQgPSBmYWxzZTtcbiAgICAgICAgaWYgKHNvbWV0aGluZykge1xuICAgICAgICAgICAgYnVpbGQgPSB0cnVlO1xuICAgICAgICB9XG4gICAgfVxufSJ9)

```
/*eslint block-scoped-var: "error"*/

function doIf() {
    var build;

    if (true) {
        build = true;
    }

    console.log(build);
}

function doIfElse() {
    var build;

    if (true) {
        build = true;
    } else {
        build = false;
    }
}

function doTryCatch() {
    var build;
    var f;

    try {
        build = 1;
    } catch (e) {
        f = build;
    }
}

function doFor() {
    for (var x = 1; x < 10; x++) {
        var y = f(x);
        console.log(y);
    }
}

class C {
    static {
        var build = false;
        if (something) {
            build = true;
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
45
46
47
48
```

## Version

This rule was introduced in ESLint v0.1.0.

## Further Reading

[JavaScript Scoping and Hoisting](https://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)
 www.adequatelygood.com[var - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#var_hoisting)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/block-scoped-var.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/block-scoped-var.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/block-scoped-var.md
                    
                
                )
