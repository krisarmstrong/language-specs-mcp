On this page

# declaration-property-unit-allowed-list

Specify a list of allowed property and unit pairs within declarations.

```
a { width: 100px; }
/** ↑         ↑
 * These properties and these units */
```

## Options[​](#options)

### `Object<string, Array<string>>`[​](#objectstring-arraystring)

```
{ "unprefixed-property-name": ["array", "of", "units"] }
```

You can specify a regex for a property name, such as `{ "/^animation/": [] }`.

Given:

```
{
  "declaration-property-unit-allowed-list": {
    "font-size": ["em", "px"],
    "/^animation/": ["s"],
    "line-height": []
  }
}
```

The following patterns are considered problems:

```
a { font-size: 1.2rem; }
```

```
a { animation: animation-name 500ms ease; }
```

```
a { -webkit-animation: animation-name 500ms ease; }
```

```
a { animation-duration: 500ms; }
```

```
a { line-height: 13px; }
```

The following patterns are not considered problems:

```
a { font-size: 1em; }
```

```
a { height: 100px; }
```

```
a { animation: animation-name 5s ease; }
```

```
a { -webkit-animation: animation-name 5s ease; }
```

```
a { animation-duration: 5s; }
```

```
a { line-height: 1; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"inside-function"`[​](#inside-function)

Ignore units that are inside a function.

Given:

```
{
  "declaration-property-unit-allowed-list": [
    {
      "/^border/": ["px"],
      "/^background/": ["%"]
    },
    {
      "ignore": ["inside-function"]
    }
  ]
}
```

The following patterns are not considered problems:

```
a {
  border: 1px solid hsla(162deg, 51%, 35%, 0.8);
}
```

```
a {
  background-image: linear-gradient(hsla(162deg, 51%, 35%, 0.8), hsla(62deg, 51%, 35%, 0.8));
}
```

[Previousdeclaration-property-max-values](/user-guide/rules/declaration-property-max-values)[Nextdeclaration-property-unit-disallowed-list](/user-guide/rules/declaration-property-unit-disallowed-list)

- [Options](#options)

  - [Object<string, Array<string>>](#objectstring-arraystring)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
