# no-restricted-imports

Disallow specified modules when loaded by `import`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [paths](#paths)

    1. [importNames](#importnames)
    2. [allowImportNames](#allowimportnames)
    3. [allowTypeImports (TypeScript only)](#allowtypeimports-typescript-only)

  2. [patterns](#patterns)

    1. [group](#group)
    2. [regex](#regex)
    3. [caseSensitive](#casesensitive)
    4. [importNames](#importnames-1)
    5. [allowImportNames](#allowimportnames-1)
    6. [importNamePattern](#importnamepattern)
    7. [allowImportNamePattern](#allowimportnamepattern)
    8. [allowTypeImports (TypeScript only)](#allowtypeimports-typescript-only-1)

3. [Known Limitations](#known-limitations)
4. [When Not To Use It](#when-not-to-use-it)
5. [Version](#version)
6. [Resources](#resources)

Imports are an ES6/ES2015 standard for making the functionality of other modules available in your current module. In CommonJS this is implemented through the `require()` call which makes this ESLint rule roughly equivalent to its CommonJS counterpart `no-restricted-modules`.

Why would you want to restrict imports?

- 

Some imports might not make sense in a particular environment. For example, Node.js’ `fs` module would not make sense in an environment that didn’t have a file system.

- 

Some modules provide similar or identical functionality, think `lodash` and `underscore`. Your project may have standardized on a module. You want to make sure that the other alternatives are not being used as this would unnecessarily bloat the project and provide a higher maintenance cost of two dependencies when one would suffice.

## Rule Details

This rule allows you to specify imports that you don’t want to use in your application.

It applies to static imports only, not dynamic ones.

## Options

This rule has both string and object options to specify the imported modules to restrict.

Using string option, you can specify the name of a module that you want to restrict from being imported as a value in the rule options array:

```
"no-restricted-imports": ["error", "import1", "import2"]
1
```

Copy code to clipboard

Examples of incorrect code for string option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCBcImZzXCJdKi9cblxuaW1wb3J0IGZzIGZyb20gJ2ZzJzsifQ==)

```
/*eslint no-restricted-imports: ["error", "fs"]*/

import fs from 'fs';
1
2
3
```

String options also restrict the module from being exported, as in this example:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCBcImZzXCJdKi9cblxuZXhwb3J0IHsgZnMgfSBmcm9tICdmcyc7In0=)

```
/*eslint no-restricted-imports: ["error", "fs"]*/

export { fs } from 'fs';
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCBcImZzXCJdKi9cblxuZXhwb3J0ICogZnJvbSAnZnMnOyJ9)

```
/*eslint no-restricted-imports: ["error", "fs"]*/

export * from 'fs';
1
2
3
```

Examples of correct code for string option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCBcImZzXCJdKi9cblxuaW1wb3J0IGNyeXB0byBmcm9tICdjcnlwdG8nO1xuZXhwb3J0IHsgZm9vIH0gZnJvbSBcImJhclwiOyJ9)

```
/*eslint no-restricted-imports: ["error", "fs"]*/

import crypto from 'crypto';
export { foo } from "bar";
1
2
3
4
```

You may also specify a custom message for a particular module using the `name` and `message` properties inside an object, where the value of the `name` is the name of the module and `message` property contains the custom message. (The custom message is appended to the default error message from the rule.)

```
"no-restricted-imports": ["error", {
    "name": "import-foo",
    "message": "Please use import-bar instead."
}, {
    "name": "import-baz",
    "message": "Please use import-quux instead."
}]
1
2
3
4
5
6
7
```

Copy code to clipboard

Examples of incorrect code for string option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7XG4gICAgXCJuYW1lXCI6IFwiZGlzYWxsb3dlZC1pbXBvcnRcIixcbiAgICBcIm1lc3NhZ2VcIjogXCJQbGVhc2UgdXNlICdhbGxvd2VkLWltcG9ydCcgaW5zdGVhZFwiXG59XSovXG5cbmltcG9ydCBmb28gZnJvbSAnZGlzYWxsb3dlZC1pbXBvcnQnOyJ9)

```
/*eslint no-restricted-imports: ["error", {
    "name": "disallowed-import",
    "message": "Please use 'allowed-import' instead"
}]*/

import foo from 'disallowed-import';
1
2
3
4
5
6
```

### paths

This is an object option whose value is an array containing the names of the modules you want to restrict.

```
"no-restricted-imports": ["error", { "paths": ["import1", "import2"] }]
1
```

Copy code to clipboard

Examples of incorrect code for `paths`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0aHNcIjogW1wiY2x1c3RlclwiXSB9XSovXG5cbmltcG9ydCBjbHVzdGVyIGZyb20gJ2NsdXN0ZXInOyJ9)

```
/*eslint no-restricted-imports: ["error", { "paths": ["cluster"] }]*/

import cluster from 'cluster';
1
2
3
```

Custom messages for a particular module can also be specified in `paths` array using objects with `name` and `message`.

```
"no-restricted-imports": ["error", {
    "paths": [{
        "name": "import-foo",
        "message": "Please use import-bar instead."
    }, {
        "name": "import-baz",
        "message": "Please use import-quux instead."
    }]
}]
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

Copy code to clipboard

#### importNames

This option in `paths` is an array and can be used to specify the names of certain bindings exported from a module. Import names specified inside `paths` array affect the module specified in the `name` property of corresponding object, so it is required to specify the `name` property first when you are using `importNames` or `message` option.

Specifying `"default"` string inside the `importNames` array will restrict the default export from being imported.

```
"no-restricted-imports": ["error", {
  "paths": [{
    "name": "import-foo",
    "importNames": ["Bar"],
    "message": "Please use Bar from /import-bar/baz/ instead."
  }]
}]
1
2
3
4
5
6
7
```

Copy code to clipboard

Examples of incorrect code when `importNames` in `paths` has `"default"`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiZm9vXCIsXG4gICAgaW1wb3J0TmFtZXM6IFtcImRlZmF1bHRcIl0sXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgdXNlIHRoZSBkZWZhdWx0IGltcG9ydCBmcm9tICcvYmFyL2Jhei8nIGluc3RlYWQuXCJcbn1dfV0qL1xuXG5pbXBvcnQgRGlzYWxsb3dlZE9iamVjdCBmcm9tIFwiZm9vXCI7In0=)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "foo",
    importNames: ["default"],
    message: "Please use the default import from '/bar/baz/' instead."
}]}]*/

import DisallowedObject from "foo";
1
2
3
4
5
6
7
```

Examples of incorrect code for `importNames` in `paths`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiZm9vXCIsXG4gICAgaW1wb3J0TmFtZXM6IFtcIkRpc2FsbG93ZWRPYmplY3RcIl0sXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgaW1wb3J0ICdEaXNhbGxvd2VkT2JqZWN0JyBmcm9tICcvYmFyL2Jhei8nIGluc3RlYWQuXCJcbn1dfV0qL1xuXG5pbXBvcnQgeyBEaXNhbGxvd2VkT2JqZWN0IH0gZnJvbSBcImZvb1wiO1xuXG5pbXBvcnQgeyBEaXNhbGxvd2VkT2JqZWN0IGFzIEFsbG93ZWRPYmplY3QgfSBmcm9tIFwiZm9vXCI7XG5cbmltcG9ydCB7IFwiRGlzYWxsb3dlZE9iamVjdFwiIGFzIFNvbWVPYmplY3QgfSBmcm9tIFwiZm9vXCI7In0=)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "foo",
    importNames: ["DisallowedObject"],
    message: "Please import 'DisallowedObject' from '/bar/baz/' instead."
}]}]*/

import { DisallowedObject } from "foo";

import { DisallowedObject as AllowedObject } from "foo";

import { "DisallowedObject" as SomeObject } from "foo";
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

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiZm9vXCIsXG4gICAgaW1wb3J0TmFtZXM6IFtcIkRpc2FsbG93ZWRPYmplY3RcIl0sXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgaW1wb3J0ICdEaXNhbGxvd2VkT2JqZWN0JyBmcm9tICcvYmFyL2Jhei8nIGluc3RlYWQuXCJcbn1dfV0qL1xuXG5pbXBvcnQgKiBhcyBGb28gZnJvbSBcImZvb1wiOyJ9)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "foo",
    importNames: ["DisallowedObject"],
    message: "Please import 'DisallowedObject' from '/bar/baz/' instead."
}]}]*/

import * as Foo from "foo";
1
2
3
4
5
6
7
```

Examples of correct code for `importNames` in `paths`:

If the local name assigned to a default export is the same as a string in `importNames`, this will not cause an error.

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbeyBuYW1lOiBcImZvb1wiLCBpbXBvcnROYW1lczogW1wiRGlzYWxsb3dlZE9iamVjdFwiXSB9XSB9XSovXG5cbmltcG9ydCBEaXNhbGxvd2VkT2JqZWN0IGZyb20gXCJmb29cIiJ9)

```
/*eslint no-restricted-imports: ["error", { paths: [{ name: "foo", importNames: ["DisallowedObject"] }] }]*/

import DisallowedObject from "foo"
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiZm9vXCIsXG4gICAgaW1wb3J0TmFtZXM6IFtcIkRpc2FsbG93ZWRPYmplY3RcIl0sXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgaW1wb3J0ICdEaXNhbGxvd2VkT2JqZWN0JyBmcm9tICcvYmFyL2Jhei8nIGluc3RlYWQuXCJcbn1dfV0qL1xuXG5pbXBvcnQgeyBBbGxvd2VkT2JqZWN0IGFzIERpc2FsbG93ZWRPYmplY3QgfSBmcm9tIFwiZm9vXCI7In0=)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "foo",
    importNames: ["DisallowedObject"],
    message: "Please import 'DisallowedObject' from '/bar/baz/' instead."
}]}]*/

import { AllowedObject as DisallowedObject } from "foo";
1
2
3
4
5
6
7
```

#### allowImportNames

This option is an array. Inverse of `importNames`, `allowImportNames` allows the imports that are specified inside this array. So it restricts all imports from a module, except specified allowed ones.

Note: `allowImportNames` cannot be used in combination with `importNames`.

```
"no-restricted-imports": ["error", {
  "paths": [{
    "name": "import-foo",
    "allowImportNames": ["Bar"],
    "message": "Please use only Bar from import-foo."
  }]
}]
1
2
3
4
5
6
7
```

Copy code to clipboard

Examples of incorrect code for `allowImportNames` in `paths`:

Disallowing all import names except ‘AllowedObject’.

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiZm9vXCIsXG4gICAgYWxsb3dJbXBvcnROYW1lczogW1wiQWxsb3dlZE9iamVjdFwiXSxcbiAgICBtZXNzYWdlOiBcIlBsZWFzZSB1c2Ugb25seSAnQWxsb3dlZE9iamVjdCcgZnJvbSAnZm9vJy5cIlxufV19XSovXG5cbmltcG9ydCB7IERpc2FsbG93ZWRPYmplY3QgfSBmcm9tIFwiZm9vXCI7In0=)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "foo",
    allowImportNames: ["AllowedObject"],
    message: "Please use only 'AllowedObject' from 'foo'."
}]}]*/

import { DisallowedObject } from "foo";
1
2
3
4
5
6
7
```

Examples of correct code for `allowImportNames` in `paths`:

Disallowing all import names except ‘AllowedObject’.

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiZm9vXCIsXG4gICAgYWxsb3dJbXBvcnROYW1lczogW1wiQWxsb3dlZE9iamVjdFwiXSxcbiAgICBtZXNzYWdlOiBcIk9ubHkgdXNlICdBbGxvd2VkT2JqZWN0JyBmcm9tICdmb28nLlwiXG59XX1dKi9cblxuaW1wb3J0IHsgQWxsb3dlZE9iamVjdCB9IGZyb20gXCJmb29cIjsifQ==)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "foo",
    allowImportNames: ["AllowedObject"],
    message: "Only use 'AllowedObject' from 'foo'."
}]}]*/

import { AllowedObject } from "foo";
1
2
3
4
5
6
7
```

#### allowTypeImports (TypeScript only)

Whether to allow [Type-Only Imports](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export) for a path. This includes type-only `export` statements, as they are equivalent to re-exporting an `import`. Default: `false`.

Examples of incorrect code for `allowTypeImports` in `paths`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiaW1wb3J0LWZvb1wiLFxuICAgIGFsbG93VHlwZUltcG9ydHM6IHRydWUsXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgdXNlIG9ubHkgdHlwZS1vbmx5IGltcG9ydHMgZnJvbSAnaW1wb3J0LWZvbycuXCJcbn1dfV0qL1xuXG5pbXBvcnQgZm9vIGZyb20gJ2ltcG9ydC1mb28nO1xuZXhwb3J0IHsgRm9vIH0gZnJvbSAnaW1wb3J0LWZvbyc7In0=)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "import-foo",
    allowTypeImports: true,
    message: "Please use only type-only imports from 'import-foo'."
}]}]*/

