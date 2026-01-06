On this page

# selector-max-universal

Limit the number of universal selectors in a selector.

```
    * {}
/** ↑
 * This universal selector */
```

This rule resolves nested selectors before counting the number of universal selectors. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

The logical combinations pseudo-class (e.g. `:not`, `:has`) is also evaluated separately. The rule processes the argument as if it were an independent selector, and the result does not count toward the total for the entire selector.

## Options[​](#options)

### `number`[​](#number)

Specify a maximum universal selectors allowed.

Given:

```
{
  "selector-max-universal": 2
}
```

The following patterns are considered problems:

```
* * * {}
```

```
* * {
  & * {}
}
```

```
* * {
  & > * {}
}
```

The following patterns are not considered problems:

```
* {}
```

```
* * {}
```

```
.foo * {}
```

```
*.foo * {}
```

```
/* each selector in a selector list is evaluated separately */
*.foo,
*.bar * {}
```

```
/* `*` is inside `:not()`, so it is evaluated separately */
* > * .foo:not(*) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAfterCombinators`[​](#ignoreaftercombinators)

```
{ "ignoreAfterCombinators": ["array", "of", "combinators"] }
```

Ignore universal selectors that come after one of the specified combinators.

Given:

```
{
  "selector-max-universal": [2, { "ignoreAfterCombinators": [">", "+"] }]
}
```

The following pattern is not considered a problem:

```
* * > * {}
```

[Previousselector-max-type](/user-guide/rules/selector-max-type)[Nextselector-nested-pattern](/user-guide/rules/selector-nested-pattern)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAfterCombinators](#ignoreaftercombinators)
