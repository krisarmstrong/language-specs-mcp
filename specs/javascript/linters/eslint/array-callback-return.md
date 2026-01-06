# array-callback-return

Enforce `return` statements in callbacks of array methods

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowImplicit](#allowimplicit)
  2. [checkForEach](#checkforeach)
  3. [allowVoid](#allowvoid)

3. [Known Limitations](#known-limitations)
4. [When Not To Use It](#when-not-to-use-it)
5. [Version](#version)
6. [Resources](#resources)

`Array` has several methods for filtering, mapping, and folding. If we forget to write `return` statement in a callback of those, it’s probably a mistake. If you don’t want to use a return or don’t need the returned results, consider using [.forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) instead.

```
// example: convert ['a', 'b', 'c'] --> {a: 0, b: 1, c: 2}
const indexMap = myArray.reduce(function(memo, item, index) {
  memo[item] = index;
}, {}); // Error: cannot set property 'b' of undefined
1
2
3
4
```

Copy code to clipboard

## Rule Details

This rule enforces usage of `return` statement in callbacks of array’s methods. Additionally, it may also enforce the `forEach` array method callback to not return a value by using the `checkForEach` option.

This rule finds callback functions of the following methods, then checks usage of `return` statement.

- [Array.from](https://www.ecma-international.org/ecma-262/6.0/#sec-array.from)
- [Array.prototype.every](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.every)
- [Array.prototype.filter](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.filter)
- [Array.prototype.find](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.find)
- [Array.prototype.findIndex](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.findindex)
- [Array.prototype.findLast](https://tc39.es/ecma262/#sec-array.prototype.findlast)
- [Array.prototype.findLastIndex](https://tc39.es/ecma262/#sec-array.prototype.findlastindex)
- [Array.prototype.flatMap](https://www.ecma-international.org/ecma-262/10.0/#sec-array.prototype.flatmap)
- [Array.prototype.forEach](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.foreach) (optional, based on `checkForEach` parameter)
- [Array.prototype.map](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.map)
- [Array.prototype.reduce](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.reduce)
- [Array.prototype.reduceRight](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.reduceright)
- [Array.prototype.some](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.some)
- [Array.prototype.sort](https://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.sort)
- [Array.prototype.toSorted](https://tc39.es/ecma262/#sec-array.prototype.tosorted)
- And above of typed arrays.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyYXktY2FsbGJhY2stcmV0dXJuOiBcImVycm9yXCIqL1xuXG5jb25zdCBpbmRleE1hcCA9IG15QXJyYXkucmVkdWNlKGZ1bmN0aW9uKG1lbW8sIGl0ZW0sIGluZGV4KSB7XG4gICAgbWVtb1tpdGVtXSA9IGluZGV4O1xufSwge30pO1xuXG5jb25zdCBmb28gPSBBcnJheS5mcm9tKG5vZGVzLCBmdW5jdGlvbihub2RlKSB7XG4gICAgaWYgKG5vZGUudGFnTmFtZSA9PT0gXCJESVZcIikge1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG59KTtcblxuY29uc3QgYmFyID0gZm9vLmZpbHRlcihmdW5jdGlvbih4KSB7XG4gICAgaWYgKHgpIHtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgcmV0dXJuO1xuICAgIH1cbn0pOyJ9)

```
/*eslint array-callback-return: "error"*/

const indexMap = myArray.reduce(function(memo, item, index) {
    memo[item] = index;
}, {});

const foo = Array.from(nodes, function(node) {
    if (node.tagName === "DIV") {
        return true;
    }
});

const bar = foo.filter(function(x) {
    if (x) {
        return true;
    } else {
        return;
    }
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
17
18
19
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyYXktY2FsbGJhY2stcmV0dXJuOiBcImVycm9yXCIqL1xuXG5jb25zdCBpbmRleE1hcCA9IG15QXJyYXkucmVkdWNlKGZ1bmN0aW9uKG1lbW8sIGl0ZW0sIGluZGV4KSB7XG4gICAgbWVtb1tpdGVtXSA9IGluZGV4O1xuICAgIHJldHVybiBtZW1vO1xufSwge30pO1xuXG5jb25zdCBmb28gPSBBcnJheS5mcm9tKG5vZGVzLCBmdW5jdGlvbihub2RlKSB7XG4gICAgaWYgKG5vZGUudGFnTmFtZSA9PT0gXCJESVZcIikge1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG4gICAgcmV0dXJuIGZhbHNlO1xufSk7XG5cbmNvbnN0IGJhciA9IGZvby5tYXAobm9kZSA9PiBub2RlLmdldEF0dHJpYnV0ZShcImlkXCIpKTsifQ==)

```
/*eslint array-callback-return: "error"*/

const indexMap = myArray.reduce(function(memo, item, index) {
    memo[item] = index;
    return memo;
}, {});

const foo = Array.from(nodes, function(node) {
    if (node.tagName === "DIV") {
        return true;
    }
    return false;
});

const bar = foo.map(node => node.getAttribute("id"));
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

## Options

This rule accepts a configuration object with three options:

- `"allowImplicit": false` (default) When set to `true`, allows callbacks of methods that require a return value to implicitly return `undefined` with a `return` statement containing no expression.
- `"checkForEach": false` (default) When set to `true`, rule will also report `forEach` callbacks that return a value.
- `"allowVoid": false` (default) When set to `true`, allows `void` in `forEach` callbacks, so rule will not report the return value with a `void` operator.

Note:`{ "allowVoid": true }` works only if `checkForEach` option is set to `true`.

### allowImplicit

Examples of correct code for the `{ "allowImplicit": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyYXktY2FsbGJhY2stcmV0dXJuOiBbXCJlcnJvclwiLCB7IGFsbG93SW1wbGljaXQ6IHRydWUgfV0qL1xuY29uc3QgdW5kZWZBbGxUaGVUaGluZ3MgPSBteUFycmF5Lm1hcChmdW5jdGlvbihpdGVtKSB7XG4gICAgcmV0dXJuO1xufSk7In0=)

```
/*eslint array-callback-return: ["error", { allowImplicit: true }]*/
const undefAllTheThings = myArray.map(function(item) {
    return;
});
1
2
3
4
```

### checkForEach

Examples of incorrect code for the `{ "checkForEach": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyYXktY2FsbGJhY2stcmV0dXJuOiBbXCJlcnJvclwiLCB7IGNoZWNrRm9yRWFjaDogdHJ1ZSB9XSovXG5cbm15QXJyYXkuZm9yRWFjaChmdW5jdGlvbihpdGVtKSB7XG4gICAgcmV0dXJuIGhhbmRsZUl0ZW0oaXRlbSk7XG59KTtcblxubXlBcnJheS5mb3JFYWNoKGZ1bmN0aW9uKGl0ZW0pIHtcbiAgICBpZiAoaXRlbSA8IDApIHtcbiAgICAgICAgcmV0dXJuIHg7XG4gICAgfVxuICAgIGhhbmRsZUl0ZW0oaXRlbSk7XG59KTtcblxubXlBcnJheS5mb3JFYWNoKGZ1bmN0aW9uKGl0ZW0pIHtcbiAgICBpZiAoaXRlbSA8IDApIHtcbiAgICAgICAgcmV0dXJuIHZvaWQgeDtcbiAgICB9XG4gICAgaGFuZGxlSXRlbShpdGVtKTtcbn0pO1xuXG5teUFycmF5LmZvckVhY2goaXRlbSA9PiBoYW5kbGVJdGVtKGl0ZW0pKTtcblxubXlBcnJheS5mb3JFYWNoKGl0ZW0gPT4gdm9pZCBoYW5kbGVJdGVtKGl0ZW0pKTtcblxubXlBcnJheS5mb3JFYWNoKGl0ZW0gPT4ge1xuICAgIHJldHVybiBoYW5kbGVJdGVtKGl0ZW0pO1xufSk7XG5cbm15QXJyYXkuZm9yRWFjaChpdGVtID0+IHtcbiAgICByZXR1cm4gdm9pZCBoYW5kbGVJdGVtKGl0ZW0pO1xufSk7In0=)

```
/*eslint array-callback-return: ["error", { checkForEach: true }]*/

myArray.forEach(function(item) {
    return handleItem(item);
});

myArray.forEach(function(item) {
    if (item < 0) {
        return x;
    }
    handleItem(item);
});

myArray.forEach(function(item) {
    if (item < 0) {
        return void x;
    }
    handleItem(item);
});

myArray.forEach(item => handleItem(item));

myArray.forEach(item => void handleItem(item));

myArray.forEach(item => {
    return handleItem(item);
});

myArray.forEach(item => {
    return void handleItem(item);
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

Examples of correct code for the `{ "checkForEach": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyYXktY2FsbGJhY2stcmV0dXJuOiBbXCJlcnJvclwiLCB7IGNoZWNrRm9yRWFjaDogdHJ1ZSB9XSovXG5cbm15QXJyYXkuZm9yRWFjaChmdW5jdGlvbihpdGVtKSB7XG4gICAgaGFuZGxlSXRlbShpdGVtKVxufSk7XG5cbm15QXJyYXkuZm9yRWFjaChmdW5jdGlvbihpdGVtKSB7XG4gICAgaWYgKGl0ZW0gPCAwKSB7XG4gICAgICAgIHJldHVybjtcbiAgICB9XG4gICAgaGFuZGxlSXRlbShpdGVtKTtcbn0pO1xuXG5teUFycmF5LmZvckVhY2goZnVuY3Rpb24oaXRlbSkge1xuICAgIGhhbmRsZUl0ZW0oaXRlbSk7XG4gICAgcmV0dXJuO1xufSk7XG5cbm15QXJyYXkuZm9yRWFjaChpdGVtID0+IHtcbiAgICBoYW5kbGVJdGVtKGl0ZW0pO1xufSk7In0=)

```
/*eslint array-callback-return: ["error", { checkForEach: true }]*/

myArray.forEach(function(item) {
    handleItem(item)
});

myArray.forEach(function(item) {
    if (item < 0) {
        return;
    }
    handleItem(item);
});

myArray.forEach(function(item) {
    handleItem(item);
    return;
});

myArray.forEach(item => {
    handleItem(item);
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
17
18
19
20
21
```

### allowVoid

Examples of correct code for the `{ "allowVoid": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyYXktY2FsbGJhY2stcmV0dXJuOiBbXCJlcnJvclwiLCB7IGNoZWNrRm9yRWFjaDogdHJ1ZSwgYWxsb3dWb2lkOiB0cnVlIH1dKi9cblxubXlBcnJheS5mb3JFYWNoKGl0ZW0gPT4gdm9pZCBoYW5kbGVJdGVtKGl0ZW0pKTtcblxubXlBcnJheS5mb3JFYWNoKGl0ZW0gPT4ge1xuICAgIHJldHVybiB2b2lkIGhhbmRsZUl0ZW0oaXRlbSk7XG59KTtcblxubXlBcnJheS5mb3JFYWNoKGl0ZW0gPT4ge1xuICAgIGlmIChpdGVtIDwgMCkge1xuICAgICAgICByZXR1cm4gdm9pZCB4O1xuICAgIH1cbiAgICBoYW5kbGVJdGVtKGl0ZW0pO1xufSk7In0=)

```
/*eslint array-callback-return: ["error", { checkForEach: true, allowVoid: true }]*/

myArray.forEach(item => void handleItem(item));

myArray.forEach(item => {
    return void handleItem(item);
});

myArray.forEach(item => {
    if (item < 0) {
        return void x;
    }
    handleItem(item);
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
```

## Known Limitations

This rule checks callback functions of methods with the given names, even if the object which has the method is not an array.

## When Not To Use It

If you don’t want to warn about usage of `return` statement in callbacks of array’s methods, then it’s safe to disable this rule.

## Version

This rule was introduced in ESLint v2.0.0-alpha-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/array-callback-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/array-callback-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/array-callback-return.md
                    
                
                )
