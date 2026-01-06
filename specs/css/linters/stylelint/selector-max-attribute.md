On this page

# selector-max-attribute

Limit the number of attribute selectors in a selector.

```
    [rel="external"] {}
/** ↑
 * This type of selector */
```

This rule resolves nested selectors before counting the number of attribute selectors. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

The `:not()` pseudo-class is also evaluated separately. The rule processes the argument as if it were an independent selector, and the result does not count toward the total for the entire selector.

## Options[​](#options)

### `number`[​](#number)

Specify a maximum attribute selectors allowed.

Given:

```
{
  "selector-max-attribute": 2
}
```

The following patterns are considered problems:

```
[type="number"][name="quality"][data-attribute="value"] {}
```

```
[type="number"][name="quality"][disabled] {}
```

```
[type="number"][name="quality"] {
  & [data-attribute="value"] {}
}
```

```
[type="number"][name="quality"] {
  & [disabled] {}
}
```

```
[type="number"][name="quality"] {
  & > [data-attribute="value"] {}
}
```

```
/* `[type="text"][data-attribute="value"][disabled]` is inside `:not()`, so it is evaluated separately */
input:not([type="text"][data-attribute="value"][disabled]) {}
```

The following patterns are not considered problems:

```
[type="text"] {}
```

```
[type="text"][name="message"] {}
```

```
[type="text"][disabled] {}
```

```
/* each selector in a selector list is evaluated separately */
[type="text"][name="message"],
[type="number"][name="quality"] {}
```

```
/* `[disabled]` is inside `:not()`, so it is evaluated separately */
[type="text"][name="message"]:not([disabled]) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAttributes`[​](#ignoreattributes)

```
{ "ignoreAttributes": ["array", "of", "attributes", "/regex/"] }
```

Given:

```
{
  "selector-max-attribute": [0, { "ignoreAttributes": ["/^data-my-/", "dir"] }]
}
```

The following patterns are not considered problems:

```
[dir] [data-my-attr] {}
```

```
[dir] [data-my-other-attr] {}
```

[Previousselector-id-pattern](/user-guide/rules/selector-id-pattern)[Nextselector-max-class](/user-guide/rules/selector-max-class)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAttributes](#ignoreattributes)
