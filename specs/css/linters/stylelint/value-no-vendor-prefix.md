On this page

# value-no-vendor-prefix

Disallow vendor prefixes for values.

```
a { display: -webkit-flex; }
/**           ↑
 *  This prefix */
```

This rule does not fix vendor-prefixed values that weren't handled by [Autoprefixer](https://github.com/postcss/autoprefixer) version 10.2.5. Exceptions may be added on a case by case basis.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule. However, it will not remove duplicate values produced when the prefixes are removed. You can use [Autoprefixer](https://github.com/postcss/autoprefixer) itself, with the [add option off and the remove option on](https://github.com/postcss/autoprefixer#options), in these situations.

## Options[​](#options)

### `true`[​](#true)

```
{
  "value-no-vendor-prefix": true
}
```

The following patterns are considered problems:

```
a { display: -webkit-flex; }
```

```
a { max-width: -moz-max-content; }
```

```
a { background: -webkit-linear-gradient(bottom, #000, #fff); }
```

The following patterns are not considered problems:

```
a { display: flex; }
```

```
a { max-width: max-content; }
```

```
a { background: linear-gradient(bottom, #000, #fff); }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreValues`[​](#ignorevalues)

```
{ "ignoreValues": ["array", "of", "values", "/regex/"] }
```

Given:

```
{
  "value-no-vendor-prefix": [
    true,
    { "ignoreValues": ["grab", "max-content", "/^-moz-all$/"] }
  ]
}
```

The following patterns are not considered problems:

```
a { cursor: -webkit-grab; }
```

```
a { max-width: -moz-max-content; }
```

```
a { -moz-user-select: -moz-all; }
```

warning

An exact match comparison will be performed for non-regex strings in the next major version. If you want to keep the legacy behavior, please consider using a regex instead. E.g. `[/^(-webkit-|-moz-)?max-content$/]`.[Previousvalue-keyword-case](/user-guide/rules/value-keyword-case)[NextIgnoring code](/user-guide/ignore-code)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreValues](#ignorevalues)