import foo from 'import-foo';
export { Foo } from 'import-foo';
1
2
3
4
5
6
7
8
```

Examples of correct code for `allowTypeImports` in `paths`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiaW1wb3J0LWZvb1wiLFxuICAgIGFsbG93VHlwZUltcG9ydHM6IHRydWUsXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgdXNlIG9ubHkgdHlwZS1vbmx5IGltcG9ydHMgZnJvbSAnaW1wb3J0LWZvbycuXCJcbn1dfV0qL1xuXG5pbXBvcnQgdHlwZSBmb28gZnJvbSAnaW1wb3J0LWZvbyc7XG5leHBvcnQgdHlwZSB7IEZvbyB9IGZyb20gJ2ltcG9ydC1mb28nO1xuXG5pbXBvcnQgdHlwZSBmb28gPSByZXF1aXJlKFwiaW1wb3J0LWZvb1wiKTsifQ==)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "import-foo",
    allowTypeImports: true,
    message: "Please use only type-only imports from 'import-foo'."
}]}]*/

import type foo from 'import-foo';
export type { Foo } from 'import-foo';

import type foo = require("import-foo");
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

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdGhzOiBbe1xuICAgIG5hbWU6IFwiaW1wb3J0LWZvb1wiLFxuXHRpbXBvcnROYW1lczogW1wiQmF6XCJdLFxuICAgIGFsbG93VHlwZUltcG9ydHM6IHRydWUsXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgdXNlICdCYXonIGZyb20gJ2ltcG9ydC1mb28nIGFzIGEgdHlwZSBvbmx5LlwiXG59XX1dKi9cblxuaW1wb3J0IHsgQmFyLCB0eXBlIEJheiB9IGZyb20gXCJpbXBvcnQtZm9vXCI7In0=)

```
/*eslint no-restricted-imports: ["error", { paths: [{
    name: "import-foo",
	importNames: ["Baz"],
    allowTypeImports: true,
    message: "Please use 'Baz' from 'import-foo' as a type only."
}]}]*/

