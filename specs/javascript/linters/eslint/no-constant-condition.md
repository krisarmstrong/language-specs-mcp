# no-constant-condition

Disallow constant expressions in conditions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [checkLoops](#checkloops)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

A constant expression (for example, a literal) as a test condition might be a typo or development trigger for a specific behavior. For example, the following code looks as if it is not ready for production.

```
if (false) {
    doSomethingUnfinished();
}
1
2
3
```

Copy code to clipboard

## Rule Details

This rule disallows constant expressions in the test condition of:

- `if`, `for`, `while`, or `do...while` statement
- `?:` ternary expression

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBcImVycm9yXCIqL1xuXG5pZiAoZmFsc2UpIHtcbiAgICBkb1NvbWV0aGluZ1VuZmluaXNoZWQoKTtcbn1cblxuaWYgKHZvaWQgeCkge1xuICAgIGRvU29tZXRoaW5nVW5maW5pc2hlZCgpO1xufVxuXG5pZiAoeCAmJj0gZmFsc2UpIHtcbiAgICBkb1NvbWV0aGluZ05ldmVyKCk7XG59XG5cbmlmIChjbGFzcyB7fSkge1xuICAgIGRvU29tZXRoaW5nQWx3YXlzKCk7XG59XG5cbmlmIChuZXcgQm9vbGVhbih4KSkge1xuICAgIGRvU29tZXRoaW5nQWx3YXlzKCk7XG59XG5cbmlmIChCb29sZWFuKDEpKSB7XG4gICAgZG9Tb21ldGhpbmdBbHdheXMoKTtcbn1cblxuaWYgKHVuZGVmaW5lZCkge1xuICAgIGRvU29tZXRoaW5nVW5maW5pc2hlZCgpO1xufVxuXG5pZiAoeCB8fD0gdHJ1ZSkge1xuICAgIGRvU29tZXRoaW5nQWx3YXlzKCk7XG59XG5cbmZvciAoOy0yOykge1xuICAgIGRvU29tZXRoaW5nRm9yZXZlcigpO1xufVxuXG53aGlsZSAodHlwZW9mIHgpIHtcbiAgICBkb1NvbWV0aGluZ0ZvcmV2ZXIoKTtcbn1cblxuZG8ge1xuICAgIGRvU29tZXRoaW5nRm9yZXZlcigpO1xufSB3aGlsZSAoeCA9IC0xKTtcblxuY29uc3QgcmVzdWx0ID0gMCA/IGEgOiBiO1xuXG5pZihpbnB1dCA9PT0gXCJoZWxsb1wiIHx8IFwiYnllXCIpe1xuICBvdXRwdXQoaW5wdXQpO1xufSJ9)

```
/*eslint no-constant-condition: "error"*/

if (false) {
    doSomethingUnfinished();
}

if (void x) {
    doSomethingUnfinished();
}

if (x &&= false) {
    doSomethingNever();
}

if (class {}) {
    doSomethingAlways();
}

if (new Boolean(x)) {
    doSomethingAlways();
}

if (Boolean(1)) {
    doSomethingAlways();
}

if (undefined) {
    doSomethingUnfinished();
}

if (x ||= true) {
    doSomethingAlways();
}

for (;-2;) {
    doSomethingForever();
}

while (typeof x) {
    doSomethingForever();
}

do {
    doSomethingForever();
} while (x = -1);

const result = 0 ? a : b;

if(input === "hello" || "bye"){
  output(input);
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
45
46
47
48
49
50
51
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBcImVycm9yXCIqL1xuXG5pZiAoeCA9PT0gMCkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59XG5cbmZvciAoOzspIHtcbiAgICBkb1NvbWV0aGluZ0ZvcmV2ZXIoKTtcbn1cblxud2hpbGUgKHR5cGVvZiB4ID09PSBcInVuZGVmaW5lZFwiKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuZG8ge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IHdoaWxlICh4KTtcblxuY29uc3QgcmVzdWx0ID0geCAhPT0gMCA/IGEgOiBiO1xuXG5pZihpbnB1dCA9PT0gXCJoZWxsb1wiIHx8IGlucHV0ID09PSBcImJ5ZVwiKXtcbiAgb3V0cHV0KGlucHV0KTtcbn0ifQ==)

```
/*eslint no-constant-condition: "error"*/

if (x === 0) {
    doSomething();
}

for (;;) {
    doSomethingForever();
}

while (typeof x === "undefined") {
    doSomething();
}

do {
    doSomething();
} while (x);

const result = x !== 0 ? a : b;

