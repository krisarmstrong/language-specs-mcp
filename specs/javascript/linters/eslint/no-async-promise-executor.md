# no-async-promise-executor

Disallow using an async function as a Promise executor

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

The `new Promise` constructor accepts an executor function as an argument, which has `resolve` and `reject` parameters that can be used to control the state of the created Promise. For example:

```
const result = new Promise(function executor(resolve, reject) {
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

The executor function can also be an `async function`. However, this is usually a mistake, for a few reasons:

- If an async executor function throws an error, the error will be lost and won’t cause the newly-constructed `Promise` to reject. This could make it difficult to debug and handle some errors.
- If a Promise executor function is using `await`, this is usually a sign that it is not actually necessary to use the `new Promise` constructor, or the scope of the `new Promise` constructor can be reduced.

## Rule Details

This rule aims to disallow async Promise executor functions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYXN5bmMtcHJvbWlzZS1leGVjdXRvcjogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0gbmV3IFByb21pc2UoYXN5bmMgKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICByZWFkRmlsZSgnZm9vLnR4dCcsIGZ1bmN0aW9uKGVyciwgcmVzdWx0KSB7XG4gICAgaWYgKGVycikge1xuICAgICAgcmVqZWN0KGVycik7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJlc29sdmUocmVzdWx0KTtcbiAgICB9XG4gIH0pO1xufSk7XG5cbmNvbnN0IHJlc3VsdCA9IG5ldyBQcm9taXNlKGFzeW5jIChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgcmVzb2x2ZShhd2FpdCBmb28pO1xufSk7In0=)

```
/*eslint no-async-promise-executor: "error"*/

const foo = new Promise(async (resolve, reject) => {
  readFile('foo.txt', function(err, result) {
    if (err) {
      reject(err);
    } else {
      resolve(result);
    }
  });
});

const result = new Promise(async (resolve, reject) => {
  resolve(await foo);
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
12
13
14
15
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYXN5bmMtcHJvbWlzZS1leGVjdXRvcjogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0gbmV3IFByb21pc2UoKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICByZWFkRmlsZSgnZm9vLnR4dCcsIGZ1bmN0aW9uKGVyciwgcmVzdWx0KSB7XG4gICAgaWYgKGVycikge1xuICAgICAgcmVqZWN0KGVycik7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJlc29sdmUocmVzdWx0KTtcbiAgICB9XG4gIH0pO1xufSk7XG5cbmNvbnN0IHJlc3VsdCA9IFByb21pc2UucmVzb2x2ZShmb28pOyJ9)

```
/*eslint no-async-promise-executor: "error"*/

const foo = new Promise((resolve, reject) => {
  readFile('foo.txt', function(err, result) {
    if (err) {
      reject(err);
    } else {
      resolve(result);
    }
  });
});

const result = Promise.resolve(foo);
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

## When Not To Use It

If your codebase doesn’t support `async function` syntax, there’s no need to enable this rule.

## Version

This rule was introduced in ESLint v5.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-async-promise-executor.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-async-promise-executor.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-async-promise-executor.md
                    
                
                )
