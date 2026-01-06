# sort-keys

Require object keys to be sorted

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [desc](#desc)
  2. [caseSensitive](#casesensitive)
  3. [natural](#natural)
  4. [minKeys](#minkeys)
  5. [allowLineSeparatedGroups](#allowlineseparatedgroups)
  6. [ignoreComputedKeys](#ignorecomputedkeys)

3. [When Not To Use It](#when-not-to-use-it)
4. [Compatibility](#compatibility)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Resources](#resources)

When declaring multiple properties, some developers prefer to sort property names alphabetically to more easily find and/or diff necessary properties at a later time. Others feel that it adds complexity and becomes burden to maintain.

## Rule Details

This rule checks all property definitions of object expressions and verifies that all variables are sorted alphabetically.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBcImVycm9yXCIqL1xuXG5jb25zdCBvYmoxID0ge2E6IDEsIGM6IDMsIGI6IDJ9O1xuY29uc3Qgb2JqMiA9IHthOiAxLCBcImNcIjogMywgYjogMn07XG5cbi8vIENhc2Utc2Vuc2l0aXZlIGJ5IGRlZmF1bHQuXG5jb25zdCBvYmozID0ge2E6IDEsIGI6IDIsIEM6IDN9O1xuXG4vLyBOb24tbmF0dXJhbCBvcmRlciBieSBkZWZhdWx0LlxuY29uc3Qgb2JqNCA9IHsxOiBhLCAyOiBjLCAxMDogYn07XG5cbi8vIFRoaXMgcnVsZSBjaGVja3MgY29tcHV0ZWQgcHJvcGVydGllcyB3aGljaCBoYXZlIGEgc2ltcGxlIG5hbWUgYXMgd2VsbC5cbi8vIFNpbXBsZSBuYW1lcyBhcmUgbmFtZXMgd2hpY2ggYXJlIGV4cHJlc3NlZCBieSBhbiBJZGVudGlmaWVyIG5vZGUgb3IgYSBMaXRlcmFsIG5vZGUuXG5jb25zdCBTID0gU3ltYm9sKFwic1wiKVxuY29uc3Qgb2JqNSA9IHthOiAxLCBbXCJjXCJdOiAzLCBiOiAyfTtcbmNvbnN0IG9iajYgPSB7YTogMSwgW1NdOiAzLCBiOiAyfTsifQ==)

```
/*eslint sort-keys: "error"*/

const obj1 = {a: 1, c: 3, b: 2};
const obj2 = {a: 1, "c": 3, b: 2};

// Case-sensitive by default.
const obj3 = {a: 1, b: 2, C: 3};

// Non-natural order by default.
const obj4 = {1: a, 2: c, 10: b};

// This rule checks computed properties which have a simple name as well.
// Simple names are names which are expressed by an Identifier node or a Literal node.
const S = Symbol("s")
const obj5 = {a: 1, ["c"]: 3, b: 2};
const obj6 = {a: 1, [S]: 3, b: 2};
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBcImVycm9yXCIqL1xuXG5jb25zdCBvYmoxID0ge2E6IDEsIGI6IDIsIGM6IDN9O1xuY29uc3Qgb2JqMiA9IHthOiAxLCBcImJcIjogMiwgYzogM307XG5cbi8vIENhc2Utc2Vuc2l0aXZlIGJ5IGRlZmF1bHQuXG5jb25zdCBvYmozID0ge0M6IDMsIGE6IDEsIGI6IDJ9O1xuXG4vLyBOb24tbmF0dXJhbCBvcmRlciBieSBkZWZhdWx0LlxuY29uc3Qgb2JqNCA9IHsxOiBhLCAxMDogYiwgMjogY307XG5cbi8vIFRoaXMgcnVsZSBjaGVja3MgY29tcHV0ZWQgcHJvcGVydGllcyB3aGljaCBoYXZlIGEgc2ltcGxlIG5hbWUgYXMgd2VsbC5cbmNvbnN0IG9iajUgPSB7YTogMSwgW1wiYlwiXTogMiwgYzogM307XG5jb25zdCBvYmo2ID0ge2E6IDEsIFtiXTogMiwgYzogM307XG5cbi8vIFRoaXMgcnVsZSBpZ25vcmVzIGNvbXB1dGVkIHByb3BlcnRpZXMgd2hpY2ggaGF2ZSBhIG5vbi1zaW1wbGUgbmFtZS5cbmNvbnN0IG9iajcgPSB7YTogMSwgW2MgKyBkXTogMywgYjogMn07XG5jb25zdCBvYmo4ID0ge2E6IDEsIFtcImNcIiArIFwiZFwiXTogMywgYjogMn07XG5jb25zdCBvYmo5ID0ge2E6IDEsIFtgJHtjfWBdOiAzLCBiOiAyfTtcbmNvbnN0IG9iajEwID0ge2E6IDEsIFt0YWdgY2BdOiAzLCBiOiAyfTtcblxuLy8gVGhpcyBydWxlIGRvZXMgbm90IHJlcG9ydCB1bnNvcnRlZCBwcm9wZXJ0aWVzIHRoYXQgYXJlIHNlcGFyYXRlZCBieSBhIHNwcmVhZCBwcm9wZXJ0eS5cbmNvbnN0IG9iajExID0ge2I6IDEsIC4uLmMsIGE6IDJ9OyJ9)

```
/*eslint sort-keys: "error"*/

const obj1 = {a: 1, b: 2, c: 3};
const obj2 = {a: 1, "b": 2, c: 3};

// Case-sensitive by default.
const obj3 = {C: 3, a: 1, b: 2};

// Non-natural order by default.
const obj4 = {1: a, 10: b, 2: c};

// This rule checks computed properties which have a simple name as well.
const obj5 = {a: 1, ["b"]: 2, c: 3};
const obj6 = {a: 1, [b]: 2, c: 3};

// This rule ignores computed properties which have a non-simple name.
const obj7 = {a: 1, [c + d]: 3, b: 2};
const obj8 = {a: 1, ["c" + "d"]: 3, b: 2};
const obj9 = {a: 1, [`${c}`]: 3, b: 2};
const obj10 = {a: 1, [tag`c`]: 3, b: 2};

// This rule does not report unsorted properties that are separated by a spread property.
const obj11 = {b: 1, ...c, a: 2};
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

```
{
    "sort-keys": ["error", "asc", {"caseSensitive": true, "natural": false, "minKeys": 2}]
}
1
2
3
```

Copy code to clipboard

The 1st option is `"asc"` or `"desc"`.

- `"asc"` (default) - enforce properties to be in ascending order.
- `"desc"` - enforce properties to be in descending order.

The 2nd option is an object which has the following properties.

- `caseSensitive` - if `true`, enforce properties to be in case-sensitive order. Default is `true`.
- `minKeys` - Specifies the minimum number of keys that an object should have in order for the object’s unsorted keys to produce an error. Default is `2`, which means by default all objects with unsorted keys will result in lint errors.
- `natural` - if `true`, enforce properties to be in natural order. Default is `false`. Natural Order compares strings containing combination of letters and numbers in the way a human being would sort. It basically sorts numerically, instead of sorting alphabetically. So the number 10 comes after the number 3 in Natural Sorting.
- `allowLineSeparatedGroups` - if `true`, the rule allows to group object keys through line breaks. In other words, a blank line after a property will reset the sorting of keys. Default is `false`.
- `ignoreComputedKeys` - if `true`, the rule ignores all computed keys and doesn’t report unsorted properties separated by them. A computed key will reset the sorting of the following non-computed keys. Default is `false`.

Example for a list:

With `natural` as `true`, the ordering would be 1 3 6 8 10

With `natural` as `false`, the ordering would be 1 10 3 6 8

### desc

Examples of incorrect code for the `"desc"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImRlc2NcIl0qL1xuXG5jb25zdCBvYmoxID0ge2I6IDIsIGM6IDMsIGE6IDF9O1xuY29uc3Qgb2JqMiA9IHtcImJcIjogMiwgYzogMywgYTogMX07XG5cbi8vIENhc2Utc2Vuc2l0aXZlIGJ5IGRlZmF1bHQuXG5jb25zdCBvYmozID0ge0M6IDEsIGI6IDMsIGE6IDJ9O1xuXG4vLyBOb24tbmF0dXJhbCBvcmRlciBieSBkZWZhdWx0LlxuY29uc3Qgb2JqNCA9IHsxMDogYiwgMjogYywgMTogYX07In0=)

```
/*eslint sort-keys: ["error", "desc"]*/

const obj1 = {b: 2, c: 3, a: 1};
const obj2 = {"b": 2, c: 3, a: 1};

// Case-sensitive by default.
const obj3 = {C: 1, b: 3, a: 2};

// Non-natural order by default.
const obj4 = {10: b, 2: c, 1: a};
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

Examples of correct code for the `"desc"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImRlc2NcIl0qL1xuXG5jb25zdCBvYmoxID0ge2M6IDMsIGI6IDIsIGE6IDF9O1xuY29uc3Qgb2JqMiA9IHtjOiAzLCBcImJcIjogMiwgYTogMX07XG5cbi8vIENhc2Utc2Vuc2l0aXZlIGJ5IGRlZmF1bHQuXG5jb25zdCBvYmozID0ge2I6IDMsIGE6IDIsIEM6IDF9O1xuXG4vLyBOb24tbmF0dXJhbCBvcmRlciBieSBkZWZhdWx0LlxuY29uc3Qgb2JqNCA9IHsyOiBjLCAxMDogYiwgMTogYX07In0=)

```
/*eslint sort-keys: ["error", "desc"]*/

const obj1 = {c: 3, b: 2, a: 1};
const obj2 = {c: 3, "b": 2, a: 1};

// Case-sensitive by default.
const obj3 = {b: 3, a: 2, C: 1};

// Non-natural order by default.
const obj4 = {2: c, 10: b, 1: a};
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

### caseSensitive

Examples of incorrect code for the `{caseSensitive: false}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7Y2FzZVNlbnNpdGl2ZTogZmFsc2V9XSovXG5cbmNvbnN0IG9iajEgPSB7YTogMSwgYzogMywgQzogNCwgYjogMn07XG5jb25zdCBvYmoyID0ge2E6IDEsIEM6IDMsIGM6IDQsIGI6IDJ9OyJ9)

```
/*eslint sort-keys: ["error", "asc", {caseSensitive: false}]*/

const obj1 = {a: 1, c: 3, C: 4, b: 2};
const obj2 = {a: 1, C: 3, c: 4, b: 2};
1
2
3
4
```

Examples of correct code for the `{caseSensitive: false}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7Y2FzZVNlbnNpdGl2ZTogZmFsc2V9XSovXG5cbmNvbnN0IG9iajEgPSB7YTogMSwgYjogMiwgYzogMywgQzogNH07XG5jb25zdCBvYmoyID0ge2E6IDEsIGI6IDIsIEM6IDMsIGM6IDR9OyJ9)

```
/*eslint sort-keys: ["error", "asc", {caseSensitive: false}]*/

const obj1 = {a: 1, b: 2, c: 3, C: 4};
const obj2 = {a: 1, b: 2, C: 3, c: 4};
1
2
3
4
```

### natural

Examples of incorrect code for the `{natural: true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7bmF0dXJhbDogdHJ1ZX1dKi9cblxuY29uc3Qgb2JqID0gezE6IGEsIDEwOiBjLCAyOiBifTsifQ==)

```
/*eslint sort-keys: ["error", "asc", {natural: true}]*/

const obj = {1: a, 10: c, 2: b};
1
2
3
```

Examples of correct code for the `{natural: true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7bmF0dXJhbDogdHJ1ZX1dKi9cblxuY29uc3Qgb2JqID0gezE6IGEsIDI6IGIsIDEwOiBjfTsifQ==)

```
/*eslint sort-keys: ["error", "asc", {natural: true}]*/

const obj = {1: a, 2: b, 10: c};
1
2
3
```

### minKeys

Examples of incorrect code for the `{minKeys: 4}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7bWluS2V5czogNH1dKi9cblxuLy8gNCBrZXlzXG5jb25zdCBvYmoxID0ge1xuICAgIGI6IDIsXG4gICAgYTogMSwgLy8gbm90IHNvcnRlZCBjb3JyZWN0bHkgKHNob3VsZCBiZSAxc3Qga2V5KVxuICAgIGM6IDMsXG4gICAgZDogNCxcbn07XG5cbi8vIDUga2V5c1xuY29uc3Qgb2JqMiA9IHtcbiAgICAyOiAnYScsXG4gICAgMTogJ2InLCAvLyBub3Qgc29ydGVkIGNvcnJlY3RseSAoc2hvdWxkIGJlIDFzdCBrZXkpXG4gICAgMzogJ2MnLFxuICAgIDQ6ICdkJyxcbiAgICA1OiAnZScsXG59OyJ9)

```
/*eslint sort-keys: ["error", "asc", {minKeys: 4}]*/

// 4 keys
const obj1 = {
    b: 2,
    a: 1, // not sorted correctly (should be 1st key)
    c: 3,
    d: 4,
};

// 5 keys
const obj2 = {
    2: 'a',
    1: 'b', // not sorted correctly (should be 1st key)
    3: 'c',
    4: 'd',
    5: 'e',
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
16
17
18
```

Examples of correct code for the `{minKeys: 4}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7bWluS2V5czogNH1dKi9cblxuLy8gMyBrZXlzXG5jb25zdCBvYmoxID0ge1xuICAgIGI6IDIsXG4gICAgYTogMSxcbiAgICBjOiAzLFxufTtcblxuLy8gMiBrZXlzXG5jb25zdCBvYmoyID0ge1xuICAgIDI6ICdiJyxcbiAgICAxOiAnYScsXG59OyJ9)

```
/*eslint sort-keys: ["error", "asc", {minKeys: 4}]*/

// 3 keys
const obj1 = {
    b: 2,
    a: 1,
    c: 3,
};

// 2 keys
const obj2 = {
    2: 'b',
    1: 'a',
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
```

### allowLineSeparatedGroups

Examples of incorrect code for the `{allowLineSeparatedGroups: true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7YWxsb3dMaW5lU2VwYXJhdGVkR3JvdXBzOiB0cnVlfV0qL1xuXG5jb25zdCBvYmoxID0ge1xuICAgIGI6IDEsXG4gICAgYyAoKSB7XG5cbiAgICB9LFxuICAgIGE6IDNcbn1cblxuY29uc3Qgb2JqMiA9IHtcbiAgICBiOiAxLFxuICAgIGM6IDIsXG5cbiAgICB6ICgpIHtcblxuICAgIH0sXG4gICAgeTogM1xufVxuXG5jb25zdCBvYmozID0ge1xuICAgIGI6IDEsXG4gICAgYzogMixcblxuICAgIHogKCkge1xuXG4gICAgfSxcbiAgICAvLyBjb21tZW50XG4gICAgeTogMyxcbn1cblxuY29uc3Qgb2JqNCA9IHtcbiAgICBiOiAxXG4gICAgLy8gY29tbWVudCBiZWZvcmUgY29tbWFcbiAgICAsIGE6IDJcbn07In0=)

```
/*eslint sort-keys: ["error", "asc", {allowLineSeparatedGroups: true}]*/

const obj1 = {
    b: 1,
    c () {

    },
    a: 3
}

const obj2 = {
    b: 1,
    c: 2,

    z () {

    },
    y: 3
}

const obj3 = {
    b: 1,
    c: 2,

    z () {

    },
    // comment
    y: 3,
}

const obj4 = {
    b: 1
    // comment before comma
    , a: 2
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
```

Examples of correct code for the `{allowLineSeparatedGroups: true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7YWxsb3dMaW5lU2VwYXJhdGVkR3JvdXBzOiB0cnVlfV0qL1xuXG5jb25zdCBvYmoxID0ge1xuICAgIGU6IDEsXG4gICAgZjogMixcbiAgICBnOiAzLFxuXG4gICAgYTogNCxcbiAgICBiOiA1LFxuICAgIGM6IDZcbn1cblxuY29uc3Qgb2JqMiA9IHtcbiAgICBiOiAxLFxuXG4gICAgLy8gY29tbWVudFxuICAgIGE6IDQsXG4gICAgYzogNSxcbn1cblxuY29uc3Qgb2JqMyA9IHtcbiAgICBjOiAxLFxuICAgIGQ6IDIsXG5cbiAgICBiICgpIHtcblxuICAgIH0sXG4gICAgZTogMyxcbn1cblxuY29uc3Qgb2JqNCA9IHtcbiAgICBjOiAxLFxuICAgIGQ6IDIsXG4gICAgLy8gY29tbWVudFxuXG4gICAgLy8gY29tbWVudFxuICAgIGIoKSB7XG5cbiAgICB9LFxuICAgIGU6IDRcbn1cblxuY29uc3Qgb2JqNSA9IHtcbiAgICBiLFxuXG4gICAgW2ZvbyArIGJhcl06IDEsXG4gICAgYVxufVxuXG5jb25zdCBvYmo2ID0ge1xuICAgIGI6IDFcbiAgICAvLyBjb21tZW50IGJlZm9yZSBjb21tYVxuXG4gICAgLFxuICAgIGE6IDJcbn07XG5cbmNvbnN0IG9iajcgPSB7XG4gICAgYjogMSxcblxuICAgIGE6IDIsXG4gICAgLi4ueixcbiAgICBjOiAzXG59In0=)

```
/*eslint sort-keys: ["error", "asc", {allowLineSeparatedGroups: true}]*/

const obj1 = {
    e: 1,
    f: 2,
    g: 3,

    a: 4,
    b: 5,
    c: 6
}

const obj2 = {
    b: 1,

    // comment
    a: 4,
    c: 5,
}

const obj3 = {
    c: 1,
    d: 2,

    b () {

    },
    e: 3,
}

const obj4 = {
    c: 1,
    d: 2,
    // comment

    // comment
    b() {

    },
    e: 4
}

const obj5 = {
    b,

    [foo + bar]: 1,
    a
}

const obj6 = {
    b: 1
    // comment before comma

    ,
    a: 2
};

const obj7 = {
    b: 1,

    a: 2,
    ...z,
    c: 3
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
64
```

### ignoreComputedKeys

Examples of correct code for the `{ignoreComputedKeys: true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1rZXlzOiBbXCJlcnJvclwiLCBcImFzY1wiLCB7aWdub3JlQ29tcHV0ZWRLZXlzOiB0cnVlfV0qL1xuXG5jb25zdCBvYmoxID0ge1xuICAgIFtiXTogMSxcbiAgICBhOiAyXG59XG5cbmNvbnN0IG9iajIgPSB7XG4gICAgYzogMSxcbiAgICBbYl06IDIsXG4gICAgYTogM1xufVxuXG5jb25zdCBvYmozID0ge1xuICAgIGM6IDEsXG4gICAgW1wiYlwiXTogMixcbiAgICBhOiAzXG59In0=)

```
/*eslint sort-keys: ["error", "asc", {ignoreComputedKeys: true}]*/

const obj1 = {
    [b]: 1,
    a: 2
}

const obj2 = {
    c: 1,
    [b]: 2,
    a: 3
}

const obj3 = {
    c: 1,
    ["b"]: 2,
    a: 3
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
```

## When Not To Use It

If you don’t want to notify about properties’ order, then it’s safe to disable this rule.

## Compatibility

- JSCS:[validateOrderInObjectKeys](https://jscs-dev.github.io/rule/validateOrderInObjectKeys)

## Related Rules

- [sort-imports](/docs/latest/rules/sort-imports)
- [sort-vars](/docs/latest/rules/sort-vars)

## Version

This rule was introduced in ESLint v3.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/sort-keys.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/sort-keys.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/sort-keys.md
                    
                
                )
