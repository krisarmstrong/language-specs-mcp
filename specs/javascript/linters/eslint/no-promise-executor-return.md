# no-promise-executor-return

Disallow returning values from Promise executor functions

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowVoid](#allowvoid)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

The `new Promise` constructor accepts a single argument, called an executor.

```
const myPromise = new Promise(function executor(resolve, reject) {
    readFile('foo.txt', function(err, result) {
        if (err) {
            reject(err);
        } else {
            resolve(result);
        }
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

The executor function usually initiates some asynchronous operation. Once it is finished, the executor should call `resolve` with the result, or `reject` if an error occurred.

The return value of the executor is ignored. Returning a value from an executor function is a possible error because the returned value cannot be used and it doesn’t affect the promise in any way.

## Rule Details

This rule disallows returning values from Promise executor functions.

Only `return` without a value is allowed, as it’s a control flow statement.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvbWlzZS1leGVjdXRvci1yZXR1cm46IFwiZXJyb3JcIiovXG5cbm5ldyBQcm9taXNlKChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICBpZiAoc29tZUNvbmRpdGlvbikge1xuICAgICAgICByZXR1cm4gZGVmYXVsdFJlc3VsdDtcbiAgICB9XG4gICAgZ2V0U29tZXRoaW5nKChlcnIsIHJlc3VsdCkgPT4ge1xuICAgICAgICBpZiAoZXJyKSB7XG4gICAgICAgICAgICByZWplY3QoZXJyKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHJlc29sdmUocmVzdWx0KTtcbiAgICAgICAgfVxuICAgIH0pO1xufSk7XG5cbm5ldyBQcm9taXNlKChyZXNvbHZlLCByZWplY3QpID0+IGdldFNvbWV0aGluZygoZXJyLCBkYXRhKSA9PiB7XG4gICAgaWYgKGVycikge1xuICAgICAgICByZWplY3QoZXJyKTtcbiAgICB9IGVsc2Uge1xuICAgICAgICByZXNvbHZlKGRhdGEpO1xuICAgIH1cbn0pKTtcblxubmV3IFByb21pc2UoKCkgPT4ge1xuICAgIHJldHVybiAxO1xufSk7XG5cbm5ldyBQcm9taXNlKHIgPT4gcigxKSk7In0=)

```
/*eslint no-promise-executor-return: "error"*/

new Promise((resolve, reject) => {
    if (someCondition) {
        return defaultResult;
    }
    getSomething((err, result) => {
        if (err) {
            reject(err);
        } else {
            resolve(result);
        }
    });
});

new Promise((resolve, reject) => getSomething((err, data) => {
    if (err) {
        reject(err);
    } else {
        resolve(data);
    }
}));

new Promise(() => {
    return 1;
});

new Promise(r => r(1));
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvbWlzZS1leGVjdXRvci1yZXR1cm46IFwiZXJyb3JcIiovXG5cbi8vIFR1cm4gcmV0dXJuIGlubGluZSBpbnRvIHR3byBsaW5lc1xubmV3IFByb21pc2UoKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgIGlmIChzb21lQ29uZGl0aW9uKSB7XG4gICAgICAgIHJlc29sdmUoZGVmYXVsdFJlc3VsdCk7XG4gICAgICAgIHJldHVybjtcbiAgICB9XG4gICAgZ2V0U29tZXRoaW5nKChlcnIsIHJlc3VsdCkgPT4ge1xuICAgICAgICBpZiAoZXJyKSB7XG4gICAgICAgICAgICByZWplY3QoZXJyKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHJlc29sdmUocmVzdWx0KTtcbiAgICAgICAgfVxuICAgIH0pO1xufSk7XG5cbi8vIEFkZCBjdXJseSBicmFjZXNcbm5ldyBQcm9taXNlKChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICBnZXRTb21ldGhpbmcoKGVyciwgZGF0YSkgPT4ge1xuICAgICAgICBpZiAoZXJyKSB7XG4gICAgICAgICAgICByZWplY3QoZXJyKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHJlc29sdmUoZGF0YSk7XG4gICAgICAgIH1cbiAgICB9KTtcbn0pO1xuXG5uZXcgUHJvbWlzZShyID0+IHsgcigxKSB9KTtcbi8vIG9yIGp1c3QgdXNlIFByb21pc2UucmVzb2x2ZVxuUHJvbWlzZS5yZXNvbHZlKDEpOyJ9)

```
/*eslint no-promise-executor-return: "error"*/

// Turn return inline into two lines
new Promise((resolve, reject) => {
    if (someCondition) {
        resolve(defaultResult);
        return;
    }
    getSomething((err, result) => {
        if (err) {
            reject(err);
        } else {
            resolve(result);
        }
    });
});

// Add curly braces
new Promise((resolve, reject) => {
    getSomething((err, data) => {
        if (err) {
            reject(err);
        } else {
            resolve(data);
        }
    });
});

new Promise(r => { r(1) });
// or just use Promise.resolve
Promise.resolve(1);
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

## Options

This rule takes one option, an object, with the following properties:

- `allowVoid`: If set to `true` (`false` by default), this rule will allow returning void values.

### allowVoid

Examples of correct code for this rule with the `{ "allowVoid": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcHJvbWlzZS1leGVjdXRvci1yZXR1cm46IFtcImVycm9yXCIsIHsgYWxsb3dWb2lkOiB0cnVlIH1dKi9cblxubmV3IFByb21pc2UoKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgIGlmIChzb21lQ29uZGl0aW9uKSB7XG4gICAgICAgIHJldHVybiB2b2lkIHJlc29sdmUoZGVmYXVsdFJlc3VsdCk7XG4gICAgfVxuICAgIGdldFNvbWV0aGluZygoZXJyLCByZXN1bHQpID0+IHtcbiAgICAgICAgaWYgKGVycikge1xuICAgICAgICAgICAgcmVqZWN0KGVycik7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICByZXNvbHZlKHJlc3VsdCk7XG4gICAgICAgIH1cbiAgICB9KTtcbn0pO1xuXG5uZXcgUHJvbWlzZSgocmVzb2x2ZSwgcmVqZWN0KSA9PiB2b2lkIGdldFNvbWV0aGluZygoZXJyLCBkYXRhKSA9PiB7XG4gICAgaWYgKGVycikge1xuICAgICAgICByZWplY3QoZXJyKTtcbiAgICB9IGVsc2Uge1xuICAgICAgICByZXNvbHZlKGRhdGEpO1xuICAgIH1cbn0pKTtcblxubmV3IFByb21pc2UociA9PiB2b2lkIHIoMSkpOyJ9)

```
/*eslint no-promise-executor-return: ["error", { allowVoid: true }]*/

new Promise((resolve, reject) => {
    if (someCondition) {
        return void resolve(defaultResult);
    }
    getSomething((err, result) => {
        if (err) {
            reject(err);
        } else {
            resolve(result);
        }
    });
});

new Promise((resolve, reject) => void getSomething((err, data) => {
    if (err) {
        reject(err);
    } else {
        resolve(data);
    }
}));

new Promise(r => void r(1));
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

## Related Rules

- [no-async-promise-executor](/docs/latest/rules/no-async-promise-executor)

## Version

This rule was introduced in ESLint v7.3.0.

## Further Reading

[Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-promise-executor-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-promise-executor-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-promise-executor-return.md
                    
                
                )
