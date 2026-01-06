# id-denylist

Disallow specified identifiers

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

“There are only two hard things in Computer Science: cache invalidation and naming things.” — Phil Karlton

Generic names can lead to hard-to-decipher code. This rule allows you to specify a deny list of disallowed identifier names to avoid this practice.

## Rule Details

This rule disallows specified identifiers in assignments and `function` definitions.

This rule will catch disallowed identifiers that are:

- variable declarations
- function declarations
- object properties assigned to during object creation
- class fields
- class methods

It will not catch disallowed identifiers that are:

- function calls (so you can still use functions you do not have control over)
- object properties (so you can still use objects you do not have control over)

## Options

The rule takes one or more strings as options: the names of restricted identifiers.

For example, to restrict the use of common generic identifiers:

```
{
    "id-denylist": ["error", "data", "err", "e", "cb", "callback"]
}
1
2
3
```

Copy code to clipboard

Note: The first element of the array is for the rule severity (see [Configure Rules](../use/configure/rules)). The other elements in the array are the identifiers that you want to disallow.

Examples of incorrect code for this rule with sample `"data", "callback"` restricted identifiers:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtZGVueWxpc3Q6IFtcImVycm9yXCIsIFwiZGF0YVwiLCBcImNhbGxiYWNrXCJdICovXG5cbmNvbnN0IGRhdGEgPSB7IC4uLnZhbHVlcyB9O1xuXG5mdW5jdGlvbiBjYWxsYmFjaygpIHtcbiAgICAvLyAuLi5cbn1cblxuZWxlbWVudC5jYWxsYmFjayA9IGZ1bmN0aW9uKCkge1xuICAgIC8vIC4uLlxufTtcblxuY29uc3QgaXRlbVNldCA9IHtcbiAgICBkYXRhOiBbLi4udmFsdWVzXVxufTtcblxuY2xhc3MgRm9vIHtcbiAgICBkYXRhID0gW107XG59XG5cbmNsYXNzIEJhciB7XG4gICAgI2RhdGEgPSBbXTtcbn1cblxuY2xhc3MgQmF6IHtcbiAgICBjYWxsYmFjaygpIHt9XG59XG5cbmNsYXNzIFF1eCB7XG4gICAgI2NhbGxiYWNrKCkge31cbn0ifQ==)

```
/*eslint id-denylist: ["error", "data", "callback"] */

const data = { ...values };

function callback() {
    // ...
}

element.callback = function() {
    // ...
};

const itemSet = {
    data: [...values]
};

class Foo {
    data = [];
}

class Bar {
    #data = [];
}

class Baz {
    callback() {}
}

class Qux {
    #callback() {}
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
```

Examples of correct code for this rule with sample `"data", "callback"` restricted identifiers:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtZGVueWxpc3Q6IFtcImVycm9yXCIsIFwiZGF0YVwiLCBcImNhbGxiYWNrXCJdICovXG5cbmNvbnN0IGVuY29kaW5nT3B0aW9ucyA9IHsuLi52YWx1ZXN9O1xuXG5mdW5jdGlvbiBwcm9jZXNzRmlsZVJlc3VsdCgpIHtcbiAgICAvLyAuLi5cbn1cblxuZWxlbWVudC5zdWNjZXNzSGFuZGxlciA9IGZ1bmN0aW9uKCkge1xuICAgIC8vIC4uLlxufTtcblxuY29uc3QgaXRlbVNldCA9IHtcbiAgICBlbnRpdGllczogWy4uLnZhbHVlc11cbn07XG5cbmNhbGxiYWNrKCk7IC8vIGFsbCBmdW5jdGlvbiBjYWxscyBhcmUgaWdub3JlZFxuXG5mb28uY2FsbGJhY2soKTsgLy8gYWxsIGZ1bmN0aW9uIGNhbGxzIGFyZSBpZ25vcmVkXG5cbmZvby5kYXRhOyAvLyBhbGwgcHJvcGVydHkgbmFtZXMgdGhhdCBhcmUgbm90IGFzc2lnbm1lbnRzIGFyZSBpZ25vcmVkXG5cbmNsYXNzIEZvbyB7XG4gICAgaXRlbXMgPSBbXTtcbn1cblxuY2xhc3MgQmFyIHtcbiAgICAjaXRlbXMgPSBbXTtcbn1cblxuY2xhc3MgQmF6IHtcbiAgICBtZXRob2QoKSB7fVxufVxuXG5jbGFzcyBRdXgge1xuICAgICNtZXRob2QoKSB7fVxufSJ9)

```
/*eslint id-denylist: ["error", "data", "callback"] */

const encodingOptions = {...values};

function processFileResult() {
    // ...
}

element.successHandler = function() {
    // ...
};

const itemSet = {
    entities: [...values]
};

callback(); // all function calls are ignored

foo.callback(); // all function calls are ignored

foo.data; // all property names that are not assignments are ignored

class Foo {
    items = [];
}

class Bar {
    #items = [];
}

class Baz {
    method() {}
}

class Qux {
    #method() {}
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
```

## When Not To Use It

You can turn this rule off if you do not want to restrict the use of certain identifiers.

## Version

This rule was introduced in ESLint v7.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/id-denylist.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/id-denylist.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/id-denylist.md
                    
                
                )
