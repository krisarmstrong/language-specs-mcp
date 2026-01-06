On this page

# lightness-notation

Specify number or percentage notation for lightness.

```
    a { color: oklch(85% 0.17 88) }
/**                  ↑
 *                   This notation */
```

This rule supports `oklch`, `oklab`, `lch` and `lab` functions.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"percentage"`[​](#percentage)

Lightness must always use the percentage notation.

```
{
  "lightness-notation": "percentage"
}
```

The following patterns are considered problems:

```
a { color: oklch(0.85 0.17 88) }
```

```
a { color: oklab(0.86 0.2 154) }
```

```
a { color: lch(85 0.17 88) }
```

```
a { color: lab(86 0.2 154) }
```

The following patterns are not considered problems:

```
a { color: oklch(85% 0.17 88) }
```

```
a { color: oklab(86% 0.2 154) }
```

```
a { color: lch(85% 0.17 88) }
```

```
a { color: lab(86% 0.2 154) }
```

### `"number"`[​](#number)

Lightness must always use the number notation.

```
{
  "lightness-notation": "number"
}
```

The following patterns are considered problems:

```
a { color: oklch(85% 0.17 88) }
```

```
a { color: oklab(86% 0.2 154) }
```

```
a { color: lch(85% 0.17 88) }
```

```
a { color: lab(86% 0.2 154) }
```

The following patterns are not considered problems:

```
a { color: oklch(0.85 0.17 88) }
```

```
a { color: oklab(0.86 0.2 154) }
```

```
a { color: lch(85 0.17 88) }
```

```
a { color: lab(86 0.2 154) }
```

[Previouslength-zero-no-unit](/user-guide/rules/length-zero-no-unit)[Nextmax-nesting-depth](/user-guide/rules/max-nesting-depth)

- [Options](#options)

  - ["percentage"](#percentage)
  - ["number"](#number)
