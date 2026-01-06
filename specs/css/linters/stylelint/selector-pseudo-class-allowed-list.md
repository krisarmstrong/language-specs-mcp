On this page

# selector-pseudo-class-allowed-list

Specify a list of allowed pseudo-class selectors.

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
  "selector-pseudo-class-allowed-list": ["hover", "/^nth-/"]
}
```

The following patterns are considered problems:

```
a:focus {}
```

```
a:first-of-type {}
```

The following patterns are not considered problems:

```
a:hover {}
```

```
a:nth-of-type(5) {}
```

```
a:nth-child(2) {}
```

[Previousselector-not-notation](/user-guide/rules/selector-not-notation)[Nextselector-pseudo-class-disallowed-list](/user-guide/rules/selector-pseudo-class-disallowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
