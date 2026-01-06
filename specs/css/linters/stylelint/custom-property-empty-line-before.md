On this page

# custom-property-empty-line-before

Require or disallow an empty line before custom properties.

```
a {
  top: 10px;
                          /* ← */
  --foo: pink;            /* ↑ */
}                         /* ↑ */
/**                          ↑
 *                   This line */
```

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

```
{
  "custom-property-empty-line-before": "always"
}
```

The following patterns are considered problems:

```
a {
  top: 10px;
  --foo: pink;
  --bar: red;
}
```

The following patterns are not considered problems:

```
a {
  top: 10px;

  --foo: pink;

  --bar: red;
}
```

### `"never"`[​](#never)

```
{
  "custom-property-empty-line-before": "never"
}
```

The following patterns are considered problems:

```
a {
  top: 10px;

  --foo: pink;

  --bar: red;
}
```

```
a {

  --foo: pink;
  --bar: red;
}
```

The following patterns are not considered problems:

```
a {
  top: 10px;
  --foo: pink;
  --bar: red;
}
```

```
a {
  --foo: pink;
  --bar: red;
}
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment)

Reverse the primary option for custom properties that follow a comment.

Shared-line comments do not trigger this option.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "except": ["after-comment"] }
  ]
}
```

The following patterns are considered problems:

```
a {

  --foo: pink;
  /* comment */

  --bar: red;
}
```

```
a {

  --foo: pink; /* comment */
  --bar: red;
}
```

The following patterns are not considered problems:

```
a {

  --foo: pink;
  /* comment */
  --bar: red;
}
```

```
a {

  --foo: pink; /* comment */

  --bar: red;
}
```

#### `"after-custom-property"`[​](#after-custom-property)

Reverse the primary option for custom properties that follow another custom property.

Shared-line comments do not affect this option.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "except": ["after-custom-property"] }
  ]
}
```

The following patterns are considered problems:

```
a {

  --foo: pink;

  --bar: red;
}
```

```
a {

  --foo: pink; /* comment */

  --bar: red;
}
```

The following patterns are not considered problems:

```
a {

  --foo: pink;
  --bar: red;
}
```

```
a {

  --foo: pink; /* comment */
  --bar: red;
}
```

#### `"first-nested"`[​](#first-nested)

Reverse the primary option for custom properties that are nested and the first child of their parent node.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "except": ["first-nested"] }
  ]
}
```

The following patterns are considered problems:

```
a {

  --foo: pink;

  --bar: red;
}
```

The following patterns are not considered problems:

```
a {
  --foo: pink;

  --bar: red;
}
```

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment-1)

Ignore custom properties that follow a comment.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "ignore": ["after-comment"] }
  ]
}
```

The following patterns are not considered problems:

```
a {
  /* comment */
  --foo: pink;
}
```

#### `"after-custom-property"`[​](#after-custom-property-1)

Ignore custom properties that follow another custom property.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "ignore": ["after-custom-property"] }
  ]
}
```

The following patterns are not considered problems:

```
a {

  --foo: pink;
  --bar: red;
}
```

#### `"first-nested"`[​](#first-nested-1)

Ignore custom properties that are nested and the first child of their parent node.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "ignore": ["first-nested"] }
  ]
}
```

The following patterns are not considered problems:

```
a {
  --foo: pink;

  --bar: red;
}
```

#### `"inside-single-line-block"`[​](#inside-single-line-block)

Ignore custom properties that are inside single-line blocks.

Given:

```
{
  "custom-property-empty-line-before": [
    "always",
    { "ignore": ["inside-single-line-block"] }
  ]
}
```

The following patterns are not considered problems:

```
a { --foo: pink; --bar: red; }
```

[Previouscustom-media-pattern](/user-guide/rules/custom-media-pattern)[Nextcustom-property-no-missing-var-function](/user-guide/rules/custom-property-no-missing-var-function)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
  - [ignore](#ignore)
