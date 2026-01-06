On this page

# no-empty-source

Disallow empty sources.

```
```

A source containing only whitespace, e.g., spaces, tabs, or newlines, is considered empty.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-empty-source": true
}
```

The following patterns are not considered problems:

```
a {}
```

```
/* Only comments */
```

[Previousno-duplicate-selectors](/user-guide/rules/no-duplicate-selectors)[Nextno-invalid-double-slash-comments](/user-guide/rules/no-invalid-double-slash-comments)

- [Options](#options)

  - [true](#true)
