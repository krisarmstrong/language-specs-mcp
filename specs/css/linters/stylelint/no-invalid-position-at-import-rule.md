On this page

# no-invalid-position-at-import-rule

Disallow invalid position `@import` rules.

```
a {}
@import 'foo.css';
/** ↑
  * This @import */
```

Any `@import` rules must precede all other valid at-rules and style rules in a stylesheet (ignoring `@charset` and `@layer`), or else the `@import` rule is invalid.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-invalid-position-at-import-rule": true
}
```

The following patterns are considered problems:

```
a {}
@import 'foo.css';
```

```
@media print {}
@import 'foo.css';
```

The following patterns are not considered problems:

```
@import 'foo.css';
a {}
```

```
/* some comment */
@import 'foo.css';
```

```
@charset 'utf-8';
@import 'foo.css';
```

```
@layer default;
@import url(theme.css) layer(theme);
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Given:

```
{
  "no-invalid-position-at-import-rule": [
    true,
    { "ignoreAtRules": ["/^--my-/", "--custom"] }
  ]
}
```

The following patterns are not considered problems:

```
@--my-at-rule "bar.css";
@import "foo.css";
```

```
@--my-other-at-rule {}
@import "foo.css";
```

```
@--custom "bar.css";
@import "foo.css"
```

[Previousno-invalid-double-slash-comments](/user-guide/rules/no-invalid-double-slash-comments)[Nextno-invalid-position-declaration](/user-guide/rules/no-invalid-position-declaration)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAtRules](#ignoreatrules)
