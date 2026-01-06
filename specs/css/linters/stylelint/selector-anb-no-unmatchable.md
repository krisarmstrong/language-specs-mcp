On this page

# selector-anb-no-unmatchable

Disallow unmatchable An+B selectors.

```
a:nth-child(0n+0) {}
/*↑             ↑
 * This unmatchable An+B selector */
```

[An+B selectors](https://www.w3.org/TR/css-syntax-3/#anb-microsyntax) are one-indexed. Selectors that always evaluate to `0` will not match any elements.

## Options[​](#options)

### `true`[​](#true)

```
{
  "selector-anb-no-unmatchable": true
}
```

The following patterns are considered problems:

```
a:nth-child(0) {}
```

```
a:nth-last-child(0n) {}
```

```
a:nth-of-type(0n+0) {}
```

```
a:nth-last-of-type(0 of a) {}
```

The following patterns are not considered problems:

```
a:nth-child(1) {}
```

```
a:nth-last-child(1n) {}
```

```
a:nth-of-type(1n+0) {}
```

```
a:nth-last-of-type(1 of a) {}
```

[Previousrule-selector-property-disallowed-list](/user-guide/rules/rule-selector-property-disallowed-list)[Nextselector-attribute-name-disallowed-list](/user-guide/rules/selector-attribute-name-disallowed-list)

- [Options](#options)

  - [true](#true)
