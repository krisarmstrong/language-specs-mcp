# vars-on-top

Require `var` declarations be placed at the top of their containing scope

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Further Reading](#further-reading)
4. [Resources](#resources)

The `vars-on-top` rule generates warnings when variable declarations are not used serially at the top of a function scope or the top of a program. By default variable declarations are always moved (“hoisted”) invisibly to the top of their containing scope by the JavaScript interpreter. This rule forces the programmer to represent that behavior by manually moving the variable declaration to the top of its containing scope.

## Rule Details

This rule aims to keep all variable declarations in the leading series of statements. Allowing multiple declarations helps promote maintainability and is thus allowed.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbi8vIFZhcmlhYmxlIGRlY2xhcmF0aW9uIGluIGEgbmVzdGVkIGJsb2NrLCBhbmQgYSB2YXJpYWJsZSBkZWNsYXJhdGlvbiBhZnRlciBvdGhlciBzdGF0ZW1lbnRzOlxuZnVuY3Rpb24gZG9Tb21ldGhpbmcoKSB7XG4gICAgaWYgKHRydWUpIHtcbiAgICAgICAgdmFyIGZpcnN0ID0gdHJ1ZTtcbiAgICB9XG4gICAgdmFyIHNlY29uZDtcbn1cblxuLy8gVmFyaWFibGUgZGVjbGFyYXRpb24gaW4gZm9yIGluaXRpYWxpemVyOlxuZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkge1xuICAgIGZvciAodmFyIGk9MDsgaTwxMDsgaSsrKSB7fVxufSJ9)

```
/*eslint vars-on-top: "error"*/

// Variable declaration in a nested block, and a variable declaration after other statements:
function doSomething() {
    if (true) {
        var first = true;
    }
    var second;
}

// Variable declaration in for initializer:
function doSomethingElse() {
    for (var i=0; i<10; i++) {}
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
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbi8vIFZhcmlhYmxlIGRlY2xhcmF0aW9uIGFmdGVyIG90aGVyIHN0YXRlbWVudHM6XG5mKCk7XG52YXIgYTsifQ==)

```
/*eslint vars-on-top: "error"*/

// Variable declaration after other statements:
f();
var a;
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbi8vIFZhcmlhYmxlcyBpbiBjbGFzcyBzdGF0aWMgYmxvY2tzIHNob3VsZCBiZSBhdCB0aGUgdG9wIG9mIHRoZSBzdGF0aWMgYmxvY2tzLlxuXG5jbGFzcyBDIHtcblxuICAgIC8vIFZhcmlhYmxlIGRlY2xhcmF0aW9uIGluIGEgbmVzdGVkIGJsb2NrOlxuICAgIHN0YXRpYyB7XG4gICAgICAgIGlmIChzb21ldGhpbmcpIHtcbiAgICAgICAgICAgIHZhciBhID0gdHJ1ZTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIC8vIFZhcmlhYmxlIGRlY2xhcmF0aW9uIGFmdGVyIG90aGVyIHN0YXRlbWVudHM6XG4gICAgc3RhdGljIHtcbiAgICAgICAgZigpO1xuICAgICAgICB2YXIgYTtcbiAgICB9XG5cbn0ifQ==)

```
/*eslint vars-on-top: "error"*/

// Variables in class static blocks should be at the top of the static blocks.

class C {

    // Variable declaration in a nested block:
    static {
        if (something) {
            var a = true;
        }
    }

    // Variable declaration after other statements:
    static {
        f();
        var a;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nKCkge1xuICAgIHZhciBmaXJzdDtcbiAgICB2YXIgc2Vjb25kOyAvL211bHRpcGxlIGRlY2xhcmF0aW9ucyBhcmUgYWxsb3dlZCBhdCB0aGUgdG9wXG4gICAgaWYgKHRydWUpIHtcbiAgICAgICAgZmlyc3QgPSB0cnVlO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKCkge1xuICAgIHZhciBpO1xuICAgIGZvciAoaT0wOyBpPDEwOyBpKyspIHt9XG59In0=)

```
/*eslint vars-on-top: "error"*/

function doSomething() {
    var first;
    var second; //multiple declarations are allowed at the top
    if (true) {
        first = true;
    }
}

function doSomethingElse() {
    var i;
    for (i=0; i<10; i++) {}
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
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbnZhciBhO1xuZigpOyJ9)

```
/*eslint vars-on-top: "error"*/

var a;
f();
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEMge1xuXG4gICAgc3RhdGljIHtcbiAgICAgICAgdmFyIGE7XG4gICAgICAgIGlmIChzb21ldGhpbmcpIHtcbiAgICAgICAgICAgIGEgPSB0cnVlO1xuICAgICAgICB9XG4gICAgfVxuXG4gICAgc3RhdGljIHtcbiAgICAgICAgdmFyIGE7XG4gICAgICAgIGYoKTtcbiAgICB9XG5cbn0ifQ==)

```
/*eslint vars-on-top: "error"*/

class C {

    static {
        var a;
        if (something) {
            a = true;
        }
    }

    static {
        var a;
        f();
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
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFycy1vbi10b3A6IFwiZXJyb3JcIiovXG5cbi8vIERpcmVjdGl2ZXMgbWF5IHByZWNlZGUgdmFyaWFibGUgZGVjbGFyYXRpb25zLlxuXCJ1c2Ugc3RyaWN0XCI7XG52YXIgYTtcbmYoKTtcblxuLy8gQ29tbWVudHMgY2FuIGRlc2NyaWJlIHZhcmlhYmxlcy5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nKCkge1xuICAgIC8vIHRoaXMgaXMgdGhlIGZpcnN0IHZhci5cbiAgICB2YXIgZmlyc3Q7XG4gICAgLy8gdGhpcyBpcyB0aGUgc2Vjb25kIHZhci5cbiAgICB2YXIgc2Vjb25kXG59In0=)

```
/*eslint vars-on-top: "error"*/

// Directives may precede variable declarations.
"use strict";
var a;
f();

// Comments can describe variables.
function doSomething() {
    // this is the first var.
    var first;
    // this is the second var.
    var second
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
```

## Version

This rule was introduced in ESLint v0.8.0.

## Further Reading

[JavaScript Scoping and Hoisting](https://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)
 www.adequatelygood.com[var - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#var_hoisting)
 developer.mozilla.org[A criticism of the Single Var Pattern in JavaScript, and a simple alternative — Dan Hough](https://danhough.com/blog/single-var-pattern-rant/)
 danhough.com[Ben Alman » Multiple var statements in JavaScript, not superfluous](https://benalman.com/news/2012/05/multiple-var-statements-javascript/)
 benalman.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/vars-on-top.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/vars-on-top.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/vars-on-top.md
                    
                
                )
