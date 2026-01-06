On this page

# color-hex-alpha

Require or disallow alpha channel for hex colors.

```
a { color: #fffa }
/**            ↑
 * This alpha channel */
```

## Options[​](#options)

### `"always"`[​](#always)

```
{
  "color-hex-alpha": "always"
}
```

The following patterns are considered problems:

```
a { color: #fff; }
```

```
a { color: #ffffff; }
```

The following patterns are not considered problems:

```
a { color: #fffa; }
```

```
a { color: #ffffffaa; }
```

### `"never"`[​](#never)

```
{
  "color-hex-alpha": "never"
}
```

The following patterns are considered problems:

```
a { color: #fffa; }
```

```
a { color: #ffffffaa; }
```

The following patterns are not considered problems:

```
a { color: #fff; }
```

```
a { color: #ffffff; }
```

[Previouscolor-function-notation](/user-guide/rules/color-function-notation)[Nextcolor-hex-length](/user-guide/rules/color-hex-length)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)
