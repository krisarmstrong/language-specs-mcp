# no-extra-boolean-cast

Disallow unnecessary boolean casts

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [enforceForInnerExpressions](#enforceforinnerexpressions)

3. [Version](#version)
4. [Resources](#resources)

In contexts such as an `if` statement’s test where the result of the expression will already be coerced to a Boolean, casting to a Boolean via double negation (`!!`) or a `Boolean` call is unnecessary. For example, these `if` statements are equivalent:

```
if (!!foo) {
    // ...
}

if (Boolean(foo)) {
    // ...
}

if (foo) {
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
```

Copy code to clipboard

## Rule Details

This rule disallows unnecessary boolean casts.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtYm9vbGVhbi1jYXN0OiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSAhISFiYXI7XG5cbmNvbnN0IGZvbzEgPSAhIWJhciA/IGJheiA6IGJhdDtcblxuY29uc3QgZm9vMiA9IEJvb2xlYW4oISFiYXIpO1xuXG5jb25zdCBmb28zID0gbmV3IEJvb2xlYW4oISFiYXIpO1xuXG5pZiAoISFmb28pIHtcbiAgICAvLyAuLi5cbn1cblxuaWYgKEJvb2xlYW4oZm9vKSkge1xuICAgIC8vIC4uLlxufVxuXG53aGlsZSAoISFmb28pIHtcbiAgICAvLyAuLi5cbn1cblxuZG8ge1xuICAgIC8vIC4uLlxufSB3aGlsZSAoQm9vbGVhbihmb28pKTtcblxuZm9yICg7ICEhZm9vOyApIHtcbiAgICAvLyAuLi5cbn0ifQ==)

```
/*eslint no-extra-boolean-cast: "error"*/

const foo = !!!bar;

const foo1 = !!bar ? baz : bat;

const foo2 = Boolean(!!bar);

const foo3 = new Boolean(!!bar);

if (!!foo) {
    // ...
}

if (Boolean(foo)) {
    // ...
}

while (!!foo) {
    // ...
}

do {
    // ...
} while (Boolean(foo));

for (; !!foo; ) {
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtYm9vbGVhbi1jYXN0OiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSAhIWJhcjtcbmNvbnN0IGZvbzEgPSBCb29sZWFuKGJhcik7XG5cbmZ1bmN0aW9uIHF1eCgpIHtcbiAgICByZXR1cm4gISFiYXI7XG59XG5cbmZvbyA9IGJhciA/ICEhYmF6IDogISFiYXQ7In0=)

```
/*eslint no-extra-boolean-cast: "error"*/

const foo = !!bar;
const foo1 = Boolean(bar);

function qux() {
    return !!bar;
}

foo = bar ? !!baz : !!bat;
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

- `"enforceForInnerExpressions"` when set to `true`, in addition to checking default contexts, checks whether extra boolean casts are present in expressions whose result is used in a boolean context. See examples below. Default is `false`, meaning that this rule by default does not warn about extra booleans cast inside inner expressions.

Deprecated: The object property `enforceForLogicalOperands` is deprecated ([eslint#18222](https://github.com/eslint/eslint/pull/18222)). Please use `enforceForInnerExpressions` instead.

### enforceForInnerExpressions

Examples of incorrect code for this rule with `"enforceForInnerExpressions"` option set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtYm9vbGVhbi1jYXN0OiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9ySW5uZXJFeHByZXNzaW9uc1wiOiB0cnVlfV0qL1xuXG5pZiAoISFmb28gfHwgYmFyKSB7XG4gICAgLy8uLi5cbn1cblxud2hpbGUgKCEhZm9vICYmIGJhcikge1xuICAgIC8vLi4uXG59XG5cbmlmICgoISFmb28gfHwgYmFyKSAmJiAhIWJheikge1xuICAgIC8vLi4uXG59XG5cbmNvbnN0IGZvbyA9IG5ldyBCb29sZWFuKCEhYmFyIHx8IGJheik7XG5cbmZvbyAmJiBCb29sZWFuKGJhcikgPyBiYXogOiBiYXQ7XG5cbmNvbnN0IHRlcm5hcnlCcmFuY2hlcyA9IEJvb2xlYW4oYmFyID8gISFiYXogOiBiYXQpO1xuXG5jb25zdCBudWxsaXNoQ29hbGVzY2luZ09wZXJhdG9yID0gQm9vbGVhbihiYXIgPz8gQm9vbGVhbihiYXopKTtcblxuY29uc3QgY29tbWFPcGVyYXRvciA9IEJvb2xlYW4oKGJhciwgYmF6LCAhIWJhdCkpO1xuXG4vLyBhbm90aGVyIGNvbW1hIG9wZXJhdG9yIGV4YW1wbGVcbmZvciAobGV0IGkgPSAwOyBjb25zb2xlLmxvZyhpKSwgQm9vbGVhbihpIDwgMTApOyBpKyspIHtcbiAgICAvLyAuLi5cbn0ifQ==)

```
/*eslint no-extra-boolean-cast: ["error", {"enforceForInnerExpressions": true}]*/

if (!!foo || bar) {
    //...
}

while (!!foo && bar) {
    //...
}

if ((!!foo || bar) && !!baz) {
    //...
}

const foo = new Boolean(!!bar || baz);

foo && Boolean(bar) ? baz : bat;

const ternaryBranches = Boolean(bar ? !!baz : bat);

const nullishCoalescingOperator = Boolean(bar ?? Boolean(baz));

const commaOperator = Boolean((bar, baz, !!bat));

// another comma operator example
for (let i = 0; console.log(i), Boolean(i < 10); i++) {
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
```

Examples of correct code for this rule with `"enforceForInnerExpressions"` option set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXh0cmEtYm9vbGVhbi1jYXN0OiBbXCJlcnJvclwiLCB7XCJlbmZvcmNlRm9ySW5uZXJFeHByZXNzaW9uc1wiOiB0cnVlfV0qL1xuXG4vLyBOb3RlIHRoYXQgYHx8YCBhbmQgYCYmYCBhbG9uZSBhcmVuJ3QgYSBib29sZWFuIGNvbnRleHQgZm9yIGVpdGhlciBvcGVyYW5kXG4vLyBzaW5jZSB0aGUgcmVzdWx0YW50IHZhbHVlIG5lZWQgbm90IGJlIGEgYm9vbGVhbiB3aXRob3V0IGNhc3RpbmcuXG5jb25zdCBmb28gPSAhIWJhciB8fCBiYXo7XG5cbmlmIChmb28gfHwgYmFyKSB7XG4gICAgLy8uLi5cbn1cblxud2hpbGUgKGZvbyAmJiBiYXIpIHtcbiAgICAvLy4uLlxufVxuXG5pZiAoKGZvbyB8fCBiYXIpICYmIGJheikge1xuICAgIC8vLi4uXG59XG5cbmNvbnN0IGZvbzEgPSBuZXcgQm9vbGVhbihiYXIgfHwgYmF6KTtcblxuZm9vICYmIGJhciA/IGJheiA6IGJhdDtcblxuY29uc3QgdGVybmFyeUJyYW5jaGVzID0gQm9vbGVhbihiYXIgPyBiYXogOiBiYXQpO1xuXG5jb25zdCBudWxsaXNoQ29hbGVzY2luZ09wZXJhdG9yID0gQm9vbGVhbihiYXIgPz8gYmF6KTtcblxuY29uc3QgY29tbWFPcGVyYXRvciA9IEJvb2xlYW4oKGJhciwgYmF6LCBiYXQpKTtcblxuLy8gYW5vdGhlciBjb21tYSBvcGVyYXRvciBleGFtcGxlXG5mb3IgKGxldCBpID0gMDsgY29uc29sZS5sb2coaSksIGkgPCAxMDsgaSsrKSB7XG4gICAgLy8gLi4uXG59XG5cbi8vIGNvbW1hIG9wZXJhdG9yIGluIG5vbi1maW5hbCBwb3NpdGlvblxuQm9vbGVhbigoQm9vbGVhbihiYXIpLCBiYXosIGJhdCkpOyJ9)

```
/*eslint no-extra-boolean-cast: ["error", {"enforceForInnerExpressions": true}]*/

// Note that `||` and `&&` alone aren't a boolean context for either operand
// since the resultant value need not be a boolean without casting.
const foo = !!bar || baz;

if (foo || bar) {
    //...
}

while (foo && bar) {
    //...
}

if ((foo || bar) && baz) {
    //...
}

const foo1 = new Boolean(bar || baz);

foo && bar ? baz : bat;

const ternaryBranches = Boolean(bar ? baz : bat);

const nullishCoalescingOperator = Boolean(bar ?? baz);

const commaOperator = Boolean((bar, baz, bat));

// another comma operator example
for (let i = 0; console.log(i), i < 10; i++) {
    // ...
}

// comma operator in non-final position
Boolean((Boolean(bar), baz, bat));
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
```

## Version

This rule was introduced in ESLint v0.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-extra-boolean-cast.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-extra-boolean-cast.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-extra-boolean-cast.md
                    
                
                )
