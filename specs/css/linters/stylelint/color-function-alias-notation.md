On this page

# color-function-alias-notation

Specify alias notation for color-functions.

```
    a { color: rgb(0 0 0 / 0.2) }
/**            ↑
 *             This notation */
```

Color functions `rgb()` and `hsl()` have aliases `rgba()` and `hsla()`. Those are exactly equivalent, and [it's preferable](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb) to use the first variant without `a`.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"without-alpha"`[​](#without-alpha)

Applicable color-functions must always use the without alpha notation.

```
{
  "color-function-alias-notation": "without-alpha"
}
```

The following patterns are considered problems:

```
a { color: rgba(0 0 0) }
```

```
a { color: hsla(270 60% 50% / 15%) }
```

The following patterns are not considered problems:

```
a { color: rgb(0 0 0) }
```

```
a { color: hsl(270 60% 50% / 15%) }
```

### `"with-alpha"`[​](#with-alpha)

Applicable color-functions must always use with alpha notation.

```
{
  "color-function-alias-notation": "with-alpha"
}
```

The following patterns are considered problems:

```
a { color: rgb(0 0 0) }
```

```
a { color: hsl(270 60% 50% / 15%) }
```

The following patterns are not considered problems:

```
a { color: rgba(0 0 0) }
```

```
a { color: hsla(270 60% 50% / 15%) }
```

[Previousblock-no-redundant-nested-style-rules](/user-guide/rules/block-no-redundant-nested-style-rules)[Nextcolor-function-notation](/user-guide/rules/color-function-notation)

- [Options](#options)

  - ["without-alpha"](#without-alpha)
  - ["with-alpha"](#with-alpha)
