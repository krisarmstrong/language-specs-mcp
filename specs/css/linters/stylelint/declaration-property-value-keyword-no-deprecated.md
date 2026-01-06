On this page

# declaration-property-value-keyword-no-deprecated

Disallow deprecated keywords for properties within declarations.

```
  a { color: ThreeDDarkShadow; }
/**     ↑         ↑
 * property and value pairs like these */
```

This rule flags keywords that were removed or deprecated after being in the CSS specifications, including editor drafts, and were subsequently either:

- shipped in a stable version of a browser
- shipped by a developer channel/edition browser
- shipped but behind experimental flags
- polyfilled with some adoption before any browser actually shipped
- had an MDN page at one point in time

The [fix option](/user-guide/options#fix) can automatically fix some of the problems reported by this rule.

Prior art:

- [@isnotdefined/no-obsolete](https://www.npmjs.com/package/@isnotdefined/stylelint-plugin)

## Options[​](#options)

### `true`[​](#true)

```
{
  "declaration-property-value-keyword-no-deprecated": true
}
```

The following patterns are considered problems:

```
a { overflow: overlay; }
```

```
a { text-justify: distribute; }
```

The following patterns are not considered problems:

```
a { overflow: auto; }
```

```
a { text-justify: inter-character; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreKeywords`[​](#ignorekeywords)

```
{ "ignoreKeywords": ["array", "of", "keywords", "/regex/"] }
```

Given:

```
{
  "declaration-property-value-keyword-no-deprecated": [
    true,
    { "ignoreKeywords": ["ActiveBorder", "/caption/i"] }
  ]
}
```

The following patterns are not considered problems:

```
a {
  color: ActiveBorder;
}
```

```
a {
  color: InactiveCaptionText;
}
```

[Previousdeclaration-property-value-disallowed-list](/user-guide/rules/declaration-property-value-disallowed-list)[Nextdeclaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreKeywords](#ignorekeywords)
