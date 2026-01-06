On this page

# selector-max-type

Limit the number of type selectors in a selector.

```
    a {}
/** ↑
 * This type of selector */
```

This rule resolves nested selectors before counting the number of type selectors. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

The `:not()` pseudo-class is also evaluated separately. The rule processes the argument as if it were an independent selector, and the result does not count toward the total for the entire selector.

## Options[​](#options)

### `number`[​](#number)

Specify a maximum type selectors allowed.

Given:

```
{
  "selector-max-type": 2
}
```

The following patterns are considered problems:

```
div a span {}
```

```
div a {
  & span {}
}
```

```
div a {
  & > a {}
}
```

The following patterns are not considered problems:

```
div {}
```

```
div a {}
```

```
.foo div a {}
```

```
div.foo a {}
```

```
/* each selector in a selector list is evaluated separately */
div,
a span {}
```

```
/* `span` is inside `:not()`, so it is evaluated separately */
div a .foo:not(span) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"child"`[​](#child)

Discount child type selectors.

Given:

```
{
  "selector-max-type": [2, { "ignore": ["child"] }]
}
```

The following patterns are not considered problems:

```
div span > a {}
```

```
#bar div span > a {}
```

#### `"compounded"`[​](#compounded)

Discount compounded type selectors -- i.e. type selectors chained with other selectors.

Given:

```
{
  "selector-max-type": [2, { "ignore": ["compounded"] }]
}
```

The following patterns are not considered problems:

```
div span a.foo {}
```

```
div span a#bar {}
```

#### `"custom-elements"`[​](#custom-elements)

Discount custom elements.

Given:

```
{
  "selector-max-type": [2, { "ignore": ["custom-elements"] }]
}
```

The following pattern is not considered a problem:

```
div a foo-bar {}
```

#### `"descendant"`[​](#descendant)

Discount descendant type selectors.

Given:

```
{
  "selector-max-type": [2, { "ignore": ["descendant"] }]
}
```

The following patterns are not considered problems:

```
.foo div span a {}
```

```
#bar div span a {}
```

#### `"next-sibling"`[​](#next-sibling)

Discount next-sibling type selectors.

Given:

```
{
  "selector-max-type": [2, { "ignore": ["next-sibling"] }]
}
```

The following patterns are not considered problems:

```
div a + span {}
```

```
#bar + div + span + a + span {}
```

### `ignoreTypes`[​](#ignoretypes)

```
{ "ignoreTypes": ["array", "of", "types", "/regex/"] }
```

Given:

```
{
  "selector-max-type": [2, { "ignoreTypes": ["/^my-/", "custom"] }]
}
```

The following patterns are not considered problems:

```
div a custom {}
```

```
div a my-type {}
```

```
div a my-other-type {}
```

[Previousselector-max-specificity](/user-guide/rules/selector-max-specificity)[Nextselector-max-universal](/user-guide/rules/selector-max-universal)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
  - [ignoreTypes](#ignoretypes)
