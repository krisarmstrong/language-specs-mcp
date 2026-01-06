# no-useless-rename

Disallow renaming import, export, and destructured assignments to the same name

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Compatibility](#compatibility)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Resources](#resources)

ES2015 allows for the renaming of references in import and export statements as well as destructuring assignments. This gives programmers a concise syntax for performing these operations while renaming these references:

```
import { foo as bar } from "baz";
export { foo as bar };
let { foo: bar } = baz;
1
2
3
```

Copy code to clipboard

With this syntax, it is possible to rename a reference to the same name. This is a completely redundant operation, as this is the same as not renaming at all. For example, this:

```
import { foo as foo } from "bar";
export { foo as foo };
let { foo: foo } = bar;
1
2
3
```

Copy code to clipboard

is the same as:

```
import { foo } from "bar";
export { foo };
let { foo } = bar;
1
2
3
```

Copy code to clipboard

## Rule Details

This rule disallows the renaming of import, export, and destructured assignments to the same name.

## Options

This rule allows for more fine-grained control with the following options:

- `ignoreImport`: When set to `true`, this rule does not check imports
- `ignoreExport`: When set to `true`, this rule does not check exports
- `ignoreDestructuring`: When set to `true`, this rule does not check destructuring assignments

By default, all options are set to `false`:

```
"no-useless-rename": ["error", {
    "ignoreDestructuring": false,
    "ignoreImport": false,
    "ignoreExport": false
}]
1
2
3
4
5
```

Copy code to clipboard

Examples of incorrect code for this rule by default:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1yZW5hbWU6IFwiZXJyb3JcIiovXG5cbmltcG9ydCB7IGZvbzEgYXMgZm9vMSB9IGZyb20gXCJiYXJcIjtcbmltcG9ydCB7IFwiZm9vMlwiIGFzIGZvbzIgfSBmcm9tIFwiYmFyXCI7XG5leHBvcnQgeyBmb28xIGFzIGZvbzEgfTtcbmV4cG9ydCB7IGZvbzIgYXMgXCJmb28yXCIgfTtcbmV4cG9ydCB7IGZvbzMgYXMgZm9vMyB9IGZyb20gXCJiYXJcIjtcbmV4cG9ydCB7IFwiZm9vNFwiIGFzIFwiZm9vNFwiIH0gZnJvbSBcImJhclwiO1xubGV0IHsgZm9vMzogZm9vMyB9ID0gYmFyO1xubGV0IHsgJ2ZvbzQnOiBmb280IH0gPSBiYXI7XG5mdW5jdGlvbiBmb28oeyBiYXI6IGJhciB9KSB7fVxuKHsgZm9vOiBmb28gfSkgPT4ge30ifQ==)

```
/*eslint no-useless-rename: "error"*/

import { foo1 as foo1 } from "bar";
import { "foo2" as foo2 } from "bar";
export { foo1 as foo1 };
export { foo2 as "foo2" };
export { foo3 as foo3 } from "bar";
export { "foo4" as "foo4" } from "bar";
let { foo3: foo3 } = bar;
let { 'foo4': foo4 } = bar;
function foo({ bar: bar }) {}
({ foo: foo }) => {}
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
```

