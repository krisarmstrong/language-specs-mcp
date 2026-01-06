On this page

# media-query-no-invalid

Disallow invalid media queries.

```
@media not(min-width: 300px) {}
/**    ↑
 * This media query */
```

Media queries must be grammatically valid according to the [Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) specification.

This rule is only appropriate for CSS. You should not turn it on for CSS-like languages, such as SCSS or Less.

It works well with other rules that validate feature names and values:

- [media-feature-name-no-unknown](/user-guide/rules/media-feature-name-no-unknown)
- [media-feature-name-value-no-unknown](/user-guide/rules/media-feature-name-value-no-unknown)

## Options[​](#options)

### `true`[​](#true)

```
{
  "media-query-no-invalid": true
}
```

The following patterns are considered problems:

```
@media not(min-width: 300px) {}
```

```
@media (width == 100px) {}
```

```
@media (color) and (hover) or (width) {}
```

The following patterns are not considered problems:

```
@media not (min-width: 300px) {}
```

```
@media (width = 100px) {}
```

```
@media ((color) and (hover)) or (width) {}
```

```
@media (color) and ((hover) or (width)) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Ignore the specified functions.

Given:

```
{
  "media-query-no-invalid": [
    true,
    { "ignoreFunctions": ["theme", "/^get.*$/"] }
  ]
}
```

The following patterns are not considered problems:

```
@media (min-width: theme(screens.md)) {}
```

```
@media (max-width: get-default-width()) {}
```

[Previousmedia-feature-range-notation](/user-guide/rules/media-feature-range-notation)[Nextmedia-type-no-deprecated](/user-guide/rules/media-type-no-deprecated)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreFunctions](#ignorefunctions)