import { Bar, type Baz } from "import-foo";
1
2
3
4
5
6
7
8
```

### patterns

This is also an object option whose value is an array. This option allows you to specify multiple modules to restrict using `gitignore`-style patterns or regular expressions.

Where `paths` option takes exact import paths, `patterns` option can be used to specify the import paths with more flexibility, allowing for the restriction of multiple modules within the same directory. For example:

```
"no-restricted-imports": ["error", {
  "paths": [{
    "name": "import-foo",
  }]
}]
1
2
3
4
5
```

Copy code to clipboard

This configuration restricts import of the `import-foo` module but wouldn’t restrict the import of `import-foo/bar` or `import-foo/baz`. You can use `patterns` to restrict both:

```
"no-restricted-imports": ["error", {
    "paths": [{
      "name": "import-foo",
    }],
    "patterns": [{
      "group": ["import-foo/ba*"],
    }]
}]
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

This configuration restricts imports not just from `import-foo` using `path`, but also `import-foo/bar` and `import-foo/baz` using `patterns`.

To re-include a module when using `gitignore-`style patterns, add a negation (`!`) mark before the pattern. (Make sure these negated patterns are placed last in the array, as order matters)

```
"no-restricted-imports": ["error", {
    "patterns": ["import1/private/*", "import2/*", "!import2/good"]
}]
1
2
3
```

