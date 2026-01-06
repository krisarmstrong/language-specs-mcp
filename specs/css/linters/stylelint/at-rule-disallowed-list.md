On this page

# at-rule-disallowed-list

Specify a list of disallowed at-rules.

```
    @keyframes name {}
/** ↑
 * At-rules like this */
```

This rule ignores the `@charset` rule.

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "unprefixed", "at-rules"]
```

Given:

```
{
  "at-rule-disallowed-list": ["extend", "keyframes"]
}
```

The following patterns are considered problems:

```
a { @extend placeholder; }
```

```
@keyframes name {
  from { top: 10px; }
  to { top: 20px; }
}
```

```
@-moz-keyframes name {
  from { top: 10px; }
  to { top: 20px; }
}
```

The following patterns are not considered problems:

```
@import "path/to/file.css";
```

[Previousat-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)[Nextat-rule-empty-line-before](/user-guide/rules/at-rule-empty-line-before)

- [Options](#options)

  - [Array<string>](#arraystring)
