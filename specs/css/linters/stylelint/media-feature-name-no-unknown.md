On this page

# media-feature-name-no-unknown

Disallow unknown media feature names.

```
@media (min-width: 700px) {}
/**     ↑
 * This media feature name */
```

This rule considers media feature names defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

This rule ignores vendor-prefixed media feature names.

## Options[​](#options)

### `true`[​](#true)

```
{
  "media-feature-name-no-unknown": true
}
```

The following patterns are considered problems:

```
@media screen and (unknown) {}
```

```
@media screen and (unknown: 10px) {}
```

```
@media screen and (unknown > 10px) {}
```

The following patterns are not considered problems:

```
@media all and (monochrome) {}
```

```
@media (min-width: 700px) {}
```

```
@media (MIN-WIDTH: 700px) {}
```

```
@media (min-width: 700px) and (orientation: landscape) {}
```

```
@media (-webkit-min-device-pixel-ratio: 2) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreMediaFeatureNames`[​](#ignoremediafeaturenames)

```
{ "ignoreMediaFeatureNames": ["array", "of", "media-features", "/regex/"] }
```

Given:

```
{
  "media-feature-name-no-unknown": [
    true,
    { "ignoreMediaFeatureNames": ["/^my-/", "custom"] }
  ]
}
```

The following patterns are not considered problems:

```
@media screen and (my-media-feature-name) {}
```

```
@media screen and (custom: 10px) {}
```

```
@media screen and (100px < custom < 700px) {}
```

```
@media (min-width: 700px) and (custom: 10px) {}
```

[Previousmedia-feature-name-disallowed-list](/user-guide/rules/media-feature-name-disallowed-list)[Nextmedia-feature-name-no-vendor-prefix](/user-guide/rules/media-feature-name-no-vendor-prefix)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreMediaFeatureNames](#ignoremediafeaturenames)
