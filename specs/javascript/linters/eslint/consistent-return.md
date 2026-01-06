# consistent-return

Require `return` statements to either always or never specify values

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [treatUndefinedAsUnspecified](#treatundefinedasunspecified)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

Unlike statically-typed languages which enforce that a function returns a specified type of value, JavaScript allows different code paths in a function to return different types of values.

A confusing aspect of JavaScript is that a function returns `undefined` if any of the following are true:

- It does not execute a `return` statement before it exits.
- It executes `return` which does not specify a value explicitly.
- It executes `return undefined`.
- It executes `return void` followed by an expression (for example, a function call).
- It executes `return` followed by any other expression which evaluates to `undefined`.

If any code paths in a function return a value explicitly but some code path do not return a value explicitly, it might be a typing mistake, especially in a large function. In the following example:

- A code path through the function returns a Boolean value `true`.
- Another code path does not return a value explicitly, therefore returns `undefined` implicitly.

```
function doSomething(condition) {
    if (condition) {
        return true;
    } else {
        return;
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

This rule requires `return` statements to either always or never specify values. This rule ignores function definitions where the name begins with an uppercase letter, because constructors (when invoked with the `new` operator) return the instantiated object implicitly if they do not return another object explicitly.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC1yZXR1cm46IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nKGNvbmRpdGlvbikge1xuICAgIGlmIChjb25kaXRpb24pIHtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgcmV0dXJuO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gZG9Tb21ldGhpbmdFbHNlKGNvbmRpdGlvbikge1xuICAgIGlmIChjb25kaXRpb24pIHtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgfVxufSJ9)

```
/*eslint consistent-return: "error"*/

function doSomething(condition) {
    if (condition) {
        return true;
    } else {
        return;
    }
}

function doSomethingElse(condition) {
    if (condition) {
        return true;
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC1yZXR1cm46IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGRvU29tZXRoaW5nKGNvbmRpdGlvbikge1xuICAgIGlmIChjb25kaXRpb24pIHtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cbn1cblxuZnVuY3Rpb24gRm9vKCkge1xuICAgIGlmICghKHRoaXMgaW5zdGFuY2VvZiBGb28pKSB7XG4gICAgICAgIHJldHVybiBuZXcgRm9vKCk7XG4gICAgfVxuXG4gICAgdGhpcy5hID0gMDtcbn0ifQ==)

```
/*eslint consistent-return: "error"*/

function doSomething(condition) {
    if (condition) {
        return true;
    } else {
        return false;
    }
}

function Foo() {
    if (!(this instanceof Foo)) {
        return new Foo();
    }

    this.a = 0;
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

## Options

This rule has an object option:

- `"treatUndefinedAsUnspecified": false` (default) always either specify values or return `undefined` implicitly only.
- `"treatUndefinedAsUnspecified": true` always either specify values or return `undefined` explicitly or implicitly.

### treatUndefinedAsUnspecified

Examples of incorrect code for this rule with the default `{ "treatUndefinedAsUnspecified": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC1yZXR1cm46IFtcImVycm9yXCIsIHsgXCJ0cmVhdFVuZGVmaW5lZEFzVW5zcGVjaWZpZWRcIjogZmFsc2UgfV0qL1xuXG5mdW5jdGlvbiBmb28oY2FsbGJhY2spIHtcbiAgICBpZiAoY2FsbGJhY2spIHtcbiAgICAgICAgcmV0dXJuIHZvaWQgY2FsbGJhY2soKTtcbiAgICB9XG4gICAgLy8gbm8gcmV0dXJuIHN0YXRlbWVudFxufVxuXG5mdW5jdGlvbiBiYXIoY29uZGl0aW9uKSB7XG4gICAgaWYgKGNvbmRpdGlvbikge1xuICAgICAgICByZXR1cm4gdW5kZWZpbmVkO1xuICAgIH1cbiAgICAvLyBubyByZXR1cm4gc3RhdGVtZW50XG59In0=)

```
/*eslint consistent-return: ["error", { "treatUndefinedAsUnspecified": false }]*/

function foo(callback) {
    if (callback) {
        return void callback();
    }
    // no return statement
}

function bar(condition) {
    if (condition) {
        return undefined;
    }
    // no return statement
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

Examples of incorrect code for this rule with the `{ "treatUndefinedAsUnspecified": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC1yZXR1cm46IFtcImVycm9yXCIsIHsgXCJ0cmVhdFVuZGVmaW5lZEFzVW5zcGVjaWZpZWRcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGZvbyhjYWxsYmFjaykge1xuICAgIGlmIChjYWxsYmFjaykge1xuICAgICAgICByZXR1cm4gdm9pZCBjYWxsYmFjaygpO1xuICAgIH1cbiAgICByZXR1cm4gdHJ1ZTtcbn1cblxuZnVuY3Rpb24gYmFyKGNvbmRpdGlvbikge1xuICAgIGlmIChjb25kaXRpb24pIHtcbiAgICAgICAgcmV0dXJuIHVuZGVmaW5lZDtcbiAgICB9XG4gICAgcmV0dXJuIHRydWU7XG59In0=)

```
/*eslint consistent-return: ["error", { "treatUndefinedAsUnspecified": true }]*/

function foo(callback) {
    if (callback) {
        return void callback();
    }
    return true;
}

function bar(condition) {
    if (condition) {
        return undefined;
    }
    return true;
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

Examples of correct code for this rule with the `{ "treatUndefinedAsUnspecified": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY29uc2lzdGVudC1yZXR1cm46IFtcImVycm9yXCIsIHsgXCJ0cmVhdFVuZGVmaW5lZEFzVW5zcGVjaWZpZWRcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGZvbyhjYWxsYmFjaykge1xuICAgIGlmIChjYWxsYmFjaykge1xuICAgICAgICByZXR1cm4gdm9pZCBjYWxsYmFjaygpO1xuICAgIH1cbiAgICAvLyBubyByZXR1cm4gc3RhdGVtZW50XG59XG5cbmZ1bmN0aW9uIGJhcihjb25kaXRpb24pIHtcbiAgICBpZiAoY29uZGl0aW9uKSB7XG4gICAgICAgIHJldHVybiB1bmRlZmluZWQ7XG4gICAgfVxuICAgIC8vIG5vIHJldHVybiBzdGF0ZW1lbnRcbn0ifQ==)

```
/*eslint consistent-return: ["error", { "treatUndefinedAsUnspecified": true }]*/

function foo(callback) {
    if (callback) {
        return void callback();
    }
    // no return statement
}

function bar(condition) {
    if (condition) {
        return undefined;
    }
    // no return statement
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

If you want to allow functions to have different `return` behavior depending on code branching, then it is safe to disable this rule.

## Version

This rule was introduced in ESLint v0.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/consistent-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/consistent-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/consistent-return.md
                    
                
                )
