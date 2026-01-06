On this page

# font-weight-notation

Require numeric or named (where possible) `font-weight` values.

```
a { font-weight: bold; }
/**              ↑
 *               This notation */

a { font: italic small-caps 600 16px/3 cursive; }
/**                         ↑
 *                          And this notation, too */

@font-face { font-weight: normal bold; }
/**                       ↑
 *                        Multiple notations are available in @font-face */
```

This rule ignores `$sass`, `@less`, and `var(--custom-property)` variable syntaxes.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"numeric"`[​](#numeric)

`font-weight` values must always be numbers.

```
{
  "font-weight-notation": "numeric"
}
```

The following patterns are considered problems:

```
a { font-weight: bold; }
```

```
a { font: italic normal 20px sans-serif; }
```

```
@font-face { font-weight: normal bold; }
```

The following patterns are not considered problems:

```
a { font-weight: 700; }
```

```
a { font: italic 400 20px; }
```

```
@font-face { font-weight: 400 700; }
```

### `"named-where-possible"`[​](#named-where-possible)

`font-weight` values must always be keywords when an appropriate keyword is available.

```
{
  "font-weight-notation": "named-where-possible"
}
```

This means that only `400` and `700` will be rejected, because those are the only numbers with keyword equivalents (`normal` and `bold`).

The following patterns are considered problems:

```
a { font-weight: 700; }
```

```
a { font: italic 400 20px sans-serif; }
```

The following patterns are not considered problems:

```
a { font-weight: bold; }
```

```
a { font: italic normal 20px sans-serif; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"relative"`[​](#relative)

Ignore the [relative](https://drafts.csswg.org/css-fonts/#font-weight-prop) keyword names of `bolder` and `lighter`.

Given:

```
{
  "font-weight-notation": ["numeric", { "ignore": ["relative"] }]
}
```

The following patterns are not considered problems:

```
a { font-weight: 400; }
a b { font-weight: lighter; }
```

[Previousfont-family-no-missing-generic-family-keyword](/user-guide/rules/font-family-no-missing-generic-family-keyword)[Nextfunction-allowed-list](/user-guide/rules/function-allowed-list)

- [Options](#options)

  - ["numeric"](#numeric)
  - ["named-where-possible"](#named-where-possible)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
