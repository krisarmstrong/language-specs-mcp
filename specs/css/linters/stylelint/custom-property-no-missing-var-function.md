On this page

# custom-property-no-missing-var-function

Disallow missing `var` function for custom properties.

```
    :root { --foo: red; }
    a { color: --foo; }
/**            ↑
 *             This custom property */
```

This rule has the following limitations:

- It only reports custom properties that are defined within the same source.
- It does not check properties that can contain author-defined identifiers, e.g. `transition-property`.

## Options[​](#options)

### `true`[​](#true)

```
{
  "custom-property-no-missing-var-function": true
}
```

The following patterns are considered problems:

```
:root { --foo: red; }
a { color: --foo; }
```

```
@property --foo {}
a { color: --foo; }
```

The following patterns are not considered problems:

```
:root { --foo: red; }
a { color: var(--foo); }
```

```
@property --foo {}
a { color: var(--foo); }
```

```
@property --foo {}
a { transition-property: --foo; }
```

[Previouscustom-property-empty-line-before](/user-guide/rules/custom-property-empty-line-before)[Nextcustom-property-pattern](/user-guide/rules/custom-property-pattern)

- [Options](#options)

  - [true](#true)
