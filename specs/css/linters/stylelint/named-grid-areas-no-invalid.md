On this page

# named-grid-areas-no-invalid

Disallow invalid named grid areas.

```
a { grid-template-areas:
      "a a a"
      "b b b"; }
/**   ↑
 *  This named grid area */
```

For a named grid area to be valid, all strings must define:

- the same number of cell tokens
- at least one cell token

And all named grid areas that spans multiple grid cells must form a single filled-in rectangle.

## Options[​](#options)

### `true`[​](#true)

```
{
  "named-grid-areas-no-invalid": true
}
```

The following patterns are considered problems:

```
a { grid-template-areas: "" }
```

```
a { grid-template-areas: "a a a"
                         "b b b b"; }
```

```
a { grid-template-areas: "a a a"
                         "b b a"; }
```

The following pattern is not considered a problem:

```
a { grid-template-areas: "a a a"
                         "b b b"; }
```

[Previousmedia-type-no-deprecated](/user-guide/rules/media-type-no-deprecated)[Nextnesting-selector-no-missing-scoping-root](/user-guide/rules/nesting-selector-no-missing-scoping-root)

- [Options](#options)

  - [true](#true)
