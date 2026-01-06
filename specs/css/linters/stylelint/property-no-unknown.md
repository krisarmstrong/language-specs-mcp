On this page

# property-no-unknown

Disallow unknown properties.

```
a { height: 100%; }
/** ↑
 * This property */
```

This rule considers properties defined in the [CSS Specifications and browser specific properties](https://github.com/betit/known-css-properties#source) to be known.

This rule ignores:

- variables (`$sass`, `@less`, `--custom-property`)
- vendor-prefixed properties (e.g., `-moz-align-self`, `-webkit-align-self`)

Use option `checkPrefixed` described below to turn on checking of vendor-prefixed properties.

For customizing syntax, see the [languageOptions](/user-guide/configure#languageoptions) section.

## Options[​](#options)

### `true`[​](#true)

```
{
  "property-no-unknown": true
}
```

The following patterns are considered problems:

```
a {
  colr: blue;
}
```

```
a {
  my-property: 1;
}
```

The following patterns are not considered problems:

```
a {
  color: green;
}
```

```
a {
  fill: black;
}
```

```
a {
  -moz-align-self: center;
}
```

```
a {
  -webkit-align-self: center;
}
```

```
a {
  align-self: center;
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Given:

```
{
  "property-no-unknown": [true, { "ignoreProperties": ["/^my-/", "custom"] }]
}
```

The following patterns are not considered problems:

```
a {
  my-property: 10px;
}
```

```
a {
  my-other-property: 10px;
}
```

```
a {
  custom: 10px;
}
```

### `ignoreSelectors`[​](#ignoreselectors)

```
{ "ignoreSelectors": ["array", "of", "selectors", "/regex/"] }
```

Skips checking properties of the given selectors against this rule.

Given:

```
{
  "property-no-unknown": [true, { "ignoreSelectors": [":root"] }]
}
```

The following patterns are not considered problems:

```
:root {
  my-property: blue;
}
```

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Ignores properties nested within specified at-rules.

Given:

```
{
  "property-no-unknown": [true, { "ignoreAtRules": ["supports"] }]
}
```

The following patterns are not considered problems:

```
@supports (display: grid) {
  a {
    my-property: 1;
  }
}
```

### `checkPrefixed`[​](#checkprefixed)

If `true`, this rule will check vendor-prefixed properties. Defaults to `false`.

Given:

```
{
  "property-no-unknown": [true, { "checkPrefixed": true }]
}
```

The following patterns are not considered problems:

```
a {
  -webkit-overflow-scrolling: auto;
}
```

```
a {
  -moz-box-flex: 0;
}
```

The following patterns are considered problems:

```
a {
  -moz-align-self: center;
}
```

```
a {
  -moz-overflow-scrolling: center;
}
```

[Previousproperty-no-deprecated](/user-guide/rules/property-no-deprecated)[Nextproperty-no-vendor-prefix](/user-guide/rules/property-no-vendor-prefix)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
  - [ignoreSelectors](#ignoreselectors)
  - [ignoreAtRules](#ignoreatrules)
  - [checkPrefixed](#checkprefixed)
