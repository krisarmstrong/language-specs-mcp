# max-nested-callbacks

Enforce a maximum depth that callbacks can be nested

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [max](#max)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Many JavaScript libraries use the callback pattern to manage asynchronous operations. A program of any complexity will most likely need to manage several asynchronous operations at various levels of concurrency. A common pitfall that is easy to fall into is nesting callbacks, which makes code more difficult to read the deeper the callbacks are nested.

```
foo(function () {
    bar(function () {
        baz(function() {
            qux(function () {

            });
        });
    });
});
1
2
3
4
5
6
7
8
9
```

Copy code to clipboard

## Rule Details

This rule enforces a maximum depth that callbacks can be nested to increase code clarity.

## Options

This rule has a number or object option:

- `"max"` (default `10`) enforces a maximum depth that callbacks can be nested

Deprecated: The object property `maximum` is deprecated; please use the object property `max` instead.

### max

Examples of incorrect code for this rule with the `{ "max": 3 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LW5lc3RlZC1jYWxsYmFja3M6IFtcImVycm9yXCIsIDNdKi9cblxuZm9vMShmdW5jdGlvbigpIHtcbiAgICBmb28yKGZ1bmN0aW9uKCkge1xuICAgICAgICBmb28zKGZ1bmN0aW9uKCkge1xuICAgICAgICAgICAgZm9vNChmdW5jdGlvbigpIHtcbiAgICAgICAgICAgICAgICAvLyBEbyBzb21ldGhpbmdcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9KTtcbiAgICB9KTtcbn0pOyJ9)

```
/*eslint max-nested-callbacks: ["error", 3]*/

foo1(function() {
    foo2(function() {
        foo3(function() {
            foo4(function() {
                // Do something
            });
        });
    });
});
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

Examples of correct code for this rule with the `{ "max": 3 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LW5lc3RlZC1jYWxsYmFja3M6IFtcImVycm9yXCIsIDNdKi9cblxuZm9vMShoYW5kbGVGb28xKTtcblxuZnVuY3Rpb24gaGFuZGxlRm9vMSgpIHtcbiAgICBmb28yKGhhbmRsZUZvbzIpO1xufVxuXG5mdW5jdGlvbiBoYW5kbGVGb28yKCkge1xuICAgIGZvbzMoaGFuZGxlRm9vMyk7XG59XG5cbmZ1bmN0aW9uIGhhbmRsZUZvbzMoKSB7XG4gICAgZm9vNChoYW5kbGVGb280KTtcbn1cblxuZnVuY3Rpb24gaGFuZGxlRm9vNCgpIHtcbiAgICBmb281KCk7XG59In0=)

```
/*eslint max-nested-callbacks: ["error", 3]*/

foo1(handleFoo1);

function handleFoo1() {
    foo2(handleFoo2);
}

function handleFoo2() {
    foo3(handleFoo3);
}

function handleFoo3() {
    foo4(handleFoo4);
}

function handleFoo4() {
    foo5();
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
```

## Related Rules

- [complexity](/docs/latest/rules/complexity)
- [max-depth](/docs/latest/rules/max-depth)
- [max-len](/docs/latest/rules/max-len)
- [max-lines](/docs/latest/rules/max-lines)
- [max-lines-per-function](/docs/latest/rules/max-lines-per-function)
- [max-params](/docs/latest/rules/max-params)
- [max-statements](/docs/latest/rules/max-statements)

## Version

This rule was introduced in ESLint v0.2.0.

## Further Reading

[7. Control flow - Mixu’s Node book](http://book.mixu.net/node/ch7.html)
 book.mixu.net[Control Flow in Node - How To Node - NodeJS](https://web.archive.org/web/20220104141150/https://howtonode.org/control-flow)
 web.archive.org[Control Flow in Node Part II - How To Node - NodeJS](https://web.archive.org/web/20220127215850/https://howtonode.org/control-flow-part-ii)
 web.archive.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-nested-callbacks.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-nested-callbacks.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-nested-callbacks.md
                    
                
                )
