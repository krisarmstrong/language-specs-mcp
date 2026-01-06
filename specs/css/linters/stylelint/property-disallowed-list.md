On this page

# property-disallowed-list

Specify a list of disallowed properties.

```
a { text-rendering: optimizeLegibility; }
/** ↑
 * This property */
```

This rule ignores preprocessor variables (e.g. `$sass`, `@less`).

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "properties", "/regex/"]
```

Given:

```
{
  "property-disallowed-list": [
    "text-rendering",
    "animation",
    "/^background/",
    "--foo"
  ]
}
```

The following patterns are considered problems:

```
a { text-rendering: optimizeLegibility; }
```

```
a {
  animation: my-animation 2s;
}
```

```
a {
  --foo: red;
}
```

```
a { -webkit-animation: my-animation 2s; }
```

```
a { background: red; }
```

```
a { background-size: cover; }
```

The following patterns are not considered problems:

```
a { color: red; }
```

```
a { no-background: sure; }
```

```
a {
  --bar: red;
}
```

[Previousproperty-allowed-list](/user-guide/rules/property-allowed-list)[Nextproperty-no-deprecated](/user-guide/rules/property-no-deprecated)

- [Options](#options)

  - [Array<string>](#arraystring)
