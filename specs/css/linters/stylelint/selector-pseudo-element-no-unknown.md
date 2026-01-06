On this page

# selector-pseudo-element-no-unknown

Disallow unknown pseudo-element selectors.

```
  a::before {}
/**  ↑
 * This pseudo-element selector */
```

This rule considers pseudo-element selectors defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

This rule ignores vendor-prefixed pseudo-element selectors.

## Options[​](#options)

### `true`[​](#true)

```
{
  "selector-pseudo-element-no-unknown": true
}
```

The following patterns are considered problems:

```
a::pseudo {}
```

```
a::PSEUDO {}
```

```
a::element {}
```

The following patterns are not considered problems:

```
a:before {}
```

```
a::before {}
```

```
::selection {}
```

```
input::-moz-placeholder {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignorePseudoElements`[​](#ignorepseudoelements)

```
{ "ignorePseudoElements": ["array", "of", "pseudo-elements", "/regex/"] }
```

Given:

```
{
  "selector-pseudo-element-no-unknown": [
    true,
    { "ignorePseudoElements": ["/^--my-/", "--pseudo-element"] }
  ]
}
```

The following patterns are not considered problems:

```
a::--my-pseudo {}
```

```
a::--my-other-pseudo {}
```

```
a::--pseudo-element {}
```

[Previousselector-pseudo-element-disallowed-list](/user-guide/rules/selector-pseudo-element-disallowed-list)[Nextselector-type-case](/user-guide/rules/selector-type-case)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignorePseudoElements](#ignorepseudoelements)
