# prefer-const

Require `const` declarations for variables that are never reassigned after declared

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [destructuring](#destructuring)
  2. [ignoreReadBeforeAssign](#ignorereadbeforeassign)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

If a variable is never reassigned, using the `const` declaration is better.

`const` declaration tells readers, “this variable is never reassigned,” reducing cognitive load and improving maintainability.

## Rule Details

This rule is aimed at flagging variables that are declared using `let` keyword, but never reassigned after the initial assignment.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBcImVycm9yXCIqL1xuXG4vLyBpdCdzIGluaXRpYWxpemVkIGFuZCBuZXZlciByZWFzc2lnbmVkLlxubGV0IGEgPSAzO1xuY29uc29sZS5sb2coYSk7XG5cbmxldCBiO1xuYiA9IDA7XG5jb25zb2xlLmxvZyhiKTtcblxuY2xhc3MgQyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgbGV0IGE7XG4gICAgICAgIGEgPSAwO1xuICAgICAgICBjb25zb2xlLmxvZyhhKTtcbiAgICB9XG59XG5cbi8vIGBpYCBpcyByZWRlZmluZWQgKG5vdCByZWFzc2lnbmVkKSBvbiBlYWNoIGxvb3Agc3RlcC5cbmZvciAobGV0IGkgaW4gWzEsIDIsIDNdKSB7XG4gICAgY29uc29sZS5sb2coaSk7XG59XG5cbi8vIGBhYCBpcyByZWRlZmluZWQgKG5vdCByZWFzc2lnbmVkKSBvbiBlYWNoIGxvb3Agc3RlcC5cbmZvciAobGV0IGEgb2YgWzEsIDIsIDNdKSB7XG4gICAgY29uc29sZS5sb2coYSk7XG59In0=)

```
/*eslint prefer-const: "error"*/

// it's initialized and never reassigned.
let a = 3;
console.log(a);

let b;
b = 0;
console.log(b);

class C {
    static {
        let a;
        a = 0;
        console.log(a);
    }
}

// `i` is redefined (not reassigned) on each loop step.
for (let i in [1, 2, 3]) {
    console.log(i);
}

// `a` is redefined (not reassigned) on each loop step.
for (let a of [1, 2, 3]) {
    console.log(a);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBcImVycm9yXCIqL1xuXG4vLyB1c2luZyBjb25zdC5cbmNvbnN0IGEgPSAwO1xuXG4vLyBpdCdzIG5ldmVyIGluaXRpYWxpemVkLlxubGV0IGI7XG5jb25zb2xlLmxvZyhiKTtcblxuLy8gaXQncyByZWFzc2lnbmVkIGFmdGVyIGluaXRpYWxpemVkLlxubGV0IGM7XG5jID0gMDtcbmMgPSAxO1xuY29uc29sZS5sb2coYyk7XG5cbi8vIGl0J3MgaW5pdGlhbGl6ZWQgaW4gYSBkaWZmZXJlbnQgYmxvY2sgZnJvbSB0aGUgZGVjbGFyYXRpb24uXG5sZXQgZDtcbmlmICh0cnVlKSB7XG4gICAgZCA9IDA7XG59XG5jb25zb2xlLmxvZyhkKTtcblxuLy8gaXQncyBpbml0aWFsaXplZCBpbiBhIGRpZmZlcmVudCBzY29wZS5cbmxldCBlO1xuY2xhc3MgQyB7XG4gICAgI3g7XG4gICAgc3RhdGljIHtcbiAgICAgICAgZSA9IG9iaiA9PiBvYmouI3g7XG4gICAgfVxufVxuXG4vLyBpdCdzIGluaXRpYWxpemVkIGF0IGEgcGxhY2UgdGhhdCB3ZSBjYW5ub3Qgd3JpdGUgYSB2YXJpYWJsZSBkZWNsYXJhdGlvbi5cbmxldCBmO1xuaWYgKHRydWUpIGYgPSAwO1xuY29uc29sZS5sb2coZik7XG5cbi8vIGBpYCBnZXRzIGEgbmV3IGJpbmRpbmcgZWFjaCBpdGVyYXRpb25cbmZvciAoY29uc3QgaSBpbiBbMSwgMiwgM10pIHtcbiAgY29uc29sZS5sb2coaSk7XG59XG5cbi8vIGBhYCBnZXRzIGEgbmV3IGJpbmRpbmcgZWFjaCBpdGVyYXRpb25cbmZvciAoY29uc3QgYSBvZiBbMSwgMiwgM10pIHtcbiAgY29uc29sZS5sb2coYSk7XG59XG5cbi8vIGBlbmRgIGlzIG5ldmVyIHJlYXNzaWduZWQsIGJ1dCB3ZSBjYW5ub3Qgc2VwYXJhdGUgdGhlIGRlY2xhcmF0aW9ucyB3aXRob3V0IG1vZGlmeWluZyB0aGUgc2NvcGUuXG5mb3IgKGxldCBpID0gMCwgZW5kID0gMTA7IGkgPCBlbmQ7ICsraSkge1xuICAgIGNvbnNvbGUubG9nKGkpO1xufVxuXG4vLyBgcHJlZGljYXRlYCBpcyBvbmx5IGFzc2lnbmVkIG9uY2UgYnV0IGNhbm5vdCBiZSBzZXBhcmF0ZWx5IGRlY2xhcmVkIGFzIGBjb25zdGBcbmxldCBwcmVkaWNhdGU7XG5bb2JqZWN0LnR5cGUsIHByZWRpY2F0ZV0gPSBmb28oKTtcblxuLy8gYGdgIGlzIG9ubHkgYXNzaWduZWQgb25jZSBidXQgY2Fubm90IGJlIHNlcGFyYXRlbHkgZGVjbGFyZWQgYXMgYGNvbnN0YFxubGV0IGc7XG5jb25zdCBoID0ge307XG4oeyBnLCBjOiBoLmMgfSA9IGZ1bmMoKSk7XG5cbi8vIHN1Z2dlc3QgdG8gdXNlIGBuby12YXJgIHJ1bGUuXG52YXIgaSA9IDM7XG5jb25zb2xlLmxvZyhpKTsifQ==)

```
/*eslint prefer-const: "error"*/

// using const.
const a = 0;

// it's never initialized.
let b;
console.log(b);

// it's reassigned after initialized.
let c;
c = 0;
c = 1;
console.log(c);

// it's initialized in a different block from the declaration.
let d;
if (true) {
    d = 0;
}
console.log(d);

// it's initialized in a different scope.
let e;
class C {
    #x;
    static {
        e = obj => obj.#x;
    }
}

// it's initialized at a place that we cannot write a variable declaration.
let f;
if (true) f = 0;
console.log(f);

// `i` gets a new binding each iteration
for (const i in [1, 2, 3]) {
  console.log(i);
}

// `a` gets a new binding each iteration
for (const a of [1, 2, 3]) {
  console.log(a);
}

// `end` is never reassigned, but we cannot separate the declarations without modifying the scope.
for (let i = 0, end = 10; i < end; ++i) {
    console.log(i);
}

// `predicate` is only assigned once but cannot be separately declared as `const`
let predicate;
[object.type, predicate] = foo();

// `g` is only assigned once but cannot be separately declared as `const`
let g;
const h = {};
({ g, c: h.c } = func());

// suggest to use `no-var` rule.
var i = 3;
console.log(i);
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
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
```

## Options

```
{
    "prefer-const": ["error", {
        "destructuring": "any",
        "ignoreReadBeforeAssign": false
    }]
}
1
2
3
4
5
6
```

Copy code to clipboard

### destructuring

The kind of the way to address variables in destructuring. There are 2 values:

- `"any"` (default) - If any variables in destructuring should be `const`, this rule warns for those variables.
- `"all"` - If all variables in destructuring should be `const`, this rule warns the variables. Otherwise, ignores them.

Examples of incorrect code for the default `{"destructuring": "any"}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBcImVycm9yXCIqL1xuXG5sZXQge2EsIGJ9ID0gb2JqOyAgICAvKmVycm9yICdiJyBpcyBuZXZlciByZWFzc2lnbmVkLCB1c2UgJ2NvbnN0JyBpbnN0ZWFkLiovXG5hID0gYSArIDE7In0=)

