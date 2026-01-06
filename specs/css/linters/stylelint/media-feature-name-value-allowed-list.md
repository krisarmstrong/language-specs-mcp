On this page

# media-feature-name-value-allowed-list

Specify a list of allowed media feature name and value pairs.

```
@media screen and (min-width: 768px) {}
/**                ↑          ↑
 *    These features and values */
```

## Options[​](#options)

### `Object<string, Array<string>>`[​](#objectstring-arraystring)

```
{ "unprefixed-media-feature-name": ["array", "of", "values", "/regex/"] }
```

You can specify a regex for a media feature name, such as `{ "/width$/": [] }`.

If a media feature name is found in the object, only its allowed-listed values are allowed. If the media feature name is not included in the object, anything goes.

Given:

```
{
  "media-feature-name-value-allowed-list": {
    "min-width": ["768px", "1024px"],
    "/resolution/": ["/dpcm$/"]
  }
}
```

The following patterns are considered problems:

```
@media screen and (min-width: 1000px) {}
```

```
@media screen and (min-resolution: 2dpi) {}
```

```
@media screen and (min-width > 1000px) {}
```

The following patterns are not considered problems:

```
@media screen and (min-width: 768px) {}
```

```
@media screen and (min-width: 1024px) {}
```

```
@media screen and (orientation: portrait) {}
```

```
@media screen and (min-resolution: 2dpcm) {}
```

```
@media screen and (resolution: 10dpcm) {}
```

```
@media screen and (768px < min-width) {}
```

[Previousmedia-feature-name-unit-allowed-list](/user-guide/rules/media-feature-name-unit-allowed-list)[Nextmedia-feature-name-value-no-unknown](/user-guide/rules/media-feature-name-value-no-unknown)

- [Options](#options)

  - [Object<string, Array<string>>](#objectstring-arraystring)
