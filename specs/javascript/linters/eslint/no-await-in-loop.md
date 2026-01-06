# no-await-in-loop

Disallow `await` inside of loops

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

Performing an operation on each element of an iterable is a common task. However, performing an `await` as part of each operation may indicate that the program is not taking full advantage of the parallelization benefits of `async`/`await`.

Often, the code can be refactored to create all the promises at once, then get access to the results using `Promise.all()` (or one of the other [promise concurrency methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)). Otherwise, each successive operation will not start until the previous one has completed.

Concretely, the following function could be refactored as shown:

```
async function foo(things) {
  const results = [];
  for (const thing of things) {
    // Bad: each loop iteration is delayed until the entire asynchronous operation completes
    results.push(await doAsyncWork(thing));
  }
  return results;
}
1
2
3
4
5
6
7
8
```

Copy code to clipboard

```
async function foo(things) {
  const promises = [];
  for (const thing of things) {
    // Good: all asynchronous operations are immediately started.
    promises.push(doAsyncWork(thing));
  }
  // Now that all the asynchronous operations are running, here we wait until they all complete.
  const results = await Promise.all(promises);
  return results;
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
```

Copy code to clipboard

This can be beneficial for subtle error-handling reasons as well. Given an array of promises that might reject, sequential awaiting puts the program at risk of unhandled promise rejections. The exact behavior of unhandled rejections depends on the environment running your code, but they are generally considered harmful regardless. In Node.js, for example, [unhandled rejections cause a program to terminate](https://nodejs.org/api/cli.html#--unhandled-rejectionsmode) unless configured otherwise.

```
async function foo() {
    const arrayOfPromises = somethingThatCreatesAnArrayOfPromises();
    for (const promise of arrayOfPromises) {
        // Bad: if any of the promises reject, an exception is thrown, and
        // subsequent loop iterations will not run. Therefore, rejections later
        // in the array will become unhandled rejections that cannot be caught
        // by a caller.
        const value = await promise;
        console.log(value);
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

Copy code to clipboard

```
async function foo() {
    const arrayOfPromises = somethingThatCreatesAnArrayOfPromises();
    // Good: Any rejections will cause a single exception to be thrown here,
    // which may be caught and handled by the caller.
    const arrayOfValues = await Promise.all(arrayOfPromises);
    for (const value of arrayOfValues) {
        console.log(value);
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

This rule disallows the use of `await` within loop bodies.

## Examples

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYXdhaXQtaW4tbG9vcDogXCJlcnJvclwiKi9cblxuYXN5bmMgZnVuY3Rpb24gZm9vKHRoaW5ncykge1xuICBjb25zdCBwcm9taXNlcyA9IFtdO1xuICBmb3IgKGNvbnN0IHRoaW5nIG9mIHRoaW5ncykge1xuICAgIC8vIEdvb2Q6IGFsbCBhc3luY2hyb25vdXMgb3BlcmF0aW9ucyBhcmUgaW1tZWRpYXRlbHkgc3RhcnRlZC5cbiAgICBwcm9taXNlcy5wdXNoKGRvQXN5bmNXb3JrKHRoaW5nKSk7XG4gIH1cbiAgLy8gTm93IHRoYXQgYWxsIHRoZSBhc3luY2hyb25vdXMgb3BlcmF0aW9ucyBhcmUgcnVubmluZywgaGVyZSB3ZSB3YWl0IHVudGlsIHRoZXkgYWxsIGNvbXBsZXRlLlxuICBjb25zdCByZXN1bHRzID0gYXdhaXQgUHJvbWlzZS5hbGwocHJvbWlzZXMpO1xuICByZXR1cm4gcmVzdWx0cztcbn0ifQ==)

```
/*eslint no-await-in-loop: "error"*/

async function foo(things) {
  const promises = [];
  for (const thing of things) {
    // Good: all asynchronous operations are immediately started.
    promises.push(doAsyncWork(thing));
  }
  // Now that all the asynchronous operations are running, here we wait until they all complete.
  const results = await Promise.all(promises);
  return results;
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

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYXdhaXQtaW4tbG9vcDogXCJlcnJvclwiKi9cblxuYXN5bmMgZnVuY3Rpb24gZm9vKHRoaW5ncykge1xuICBjb25zdCByZXN1bHRzID0gW107XG4gIGZvciAoY29uc3QgdGhpbmcgb2YgdGhpbmdzKSB7XG4gICAgLy8gQmFkOiBlYWNoIGxvb3AgaXRlcmF0aW9uIGlzIGRlbGF5ZWQgdW50aWwgdGhlIGVudGlyZSBhc3luY2hyb25vdXMgb3BlcmF0aW9uIGNvbXBsZXRlc1xuICAgIHJlc3VsdHMucHVzaChhd2FpdCBkb0FzeW5jV29yayh0aGluZykpO1xuICB9XG4gIHJldHVybiByZXN1bHRzO1xufVxuXG5hc3luYyBmdW5jdGlvbiBiYXIodGhpbmdzKSB7XG4gIGZvciAoY29uc3QgdGhpbmcgb2YgdGhpbmdzKSB7XG4gICAgYXdhaXQgdXNpbmcgcmVzb3VyY2UgPSBnZXRBc3luY1Jlc291cmNlKHRoaW5nKTtcbiAgfVxufSJ9)

```
/*eslint no-await-in-loop: "error"*/

async function foo(things) {
  const results = [];
  for (const thing of things) {
    // Bad: each loop iteration is delayed until the entire asynchronous operation completes
    results.push(await doAsyncWork(thing));
  }
  return results;
}

async function bar(things) {
  for (const thing of things) {
    await using resource = getAsyncResource(thing);
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

## When Not To Use It

In many cases the iterations of a loop are not actually independent of each other, and awaiting in the loop is correct. As a few examples:

- 

The output of one iteration might be used as the input to another.

```
async function loopIterationsDependOnEachOther() {
    let previousResult = null;
    for (let i = 0; i < 10; i++) {
        const result = await doSomething(i, previousResult);
        if (someCondition(result, previousResult)) {
            break;
        } else {
            previousResult = result;
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
```

Copy code to clipboard
- 

Loops may be used to retry asynchronous operations that were unsuccessful.

```
async function retryUpTo10Times() {
    for (let i = 0; i < 10; i++) {
        const wasSuccessful = await tryToDoSomething();
        if (wasSuccessful)
            return 'succeeded!';
        // wait to try again.
        await new Promise(resolve => setTimeout(resolve, 1000));
    }
    return 'failed!';
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
```

Copy code to clipboard
- 

Loops may be used to prevent your code from sending an excessive amount of requests in parallel.

```
async function makeUpdatesToRateLimitedApi(thingsToUpdate) {
    // we'll exceed our rate limit if we make all the network calls in parallel.
    for (const thing of thingsToUpdate) {
        await updateThingWithRateLimitedApi(thing);
    }
}
1
2
3
4
5
6
```

Copy code to clipboard

In such cases it makes sense to use `await` within a loop and it is recommended to disable the rule via a standard ESLint disable comment.

## Version

This rule was introduced in ESLint v3.12.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-await-in-loop.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-await-in-loop.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-await-in-loop.md
                    
                
                )
