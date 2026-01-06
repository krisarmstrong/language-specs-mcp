# yoda

Require or disallow "Yoda" conditions

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [never](#never)
  2. [exceptRange](#exceptrange)
  3. [onlyEquality](#onlyequality)
  4. [always](#always)

3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Yoda conditions are so named because the literal value of the condition comes first while the variable comes second. For example, the following is a Yoda condition:

```
if ("red" === color) {
    // ...
}
1
2
3
```

Copy code to clipboard

This is called a Yoda condition because it reads as, “if red equals the color”, similar to the way the Star Wars character Yoda speaks. Compare to the other way of arranging the operands:

```
if (color === "red") {
    // ...
}
1
2
3
```

Copy code to clipboard

This typically reads, “if the color equals red”, which is arguably a more natural way to describe the comparison.

Proponents of Yoda conditions highlight that it is impossible to mistakenly use `=` instead of `==` because you cannot assign to a literal value. Doing so will cause a syntax error and you will be informed of the mistake early on. This practice was therefore very common in early programming where tools were not yet available.

Opponents of Yoda conditions point out that tooling has made us better programmers because tools will catch the mistaken use of `=` instead of `==` (ESLint will catch this for you). Therefore, they argue, the utility of the pattern doesn’t outweigh the readability hit the code takes while using Yoda conditions.

## Rule Details

This rule aims to enforce consistent style of conditions which compare a variable to a literal value.

## Options

This rule can take a string option:

- If it is the default `"never"`, then comparisons must never be Yoda conditions.
- If it is `"always"`, then the literal value must always come first.

The default `"never"` option can have exception options in an object literal:

- If the `"exceptRange"` property is `true`, the rule allows Yoda conditions in range comparisons which are wrapped directly in parentheses, including the parentheses of an `if` or `while` condition. The default value is `false`. A range comparison tests whether a variable is inside or outside the range between two literal values.
- If the `"onlyEquality"` property is `true`, the rule reports Yoda conditions only for the equality operators `==` and `===`. The default value is `false`.

The `onlyEquality` option allows a superset of the exceptions which `exceptRange` allows, thus both options are not useful together.

### never

Examples of incorrect code for the default `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgeW9kYTogXCJlcnJvclwiKi9cblxuaWYgKFwicmVkXCIgPT09IGNvbG9yKSB7XG4gICAgLy8gLi4uXG59XG5cbmlmIChgcmVkYCA9PT0gY29sb3IpIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKGByZWRgID09PSBgJHtjb2xvcn1gKSB7XG4gICAgLy8gLi4uXG59XG5cbmlmICh0cnVlID09IGZsYWcpIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKDUgPiBjb3VudCkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoLTEgPCBzdHIuaW5kZXhPZihzdWJzdHIpKSB7XG4gICAgLy8gLi4uXG59XG5cbmlmICgwIDw9IHggJiYgeCA8IDEpIHtcbiAgICAvLyAuLi5cbn0ifQ==)

```
/*eslint yoda: "error"*/

if ("red" === color) {
    // ...
}

if (`red` === color) {
    // ...
}

if (`red` === `${color}`) {
    // ...
}

if (true == flag) {
    // ...
}

if (5 > count) {
    // ...
}

if (-1 < str.indexOf(substr)) {
    // ...
}

if (0 <= x && x < 1) {
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
```

Examples of correct code for the default `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgeW9kYTogXCJlcnJvclwiKi9cblxuaWYgKDUgJiB2YWx1ZSkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAodmFsdWUgPT09IFwicmVkXCIpIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKHZhbHVlID09PSBgcmVkYCkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoYCR7dmFsdWV9YCA9PT0gYHJlZGApIHtcblxufSJ9)

```
/*eslint yoda: "error"*/

if (5 & value) {
    // ...
}

if (value === "red") {
    // ...
}

if (value === `red`) {
    // ...
}

if (`${value}` === `red`) {

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

### exceptRange

Examples of correct code for the `"never", { "exceptRange": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgeW9kYTogW1wiZXJyb3JcIiwgXCJuZXZlclwiLCB7IFwiZXhjZXB0UmFuZ2VcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIGlzUmVkZGlzaChjb2xvcikge1xuICAgIHJldHVybiAoY29sb3IuaHVlIDwgNjAgfHwgMzAwIDwgY29sb3IuaHVlKTtcbn1cblxuaWYgKHggPCAtMSB8fCAxIDwgeCkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoY291bnQgPCAxMCAmJiAoMCA8PSByYW5kICYmIHJhbmQgPCAxKSkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoYGJsdWVgIDwgeCAmJiB4IDwgYGdyZWVuYCkge1xuICAgIC8vIC4uLlxufVxuXG5mdW5jdGlvbiBob3dMb25nKGFycikge1xuICAgIHJldHVybiAoMCA8PSBhcnIubGVuZ3RoICYmIGFyci5sZW5ndGggPCAxMCkgPyBcInNob3J0XCIgOiBcImxvbmdcIjtcbn0ifQ==)

```
/*eslint yoda: ["error", "never", { "exceptRange": true }]*/

function isReddish(color) {
    return (color.hue < 60 || 300 < color.hue);
}

if (x < -1 || 1 < x) {
    // ...
}

if (count < 10 && (0 <= rand && rand < 1)) {
    // ...
}

if (`blue` < x && x < `green`) {
    // ...
}

function howLong(arr) {
    return (0 <= arr.length && arr.length < 10) ? "short" : "long";
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
```

### onlyEquality

Examples of correct code for the `"never", { "onlyEquality": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgeW9kYTogW1wiZXJyb3JcIiwgXCJuZXZlclwiLCB7IFwib25seUVxdWFsaXR5XCI6IHRydWUgfV0qL1xuXG5pZiAoeCA8IC0xIHx8IDkgPCB4KSB7XG59XG5cbmlmICh4ICE9PSAnZm9vJyAmJiAnYmFyJyAhPSB4KSB7XG59XG5cbmlmICh4ICE9PSBgZm9vYCAmJiBgYmFyYCAhPSB4KSB7XG59In0=)

```
/*eslint yoda: ["error", "never", { "onlyEquality": true }]*/

if (x < -1 || 9 < x) {
}

if (x !== 'foo' && 'bar' != x) {
}

if (x !== `foo` && `bar` != x) {
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

### always

Examples of incorrect code for the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgeW9kYTogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5pZiAoY29sb3IgPT0gXCJibHVlXCIpIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKGNvbG9yID09IGBibHVlYCkge1xuICAgIC8vIC4uLlxufSJ9)

```
/*eslint yoda: ["error", "always"]*/

if (color == "blue") {
    // ...
}

if (color == `blue`) {
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

Examples of correct code for the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgeW9kYTogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5pZiAoXCJibHVlXCIgPT0gdmFsdWUpIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKGBibHVlYCA9PSB2YWx1ZSkge1xuICAgIC8vIC4uLlxufVxuXG5pZiAoYGJsdWVgID09IGAke3ZhbHVlfWApIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKC0xIDwgc3RyLmluZGV4T2Yoc3Vic3RyKSkge1xuICAgIC8vIC4uLlxufSJ9)

```
/*eslint yoda: ["error", "always"]*/

if ("blue" == value) {
    // ...
}

if (`blue` == value) {
    // ...
}

if (`blue` == `${value}`) {
    // ...
}

if (-1 < str.indexOf(substr)) {
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

## Version

This rule was introduced in ESLint v0.7.1.

## Further Reading

[Yoda conditions - Wikipedia](https://en.wikipedia.org/wiki/Yoda_conditions)
 en.wikipedia.org[Coding in Style](http://thomas.tuerke.net/on/design/?with=1249091668#msg1146181680)
 thomas.tuerke.net

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/yoda.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/yoda.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/yoda.md
                    
                
                )
