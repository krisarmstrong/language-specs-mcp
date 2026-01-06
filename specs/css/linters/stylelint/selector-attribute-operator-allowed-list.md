On this page

# selector-attribute-operator-allowed-list

Specify a list of allowed attribute operators.

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
  "selector-attribute-operator-allowed-list": ["=", "|="]
}
```

The following patterns are considered problems:

```
[class*="test"] {}
```

```
[title~="flower"] {}
```

```
[class^="top"] {}
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

[Previousselector-attribute-name-disallowed-list](/user-guide/rules/selector-attribute-name-disallowed-list)[Nextselector-attribute-operator-disallowed-list](/user-guide/rules/selector-attribute-operator-disallowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