Examples of correct code for this rule by default:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1yZW5hbWU6IFwiZXJyb3JcIiovXG5cbmltcG9ydCAqIGFzIGZvbzEgZnJvbSBcImZvb1wiO1xuaW1wb3J0IHsgZm9vMiB9IGZyb20gXCJiYXJcIjtcbmltcG9ydCB7IGZvbyBhcyBiYXIxIH0gZnJvbSBcImJhelwiO1xuaW1wb3J0IHsgXCJmb29cIiBhcyBiYXIyIH0gZnJvbSBcImJhelwiO1xuXG5leHBvcnQgeyBmb28gfTtcbmV4cG9ydCB7IGZvbyBhcyBiYXIxIH07XG5leHBvcnQgeyBmb28gYXMgXCJiYXIyXCIgfTtcbmV4cG9ydCB7IGZvbyBhcyBiYXIzIH0gZnJvbSBcImZvb1wiO1xuZXhwb3J0IHsgXCJmb29cIiBhcyBcImJhcjRcIiB9IGZyb20gXCJmb29cIjtcblxubGV0IHsgZm9vIH0gPSBiYXI7XG5sZXQgeyBmb286IGJhciB9ID0gYmF6O1xubGV0IHsgW3F1eF06IHF1eCB9ID0gYmFyO1xuXG5mdW5jdGlvbiBmb28zKHsgYmFyIH0pIHt9XG5mdW5jdGlvbiBmb280KHsgYmFyOiBiYXogfSkge31cblxuKHsgZm9vIH0pID0+IHt9XG4oeyBmb286IGJhciB9KSA9PiB7fSJ9)

```
/*eslint no-useless-rename: "error"*/

import * as foo1 from "foo";
import { foo2 } from "bar";
import { foo as bar1 } from "baz";
import { "foo" as bar2 } from "baz";

export { foo };
export { foo as bar1 };
export { foo as "bar2" };
export { foo as bar3 } from "foo";
export { "foo" as "bar4" } from "foo";

let { foo } = bar;
let { foo: bar } = baz;
let { [qux]: qux } = bar;

function foo3({ bar }) {}
function foo4({ bar: baz }) {}

({ foo }) => {}
({ foo: bar }) => {}
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
```

Examples of correct code for this rule with `{ ignoreImport: true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1yZW5hbWU6IFtcImVycm9yXCIsIHsgaWdub3JlSW1wb3J0OiB0cnVlIH1dKi9cblxuaW1wb3J0IHsgZm9vIGFzIGZvbyB9IGZyb20gXCJiYXJcIjsifQ==)

```
/*eslint no-useless-rename: ["error", { ignoreImport: true }]*/

import { foo as foo } from "bar";
1
2
3
```

Examples of correct code for this rule with `{ ignoreExport: true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1yZW5hbWU6IFtcImVycm9yXCIsIHsgaWdub3JlRXhwb3J0OiB0cnVlIH1dKi9cblxuY29uc3QgZm9vID0gMTtcbmV4cG9ydCB7IGZvbyBhcyBmb28gfTtcbmV4cG9ydCB7IGJhciBhcyBiYXIgfSBmcm9tIFwiYmFyXCI7In0=)

```
/*eslint no-useless-rename: ["error", { ignoreExport: true }]*/

const foo = 1;
export { foo as foo };
export { bar as bar } from "bar";
1
2
3
4
5
```

Examples of correct code for this rule with `{ ignoreDestructuring: true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1yZW5hbWU6IFtcImVycm9yXCIsIHsgaWdub3JlRGVzdHJ1Y3R1cmluZzogdHJ1ZSB9XSovXG5cbmxldCB7IGZvbzogZm9vIH0gPSBiYXI7XG5mdW5jdGlvbiBiYXooeyBiYXI6IGJhciB9KSB7fVxuKHsgZm9vOiBmb28gfSkgPT4ge30ifQ==)

```
/*eslint no-useless-rename: ["error", { ignoreDestructuring: true }]*/

let { foo: foo } = bar;
function baz({ bar: bar }) {}
({ foo: foo }) => {}
1
2
3
4
5
```

## When Not To Use It

You can safely disable this rule if you do not care about redundantly renaming import, export, and destructuring assignments.

## Compatibility

- JSCS: [disallowIdenticalDestructuringNames](https://jscs-dev.github.io/rule/disallowIdenticalDestructuringNames)

## Related Rules

- [object-shorthand](/docs/latest/rules/object-shorthand)

## Version

This rule was introduced in ESLint v2.11.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-rename.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-rename.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-rename.md
                    
                
                )
