# no-dupe-keys

Disallow duplicate keys in object literals

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Handled by TypeScript](#handled_by_typescript)
3. [Version](#version)
4. [Resources](#resources)

Multiple properties with the same key in object literals can cause unexpected behavior in your application.

```
const foo = {
    bar: "baz",
    bar: "qux"
};
1
2
3
4
```

Copy code to clipboard

## Rule Details

This rule disallows duplicate keys in object literals.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1rZXlzOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSB7XG4gICAgYmFyOiBcImJhelwiLFxuICAgIGJhcjogXCJxdXhcIlxufTtcblxuY29uc3QgYmFyID0ge1xuICAgIFwiYmFyXCI6IFwiYmF6XCIsXG4gICAgYmFyOiBcInF1eFwiXG59O1xuXG5jb25zdCBiYXogPSB7XG4gICAgMHgxOiBcImJhelwiLFxuICAgIDE6IFwicXV4XCJcbn07In0=)

```
/*eslint no-dupe-keys: "error"*/

const foo = {
    bar: "baz",
    bar: "qux"
};

const bar = {
    "bar": "baz",
    bar: "qux"
};

const baz = {
    0x1: "baz",
    1: "qux"
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1rZXlzOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSB7XG4gICAgYmFyOiBcImJhelwiLFxuICAgIHF1eHg6IFwicXV4XCJcbn07XG5cbmNvbnN0IG9iaiA9IHtcbiAgICBcIl9fcHJvdG9fX1wiOiBiYXosIC8vIGRlZmluZXMgb2JqZWN0J3MgcHJvdG90eXBlXG4gICAgW1wiX19wcm90b19fXCJdOiBxdXggLy8gZGVmaW5lcyBhIHByb3BlcnR5IG5hbWVkIFwiX19wcm90b19fXCJcbn07In0=)

```
/*eslint no-dupe-keys: "error"*/

const foo = {
    bar: "baz",
    quxx: "qux"
};

const obj = {
    "__proto__": baz, // defines object's prototype
    ["__proto__"]: qux // defines a property named "__proto__"
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
```

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-dupe-keys.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-dupe-keys.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-dupe-keys.md
                    
                
                )
