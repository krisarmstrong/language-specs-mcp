On this page

# at-rule-no-deprecated

Disallow deprecated at-rules.

```
    @viewport {}
/** ↑
 * At-rules like this */
```

This rule flags at-rules that were removed or deprecated after being in the CSS specifications, including editor drafts, and were subsequently either:

- shipped in a stable version of a browser
- shipped by a developer channel/edition browser
- shipped but behind experimental flags
- polyfilled with some adoption before any browser actually shipped
- had an MDN page at one point in time

The [fix option](/user-guide/options#fix) can automatically fix some of the problems reported by this rule.

Prior art:

- [@csstools/stylelint-no-at-nest-rule](https://www.npmjs.com/package/@csstools/stylelint-no-at-nest-rule)
- [@isnotdefined/no-obsolete](https://www.npmjs.com/package/@isnotdefined/stylelint-plugin)

## Options[​](#options)

### `true`[​](#true)

```
{
  "at-rule-no-deprecated": true
}
```

The following patterns are considered problems:

```
@viewport {}
```

```
a { @apply foo; }
```

The following patterns are not considered problems:

```
@starting-style {}
```

```
a { @layer {} }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Given:

```
{
  "at-rule-no-deprecated": [true, { "ignoreAtRules": ["/^view/", "apply"] }]
}
```

The following patterns are not considered problems:

```
@viewport {}
```

```
a { @apply foo; }
```

[Previousat-rule-empty-line-before](/user-guide/rules/at-rule-empty-line-before)[Nextat-rule-no-unknown](/user-guide/rules/at-rule-no-unknown)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAtRules](#ignoreatrules)
