On this page

# shorthand-property-no-redundant-values

Disallow redundant values within shorthand properties.

```
a { margin: 1px 1px 1px 1px; }
/**             ↑   ↑   ↑
 *           These values */
```

You can use [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties) to set multiple values at once. For example, you can use the `margin` property to set the `margin-top`, `margin-right`, `margin-bottom`, and `margin-left` properties at once.

For some shorthand properties, e.g. those related to the [edges of a box](https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties#edges_of_a_box), you can safely omit some values.

This rule checks the following shorthand properties:

- `margin`, `margin-block`, `margin-inline`
- `padding`, `padding-block`, `padding-inline`
- `border-color`, `border-style`, `border-width`
- `border-radius`
- `border-block-color`, `border-block-style`, `border-block-width`
- `border-inline-color`, `border-inline-style`, `border-inline-width`
- `gap`, `grid-gap`
- `overflow`,
- `overscroll-behavior`,
- `scroll-margin`, `scroll-margin-block`, `scroll-margin-inline`
- `scroll-padding`, `scroll-padding-block`, `scroll-padding-inline`
- `inset`, `inset-block`, `inset-inline`

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `true`[​](#true)

```
{
  "shorthand-property-no-redundant-values": true
}
```

The following patterns are considered problems:

```
a { margin: 1px 1px; }
```

```
a { margin: 1px 1px 1px 1px; }
```

```
a { padding: 1px 2px 1px; }
```

```
a { border-radius: 1px 2px 1px 2px; }
```

```
a { -webkit-border-radius: 1px 1px 1px 1px; }
```

The following patterns are not considered problems:

```
a { margin: 1px; }
```

```
a { margin: 1px 1px 1px 2px; }
```

```
a { padding: 1px 1em 1pt 1pc; }
```

```
a { border-radius: 10px / 5px; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"four-into-three-edge-values"`[​](#four-into-three-edge-values)

Ignore four-value shorthand declarations that could be shortened to three values when applied to edges.

The following patterns are not considered problems:

```
a { margin: 1px 2px 3px 2px; }
```

```
a { inset: auto 0 0 0; }
```

[Previousselector-type-no-unknown](/user-guide/rules/selector-type-no-unknown)[Nextstring-no-newline](/user-guide/rules/string-no-newline)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
