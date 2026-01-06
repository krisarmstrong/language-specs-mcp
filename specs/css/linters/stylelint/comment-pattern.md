On this page

# comment-pattern

Specify a pattern for comments.

```
/*  comment */
/** ↑
 * The pattern of this */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

Given:

```
{
  "comment-pattern": "foo .+"
}
```

The following patterns are considered problems:

```
/*not starting with foo*/
a { color: red; }
```

The following patterns are not considered problems:

```
/*foo at the beginning*/
a { color: red; }
```

[Previouscomment-no-empty](/user-guide/rules/comment-no-empty)[Nextcomment-whitespace-inside](/user-guide/rules/comment-whitespace-inside)

- [Options](#options)

  - [string](#string)
