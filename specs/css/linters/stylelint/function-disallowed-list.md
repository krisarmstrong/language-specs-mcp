On this page

# function-disallowed-list

Specify a list of disallowed functions.

```
a { transform: scale(1); }
/**            ↑
 * This function */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "unprefixed", "functions", "/regex/"]
```

Given:

```
{
  "function-disallowed-list": ["scale", "rgba", "/linear-gradient/"]
}
```

The following patterns are considered problems:

```
a { transform: scale(1); }
```

```
a {
  color: rgba(0, 0, 0, 0.5);
}
```

```
a {
  background:
    red,
    -moz-linear-gradient(45deg, blue, red);
}
```

The following patterns are not considered problems:

```
a { background: red; }
```

[Previousfunction-calc-no-unspaced-operator](/user-guide/rules/function-calc-no-unspaced-operator)[Nextfunction-linear-gradient-no-nonstandard-direction](/user-guide/rules/function-linear-gradient-no-nonstandard-direction)

- [Options](#options)

  - [Array<string>](#arraystring)
