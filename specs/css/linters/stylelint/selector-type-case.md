On this page

# selector-type-case

Specify lowercase or uppercase for type selectors.

```
    a {}
/** ↑
 * This is type selector */
```

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"lower"`[​](#lower)

```
{
  "selector-type-case": "lower"
}
```

The following patterns are considered problems:

```
A {}
```

```
LI {}
```

The following patterns are not considered problems:

```
a {}
```

```
li {}
```

### `"upper"`[​](#upper)

```
{
  "selector-type-case": "upper"
}
```

The following patterns are considered problems:

```
a {}
```

```
li {}
```

The following patterns are not considered problems:

```
A {}
```

```
LI {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreTypes`[​](#ignoretypes)

```
{ "ignoreTypes": ["array", "of", "types", "/regex/"] }
```

Given:

```
{
  "selector-type-case": [
    "lower",
    { "ignoreTypes": ["$childClass", "/(p|P)arent.*/"] }
  ]
}
```

The following patterns are not considered problems:

```
myParentClass {
  color: pink;
}

$childClass {
  color: pink;
}
```

[Previousselector-pseudo-element-no-unknown](/user-guide/rules/selector-pseudo-element-no-unknown)[Nextselector-type-no-unknown](/user-guide/rules/selector-type-no-unknown)

- [Options](#options)

  - ["lower"](#lower)
  - ["upper"](#upper)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreTypes](#ignoretypes)