Copy code to clipboard

You can also use regular expressions to restrict modules (see the [regex option](#regex)).

Examples of incorrect code for `patterns` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0dGVybnNcIjogW1wibG9kYXNoLypcIl0gfV0qL1xuXG5pbXBvcnQgcGljayBmcm9tICdsb2Rhc2gvcGljayc7In0=)

```
/*eslint no-restricted-imports: ["error", { "patterns": ["lodash/*"] }]*/

import pick from 'lodash/pick';
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0dGVybnNcIjogW1wibG9kYXNoLypcIiwgXCIhbG9kYXNoL3BpY2tcIl0gfV0qL1xuXG5pbXBvcnQgcGljayBmcm9tICdsb2Rhc2gvbWFwJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { "patterns": ["lodash/*", "!lodash/pick"] }]*/

import pick from 'lodash/map';
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0dGVybnNcIjogW1wiaW1wb3J0MS8qXCIsIFwiIWltcG9ydDEvcHJpdmF0ZS8qXCJdIH1dKi9cblxuaW1wb3J0IHBpY2sgZnJvbSAnaW1wb3J0MS9wcml2YXRlL3NvbWVNb2R1bGUnOyJ9)

```
/*eslint no-restricted-imports: ["error", { "patterns": ["import1/*", "!import1/private/*"] }]*/

import pick from 'import1/private/someModule';
1
2
3
```

In this example, `"!import1/private/*"` is not reincluding the modules inside `private` because the negation mark (`!`) does not reinclude the files if it’s parent directory is excluded by a pattern. In this case, `import1/private` directory is already excluded by the `import1/*` pattern. (The excluded directory can be reincluded using `"!import1/private"`.)

Examples of correct code for `patterns` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0dGVybnNcIjogW1wiY3J5cHRvLypcIl0gfV0qL1xuXG5pbXBvcnQgY3J5cHRvIGZyb20gJ2NyeXB0byc7In0=)

```
/*eslint no-restricted-imports: ["error", { "patterns": ["crypto/*"] }]*/

import crypto from 'crypto';
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0dGVybnNcIjogW1wibG9kYXNoLypcIiwgXCIhbG9kYXNoL3BpY2tcIl0gfV0qL1xuXG5pbXBvcnQgcGljayBmcm9tICdsb2Rhc2gvcGljayc7In0=)

```
/*eslint no-restricted-imports: ["error", { "patterns": ["lodash/*", "!lodash/pick"] }]*/

import pick from 'lodash/pick';
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwicGF0dGVybnNcIjogW1wiaW1wb3J0MS8qXCIsIFwiIWltcG9ydDEvcHJpdmF0ZVwiXSB9XSovXG5cbmltcG9ydCBwaWNrIGZyb20gJ2ltcG9ydDEvcHJpdmF0ZS9zb21lTW9kdWxlJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { "patterns": ["import1/*", "!import1/private"] }]*/

import pick from 'import1/private/someModule';
1
2
3
```

#### group

The `patterns` array can also include objects. The `group` property is used to specify the `gitignore`-style patterns for restricting modules and the `message` property is used to specify a custom message.

Either of the `group` or `regex` properties is required when using the `patterns` option.

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "group": ["import1/private/*"],
      "message": "usage of import1 private modules not allowed."
    }, {
      "group": ["import2/*", "!import2/good"],
      "message": "import2 is deprecated, except the modules in import2/good."
    }]
}]
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

Copy code to clipboard

Examples of incorrect code for `group` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJsb2Rhc2gvKlwiXSxcbiAgICBtZXNzYWdlOiBcIlBsZWFzZSB1c2UgdGhlIGRlZmF1bHQgaW1wb3J0IGZyb20gJ2xvZGFzaCcgaW5zdGVhZC5cIlxufV19XSovXG5cbmltcG9ydCBwaWNrIGZyb20gJ2xvZGFzaC9waWNrJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["lodash/*"],
    message: "Please use the default import from 'lodash' instead."
}]}]*/

