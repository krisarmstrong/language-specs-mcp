# no-restricted-exports

Disallow specified names in exports

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [restrictedNamedExports](#restrictednamedexports)

    1. [Default exports](#default-exports)

  2. [restrictedNamedExportsPattern](#restrictednamedexportspattern)
  3. [restrictDefaultExports](#restrictdefaultexports)

    1. [direct](#direct)
    2. [named](#named)
    3. [defaultFrom](#defaultfrom)
    4. [namedFrom](#namedfrom)
    5. [namespaceFrom](#namespacefrom)

3. [Known Limitations](#known-limitations)
4. [Version](#version)
5. [Resources](#resources)

In a project, certain names may be disallowed from being used as exported names for various reasons.

## Rule Details

This rule disallows specified names from being used as exported names.

## Options

By default, this rule doesn’t disallow any names. Only the names you specify in the configuration will be disallowed.

This rule has an object option:

- `"restrictedNamedExports"` is an array of strings, where each string is a name to be restricted.
- `"restrictedNamedExportsPattern"` is a string representing a regular expression pattern. Named exports matching this pattern will be restricted. This option does not apply to `default` named exports.
- `"restrictDefaultExports"` is an object option with boolean properties to restrict certain default export declarations. The option works only if the `restrictedNamedExports` option does not contain the `"default"` value. The following properties are allowed: 

  - `direct`: restricts `export default` declarations.
  - `named`: restricts `export { foo as default };` declarations.
  - `defaultFrom`: restricts `export { default } from 'foo';` declarations.
  - `namedFrom`: restricts `export { foo as default } from 'foo';` declarations.
  - `namespaceFrom`: restricts `export * as default from 'foo';` declarations.

### restrictedNamedExports

Examples of incorrect code for the `"restrictedNamedExports"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7XG4gICAgXCJyZXN0cmljdGVkTmFtZWRFeHBvcnRzXCI6IFtcImZvb1wiLCBcImJhclwiLCBcIkJhelwiLCBcImFcIiwgXCJiXCIsIFwiY1wiLCBcImRcIiwgXCJlXCIsIFwi8J+RjVwiXVxufV0qL1xuXG5leHBvcnQgY29uc3QgZm9vID0gMTtcblxuZXhwb3J0IGZ1bmN0aW9uIGJhcigpIHt9XG5cbmV4cG9ydCBjbGFzcyBCYXoge31cblxuY29uc3QgYSA9IHt9O1xuZXhwb3J0IHsgYSB9O1xuXG5mdW5jdGlvbiBzb21lRnVuY3Rpb24oKSB7fVxuZXhwb3J0IHsgc29tZUZ1bmN0aW9uIGFzIGIgfTtcblxuZXhwb3J0IHsgYyB9IGZyb20gXCJzb21lX21vZHVsZVwiO1xuXG5leHBvcnQgeyBcImRcIiB9IGZyb20gXCJzb21lX21vZHVsZVwiO1xuXG5leHBvcnQgeyBzb21ldGhpbmcgYXMgZSB9IGZyb20gXCJzb21lX21vZHVsZVwiO1xuXG5leHBvcnQgeyBcIvCfkY1cIiB9IGZyb20gXCJzb21lX21vZHVsZVwiOyJ9)

```
/*eslint no-restricted-exports: ["error", {
    "restrictedNamedExports": ["foo", "bar", "Baz", "a", "b", "c", "d", "e", "👍"]
}]*/

export const foo = 1;

export function bar() {}

export class Baz {}

const a = {};
export { a };

function someFunction() {}
export { someFunction as b };

export { c } from "some_module";

export { "d" } from "some_module";

export { something as e } from "some_module";

export { "👍" } from "some_module";
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

Examples of correct code for the `"restrictedNamedExports"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7XG4gICAgXCJyZXN0cmljdGVkTmFtZWRFeHBvcnRzXCI6IFtcImZvb1wiLCBcImJhclwiLCBcIkJhelwiLCBcImFcIiwgXCJiXCIsIFwiY1wiLCBcImRcIiwgXCJlXCIsIFwi8J+RjVwiXVxufV0qL1xuXG5leHBvcnQgY29uc3QgcXV1eCA9IDE7XG5cbmV4cG9ydCBmdW5jdGlvbiBteUZ1bmN0aW9uKCkge31cblxuZXhwb3J0IGNsYXNzIE15Q2xhc3Mge31cblxuY29uc3QgYSA9IHt9O1xuZXhwb3J0IHsgYSBhcyBteU9iamVjdCB9O1xuXG5mdW5jdGlvbiBzb21lRnVuY3Rpb24oKSB7fVxuZXhwb3J0IHsgc29tZUZ1bmN0aW9uIH07XG5cbmV4cG9ydCB7IGMgYXMgc29tZU5hbWUgfSBmcm9tIFwic29tZV9tb2R1bGVcIjtcblxuZXhwb3J0IHsgXCJkXCIgYXMgXCIgZCBcIiB9IGZyb20gXCJzb21lX21vZHVsZVwiO1xuXG5leHBvcnQgeyBzb21ldGhpbmcgfSBmcm9tIFwic29tZV9tb2R1bGVcIjtcblxuZXhwb3J0IHsgXCLwn5GNXCIgYXMgdGh1bWJzVXAgfSBmcm9tIFwic29tZV9tb2R1bGVcIjsifQ==)

```
/*eslint no-restricted-exports: ["error", {
    "restrictedNamedExports": ["foo", "bar", "Baz", "a", "b", "c", "d", "e", "👍"]
}]*/

export const quux = 1;

export function myFunction() {}

export class MyClass {}

const a = {};
export { a as myObject };

function someFunction() {}
export { someFunction };

export { c as someName } from "some_module";

export { "d" as " d " } from "some_module";

export { something } from "some_module";

export { "👍" as thumbsUp } from "some_module";
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

#### Default exports

By design, the `"restrictedNamedExports"` option doesn’t disallow `export default` declarations. If you configure `"default"` as a restricted name, that restriction will apply only to named export declarations.

Examples of additional incorrect code for the `"restrictedNamedExports": ["default"]` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3RlZE5hbWVkRXhwb3J0c1wiOiBbXCJkZWZhdWx0XCJdIH1dKi9cblxuZnVuY3Rpb24gZm9vKCkge31cblxuZXhwb3J0IHsgZm9vIGFzIGRlZmF1bHQgfTsifQ==)

```
/*eslint no-restricted-exports: ["error", { "restrictedNamedExports": ["default"] }]*/

function foo() {}

export { foo as default };
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3RlZE5hbWVkRXhwb3J0c1wiOiBbXCJkZWZhdWx0XCJdIH1dKi9cblxuZXhwb3J0IHsgZGVmYXVsdCB9IGZyb20gXCJzb21lX21vZHVsZVwiOyJ9)

```
/*eslint no-restricted-exports: ["error", { "restrictedNamedExports": ["default"] }]*/

export { default } from "some_module";
1
2
3
```

Examples of additional correct code for the `"restrictedNamedExports": ["default"]` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3RlZE5hbWVkRXhwb3J0c1wiOiBbXCJkZWZhdWx0XCIsIFwiZm9vXCJdIH1dKi9cblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gZm9vKCkge30ifQ==)

```
/*eslint no-restricted-exports: ["error", { "restrictedNamedExports": ["default", "foo"] }]*/

export default function foo() {}
1
2
3
```

### restrictedNamedExportsPattern

Example of incorrect code for the `"restrictedNamedExportsPattern"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7XG4gICAgXCJyZXN0cmljdGVkTmFtZWRFeHBvcnRzUGF0dGVyblwiOiBcImJhciRcIlxufV0qL1xuXG5leHBvcnQgY29uc3QgZm9vYmFyID0gMTsifQ==)

```
/*eslint no-restricted-exports: ["error", {
    "restrictedNamedExportsPattern": "bar$"
}]*/

export const foobar = 1;
1
2
3
4
5
```

Example of correct code for the `"restrictedNamedExportsPattern"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7XG4gICAgXCJyZXN0cmljdGVkTmFtZWRFeHBvcnRzUGF0dGVyblwiOiBcImJhciRcIlxufV0qL1xuXG5leHBvcnQgY29uc3QgYWJjID0gMTsifQ==)

```
/*eslint no-restricted-exports: ["error", {
    "restrictedNamedExportsPattern": "bar$"
}]*/

export const abc = 1;
1
2
3
4
5
```

Note that this option does not apply to `export default` or any `default` named exports. If you want to also restrict `default` exports, use the `restrictDefaultExports` option.

### restrictDefaultExports

This option allows you to restrict certain `default` declarations. The option works only if the `restrictedNamedExports` option does not contain the `"default"` value. This option accepts the following properties:

#### direct

Examples of incorrect code for the `"restrictDefaultExports": { "direct": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwiZGlyZWN0XCI6IHRydWUgfSB9XSovXG5cbmV4cG9ydCBkZWZhdWx0IGZvbzsifQ==)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "direct": true } }]*/

export default foo;
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwiZGlyZWN0XCI6IHRydWUgfSB9XSovXG5cbmV4cG9ydCBkZWZhdWx0IDQyOyJ9)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "direct": true } }]*/

export default 42;
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwiZGlyZWN0XCI6IHRydWUgfSB9XSovXG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIGZvbygpIHt9In0=)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "direct": true } }]*/

