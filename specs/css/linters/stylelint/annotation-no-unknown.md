On this page

# annotation-no-unknown

Disallow unknown annotations.

```
a { color: green !imprtant; }
/**              ↑
 * This annotation */
```

This rule considers annotations defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

## Options[​](#options)

### `true`[​](#true)

```
{
  "annotation-no-unknown": true
}
```

The following pattern is considered a problem:

```
a {
  color: green !imprtant;
}
```

The following pattern is not considered a problem:

```
a {
  color: green !important;
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAnnotations`[​](#ignoreannotations)

```
{ "ignoreAnnotations": ["array", "of", "annotations", "/regex/"] }
```

Given:

```
{
  "annotation-no-unknown": [
    true,
    { "ignoreAnnotations": ["/^--foo-/", "--bar"] }
  ]
}
```

The following patterns are not considered problems:

```
a {
  color: green !--foo--bar;
}
```

```
a {
  color: green !--bar;
}
```

[Previousalpha-value-notation](/user-guide/rules/alpha-value-notation)[Nextat-rule-allowed-list](/user-guide/rules/at-rule-allowed-list)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAnnotations](#ignoreannotations)
