On this page

# length-zero-no-unit

Disallow units for zero lengths.

```
a { top: 0px; }
/**      ↑↑
 * This zero and this type of length unit */
```

Lengths refer to distance measurements. A length is a dimension, which is a number immediately followed by a unit identifier. However, for zero lengths the unit identifier is optional. The length units are: `em`, `ex`, `ch`, `vw`, `vh`, `cm`, `mm`, `in`, `pt`, `pc`, `px`, `rem`, `vmin`, and `vmax`.

This rule ignores lengths within math functions (e.g. `calc`).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `true`[​](#true)

```
{
  "length-zero-no-unit": true
}
```

The following patterns are considered problems:

```
a { top: 0px }
```

```
a { top: 0.000em }
```

The following patterns are not considered problems:

```
a { top: 0 } /* no unit */
```

```
a { transition-delay: 0s; } /* dimension */
```

```
a { top: 2in; }
```

```
a { top: 1.001vh }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"custom-properties"`[​](#custom-properties)

Ignore units for zero lengths in custom properties.

```
{
  "length-zero-no-unit": [true, { "ignore": ["custom-properties"] }]
}
```

The following pattern is not considered a problem:

```
a { --x: 0px; }
```

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Ignore units for zero lengths within the specified functions.

Given:

```
{
  "length-zero-no-unit": [true, { "ignoreFunctions": ["var", "/^--/"] }]
}
```

The following patterns are not considered problems:

```
a { top: var(--foo, 0px); }
```

```
a { top: --bar(0px); }
```

### `ignorePreludeOfAtRules`[​](#ignorepreludeofatrules)

```
{
  "ignorePreludeOfAtRules": ["array", "of", "at-rules", "/regex/"]
}
```

Ignore units for zero lengths within the preludes of the specified at-rules.

Given:

```
{
  "length-zero-no-unit": [
    true,
    { "ignorePreludeOfAtRules": ["media", "/^--bar/"] }
  ]
}
```

The following patterns are not considered problems:

```
@media (height > 0px) {}
```

```
@--bar-baz 0px;
```

[Previouslayer-name-pattern](/user-guide/rules/layer-name-pattern)[Nextlightness-notation](/user-guide/rules/lightness-notation)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
  - [ignoreFunctions](#ignorefunctions)
  - [ignorePreludeOfAtRules](#ignorepreludeofatrules)
