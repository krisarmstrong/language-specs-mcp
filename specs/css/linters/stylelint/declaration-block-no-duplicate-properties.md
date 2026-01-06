On this page

# declaration-block-no-duplicate-properties

Disallow duplicate properties within declaration blocks.

```
a { color: pink; color: orange; }
/** ↑            ↑
 * These duplicated properties */
```

This rule ignores variables (`$sass`, `@less`, `--custom-property`).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `true`[​](#true)

```
{
  "declaration-block-no-duplicate-properties": true
}
```

The following patterns are considered problems:

```
a { color: pink; color: orange; }
```

```
a { color: pink; background: orange; color: orange }
```

The following patterns are not considered problems:

```
a { color: pink; }
```

```
a { color: pink; background: orange; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"consecutive-duplicates"`[​](#consecutive-duplicates)

Ignore consecutive duplicated properties.

```
{
  "declaration-block-no-duplicate-properties": [
    true,
    { "ignore": ["consecutive-duplicates"] }
  ]
}
```

They can prove to be useful fallbacks for older browsers.

The following patterns are considered problems:

```
p {
  font-size: 16px;
  font-weight: 400;
  font-size: 1rem;
}
```

The following patterns are not considered problems:

```
p {
  font-size: 16px;
  font-size: 1rem;
  font-weight: 400;
}
```

#### `"consecutive-duplicates-with-different-values"`[​](#consecutive-duplicates-with-different-values)

Ignore consecutive duplicated properties with different values.

```
{
  "declaration-block-no-duplicate-properties": [
    true,
    { "ignore": ["consecutive-duplicates-with-different-values"] }
  ]
}
```

Including duplicate properties (fallbacks) is useful to deal with older browsers support for CSS properties. E.g. using `px` units when `rem` isn't available.

The following patterns are considered problems:

```
/* properties with the same value */
p {
  font-size: 16px;
  font-size: 16px;
  font-weight: 400;
}
```

```
/* nonconsecutive duplicates */
p {
  font-size: 16px;
  font-weight: 400;
  font-size: 1rem;
}
```

The following patterns are not considered problems:

```
p {
  font-size: 16px;
  font-size: 1rem;
  font-weight: 400;
}
```

#### `"consecutive-duplicates-with-different-syntaxes"`[​](#consecutive-duplicates-with-different-syntaxes)

Ignore consecutive duplicated properties with different value syntaxes (type and unit of value).

```
{
  "declaration-block-no-duplicate-properties": [
    true,
    { "ignore": ["consecutive-duplicates-with-different-syntaxes"] }
  ]
}
```

The following patterns are considered problems:

```
/* properties with the same value syntax */
p {
  font-size: 16px;
  font-size: 14px;
  font-weight: 400;
}
```

The following patterns are not considered problems:

```
p {
  font-size: 16px;
  font-size: 16rem;
  font-weight: 400;
}
```

#### `"consecutive-duplicates-with-same-prefixless-values"`[​](#consecutive-duplicates-with-same-prefixless-values)

Ignore consecutive duplicated properties with identical values, when ignoring their prefix.

```
{
  "declaration-block-no-duplicate-properties": [
    true,
    { "ignore": ["consecutive-duplicates-with-same-prefixless-values"] }
  ]
}
```

This option is useful to deal with draft CSS values while still being future proof. E.g. using `fit-content` and `-moz-fit-content`.

The following patterns are considered problems:

```
/* nonconsecutive duplicates */
p {
  width: fit-content;
  height: 32px;
  width: -moz-fit-content;
}
```

```
/* properties with different prefixless values */
p {
  width: -moz-fit-content;
  width: 100%;
}
```

The following patterns are not considered problems:

```
p {
  width: -moz-fit-content;
  width: fit-content;
}
```

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Ignore duplicates of specific properties.

Given:

```
{
  "declaration-block-no-duplicate-properties": [
    true,
    { "ignoreProperties": ["color", "/background-/"] }
  ]
}
```

The following patterns are considered problems:

```
a { color: pink; background: orange; background: white; }
```

```
a { background: orange; color: pink; background: white; }
```

The following patterns are not considered problems:

```
a { color: pink; color: orange; background-color: orange; background-color: white; }
```

```
a { color: pink; background-color: orange; color: orange; background-color: white; }
```

[Previousdeclaration-block-no-duplicate-custom-properties](/user-guide/rules/declaration-block-no-duplicate-custom-properties)[Nextdeclaration-block-no-redundant-longhand-properties](/user-guide/rules/declaration-block-no-redundant-longhand-properties)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
  - [ignoreProperties](#ignoreproperties)
