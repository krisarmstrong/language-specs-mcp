# no-plusplus

Disallow the unary operators `++` and `--`

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowForLoopAfterthoughts](#allowforloopafterthoughts)

3. [Version](#version)
4. [Resources](#resources)

Because the unary `++` and `--` operators are subject to automatic semicolon insertion, differences in whitespace can change semantics of source code.

```
let i = 10;
let j = 20;

i ++
j
// i = 11, j = 20
1
2
3
4
5
6
```

Copy code to clipboard

```
let i = 10;
let j = 20;

i
++
j
// i = 10, j = 21
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

This rule disallows the unary operators `++` and `--`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGx1c3BsdXM6IFwiZXJyb3JcIiovXG5cbmxldCBmb28gPSAwO1xuZm9vKys7XG5cbmxldCBiYXIgPSA0MjtcbmJhci0tO1xuXG5mb3IgKGxldCBpID0gMDsgaSA8IGw7IGkrKykge1xuICAgIGRvU29tZXRoaW5nKGkpO1xufSJ9)

```
/*eslint no-plusplus: "error"*/

let foo = 0;
foo++;

let bar = 42;
bar--;

for (let i = 0; i < l; i++) {
    doSomething(i);
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGx1c3BsdXM6IFwiZXJyb3JcIiovXG5cbmxldCBmb28gPSAwO1xuZm9vICs9IDE7XG5cbmxldCBiYXIgPSA0MjtcbmJhciAtPSAxO1xuXG5mb3IgKGxldCBpID0gMDsgaSA8IGw7IGkgKz0gMSkge1xuICAgIGRvU29tZXRoaW5nKGkpO1xufSJ9)

```
/*eslint no-plusplus: "error"*/

let foo = 0;
foo += 1;

let bar = 42;
bar -= 1;

for (let i = 0; i < l; i += 1) {
    doSomething(i);
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

## Options

This rule has an object option.

- `"allowForLoopAfterthoughts": true` allows unary operators `++` and `--` in the afterthought (final expression) of a `for` loop.

### allowForLoopAfterthoughts

Examples of correct code for this rule with the `{ "allowForLoopAfterthoughts": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGx1c3BsdXM6IFtcImVycm9yXCIsIHsgXCJhbGxvd0Zvckxvb3BBZnRlcnRob3VnaHRzXCI6IHRydWUgfV0qL1xuXG5mb3IgKGxldCBpID0gMDsgaSA8IGw7IGkrKykge1xuICAgIGRvU29tZXRoaW5nKGkpO1xufVxuXG5mb3IgKGxldCBpID0gbDsgaSA+PSAwOyBpLS0pIHtcbiAgICBkb1NvbWV0aGluZyhpKTtcbn1cblxuZm9yIChsZXQgaSA9IDAsIGogPSBsOyBpIDwgbDsgaSsrLCBqLS0pIHtcbiAgICBkb1NvbWV0aGluZyhpLCBqKTtcbn0ifQ==)

```
/*eslint no-plusplus: ["error", { "allowForLoopAfterthoughts": true }]*/

for (let i = 0; i < l; i++) {
    doSomething(i);
}

for (let i = l; i >= 0; i--) {
    doSomething(i);
}

for (let i = 0, j = l; i < l; i++, j--) {
    doSomething(i, j);
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

Examples of incorrect code for this rule with the `{ "allowForLoopAfterthoughts": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcGx1c3BsdXM6IFtcImVycm9yXCIsIHsgXCJhbGxvd0Zvckxvb3BBZnRlcnRob3VnaHRzXCI6IHRydWUgfV0qL1xuXG5mb3IgKGxldCBpID0gMDsgaSA8IGw7IGogPSBpKyspIHtcbiAgICBkb1NvbWV0aGluZyhpLCBqKTtcbn1cblxuZm9yIChsZXQgaSA9IGw7IGktLTspIHtcbiAgICBkb1NvbWV0aGluZyhpKTtcbn1cblxuZm9yIChsZXQgaSA9IDA7IGkgPCBsOykgaSsrOyJ9)

```
/*eslint no-plusplus: ["error", { "allowForLoopAfterthoughts": true }]*/

for (let i = 0; i < l; j = i++) {
    doSomething(i, j);
}

for (let i = l; i--;) {
    doSomething(i);
}

for (let i = 0; i < l;) i++;
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

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-plusplus.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-plusplus.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-plusplus.md
                    
                
                )
