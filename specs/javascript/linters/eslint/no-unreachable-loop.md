# no-unreachable-loop

Disallow loops with a body that allows only one iteration

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [ignore](#ignore)

3. [Known Limitations](#known-limitations)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

A loop that can never reach the second iteration is a possible error in the code.

```
for (let i = 0; i < arr.length; i++) {
    if (arr[i].name === myName) {
        doSomething(arr[i]);
        // break was supposed to be here
    }
    break;
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

In rare cases where only one iteration (or at most one iteration) is intended behavior, the code should be refactored to use `if` conditionals instead of `while`, `do-while` and `for` loops. It’s considered a best practice to avoid using loop constructs for such cases.

## Rule Details

This rule aims to detect and disallow loops that can have at most one iteration, by performing static code path analysis on loop bodies.

In particular, this rule will disallow a loop with a body that exits the loop in all code paths. If all code paths in the loop’s body will end with either a `break`, `return` or a `throw` statement, the second iteration of such loop is certainly unreachable, regardless of the loop’s condition.

This rule checks `while`, `do-while`, `for`, `for-in` and `for-of` loops. You can optionally disable checks for each of these constructs.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGUtbG9vcDogXCJlcnJvclwiKi9cblxud2hpbGUgKGZvbykge1xuICAgIGRvU29tZXRoaW5nKGZvbyk7XG4gICAgZm9vID0gZm9vLnBhcmVudDtcbiAgICBicmVhaztcbn1cblxuZnVuY3Rpb24gdmVyaWZ5TGlzdChoZWFkKSB7XG4gICAgbGV0IGl0ZW0gPSBoZWFkO1xuICAgIGRvIHtcbiAgICAgICAgaWYgKHZlcmlmeShpdGVtKSkge1xuICAgICAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cbiAgICB9IHdoaWxlIChpdGVtKTtcbn1cblxuZnVuY3Rpb24gZmluZFNvbWV0aGluZyhhcnIpIHtcbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IGFyci5sZW5ndGg7IGkrKykge1xuICAgICAgICBpZiAoaXNTb21ldGhpbmcoYXJyW2ldKSkge1xuICAgICAgICAgICAgcmV0dXJuIGFycltpXTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcihcIkRvZXNuJ3QgZXhpc3QuXCIpO1xuICAgICAgICB9XG4gICAgfVxufVxuXG5mb3IgKGtleSBpbiBvYmopIHtcbiAgICBpZiAoa2V5LnN0YXJ0c1dpdGgoXCJfXCIpKSB7XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgICBmaXJzdEtleSA9IGtleTtcbiAgICBmaXJzdFZhbHVlID0gb2JqW2tleV07XG4gICAgYnJlYWs7XG59XG5cbmZvciAoZm9vIG9mIGJhcikge1xuICAgIGlmIChmb28uaWQgPT09IGlkKSB7XG4gICAgICAgIGRvU29tZXRoaW5nKGZvbyk7XG4gICAgfVxuICAgIGJyZWFrO1xufSJ9)

```
/*eslint no-unreachable-loop: "error"*/

while (foo) {
    doSomething(foo);
    foo = foo.parent;
    break;
}

function verifyList(head) {
    let item = head;
    do {
        if (verify(item)) {
            return true;
        } else {
            return false;
        }
    } while (item);
}

function findSomething(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (isSomething(arr[i])) {
            return arr[i];
        } else {
            throw new Error("Doesn't exist.");
        }
    }
}

for (key in obj) {
    if (key.startsWith("_")) {
        break;
    }
    firstKey = key;
    firstValue = obj[key];
    break;
}

for (foo of bar) {
    if (foo.id === id) {
        doSomething(foo);
    }
    break;
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
42
43
44
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGUtbG9vcDogXCJlcnJvclwiKi9cblxud2hpbGUgKGZvbykge1xuICAgIGRvU29tZXRoaW5nKGZvbyk7XG4gICAgZm9vID0gZm9vLnBhcmVudDtcbn1cblxuZnVuY3Rpb24gdmVyaWZ5TGlzdChoZWFkKSB7XG4gICAgbGV0IGl0ZW0gPSBoZWFkO1xuICAgIGRvIHtcbiAgICAgICAgaWYgKHZlcmlmeShpdGVtKSkge1xuICAgICAgICAgICAgaXRlbSA9IGl0ZW0ubmV4dDtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfVxuICAgIH0gd2hpbGUgKGl0ZW0pO1xuXG4gICAgcmV0dXJuIHRydWU7XG59XG5cbmZ1bmN0aW9uIGZpbmRTb21ldGhpbmcoYXJyKSB7XG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBhcnIubGVuZ3RoOyBpKyspIHtcbiAgICAgICAgaWYgKGlzU29tZXRoaW5nKGFycltpXSkpIHtcbiAgICAgICAgICAgIHJldHVybiBhcnJbaV07XG4gICAgICAgIH1cbiAgICB9XG4gICAgdGhyb3cgbmV3IEVycm9yKFwiRG9lc24ndCBleGlzdC5cIik7XG59XG5cbmZvciAoa2V5IGluIG9iaikge1xuICAgIGlmIChrZXkuc3RhcnRzV2l0aChcIl9cIikpIHtcbiAgICAgICAgY29udGludWU7XG4gICAgfVxuICAgIGZpcnN0S2V5ID0ga2V5O1xuICAgIGZpcnN0VmFsdWUgPSBvYmpba2V5XTtcbiAgICBicmVhaztcbn1cblxuZm9yIChmb28gb2YgYmFyKSB7XG4gICAgaWYgKGZvby5pZCA9PT0gaWQpIHtcbiAgICAgICAgZG9Tb21ldGhpbmcoZm9vKTtcbiAgICAgICAgYnJlYWs7XG4gICAgfVxufSJ9)

```
/*eslint no-unreachable-loop: "error"*/

while (foo) {
    doSomething(foo);
    foo = foo.parent;
}

function verifyList(head) {
    let item = head;
    do {
        if (verify(item)) {
            item = item.next;
        } else {
            return false;
        }
    } while (item);

    return true;
}

function findSomething(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (isSomething(arr[i])) {
            return arr[i];
        }
    }
    throw new Error("Doesn't exist.");
}

for (key in obj) {
    if (key.startsWith("_")) {
        continue;
    }
    firstKey = key;
    firstValue = obj[key];
    break;
}

for (foo of bar) {
    if (foo.id === id) {
        doSomething(foo);
        break;
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
42
43
44
```

Please note that this rule is not designed to check loop conditions, and will not warn in cases such as the following examples.

Examples of additional correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGUtbG9vcDogXCJlcnJvclwiKi9cblxuZG8ge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IHdoaWxlIChmYWxzZSlcblxuZm9yIChsZXQgaSA9IDA7IGkgPCAxOyBpKyspIHtcbiAgICBkb1NvbWV0aGluZyhpKTtcbn1cblxuZm9yIChjb25zdCBhIG9mIFsxXSkge1xuICAgIGRvU29tZXRoaW5nKGEpO1xufSJ9)