```
/*eslint prefer-const: "error"*/

let {a, b} = obj;    /*error 'b' is never reassigned, use 'const' instead.*/
a = a + 1;
1
2
3
4
```

Examples of correct code for the default `{"destructuring": "any"}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBcImVycm9yXCIqL1xuXG4vLyB1c2luZyBjb25zdC5cbmNvbnN0IHthOiBhMCwgYn0gPSBvYmo7XG5jb25zdCBhID0gYTAgKyAxO1xuXG4vLyBhbGwgdmFyaWFibGVzIGFyZSByZWFzc2lnbmVkLlxubGV0IHtjLCBkfSA9IG9iajtcbmMgPSBjICsgMTtcbmQgPSBkICsgMTsifQ==)

```
/*eslint prefer-const: "error"*/

// using const.
const {a: a0, b} = obj;
const a = a0 + 1;

// all variables are reassigned.
let {c, d} = obj;
c = c + 1;
d = d + 1;
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

Examples of incorrect code for the `{"destructuring": "all"}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBbXCJlcnJvclwiLCB7XCJkZXN0cnVjdHVyaW5nXCI6IFwiYWxsXCJ9XSovXG5cbi8vIGFsbCBvZiBgYWAgYW5kIGBiYCBzaG91bGQgYmUgY29uc3QsIHNvIHRob3NlIGFyZSB3YXJuZWQuXG5sZXQge2EsIGJ9ID0gb2JqOyAgICAvKmVycm9yICdhJyBpcyBuZXZlciByZWFzc2lnbmVkLCB1c2UgJ2NvbnN0JyBpbnN0ZWFkLlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnYicgaXMgbmV2ZXIgcmVhc3NpZ25lZCwgdXNlICdjb25zdCcgaW5zdGVhZC4qLyJ9)

```
/*eslint prefer-const: ["error", {"destructuring": "all"}]*/