export default function foo() {}
1
2
3
```

#### named

Examples of incorrect code for the `"restrictDefaultExports": { "named": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwibmFtZWRcIjogdHJ1ZSB9IH1dKi9cblxuY29uc3QgZm9vID0gMTIzO1xuXG5leHBvcnQgeyBmb28gYXMgZGVmYXVsdCB9OyJ9)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "named": true } }]*/

const foo = 123;

export { foo as default };
1
2
3
4
5
```

#### defaultFrom

Examples of incorrect code for the `"restrictDefaultExports": { "defaultFrom": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwiZGVmYXVsdEZyb21cIjogdHJ1ZSB9IH1dKi9cblxuZXhwb3J0IHsgZGVmYXVsdCB9IGZyb20gJ2Zvbyc7In0=)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "defaultFrom": true } }]*/

export { default } from 'foo';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwiZGVmYXVsdEZyb21cIjogdHJ1ZSB9IH1dKi9cblxuZXhwb3J0IHsgZGVmYXVsdCBhcyBkZWZhdWx0IH0gZnJvbSAnZm9vJzsifQ==)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "defaultFrom": true } }]*/

export { default as default } from 'foo';
1
2
3
```

#### namedFrom

Examples of incorrect code for the `"restrictDefaultExports": { "namedFrom": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwibmFtZWRGcm9tXCI6IHRydWUgfSB9XSovXG5cbmV4cG9ydCB7IGZvbyBhcyBkZWZhdWx0IH0gZnJvbSAnZm9vJzsifQ==)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "namedFrom": true } }]*/

