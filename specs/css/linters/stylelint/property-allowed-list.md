On this page

# property-allowed-list

Specify a list of allowed properties.

```
a { color: red; }
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
  "property-allowed-list": ["display", "animation", "/^background/", "--foo"]
}
```

The following patterns are considered problems:

```
a { color: red; }
```

```
a {
  animation: my-animation 2s;
  color: red;
}
```

```
a { borkgrund: orange; }
```

```
a { --bar: red; }
```

The following patterns are not considered problems:

```
a { display: block; }
```

```
a { -webkit-animation: my-animation 2s; }
```

```
a {
  animation: my-animation 2s;
  -webkit-animation: my-animation 2s;
  display: block;
}
```

```
a { background: red; }
```

```
a { background-color: red; }
```

```
a { --foo: red; }
```

[Previousnumber-max-precision](/user-guide/rules/number-max-precision)[Nextproperty-disallowed-list](/user-guide/rules/property-disallowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