import pick from 'lodash/pick';
1
2
3
4
5
6
```

Examples of correct code for this `group` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJsb2Rhc2gvKlwiXSxcbiAgICBtZXNzYWdlOiBcIlBsZWFzZSB1c2UgdGhlIGRlZmF1bHQgaW1wb3J0IGZyb20gJ2xvZGFzaCcgaW5zdGVhZC5cIlxufV19XSovXG5cbmltcG9ydCBsb2Rhc2ggZnJvbSAnbG9kYXNoJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["lodash/*"],
    message: "Please use the default import from 'lodash' instead."
}]}]*/

import lodash from 'lodash';
1
2
3
4
5
6
```

#### regex

The `regex` property is used to specify the regex patterns for restricting modules.

Note: `regex` cannot be used in combination with `group`.

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "regex": "import1/private/",
      "message": "usage of import1 private modules not allowed."
    }, {
      "regex": "import2/(?!good)",
      "message": "import2 is deprecated, except the modules in import2/good."
    }]
}]
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

Copy code to clipboard

Examples of incorrect code for `regex` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIHJlZ2V4OiBcIkBhcHAvKD8hKGFwaS9lbnVtcyQpKS4qXCIsXG59XX1dKi9cblxuaW1wb3J0IEZvbyBmcm9tICdAYXBwL2FwaSc7XG5pbXBvcnQgQmFyIGZyb20gJ0BhcHAvYXBpL2Jhcic7XG5pbXBvcnQgQmF6IGZyb20gJ0BhcHAvYXBpL2Jheic7XG5pbXBvcnQgQnV4IGZyb20gJ0BhcHAvYXBpL2VudW1zL2Zvbyc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    regex: "@app/(?!(api/enums$)).*",
}]}]*/

import Foo from '@app/api';
import Bar from '@app/api/bar';
import Baz from '@app/api/baz';
import Bux from '@app/api/enums/foo';
1
2
3
4
5
6
7
8
```

Examples of correct code for `regex` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIHJlZ2V4OiBcIkBhcHAvKD8hKGFwaS9lbnVtcyQpKS4qXCIsXG59XX1dKi9cblxuaW1wb3J0IEZvbyBmcm9tICdAYXBwL2FwaS9lbnVtcyc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    regex: "@app/(?!(api/enums$)).*",
}]}]*/

import Foo from '@app/api/enums';
1
2
3
4
5
```

#### caseSensitive

This is a boolean option and sets the patterns specified in the `group` or `regex` properties to be case-sensitive when `true`. Default is `false`.

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "group": ["import1/private/prefix[A-Z]*"],
      "caseSensitive": true
    }]
}]
1
2
3
4
5
6
```

Copy code to clipboard

Examples of incorrect code for `caseSensitive: true` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJmb29bQS1aXSpcIl0sXG4gICAgY2FzZVNlbnNpdGl2ZTogdHJ1ZVxufV19XSovXG5cbmltcG9ydCBwaWNrIGZyb20gJ2Zvb0Jhcic7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["foo[A-Z]*"],
    caseSensitive: true
}]}]*/

import pick from 'fooBar';
1
2
3
4
5
6
```

Examples of correct code for `caseSensitive: true` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJmb29bQS1aXSpcIl0sXG4gICAgY2FzZVNlbnNpdGl2ZTogdHJ1ZVxufV19XSovXG5cbmltcG9ydCBwaWNrIGZyb20gJ2Zvb2QnOyJ9)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["foo[A-Z]*"],
    caseSensitive: true
}]}]*/

import pick from 'food';
1
2
3
4
5
6
```

#### importNames

You can also specify `importNames` within objects inside the `patterns` array. In this case, the specified names apply only to the associated `group` or `regex` property.

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "group": ["utils/*"],
      "importNames": ["isEmpty"],
      "message": "Use 'isEmpty' from lodash instead."
    }]
}]
1
2
3
4
5
6
7
```

Copy code to clipboard

Examples of incorrect code for `importNames` in `patterns`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGltcG9ydE5hbWVzOiBbJ2lzRW1wdHknXSxcbiAgICBtZXNzYWdlOiBcIlVzZSAnaXNFbXB0eScgZnJvbSBsb2Rhc2ggaW5zdGVhZC5cIlxufV19XSovXG5cbmltcG9ydCB7IGlzRW1wdHkgfSBmcm9tICd1dGlscy9jb2xsZWN0aW9uLXV0aWxzJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    importNames: ['isEmpty'],
    message: "Use 'isEmpty' from lodash instead."
}]}]*/

