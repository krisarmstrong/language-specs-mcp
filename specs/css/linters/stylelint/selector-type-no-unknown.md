On this page

# selector-type-no-unknown

Disallow unknown type selectors.

```
    unknown {}
/** ↑
 * This type selector */
```

This rule considers tags defined in the HTML, SVG, and MathML specifications to be known.

## Options[​](#options)

### `true`[​](#true)

```
{
  "selector-type-no-unknown": true
}
```

The following patterns are considered problems:

```
unknown {}
```

```
tag {}
```

The following patterns are not considered problems:

```
input {}
```

```
ul li {}
```

```
li > a {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"custom-elements"`[​](#custom-elements)

Allow custom elements.

```
{
  "selector-type-no-unknown": [true, { "ignore": ["custom-elements"] }]
}
```

The following patterns are considered problems:

```
unknown {}
```

```
x-Foo {}
```

The following patterns are not considered problems:

```
x-foo {}
```

#### `"default-namespace"`[​](#default-namespace)

Allow unknown type selectors if they belong to the default namespace.

```
{
  "selector-type-no-unknown": [true, { "ignore": ["default-namespace"] }]
}
```

The following patterns are considered problems:

```
namespace|unknown {}
```

The following patterns are not considered problems:

```
unknown {}
```

### `ignoreNamespaces`[​](#ignorenamespaces)

```
{ "ignoreNamespaces": ["array", "of", "namespaces", "/regex/"] }
```

Given:

```
{
  "selector-type-no-unknown": [
    true,
    { "ignoreNamespaces": ["/^my-/", "custom-namespace"] }
  ]
}
```

The following patterns are not considered problems:

```
custom-namespace|unknown {}
```

```
my-namespace|unknown {}
```

```
my-other-namespace|unknown {}
```

### `ignoreTypes`[​](#ignoretypes)

```
{ "ignoreTypes": ["array", "of", "types", "/regex/"] }
```

Given:

```
{
  "selector-type-no-unknown": [
    true,
    { "ignoreTypes": ["/^my-/", "custom-type"] }
  ]
}
```

The following patterns are not considered problems:

```
custom-type {}
```

```
my-type {}
```

```
my-other-type {}
```

[Previousselector-type-case](/user-guide/rules/selector-type-case)[Nextshorthand-property-no-redundant-values](/user-guide/rules/shorthand-property-no-redundant-values)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
  - [ignoreNamespaces](#ignorenamespaces)
  - [ignoreTypes](#ignoretypes)
