On this page

# selector-pseudo-class-disallowed-list

Specify a list of disallowed pseudo-class selectors.

```
  a:hover {}
/** ↑
 * This pseudo-class selector */
```

This rule ignores selectors that use variable interpolation e.g. `:#{$variable} {}`.

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "unprefixed", "pseudo-classes", "/regex/"]
```

Given:

```
{
  "selector-pseudo-class-disallowed-list": ["hover", "/^nth-/"]
}
```

The following patterns are considered problems:

```
a:hover {}
```

```
a:nth-of-type(5) {}
```

```
a:nth-child(2) {}
```

The following patterns are not considered problems:

```
a:focus {}
```

```
a:first-of-type {}
```

[Previousselector-pseudo-class-allowed-list](/user-guide/rules/selector-pseudo-class-allowed-list)[Nextselector-pseudo-class-no-unknown](/user-guide/rules/selector-pseudo-class-no-unknown)

- [Options](#options)

  - [Array<string>](#arraystring)
