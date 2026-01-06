On this page

# block-no-empty

Disallow empty blocks.

```
 a { }
/** ↑
 * Blocks like this */
```

## Options[​](#options)

### `true`[​](#true)

```
{
  "block-no-empty": true
}
```

The following patterns are considered problems:

```
a {}
```

```
a { }
```

```
@media print {
  a {}
}
```

The following patterns are not considered problems:

```
a {
  /* foo */
}
```

```
@media print {
  a {
    color: pink;
  }
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"comments"`[​](#comments)

Exclude comments from being treated as content inside of a block.

```
{
  "block-no-empty": [true, { "ignore": ["comments"] }]
}
```

The following patterns are considered problems:

```
a {
  /* foo */
}
```

```
@media print {
  a {
    /* foo */
  }
}
```

[Previousat-rule-property-required-list](/user-guide/rules/at-rule-property-required-list)[Nextblock-no-redundant-nested-style-rules](/user-guide/rules/block-no-redundant-nested-style-rules)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
