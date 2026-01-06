On this page

# declaration-property-value-allowed-list

Specify a list of allowed property and value pairs within declarations.

```
a { text-transform: uppercase; }
/** ↑               ↑
 * These properties and these values */
```

## Options[​](#options)

### `Object<string, Array<string>>`[​](#objectstring-arraystring)

```
{ "unprefixed-property-name": ["array", "of", "values", "/regex/"] }
```

You can specify a regex for a property name, such as `{ "/^animation/": [] }`.

If a property name is found in the object, only the listed property values are allowed. This rule complains about all non-matching values. (If the property name is not included in the object, anything goes.)

The same goes for values. Keep in mind that a regular expression value is matched against the entire value of the declaration, not specific parts of it. For example, a value like `"10px solid rgba( 255 , 0 , 0 , 0.5 )"` will not match `"/^solid/"` (notice beginning of the line boundary) but will match `"/\\s+solid\\s+/"` or `"/\\bsolid\\b/"`.

Be careful with regex matching not to accidentally consider quoted string values and `url()` arguments. For example, `"/red/"` will match value such as `"1px dotted red"` as well as `"\"red\""` and `"white url(/mysite.com/red.png)"`.

Given:

```
{
  "declaration-property-value-allowed-list": {
    "transform": ["/scale/"],
    "whitespace": ["nowrap"],
    "/color/": ["/^green/"]
  }
}
```

The following patterns are considered problems:

```
a { whitespace: pre; }
```

```
a { transform: translate(1, 1); }
```

```
a { -webkit-transform: translate(1, 1); }
```

```
a { color: pink; }
```

```
a { background-color: pink; }
```

The following patterns are not considered problems:

```
a { whitespace: nowrap; }
```

```
a { transform: scale(1, 1); }
```

```
a { -webkit-transform: scale(1, 1); }
```

```
a { color: green; }
```

```
a { background-color: green; }
```

[Previousdeclaration-property-unit-disallowed-list](/user-guide/rules/declaration-property-unit-disallowed-list)[Nextdeclaration-property-value-disallowed-list](/user-guide/rules/declaration-property-value-disallowed-list)

- [Options](#options)

  - [Object<string, Array<string>>](#objectstring-arraystring)
