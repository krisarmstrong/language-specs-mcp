On this page

# font-family-no-missing-generic-family-keyword

Disallow a missing generic family keyword within font families.

```
a { font-family: Arial, sans-serif; }
/**                     ↑
 * An example of generic family name */
```

The generic font family can be:

- placed anywhere in the font family list
- omitted if a keyword related to property inheritance or a system font is used

This rule checks the `font` and `font-family` properties.

## Options[​](#options)

### `true`[​](#true)

```
{
  "font-family-no-missing-generic-family-keyword": true
}
```

The following patterns are considered problems:

```
a { font-family: Helvetica, Arial, Verdana, Tahoma; }
```

```
a { font: 1em/1.3 Times; }
```

The following patterns are not considered problems:

```
a { font-family: Helvetica, Arial, Verdana, Tahoma, sans-serif; }
```

```
a { font: 1em/1.3 Times, serif, Apple Color Emoji; }
```

```
a { font: inherit; }
```

```
a { font: caption; }
```

```
a { font-family: var(--font-family-common); }
```

```
a { font-family: Helvetica, var(--font-family-common); }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreFontFamilies`[​](#ignorefontfamilies)

```
{ "ignoreFontFamilies": ["array", "of", "font-families", "/regex/"] }
```

Given:

```
{
  "font-family-no-missing-generic-family-keyword": [
    true,
    {
      "ignoreFontFamilies": ["custom-font"]
    }
  ]
}
```

The following pattern is not considered a problem:

```
a { font-family: custom-font; }
```

The following pattern is considered a problem:

```
a { font-family: invalid-custom-font; }
```

[Previousfont-family-no-duplicate-names](/user-guide/rules/font-family-no-duplicate-names)[Nextfont-weight-notation](/user-guide/rules/font-weight-notation)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreFontFamilies](#ignorefontfamilies)
