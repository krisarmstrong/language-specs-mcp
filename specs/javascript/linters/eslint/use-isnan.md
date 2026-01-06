# use-isnan

Require calls to `isNaN()` when checking for `NaN`

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [enforceForSwitchCase](#enforceforswitchcase)
  2. [enforceForIndexOf](#enforceforindexof)

    1. [Known Limitations](#known-limitations)

3. [Version](#version)
4. [Resources](#resources)

In JavaScript, `NaN` is a special value of the `Number` type. It’s used to represent any of the “not-a-number” values represented by the double-precision 64-bit format as specified by the IEEE Standard for Binary Floating-Point Arithmetic.

Because `NaN` is unique in JavaScript by not being equal to anything, including itself, the results of comparisons to `NaN` are confusing:

- `NaN === NaN` or `NaN == NaN` evaluate to `false`
- `NaN !== NaN` or `NaN != NaN` evaluate to `true`

Therefore, use `Number.isNaN()` or global `isNaN()` functions to test whether a value is `NaN`.

## Rule Details

This rule disallows comparisons to `NaN`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBcImVycm9yXCIqL1xuXG5pZiAoZm9vID09IE5hTikge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoZm9vICE9IE5hTikge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoZm9vID09IE51bWJlci5OYU4pIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKGZvbyAhPSBOdW1iZXIuTmFOKSB7XG4gICAgLy8gLi4uXG59In0=)

```
/*eslint use-isnan: "error"*/

if (foo == NaN) {
    // ...
}

if (foo != NaN) {
    // ...
}

if (foo == Number.NaN) {
    // ...
}

if (foo != Number.NaN) {
    // ...
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBcImVycm9yXCIqL1xuXG5pZiAoaXNOYU4oZm9vKSkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoIWlzTmFOKGZvbykpIHtcbiAgICAvLyAuLi5cbn0ifQ==)

```
/*eslint use-isnan: "error"*/

if (isNaN(foo)) {
    // ...
}

if (!isNaN(foo)) {
    // ...
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

## Options

This rule has an object option, with two options:

- `"enforceForSwitchCase": true` (default) additionally disallows `case NaN` and `switch(NaN)` in `switch` statements.
- `"enforceForIndexOf": true` additionally disallows the use of `indexOf` and `lastIndexOf` methods with `NaN`. Default is `false`, meaning that this rule by default does not warn about `indexOf(NaN)` or `lastIndexOf(NaN)` method calls.

### enforceForSwitchCase

The `switch` statement internally uses the `===` comparison to match the expression’s value to a case clause. Therefore, it can never match `case NaN`. Also, `switch(NaN)` can never match a case clause.

Examples of incorrect code for this rule with `"enforceForSwitchCase"` option set to `true` (default):

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9yU3dpdGNoQ2FzZVwiOiB0cnVlfV0qL1xuXG5zd2l0Y2ggKGZvbykge1xuICAgIGNhc2UgTmFOOlxuICAgICAgICBiYXIoKTtcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSAxOlxuICAgICAgICBiYXooKTtcbiAgICAgICAgYnJlYWs7XG4gICAgLy8gLi4uXG59XG5cbnN3aXRjaCAoTmFOKSB7XG4gICAgY2FzZSBhOlxuICAgICAgICBiYXIoKTtcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSBiOlxuICAgICAgICBiYXooKTtcbiAgICAgICAgYnJlYWs7XG4gICAgLy8gLi4uXG59XG5cbnN3aXRjaCAoZm9vKSB7XG4gICAgY2FzZSBOdW1iZXIuTmFOOlxuICAgICAgICBiYXIoKTtcbiAgICAgICAgYnJlYWs7XG4gICAgY2FzZSAxOlxuICAgICAgICBiYXooKTtcbiAgICAgICAgYnJlYWs7XG4gICAgLy8gLi4uXG59XG5cbnN3aXRjaCAoTnVtYmVyLk5hTikge1xuICAgIGNhc2UgYTpcbiAgICAgICAgYmFyKCk7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgYjpcbiAgICAgICAgYmF6KCk7XG4gICAgICAgIGJyZWFrO1xuICAgIC8vIC4uLlxufSJ9)

```
/*eslint use-isnan: ["error", {"enforceForSwitchCase": true}]*/

switch (foo) {
    case NaN:
        bar();
        break;
    case 1:
        baz();
        break;
    // ...
}

switch (NaN) {
    case a:
        bar();
        break;
    case b:
        baz();
        break;
    // ...
}

switch (foo) {
    case Number.NaN:
        bar();
        break;
    case 1:
        baz();
        break;
    // ...
}

switch (Number.NaN) {
    case a:
        bar();
        break;
    case b:
        baz();
        break;
    // ...
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
```

Examples of correct code for this rule with `"enforceForSwitchCase"` option set to `true` (default):

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9yU3dpdGNoQ2FzZVwiOiB0cnVlfV0qL1xuXG5pZiAoTnVtYmVyLmlzTmFOKGZvbykpIHtcbiAgICBiYXIoKTtcbn0gZWxzZSB7XG4gICAgc3dpdGNoIChmb28pIHtcbiAgICAgICAgY2FzZSAxOlxuICAgICAgICAgICAgYmF6KCk7XG4gICAgICAgICAgICBicmVhaztcbiAgICAgICAgLy8gLi4uXG4gICAgfVxufVxuXG5pZiAoTnVtYmVyLmlzTmFOKGEpKSB7XG4gICAgYmFyKCk7XG59IGVsc2UgaWYgKE51bWJlci5pc05hTihiKSkge1xuICAgIGJheigpO1xufSAvLyAuLi4ifQ==)

```
/*eslint use-isnan: ["error", {"enforceForSwitchCase": true}]*/

if (Number.isNaN(foo)) {
    bar();
} else {
    switch (foo) {
        case 1:
            baz();
            break;
        // ...
    }
}

if (Number.isNaN(a)) {
    bar();
} else if (Number.isNaN(b)) {
    baz();
} // ...
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
```

Examples of correct code for this rule with `"enforceForSwitchCase"` option set to `false`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9yU3dpdGNoQ2FzZVwiOiBmYWxzZX1dKi9cblxuc3dpdGNoIChmb28pIHtcbiAgICBjYXNlIE5hTjpcbiAgICAgICAgYmFyKCk7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgMTpcbiAgICAgICAgYmF6KCk7XG4gICAgICAgIGJyZWFrO1xuICAgIC8vIC4uLlxufVxuXG5zd2l0Y2ggKE5hTikge1xuICAgIGNhc2UgYTpcbiAgICAgICAgYmFyKCk7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgYjpcbiAgICAgICAgYmF6KCk7XG4gICAgICAgIGJyZWFrO1xuICAgIC8vIC4uLlxufVxuXG5zd2l0Y2ggKGZvbykge1xuICAgIGNhc2UgTnVtYmVyLk5hTjpcbiAgICAgICAgYmFyKCk7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgMTpcbiAgICAgICAgYmF6KCk7XG4gICAgICAgIGJyZWFrO1xuICAgIC8vIC4uLlxufVxuXG5zd2l0Y2ggKE51bWJlci5OYU4pIHtcbiAgICBjYXNlIGE6XG4gICAgICAgIGJhcigpO1xuICAgICAgICBicmVhaztcbiAgICBjYXNlIGI6XG4gICAgICAgIGJheigpO1xuICAgICAgICBicmVhaztcbiAgICAvLyAuLi5cbn0ifQ==)

```
/*eslint use-isnan: ["error", {"enforceForSwitchCase": false}]*/

switch (foo) {
    case NaN:
        bar();
        break;
    case 1:
        baz();
        break;
    // ...
}

switch (NaN) {
    case a:
        bar();
        break;
    case b:
        baz();
        break;
    // ...
}

switch (foo) {
    case Number.NaN:
        bar();
        break;
    case 1:
        baz();
        break;
    // ...
}

switch (Number.NaN) {
    case a:
        bar();
        break;
    case b:
        baz();
        break;
    // ...
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
```

### enforceForIndexOf

The following methods internally use the `===` comparison to match the given value with an array element:

- [Array.prototype.indexOf](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.indexof)
- [Array.prototype.lastIndexOf](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.lastindexof)

Therefore, for any array `foo`, `foo.indexOf(NaN)` and `foo.lastIndexOf(NaN)` will always return `-1`.

Set `"enforceForIndexOf"` to `true` if you want this rule to report `indexOf(NaN)` and `lastIndexOf(NaN)` method calls.

Examples of incorrect code for this rule with `"enforceForIndexOf"` option set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9ySW5kZXhPZlwiOiB0cnVlfV0qL1xuXG5jb25zdCBoYXNOYU4gPSBteUFycmF5LmluZGV4T2YoTmFOKSA+PSAwO1xuXG5jb25zdCBmaXJzdEluZGV4ID0gbXlBcnJheS5pbmRleE9mKE5hTik7XG5cbmNvbnN0IGxhc3RJbmRleCA9IG15QXJyYXkubGFzdEluZGV4T2YoTmFOKTtcblxuY29uc3QgaW5kZXhXaXRoU2VxdWVuY2VFeHByZXNzaW9uID0gbXlBcnJheS5pbmRleE9mKChkb1N0dWZmKCksIE5hTikpO1xuXG5jb25zdCBmaXJzdEluZGV4RnJvbVNlY29uZEVsZW1lbnQgPSBteUFycmF5LmluZGV4T2YoTmFOLCAxKTtcblxuY29uc3QgbGFzdEluZGV4RnJvbVNlY29uZEVsZW1lbnQgPSBteUFycmF5Lmxhc3RJbmRleE9mKE5hTiwgMSk7In0=)

```
/*eslint use-isnan: ["error", {"enforceForIndexOf": true}]*/

const hasNaN = myArray.indexOf(NaN) >= 0;

const firstIndex = myArray.indexOf(NaN);

const lastIndex = myArray.lastIndexOf(NaN);

const indexWithSequenceExpression = myArray.indexOf((doStuff(), NaN));

const firstIndexFromSecondElement = myArray.indexOf(NaN, 1);

const lastIndexFromSecondElement = myArray.lastIndexOf(NaN, 1);
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

Examples of correct code for this rule with `"enforceForIndexOf"` option set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdXNlLWlzbmFuOiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9ySW5kZXhPZlwiOiB0cnVlfV0qL1xuXG5mdW5jdGlvbiBteUlzTmFOKHZhbCkge1xuICAgIHJldHVybiB0eXBlb2YgdmFsID09PSBcIm51bWJlclwiICYmIGlzTmFOKHZhbCk7XG59XG5cbmZ1bmN0aW9uIGluZGV4T2ZOYU4oYXJyKSB7XG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBhcnIubGVuZ3RoOyBpKyspIHtcbiAgICAgICAgaWYgKG15SXNOYU4oYXJyW2ldKSkge1xuICAgICAgICAgICAgcmV0dXJuIGk7XG4gICAgICAgIH1cbiAgICB9XG4gICAgcmV0dXJuIC0xO1xufVxuXG5mdW5jdGlvbiBsYXN0SW5kZXhPZk5hTihhcnIpIHtcbiAgICBmb3IgKGxldCBpID0gYXJyLmxlbmd0aCAtIDE7IGkgPj0gMDsgaS0tKSB7XG4gICAgICAgIGlmIChteUlzTmFOKGFycltpXSkpIHtcbiAgICAgICAgICAgIHJldHVybiBpO1xuICAgICAgICB9XG4gICAgfVxuICAgIHJldHVybiAtMTtcbn1cblxuY29uc3QgaGFzTmFOID0gbXlBcnJheS5zb21lKG15SXNOYU4pO1xuXG5jb25zdCBoYXNOYU4xID0gaW5kZXhPZk5hTihteUFycmF5KSA+PSAwO1xuXG5jb25zdCBmaXJzdEluZGV4ID0gaW5kZXhPZk5hTihteUFycmF5KTtcblxuY29uc3QgbGFzdEluZGV4ID0gbGFzdEluZGV4T2ZOYU4obXlBcnJheSk7XG5cbi8vIEVTMjAxNVxuY29uc3QgaGFzTmFOMiA9IG15QXJyYXkuc29tZShOdW1iZXIuaXNOYU4pO1xuXG4vLyBFUzIwMTVcbmNvbnN0IGZpcnN0SW5kZXgxID0gbXlBcnJheS5maW5kSW5kZXgoTnVtYmVyLmlzTmFOKTtcblxuLy8gRVMyMDE2XG5jb25zdCBoYXNOYU4zID0gbXlBcnJheS5pbmNsdWRlcyhOYU4pOyJ9)

```
/*eslint use-isnan: ["error", {"enforceForIndexOf": true}]*/

function myIsNaN(val) {
    return typeof val === "number" && isNaN(val);
}

function indexOfNaN(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (myIsNaN(arr[i])) {
            return i;
        }
    }
    return -1;
}

function lastIndexOfNaN(arr) {
    for (let i = arr.length - 1; i >= 0; i--) {
        if (myIsNaN(arr[i])) {
            return i;
        }
    }
    return -1;
}

const hasNaN = myArray.some(myIsNaN);

const hasNaN1 = indexOfNaN(myArray) >= 0;

const firstIndex = indexOfNaN(myArray);

const lastIndex = lastIndexOfNaN(myArray);

// ES2015
const hasNaN2 = myArray.some(Number.isNaN);

// ES2015
const firstIndex1 = myArray.findIndex(Number.isNaN);

// ES2016
const hasNaN3 = myArray.includes(NaN);
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

#### Known Limitations

This option checks methods with the given names, even if the object which has the method is not an array.

## Version

This rule was introduced in ESLint v0.0.6.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/use-isnan.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/use-isnan.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/use-isnan.md
                    
                
                )
