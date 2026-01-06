# max-depth

Enforce a maximum depth that blocks can be nested

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [max](#max)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Many developers consider code difficult to read if blocks are nested beyond a certain depth.

## Rule Details

This rule enforces a maximum depth that blocks can be nested to reduce code complexity.

## Options

This rule has a number or object option:

- `"max"` (default `4`) enforces a maximum depth that blocks can be nested

Deprecated: The object property `maximum` is deprecated; please use the object property `max` instead.

### max

Examples of incorrect code for this rule with the default `{ "max": 4 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWRlcHRoOiBbXCJlcnJvclwiLCA0XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBmb3IgKDs7KSB7IC8vIE5lc3RlZCAxIGRlZXBcbiAgICAgICAgd2hpbGUgKHRydWUpIHsgLy8gTmVzdGVkIDIgZGVlcFxuICAgICAgICAgICAgaWYgKHRydWUpIHsgLy8gTmVzdGVkIDMgZGVlcFxuICAgICAgICAgICAgICAgIGlmICh0cnVlKSB7IC8vIE5lc3RlZCA0IGRlZXBcbiAgICAgICAgICAgICAgICAgICAgaWYgKHRydWUpIHsgLy8gTmVzdGVkIDUgZGVlcFxuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9XG4gICAgfVxufSJ9)

```
/*eslint max-depth: ["error", 4]*/

function foo() {
    for (;;) { // Nested 1 deep
        while (true) { // Nested 2 deep
            if (true) { // Nested 3 deep
                if (true) { // Nested 4 deep
                    if (true) { // Nested 5 deep
                    }
                }
            }
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
```

Examples of correct code for this rule with the default `{ "max": 4 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWRlcHRoOiBbXCJlcnJvclwiLCA0XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBmb3IgKDs7KSB7IC8vIE5lc3RlZCAxIGRlZXBcbiAgICAgICAgd2hpbGUgKHRydWUpIHsgLy8gTmVzdGVkIDIgZGVlcFxuICAgICAgICAgICAgaWYgKHRydWUpIHsgLy8gTmVzdGVkIDMgZGVlcFxuICAgICAgICAgICAgICAgIGlmICh0cnVlKSB7IC8vIE5lc3RlZCA0IGRlZXBcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9XG59In0=)

```
/*eslint max-depth: ["error", 4]*/

function foo() {
    for (;;) { // Nested 1 deep
        while (true) { // Nested 2 deep
            if (true) { // Nested 3 deep
                if (true) { // Nested 4 deep
                }
            }
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
```

Note that class static blocks do not count as nested blocks, and that the depth in them is calculated separately from the enclosing context.

Examples of incorrect code for this rule with `{ "max": 2 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWRlcHRoOiBbXCJlcnJvclwiLCAyXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBpZiAodHJ1ZSkgeyAvLyBOZXN0ZWQgMSBkZWVwXG4gICAgICAgIGNsYXNzIEMge1xuICAgICAgICAgICAgc3RhdGljIHtcbiAgICAgICAgICAgICAgICBpZiAodHJ1ZSkgeyAvLyBOZXN0ZWQgMSBkZWVwXG4gICAgICAgICAgICAgICAgICAgIGlmICh0cnVlKSB7IC8vIE5lc3RlZCAyIGRlZXBcbiAgICAgICAgICAgICAgICAgICAgICAgIGlmICh0cnVlKSB7IC8vIE5lc3RlZCAzIGRlZXBcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH1cbn0ifQ==)

```
/*eslint max-depth: ["error", 2]*/

function foo() {
    if (true) { // Nested 1 deep
        class C {
            static {
                if (true) { // Nested 1 deep
                    if (true) { // Nested 2 deep
                        if (true) { // Nested 3 deep
                        }
                    }
                }
            }
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

Examples of correct code for this rule with `{ "max": 2 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWRlcHRoOiBbXCJlcnJvclwiLCAyXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBpZiAodHJ1ZSkgeyAvLyBOZXN0ZWQgMSBkZWVwXG4gICAgICAgIGNsYXNzIEMge1xuICAgICAgICAgICAgc3RhdGljIHtcbiAgICAgICAgICAgICAgICBpZiAodHJ1ZSkgeyAvLyBOZXN0ZWQgMSBkZWVwXG4gICAgICAgICAgICAgICAgICAgIGlmICh0cnVlKSB7IC8vIE5lc3RlZCAyIGRlZXBcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH1cbn0ifQ==)

```
/*eslint max-depth: ["error", 2]*/

function foo() {
    if (true) { // Nested 1 deep
        class C {
            static {
                if (true) { // Nested 1 deep
                    if (true) { // Nested 2 deep
                    }
                }
            }
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
```

## Related Rules

- [complexity](/docs/latest/rules/complexity)
- [max-len](/docs/latest/rules/max-len)
- [max-lines](/docs/latest/rules/max-lines)
- [max-lines-per-function](/docs/latest/rules/max-lines-per-function)
- [max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)
- [max-params](/docs/latest/rules/max-params)
- [max-statements](/docs/latest/rules/max-statements)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-depth.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-depth.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-depth.md
                    
                
                )
