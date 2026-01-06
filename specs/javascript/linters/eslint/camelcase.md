# camelcase

Enforce camelcase naming convention

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [properties: “always”](#properties-always)
  2. [properties: “never”](#properties-never)
  3. [ignoreDestructuring: false](#ignoredestructuring-false)
  4. [ignoreDestructuring: true](#ignoredestructuring-true)
  5. [ignoreImports: false](#ignoreimports-false)
  6. [ignoreImports: true](#ignoreimports-true)
  7. [ignoreGlobals: false](#ignoreglobals-false)
  8. [ignoreGlobals: true](#ignoreglobals-true)
  9. [allow](#allow)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

When it comes to naming variables, style guides generally fall into one of two camps: camelcase (`variableName`) and underscores (`variable_name`). This rule focuses on using the camelcase approach. If your style guide calls for camelCasing your variable names, then this rule is for you!

## Rule Details

This rule looks for any underscores (`_`) located within the source code. It ignores leading and trailing underscores and only checks those in the middle of a variable name. If ESLint decides that the variable is a constant (all uppercase), then no warning will be thrown. Otherwise, a warning will be thrown. This rule only flags definitions and assignments but not function calls. In case of ES6 `import` statements, this rule only targets the name of the variable that will be imported into the local module scope.

## Options

This rule has an object option:

- `"properties": "always"` (default) enforces camelcase style for property names
- `"properties": "never"` does not check property names
- `"ignoreDestructuring": false` (default) enforces camelcase style for destructured identifiers
- `"ignoreDestructuring": true` does not check destructured identifiers (but still checks any use of those identifiers later in the code)
- `"ignoreImports": false` (default) enforces camelcase style for ES2015 imports
- `"ignoreImports": true` does not check ES2015 imports (but still checks any use of the imports later in the code except function arguments)
- `"ignoreGlobals": false` (default) enforces camelcase style for global variables
- `"ignoreGlobals": true` does not enforce camelcase style for global variables
- `allow` (`string[]`) list of properties to accept. Accept regex.

### properties: “always”

Examples of incorrect code for this rule with the default `{ "properties": "always" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBcImVycm9yXCIqL1xuXG5pbXBvcnQgeyBub19jYW1lbGNhc2VkIH0gZnJvbSBcImV4dGVybmFsLW1vZHVsZVwiXG5cbmNvbnN0IG15X2Zhdm9yaXRlX2NvbG9yID0gXCIjMTEyQzg1XCI7XG5cbmZ1bmN0aW9uIGRvX3NvbWV0aGluZygpIHtcbiAgICAvLyAuLi5cbn1cblxub2JqLmRvX3NvbWV0aGluZyA9IGZ1bmN0aW9uKCkge1xuICAgIC8vIC4uLlxufTtcblxuZnVuY3Rpb24gZm9vKHsgbm9fY2FtZWxjYXNlZCB9KSB7XG4gICAgLy8gLi4uXG59O1xuXG5mdW5jdGlvbiBiYXIoeyBpc0NhbWVsY2FzZWQ6IG5vX2NhbWVsY2FzZWQgfSkge1xuICAgIC8vIC4uLlxufVxuXG5mdW5jdGlvbiBiYXooeyBub19jYW1lbGNhc2VkID0gJ2RlZmF1bHQgdmFsdWUnIH0pIHtcbiAgICAvLyAuLi5cbn07XG5cbmNvbnN0IG9iaiA9IHtcbiAgICBteV9wcmVmOiAxXG59O1xuXG5jb25zdCB7IGNhdGVnb3J5X2lkID0gMSB9ID0gcXVlcnk7XG5cbmNvbnN0IHsgZm9vOiBzbmFrZV9jYXNlZCB9ID0gYmFyO1xuXG5jb25zdCB7IGZvbzogYmFyX2JheiA9IDEgfSA9IHF1ejsifQ==)

```
/*eslint camelcase: "error"*/

import { no_camelcased } from "external-module"

const my_favorite_color = "#112C85";

function do_something() {
    // ...
}

obj.do_something = function() {
    // ...
};

function foo({ no_camelcased }) {
    // ...
};

function bar({ isCamelcased: no_camelcased }) {
    // ...
}

function baz({ no_camelcased = 'default value' }) {
    // ...
};

const obj = {
    my_pref: 1
};

const { category_id = 1 } = query;

const { foo: snake_cased } = bar;

const { foo: bar_baz = 1 } = quz;
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

Examples of correct code for this rule with the default `{ "properties": "always" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBcImVycm9yXCIqL1xuXG5pbXBvcnQgeyBub19jYW1lbGNhc2VkIGFzIGNhbWVsQ2FzZWQgfSBmcm9tIFwiZXh0ZXJuYWwtbW9kdWxlXCI7XG5cbmNvbnN0IG15RmF2b3JpdGVDb2xvciAgID0gXCIjMTEyQzg1XCI7XG5jb25zdCBfbXlGYXZvcml0ZUNvbG9yICA9IFwiIzExMkM4NVwiO1xuY29uc3QgbXlGYXZvcml0ZUNvbG9yXyAgPSBcIiMxMTJDODVcIjtcbmNvbnN0IE1ZX0ZBVk9SSVRFX0NPTE9SID0gXCIjMTEyQzg1XCI7XG5jb25zdCBmb28xID0gYmFyLmJhel9ib29tO1xuY29uc3QgZm9vMiA9IHsgcXV4OiBiYXIuYmF6X2Jvb20gfTtcblxub2JqLmRvX3NvbWV0aGluZygpO1xuZG9fc29tZXRoaW5nKCk7XG5uZXcgZG9fc29tZXRoaW5nKCk7XG5cbmNvbnN0IHsgY2F0ZWdvcnlfaWQ6IGNhdGVnb3J5IH0gPSBxdWVyeTtcblxuZnVuY3Rpb24gZm9vKHsgaXNDYW1lbENhc2VkIH0pIHtcbiAgICAvLyAuLi5cbn07XG5cbmZ1bmN0aW9uIGJhcih7IGlzQ2FtZWxDYXNlZDogaXNBbHNvQ2FtZWxDYXNlZCB9KSB7XG4gICAgLy8gLi4uXG59XG5cbmZ1bmN0aW9uIGJheih7IGlzQ2FtZWxDYXNlZCA9ICdkZWZhdWx0IHZhbHVlJyB9KSB7XG4gICAgLy8gLi4uXG59O1xuXG5jb25zdCB7IGNhdGVnb3J5SWQgPSAxIH0gPSBxdWVyeTtcblxuY29uc3QgeyBmb286IGlzQ2FtZWxDYXNlZCB9ID0gYmFyO1xuXG5jb25zdCB7IGZvbzogY2FtZWxDYXNlZE5hbWUgPSAxIH0gPSBxdXo7XG4ifQ==)

```
/*eslint camelcase: "error"*/

import { no_camelcased as camelCased } from "external-module";

const myFavoriteColor   = "#112C85";
const _myFavoriteColor  = "#112C85";
const myFavoriteColor_  = "#112C85";
const MY_FAVORITE_COLOR = "#112C85";
const foo1 = bar.baz_boom;
const foo2 = { qux: bar.baz_boom };

obj.do_something();
do_something();
new do_something();

const { category_id: category } = query;

function foo({ isCamelCased }) {
    // ...
};

function bar({ isCamelCased: isAlsoCamelCased }) {
    // ...
}

function baz({ isCamelCased = 'default value' }) {
    // ...
};

const { categoryId = 1 } = query;

const { foo: isCamelCased } = bar;

const { foo: camelCasedName = 1 } = quz;

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

### properties: “never”

Examples of correct code for this rule with the `{ "properties": "never" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7cHJvcGVydGllczogXCJuZXZlclwifV0qL1xuXG5jb25zdCBvYmogPSB7XG4gICAgbXlfcHJlZjogMVxufTtcblxub2JqLmZvb19iYXIgPSBcImJhelwiOyJ9)

```
/*eslint camelcase: ["error", {properties: "never"}]*/

const obj = {
    my_pref: 1
};

obj.foo_bar = "baz";
1
2
3
4
5
6
7
```

### ignoreDestructuring: false

Examples of incorrect code for this rule with the default `{ "ignoreDestructuring": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBcImVycm9yXCIqL1xuXG5jb25zdCB7IGNhdGVnb3J5X2lkIH0gPSBxdWVyeTtcblxuY29uc3QgeyBjYXRlZ29yeV9uYW1lID0gMSB9ID0gcXVlcnk7XG5cbmNvbnN0IHsgY2F0ZWdvcnlfaWQ6IGNhdGVnb3J5X3RpdGxlIH0gPSBxdWVyeTtcblxuY29uc3QgeyBjYXRlZ29yeV9pZDogY2F0ZWdvcnlfYWxpYXMgfSA9IHF1ZXJ5O1xuXG5jb25zdCB7IGNhdGVnb3J5X2lkOiBjYXRlZ29yeUlkLCAuLi5vdGhlcl9wcm9wcyB9ID0gcXVlcnk7In0=)

```
/*eslint camelcase: "error"*/

const { category_id } = query;

const { category_name = 1 } = query;

const { category_id: category_title } = query;

const { category_id: category_alias } = query;

const { category_id: categoryId, ...other_props } = query;
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

Examples of incorrect code for this rule with the `{ "ignoreDestructuring": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlRGVzdHJ1Y3R1cmluZzogdHJ1ZX1dKi9cblxuY29uc3QgeyBjYXRlZ29yeV9pZDogY2F0ZWdvcnlfYWxpYXMgfSA9IHF1ZXJ5O1xuXG5jb25zdCB7IGNhdGVnb3J5X2lkLCAuLi5vdGhlcl9wcm9wcyB9ID0gcXVlcnk7In0=)

```
/*eslint camelcase: ["error", {ignoreDestructuring: true}]*/

const { category_id: category_alias } = query;

const { category_id, ...other_props } = query;
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "ignoreDestructuring": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlRGVzdHJ1Y3R1cmluZzogdHJ1ZX1dKi9cblxuY29uc3QgeyBjYXRlZ29yeV9pZCB9ID0gcXVlcnk7XG5cbmNvbnN0IHsgY2F0ZWdvcnlfbmFtZSA9IDEgfSA9IHF1ZXJ5O1xuXG5jb25zdCB7IGNhdGVnb3J5X2lkX25hbWU6IGNhdGVnb3J5X2lkX25hbWUgfSA9IHF1ZXJ5OyJ9)

```
/*eslint camelcase: ["error", {ignoreDestructuring: true}]*/

const { category_id } = query;

const { category_name = 1 } = query;

const { category_id_name: category_id_name } = query;
1
2
3
4
5
6
7
```

Please note that this option applies only to identifiers inside destructuring patterns. It doesn’t additionally allow any particular use of the created variables later in the code apart from the use that is already allowed by default or by other options.

Examples of additional incorrect code for this rule with the `{ "ignoreDestructuring": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlRGVzdHJ1Y3R1cmluZzogdHJ1ZX1dKi9cblxuY29uc3QgeyBzb21lX3Byb3BlcnR5IH0gPSBvYmo7IC8vIGFsbG93ZWQgYnkge2lnbm9yZURlc3RydWN0dXJpbmc6IHRydWV9XG5jb25zdCBmb28gPSBzb21lX3Byb3BlcnR5ICsgMTsgLy8gZXJyb3IsIGlnbm9yZURlc3RydWN0dXJpbmcgZG9lcyBub3QgYXBwbHkgdG8gdGhpcyBzdGF0ZW1lbnQifQ==)

```
/*eslint camelcase: ["error", {ignoreDestructuring: true}]*/

const { some_property } = obj; // allowed by {ignoreDestructuring: true}
const foo = some_property + 1; // error, ignoreDestructuring does not apply to this statement
1
2
3
4
```

A common use case for this option is to avoid useless renaming when the identifier is not intended to be used later in the code.

Examples of additional correct code for this rule with the `{ "ignoreDestructuring": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlRGVzdHJ1Y3R1cmluZzogdHJ1ZX1dKi9cblxuY29uc3QgeyBzb21lX3Byb3BlcnR5LCAuLi5yZXN0IH0gPSBvYmo7XG4vLyBkbyBzb21ldGhpbmcgd2l0aCAncmVzdCcsIG5vdGhpbmcgd2l0aCAnc29tZV9wcm9wZXJ0eScifQ==)

```
/*eslint camelcase: ["error", {ignoreDestructuring: true}]*/

const { some_property, ...rest } = obj;
// do something with 'rest', nothing with 'some_property'
1
2
3
4
```

Another common use case for this option is in combination with `{ "properties": "never" }`, when the identifier is intended to be used only as a property shorthand.

Examples of additional correct code for this rule with the `{ "properties": "never", "ignoreDestructuring": true }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7XCJwcm9wZXJ0aWVzXCI6IFwibmV2ZXJcIiwgaWdub3JlRGVzdHJ1Y3R1cmluZzogdHJ1ZX1dKi9cblxuY29uc3QgeyBzb21lX3Byb3BlcnR5IH0gPSBvYmo7XG5kb1NvbWV0aGluZyh7IHNvbWVfcHJvcGVydHkgfSk7In0=)

```
/*eslint camelcase: ["error", {"properties": "never", ignoreDestructuring: true}]*/

const { some_property } = obj;
doSomething({ some_property });
1
2
3
4
```

### ignoreImports: false

Examples of incorrect code for this rule with the default `{ "ignoreImports": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBcImVycm9yXCIqL1xuXG5pbXBvcnQgeyBzbmFrZV9jYXNlZCB9IGZyb20gJ21vZCc7In0=)

```
/*eslint camelcase: "error"*/

import { snake_cased } from 'mod';
1
2
3
```

### ignoreImports: true

Examples of incorrect code for this rule with the `{ "ignoreImports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlSW1wb3J0czogdHJ1ZX1dKi9cblxuaW1wb3J0IGRlZmF1bHRfaW1wb3J0IGZyb20gJ21vZCc7XG5cbmltcG9ydCAqIGFzIG5hbWVzcGFjZWRfaW1wb3J0IGZyb20gJ21vZCc7In0=)

```
/*eslint camelcase: ["error", {ignoreImports: true}]*/

import default_import from 'mod';

import * as namespaced_import from 'mod';
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "ignoreImports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlSW1wb3J0czogdHJ1ZX1dKi9cblxuaW1wb3J0IHsgc25ha2VfY2FzZWQgfSBmcm9tICdtb2QnOyJ9)

```
/*eslint camelcase: ["error", {ignoreImports: true}]*/

import { snake_cased } from 'mod';
1
2
3
```

### ignoreGlobals: false

Examples of incorrect code for this rule with the default `{ "ignoreGlobals": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlR2xvYmFsczogZmFsc2V9XSovXG4vKiBnbG9iYWwgbm9fY2FtZWxjYXNlZCAqL1xuXG5jb25zdCBmb28gPSBub19jYW1lbGNhc2VkOyJ9)

```
/*eslint camelcase: ["error", {ignoreGlobals: false}]*/
/* global no_camelcased */

const foo = no_camelcased;
1
2
3
4
```

### ignoreGlobals: true

Examples of correct code for this rule with the `{ "ignoreGlobals": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7aWdub3JlR2xvYmFsczogdHJ1ZX1dKi9cbi8qIGdsb2JhbCBub19jYW1lbGNhc2VkICovXG5cbmNvbnN0IGZvbyA9IG5vX2NhbWVsY2FzZWQ7In0=)

```
/*eslint camelcase: ["error", {ignoreGlobals: true}]*/
/* global no_camelcased */

const foo = no_camelcased;
1
2
3
4
```

### allow

Examples of correct code for this rule with the `allow` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7YWxsb3c6IFtcIlVOU0FGRV9jb21wb25lbnRXaWxsTW91bnRcIl19XSovXG5cbmZ1bmN0aW9uIFVOU0FGRV9jb21wb25lbnRXaWxsTW91bnQoKSB7XG4gICAgLy8gLi4uXG59In0=)

```
/*eslint camelcase: ["error", {allow: ["UNSAFE_componentWillMount"]}]*/

function UNSAFE_componentWillMount() {
    // ...
}
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2FtZWxjYXNlOiBbXCJlcnJvclwiLCB7YWxsb3c6IFtcIl5VTlNBRkVfXCJdfV0qL1xuXG5mdW5jdGlvbiBVTlNBRkVfY29tcG9uZW50V2lsbE1vdW50KCkge1xuICAgIC8vIC4uLlxufVxuXG5mdW5jdGlvbiBVTlNBRkVfY29tcG9uZW50V2lsbFJlY2VpdmVQcm9wcygpIHtcbiAgICAvLyAuLi5cbn0ifQ==)

```
/*eslint camelcase: ["error", {allow: ["^UNSAFE_"]}]*/

function UNSAFE_componentWillMount() {
    // ...
}

function UNSAFE_componentWillReceiveProps() {
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

## When Not To Use It

If you have established coding standards using a different naming convention (separating words with underscores), turn this rule off.

## Version

This rule was introduced in ESLint v0.0.2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/camelcase.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/camelcase.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/camelcase.md
                    
                
                )