// all of `a` and `b` should be const, so those are warned.
let {a, b} = obj;    /*error 'a' is never reassigned, use 'const' instead.
                             'b' is never reassigned, use 'const' instead.*/
1
2
3
4
5
```

Examples of correct code for the `{"destructuring": "all"}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBbXCJlcnJvclwiLCB7XCJkZXN0cnVjdHVyaW5nXCI6IFwiYWxsXCJ9XSovXG5cbi8vICdiJyBpcyBuZXZlciByZWFzc2lnbmVkLCBidXQgYWxsIG9mIGBhYCBhbmQgYGJgIHNob3VsZCBub3QgYmUgY29uc3QsIHNvIHRob3NlIGFyZSBpZ25vcmVkLlxubGV0IHthLCBifSA9IG9iajtcbmEgPSBhICsgMTsifQ==)

```
/*eslint prefer-const: ["error", {"destructuring": "all"}]*/

// 'b' is never reassigned, but all of `a` and `b` should not be const, so those are ignored.
let {a, b} = obj;
a = a + 1;
1
2
3
4
5
```

### ignoreReadBeforeAssign

This is an option to avoid conflicting with `no-use-before-define` rule (without `"nofunc"` option). If `true` is specified, this rule will ignore variables that are read between the declaration and the first assignment. Default is `false`.

Examples of correct code for the `{"ignoreReadBeforeAssign": true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBbXCJlcnJvclwiLCB7XCJpZ25vcmVSZWFkQmVmb3JlQXNzaWduXCI6IHRydWV9XSovXG5cbmxldCB0aW1lcjtcbmZ1bmN0aW9uIGluaXRpYWxpemUoKSB7XG4gICAgaWYgKGZvbygpKSB7XG4gICAgICAgIGNsZWFySW50ZXJ2YWwodGltZXIpO1xuICAgIH1cbn1cbnRpbWVyID0gc2V0SW50ZXJ2YWwoaW5pdGlhbGl6ZSwgMTAwKTsifQ==)

```
/*eslint prefer-const: ["error", {"ignoreReadBeforeAssign": true}]*/

let timer;
function initialize() {
    if (foo()) {
        clearInterval(timer);
    }
}
timer = setInterval(initialize, 100);
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

Examples of correct code for the default `{"ignoreReadBeforeAssign": false}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLWNvbnN0OiBbXCJlcnJvclwiLCB7XCJpZ25vcmVSZWFkQmVmb3JlQXNzaWduXCI6IGZhbHNlfV0qL1xuXG5jb25zdCB0aW1lciA9IHNldEludGVydmFsKGluaXRpYWxpemUsIDEwMCk7XG5mdW5jdGlvbiBpbml0aWFsaXplKCkge1xuICAgIGlmIChmb28oKSkge1xuICAgICAgICBjbGVhckludGVydmFsKHRpbWVyKTtcbiAgICB9XG59In0=)

```
/*eslint prefer-const: ["error", {"ignoreReadBeforeAssign": false}]*/

const timer = setInterval(initialize, 100);
function initialize() {
    if (foo()) {
        clearInterval(timer);
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
```

## When Not To Use It

If you don’t want to be notified about variables that are never reassigned after initial assignment, you can safely disable this rule.

## Related Rules

- [no-var](/docs/latest/rules/no-var)
- [no-unassigned-vars](/docs/latest/rules/no-unassigned-vars)
- [no-use-before-define](/docs/latest/rules/no-use-before-define)

## Version

This rule was introduced in ESLint v0.23.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-const.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-const.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-const.md
                    
                
                )
