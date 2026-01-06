On this page

# media-type-no-deprecated

Disallow deprecated media types.

```
    @media tv {}
/**        ↑
 * Deprecated media type */
```

Several CSS media types defined in earlier specifications have been deprecated and should no longer be used. According to the CSS [media queries specification](https://drafts.csswg.org/mediaqueries-5/#media-types), the following media types are recognized as valid but match nothing:

- `aural`
- `braille`
- `embossed`
- `handheld`
- `projection`
- `speech`
- `tty`
- `tv`

Currently, the recommended media types are:

- `all`
- `screen`
- `print`

The deprecated media types were removed because they were either never widely implemented or their use cases are now better handled by media features rather than broad device categories.

## Options[​](#options)

### `true`[​](#true)

```
{
  "media-type-no-deprecated": true
}
```

The following pattern is considered a problem:

```
@media tty {}
```

The following pattern is not considered a problem:

```
@media screen {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreMediaTypes`[​](#ignoremediatypes)

```
{ "ignoreMediaTypes": ["array", "of", "types", "/regex/"] }
```

Ignore the specified media types.

Given:

```
{
  "media-type-no-deprecated": [true, { "ignoreMediaTypes": ["/^t/", "speech"] }]
}
```

The following patterns are not considered problems:

```
@media tv {}
```

```
@media tty {}
```

```
@media speech {}
```

[Previousmedia-query-no-invalid](/user-guide/rules/media-query-no-invalid)[Nextnamed-grid-areas-no-invalid](/user-guide/rules/named-grid-areas-no-invalid)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreMediaTypes](#ignoremediatypes)
