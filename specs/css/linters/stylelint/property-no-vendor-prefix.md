On this page

# property-no-vendor-prefix

Disallow vendor prefixes for properties.

```
a { -webkit-transform: scale(1); }
/**  ↑
 * This prefix */
```

This rule ignores non-standard vendor-prefixed properties that aren't handled by [Autoprefixer](https://github.com/postcss/autoprefixer).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule. However, it will not remove duplicate properties produced when the prefixes are removed. You can use [Autoprefixer](https://github.com/postcss/autoprefixer) itself, with the [add option off and the remove option on](https://github.com/postcss/autoprefixer#options), in these situations.

## Options[​](#options)

### `true`[​](#true)

```
{
  "property-no-vendor-prefix": true
}
```

The following patterns are considered problems:

```
a { -webkit-transform: scale(1); }
```

```
a { -moz-columns: 2; }
```

The following patterns are not considered problems:

```
a { transform: scale(1); }
```

```
a { columns: 2; }
```

```
a { -webkit-touch-callout: none; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Given:

```
{
  "property-no-vendor-prefix": [
    true,
    { "ignoreProperties": ["transform", "columns"] }
  ]
}
```

The following patterns are not considered problems:

```
a { -webkit-transform: scale(1); }
```

```
a { -moz-columns: 2; }
```

[Previousproperty-no-unknown](/user-guide/rules/property-no-unknown)[Nextrule-empty-line-before](/user-guide/rules/rule-empty-line-before)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
