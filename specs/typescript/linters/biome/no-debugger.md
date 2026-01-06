# noDebugger

- [JavaScript (and super languages)](#tab-panel-734)

## Summary

[Section titled “Summary”](#summary)

- Rule available since: `v1.0.0`
- Diagnostic Category: [lint/suspicious/noDebugger](/reference/diagnostics#diagnostic-category)
- This rule is recommended, meaning it is enabled by default.
- This rule has an [unsafe](/linter/#unsafe-fixes) fix.
- The default severity of this rule is [error](/reference/diagnostics#error).
- Sources: 

  - Same as [no-debugger](https://eslint.org/docs/latest/rules/no-debugger)

## How to configure

[Section titled “How to configure”](#how-to-configure)biome.json

```
1{2  "linter": {3    "rules": {4      "suspicious": {5        "noDebugger": "error"6      }7    }8  }9}
```

## Description

[Section titled “Description”](#description)

Disallow the use of `debugger`

## Examples

[Section titled “Examples”](#examples)

### Invalid

[Section titled “Invalid”](#invalid)

```
1debugger;
```

```
code-block.js:1:1 lint/suspicious/noDebuggerhttps://biomejs.dev/linter/rules/no-debugger  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ This is an unexpected use of the debugger statement.
  
  > 1 │ debugger;
      │ ^^^^^^^^^
    2 │ 
  
  ℹ Unsafe fix: Remove debugger statement
  
    1 │ debugger;
      │ ---------
```

### Valid

[Section titled “Valid”](#valid)

```
1const test = { debugger: 1 };2test.debugger;
```

## Related links

[Section titled “Related links”](#related-links)

- [Disable a rule](/linter/#disable-a-rule)
- [Configure the code fix](/linter#configure-the-code-fix)
- [Rule options](/linter/#rule-options)
- [Source Code](https://github.com/biomejs/biome/blob/main/crates/biome_js_analyze/src/lint/suspicious/no_debugger.rs)
- [Test Cases](https://github.com/biomejs/biome/blob/main/crates/biome_js_analyze/tests/specs/suspicious/noDebugger)

[Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/linter/rules/no-debugger.mdx)

 Sponsored by 

Copyright (c) 2023-present Biome Developers and Contributors.
