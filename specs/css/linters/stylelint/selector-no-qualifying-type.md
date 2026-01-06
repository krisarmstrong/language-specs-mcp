On this page

# selector-no-qualifying-type

Disallow qualifying a selector by type.

```
    a.foo {}
/** ↑
 * This type selector is qualifying the class */
```

A type selector is "qualifying" when it is compounded with (chained to) another selector (e.g. `a.foo`, `a#foo`). This rule does not regulate type selectors that are combined with other selectors via a combinator (e.g. `a > .foo`, `a #foo`).

## Options[​](#options)

### `true`[​](#true)

```
{
  "selector-no-qualifying-type": true
}
```

The following patterns are considered problems:

```
a.foo {
  margin: 0
}
```

```
a#foo {
  margin: 0
}
```

```
input[type='button'] {
  margin: 0
}
```

The following patterns are not considered problems:

```
.foo {
  margin: 0
}
```

```
#foo {
  margin: 0
}
```

```
input {
  margin: 0
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"attribute"`[​](#attribute)

Allow attribute selectors qualified by type.

```
{
  "selector-no-qualifying-type": [true, { "ignore": ["attribute"] }]
}
```

The following patterns are not considered problems:

```
input[type='button'] {
  margin: 0
}
```

#### `"class"`[​](#class)

Allow class selectors qualified by type.

```
{
  "selector-no-qualifying-type": [true, { "ignore": ["class"] }]
}
```

The following patterns are not considered problems:

```
a.foo {
  margin: 0
}
```

#### `"id"`[​](#id)

Allow ID selectors qualified by type.

```
{
  "selector-no-qualifying-type": [true, { "ignore": ["id"] }]
}
```

The following patterns are not considered problems:

```
a#foo {
  margin: 0
}
```

[Previousselector-nested-pattern](/user-guide/rules/selector-nested-pattern)[Nextselector-no-vendor-prefix](/user-guide/rules/selector-no-vendor-prefix)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
