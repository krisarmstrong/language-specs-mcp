# id-match

Require identifiers to match a specified regular expression

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [properties](#properties)
  2. [classFields](#classfields)
  3. [onlyDeclarations](#onlydeclarations)
  4. [ignoreDestructuring: false](#ignoredestructuring-false)
  5. [ignoreDestructuring: true](#ignoredestructuring-true)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

“There are only two hard things in Computer Science: cache invalidation and naming things.” — Phil Karlton

Naming things consistently in a project is an often underestimated aspect of code creation. When done correctly, it can save your team hours of unnecessary head scratching and misdirections. This rule allows you to precisely define and enforce the variables and function names on your team should use. No more limiting yourself to camelCase, snake_case, PascalCase, or HungarianNotation. `id-match` has all your needs covered!

## Rule Details

This rule requires identifiers in assignments and `function` definitions to match a specified regular expression.

## Options

This rule has a string option for the specified regular expression.

For example, to enforce a camelcase naming convention:

```
{
    "id-match": ["error", "^[a-z]+([A-Z][a-z]+)*$"]
}
1
2
3
```

Copy code to clipboard

Examples of incorrect code for this rule with the `"^[a-z]+([A-Z][a-z]+)*$"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFtcImVycm9yXCIsIFwiXlthLXpdKyhbQS1aXVthLXpdKykqJFwiXSovXG5cbmNvbnN0IG15X2Zhdm9yaXRlX2NvbG9yID0gXCIjMTEyQzg1XCI7XG5jb25zdCBfbXlGYXZvcml0ZUNvbG9yICA9IFwiIzExMkM4NVwiO1xuY29uc3QgbXlGYXZvcml0ZUNvbG9yXyAgPSBcIiMxMTJDODVcIjtcbmNvbnN0IE1ZX0ZBVk9SSVRFX0NPTE9SID0gXCIjMTEyQzg1XCI7XG5mdW5jdGlvbiBkb19zb21ldGhpbmcoKSB7XG4gICAgLy8gLi4uXG59XG5cbmNsYXNzIE15X0NsYXNzIHt9XG5cbmNsYXNzIG15Q2xhc3Mge1xuICAgIGRvX3NvbWV0aGluZygpIHt9XG59XG5cbmNsYXNzIGFub3RoZXJDbGFzcyB7XG4gICAgI2RvX3NvbWV0aGluZygpIHt9XG59In0=)

```
/*eslint id-match: ["error", "^[a-z]+([A-Z][a-z]+)*$"]*/

const my_favorite_color = "#112C85";
const _myFavoriteColor  = "#112C85";
const myFavoriteColor_  = "#112C85";
const MY_FAVORITE_COLOR = "#112C85";
function do_something() {
    // ...
}

class My_Class {}

class myClass {
    do_something() {}
}

class anotherClass {
    #do_something() {}
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
```

Examples of correct code for this rule with the `"^[a-z]+([A-Z][a-z]+)*$"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFtcImVycm9yXCIsIFwiXlthLXpdKyhbQS1aXVthLXpdKykqJFwiXSovXG5cbmNvbnN0IG15RmF2b3JpdGVDb2xvciAgID0gXCIjMTEyQzg1XCI7XG5jb25zdCBmb28gPSBiYXIuYmF6X2Jvb207XG5jb25zdCBidXogPSB7IHF1eDogYmFyLmJhel9ib29tIH07XG5kb19zb21ldGhpbmcoKTtcbmNvbnN0IG9iaiA9IHtcbiAgICBteV9wcmVmOiAxXG59O1xuXG5jbGFzcyBteUNsYXNzIHt9XG5cbmNsYXNzIGFub3RoZXJDbGFzcyB7XG4gICAgZG9Tb21ldGhpbmcoKSB7fVxufVxuXG5jbGFzcyBvbmVNb3JlQ2xhc3Mge1xuICAgICNkb1NvbWV0aGluZygpIHt9XG59In0=)

```
/*eslint id-match: ["error", "^[a-z]+([A-Z][a-z]+)*$"]*/

const myFavoriteColor   = "#112C85";
const foo = bar.baz_boom;
const buz = { qux: bar.baz_boom };
do_something();
const obj = {
    my_pref: 1
};

class myClass {}

class anotherClass {
    doSomething() {}
}

class oneMoreClass {
    #doSomething() {}
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
```

This rule has an object option:

- `"properties": false` (default) does not check object properties
- `"properties": true` requires object literal properties and member expression assignment properties to match the specified regular expression
- `"classFields": false` (default) does not check class field names
- `"classFields": true` requires class field names to match the specified regular expression
- `"onlyDeclarations": false` (default) requires all variable names to match the specified regular expression
- `"onlyDeclarations": true` requires only `var`, `const`, `let`, `function`, and `class` declarations to match the specified regular expression
- `"ignoreDestructuring": false` (default) enforces `id-match` for destructured identifiers
- `"ignoreDestructuring": true` does not check destructured identifiers

### properties

Examples of incorrect code for this rule with the `"^[a-z]+([A-Z][a-z]+)*$", { "properties": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFtcImVycm9yXCIsIFwiXlthLXpdKyhbQS1aXVthLXpdKykqJFwiLCB7IFwicHJvcGVydGllc1wiOiB0cnVlIH1dKi9cblxuY29uc3Qgb2JqID0ge1xuICAgIG15X3ByZWY6IDFcbn07XG5cbm9iai5kb19zb21ldGhpbmcgPSBmdW5jdGlvbigpIHtcbiAgICAvLyAuLi5cbn07In0=)

```
/*eslint id-match: ["error", "^[a-z]+([A-Z][a-z]+)*$", { "properties": true }]*/

const obj = {
    my_pref: 1
};

obj.do_something = function() {
    // ...
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

### classFields

Examples of incorrect code for this rule with the `"^[a-z]+([A-Z][a-z]+)*$", { "classFields": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFtcImVycm9yXCIsIFwiXlthLXpdKyhbQS1aXVthLXpdKykqJFwiLCB7IFwiY2xhc3NGaWVsZHNcIjogdHJ1ZSB9XSovXG5cbmNsYXNzIG15Q2xhc3Mge1xuICAgIG15X3ByZWYgPSAxO1xufVxuXG5jbGFzcyBhbm90aGVyQ2xhc3Mge1xuICAgICNteV9wcmVmID0gMTtcbn0ifQ==)

```
/*eslint id-match: ["error", "^[a-z]+([A-Z][a-z]+)*$", { "classFields": true }]*/

class myClass {
    my_pref = 1;
}

class anotherClass {
    #my_pref = 1;
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

### onlyDeclarations

Examples of correct code for this rule with the `"^[a-z]+([A-Z][a-z]+)*$", { "onlyDeclarations": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFsyLCBcIl5bYS16XSsoW0EtWl1bYS16XSspKiRcIiwgeyBcIm9ubHlEZWNsYXJhdGlvbnNcIjogdHJ1ZSB9XSovXG5cbmZvbyA9IF9fZGlybmFtZTsifQ==)

```
/*eslint id-match: [2, "^[a-z]+([A-Z][a-z]+)*$", { "onlyDeclarations": true }]*/

foo = __dirname;
1
2
3
```

### ignoreDestructuring: false

Examples of incorrect code for this rule with the default `"^[^_]+$", { "ignoreDestructuring": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFsyLCBcIl5bXl9dKyRcIiwgeyBcImlnbm9yZURlc3RydWN0dXJpbmdcIjogZmFsc2UgfV0qL1xuXG5jb25zdCB7IGNhdGVnb3J5X2lkIH0gPSBxdWVyeTtcblxuY29uc3QgeyBjYXRlZ29yeWlkX0RlZmF1bHQgPSAxIH0gPSBxdWVyeTtcblxuY29uc3QgeyBjYXRlZ29yeV9pZHM6IGNhdGVnb3J5X2lkcyB9ID0gcXVlcnk7XG5cbmNvbnN0IHsgY2F0ZWdvcnlfaWQ6IGNhdGVnb3J5X0FsaWFzIH0gPSBxdWVyeTtcblxuY29uc3QgeyBjYXRlZ29yeV9pZDogY2F0ZWdvcnlfSWRSZW5hbWVkLCAuLi5vdGhlcl9Qcm9wcyB9ID0gcXVlcnk7In0=)

```
/*eslint id-match: [2, "^[^_]+$", { "ignoreDestructuring": false }]*/

const { category_id } = query;

const { categoryid_Default = 1 } = query;

const { category_ids: category_ids } = query;

const { category_id: category_Alias } = query;

const { category_id: category_IdRenamed, ...other_Props } = query;
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

### ignoreDestructuring: true

Examples of incorrect code for this rule with the `"^[^_]+$", { "ignoreDestructuring": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFsyLCBcIl5bXl9dKyRcIiwgeyBcImlnbm9yZURlc3RydWN0dXJpbmdcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IHsgY2F0ZWdvcnlfaWQ6IGNhdGVnb3J5X2FsaWFzIH0gPSBxdWVyeTtcblxuY29uc3QgeyBjYXRlZ29yeV9pZDogY2F0ZWdvcnlfSWQsIC4uLm90aGVyX3Byb3BzIH0gPSBxdWVyeTsifQ==)

```
/*eslint id-match: [2, "^[^_]+$", { "ignoreDestructuring": true }]*/

const { category_id: category_alias } = query;

const { category_id: category_Id, ...other_props } = query;
1
2
3
4
5
```

Examples of correct code for this rule with the `"^[^_]+$", { "ignoreDestructuring": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgaWQtbWF0Y2g6IFsyLCBcIl5bXl9dKyRcIiwgeyBcImlnbm9yZURlc3RydWN0dXJpbmdcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IHsgY2F0ZWdvcnlfaWQgfSA9IHF1ZXJ5O1xuXG5jb25zdCB7IGNhdGVnb3J5X0lkID0gMSB9ID0gcXVlcnk7XG5cbmNvbnN0IHsgY2F0ZWdvcnlfYWxpYXM6IGNhdGVnb3J5X2FsaWFzIH0gPSBxdWVyeTsifQ==)

```
/*eslint id-match: [2, "^[^_]+$", { "ignoreDestructuring": true }]*/

const { category_id } = query;

const { category_Id = 1 } = query;

const { category_alias: category_alias } = query;
1
2
3
4
5
6
7
```

## When Not To Use It

If you don’t want to enforce any particular naming convention for all identifiers, or your naming convention is too complex to be enforced by configuring this rule, then you should not enable this rule.

## Version

This rule was introduced in ESLint v1.0.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/id-match.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/id-match.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/id-match.md
                    
                
                )
