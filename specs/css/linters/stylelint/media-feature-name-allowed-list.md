On this page

# media-feature-name-allowed-list

Specify a list of allowed media feature names.

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
  "media-feature-name-allowed-list": ["max-width", "/^my-/"]
}
```

The following patterns are considered problems:

```
@media (min-width: 50em) {}
```

```
@media print and (min-resolution: 300dpi) {}
```

```
@media (min-width < 50em) {}
```

```
@media (10em < min-width < 50em) {}
```

The following patterns are not considered problems:

```
@media (max-width: 50em) {}
```

```
@media (my-width: 50em) {}
```

```
@media (max-width > 50em) {}
```

```
@media (10em < my-width < 50em) {}
```

[Previousmax-nesting-depth](/user-guide/rules/max-nesting-depth)[Nextmedia-feature-name-disallowed-list](/user-guide/rules/media-feature-name-disallowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
