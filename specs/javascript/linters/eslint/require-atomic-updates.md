# require-atomic-updates

Disallow assignments that can lead to race conditions due to usage of `await` or `yield`

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Variables](#variables)
  2. [Properties](#properties)

2. [Options](#options)

  1. [allowProperties](#allowproperties)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

When writing asynchronous code, it is possible to create subtle race condition bugs. Consider the following example:

```
let totalLength = 0;

async function addLengthOfSinglePage(pageNum) {
  totalLength += await getPageLength(pageNum);
}

Promise.all([addLengthOfSinglePage(1), addLengthOfSinglePage(2)]).then(() => {
  console.log('The combined length of both pages is', totalLength);
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

This code looks like it will sum the results of calling `getPageLength(1)` and `getPageLength(2)`, but in reality the final value of `totalLength` will only be the length of one of the two pages. The bug is in the statement `totalLength += await getPageLength(pageNum);`. This statement first reads an initial value of `totalLength`, then calls `getPageLength(pageNum)` and waits for that Promise to fulfill. Finally, it sets the value of `totalLength` to the sum of `await getPageLength(pageNum)` and the initial value of `totalLength`. If the `totalLength` variable is updated in a separate function call during the time that the `getPageLength(pageNum)` Promise is pending, that update will be lost because the new value is overwritten without being read.

One way to fix this issue would be to ensure that `totalLength` is read at the same time as it’s updated, like this:

```
async function addLengthOfSinglePage(pageNum) {
  const lengthOfThisPage = await getPageLength(pageNum);

  totalLength += lengthOfThisPage;
}
1
2
3
4
5
```

Copy code to clipboard

Another solution would be to avoid using a mutable variable reference at all:

```
Promise.all([getPageLength(1), getPageLength(2)]).then(pageLengths => {
  const totalLength = pageLengths.reduce((accumulator, length) => accumulator + length, 0);

  console.log('The combined length of both pages is', totalLength);
});
1
2
3
4
5
```

Copy code to clipboard

## Rule Details

This rule aims to report assignments to variables or properties in cases where the assignments may be based on outdated values.

### Variables

This rule reports an assignment to a variable when it detects the following execution flow in a generator or async function:

1. The variable is read.
2. A `yield` or `await` pauses the function.
3. After the function is resumed, a value is assigned to the variable from step 1.

The assignment in step 3 is reported because it may be incorrectly resolved because the value of the variable from step 1 may have changed between steps 2 and 3. In particular, if the variable can be accessed from other execution contexts (for example, if it is not a local variable and therefore other functions can change it), the value of the variable may have changed elsewhere while the function was paused in step 2.

Note that the rule does not report the assignment in step 3 in any of the following cases:

- If the variable is read again between steps 2 and 3.
- If the variable cannot be accessed while the function is paused (for example, if it’s a local variable).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHJlcXVpcmUtYXRvbWljLXVwZGF0ZXM6IGVycm9yICovXG5cbmxldCByZXN1bHQ7XG5cbmFzeW5jIGZ1bmN0aW9uIGZvbygpIHtcbiAgICByZXN1bHQgKz0gYXdhaXQgc29tZXRoaW5nO1xufVxuXG5hc3luYyBmdW5jdGlvbiBiYXIoKSB7XG4gICAgcmVzdWx0ID0gcmVzdWx0ICsgYXdhaXQgc29tZXRoaW5nO1xufVxuXG5hc3luYyBmdW5jdGlvbiBiYXooKSB7XG4gICAgcmVzdWx0ID0gcmVzdWx0ICsgZG9Tb21ldGhpbmcoYXdhaXQgc29tZXRoaW5nRWxzZSk7XG59XG5cbmFzeW5jIGZ1bmN0aW9uIHF1eCgpIHtcbiAgICBpZiAoIXJlc3VsdCkge1xuICAgICAgICByZXN1bHQgPSBhd2FpdCBpbml0aWFsaXplKCk7XG4gICAgfVxufVxuXG5mdW5jdGlvbiogZ2VuZXJhdG9yKCkge1xuICAgIHJlc3VsdCArPSB5aWVsZDtcbn0ifQ==)

```
/* eslint require-atomic-updates: error */

let result;

async function foo() {
    result += await something;
}

async function bar() {
    result = result + await something;
}

async function baz() {
    result = result + doSomething(await somethingElse);
}

async function qux() {
    if (!result) {
        result = await initialize();
    }
}

function* generator() {
    result += yield;
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHJlcXVpcmUtYXRvbWljLXVwZGF0ZXM6IGVycm9yICovXG5cbmxldCByZXN1bHQ7XG5cbmFzeW5jIGZ1bmN0aW9uIGZvb2JhcigpIHtcbiAgICByZXN1bHQgPSBhd2FpdCBzb21ldGhpbmcgKyByZXN1bHQ7XG59XG5cbmFzeW5jIGZ1bmN0aW9uIGJheigpIHtcbiAgICBjb25zdCB0bXAgPSBkb1NvbWV0aGluZyhhd2FpdCBzb21ldGhpbmdFbHNlKTtcbiAgICByZXN1bHQgKz0gdG1wO1xufVxuXG5hc3luYyBmdW5jdGlvbiBxdXgoKSB7XG4gICAgaWYgKCFyZXN1bHQpIHtcbiAgICAgICAgY29uc3QgdG1wID0gYXdhaXQgaW5pdGlhbGl6ZSgpO1xuICAgICAgICBpZiAoIXJlc3VsdCkge1xuICAgICAgICAgICAgcmVzdWx0ID0gdG1wO1xuICAgICAgICB9XG4gICAgfVxufVxuXG5hc3luYyBmdW5jdGlvbiBxdXV4KCkge1xuICAgIGxldCBsb2NhbFZhcmlhYmxlID0gMDtcbiAgICBsb2NhbFZhcmlhYmxlICs9IGF3YWl0IHNvbWV0aGluZztcbn1cblxuZnVuY3Rpb24qIGdlbmVyYXRvcigpIHtcbiAgICByZXN1bHQgPSAoeWllbGQpICsgcmVzdWx0O1xufSJ9)

```
/* eslint require-atomic-updates: error */

let result;

async function foobar() {
    result = await something + result;
}

async function baz() {
    const tmp = doSomething(await somethingElse);
    result += tmp;
}

async function qux() {
    if (!result) {
        const tmp = await initialize();
        if (!result) {
            result = tmp;
        }
    }
}

async function quux() {
    let localVariable = 0;
    localVariable += await something;
}

function* generator() {
    result = (yield) + result;
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
```

### Properties

This rule reports an assignment to a property through a variable when it detects the following execution flow in a generator or async function:

1. The variable or object property is read.
2. A `yield` or `await` pauses the function.
3. After the function is resumed, a value is assigned to a property.

This logic is similar to the logic for variables, but stricter because the property in step 3 doesn’t have to be the same as the property in step 1. It is assumed that the flow depends on the state of the object as a whole.

Example of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHJlcXVpcmUtYXRvbWljLXVwZGF0ZXM6IGVycm9yICovXG5cbmFzeW5jIGZ1bmN0aW9uIGZvbyhvYmopIHtcbiAgICBpZiAoIW9iai5kb25lKSB7XG4gICAgICAgIG9iai5zb21ldGhpbmcgPSBhd2FpdCBnZXRTb21ldGhpbmcoKTtcbiAgICB9XG59In0=)

```
/* eslint require-atomic-updates: error */

async function foo(obj) {
    if (!obj.done) {
        obj.something = await getSomething();
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

Example of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHJlcXVpcmUtYXRvbWljLXVwZGF0ZXM6IGVycm9yICovXG5cbmFzeW5jIGZ1bmN0aW9uIGZvbyhvYmopIHtcbiAgICBpZiAoIW9iai5kb25lKSB7XG4gICAgICAgIGNvbnN0IHRtcCA9IGF3YWl0IGdldFNvbWV0aGluZygpO1xuICAgICAgICBpZiAoIW9iai5kb25lKSB7XG4gICAgICAgICAgICBvYmouc29tZXRoaW5nID0gdG1wO1xuICAgICAgICB9XG4gICAgfVxufSJ9)

```
/* eslint require-atomic-updates: error */

async function foo(obj) {
    if (!obj.done) {
        const tmp = await getSomething();
        if (!obj.done) {
            obj.something = tmp;
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
```

## Options

This rule has an object option:

- `"allowProperties"`: When set to `true`, the rule does not report assignments to properties. Default is `false`.

### allowProperties

Example of correct code for this rule with the `{ "allowProperties": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHJlcXVpcmUtYXRvbWljLXVwZGF0ZXM6IFtcImVycm9yXCIsIHsgXCJhbGxvd1Byb3BlcnRpZXNcIjogdHJ1ZSB9XSAqL1xuXG5hc3luYyBmdW5jdGlvbiBmb28ob2JqKSB7XG4gICAgaWYgKCFvYmouZG9uZSkge1xuICAgICAgICBvYmouc29tZXRoaW5nID0gYXdhaXQgZ2V0U29tZXRoaW5nKCk7XG4gICAgfVxufSJ9)

```
/* eslint require-atomic-updates: ["error", { "allowProperties": true }] */

async function foo(obj) {
    if (!obj.done) {
        obj.something = await getSomething();
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

## When Not To Use It

If you don’t use async or generator functions, you don’t need to enable this rule.

## Version

This rule was introduced in ESLint v5.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/require-atomic-updates.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/require-atomic-updates.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/require-atomic-updates.md
                    
                
                )
