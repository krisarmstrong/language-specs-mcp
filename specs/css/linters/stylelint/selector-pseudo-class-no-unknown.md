On this page

# selector-pseudo-class-no-unknown

Disallow unknown pseudo-class selectors.

```
  a:hover {}
/** ↑
 * This pseudo-class selector */
```

This rule considers pseudo-class selectors defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

This rule ignores vendor-prefixed pseudo-class selectors.

## Options[​](#options)

### `true`[​](#true)

```
{
  "selector-pseudo-class-no-unknown": true
}
```

The following patterns are considered problems:

```
a:unknown {}
```

```
a:UNKNOWN {}
```

```
a:hoverr {}
```

The following patterns are not considered problems:

```
a:hover {}
```

```
a:focus {}
```

```
:not(p) {}
```

```
input:-moz-placeholder {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignorePseudoClasses`[​](#ignorepseudoclasses)

```
{ "ignorePseudoClasses": ["array", "of", "pseudo-classes", "/regex/"] }
```

Given:

```
{
  "selector-pseudo-class-no-unknown": [
    true,
    { "ignorePseudoClasses": ["/^--my-/", "--pseudo-class"] }
  ]
}
```

The following patterns are not considered problems:

```
a:--my-pseudo {}
```

```
a:--my-other-pseudo {}
```

```
a:--pseudo-class {}
```

[Previousselector-pseudo-class-disallowed-list](/user-guide/rules/selector-pseudo-class-disallowed-list)[Nextselector-pseudo-element-allowed-list](/user-guide/rules/selector-pseudo-element-allowed-list)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignorePseudoClasses](#ignorepseudoclasses)