export { foo as default } from 'foo';
1
2
3
```

#### namespaceFrom

Examples of incorrect code for the `"restrictDefaultExports": { "namespaceFrom": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1leHBvcnRzOiBbXCJlcnJvclwiLCB7IFwicmVzdHJpY3REZWZhdWx0RXhwb3J0c1wiOiB7IFwibmFtZXNwYWNlRnJvbVwiOiB0cnVlIH0gfV0qL1xuXG5leHBvcnQgKiBhcyBkZWZhdWx0IGZyb20gJ2Zvbyc7In0=)

```
/*eslint no-restricted-exports: ["error", { "restrictDefaultExports": { "namespaceFrom": true } }]*/

export * as default from 'foo';
1
2
3
```

## Known Limitations

This rule doesn’t inspect the content of source modules in re-export declarations. In particular, if you are re-exporting everything from another module’s export, that export may include a restricted name. This rule cannot detect such cases.

```

//----- some_module.js -----
export function foo() {}

//----- my_module.js -----
/*eslint no-restricted-exports: ["error", { "restrictedNamedExports": ["foo"] }]*/

export * from "some_module"; // allowed, although this declaration exports "foo" from my_module
1
2
3
4
5
6
7
8
```

Copy code to clipboard

## Version

This rule was introduced in ESLint v7.0.0-alpha.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-restricted-exports.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-restricted-exports.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-restricted-exports.md
                    
                
                )
