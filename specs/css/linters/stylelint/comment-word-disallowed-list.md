On this page

# comment-word-disallowed-list

Specify a list of disallowed words within comments.

```
 /* words within comments */
/** ↑     ↑      ↑
 * These three words */
```

warning

Comments within selector and value lists are currently ignored.

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "words", "/regex/"]
```

Given:

```
{
  "comment-word-disallowed-list": ["/^TODO:/", "badword"]
}
```

The following patterns are considered problems:

```
/* TODO: */
```

```
/* TODO: add fallback */
```

```
/* some badword */
```

The following patterns are not considered problems:

```
/* comment */
```

[Previouscomment-whitespace-inside](/user-guide/rules/comment-whitespace-inside)[Nextcontainer-name-pattern](/user-guide/rules/container-name-pattern)

- [Options](#options)

  - [Array<string>](#arraystring)
