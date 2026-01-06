On this page

# selector-no-vendor-prefix

Disallow vendor prefixes for selectors.

```
input::-moz-placeholder {}
/**     ↑
 * This prefix */
```

This rule ignores non-standard vendor-prefixed selectors that aren't handled by [Autoprefixer](https://github.com/postcss/autoprefixer).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule. However, it will not remove duplicate selectors produced when the prefixes are removed. You can use [Autoprefixer](https://github.com/postcss/autoprefixer) itself, with the [add option off and the remove option on](https://github.com/postcss/autoprefixer#options), in these situations.

## Options[​](#options)

### `true`[​](#true)

```
{
  "selector-no-vendor-prefix": true
}
```

The following patterns are considered problems:

```
input::-moz-placeholder {}
```

```
:-webkit-full-screen a {}
```

The following patterns are not considered problems:

```
input::placeholder {}
```

```
:full-screen a {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreSelectors`[​](#ignoreselectors)

```
{ "ignoreSelectors": ["array", "of", "selectors", "/regex/"] }
```

Ignore vendor prefixes for selectors.

Given:

```
{
  "selector-no-vendor-prefix": [
    true,
    { "ignoreSelectors": ["::-webkit-input-placeholder", "/-moz-.*/"] }
  ]
}
```

The following patterns are not considered problems:

```
input::-webkit-input-placeholder {
  color: pink;
}

input::-moz-placeholder {
  color: pink;
}
```

[Previousselector-no-qualifying-type](/user-guide/rules/selector-no-qualifying-type)[Nextselector-not-notation](/user-guide/rules/selector-not-notation)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreSelectors](#ignoreselectors)
