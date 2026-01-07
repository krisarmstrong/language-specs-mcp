noDebugger | Biome[Skip to content](#_top)[Biome](/)[Docs](/guides/getting-started)[Enterprise](/enterprise)[Playground](/playground)SearchCtrlK Cancel [Discord](https://biomejs.dev/chat)[GitHub](https://github.com/biomejs/biome)[Mastodon](https://fosstodon.org/@biomejs)[Open Collective](https://opencollective.com/biome)[YouTube](https://youtube.com/@Biomejs)[BlueSky](https://bsky.app/profile/biomejs.dev)[RSS](https://biomejs.dev/blog/rss.xml)[Blog](/blog/)Select themeDarkLightAutoSelect languageEnglishEspañolFrançais日本語简体中文PolskiPortuguêsУкраїнськаРусскийVersionv1.xv2.xnext

- [Blog](/blog/)
- [Playground](/playground)
- [Enterprise](/enterprise)
- Guides

  - [Getting Started](/guides/getting-started)
  - [Manual installation](/guides/manual-installation)
  - [Configure Biome updated](/guides/configure-biome)
  - [Use Biome in big projects](/guides/big-projects)
  - [Upgrade to Biome v2](/guides/upgrade-to-biome-v2)
  - Biome in your IDE

    - [First-party extensions](/guides/editors/first-party-extensions)
    - [Third-party extensions](/guides/editors/third-party-extensions)
    - [Integrate Biome in an editor extension](/guides/editors/create-an-extension)

  - [Integrate Biome with your VCS](/guides/integrate-in-vcs)
  - [Migrate from ESLint & Prettier](/guides/migrate-eslint-prettier)
  - [Investigate slowness](/guides/investigate-slowness)

- Formatter

  - [Introduction](/formatter)
  - [Differences with Prettier](/formatter/differences-with-prettier)
  - [Formatter Option Philosophy](/formatter/option-philosophy)

- Analyzer

  - [Suppressions](/analyzer/suppressions)
  - Linter

    - [Introduction](/linter)
    - [Domains](/linter/domains)
    - [Plugins](/linter/plugins)
    - [JavaScript Rules](/linter/javascript/rules)
    - [JavaScript Rules sources](/linter/javascript/sources)
    - [CSS Rules](/linter/css/rules)
    - [CSS Rules sources](/linter/css/sources)
    - [JSON Rules](/linter/json/rules)
    - [JSON Rules sources](/linter/json/sources)
    - [GraphQL Rules](/linter/graphql/rules)
    - [GraphQL Rules sources](/linter/graphql/sources)
    - [HTML Rules](/linter/html/rules)
    - [HTML Rules sources](/linter/html/sources)

  - Assist

    - [Introduction](/assist)
    - [JavaScript Actions](/assist/javascript/actions)
    - [JavaScript Actions sources](/assist/javascript/sources)
    - [CSS Actions](/assist/css/actions)
    - [CSS Actions sources](/assist/css/sources)
    - [JSON Actions](/assist/json/actions)
    - [JSON Actions sources](/assist/json/sources)
    - [GraphQL Actions](/assist/graphql/actions)
    - [GraphQL Actions sources](/assist/graphql/sources)

- Reference

  - [CLI](/reference/cli)
  - [Diagnostics](/reference/diagnostics)
  - [Environment variables](/reference/environment-variables)
  - [Reporters](/reference/reporters)
  - [Configuration](/reference/configuration)
  - [VS Code extension](/reference/vscode)
  - [Zed extension](/reference/zed)
  - [GritQL](/reference/gritql)

- Recipes

  - [Continuous Integration](/recipes/continuous-integration)
  - [Git Hooks](/recipes/git-hooks)
  - [Renovate](/recipes/renovate)
  - [Social Badges](/recipes/badges)

- Internals

  - [Philosophy](/internals/philosophy)
  - [Language support updated](/internals/language-support)
  - [Architecture](/internals/architecture)
  - [People and Credits](/internals/people-and-credits)
  - [Versioning](/internals/versioning)
  - [Changelog](/internals/changelog/)
  - [Changelog v1](/internals/changelog_v1)

[Discord](https://biomejs.dev/chat)[GitHub](https://github.com/biomejs/biome)[Mastodon](https://fosstodon.org/@biomejs)[Open Collective](https://opencollective.com/biome)[YouTube](https://youtube.com/@Biomejs)[BlueSky](https://bsky.app/profile/biomejs.dev)[RSS](https://biomejs.dev/blog/rss.xml)[Blog](/blog/)Select themeDarkLightAutoSelect languageEnglishEspañolFrançais日本語简体中文PolskiPortuguêsУкраїнськаРусскийVersionv1.xv2.xnextOn this page

- [Overview](#_top)
- [Summary](#summary)
- [How to configure](#how-to-configure)
- [Description](#description)
- [Examples](#examples)

  - [Invalid](#invalid)
  - [Valid](#valid)

- [Related links](#related-links)

## On this page

- [Overview](#_top)
- [Summary](#summary)
- [How to configure](#how-to-configure)
- [Description](#description)
- [Examples](#examples)

  - [Invalid](#invalid)
  - [Valid](#valid)

- [Related links](#related-links)

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
