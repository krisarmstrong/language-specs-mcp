On this page

# selector-attribute-name-disallowed-list

Specify a list of disallowed attribute names.

```
    [class~="foo"] {}
/**  ↑
 * This name */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "attribute-names", "/regex/"]
```

Given:

```
{
  "selector-attribute-name-disallowed-list": ["class", "id", "/^data-/"]
}
```

The following patterns are considered problems:

```
[class*="foo"] {}
```

```
[id~="bar"] {}
```

```
[data-foo*="bar"] {}
```

The following patterns are not considered problems:

```
[lang~="en-us"] {}
```

```
[target="_blank"] {}
```

```
[href$=".bar"] {}
```

[Previousselector-anb-no-unmatchable](/user-guide/rules/selector-anb-no-unmatchable)[Nextselector-attribute-operator-allowed-list](/user-guide/rules/selector-attribute-operator-allowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
