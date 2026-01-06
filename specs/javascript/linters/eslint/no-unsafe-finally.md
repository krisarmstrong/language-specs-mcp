# no-unsafe-finally

Disallow control flow statements in `finally` blocks

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

JavaScript suspends the control flow statements of `try` and `catch` blocks until the execution of `finally` block finishes. So, when `return`, `throw`, `break`, or `continue` is used in `finally`, control flow statements inside `try` and `catch` are overwritten, which is considered as unexpected behavior. Such as:

```
// We expect this function to return 1;
(() => {
    try {
        return 1; // 1 is returned but suspended until finally block ends
    } catch(err) {
        return 2;
    } finally {
        return 3; // 3 is returned before 1, which we did not expect
    }
})();

// > 3
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

Copy code to clipboard

```
// We expect this function to throw an error, then return
(() => {
    try {
        throw new Error("Try"); // error is thrown but suspended until finally block ends
    } finally {
        return 3; // 3 is returned before the error is thrown, which we did not expect
    }
})();

// > 3
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
```

Copy code to clipboard

```
// We expect this function to throw Try(...) error from the catch block
(() => {
    try {
        throw new Error("Try")
    } catch(err) {
        throw err; // The error thrown from try block is caught and rethrown
    } finally {
        throw new Error("Finally"); // Finally(...) is thrown, which we did not expect
    }
})();

// > Uncaught Error: Finally(...)
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

Copy code to clipboard

```
// We expect this function to return 0 from try block.
(() => {
  label: try {
    return 0; // 0 is returned but suspended until finally block ends
  } finally {
    break label; // It breaks out the try-finally block, before 0 is returned.
  }
  return 1;
})();

// > 1
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

Copy code to clipboard

## Rule Details

This rule disallows `return`, `throw`, `break`, and `continue` statements inside `finally` blocks. It allows indirect usages, such as in `function` or `class` definitions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLWZpbmFsbHk6IFwiZXJyb3JcIiovXG5sZXQgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgdHJ5IHtcbiAgICAgICAgcmV0dXJuIDE7XG4gICAgfSBjYXRjaChlcnIpIHtcbiAgICAgICAgcmV0dXJuIDI7XG4gICAgfSBmaW5hbGx5IHtcbiAgICAgICAgcmV0dXJuIDM7XG4gICAgfVxufTsifQ==)

```
/*eslint no-unsafe-finally: "error"*/
let foo = function() {
    try {
        return 1;
    } catch(err) {
        return 2;
    } finally {
        return 3;
    }
};
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
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLWZpbmFsbHk6IFwiZXJyb3JcIiovXG5sZXQgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgdHJ5IHtcbiAgICAgICAgcmV0dXJuIDE7XG4gICAgfSBjYXRjaChlcnIpIHtcbiAgICAgICAgcmV0dXJuIDI7XG4gICAgfSBmaW5hbGx5IHtcbiAgICAgICAgdGhyb3cgbmV3IEVycm9yO1xuICAgIH1cbn07In0=)

```
/*eslint no-unsafe-finally: "error"*/
let foo = function() {
    try {
        return 1;
    } catch(err) {
        return 2;
    } finally {
        throw new Error;
    }
};
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLWZpbmFsbHk6IFwiZXJyb3JcIiovXG5sZXQgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgdHJ5IHtcbiAgICAgICAgcmV0dXJuIDE7XG4gICAgfSBjYXRjaChlcnIpIHtcbiAgICAgICAgcmV0dXJuIDI7XG4gICAgfSBmaW5hbGx5IHtcbiAgICAgICAgY29uc29sZS5sb2coXCJob2xhIVwiKTtcbiAgICB9XG59OyJ9)

```
/*eslint no-unsafe-finally: "error"*/
let foo = function() {
    try {
        return 1;
    } catch(err) {
        return 2;
    } finally {
        console.log("hola!");
    }
};
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
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLWZpbmFsbHk6IFwiZXJyb3JcIiovXG5sZXQgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgdHJ5IHtcbiAgICAgICAgcmV0dXJuIDE7XG4gICAgfSBjYXRjaChlcnIpIHtcbiAgICAgICAgcmV0dXJuIDI7XG4gICAgfSBmaW5hbGx5IHtcbiAgICAgICAgbGV0IGEgPSBmdW5jdGlvbigpIHtcbiAgICAgICAgICAgIHJldHVybiBcImhvbGEhXCI7XG4gICAgICAgIH1cbiAgICB9XG59OyJ9)

```
/*eslint no-unsafe-finally: "error"*/
let foo = function() {
    try {
        return 1;
    } catch(err) {
        return 2;
    } finally {
        let a = function() {
            return "hola!";
        }
    }
};
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLWZpbmFsbHk6IFwiZXJyb3JcIiovXG5sZXQgZm9vID0gZnVuY3Rpb24oYSkge1xuICAgIHRyeSB7XG4gICAgICAgIHJldHVybiAxO1xuICAgIH0gY2F0Y2goZXJyKSB7XG4gICAgICAgIHJldHVybiAyO1xuICAgIH0gZmluYWxseSB7XG4gICAgICAgIHN3aXRjaChhKSB7XG4gICAgICAgICAgICBjYXNlIDE6IHtcbiAgICAgICAgICAgICAgICBjb25zb2xlLmxvZyhcImhvbGEhXCIpXG4gICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9XG59OyJ9)

```
/*eslint no-unsafe-finally: "error"*/
let foo = function(a) {
    try {
        return 1;
    } catch(err) {
        return 2;
    } finally {
        switch(a) {
            case 1: {
                console.log("hola!")
                break;
            }
        }
    }
};
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

If you want to allow control flow operations in `finally` blocks, you can turn this rule off.

## Version

This rule was introduced in ESLint v2.9.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unsafe-finally.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unsafe-finally.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unsafe-finally.md
                    
                
                )