```
/*eslint no-unreachable-loop: "error"*/

do {
    doSomething();
} while (false)

for (let i = 0; i < 1; i++) {
    doSomething(i);
}

for (const a of [1]) {
    doSomething(a);
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
```

## Options

This rule has an object option, with one option:

- `"ignore"` - an optional array of loop types that will be ignored by this rule.

### ignore

You can specify up to 5 different elements in the `"ignore"` array:

- `"WhileStatement"` - to ignore all `while` loops.
- `"DoWhileStatement"` - to ignore all `do-while` loops.
- `"ForStatement"` - to ignore all `for` loops (does not apply to `for-in` and `for-of` loops).
- `"ForInStatement"` - to ignore all `for-in` loops.
- `"ForOfStatement"` - to ignore all `for-of` loops.

Examples of correct code for this rule with the `"ignore"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5yZWFjaGFibGUtbG9vcDogW1wiZXJyb3JcIiwgeyBcImlnbm9yZVwiOiBbXCJGb3JJblN0YXRlbWVudFwiLCBcIkZvck9mU3RhdGVtZW50XCJdIH1dKi9cblxuZm9yIChsZXQga2V5IGluIG9iaikge1xuICBoYXNFbnVtZXJhYmxlUHJvcGVydGllcyA9IHRydWU7XG4gIGJyZWFrO1xufVxuXG5mb3IgKGNvbnN0IGEgb2YgYikgYnJlYWs7In0=)

```
/*eslint no-unreachable-loop: ["error", { "ignore": ["ForInStatement", "ForOfStatement"] }]*/

for (let key in obj) {
  hasEnumerableProperties = true;
  break;
}

for (const a of b) break;
1
2
3
4
5
6
7
8
```

## Known Limitations

Static code path analysis, in general, does not evaluate conditions. Due to this fact, this rule might miss reporting cases such as the following:

```
for (let i = 0; i < 10; i++) {
    doSomething(i);
    if (true) {
        break;
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

## Related Rules

- [no-unreachable](/docs/latest/rules/no-unreachable)
- [no-constant-condition](/docs/latest/rules/no-constant-condition)
- [no-unmodified-loop-condition](/docs/latest/rules/no-unmodified-loop-condition)
- [for-direction](/docs/latest/rules/for-direction)

## Version

This rule was introduced in ESLint v7.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unreachable-loop.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unreachable-loop.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unreachable-loop.md
                    
                
                )
