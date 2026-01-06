On this page

# rule-empty-line-before

Require or disallow an empty line before rules.

```
a {}
      /* ← */
b {}  /* ↑ */
/**      ↑
 * This line */
```

This rule ignores rules that are the very first node in a source.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

There must always be an empty line before rules.

```
{
  "rule-empty-line-before": "always"
}
```

The following patterns are considered problems:

```
a {} b {}
```

```
a {}
b {}
```

The following patterns are not considered problems:

```
a {}

b {}
```

### `"never"`[​](#never)

There must never be an empty line before rules.

```
{
  "rule-empty-line-before": "never"
}
```

The following patterns are considered problems:

```
a {}

b {}
```

The following patterns are not considered problems:

```
a {} b {}
```

```
a {}
b {}
```

### `"always-multi-line"`[​](#always-multi-line)

There must always be an empty line before multi-line rules.

```
{
  "rule-empty-line-before": "always-multi-line"
}
```

The following patterns are considered problems:

```
a {
  color: red;
}
b {
  color: blue;
}
```

The following patterns are not considered problems:

```
a {
  color: red;
}

b {
  color: blue;
}
```

### `"never-multi-line"`[​](#never-multi-line)

There must never be an empty line before multi-line rules.

```
{
  "rule-empty-line-before": "never-multi-line"
}
```

The following patterns are considered problems:

```
a {
  color: red;
}

b {
  color: blue;
}
```

The following patterns are not considered problems:

```
a {
  color: red;
}
b {
  color: blue;
}
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"after-rule"`[​](#after-rule)

Reverse the primary option for rules that follow another rule.

Given:

```
{
  "rule-empty-line-before": ["always", { "except": ["after-rule"] }]
}
```

The following patterns are considered problems:

```
a {}

b {}
```

The following patterns are not considered problems:

```
a {}
b {}
```

#### `"after-single-line-comment"`[​](#after-single-line-comment)

Reverse the primary option for rules that follow a single-line comment.

Given:

```
{
  "rule-empty-line-before": [
    "always",
    { "except": ["after-single-line-comment"] }
  ]
}
```

The following patterns are considered problems:

```
/* comment */

a {}
```

The following patterns are not considered problems:

```
/* comment */
a {}
```

#### `"inside-block-and-after-rule"`[​](#inside-block-and-after-rule)

Reverse the primary option for rules that are inside a block and follow another rule.

Given:

```
{
  "rule-empty-line-before": [
    "always",
    { "except": ["inside-block-and-after-rule"] }
  ]
}
```

The following patterns are considered problems:

```
@media {

  a {}

  b {}
}
```

The following patterns are not considered problems:

```
@media {

  a {}
  b {}
}
```

#### `"inside-block"`[​](#inside-block)

Reverse the primary option for rules that are inside a block.

Given:

```
{
  "rule-empty-line-before": ["always", { "except": ["inside-block"] }]
}
```

The following patterns are considered problems:

```
a {
  color: red;

  & b {
    color: blue;
  }
}

```

The following patterns are not considered problems:

```
a {
  color: red;
  & b {
    color: blue;
  }
}
```

#### `"first-nested"`[​](#first-nested)

Reverse the primary option for rules that are nested and the first child of their parent node.

Given:

```
{
  "rule-empty-line-before": ["always", { "except": ["first-nested"] }]
}
```

The following patterns are considered problems:

```
@media {

  a {}

  b {}
}
```

The following patterns are not considered problems:

```
@media {
  a {}

  b {}
}
```

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment)

Ignore rules that follow a comment.

Given:

```
{
  "rule-empty-line-before": ["always", { "ignore": ["after-comment"] }]
}
```

The following patterns are not considered problems:

```
/* comment */
a {}
```

#### `"first-nested"`[​](#first-nested-1)

Ignore rules that are nested and the first child of their parent node.

Given:

```
{
  "rule-empty-line-before": ["always", { "ignore": ["first-nested"] }]
}
```

The following patterns are not considered problems:

```
@media {
  a {}

  b {}
}
```

#### `"inside-block"`[​](#inside-block-1)

Ignore rules that are inside a block.

Given:

```
{
  "rule-empty-line-before": ["always", { "ignore": ["inside-block"] }]
}
```

The following patterns are not considered problems:

```
@media {
  a {}
}
```

```
@media {
  a {}
  b {}
}
```

[Previousproperty-no-vendor-prefix](/user-guide/rules/property-no-vendor-prefix)[Nextrule-nesting-at-rule-required-list](/user-guide/rules/rule-nesting-at-rule-required-list)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)
  - ["always-multi-line"](#always-multi-line)
  - ["never-multi-line"](#never-multi-line)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
  - [ignore](#ignore)
