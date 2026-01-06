On this page

# no-unknown-custom-properties

Disallow unknown custom properties.

```
a { color: var(--foo); }
/**            ↑
 *             This custom property */

a { color: var(--foo, var(--bar)); }
/**                       ↑
 *                        And this one */
```

This rule considers custom properties defined within the same source to be known.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-unknown-custom-properties": true
}
```

The following patterns are considered problems:

```
a { color: var(--foo); }
```

```
a { color: var(--foo, var(--bar)); }
```

The following patterns are not considered problems:

```
a { --foo: #f00; color: var(--foo); }
```

```
a { color: var(--foo, #f00); }
```

```
a { --foo: #f00; color: var(--bar, var(--foo)); }
```

```
@property --foo { syntax: "<color>"; inherits: false; initial-value: #f00; }
a { color: var(--foo); }
```

[Previousno-unknown-custom-media](/user-guide/rules/no-unknown-custom-media)[Nextnumber-max-precision](/user-guide/rules/number-max-precision)

- [Options](#options)

  - [true](#true)