import { isEmpty } from 'utils/collection-utils';
1
2
3
4
5
6
7
```

Examples of correct code for `importNames` in `patterns`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGltcG9ydE5hbWVzOiBbJ2lzRW1wdHknXSxcbiAgICBtZXNzYWdlOiBcIlVzZSAnaXNFbXB0eScgZnJvbSBsb2Rhc2ggaW5zdGVhZC5cIlxufV19XSovXG5cbmltcG9ydCB7IGhhc1ZhbHVlcyB9IGZyb20gJ3V0aWxzL2NvbGxlY3Rpb24tdXRpbHMnOyJ9)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    importNames: ['isEmpty'],
    message: "Use 'isEmpty' from lodash instead."
}]}]*/

import { hasValues } from 'utils/collection-utils';
1
2
3
4
5
6
7
```

#### allowImportNames

You can also specify `allowImportNames` within objects inside the `patterns` array. In this case, the specified names apply only to the associated `group` or `regex` property.

Note: `allowImportNames` cannot be used in combination with `importNames`, `importNamePattern` or `allowImportNamePattern`.

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "group": ["utils/*"],
      "allowImportNames": ["isEmpty"],
      "message": "Please use only 'isEmpty' from utils."
    }]
}]
1
2
3
4
5
6
7
```

Copy code to clipboard

Examples of incorrect code for `allowImportNames` in `patterns`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGFsbG93SW1wb3J0TmFtZXM6IFsnaXNFbXB0eSddLFxuICAgIG1lc3NhZ2U6IFwiUGxlYXNlIHVzZSBvbmx5ICdpc0VtcHR5JyBmcm9tIHV0aWxzLlwiXG59XX1dKi9cblxuaW1wb3J0IHsgaGFzVmFsdWVzIH0gZnJvbSAndXRpbHMvY29sbGVjdGlvbi11dGlscyc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    allowImportNames: ['isEmpty'],
    message: "Please use only 'isEmpty' from utils."
}]}]*/

import { hasValues } from 'utils/collection-utils';
1
2
3
4
5
6
7
```

Examples of correct code for `allowImportNames` in `patterns`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGFsbG93SW1wb3J0TmFtZXM6IFsnaXNFbXB0eSddLFxuICAgIG1lc3NhZ2U6IFwiUGxlYXNlIHVzZSBvbmx5ICdpc0VtcHR5JyBmcm9tIHV0aWxzLlwiXG59XX1dKi9cblxuaW1wb3J0IHsgaXNFbXB0eSB9IGZyb20gJ3V0aWxzL2NvbGxlY3Rpb24tdXRpbHMnOyJ9)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    allowImportNames: ['isEmpty'],
    message: "Please use only 'isEmpty' from utils."
}]}]*/

import { isEmpty } from 'utils/collection-utils';
1
2
3
4
5
6
7
```

#### importNamePattern

This option allows you to use regex patterns to restrict import names:

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "group": ["import-foo/*"],
      "importNamePattern": "^foo",
    }]
}]
1
2
3
4
5
6
```

Copy code to clipboard

Examples of incorrect code for `importNamePattern` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGltcG9ydE5hbWVQYXR0ZXJuOiAnXmlzJyxcbiAgICBtZXNzYWdlOiBcIlVzZSAnaXMqJyBmdW5jdGlvbnMgZnJvbSBsb2Rhc2ggaW5zdGVhZC5cIlxufV19XSovXG5cbmltcG9ydCB7IGlzRW1wdHkgfSBmcm9tICd1dGlscy9jb2xsZWN0aW9uLXV0aWxzJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    importNamePattern: '^is',
    message: "Use 'is*' functions from lodash instead."
}]}]*/

import { isEmpty } from 'utils/collection-utils';
1
2
3
4
5
6
7
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJmb28vKlwiXSxcbiAgICBpbXBvcnROYW1lUGF0dGVybjogJ14oaXN8aGFzKScsXG4gICAgbWVzc2FnZTogXCJVc2UgJ2lzKicgYW5kICdoYXMqJyBmdW5jdGlvbnMgZnJvbSBiYXovYmFyIGluc3RlYWRcIlxufV19XSovXG5cbmltcG9ydCB7IGlzU29tZXRoaW5nLCBoYXNTb21ldGhpbmcgfSBmcm9tICdmb28vYmFyJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["foo/*"],
    importNamePattern: '^(is|has)',
    message: "Use 'is*' and 'has*' functions from baz/bar instead"
}]}]*/

import { isSomething, hasSomething } from 'foo/bar';
1
2
3
4
5
6
7
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJmb28vKlwiXSxcbiAgICBpbXBvcnROYW1lczogW1wiYmFyXCJdLFxuICAgIGltcG9ydE5hbWVQYXR0ZXJuOiAnXmJheicsXG59XX1dKi9cblxuaW1wb3J0IHsgYmFyLCBiYXpRdXggfSBmcm9tICdmb28vcXV1eCc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["foo/*"],
    importNames: ["bar"],
    importNamePattern: '^baz',
}]}]*/

