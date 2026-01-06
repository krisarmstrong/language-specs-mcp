On this page

# selector-nested-pattern

Specify a pattern for the selectors of rules nested within rules.

```
    a {
      color: orange;
      &:hover { color: pink; } }
/**   ↑
 * This nested selector */
```

Non-standard selectors (e.g. selectors with Sass or Less interpolation) and selectors of rules nested within at-rules are ignored.

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

The selector value will be checked in its entirety. If you'd like to allow for combinators and commas, you must incorporate them into your pattern.

Given:

```
{
  "selector-nested-pattern": "^&:(?:hover|focus)$"
}
```

The following patterns are considered problems:

```
a {
  .bar {}
}
```

```
a {
  .bar:hover {}
}
```

```
a {
  &:hover,
  &:focus {}
}
```

The following patterns are not considered problems:

```
a {
  &:hover {}
}
```

```
a {
  &:focus {}
}
```

```
a {
  &:hover {}
  &:focus {}
}
```

## Optional secondary options[​](#optional-secondary-options)

### `splitList`[​](#splitlist)

Split selector lists into individual selectors. Defaults to `false`.

Given:

```
{
  "selector-nested-pattern": ["^&:(?:hover|focus)$", { "splitList": true }]
}
```

The following patterns are considered problems:

```
a {
  .bar:hover,
  &:focus {}
}
```

The following patterns are not considered problems:

```
a {
  &:hover,
  &:focus {}
}
```

[Previousselector-max-universal](/user-guide/rules/selector-max-universal)[Nextselector-no-qualifying-type](/user-guide/rules/selector-no-qualifying-type)

- [Options](#options)

  - [string](#string)

- [Optional secondary options](#optional-secondary-options)

  - [splitList](#splitlist)
