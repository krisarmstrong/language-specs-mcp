On this page

# selector-attribute-operator-disallowed-list

Specify a list of disallowed attribute operators.

```
[target="_blank"] {}
/**    ↑
 * This operator */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "attribute-operators"]
```

Given:

```
{
  "selector-attribute-operator-disallowed-list": ["*="]
}
```

The following patterns are considered problems:

```
[class*="test"] {}
```

The following patterns are not considered problems:

```
[target] {}
```

```
[target="_blank"] {}
```

```
[class|="top"] {}
```

[Previousselector-attribute-operator-allowed-list](/user-guide/rules/selector-attribute-operator-allowed-list)[Nextselector-attribute-quotes](/user-guide/rules/selector-attribute-quotes)

- [Options](#options)

  - [Array<string>](#arraystring)
