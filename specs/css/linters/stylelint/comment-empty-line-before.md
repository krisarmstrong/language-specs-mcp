On this page

# comment-empty-line-before

Require or disallow an empty line before comments.

```
a {}
              /* ← */
/* comment */ /* ↑ */
/**              ↑
*        This line */
```

This rule ignores:

- comments that are the very first node in the source
- shared-line comments
- single-line comments with `//` (when you're using a custom syntax that supports them)
- comments within selector and value lists

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

There must always be an empty line before comments.

```
{
  "comment-empty-line-before": "always"
}
```

The following patterns are considered problems:

```
a {}
/* comment */
```

The following patterns are not considered problems:

```
a {}

/* comment */
```

```
a {} /* comment */
```

### `"never"`[​](#never)

There must never be an empty line before comments.

```
{
  "comment-empty-line-before": "never"
}
```

The following patterns are considered problems:

```
a {}

/* comment */
```

The following patterns are not considered problems:

```
a {}
/* comment */
```

```
a {} /* comment */
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"first-nested"`[​](#first-nested)

Reverse the primary option for comments that are nested and the first child of their parent node.

Given:

```
{
  "comment-empty-line-before": ["always", { "except": ["first-nested"] }]
}
```

The following patterns are considered problems:

```
a {

  /* comment */
  color: pink;
}
```

The following patterns are not considered problems:

```
a {
  /* comment */
  color: pink;
}
```

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment)

Ignore comments that follow another comment.

Given:

```
{
  "comment-empty-line-before": ["always", { "ignore": ["after-comment"] }]
}
```

The following patterns are not considered problems:

```
a {
  background: pink;

  /* comment */
  /* comment */
  color: #eee;
}
```

```
a {
  background: pink;

  /* comment */

  /* comment */
  color: #eee;
}
```

#### `"stylelint-commands"`[​](#stylelint-commands)

Ignore configuration comments, e.g. `/* stylelint-disable color-no-hex */`.

Given:

```
{
  "comment-empty-line-before": ["always", { "ignore": ["stylelint-commands"] }]
}
```

The following patterns are considered problems:

```
a {
  background: pink;
  /* not a configuration comment */
  color: #eee;
}
```

The following patterns are not considered problems:

```
a {
  background: pink;
  /* stylelint-disable color-no-hex */
  color: pink;
}
```

### `ignoreComments`[​](#ignorecomments)

```
{ "ignoreComments": ["array", "of", "comments", "/regex/"] }
```

Ignore comments matching the given regular expressions or strings.

Given:

```
{
  "comment-empty-line-before": [
    "always",
    { "ignoreComments": ["/^ignore/", "string-ignore"] }
  ]
}
```

The following patterns are not considered problems:

```
:root {
  background: pink;
  /* ignore this comment because of the regex */
  color: pink;
}
```

```
:root {
  background: pink;
  /* string-ignore */
  color: pink;
}
```

[Previouscolor-no-invalid-hex](/user-guide/rules/color-no-invalid-hex)[Nextcomment-no-empty](/user-guide/rules/comment-no-empty)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
  - [ignore](#ignore)
  - [ignoreComments](#ignorecomments)
