On this page

# color-no-hex

Disallow hex colors.

```
a { color: #333 }
/**        ↑
 * This hex color */
```

## Options[​](#options)

### `true`[​](#true)

```
{
  "color-no-hex": true
}
```

The following patterns are considered problems:

```
a { color: #000; }
```

```
a { color: #fff1aa; }
```

```
a { color: #123456aa; }
```

Hex values that are not valid also cause problems:

```
a { color: #foobar; }
```

```
a { color: #0000000000000000; }
```

The following patterns are not considered problems:

```
a { color: black; }
```

```
a { color: rgb(0, 0, 0); }
```

```
a { color: rgba(0, 0, 0, 1); }
```

[Previouscolor-named](/user-guide/rules/color-named)[Nextcolor-no-invalid-hex](/user-guide/rules/color-no-invalid-hex)

- [Options](#options)

  - [true](#true)