import { bar, bazQux } from 'foo/quux';
1
2
3
4
5
6
7
```

Examples of correct code for `importNamePattern` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGltcG9ydE5hbWVQYXR0ZXJuOiAnXmlzJyxcbiAgICBtZXNzYWdlOiBcIlVzZSAnaXMqJyBmdW5jdGlvbnMgZnJvbSBsb2Rhc2ggaW5zdGVhZC5cIlxufV19XSovXG5cbmltcG9ydCBpc0VtcHR5LCB7IGhhc1ZhbHVlIH0gZnJvbSAndXRpbHMvY29sbGVjdGlvbi11dGlscyc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    importNamePattern: '^is',
    message: "Use 'is*' functions from lodash instead."
}]}]*/

import isEmpty, { hasValue } from 'utils/collection-utils';
1
2
3
4
5
6
7
```

You can also use this option to allow only side-effect imports by setting it to a pattern that matches any name, such as `^`.

Examples of incorrect code for `importNamePattern` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGltcG9ydE5hbWVQYXR0ZXJuOiBcIl5cIlxufV19XSovXG5cbmltcG9ydCBpc0VtcHR5LCB7IGhhc1ZhbHVlIH0gZnJvbSAndXRpbHMvY29sbGVjdGlvbi11dGlscyc7XG5cbmltcG9ydCAqIGFzIGZpbGUgZnJvbSAndXRpbHMvZmlsZS11dGlscyc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    importNamePattern: "^"
}]}]*/

import isEmpty, { hasValue } from 'utils/collection-utils';

import * as file from 'utils/file-utils';
1
2
3
4
5
6
7
8
```

Examples of correct code for `importNamePattern` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGltcG9ydE5hbWVQYXR0ZXJuOiBcIl5cIlxufV19XSovXG5cbmltcG9ydCAndXRpbHMvaW5pdC11dGlscyc7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    importNamePattern: "^"
}]}]*/

import 'utils/init-utils';
1
2
3
4
5
6
```

#### allowImportNamePattern

This is a string option. Inverse of `importNamePattern`, this option allows imports that matches the specified regex pattern. So it restricts all imports from a module, except specified allowed patterns.

Note: `allowImportNamePattern` cannot be used in combination with `importNames`, `importNamePattern` or `allowImportNames`.

```
"no-restricted-imports": ["error", {
    "patterns": [{
      "group": ["import-foo/*"],
      "allowImportNamePattern": "^foo",
    }]
}]
1
2
3
4
5
6
```

Copy code to clipboard

Examples of incorrect code for `allowImportNamePattern` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGFsbG93SW1wb3J0TmFtZVBhdHRlcm46ICdeaGFzJ1xufV19XSovXG5cbmltcG9ydCB7IGlzRW1wdHkgfSBmcm9tICd1dGlscy9jb2xsZWN0aW9uLXV0aWxzJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    allowImportNamePattern: '^has'
}]}]*/

import { isEmpty } from 'utils/collection-utils';
1
2
3
4
5
6
```

Examples of correct code for `allowImportNamePattern` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJ1dGlscy8qXCJdLFxuICAgIGFsbG93SW1wb3J0TmFtZVBhdHRlcm46ICdeaXMnXG59XX1dKi9cblxuaW1wb3J0IHsgaXNFbXB0eSB9IGZyb20gJ3V0aWxzL2NvbGxlY3Rpb24tdXRpbHMnOyJ9)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["utils/*"],
    allowImportNamePattern: '^is'
}]}]*/

import { isEmpty } from 'utils/collection-utils';
1
2
3
4
5
6
```

#### allowTypeImports (TypeScript only)

Whether to allow [Type-Only Imports](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export) for a path. This includes type-only `export` statements, as they are equivalent to re-exporting an `import`. Default: `false`.

```
"no-restricted-imports": ["error", {
  "patterns": [{
    "group": ["import/private/*"],
    "allowTypeImports": true,
  }]
}]
1
2
3
4
5
6
```

Copy code to clipboard

Examples of incorrect code for `allowTypeImports` in `patterns`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJpbXBvcnQvcHJpdmF0ZS8qXCJdLFxuICAgIGFsbG93VHlwZUltcG9ydHM6IHRydWUsXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgdXNlIG9ubHkgdHlwZS1vbmx5IGltcG9ydHMgZnJvbSAnaW1wb3J0L3ByaXZhdGUvKicuXCJcbn1dfV0qL1xuXG5pbXBvcnQgeyBmb28gfSBmcm9tICdpbXBvcnQvcHJpdmF0ZS9iYXInO1xuZXhwb3J0IHsgZm9vIH0gZnJvbSAnaW1wb3J0L3ByaXZhdGUvYmFyJzsifQ==)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["import/private/*"],
    allowTypeImports: true,
    message: "Please use only type-only imports from 'import/private/*'."
}]}]*/

