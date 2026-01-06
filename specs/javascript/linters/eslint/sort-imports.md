# sort-imports

Enforce sorted `import` declarations within modules

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [Examples](#examples)

  1. [Default settings](#default-settings)
  2. [ignoreCase](#ignorecase)
  3. [ignoreDeclarationSort](#ignoredeclarationsort)
  4. [ignoreMemberSort](#ignoremembersort)
  5. [memberSyntaxSortOrder](#membersyntaxsortorder)
  6. [allowSeparatedGroups](#allowseparatedgroups)

4. [When Not To Use It](#when-not-to-use-it)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Resources](#resources)

The `import` statement is used to import members (functions, objects or primitives) that have been exported from an external module. Using a specific member syntax:

```
// single - Import single member.
import myMember from "my-module.js";
import {myOtherMember} from "my-other-module.js";

// multiple - Import multiple members.
import {foo, bar} from "my-module.js";

// all - Import all members, where myModule contains all the exported bindings.
import * as myModule from "my-module.js";
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

The `import` statement can also import a module without exported bindings. Used when the module does not export anything, but runs it own code or changes the global context object.

```
// none - Import module without exported bindings.
import "my-module.js"
1
2
```

Copy code to clipboard

When declaring multiple imports, a sorted list of `import` declarations make it easier for developers to read the code and find necessary imports later. This rule is purely a matter of style.

## Rule Details

This rule checks all `import` declarations and verifies that all imports are first sorted by the used member syntax and then alphabetically by the first member or alias name.

The `--fix` option on the command line automatically fixes some problems reported by this rule: multiple members on a single line are automatically sorted (e.g. `import { b, a } from 'foo.js'` is corrected to `import { a, b } from 'foo.js'`), but multiple lines are not reordered.

## Options

This rule accepts an object with its properties as

- `ignoreCase` (default: `false`)
- `ignoreDeclarationSort` (default: `false`)
- `ignoreMemberSort` (default: `false`)
- `memberSyntaxSortOrder` (default: `["none", "all", "multiple", "single"]`); all 4 items must be present in the array, but you can change the order: 

  - `none` = import module without exported bindings.
  - `all` = import all members provided by exported bindings.
  - `multiple` = import multiple members.
  - `single` = import single member.

- `allowSeparatedGroups` (default: `false`)

Default option settings are:

```
{
    "sort-imports": ["error", {
        "ignoreCase": false,
        "ignoreDeclarationSort": false,
        "ignoreMemberSort": false,
        "memberSyntaxSortOrder": ["none", "all", "multiple", "single"],
        "allowSeparatedGroups": false
    }]
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

Copy code to clipboard

## Examples

### Default settings

Examples of correct code for this rule when using default options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0ICdtb2R1bGUtd2l0aG91dC1leHBvcnQuanMnO1xuaW1wb3J0ICogYXMgYmFyIGZyb20gJ2Jhci5qcyc7XG5pbXBvcnQgKiBhcyBmb28gZnJvbSAnZm9vLmpzJztcbmltcG9ydCB7YWxwaGEsIGJldGF9IGZyb20gJ2FscGhhLmpzJztcbmltcG9ydCB7ZGVsdGEsIGdhbW1hfSBmcm9tICdkZWx0YS5qcyc7XG5pbXBvcnQgYSBmcm9tICdiYXouanMnO1xuaW1wb3J0IHtifSBmcm9tICdxdXguanMnOyJ9)

```
/*eslint sort-imports: "error"*/
import 'module-without-export.js';
import * as bar from 'bar.js';
import * as foo from 'foo.js';
import {alpha, beta} from 'alpha.js';
import {delta, gamma} from 'delta.js';
import a from 'baz.js';
import {b} from 'qux.js';
1
2
3
4
5
6
7
8
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IGEgZnJvbSAnZm9vLmpzJztcbmltcG9ydCBiIGZyb20gJ2Jhci5qcyc7XG5pbXBvcnQgYyBmcm9tICdiYXouanMnOyJ9)

```
/*eslint sort-imports: "error"*/
import a from 'foo.js';
import b from 'bar.js';
import c from 'baz.js';
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0ICdmb28uanMnXG5pbXBvcnQgKiBhcyBiYXIgZnJvbSAnYmFyLmpzJztcbmltcG9ydCB7YSwgYn0gZnJvbSAnYmF6LmpzJztcbmltcG9ydCBjIGZyb20gJ3F1eC5qcyc7XG5pbXBvcnQge2R9IGZyb20gJ3F1dXguanMnOyJ9)

```
/*eslint sort-imports: "error"*/
import 'foo.js'
import * as bar from 'bar.js';
import {a, b} from 'baz.js';
import c from 'qux.js';
import {d} from 'quux.js';
1
2
3
4
5
6
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IHthLCBiLCBjfSBmcm9tICdmb28uanMnIn0=)

```
/*eslint sort-imports: "error"*/
import {a, b, c} from 'foo.js'
1
2
```

Examples of incorrect code for this rule when using default options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IGIgZnJvbSAnZm9vLmpzJztcbmltcG9ydCBhIGZyb20gJ2Jhci5qcyc7In0=)

```
/*eslint sort-imports: "error"*/
import b from 'foo.js';
import a from 'bar.js';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IGEgZnJvbSAnZm9vLmpzJztcbmltcG9ydCBBIGZyb20gJ2Jhci5qcyc7In0=)

```
/*eslint sort-imports: "error"*/
import a from 'foo.js';
import A from 'bar.js';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IHtjLCBkfSBmcm9tICdmb28uanMnO1xuaW1wb3J0IHthLCBifSBmcm9tICdiYXIuanMnOyJ9)

```
/*eslint sort-imports: "error"*/
import {c, d} from 'foo.js';
import {a, b} from 'bar.js';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IGEgZnJvbSAnZm9vLmpzJztcbmltcG9ydCB7YiwgY30gZnJvbSAnYmFyLmpzJzsifQ==)

```
/*eslint sort-imports: "error"*/
import a from 'foo.js';
import {b, c} from 'bar.js';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IHthfSBmcm9tICdmb28uanMnO1xuaW1wb3J0IHtiLCBjfSBmcm9tICdiYXIuanMnOyJ9)

```
/*eslint sort-imports: "error"*/
import {a} from 'foo.js';
import {b, c} from 'bar.js';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IGEgZnJvbSAnZm9vLmpzJztcbmltcG9ydCAqIGFzIGIgZnJvbSAnYmFyLmpzJzsifQ==)

```
/*eslint sort-imports: "error"*/
import a from 'foo.js';
import * as b from 'bar.js';
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IHtiLCBhLCBjfSBmcm9tICdmb28uanMnIn0=)

```
/*eslint sort-imports: "error"*/
import {b, a, c} from 'foo.js'
1
2
```

### `ignoreCase`

When `false` (default), uppercase letters of the alphabet must always precede lowercase letters.

When `true`, the rule ignores the case-sensitivity of the imports local name.

Examples of incorrect code for this rule with the default `{ "ignoreCase": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2FzZVwiOiBmYWxzZSB9XSovXG5pbXBvcnQgYSBmcm9tICdiYXIuanMnO1xuaW1wb3J0IEIgZnJvbSAnZm9vLmpzJztcbmltcG9ydCBjIGZyb20gJ2Jhei5qcyc7In0=)

```
/*eslint sort-imports: ["error", { "ignoreCase": false }]*/
import a from 'bar.js';
import B from 'foo.js';
import c from 'baz.js';
1
2
3
4
```

Examples of correct code for this rule with the default `{ "ignoreCase": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2FzZVwiOiBmYWxzZSB9XSovXG5pbXBvcnQgQiBmcm9tICdiYXIuanMnO1xuaW1wb3J0IGEgZnJvbSAnZm9vLmpzJztcbmltcG9ydCBjIGZyb20gJ2Jhei5qcyc7In0=)

```
/*eslint sort-imports: ["error", { "ignoreCase": false }]*/
import B from 'bar.js';
import a from 'foo.js';
import c from 'baz.js';
1
2
3
4
```

Examples of correct code for this rule with `{ "ignoreCase": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2FzZVwiOiB0cnVlIH1dKi9cbmltcG9ydCBhIGZyb20gJ2Jhci5qcyc7XG5pbXBvcnQgQiBmcm9tICdmb28uanMnO1xuaW1wb3J0IGMgZnJvbSAnYmF6LmpzJzsifQ==)

```
/*eslint sort-imports: ["error", { "ignoreCase": true }]*/
import a from 'bar.js';
import B from 'foo.js';
import c from 'baz.js';
1
2
3
4
```

Examples of incorrect code for this rule with the `{ "ignoreCase": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2FzZVwiOiB0cnVlIH1dKi9cbmltcG9ydCBCIGZyb20gJ2Zvby5qcyc7XG5pbXBvcnQgYSBmcm9tICdiYXIuanMnOyJ9)

```
/*eslint sort-imports: ["error", { "ignoreCase": true }]*/
import B from 'foo.js';
import a from 'bar.js';
1
2
3
```

### `ignoreDeclarationSort`

When `true`, the rule ignores the sorting of import declaration statements. Default is `false`.

Examples of incorrect code for this rule with the default `{ "ignoreDeclarationSort": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlRGVjbGFyYXRpb25Tb3J0XCI6IGZhbHNlIH1dKi9cbmltcG9ydCBiIGZyb20gJ2Zvby5qcydcbmltcG9ydCBhIGZyb20gJ2Jhci5qcycifQ==)

```
/*eslint sort-imports: ["error", { "ignoreDeclarationSort": false }]*/
import b from 'foo.js'
import a from 'bar.js'
1
2
3
```

Examples of correct code for this rule with the default `{ "ignoreDeclarationSort": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlRGVjbGFyYXRpb25Tb3J0XCI6IGZhbHNlIH1dKi9cbmltcG9ydCBhIGZyb20gJ2Jhci5qcyc7XG5pbXBvcnQgYiBmcm9tICdmb28uanMnOyJ9)

```
/*eslint sort-imports: ["error", { "ignoreDeclarationSort": false }]*/
import a from 'bar.js';
import b from 'foo.js';
1
2
3
```

Examples of correct code for this rule with the `{ "ignoreDeclarationSort": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlRGVjbGFyYXRpb25Tb3J0XCI6IHRydWUgfV0qL1xuaW1wb3J0IGIgZnJvbSAnZm9vLmpzJ1xuaW1wb3J0IGEgZnJvbSAnYmFyLmpzJyJ9)

```
/*eslint sort-imports: ["error", { "ignoreDeclarationSort": true }]*/
import b from 'foo.js'
import a from 'bar.js'
1
2
3
```

Examples of incorrect code for this rule with the `{ "ignoreDeclarationSort": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlRGVjbGFyYXRpb25Tb3J0XCI6IHRydWUgfV0qL1xuaW1wb3J0IHtiLCBhLCBjfSBmcm9tICdmb28uanMnOyJ9)

```
/*eslint sort-imports: ["error", { "ignoreDeclarationSort": true }]*/
import {b, a, c} from 'foo.js';
1
2
```

### `ignoreMemberSort`

When `true`, the rule ignores the member sorting within a `multiple` member import declaration. Default is `false`.

Examples of incorrect code for this rule with the default `{ "ignoreMemberSort": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTWVtYmVyU29ydFwiOiBmYWxzZSB9XSovXG5pbXBvcnQge2IsIGEsIGN9IGZyb20gJ2Zvby5qcycifQ==)

```
/*eslint sort-imports: ["error", { "ignoreMemberSort": false }]*/
import {b, a, c} from 'foo.js'
1
2
```

Examples of correct code for this rule with the default `{ "ignoreMemberSort": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTWVtYmVyU29ydFwiOiBmYWxzZSB9XSovXG5pbXBvcnQge2EsIGIsIGN9IGZyb20gJ2Zvby5qcyc7In0=)

```
/*eslint sort-imports: ["error", { "ignoreMemberSort": false }]*/
import {a, b, c} from 'foo.js';
1
2
```

Examples of correct code for this rule with the `{ "ignoreMemberSort": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTWVtYmVyU29ydFwiOiB0cnVlIH1dKi9cbmltcG9ydCB7YiwgYSwgY30gZnJvbSAnZm9vLmpzJyJ9)

```
/*eslint sort-imports: ["error", { "ignoreMemberSort": true }]*/
import {b, a, c} from 'foo.js'
1
2
```

Examples of incorrect code for this rule with the `{ "ignoreMemberSort": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTWVtYmVyU29ydFwiOiB0cnVlIH1dKi9cbmltcG9ydCBiIGZyb20gJ2Zvby5qcyc7XG5pbXBvcnQgYSBmcm9tICdiYXIuanMnOyJ9)

```
/*eslint sort-imports: ["error", { "ignoreMemberSort": true }]*/
import b from 'foo.js';
import a from 'bar.js';
1
2
3
```

### `memberSyntaxSortOrder`

This option takes an array with four predefined elements, the order of elements specifies the order of import styles.

Default order is `["none", "all", "multiple", "single"]`.

There are four different styles and the default member syntax sort order is:

- `none` - import module without exported bindings.
- `all` - import all members provided by exported bindings.
- `multiple` - import multiple members.
- `single` - import single member.

All four options must be specified in the array, but you can customize their order.

Examples of incorrect code for this rule with the default `{ "memberSyntaxSortOrder": ["none", "all", "multiple", "single"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBcImVycm9yXCIqL1xuaW1wb3J0IGEgZnJvbSAnZm9vLmpzJztcbmltcG9ydCAqIGFzIGIgZnJvbSAnYmFyLmpzJzsifQ==)

```
/*eslint sort-imports: "error"*/
import a from 'foo.js';
import * as b from 'bar.js';
1
2
3
```

Examples of correct code for this rule with the `{ "memberSyntaxSortOrder": ['single', 'all', 'multiple', 'none'] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwibWVtYmVyU3ludGF4U29ydE9yZGVyXCI6IFsnc2luZ2xlJywgJ2FsbCcsICdtdWx0aXBsZScsICdub25lJ10gfV0qL1xuXG5pbXBvcnQgYSBmcm9tICdmb28uanMnO1xuaW1wb3J0ICogYXMgYiBmcm9tICdiYXIuanMnOyJ9)

```
/*eslint sort-imports: ["error", { "memberSyntaxSortOrder": ['single', 'all', 'multiple', 'none'] }]*/

import a from 'foo.js';
import * as b from 'bar.js';
1
2
3
4
```

Examples of correct code for this rule with the `{ "memberSyntaxSortOrder": ['all', 'single', 'multiple', 'none'] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwibWVtYmVyU3ludGF4U29ydE9yZGVyXCI6IFsnYWxsJywgJ3NpbmdsZScsICdtdWx0aXBsZScsICdub25lJ10gfV0qL1xuXG5pbXBvcnQgKiBhcyBmb28gZnJvbSAnZm9vLmpzJztcbmltcG9ydCB6IGZyb20gJ3pvby5qcyc7XG5pbXBvcnQge2EsIGJ9IGZyb20gJ2Zvby5qcyc7In0=)

```
/*eslint sort-imports: ["error", { "memberSyntaxSortOrder": ['all', 'single', 'multiple', 'none'] }]*/

import * as foo from 'foo.js';
import z from 'zoo.js';
import {a, b} from 'foo.js';
1
2
3
4
5
```

### `allowSeparatedGroups`

When `true`, the rule checks the sorting of import declaration statements only for those that appear on consecutive lines. Default is `false`.

In other words, a blank line or a comment line or line with any other statement after an import declaration statement will reset the sorting of import declaration statements.

Examples of incorrect code for this rule with the `{ "allowSeparatedGroups": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTZXBhcmF0ZWRHcm91cHNcIjogdHJ1ZSB9XSovXG5cbmltcG9ydCBiIGZyb20gJ2Zvby5qcyc7XG5pbXBvcnQgYyBmcm9tICdiYXIuanMnO1xuaW1wb3J0IGEgZnJvbSAnYmF6LmpzJzsifQ==)

```
/*eslint sort-imports: ["error", { "allowSeparatedGroups": true }]*/

import b from 'foo.js';
import c from 'bar.js';
import a from 'baz.js';
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "allowSeparatedGroups": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTZXBhcmF0ZWRHcm91cHNcIjogdHJ1ZSB9XSovXG5cbmltcG9ydCBiIGZyb20gJ2Zvby5qcyc7XG5pbXBvcnQgYyBmcm9tICdiYXIuanMnO1xuXG5pbXBvcnQgYSBmcm9tICdiYXouanMnOyJ9)

```
/*eslint sort-imports: ["error", { "allowSeparatedGroups": true }]*/

import b from 'foo.js';
import c from 'bar.js';

import a from 'baz.js';
1
2
3
4
5
6
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTZXBhcmF0ZWRHcm91cHNcIjogdHJ1ZSB9XSovXG5cbmltcG9ydCBiIGZyb20gJ2Zvby5qcyc7XG5pbXBvcnQgYyBmcm9tICdiYXIuanMnO1xuLy8gY29tbWVudFxuaW1wb3J0IGEgZnJvbSAnYmF6LmpzJzsifQ==)

```
/*eslint sort-imports: ["error", { "allowSeparatedGroups": true }]*/

import b from 'foo.js';
import c from 'bar.js';
// comment
import a from 'baz.js';
1
2
3
4
5
6
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC1pbXBvcnRzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dTZXBhcmF0ZWRHcm91cHNcIjogdHJ1ZSB9XSovXG5cbmltcG9ydCBiIGZyb20gJ2Zvby5qcyc7XG5pbXBvcnQgYyBmcm9tICdiYXIuanMnO1xucXV1eCgpO1xuaW1wb3J0IGEgZnJvbSAnYmF6LmpzJzsifQ==)

```
/*eslint sort-imports: ["error", { "allowSeparatedGroups": true }]*/

import b from 'foo.js';
import c from 'bar.js';
quux();
import a from 'baz.js';
1
2
3
4
5
6
```

## When Not To Use It

This rule is a formatting preference and not following it won’t negatively affect the quality of your code. If alphabetizing imports isn’t a part of your coding standards, then you can leave this rule disabled.

## Related Rules

- [sort-keys](/docs/latest/rules/sort-keys)
- [sort-vars](/docs/latest/rules/sort-vars)

## Version

This rule was introduced in ESLint v2.0.0-beta.1.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/sort-imports.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/sort-imports.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/sort-imports.md
                    
                
                )
