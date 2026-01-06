On this page

# unit-disallowed-list

Specify a list of disallowed units.

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
  "unit-disallowed-list": ["px", "em", "deg"]
}
```

The following patterns are considered problems:

```
a { width: 100px; }
```

```
a { font-size: 10em; }
```

```
a { transform: rotate(30deg); }
```

The following patterns are not considered problems:

```
a { font-size: 1.2rem; }
```

```
a { line-height: 1.2; }
```

```
a { height: 100vmin; }
```

```
a { animation: animation-name 5s ease; }
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
  "unit-disallowed-list": [
    ["px", "vmin"],
    {
      "ignoreProperties": {
        "px": ["font-size", "/^border/"],
        "vmin": "width"
      }
    }
  ]
}
```

The following patterns are not considered problems:

```
a { font-size: 13px; }
```

```
a { border-bottom-width: 6px; }
```

```
a { width: 100vmin; }
```

The following patterns are considered problems:

```
a { line-height: 12px; }
```

```
a { -moz-border-radius-topright: 40px; }
```

```
a { height: 100vmin; }
```

### `ignoreMediaFeatureNames`[​](#ignoremediafeaturenames)

```
{
  "ignoreMediaFeatureNames": {
    "unit": ["array", "of", "feature-names", "/regex/"]
  }
}
```

Ignore units for specific feature names.

Given:

```
{
  "unit-disallowed-list": [
    ["px", "dpi"],
    {
      "ignoreMediaFeatureNames": {
        "px": ["min-width", "/height$/"],
        "dpi": "resolution"
      }
    }
  ]
}
```

The following patterns are not considered problems:

```
@media (min-width: 960px) {}
```

```
@media (max-height: 280px) {}
```

```
@media not (resolution: 300dpi) {}
```

The following patterns are considered problems:

```
@media screen and (max-device-width: 500px) {}
```

```
@media all and (min-width: 500px) and (max-width: 200px) {}
```

```
@media print and (max-resolution: 100dpi) {}
```

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": { "unit": ["array", "of", "functions", "/regex/"] } }
```

Ignore units that are inside of the specified functions.

Given:

```
{
  "unit-disallowed-list": [
    ["px"],
    { "ignoreFunctions": ["calc", "/^translate/"] }
  ]
}
```

The following patterns are not considered problems:

```
a { margin: calc(50% - 100px) }
```

```
a { transform: translateX(100px) }
```

[Previousunit-allowed-list](/user-guide/rules/unit-allowed-list)[Nextunit-no-unknown](/user-guide/rules/unit-no-unknown)

- [Options](#options)

  - [Array<string>](#arraystring)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
  - [ignoreMediaFeatureNames](#ignoremediafeaturenames)
  - [ignoreFunctions](#ignorefunctions)