if(input === "hello" || input === "bye"){
  output(input);
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
```

## Options

### checkLoops

This is a string option having following values:

- `"all"` - Disallow constant expressions in all loops.
- `"allExceptWhileTrue"` (default) - Disallow constant expressions in all loops except `while` loops with expression `true`.
- `"none"` - Allow constant expressions in loops.

Or instead you can set the `checkLoops` value to booleans where `true` is same as `"all"` and `false` is same as `"none"`.

Examples of incorrect code for when `checkLoops` is `"all"` or `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBbXCJlcnJvclwiLCB7IFwiY2hlY2tMb29wc1wiOiBcImFsbFwiIH1dKi9cblxud2hpbGUgKHRydWUpIHtcbiAgICBkb1NvbWV0aGluZygpO1xufTtcblxuZm9yICg7dHJ1ZTspIHtcbiAgICBkb1NvbWV0aGluZygpO1xufTsifQ==)

```
/*eslint no-constant-condition: ["error", { "checkLoops": "all" }]*/

while (true) {
    doSomething();
};

for (;true;) {
    doSomething();
};
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBbXCJlcnJvclwiLCB7IFwiY2hlY2tMb29wc1wiOiB0cnVlIH1dKi9cblxud2hpbGUgKHRydWUpIHtcbiAgICBkb1NvbWV0aGluZygpO1xufTtcblxuZG8ge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IHdoaWxlICh0cnVlKSJ9)

```
/*eslint no-constant-condition: ["error", { "checkLoops": true }]*/

while (true) {
    doSomething();
};

do {
    doSomething();
} while (true)
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

Examples of correct code for when `checkLoops` is `"all"` or `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBbXCJlcnJvclwiLCB7IFwiY2hlY2tMb29wc1wiOiBcImFsbFwiIH1dKi9cblxud2hpbGUgKGEgPT09IGIpIHtcbiAgICBkb1NvbWV0aGluZygpO1xufTsifQ==)

```
/*eslint no-constant-condition: ["error", { "checkLoops": "all" }]*/

while (a === b) {
    doSomething();
};
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBbXCJlcnJvclwiLCB7IFwiY2hlY2tMb29wc1wiOiB0cnVlIH1dKi9cblxuZm9yIChsZXQgeCA9IDA7IHggPD0gMTA7IHgrKykge1xuICAgIGRvU29tZXRoaW5nKCk7XG59OyJ9)

```
/*eslint no-constant-condition: ["error", { "checkLoops": true }]*/

for (let x = 0; x <= 10; x++) {
    doSomething();
};
1
2
3
4
5
```

Example of correct code for when `checkLoops` is `"allExceptWhileTrue"`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBcImVycm9yXCIqL1xuXG53aGlsZSAodHJ1ZSkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59OyJ9)

```
/*eslint no-constant-condition: "error"*/

while (true) {
    doSomething();
};
1
2
3
4
5
```

Examples of correct code for when `checkLoops` is `"none"` or `false`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBbXCJlcnJvclwiLCB7IFwiY2hlY2tMb29wc1wiOiBcIm5vbmVcIiB9XSovXG5cbndoaWxlICh0cnVlKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbiAgICBpZiAoY29uZGl0aW9uKCkpIHtcbiAgICAgICAgYnJlYWs7XG4gICAgfVxufTtcblxuZG8ge1xuICAgIGRvU29tZXRoaW5nKCk7XG4gICAgaWYgKGNvbmRpdGlvbigpKSB7XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbn0gd2hpbGUgKHRydWUpIn0=)

```
/*eslint no-constant-condition: ["error", { "checkLoops": "none" }]*/

while (true) {
    doSomething();
    if (condition()) {
        break;
    }
};

do {
    doSomething();
    if (condition()) {
        break;
    }
} while (true)
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtY29uZGl0aW9uOiBbXCJlcnJvclwiLCB7IFwiY2hlY2tMb29wc1wiOiBmYWxzZSB9XSovXG5cbndoaWxlICh0cnVlKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbiAgICBpZiAoY29uZGl0aW9uKCkpIHtcbiAgICAgICAgYnJlYWs7XG4gICAgfVxufTtcblxuZm9yICg7dHJ1ZTspIHtcbiAgICBkb1NvbWV0aGluZygpO1xuICAgIGlmIChjb25kaXRpb24oKSkge1xuICAgICAgICBicmVhaztcbiAgICB9XG59OyJ9)

```
/*eslint no-constant-condition: ["error", { "checkLoops": false }]*/

while (true) {
    doSomething();
    if (condition()) {
        break;
    }
};

for (;true;) {
    doSomething();
    if (condition()) {
        break;
    }
};
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

## Related Rules

- [no-constant-binary-expression](/docs/latest/rules/no-constant-binary-expression)

## Version

This rule was introduced in ESLint v0.4.1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-constant-condition.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-constant-condition.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-constant-condition.md
                    
                
                )