import { foo } from 'import/private/bar';
export { foo } from 'import/private/bar';
1
2
3
4
5
6
7
8
```

Examples of correct code for `allowTypeImports` in `patterns`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJpbXBvcnQvcHJpdmF0ZS8qXCJdLFxuICAgIGFsbG93VHlwZUltcG9ydHM6IHRydWUsXG4gICAgbWVzc2FnZTogXCJQbGVhc2UgdXNlIG9ubHkgdHlwZS1vbmx5IGltcG9ydHMgZnJvbSAnaW1wb3J0L3ByaXZhdGUvKicuXCJcbn1dfV0qL1xuXG5pbXBvcnQgdHlwZSB7IGZvbyB9IGZyb20gJ2ltcG9ydC9wcml2YXRlL2Jhcic7XG5leHBvcnQgdHlwZSB7IGZvbyB9IGZyb20gJ2ltcG9ydC9wcml2YXRlL2Jhcic7XG5cbmltcG9ydCB0eXBlIGZvbyA9IHJlcXVpcmUoXCJpbXBvcnQvcHJpdmF0ZS9iYXJcIik7In0=)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["import/private/*"],
    allowTypeImports: true,
    message: "Please use only type-only imports from 'import/private/*'."
}]}]*/

import type { foo } from 'import/private/bar';
export type { foo } from 'import/private/bar';

import type foo = require("import/private/bar");
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

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IHBhdHRlcm5zOiBbe1xuICAgIGdyb3VwOiBbXCJpbXBvcnQvcHJpdmF0ZS8qXCJdLFxuICAgIGltcG9ydE5hbWVzOiBbXCJCYXpcIl0sXG4gICAgYWxsb3dUeXBlSW1wb3J0czogdHJ1ZSxcbiAgICBtZXNzYWdlOiBcIlBsZWFzZSB1c2UgJ0JheicgZnJvbSAnaW1wb3J0L3ByaXZhdGUvKicgYXMgYSB0eXBlIG9ubHkuXCJcbn1dfV0qL1xuXG5pbXBvcnQgeyBCYXIsIHR5cGUgQmF6IH0gZnJvbSBcImltcG9ydC9wcml2YXRlL2JhclwiOyJ9)

```
/*eslint no-restricted-imports: ["error", { patterns: [{
    group: ["import/private/*"],
    importNames: ["Baz"],
    allowTypeImports: true,
    message: "Please use 'Baz' from 'import/private/*' as a type only."
}]}]*/

import { Bar, type Baz } from "import/private/bar";
1
2
3
4
5
6
7
8
```

## Known Limitations

TypeScript [import = require() syntax](https://www.typescriptlang.org/docs/handbook/2/modules.html#es-module-syntax-with-commonjs-behavior) is valid and the rule can recognize and lint such instances, but with certain limitations.

You can only fully restrict these imports, you cannot restrict them based on specific import names like `importNames`, `allowImportNames`, `importNamePattern`, or `allowImportNamePattern` options.

Examples of incorrect code for TypeScript import equals declarations:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCBcImRpc2FsbG93ZWQtaW1wb3J0XCJdKi9cblxuaW1wb3J0IGZvbyA9IHJlcXVpcmUoXCJkaXNhbGxvd2VkLWltcG9ydFwiKTsifQ==)

```
/*eslint no-restricted-imports: ["error", "disallowed-import"]*/

import foo = require("disallowed-import");
1
2
3
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFxuICBcInBhdGhzXCI6IFt7IFwibmFtZVwiOiBcImRpc2FsbG93ZWQtaW1wb3J0XCIgfV0gXG59XSovXG5cbmltcG9ydCBmb28gPSByZXF1aXJlKFwiZGlzYWxsb3dlZC1pbXBvcnRcIik7In0=)

```
/*eslint no-restricted-imports: ["error", { 
  "paths": [{ "name": "disallowed-import" }] 
}]*/

import foo = require("disallowed-import");
1
2
3
4
5
```

Note: Import name restrictions do not apply to TypeScript import equals declarations. The following configuration will not restrict the import equals declaration:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIiwicGFyc2VyIjoiQHR5cGVzY3JpcHQtZXNsaW50L3BhcnNlciIsInBhcnNlck9wdGlvbnMiOnsiZWNtYUZlYXR1cmVzIjp7ImpzeCI6dHJ1ZX0sInNvdXJjZVR5cGUiOiJtb2R1bGUifX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFxuICBcInBhdGhzXCI6IFt7IFxuICAgIFwibmFtZVwiOiBcImZvb1wiLFxuICAgIFwiaW1wb3J0TmFtZXNcIjogW1wiZm9vXCJdXG4gIH1dIFxufV0qL1xuXG4vLyBUaGlzIGltcG9ydCBlcXVhbHMgZGVjbGFyYXRpb24gd2lsbCBOT1QgYmUgcmVzdHJpY3RlZFxuLy8gZXZlbiB0aG91Z2ggaXQgaW1wb3J0cyB0aGUgZW50aXJlIG1vZHVsZVxuaW1wb3J0IGZvbyA9IHJlcXVpcmUoXCJmb29cIik7In0=)

```
/*eslint no-restricted-imports: ["error", { 
  "paths": [{ 
    "name": "foo",
    "importNames": ["foo"]
  }] 
}]*/

// This import equals declaration will NOT be restricted
// even though it imports the entire module
import foo = require("foo");
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

## When Not To Use It

Don’t use this rule or don’t include a module in the list for this rule if you want to be able to import a module in your project without an ESLint error or warning.

## Version

This rule was introduced in ESLint v2.0.0-alpha-1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-restricted-imports.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-restricted-imports.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-restricted-imports.md
                    
                
                )
