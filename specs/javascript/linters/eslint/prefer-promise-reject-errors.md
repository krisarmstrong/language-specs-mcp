# prefer-promise-reject-errors

Require using Error objects as Promise rejection reasons

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [Known Limitations](#known-limitations)
4. [When Not To Use It](#when-not-to-use-it)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Further Reading](#further-reading)
8. [Resources](#resources)

It is considered good practice to only pass instances of the built-in `Error` object to the `reject()` function for user-defined errors in Promises. `Error` objects automatically store a stack trace, which can be used to debug an error by determining where it came from. If a Promise is rejected with a non-`Error` value, it can be difficult to determine where the rejection occurred.

## Rule Details

This rule aims to ensure that Promises are only rejected with `Error` objects.

## Options

This rule takes one optional object argument:

- `allowEmptyReject: true` (`false` by default) allows calls to `Promise.reject()` with no arguments.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXByb21pc2UtcmVqZWN0LWVycm9yczogXCJlcnJvclwiKi9cblxuUHJvbWlzZS5yZWplY3QoXCJzb21ldGhpbmcgYmFkIGhhcHBlbmVkXCIpO1xuXG5Qcm9taXNlLnJlamVjdCg1KTtcblxuUHJvbWlzZS5yZWplY3QoKTtcblxubmV3IFByb21pc2UoZnVuY3Rpb24ocmVzb2x2ZSwgcmVqZWN0KSB7XG4gIHJlamVjdChcInNvbWV0aGluZyBiYWQgaGFwcGVuZWRcIik7XG59KTtcblxubmV3IFByb21pc2UoZnVuY3Rpb24ocmVzb2x2ZSwgcmVqZWN0KSB7XG4gIHJlamVjdCgpO1xufSk7XG4ifQ==)

```
/*eslint prefer-promise-reject-errors: "error"*/

Promise.reject("something bad happened");

Promise.reject(5);

Promise.reject();

new Promise(function(resolve, reject) {
  reject("something bad happened");
});

new Promise(function(resolve, reject) {
  reject();
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
16
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXByb21pc2UtcmVqZWN0LWVycm9yczogXCJlcnJvclwiKi9cblxuUHJvbWlzZS5yZWplY3QobmV3IEVycm9yKFwic29tZXRoaW5nIGJhZCBoYXBwZW5lZFwiKSk7XG5cblByb21pc2UucmVqZWN0KG5ldyBUeXBlRXJyb3IoXCJzb21ldGhpbmcgYmFkIGhhcHBlbmVkXCIpKTtcblxubmV3IFByb21pc2UoZnVuY3Rpb24ocmVzb2x2ZSwgcmVqZWN0KSB7XG4gIHJlamVjdChuZXcgRXJyb3IoXCJzb21ldGhpbmcgYmFkIGhhcHBlbmVkXCIpKTtcbn0pO1xuXG5jb25zdCBmb28gPSBnZXRVbmtub3duVmFsdWUoKTtcblByb21pc2UucmVqZWN0KGZvbyk7In0=)

```
/*eslint prefer-promise-reject-errors: "error"*/

Promise.reject(new Error("something bad happened"));

Promise.reject(new TypeError("something bad happened"));

new Promise(function(resolve, reject) {
  reject(new Error("something bad happened"));
});

const foo = getUnknownValue();
Promise.reject(foo);
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

Examples of correct code for this rule with the `allowEmptyReject: true` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLXByb21pc2UtcmVqZWN0LWVycm9yczogW1wiZXJyb3JcIiwge1wiYWxsb3dFbXB0eVJlamVjdFwiOiB0cnVlfV0qL1xuXG5Qcm9taXNlLnJlamVjdCgpO1xuXG5uZXcgUHJvbWlzZShmdW5jdGlvbihyZXNvbHZlLCByZWplY3QpIHtcbiAgcmVqZWN0KCk7XG59KTsifQ==)

```
/*eslint prefer-promise-reject-errors: ["error", {"allowEmptyReject": true}]*/

Promise.reject();

new Promise(function(resolve, reject) {
  reject();
});
1
2
3
4
5
6
7
```

## Known Limitations

Due to the limits of static analysis, this rule cannot guarantee that you will only reject Promises with `Error` objects. While the rule will report cases where it can guarantee that the rejection reason is clearly not an `Error`, it will not report cases where there is uncertainty about whether a given reason is an `Error`. For more information on this caveat, see the [similar limitations](no-throw-literal#known-limitations) in the `no-throw-literal` rule.

To avoid conflicts between rules, this rule does not report non-error values used in `throw` statements in async functions, even though these lead to Promise rejections. To lint for these cases, use the [no-throw-literal](no-throw-literal) rule.

## When Not To Use It

If you’re using custom non-error values as Promise rejection reasons, you can turn off this rule.

## Related Rules

- [no-throw-literal](/docs/latest/rules/no-throw-literal)

## Version

This rule was introduced in ESLint v3.14.0.

## Further Reading

[Warning Explanations | bluebird](http://bluebirdjs.com/docs/warning-explanations.html#warning-a-promise-was-rejected-with-a-non-error)
 bluebirdjs.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-promise-reject-errors.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-promise-reject-errors.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-promise-reject-errors.md
                    
                
                )
