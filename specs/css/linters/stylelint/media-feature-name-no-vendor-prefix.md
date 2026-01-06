On this page

# media-feature-name-no-vendor-prefix

Disallow vendor prefixes for media feature names.

```
@media (-webkit-min-device-pixel-ratio: 1) {}
/**      ↑
 * This prefix */
```

This rule ignores non-standard vendor-prefixed media feature names that aren't handled by [Autoprefixer](https://github.com/postcss/autoprefixer).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule. However, it will not remove duplicate media feature names produced when the prefixes are removed. You can use [Autoprefixer](https://github.com/postcss/autoprefixer) itself, with the [add option off and the remove option on](https://github.com/postcss/autoprefixer#options), in these situations.

## Options[​](#options)

### `true`[​](#true)

```
{
  "media-feature-name-no-vendor-prefix": true
}
```

The following patterns are considered problems:

```
@media (-webkit-min-device-pixel-ratio: 1) {}
```

```
@media (min--mox-device-pixel-ratio: 1) {}
```

```
@media (-o-max-device-pixel-ratio: 1/1) {}
```

The following patterns are not considered problems:

```
@media (min-resolution: 96dpi) {}
```

```
@media (max-resolution: 900dpi) {}
```

[Previousmedia-feature-name-no-unknown](/user-guide/rules/media-feature-name-no-unknown)[Nextmedia-feature-name-unit-allowed-list](/user-guide/rules/media-feature-name-unit-allowed-list)

- [Options](#options)

  - [true](#true)
