On this page

# block-no-redundant-nested-style-rules

Disallow redundant nested style rules within blocks.

```
a { & { color: red; } }
/** ↑
 * This nested style rule */
```

## Options[​](#options)

### `true`[​](#true)

```
{
  "block-no-redundant-nested-style-rules": true
}
```

The following patterns are considered problems:

```
a { & { color: red; } }
```

```
a { @media all { & { color: red; } } }
```

The following patterns are not considered problems:

```
a { color: red; }
```

```
a { @media all { color: red; } }
```

```
a { &.foo { color: red; } }
```

[Previousblock-no-empty](/user-guide/rules/block-no-empty)[Nextcolor-function-alias-notation](/user-guide/rules/color-function-alias-notation)

- [Options](#options)

  - [true](#true)
