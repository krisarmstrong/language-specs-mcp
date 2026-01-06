On this page

# declaration-property-unit-disallowed-list

Specify a list of disallowed property and unit pairs within declarations.

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
  "declaration-property-unit-disallowed-list": {
    "font-size": ["em", "px"],
    "/^animation/": ["s"]
  }
}
```

The following patterns are considered problems:

```
a { font-size: 1em; }
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

The following patterns are not considered problems:

```
a { font-size: 1.2rem; }
```

```
a { height: 100px; }
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

[Previousdeclaration-property-unit-allowed-list](/user-guide/rules/declaration-property-unit-allowed-list)[Nextdeclaration-property-value-allowed-list](/user-guide/rules/declaration-property-value-allowed-list)

- [Options](#options)

  - [Object<string, Array<string>>](#objectstring-arraystring)
