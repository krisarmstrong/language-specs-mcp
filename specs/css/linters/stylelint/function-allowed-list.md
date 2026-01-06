On this page

# function-allowed-list

Specify a list of allowed functions.

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
  "function-allowed-list": ["scale", "rgba", "/linear-gradient/"]
}
```

The following patterns are considered problems:

```
a { transform: rotate(1); }
```

```
a {
  color: hsla(170, 50%, 45%, 1)
}
```

```
a {
  background:
    red,
    -webkit-radial-gradient(red, green, blue);
}
```

The following patterns are not considered problems:

```
a { background: red; }
```

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

## Optional secondary options[​](#optional-secondary-options)

### `exceptWithoutPropertyFallback`[​](#exceptwithoutpropertyfallback)

```
{
  "exceptWithoutPropertyFallback": [
    "array",
    "of",
    "unprefixed",
    "functions",
    "/regex/"
  ]
}
```

Disallow the matching functions when they are without a property fallback in the same declaration block.

Given:

```
{
  "function-allowed-list": [
    ["scale", "min", "/max/"],
    { "exceptWithoutPropertyFallback": ["min", "/max/"] }
  ]
}
```

The following patterns are considered problems:

```
a { width: min(50%, 100px); }
```

```
a { height: max(50%, 100px); }
```

```
a {
  width: max(50%, 100px);
  width: 100px;
}
```

The following patterns are not considered problems:

```
a { transform: scale(1); }
```

```
a {
  width: 100px;
  width: min(50%, 100px);
}
```

[Previousfont-weight-notation](/user-guide/rules/font-weight-notation)[Nextfunction-calc-no-unspaced-operator](/user-guide/rules/function-calc-no-unspaced-operator)

- [Options](#options)

  - [Array<string>](#arraystring)

- [Optional secondary options](#optional-secondary-options)

  - [exceptWithoutPropertyFallback](#exceptwithoutpropertyfallback)
