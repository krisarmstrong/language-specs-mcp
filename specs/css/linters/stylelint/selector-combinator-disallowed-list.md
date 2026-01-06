On this page

# selector-combinator-disallowed-list

Specify a list of disallowed combinators.

```
  a + b {}
/** ↑
 * This combinator */
```

This rule normalizes the whitespace descendant combinator to be a single space.

This rule ignores [reference combinators](https://www.w3.org/TR/selectors4/#idref-combinators) e.g. `/for/`.

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "combinators"]
```

Given:

```
{
  "selector-combinator-disallowed-list": [">", " "]
}
```

The following patterns are considered problems:

```
a > b {}
```

```
a b {}
```

```
a
b {}
```

The following patterns are not considered problems:

```
a + b {}
```

```
a ~ b {}
```

[Previousselector-combinator-allowed-list](/user-guide/rules/selector-combinator-allowed-list)[Nextselector-disallowed-list](/user-guide/rules/selector-disallowed-list)

- [Options](#options)

  - [Array<string>](#arraystring)
