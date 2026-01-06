On this page

# property-no-deprecated

Disallow deprecated properties.

```
  a { word-wrap: break-word; }
/**      ↑
 * Deprecated property */
```

This rule flags properties that were removed or deprecated after being in the CSS specifications, including editor drafts, and were either:

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
  "property-no-deprecated": true
}
```

The following patterns are considered problems:

```
a { clip: rect(0, 0, 0, 0); }
```

```
a { word-wrap: break-word; }
```

The following patterns are not considered problems:

```
a { clip-path: rect(0 0 0 0); }
```

```
a { overflow-wrap: break-word; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Given:

```
{
  "property-no-deprecated": [true, { "ignoreProperties": ["clip", "/^grid-/"] }]
}
```

The following patterns are not considered problems:

```
a { clip: rect(0, 0, 0, 0); }
```

```
a { grid-row-gap: 4px; }
```

[Previousproperty-disallowed-list](/user-guide/rules/property-disallowed-list)[Nextproperty-no-unknown](/user-guide/rules/property-no-unknown)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
