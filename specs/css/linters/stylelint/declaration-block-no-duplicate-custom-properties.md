On this page

# declaration-block-no-duplicate-custom-properties

Disallow duplicate custom properties within declaration blocks.

```
a { --custom-property: pink; --custom-property: orange; }
/** ↑                        ↑
 * These duplicated custom properties */
```

This rule is case-sensitive.

## Options[​](#options)

### `true`[​](#true)

```
{
  "declaration-block-no-duplicate-custom-properties": true
}
```

The following patterns are considered problems:

```
a { --custom-property: pink; --custom-property: orange; }
```

```
a { --custom-property: pink; background: orange; --custom-property: orange }
```

The following patterns are not considered problems:

```
a { --custom-property: pink; }
```

```
a { --custom-property: pink; --cUstOm-prOpErtY: orange; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Ignore duplicates of specific properties.

Given:

```
{
  "declaration-block-no-duplicate-custom-properties": [
    true,
    { "ignoreProperties": ["--custom-property", "/ignored/"] }
  ]
}
```

The following patterns are considered problems:

```
a { --another-custom-property: 1; --another-custom-property: 1; }
```

The following patterns are not considered problems:

```
a { --custom-property: 1; --custom-property: 1; }
```

```
a { --custom-ignored-property: 1; --custom-ignored-property: 1; }
```

[Previouscustom-property-pattern](/user-guide/rules/custom-property-pattern)[Nextdeclaration-block-no-duplicate-properties](/user-guide/rules/declaration-block-no-duplicate-properties)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
