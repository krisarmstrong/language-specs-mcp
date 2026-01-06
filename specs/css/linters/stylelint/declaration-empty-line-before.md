On this page

# declaration-empty-line-before

Require or disallow an empty line before declarations.

```
a {
  --foo: pink;
             /* ← */
  top: 15px; /* ↑ */
}            /* ↑ */
/**             ↑
 *      This line */
```

This rule only applies to standard property declarations. Use the [custom-property-empty-line-before](/user-guide/rules/custom-property-empty-line-before) rule for custom property declarations.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

```
{
  "declaration-empty-line-before": "always"
}
```

The following patterns are considered problems:

```
a {
  --foo: pink;
  top: 5px;
}
```

```
a {
  bottom: 15px;
  top: 5px;
}
```

The following patterns are not considered problems:

```
a {
  --foo: pink;

  top: 5px;
}
```

```
a {

  bottom: 15px;

  top: 5px;
}
```

### `"never"`[​](#never)

```
{
  "declaration-empty-line-before": "never"
}
```

The following patterns are considered problems:

```
a {
  --foo: pink;

  bottom: 15px;
}
```

```
a {

  bottom: 15px;

  top: 5px;
}
```

The following patterns are not considered problems:

```
a {
  --foo: pink;
  bottom: 15px;
}
```

```
a {
  bottom: 15px;
  top: 5px;
}
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment)

Reverse the primary option for declarations that follow a comment.

Shared-line comments do not trigger this option.

Given:

```
{
  "declaration-empty-line-before": ["always", { "except": ["after-comment"] }]
}
```

The following patterns are considered problems:

```
a {
  /* comment */

  top: 5px;
}
```

```
a {
  bottom: 5px; /* comment */
  top: 5px;
}
```

The following patterns are not considered problems:

```
a {
  /* comment */
  top: 5px;
}

```

```
a {
  bottom: 5px; /* comment */

  top: 5px;
}

```

#### `"after-declaration"`[​](#after-declaration)

Reverse the primary option for declarations that follow another declaration.

Shared-line comments do not affect this option.

Given:

```
{
  "declaration-empty-line-before": [
    "always",
    { "except": ["after-declaration"] }
  ]
}
```

The following patterns are considered problems:

```
a {

  bottom: 15px;

  top: 5px;
}
```

```
a {

  bottom: 15px; /* comment */

  top: 5px;
}
```

The following patterns are not considered problems:

```
a {

  bottom: 15px;
  top: 5px;
}
```

```
a {

  bottom: 15px; /* comment */
  top: 5px;
}
```

#### `"first-nested"`[​](#first-nested)

Reverse the primary option for declarations that are nested and the first child of their parent node.

Given:

```
{
  "declaration-empty-line-before": ["always", { "except": ["first-nested"] }]
}
```

The following patterns are considered problems:

```
a {

  bottom: 15px;

  top: 5px;
}
```

The following patterns are not considered problems:

```
a {
  bottom: 15px;

  top: 5px;
}
```

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment-1)

Ignore declarations that follow a comment.

Given:

```
{
  "declaration-empty-line-before": ["always", { "ignore": ["after-comment"] }]
}
```

The following patterns are not considered problems:

```
a {
  /* comment */
  bottom: 15px;
}
```

#### `"after-declaration"`[​](#after-declaration-1)

Ignore declarations that follow another declaration.

Given:

```
{
  "declaration-empty-line-before": [
    "always",
    { "ignore": ["after-declaration"] }
  ]
}
```

The following patterns are not considered problems:

```
a {

  bottom: 15px;
  top: 15px;
}
```

```
a {

  bottom: 15px;

  top: 15px;
}
```

```
a {

  color: orange;
  text-decoration: none;

  bottom: 15px;
  top: 15px;
}
```

#### `"first-nested"`[​](#first-nested-1)

Ignore declarations that are nested and the first child of their parent node.

Given:

```
{
  "declaration-empty-line-before": ["always", { "ignore": ["first-nested"] }]
}
```

The following patterns are not considered problems:

```
a {
  bottom: 15px;

  top: 5px;
}
```

#### `"inside-single-line-block"`[​](#inside-single-line-block)

Ignore declarations that are inside single-line blocks.

Given:

```
{
  "declaration-empty-line-before": [
    "always",
    { "ignore": ["inside-single-line-block"] }
  ]
}
```

The following patterns are not considered problems:

```
a { bottom: 15px; top: 5px; }
```

[Previousdeclaration-block-single-line-max-declarations](/user-guide/rules/declaration-block-single-line-max-declarations)[Nextdeclaration-no-important](/user-guide/rules/declaration-no-important)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
  - [ignore](#ignore)
