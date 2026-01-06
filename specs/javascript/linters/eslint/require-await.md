# require-await

Disallow async functions which have no `await` expression

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Asynchronous functions in JavaScript behave differently than other functions in two important ways:

1. The return value is always a `Promise`.
2. You can use the `await` operator inside of them.

The primary reason to use asynchronous functions is typically to use the `await` operator, such as this:

```
async function fetchData(processDataItem) {
    const response = await fetch(DATA_URL);
    const data = await response.json();

    return data.map(processDataItem);
}
1
2
3
4
5
6
```

Copy code to clipboard

Asynchronous functions that don’t use `await` might not need to be asynchronous functions and could be the unintentional result of refactoring.

Note: this rule ignores async generator functions. This is because generators yield rather than return a value and async generators might yield all the values of another async generator without ever actually needing to use await.

## Rule Details

This rule warns async functions which have no `await` expression.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS1hd2FpdDogXCJlcnJvclwiKi9cblxuYXN5bmMgZnVuY3Rpb24gZm9vKCkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59XG5cbmJhcihhc3luYyAoKSA9PiB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0pOyJ9)

```
/*eslint require-await: "error"*/

async function foo() {
    doSomething();
}

bar(async () => {
    doSomething();
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS1hd2FpdDogXCJlcnJvclwiKi9cblxuYXN5bmMgZnVuY3Rpb24gZm9vKCkge1xuICAgIGF3YWl0IGRvU29tZXRoaW5nKCk7XG59XG5cbmJhcihhc3luYyAoKSA9PiB7XG4gICAgYXdhaXQgZG9Tb21ldGhpbmcoKTtcbn0pO1xuXG5mdW5jdGlvbiBiYXooKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuYmFyKCgpID0+IHtcbiAgICBkb1NvbWV0aGluZygpO1xufSk7XG5cbmFzeW5jIGZ1bmN0aW9uIHJlc291cmNlTWFuYWdlbWVudCgpIHtcbiAgICBhd2FpdCB1c2luZyByZXNvdXJjZSA9IGdldEFzeW5jUmVzb3VyY2UoKTtcbiAgICByZXNvdXJjZS51c2UoKTtcbn1cblxuLy8gQWxsb3cgZW1wdHkgZnVuY3Rpb25zLlxuYXN5bmMgZnVuY3Rpb24gbm9vcCgpIHt9In0=)

```
/*eslint require-await: "error"*/

async function foo() {
    await doSomething();
}

bar(async () => {
    await doSomething();
});

function baz() {
    doSomething();
}

bar(() => {
    doSomething();
});

async function resourceManagement() {
    await using resource = getAsyncResource();
    resource.use();
}

// Allow empty functions.
async function noop() {}
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
```

## When Not To Use It

Asynchronous functions are designed to work with promises such that throwing an error will cause a promise’s rejection handler (such as `catch()`) to be called. For example:

```
async function fail() {
    throw new Error("Failure!");
}

fail().catch(error => {
    console.log(error.message);
});
1
2
3
4
5
6
7
```

Copy code to clipboard

In this case, the `fail()` function throws an error that is intended to be caught by the `catch()` handler assigned later. Converting the `fail()` function into a synchronous function would require the call to `fail()` to be refactored to use a `try-catch` statement instead of a promise.

If you are throwing an error inside of an asynchronous function for this purpose, then you may want to disable this rule.

## Related Rules

- [require-yield](/docs/latest/rules/require-yield)

## Version

This rule was introduced in ESLint v3.11.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/require-await.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/require-await.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/require-await.md
                    
                
                )
