On this page

# at-rule-empty-line-before

Require or disallow an empty line before at-rules.

```
a {}
          /* ← */
@media {} /* ↑ */
/**          ↑
 *   This line */
```

This rule ignores:

- at-rules that are the very first node in the source
- the `@charset` rule
- `@import` in Less

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

There must always be an empty line before at-rules.

```
{
  "at-rule-empty-line-before": "always"
}
```

The following patterns are considered problems:

```
a {} @media {}
```

```
a {}
@media {}
```

The following patterns are not considered problems:

```
a {}

@media {}
```

### `"never"`[​](#never)

There must never be an empty line before at-rules.

```
{
  "at-rule-empty-line-before": "never"
}
```

The following patterns are considered problems:

```
a {}

@media {}
```

The following patterns are not considered problems:

```
a {} @media {}
```

```
a {}
@media {}
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"after-same-name"`[​](#after-same-name)

Reverse the primary option for at-rules that follow another at-rule with the same name.

This means that you can group your at-rules by name.

Given:

```
{
  "at-rule-empty-line-before": ["always", { "except": ["after-same-name"] }]
}
```

The following patterns are not considered problems:

```
@import url(x.css);
@import url(y.css);

@media (min-width: 100px) {}
@media (min-width: 200px) {}
```

```
a {

  @extends .foo;
  @extends .bar;

  @include x;
  @include y {}
}
```

#### `"inside-block"`[​](#inside-block)

Reverse the primary option for at-rules that are inside a block.

Given:

```
{
  "at-rule-empty-line-before": ["always", { "except": ["inside-block"] }]
}
```

The following patterns are considered problems:

```
a {

  @extend foo;
  color: pink;
}

b {
  color: pink;

  @extend foo;
}
```

The following patterns are not considered problems:

```
a {
  @extend foo;
  color: pink;
}

b {
  color: pink;
  @extend foo;
}
```

#### `"blockless-after-same-name-blockless"`[​](#blockless-after-same-name-blockless)

Reverse the primary option for blockless at-rules that follow another blockless at-rule with the same name.

This means that you can group your blockless at-rules by name.

Shared-line comments do not affect this option.

Given:

```
{
  "at-rule-empty-line-before": [
    "always",
    { "except": ["blockless-after-same-name-blockless"] }
  ]
}
```

The following patterns are not considered problems:

```
@import url(x.css);
@import url(y.css);

@namespace svg url('http://www.w3.org/2000/svg');
```

```
@import url(x.css); /* comment */
@import url(y.css);

@namespace svg url('http://www.w3.org/2000/svg');
```

```
a {

  @extends .foo;
  @extends .bar;

  @include loop;
  @include doo;
}
```

#### `"blockless-after-blockless"`[​](#blockless-after-blockless)

Reverse the primary option for blockless at-rules that follow another blockless at-rule.

Shared-line comments do not affect this option.

Given:

```
{
  "at-rule-empty-line-before": [
    "always",
    { "except": ["blockless-after-blockless"] }
  ]
}
```

The following patterns are considered problems:

```
@import url(x.css);

@import url(y.css);

@media print {}
```

The following patterns are not considered problems:

```
@import url(x.css);
@import url(y.css);

@media print {}
```

```
@import url(x.css); /* comment */
@import url(y.css);

@media print {}
```

#### `"first-nested"`[​](#first-nested)

Reverse the primary option for at-rules that are nested and the first child of their parent node.

Given:

```
{
  "at-rule-empty-line-before": ["always", { "except": ["first-nested"] }]
}
```

The following patterns are considered problems:

```
a {

  @extend foo;
  color: pink;
}

b {
  color: pink;
  @extend foo;
}
```

The following patterns are not considered problems:

```
a {
  @extend foo;
  color: pink;
}

b {
  color: pink;

  @extend foo;
}
```

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"after-comment"`[​](#after-comment)

Ignore at-rules that follow a comment.

Shared-line comments do not trigger this option.

Given:

```
{
  "at-rule-empty-line-before": ["always", { "ignore": ["after-comment"] }]
}
```

The following patterns are not considered problems:

```
/* comment */
@media {}
```

```
/* comment */

@media {}
```

```
@media {} /* comment */

@media {}
```

#### `"first-nested"`[​](#first-nested-1)

Ignore at-rules that are nested and the first child of their parent node.

Given:

```
{
  "at-rule-empty-line-before": ["always", { "ignore": ["first-nested"] }]
}
```

The following patterns are not considered problems:

```
@supports {
  @media {}

  @media {}
}
```

#### `"inside-block"`[​](#inside-block-1)

Ignore at-rules that are inside a block.

Given:

```
{
  "at-rule-empty-line-before": ["always", { "ignore": ["inside-block"] }]
}
```

The following patterns are not considered problems:

```
a {
  @extend foo;
  color: pink;
}

a {

  @extend foo;
  color: pink;
}

b {
  color: pink;
  @extend foo;
}

b {
  color: pink;

  @extend foo;
}
```

#### `"blockless-after-same-name-blockless"`[​](#blockless-after-same-name-blockless-1)

Ignore blockless at-rules that follow another blockless at-rule with the same name.

This means that you can group your blockless at-rules by name.

Given:

```
{
  "at-rule-empty-line-before": [
    "always",
    { "ignore": ["blockless-after-same-name-blockless"] }
  ]
}
```

The following patterns are not considered problems:

```

@import url(x.css);
@import url(y.css);

@namespace svg url('http://www.w3.org/2000/svg');
```

```
a {

  @extends .foo;
  @extends .bar;

  @include loop;
  @include doo;
}
```

#### `"blockless-after-blockless"`[​](#blockless-after-blockless-1)

Ignore blockless at-rules that follow another blockless at-rule.

Given:

```
{
  "at-rule-empty-line-before": [
    "always",
    { "ignore": ["blockless-after-blockless"] }
  ]
}
```

The following patterns are not considered problems:

```
@import url(x.css);

@import url(y.css);

@media print {}
```

```
@import url(x.css);
@import url(y.css);

@media print {}
```

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Ignore specified at-rules.

Given:

```
{
  "at-rule-empty-line-before": [
    "always",
    { "ignoreAtRules": ["namespace", "/^my-/"] }
  ]
}
```

The following patterns are not considered problems:

```
@import "foo.css";
@namespace svg url('http://www.w3.org/2000/svg');
```

```
a {}
@my-at-rule {}
```

[Previousat-rule-disallowed-list](/user-guide/rules/at-rule-disallowed-list)[Nextat-rule-no-deprecated](/user-guide/rules/at-rule-no-deprecated)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
  - [ignore](#ignore)
  - [ignoreAtRules](#ignoreatrules)
