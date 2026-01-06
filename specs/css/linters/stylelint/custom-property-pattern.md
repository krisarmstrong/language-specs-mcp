On this page

# custom-property-pattern

Specify a pattern for custom properties.

```
a { --foo-: 1px; }
/**   ↑
 * The pattern of this */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

Given:

```
{
  "custom-property-pattern": "foo-.+"
}
```

The following patterns are considered problems:

```
:root { --boo-bar: 0; }
```

The following patterns are not considered problems:

```
:root { --foo-bar: 0; }
```

[Previouscustom-property-no-missing-var-function](/user-guide/rules/custom-property-no-missing-var-function)[Nextdeclaration-block-no-duplicate-custom-properties](/user-guide/rules/declaration-block-no-duplicate-custom-properties)

- [Options](#options)

  - [string](#string)
