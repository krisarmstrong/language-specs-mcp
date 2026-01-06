On this page

# no-unknown-custom-media

Disallow unknown custom media queries.

```
@custom-media --sm (min-width: 40rem);
/**             ↑
*   This custom media query name */

@media (--sm) {}
/**      ↑
*   And this one */
```

This rule considers custom media queries defined within the same source to be known.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-unknown-custom-media": true
}
```

The following patterns are considered problems:

```
@media (--sm) {}

@media (--sm), (max-height: 40rem) {}
```

The following patterns are not considered problems:

```
@custom-media --sm (min-width: 40rem);

@media (--sm), (max-height: 40rem) {}
```

note

The `@custom-media` name can be used before its declaration

```
@media (--lg) {}

@custom-media --lg (min-width: 60rem);
```

[Previousno-unknown-animations](/user-guide/rules/no-unknown-animations)[Nextno-unknown-custom-properties](/user-guide/rules/no-unknown-custom-properties)

- [Options](#options)

  - [true](#true)
