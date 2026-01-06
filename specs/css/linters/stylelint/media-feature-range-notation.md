On this page

# media-feature-range-notation

Specify context or prefix notation for media feature ranges.

```
@media (width >= 600px) and (min-width: 600px) {}
/**    ↑                    ↑
 *     These media feature notations */
```

Media features of the range type can be written using prefixes or the more modern context notation.

Because `min-` and `max-` both equate to range comparisons that include the value, they may be [limiting in certain situations](https://drafts.csswg.org/mediaqueries/#mq-min-max).

The [fix option](/user-guide/options#fix) can automatically fix some of the problems reported by this rule.

## Options[​](#options)

### `"context"`[​](#context)

Media feature ranges must always use context notation.

```
{
  "media-feature-range-notation": "context"
}
```

The following patterns are considered problems:

```
@media (min-width: 1px) {}
```

```
@media (min-width: 1px) and (max-width: 2px) {}
```

The following patterns are not considered problems:

```
@media (width >= 1px) {}
```

```
@media (1px <= width <= 2px) {}
```

### `"prefix"`[​](#prefix)

Media feature ranges must always use prefix notation.

```
{
  "media-feature-range-notation": "prefix"
}
```

The following patterns are considered problems:

```
@media (width >= 1px) {}
```

```
@media (1px <= width <= 2px) {}
```

The following patterns are not considered problems:

```
@media (min-width: 1px) {}
```

```
@media (min-width: 1px) and (max-width: 2px) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"exact-value"`[​](#exact-value)

Reverse the primary option for media features with exact values.

Given:

```
{
  "media-feature-range-notation": ["context", { "except": ["exact-value"] }]
}
```

The following pattern is considered a problem:

```
@media (min-width: 1px) {}
```

The following pattern is not considered a problem:

```
@media (width: 1px) {}
```

[Previousmedia-feature-name-value-no-unknown](/user-guide/rules/media-feature-name-value-no-unknown)[Nextmedia-query-no-invalid](/user-guide/rules/media-query-no-invalid)

- [Options](#options)

  - ["context"](#context)
  - ["prefix"](#prefix)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
