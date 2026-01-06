On this page

# hue-degree-notation

Specify number or angle notation for degree hues.

```
    a { color: hsl(198deg 28% 50%) }
/**                ↑
 *                 This notation */
```

Because hues are so often given in degrees, a hue can also be given as a number, which is interpreted as a number of degrees.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"angle"`[​](#angle)

Degree hues must always use angle notation.

```
{
  "hue-degree-notation": "angle"
}
```

The following patterns are considered problems:

```
a { color: hsl(198 28% 50%) }
```

```
a { color: lch(56.29% 19.86 10 / 15%) }
```

The following patterns are not considered problems:

```
a { color: hsl(198deg 28% 50%) }
```

```
a { color: lch(56.29% 19.86 10deg / 15%) }
```

### `"number"`[​](#number)

Degree hues must always use the number notation.

```
{
  "hue-degree-notation": "number"
}
```

The following patterns are considered problems:

```
a { color: hsl(198deg 28% 50%) }
```

```
a { color: lch(56.29% 19.86 10deg / 15%) }
```

The following patterns are not considered problems:

```
a { color: hsl(198 28% 50%) }
```

```
a { color: lch(56.29% 19.86 10 / 15%) }
```

[Previousfunction-url-scheme-disallowed-list](/user-guide/rules/function-url-scheme-disallowed-list)[Nextimport-notation](/user-guide/rules/import-notation)

- [Options](#options)

  - ["angle"](#angle)
  - ["number"](#number)
