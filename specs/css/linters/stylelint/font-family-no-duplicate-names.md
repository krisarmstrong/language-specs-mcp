On this page

# font-family-no-duplicate-names

Disallow duplicate names within font families.

```
a { font-family: serif, serif; }
/**              ↑      ↑
 * These font family names */
```

This rule checks the `font` and `font-family` properties.

This rule ignores `$sass`, `@less`, and `var(--custom-property)` variable syntaxes.

warning

This rule will stumble on unquoted multi-word font names and unquoted font names containing escape sequences. Wrap these font names in quotation marks, and everything should be fine.

## Options[​](#options)

### `true`[​](#true)

```
{
  "font-family-no-duplicate-names": true
}
```

The following patterns are considered problems:

```
a { font-family: 'Times', Times, serif; }
```

```
a { font: 1em "Arial", 'Arial', sans-serif; }
```

```
a { font: normal 14px/32px -apple-system, BlinkMacSystemFont, sans-serif, sans-serif; }
```

The following patterns are not considered problems:

```
a { font-family: Times, serif; }
```

```
a { font: 1em "Arial", "sans-serif", sans-serif; }
```

```
a { font: normal 14px/32px -apple-system, BlinkMacSystemFont, sans-serif; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreFontFamilyNames`[​](#ignorefontfamilynames)

```
{ "ignoreFontFamilyNames": ["array", "of", "font-family-names", "/regex/"] }
```

Given:

```
{
  "font-family-no-duplicate-names": [
    true,
    { "ignoreFontFamilyNames": ["/^My Font /", "monospace"] }
  ]
}
```

The following patterns are not considered problems:

```
font-family: monospace, monospace
```

```
font-family: "My Font Family", "My Font Family", monospace
```

[Previousfont-family-name-quotes](/user-guide/rules/font-family-name-quotes)[Nextfont-family-no-missing-generic-family-keyword](/user-guide/rules/font-family-no-missing-generic-family-keyword)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreFontFamilyNames](#ignorefontfamilynames)
