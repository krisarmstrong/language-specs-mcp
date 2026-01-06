On this page

# comment-whitespace-inside

Require or disallow whitespace on the inside of comment markers.

```
    /* comment */
/**  ↑         ↑
 * The space inside these two markers */
```

Any number of asterisks are allowed at the beginning or end of the comment. So `/** comment **/` is treated the same way as `/* comment */`.

warning

Comments within selector and value lists are currently ignored.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

There must always be whitespace inside the markers.

```
{
  "comment-whitespace-inside": "always"
}
```

The following patterns are considered problems:

```
/*comment*/
```

```
/*comment */
```

```
/** comment**/
```

The following patterns are not considered problems:

```
/* comment */
```

```
/** comment **/
```

```
/**
 * comment
 */
```

```
/*     comment
*/
```

### `"never"`[​](#never)

There must never be whitespace on the inside the markers.

```
{
  "comment-whitespace-inside": "never"
}
```

The following patterns are considered problems:

```
/* comment */
```

```
/*comment */
```

```
/** comment**/
```

The following patterns are not considered problems:

```
/*comment*/
```

```
/****comment****/
```

[Previouscomment-pattern](/user-guide/rules/comment-pattern)[Nextcomment-word-disallowed-list](/user-guide/rules/comment-word-disallowed-list)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)
