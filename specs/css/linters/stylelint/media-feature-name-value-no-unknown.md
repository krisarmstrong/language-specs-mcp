On this page

# media-feature-name-value-no-unknown

Disallow unknown values for media features.

```
@media (color: red) {}
/**     ↑      ↑
 * feature and value pairs like these */
```

This rule considers values for media features defined within the CSS specifications to be known.

This rule is only appropriate for CSS. You should not turn it on for CSS-like languages, such as SCSS or Less.

It sometimes overlaps with:

- [unit-no-unknown](/user-guide/rules/unit-no-unknown)

If duplicate problems are flagged, you can turn off the corresponding rule.

## Options[​](#options)

### `true`[​](#true)

```
{
  "media-feature-name-value-no-unknown": true
}
```

The following patterns are considered problems:

```
@media (color: red) { top: 1px; }
```

```
@media (width: 10) { top: 1px; }
```

```
@media (width: auto) { top: 1px; }
```

The following patterns are not considered problems:

```
@media (color: 8) { top: 1px; }
```

```
@media (width: 10px) { top: 1px; }
```

[Previousmedia-feature-name-value-allowed-list](/user-guide/rules/media-feature-name-value-allowed-list)[Nextmedia-feature-range-notation](/user-guide/rules/media-feature-range-notation)

- [Options](#options)

  - [true](#true)
