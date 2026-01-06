On this page

# unit-allowed-list

Specify a list of allowed units.

```
a { width: 100px; }
/**           ↑
 *  These units */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "units"]
```

Given:

```
{
  "unit-allowed-list": ["px", "em", "deg"]
}
```

The following patterns are considered problems:

```
a { width: 100%; }
```

```
a { font-size: 10rem; }
```

```
a { animation: animation-name 5s ease; }
```

The following patterns are not considered problems:

```
a { font-size: 1.2em; }
```

```
a { line-height: 1.2; }
```

```
a { height: 100px; }
```

```
a { height: 100PX; }
```

```
a { transform: rotate(30deg); }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": { "unit": ["array", "of", "properties", "/regex/"] } }
```

Ignore units in the values of declarations with the specified properties.

Given:

```
{
  "unit-allowed-list": [
    ["px", "em"],
    {
      "ignoreProperties": {
        "rem": ["line-height", "/^border/"],
        "%": ["width"]
      }
    }
  ]
}
```

The following patterns are not considered problems:

```
a { line-height: 0.1rem; }
```

```
a { border-bottom-width: 6rem; }
```

```
a { width: 100%; }
```

The following patterns are considered problems:

```
a { margin: 0 20rem; }
```

```
a { -moz-border-radius-topright: 20rem; }
```

```
a { height: 100%; }
```

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Ignore units that are inside of the specified functions.

Given:

```
{
  "unit-allowed-list": [["px", "em"], { "ignoreFunctions": ["/^hsl/", "calc"] }]
}
```

The following patterns are not considered problems:

```
a {
  border: 1px solid hsl(162deg, 51%, 35%, 0.8);
}
```

```
a {
  background-image: linear-gradient(hsla(162deg, 51%, 35%, 0.8), hsla(62deg, 51%, 35%, 0.8));
}
```

```
a {
  width: calc(100% - 10px);
}
```

[Previoustime-min-milliseconds](/user-guide/rules/time-min-milliseconds)[Nextunit-disallowed-list](/user-guide/rules/unit-disallowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
  - [ignoreFunctions](#ignorefunctions)
