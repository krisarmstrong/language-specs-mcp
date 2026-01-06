On this page

# color-hex-length

Specify short or long notation for hex colors.

```
a { color: #fff }
/**        ↑
 * This hex color */
```

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"short"`[​](#short)

```
{
  "color-hex-length": "short"
}
```

The following patterns are considered problems:

```
a { color: #ffffff; }
```

```
a { color: #ffffffaa; }
```

The following patterns are not considered problems:

```
a { color: #fff; }
```

```
a { color: #fffa; }
```

```
a { color: #a4a4a4; }
```

### `"long"`[​](#long)

```
{
  "color-hex-length": "long"
}
```

The following patterns are considered problems:

```
a { color: #fff; }
```

```
a { color: #fffa; }
```

The following patterns are not considered problems:

```
a { color: #ffffff; }
```

```
a { color: #ffffffaa; }
```

[Previouscolor-hex-alpha](/user-guide/rules/color-hex-alpha)[Nextcolor-named](/user-guide/rules/color-named)

- [Options](#options)

  - ["short"](#short)
  - ["long"](#long)
