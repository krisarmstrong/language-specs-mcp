On this page

# nesting-selector-no-missing-scoping-root

Disallow missing scoping root for nesting selectors.

```
    & {}
/** ↑
 * This nesting selector */
```

CSS nesting selectors (`&`) represent the parent selector in nested CSS. When used at the top level or within certain at-rules without a scoping root, they can cause unexpected behavior or indicate a mistake in the CSS structure.

## Options[​](#options)

### `true`[​](#true)

```
{
  "nesting-selector-no-missing-scoping-root": true
}
```

The following patterns are considered problems:

```
& {}
```

```
@media all {
  & {}
}
```

```
@scope (&) {}
```

The following patterns are not considered problems:

```
a {
  & {}
}
```

```
a {
  @media all {
    & {}
  }
}
```

```
a {
  @scope (&) {}
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Ignore nesting selectors within specified at-rules.

Given:

```
{
  "nesting-selector-no-missing-scoping-root": [
    true,
    { "ignoreAtRules": ["--foo", "/^--bar-/"] }
  ]
}
```

The following patterns are not considered problems:

```
@--foo {
  & {}
}
```

```
@--bar-baz qux {
  & {}
}
```

[Previousnamed-grid-areas-no-invalid](/user-guide/rules/named-grid-areas-no-invalid)[Nextno-descending-specificity](/user-guide/rules/no-descending-specificity)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAtRules](#ignoreatrules)
