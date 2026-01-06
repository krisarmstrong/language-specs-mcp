On this page

# comment-no-empty

Disallow empty comments.

```
    /* */
/** ↑
 * Comments like this */
```

This rule ignores SCSS-like comments.

warning

Comments within selector and value lists are currently ignored.

## Options[​](#options)

### `true`[​](#true)

```
{
  "comment-no-empty": true
}
```

The following patterns are considered problems:

```
/**/
```

```
/* */
```

```
/*

 */
```

The following patterns are not considered problems:

```
/* comment */
```

```
/*
 * Multi-line Comment
**/
```

[Previouscomment-empty-line-before](/user-guide/rules/comment-empty-line-before)[Nextcomment-pattern](/user-guide/rules/comment-pattern)

- [Options](#options)

  - [true](#true)
