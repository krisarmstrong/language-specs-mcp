# valid-typeof

Enforce comparing `typeof` expressions against valid strings

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [requireStringLiterals](#requirestringliterals)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

For a vast majority of use cases, the result of the `typeof` operator is one of the following string literals: `"undefined"`, `"object"`, `"boolean"`, `"number"`, `"string"`, `"function"`, `"symbol"`, and `"bigint"`. It is usually a typing mistake to compare the result of a `typeof` operator to other string literals.

## Rule Details

This rule enforces comparing `typeof` expressions to valid string literals.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFsaWQtdHlwZW9mOiBcImVycm9yXCIqL1xuXG50eXBlb2YgZm9vID09PSBcInN0cm5pZ1wiXG50eXBlb2YgZm9vID09IFwidW5kZWZpbWVkXCJcbnR5cGVvZiBiYXIgIT0gXCJudW5iZXJcIlxudHlwZW9mIGJhciAhPT0gXCJmdWNudGlvblwiIn0=)

```
/*eslint valid-typeof: "error"*/

typeof foo === "strnig"
typeof foo == "undefimed"
typeof bar != "nunber"
typeof bar !== "fucntion"
1
2
3
4
5
6
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFsaWQtdHlwZW9mOiBcImVycm9yXCIqL1xuXG50eXBlb2YgZm9vID09PSBcInN0cmluZ1wiXG50eXBlb2YgYmFyID09IFwidW5kZWZpbmVkXCJcbnR5cGVvZiBmb28gPT09IGJhelxudHlwZW9mIGJhciA9PT0gdHlwZW9mIHF1eCJ9)

```
/*eslint valid-typeof: "error"*/

typeof foo === "string"
typeof bar == "undefined"
typeof foo === baz
typeof bar === typeof qux
1
2
3
4
5
6
```

## Options

This rule has an object option:

- `"requireStringLiterals": true` allows the comparison of `typeof` expressions with only string literals or other `typeof` expressions, and disallows comparisons to any other value. Default is `false`.

### requireStringLiterals

Examples of incorrect code with the `{ "requireStringLiterals": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFsaWQtdHlwZW9mOiBbXCJlcnJvclwiLCB7IFwicmVxdWlyZVN0cmluZ0xpdGVyYWxzXCI6IHRydWUgfV0qL1xuXG50eXBlb2YgZm9vID09PSB1bmRlZmluZWRcbnR5cGVvZiBiYXIgPT0gT2JqZWN0XG50eXBlb2YgYmF6ID09PSBcInN0cm5pZ1wiXG50eXBlb2YgcXV4ID09PSBcInNvbWUgaW52YWxpZCB0eXBlXCJcbnR5cGVvZiBiYXogPT09IGFub3RoZXJWYXJpYWJsZVxudHlwZW9mIGZvbyA9PSA1In0=)

```
/*eslint valid-typeof: ["error", { "requireStringLiterals": true }]*/

typeof foo === undefined
typeof bar == Object
typeof baz === "strnig"
typeof qux === "some invalid type"
typeof baz === anotherVariable
typeof foo == 5
1
2
3
4
5
6
7
8
```

Examples of correct code with the `{ "requireStringLiterals": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdmFsaWQtdHlwZW9mOiBbXCJlcnJvclwiLCB7IFwicmVxdWlyZVN0cmluZ0xpdGVyYWxzXCI6IHRydWUgfV0qL1xuXG50eXBlb2YgZm9vID09PSBcInVuZGVmaW5lZFwiXG50eXBlb2YgYmFyID09IFwib2JqZWN0XCJcbnR5cGVvZiBiYXogPT09IFwic3RyaW5nXCJcbnR5cGVvZiBiYXIgPT09IHR5cGVvZiBxdXgifQ==)

```
/*eslint valid-typeof: ["error", { "requireStringLiterals": true }]*/

typeof foo === "undefined"
typeof bar == "object"
typeof baz === "string"
typeof bar === typeof qux
1
2
3
4
5
6
```

## When Not To Use It

You may want to turn this rule off if you will be using the `typeof` operator on host objects.

## Version

This rule was introduced in ESLint v0.5.0.

## Further Reading

[typeof - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/valid-typeof.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/valid-typeof.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/valid-typeof.md
                    
                
                )
