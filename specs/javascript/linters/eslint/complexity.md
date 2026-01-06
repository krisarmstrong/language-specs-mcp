# complexity

Enforce a maximum cyclomatic complexity allowed in a program

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [max](#max)
  2. [variant](#variant)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

Cyclomatic complexity measures the number of linearly independent paths through a program’s source code. This rule allows setting a cyclomatic complexity threshold.

```
function a(x) {
    if (true) {
        return x; // 1st path
    } else if (false) {
        return x+1; // 2nd path
    } else {
        return 4; // 3rd path
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
```

Copy code to clipboard

## Rule Details

This rule is aimed at reducing code complexity by capping the amount of cyclomatic complexity allowed in a program. As such, it will warn when the cyclomatic complexity crosses the configured threshold (default is `20`).

Examples of incorrect code for a maximum of `2`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29tcGxleGl0eTogW1wiZXJyb3JcIiwgMl0qL1xuXG5mdW5jdGlvbiBhKHgpIHtcbiAgICBpZiAodHJ1ZSkge1xuICAgICAgICByZXR1cm4geDtcbiAgICB9IGVsc2UgaWYgKGZhbHNlKSB7XG4gICAgICAgIHJldHVybiB4KzE7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgcmV0dXJuIDQ7IC8vIDNyZCBwYXRoXG4gICAgfVxufVxuXG5mdW5jdGlvbiBiKCkge1xuICAgIGZvbyB8fD0gMTtcbiAgICBiYXIgJiY9IDE7XG59XG5cbmZ1bmN0aW9uIGMoYSA9IHt9KSB7IC8vIGRlZmF1bHQgcGFyYW1ldGVyIC0+IDJuZCBwYXRoXG4gICAgY29uc3QgeyBiID0gJ2RlZmF1bHQnIH0gPSBhOyAvLyBkZWZhdWx0IHZhbHVlIGR1cmluZyBkZXN0cnVjdHVyaW5nIC0+IDNyZCBwYXRoXG59XG5cbmZ1bmN0aW9uIGQoYSkge1xuICAgIHJldHVybiBhPy5iPy5jOyAvLyBvcHRpb25hbCBjaGFpbmluZyB3aXRoIHR3byBvcHRpb25hbCBwcm9wZXJ0aWVzIGNyZWF0ZXMgdHdvIGFkZGl0aW9uYWwgYnJhbmNoZXNcbn0ifQ==)

```
/*eslint complexity: ["error", 2]*/

function a(x) {
    if (true) {
        return x;
    } else if (false) {
        return x+1;
    } else {
        return 4; // 3rd path
    }
}

function b() {
    foo ||= 1;
    bar &&= 1;
}

function c(a = {}) { // default parameter -> 2nd path
    const { b = 'default' } = a; // default value during destructuring -> 3rd path
}

function d(a) {
    return a?.b?.c; // optional chaining with two optional properties creates two additional branches
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

Examples of correct code for a maximum of `2`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29tcGxleGl0eTogW1wiZXJyb3JcIiwgMl0qL1xuXG5mdW5jdGlvbiBhKHgpIHtcbiAgICBpZiAodHJ1ZSkge1xuICAgICAgICByZXR1cm4geDtcbiAgICB9IGVsc2Uge1xuICAgICAgICByZXR1cm4gNDtcbiAgICB9XG59XG5cbmZ1bmN0aW9uIGIoKSB7XG4gICAgZm9vIHx8PSAxO1xufSJ9)

```
/*eslint complexity: ["error", 2]*/

function a(x) {
    if (true) {
        return x;
    } else {
        return 4;
    }
}

function b() {
    foo ||= 1;
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
```

Class field initializers and class static blocks are implicit functions. Therefore, their complexity is calculated separately for each initializer and each static block, and it doesn’t contribute to the complexity of the enclosing code.

Examples of additional incorrect code for a maximum of `2`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29tcGxleGl0eTogW1wiZXJyb3JcIiwgMl0qL1xuXG5jbGFzcyBDIHtcbiAgICB4ID0gYSB8fCBiIHx8IGM7IC8vIHRoaXMgaW5pdGlhbGl6ZXIgaGFzIGNvbXBsZXhpdHkgPSAzXG59XG5cbmNsYXNzIEQgeyAvLyB0aGlzIHN0YXRpYyBibG9jayBoYXMgY29tcGxleGl0eSA9IDNcbiAgICBzdGF0aWMge1xuICAgICAgICBpZiAoZm9vKSB7XG4gICAgICAgICAgICBiYXIgPSBiYXogfHwgcXV4O1xuICAgICAgICB9XG4gICAgfVxufSJ9)

```
/*eslint complexity: ["error", 2]*/

class C {
    x = a || b || c; // this initializer has complexity = 3
}

class D { // this static block has complexity = 3
    static {
        if (foo) {
            bar = baz || qux;
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
```

Examples of additional correct code for a maximum of `2`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29tcGxleGl0eTogW1wiZXJyb3JcIiwgMl0qL1xuXG5mdW5jdGlvbiBmb28oKSB7IC8vIHRoaXMgZnVuY3Rpb24gaGFzIGNvbXBsZXhpdHkgPSAxXG4gICAgY2xhc3MgQyB7XG4gICAgICAgIHggPSBhICsgYjsgLy8gdGhpcyBpbml0aWFsaXplciBoYXMgY29tcGxleGl0eSA9IDFcbiAgICAgICAgeSA9IGMgfHwgZDsgLy8gdGhpcyBpbml0aWFsaXplciBoYXMgY29tcGxleGl0eSA9IDJcbiAgICAgICAgeiA9IGUgJiYgZjsgLy8gdGhpcyBpbml0aWFsaXplciBoYXMgY29tcGxleGl0eSA9IDJcblxuICAgICAgICBzdGF0aWMgcCA9IGcgfHwgaDsgLy8gdGhpcyBpbml0aWFsaXplciBoYXMgY29tcGxleGl0eSA9IDJcbiAgICAgICAgc3RhdGljIHEgPSBpID8gaiA6IGs7IC8vIHRoaXMgaW5pdGlhbGl6ZXIgaGFzIGNvbXBsZXhpdHkgPSAyXG5cbiAgICAgICAgc3RhdGljIHsgLy8gdGhpcyBzdGF0aWMgYmxvY2sgaGFzIGNvbXBsZXhpdHkgPSAyXG4gICAgICAgICAgICBpZiAoZm9vKSB7XG4gICAgICAgICAgICAgICAgYmF6ID0gYmFyO1xuICAgICAgICAgICAgfVxuICAgICAgICB9XG5cbiAgICAgICAgc3RhdGljIHsgLy8gdGhpcyBzdGF0aWMgYmxvY2sgaGFzIGNvbXBsZXhpdHkgPSAyXG4gICAgICAgICAgICBxdXggPSBiYXogfHwgcXV1eDtcbiAgICAgICAgfVxuICAgIH1cbn0ifQ==)

```
/*eslint complexity: ["error", 2]*/

function foo() { // this function has complexity = 1
    class C {
        x = a + b; // this initializer has complexity = 1
        y = c || d; // this initializer has complexity = 2
        z = e && f; // this initializer has complexity = 2

        static p = g || h; // this initializer has complexity = 2
        static q = i ? j : k; // this initializer has complexity = 2

        static { // this static block has complexity = 2
            if (foo) {
                baz = bar;
            }
        }

        static { // this static block has complexity = 2
            qux = baz || quux;
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
```

## Options

This rule has a number or object option:

- 

`"max"` (default: `20`) enforces a maximum complexity

- 

`"variant": "classic" | "modified"` (default: `"classic"`) cyclomatic complexity variant to use

### max

Customize the threshold with the `max` property.

```
"complexity": ["error", { "max": 2 }]
1
```

Copy code to clipboard

Deprecated: the object property `maximum` is deprecated. Please use the property `max` instead.

Or use the shorthand syntax:

```
"complexity": ["error", 2]
1
```

Copy code to clipboard

### variant

Cyclomatic complexity variant to use:

- `"classic"` (default) - Classic McCabe cyclomatic complexity
- `"modified"` - Modified cyclomatic complexity

Modified cyclomatic complexity is the same as the classic cyclomatic complexity, but each `switch` statement only increases the complexity value by `1`, regardless of how many `case` statements it contains.

Examples of correct code for this rule with the `{ "max": 3, "variant": "modified" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29tcGxleGl0eTogW1wiZXJyb3JcIiwge1wibWF4XCI6IDMsIFwidmFyaWFudFwiOiBcIm1vZGlmaWVkXCJ9XSovXG5cbmZ1bmN0aW9uIGEoeCkgeyAgICAgLy8gaW5pdGlhbCBtb2RpZmllZCBjb21wbGV4aXR5IGlzIDFcbiAgICBzd2l0Y2ggKHgpIHsgICAgLy8gc3dpdGNoIHN0YXRlbWVudCBpbmNyZWFzZXMgbW9kaWZpZWQgY29tcGxleGl0eSBieSAxXG4gICAgICAgIGNhc2UgMTpcbiAgICAgICAgICAgIDE7XG4gICAgICAgICAgICBicmVhaztcbiAgICAgICAgY2FzZSAyOlxuICAgICAgICAgICAgMjtcbiAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICBjYXNlIDM6XG4gICAgICAgICAgICBpZiAoeCA9PT0gJ2ZvbycpIHsgIC8vIGlmIGJsb2NrIGluY3JlYXNlcyBtb2RpZmllZCBjb21wbGV4aXR5IGJ5IDFcbiAgICAgICAgICAgICAgICAzO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgIGRlZmF1bHQ6XG4gICAgICAgICAgICA0O1xuICAgIH1cbn0ifQ==)

```
/*eslint complexity: ["error", {"max": 3, "variant": "modified"}]*/

function a(x) {     // initial modified complexity is 1
    switch (x) {    // switch statement increases modified complexity by 1
        case 1:
            1;
            break;
        case 2:
            2;
            break;
        case 3:
            if (x === 'foo') {  // if block increases modified complexity by 1
                3;
            }
            break;
        default:
            4;
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
```

The classic cyclomatic complexity of the above function is `5`, but the modified cyclomatic complexity is only `3`.

## When Not To Use It

If you can’t determine an appropriate complexity limit for your code, then it’s best to disable this rule.

## Related Rules

- [max-depth](/docs/latest/rules/max-depth)
- [max-len](/docs/latest/rules/max-len)
- [max-lines](/docs/latest/rules/max-lines)
- [max-lines-per-function](/docs/latest/rules/max-lines-per-function)
- [max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)
- [max-params](/docs/latest/rules/max-params)
- [max-statements](/docs/latest/rules/max-statements)

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[Cyclomatic complexity - Wikipedia](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
 en.wikipedia.org[Complexity Analysis of JavaScript Code](https://ariya.io/2012/12/complexity-analysis-of-javascript-code)
 ariya.io[Complexity for JavaScript](https://craftsmanshipforsoftware.com/2015/05/25/complexity-for-javascript/)
 craftsmanshipforsoftware.com[About complexity | JSComplexity.org](https://web.archive.org/web/20160808115119/http://jscomplexity.org/complexity)
 web.archive.org[Complexity has no default · Issue #4808 · eslint/eslint](https://github.com/eslint/eslint/issues/4808#issuecomment-167795140)
 github.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/complexity.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/complexity.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/complexity.md
                    
                
                )
