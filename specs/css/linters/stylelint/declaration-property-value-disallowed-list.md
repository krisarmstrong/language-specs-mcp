On this page

# declaration-property-value-disallowed-list

Specify a list of disallowed property and value pairs within declarations.

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

The same goes for values. Keep in mind that a regular expression value is matched against the entire value of the declaration, not specific parts of it. For example, a value like `"10px solid rgba( 255 , 0 , 0 , 0.5 )"` will not match `"/^solid/"` (notice beginning of the line boundary) but will match `"/\\s+solid\\s+/"` or `"/\\bsolid\\b/"`.

Be careful with regex matching not to accidentally consider quoted string values and `url()` arguments. For example, `"/red/"` will match value such as `"1px dotted red"` as well as `"\"foo\""` and `"white url(/mysite.com/red.png)"`.

Given:

```
{
  "declaration-property-value-disallowed-list": {
    "transform": ["/scale3d/", "/rotate3d/", "/translate3d/"],
    "position": ["fixed"],
    "color": ["/^green/"],
    "/^animation/": ["/ease/"]
  }
}
```

The following patterns are considered problems:

```
a { position: fixed; }
```

```
a { transform: scale3d(1, 2, 3); }
```

```
a { -webkit-transform: scale3d(1, 2, 3); }
```

```
a { color: green; }
```

```
a { animation: foo 2s ease-in-out; }
```

```
a { animation-timing-function: ease-in-out; }
```

```
a { -webkit-animation-timing-function: ease-in-out; }
```

The following patterns are not considered problems:

```
a { position: relative; }
```

```
a { transform: scale(2); }
```

```
a { -webkit-transform: scale(2); }
```

```
a { color: lightgreen; }
```

```
a { animation: foo 2s linear; }
```

```
a { animation-timing-function: linear; }
```

```
a { -webkit-animation-timing-function: linear; }
```

[Previousdeclaration-property-value-allowed-list](/user-guide/rules/declaration-property-value-allowed-list)[Nextdeclaration-property-value-keyword-no-deprecated](/user-guide/rules/declaration-property-value-keyword-no-deprecated)

- [Options](#options)

  - [Object<string, Array<string>>](#objectstring-arraystring)
