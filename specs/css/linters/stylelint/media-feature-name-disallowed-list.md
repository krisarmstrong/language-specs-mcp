On this page

# media-feature-name-disallowed-list

Specify a list of disallowed media feature names.

```
@media (min-width: 700px) {}
/**     ↑
 * This media feature name */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "unprefixed", "media-features", "/regex/"]
```

Given:

```
{
  "media-feature-name-disallowed-list": ["max-width", "/^my-/"]
}
```

The following patterns are considered problems:

```
@media (max-width: 50em) {}
```

```
@media (my-width: 50em) {}
```

```
@media (max-width < 50em) {}
```

```
@media (10em < my-height < 50em) {}
```

The following patterns are not considered problems:

```
@media (min-width: 50em) {}
```

```
@media print and (min-resolution: 300dpi) {}
```

```
@media (min-width >= 50em) {}
```

```
@media (10em < width < 50em) {}
```

[Previousmedia-feature-name-allowed-list](/user-guide/rules/media-feature-name-allowed-list)[Nextmedia-feature-name-no-unknown](/user-guide/rules/media-feature-name-no-unknown)

- [Options](#options)

  - [Array<string>](#arraystring)
