# no-unmodified-loop-condition

Disallow unmodified loop conditions

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

Variables in a loop condition often are modified in the loop. If not, it’s possibly a mistake.

```
while (node) {
    doSomething(node);
}
1
2
3
```

Copy code to clipboard

```
while (node) {
    doSomething(node);
    node = node.parent;
}
1
2
3
4
```

Copy code to clipboard

## Rule Details

This rule finds references which are inside of loop conditions, then checks the variables of those references are modified in the loop.

If a reference is inside of a binary expression or a ternary expression, this rule checks the result of the expression instead. If a reference is inside of a dynamic expression (e.g. `CallExpression`, `YieldExpression`, …), this rule ignores it.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5tb2RpZmllZC1sb29wLWNvbmRpdGlvbjogXCJlcnJvclwiKi9cblxubGV0IG5vZGUgPSBzb21ldGhpbmc7XG5cbndoaWxlIChub2RlKSB7XG4gICAgZG9Tb21ldGhpbmcobm9kZSk7XG59XG5ub2RlID0gb3RoZXI7XG5cbmZvciAobGV0IGogPSAwOyBqIDwgNTspIHtcbiAgICBkb1NvbWV0aGluZyhqKTtcbn1cblxud2hpbGUgKG5vZGUgIT09IHJvb3QpIHtcbiAgICBkb1NvbWV0aGluZyhub2RlKTtcbn0ifQ==)

```
/*eslint no-unmodified-loop-condition: "error"*/

let node = something;

while (node) {
    doSomething(node);
}
node = other;

for (let j = 0; j < 5;) {
    doSomething(j);
}

while (node !== root) {
    doSomething(node);
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5tb2RpZmllZC1sb29wLWNvbmRpdGlvbjogXCJlcnJvclwiKi9cblxud2hpbGUgKG5vZGUpIHtcbiAgICBkb1NvbWV0aGluZyhub2RlKTtcbiAgICBub2RlID0gbm9kZS5wYXJlbnQ7XG59XG5cbmZvciAobGV0IGogPSAwOyBqIDwgaXRlbXMubGVuZ3RoOyArK2opIHtcbiAgICBkb1NvbWV0aGluZyhpdGVtc1tqXSk7XG59XG5cbi8vIE9LLCB0aGUgcmVzdWx0IG9mIHRoaXMgYmluYXJ5IGV4cHJlc3Npb24gaXMgY2hhbmdlZCBpbiB0aGlzIGxvb3AuXG53aGlsZSAobm9kZSAhPT0gcm9vdCkge1xuICAgIGRvU29tZXRoaW5nKG5vZGUpO1xuICAgIG5vZGUgPSBub2RlLnBhcmVudDtcbn1cblxuLy8gT0ssIHRoZSByZXN1bHQgb2YgdGhpcyB0ZXJuYXJ5IGV4cHJlc3Npb24gaXMgY2hhbmdlZCBpbiB0aGlzIGxvb3AuXG53aGlsZSAobm9kZSA/IEEgOiBCKSB7XG4gICAgZG9Tb21ldGhpbmcobm9kZSk7XG4gICAgbm9kZSA9IG5vZGUucGFyZW50O1xufVxuXG4vLyBBIHByb3BlcnR5IG1pZ2h0IGJlIGEgZ2V0dGVyIHdoaWNoIGhhcyBzaWRlIGVmZmVjdC4uLlxuLy8gT3IgXCJkb1NvbWV0aGluZ1wiIGNhbiBtb2RpZnkgXCJvYmouZm9vXCIuXG53aGlsZSAob2JqLmZvbykge1xuICAgIGRvU29tZXRoaW5nKG9iaik7XG59XG5cbi8vIEEgZnVuY3Rpb24gY2FsbCBjYW4gcmV0dXJuIHZhcmlvdXMgdmFsdWVzLlxud2hpbGUgKGNoZWNrKG9iaikpIHtcbiAgICBkb1NvbWV0aGluZyhvYmopO1xufSJ9)

```
/*eslint no-unmodified-loop-condition: "error"*/

while (node) {
    doSomething(node);
    node = node.parent;
}

for (let j = 0; j < items.length; ++j) {
    doSomething(items[j]);
}

// OK, the result of this binary expression is changed in this loop.
while (node !== root) {
    doSomething(node);
    node = node.parent;
}

// OK, the result of this ternary expression is changed in this loop.
while (node ? A : B) {
    doSomething(node);
    node = node.parent;
}

// A property might be a getter which has side effect...
// Or "doSomething" can modify "obj.foo".
while (obj.foo) {
    doSomething(obj);
}

// A function call can return various values.
while (check(obj)) {
    doSomething(obj);
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
```

## When Not To Use It

If you don’t want to notified about references inside of loop conditions, then it’s safe to disable this rule.

## Version

This rule was introduced in ESLint v2.0.0-alpha-2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unmodified-loop-condition.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unmodified-loop-condition.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unmodified-loop-condition.md
                    
                
                )
