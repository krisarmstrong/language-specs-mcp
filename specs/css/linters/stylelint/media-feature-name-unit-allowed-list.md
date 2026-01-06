On this page

# media-feature-name-unit-allowed-list

Specify a list of allowed name and unit pairs within media features.

```
@media (width: 50em) {}
/**     ↑         ↑
 * This media feature name and these units */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
{ "media-feature-name": ["array", "of", "units"] }
```

You can specify a regex for a media feature name, such as `{ "/height$/": [] }`.

Given:

```
{
  "media-feature-name-unit-allowed-list": {
    "width": "em",
    "/height/": ["em", "rem"]
  }
}
```

The following patterns are considered problems:

```
@media (width: 50rem) {}
```

```
@media (height: 1000px) {}
```

```
@media (min-height: 1000px) {}
```

```
@media (height <= 1000px) {}
```

The following patterns are not considered problems:

```
@media (width: 50em) {}
```

```
@media (width <= 50em) {}
```

```
@media (height: 50em) {}
```

```
@media (min-height: 50rem) {}
```

[Previousmedia-feature-name-no-vendor-prefix](/user-guide/rules/media-feature-name-no-vendor-prefix)[Nextmedia-feature-name-value-allowed-list](/user-guide/rules/media-feature-name-value-allowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
