# no-duplicate-imports

Disallow duplicate module imports

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [includeExports](#includeexports)
  2. [allowSeparateTypeImports](#allowseparatetypeimports)

3. [Version](#version)
4. [Resources](#resources)

Using a single `import` statement per module will make the code clearer because you can see everything being imported from that module on one line.

In the following example the `module` import on line 1 is repeated on line 3. These can be combined to make the list of imports more succinct.

```
import { merge } from 'module';
import something from 'another-module';
import { find } from 'module';
1
2
3
```

Copy code to clipboard

## Rule Details

This rule requires that all imports from a single module that can be merged exist in a single `import` statement.

Example of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWltcG9ydHM6IFwiZXJyb3JcIiovXG5cbmltcG9ydCB7IG1lcmdlIH0gZnJvbSAnbW9kdWxlJztcbmltcG9ydCBzb21ldGhpbmcgZnJvbSAnYW5vdGhlci1tb2R1bGUnO1xuaW1wb3J0IHsgZmluZCB9IGZyb20gJ21vZHVsZSc7In0=)

```
/*eslint no-duplicate-imports: "error"*/

import { merge } from 'module';
import something from 'another-module';
import { find } from 'module';
1
2
3
4
5
```

Example of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWltcG9ydHM6IFwiZXJyb3JcIiovXG5cbmltcG9ydCB7IG1lcmdlLCBmaW5kIH0gZnJvbSAnbW9kdWxlJztcbmltcG9ydCBzb21ldGhpbmcgZnJvbSAnYW5vdGhlci1tb2R1bGUnOyJ9)

```
/*eslint no-duplicate-imports: "error"*/

import { merge, find } from 'module';
import something from 'another-module';
1
2
3
4
```

Example of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWltcG9ydHM6IFwiZXJyb3JcIiovXG5cbi8vIG5vdCBtZXJnZWFibGVcbmltcG9ydCB7IG1lcmdlIH0gZnJvbSAnbW9kdWxlJztcbmltcG9ydCAqIGFzIHNvbWV0aGluZyBmcm9tICdtb2R1bGUnOyJ9)

```
/*eslint no-duplicate-imports: "error"*/

// not mergeable
import { merge } from 'module';
import * as something from 'module';
1
2
3
4
5
```

## Options

This rule has an object option:

- `"includeExports"`: `true` (default `false`) checks for exports in addition to imports.
- `"allowSeparateTypeImports"`: `true` (default `false`) allows a type import alongside a value import from the same module in TypeScript files.

### includeExports

If re-exporting from an imported module, you should add the imports to the `import`-statement, and export that directly, not use `export ... from`.

Example of incorrect code for this rule with the `{ "includeExports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWltcG9ydHM6IFtcImVycm9yXCIsIHsgXCJpbmNsdWRlRXhwb3J0c1wiOiB0cnVlIH1dKi9cblxuaW1wb3J0IHsgbWVyZ2UgfSBmcm9tICdtb2R1bGUnO1xuXG5leHBvcnQgeyBmaW5kIH0gZnJvbSAnbW9kdWxlJzsifQ==)

```
/*eslint no-duplicate-imports: ["error", { "includeExports": true }]*/

import { merge } from 'module';

export { find } from 'module';
1
2
3
4
5
```

Example of correct code for this rule with the `{ "includeExports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWltcG9ydHM6IFtcImVycm9yXCIsIHsgXCJpbmNsdWRlRXhwb3J0c1wiOiB0cnVlIH1dKi9cblxuaW1wb3J0IHsgbWVyZ2UsIGZpbmQgfSBmcm9tICdtb2R1bGUnO1xuXG5leHBvcnQgeyBmaW5kIH07In0=)

```
/*eslint no-duplicate-imports: ["error", { "includeExports": true }]*/

import { merge, find } from 'module';

export { find };
1
2
3
4
5
```

Example of correct code for this rule with the `{ "includeExports": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwbGljYXRlLWltcG9ydHM6IFtcImVycm9yXCIsIHsgXCJpbmNsdWRlRXhwb3J0c1wiOiB0cnVlIH1dKi9cblxuaW1wb3J0IHsgbWVyZ2UsIGZpbmQgfSBmcm9tICdtb2R1bGUnO1xuXG4vLyBjYW5ub3QgYmUgbWVyZ2VkIHdpdGggdGhlIGFib3ZlIGltcG9ydFxuZXhwb3J0ICogYXMgc29tZXRoaW5nIGZyb20gJ21vZHVsZSc7XG5cbi8vIGNhbm5vdCBiZSB3cml0dGVuIGRpZmZlcmVudGx5XG5leHBvcnQgKiBmcm9tICdtb2R1bGUnOyJ9)

```
/*eslint no-duplicate-imports: ["error", { "includeExports": true }]*/

import { merge, find } from 'module';

// cannot be merged with the above import
export * as something from 'module';

// cannot be written differently
export * from 'module';
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

### allowSeparateTypeImports

TypeScript allows importing types using `import type`. By default, this rule flags instances of `import type` that have the same specifier as `import`. The `allowSeparateTypeImports` option allows you to override this behavior.

Example of incorrect TypeScript code for this rule with the default `{ "allowSeparateTypeImports": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1kdXBsaWNhdGUtaW1wb3J0czogW1wiZXJyb3JcIiwgeyBcImFsbG93U2VwYXJhdGVUeXBlSW1wb3J0c1wiOiBmYWxzZSB9XSovXG5cbmltcG9ydCB7IHNvbWVWYWx1ZSB9IGZyb20gJ21vZHVsZSc7XG5pbXBvcnQgdHlwZSB7IFNvbWVUeXBlIH0gZnJvbSAnbW9kdWxlJzsifQ==)

```
/*eslint no-duplicate-imports: ["error", { "allowSeparateTypeImports": false }]*/

import { someValue } from 'module';
import type { SomeType } from 'module';
1
2
3
4
```

Example of correct TypeScript code for this rule with the default `{ "allowSeparateTypeImports": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1kdXBsaWNhdGUtaW1wb3J0czogW1wiZXJyb3JcIiwgeyBcImFsbG93U2VwYXJhdGVUeXBlSW1wb3J0c1wiOiBmYWxzZSB9XSovXG5cbmltcG9ydCB7IHNvbWVWYWx1ZSwgdHlwZSBTb21lVHlwZSB9IGZyb20gJ21vZHVsZSc7In0=)

```
/*eslint no-duplicate-imports: ["error", { "allowSeparateTypeImports": false }]*/

import { someValue, type SomeType } from 'module';
1
2
3
```

Example of incorrect TypeScript code for this rule with the `{ "allowSeparateTypeImports": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1kdXBsaWNhdGUtaW1wb3J0czogW1wiZXJyb3JcIiwgeyBcImFsbG93U2VwYXJhdGVUeXBlSW1wb3J0c1wiOiB0cnVlIH1dKi9cblxuaW1wb3J0IHsgc29tZVZhbHVlIH0gZnJvbSAnbW9kdWxlJztcbmltcG9ydCB0eXBlIHsgU29tZVR5cGUgfSBmcm9tICdtb2R1bGUnO1xuaW1wb3J0IHR5cGUgeyBBbm90aGVyVHlwZSB9IGZyb20gJ21vZHVsZSc7In0=)

```
/*eslint no-duplicate-imports: ["error", { "allowSeparateTypeImports": true }]*/

import { someValue } from 'module';
import type { SomeType } from 'module';
import type { AnotherType } from 'module';
1
2
3
4
5
```

Example of correct TypeScript code for this rule with the `{ "allowSeparateTypeImports": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1kdXBsaWNhdGUtaW1wb3J0czogW1wiZXJyb3JcIiwgeyBcImFsbG93U2VwYXJhdGVUeXBlSW1wb3J0c1wiOiB0cnVlIH1dKi9cblxuaW1wb3J0IHsgc29tZVZhbHVlIH0gZnJvbSAnbW9kdWxlJztcbmltcG9ydCB0eXBlIHsgU29tZVR5cGUsIEFub3RoZXJUeXBlIH0gZnJvbSAnbW9kdWxlJzsifQ==)

```
/*eslint no-duplicate-imports: ["error", { "allowSeparateTypeImports": true }]*/

import { someValue } from 'module';
import type { SomeType, AnotherType } from 'module';
1
2
3
4
```

## Version

This rule was introduced in ESLint v2.5.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-duplicate-imports.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-duplicate-imports.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-duplicate-imports.md
                    
                
                )
