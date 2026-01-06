On this page

# number-max-precision

Limit the number of decimal places allowed in numbers.

```
a { top: 3.245634px; }
/**           ↑
 * This decimal place */
```

## Options[​](#options)

### `number`[​](#number)

Specify a maximum number of decimal places allowed.

Given:

```
{
  "number-max-precision": 2
}
```

The following patterns are considered problems:

```
a { top: 3.245px; }
```

```
a { top: 3.245634px; }
```

```
@media (min-width: 3.234em) {}
```

The following patterns are not considered problems:

```
a { top: 3.24px; }
```

```
@media (min-width: 3.23em) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Ignore the precision of numbers for the specified properties.

Given:

```
{
  "number-max-precision": [0, { "ignoreProperties": ["transition"] }]
}
```

The following patterns are considered problems:

```
a { top: 10.5px; }
```

The following patterns are not considered problems:

```
a { transition: all 4.5s ease; }
```

### `ignoreUnits`[​](#ignoreunits)

```
{ "ignoreUnits": ["array", "of", "units", "/regex/"] }
```

Ignore the precision of numbers for values with the specified units.

Given:

```
{
  "number-max-precision": [2, { "ignoreUnits": ["/^my-/", "%"] }]
}
```

The following patterns are considered problems:

```
a { top: 3.245px; }
```

```
a { top: 3.245634px; }
```

```
@media (min-width: 3.234em) {}
```

The following patterns are not considered problems:

```
a { top: 3.245%; }
```

```
@media (min-width: 3.23em) {}
```

```
a {
  width: 10.5432%;
}
```

```
a { top: 3.245my-unit; }
```

```
a {
  width: 10.989my-other-unit;
}
```

### `insideFunctions`[​](#insidefunctions)

```
{ "insideFunctions": { "function-name": 0 } }
```

You can specify a regex for a function name, such as `{ "/^(oklch|oklab)$/": 0 }`.

The `insideFunctions` option can change a primary option value for specified functions.

Given:

```
{
  "number-max-precision": [
    2,
    { "insideFunctions": { "/^(oklch|oklab|lch|lab)$/": 4 } }
  ]
}
```

The following patterns are considered problems:

```
a { color: rgb(127.333 0 0); }
```

```
a { color: rgb(calc(127.333 / 3) 0 0); }
```

The following patterns are not considered problems:

```
a { color: oklch(0.333 0 0); }
```

```
a { color: lab(0.3333 0 0); }
```

```
a { color: oklab(calc(127.333 / 3) 0 0); }
```

[Previousno-unknown-custom-properties](/user-guide/rules/no-unknown-custom-properties)[Nextproperty-allowed-list](/user-guide/rules/property-allowed-list)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
  - [ignoreUnits](#ignoreunits)
  - [insideFunctions](#insidefunctions)
