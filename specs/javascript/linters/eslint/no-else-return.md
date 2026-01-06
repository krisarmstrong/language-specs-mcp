# no-else-return

Disallow `else` blocks after `return` statements in `if` statements

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowElseIf](#allowelseif)

3. [Version](#version)
4. [Resources](#resources)

If an `if` block contains a `return` statement, the `else` block becomes unnecessary. Its contents can be placed outside of the block.

```
function foo() {
    if (x) {
        return y;
    } else {
        return z;
    }
}
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

This rule is aimed at highlighting an unnecessary block of code following an `if` containing a `return` statement. As such, it will warn when it encounters an `else` following a chain of `if`s, all of them containing a `return` statement.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZWxzZS1yZXR1cm46IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgaWYgKHgpIHtcbiAgICAgICAgcmV0dXJuIHk7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgcmV0dXJuIHo7XG4gICAgfVxufVxuXG5mdW5jdGlvbiBmb28yKCkge1xuICAgIGlmICh4KSB7XG4gICAgICAgIHJldHVybiB5O1xuICAgIH0gZWxzZSB7XG4gICAgICAgIGNvbnN0IHQgPSBcImZvb1wiO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gZm9vMygpIHtcbiAgICBpZiAoZXJyb3IpIHtcbiAgICAgICAgcmV0dXJuICdJdCBmYWlsZWQnO1xuICAgIH0gZWxzZSB7XG4gICAgICAgIGlmIChsb2FkaW5nKSB7XG4gICAgICAgICAgICByZXR1cm4gXCJJdCdzIHN0aWxsIGxvYWRpbmdcIjtcbiAgICAgICAgfVxuICAgIH1cbn1cblxuLy8gVHdvIHdhcm5pbmdzIGZvciBuZXN0ZWQgb2NjdXJyZW5jZXNcbmZ1bmN0aW9uIGZvbzQoKSB7XG4gICAgaWYgKHgpIHtcbiAgICAgICAgaWYgKHkpIHtcbiAgICAgICAgICAgIHJldHVybiB5O1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgcmV0dXJuIHg7XG4gICAgICAgIH1cbiAgICB9IGVsc2Uge1xuICAgICAgICByZXR1cm4gejtcbiAgICB9XG59In0=)

```
/*eslint no-else-return: "error"*/

function foo1() {
    if (x) {
        return y;
    } else {
        return z;
    }
}

function foo2() {
    if (x) {
        return y;
    } else {
        const t = "foo";
    }
}

function foo3() {
    if (error) {
        return 'It failed';
    } else {
        if (loading) {
            return "It's still loading";
        }
    }
}

// Two warnings for nested occurrences
function foo4() {
    if (x) {
        if (y) {
            return y;
        } else {
            return x;
        }
    } else {
        return z;
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZWxzZS1yZXR1cm46IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbzEoKSB7XG4gICAgaWYgKHgpIHtcbiAgICAgICAgcmV0dXJuIHk7XG4gICAgfVxuXG4gICAgcmV0dXJuIHo7XG59XG5cbmZ1bmN0aW9uIGZvbzIoKSB7XG4gICAgaWYgKHgpIHtcbiAgICAgICAgcmV0dXJuIHk7XG4gICAgfVxuXG4gICAgY29uc3QgdCA9IFwiZm9vXCI7XG59XG5cbmZ1bmN0aW9uIGZvbzMoKSB7XG4gICAgaWYgKGVycm9yKSB7XG4gICAgICAgIHJldHVybiAnSXQgZmFpbGVkJztcbiAgICB9XG5cbiAgICBpZiAobG9hZGluZykge1xuICAgICAgICByZXR1cm4gXCJJdCdzIHN0aWxsIGxvYWRpbmdcIjtcbiAgICB9ICAgXG59XG5cbmZ1bmN0aW9uIGZvbzQoKSB7XG4gICAgaWYgKHgpIHtcbiAgICAgICAgaWYgKHkpIHtcbiAgICAgICAgICAgIHJldHVybiB5O1xuICAgICAgICB9XG5cbiAgICAgICAgcmV0dXJuIHg7XG4gICAgfVxuXG4gICAgcmV0dXJuIHo7ICAgIFxufVxuXG5mdW5jdGlvbiBmb281KCkge1xuICBpZiAoeCkge1xuICAgIGNvbnN0IHQgPSBcImZvb1wiO1xuICB9IGVsc2Uge1xuICAgIHJldHVybiB5XG4gIH1cbn0ifQ==)

```
/*eslint no-else-return: "error"*/

function foo1() {
    if (x) {
        return y;
    }

    return z;
}

function foo2() {
    if (x) {
        return y;
    }

    const t = "foo";
}

function foo3() {
    if (error) {
        return 'It failed';
    }

    if (loading) {
        return "It's still loading";
    }   
}

function foo4() {
    if (x) {
        if (y) {
            return y;
        }

        return x;
    }

    return z;    
}

function foo5() {
  if (x) {
    const t = "foo";
  } else {
    return y
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
```

## Options

### allowElseIf

This rule has an object option:

- `allowElseIf: true` (default) - If true, allows `else if` blocks after a `return`

Examples of correct code for the default `{"allowElseIf": true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZWxzZS1yZXR1cm46IFtcImVycm9yXCIsIHthbGxvd0Vsc2VJZjogdHJ1ZX1dKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIGlmIChlcnJvcikge1xuICAgICAgICByZXR1cm4gJ0l0IGZhaWxlZCc7XG4gICAgfSBlbHNlIGlmIChsb2FkaW5nKSB7XG4gICAgICAgIHJldHVybiBcIkl0J3Mgc3RpbGwgbG9hZGluZ1wiO1xuICAgIH1cbn1cblxuLy8gVXNpbmcgbXVsdGlwbGUgYGlmYCBzdGF0ZW1lbnRzIGluc3RlYWQgb2YgYGVsc2UgaWZgIGlzIGFsc28gYWxsb3dlZFxuZnVuY3Rpb24gZm9vMigpIHtcbiAgICBpZiAoZXJyb3IpIHtcbiAgICAgICAgcmV0dXJuICdJdCBmYWlsZWQnO1xuICAgIH1cbiAgXG4gICAgaWYgKGxvYWRpbmcpIHtcbiAgICAgICAgcmV0dXJuIFwiSXQncyBzdGlsbCBsb2FkaW5nXCI7XG4gICAgfVxufSJ9)

```
/*eslint no-else-return: ["error", {allowElseIf: true}]*/

function foo() {
    if (error) {
        return 'It failed';
    } else if (loading) {
        return "It's still loading";
    }
}

// Using multiple `if` statements instead of `else if` is also allowed
function foo2() {
    if (error) {
        return 'It failed';
    }
  
    if (loading) {
        return "It's still loading";
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

Examples of incorrect code for the `{"allowElseIf": false}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZWxzZS1yZXR1cm46IFtcImVycm9yXCIsIHthbGxvd0Vsc2VJZjogZmFsc2V9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBpZiAoZXJyb3IpIHtcbiAgICAgICAgcmV0dXJuICdJdCBmYWlsZWQnO1xuICAgIH0gZWxzZSBpZiAobG9hZGluZykge1xuICAgICAgICByZXR1cm4gXCJJdCdzIHN0aWxsIGxvYWRpbmdcIjtcbiAgICB9XG59In0=)

```
/*eslint no-else-return: ["error", {allowElseIf: false}]*/

function foo() {
    if (error) {
        return 'It failed';
    } else if (loading) {
        return "It's still loading";
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

Examples of correct code for the `{"allowElseIf": false}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZWxzZS1yZXR1cm46IFtcImVycm9yXCIsIHthbGxvd0Vsc2VJZjogZmFsc2V9XSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBpZiAoZXJyb3IpIHtcbiAgICAgICAgcmV0dXJuICdJdCBmYWlsZWQnO1xuICAgIH1cblxuICAgIGlmIChsb2FkaW5nKSB7XG4gICAgICAgIHJldHVybiBcIkl0J3Mgc3RpbGwgbG9hZGluZ1wiO1xuICAgIH1cbn0ifQ==)

```
/*eslint no-else-return: ["error", {allowElseIf: false}]*/

function foo() {
    if (error) {
        return 'It failed';
    }

    if (loading) {
        return "It's still loading";
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
```

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-else-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-else-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-else-return.md
                    
                
                )
