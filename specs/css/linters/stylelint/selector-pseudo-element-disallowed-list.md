On this page

# selector-pseudo-element-disallowed-list

Specify a list of disallowed pseudo-element selectors.

```
  a::before {}
/**  ↑
 * This pseudo-element selector */
```

This rule ignores:

- CSS2 pseudo-elements i.e. those prefixed with a single colon
- selectors that use variable interpolation e.g. `::#{$variable} {}`

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "unprefixed", "pseudo-elements", "/regex/"]
```

Given:

```
{
  "selector-pseudo-element-disallowed-list": ["before", "/^--my-/i"]
}
```

The following patterns are considered problems:

```
a::before {}
```

```
a::--my-pseudo-element {}
```

```
a::--MY-OTHER-pseudo-element {}
```

The following patterns are not considered problems:

```
a::after {}
```

```
a::--not-my-pseudo-element {}
```

[Previousselector-pseudo-element-colon-notation](/user-guide/rules/selector-pseudo-element-colon-notation)[Nextselector-pseudo-element-no-unknown](/user-guide/rules/selector-pseudo-element-no-unknown)

- [Options](#options)

  - [Array<string>](#arraystring)
