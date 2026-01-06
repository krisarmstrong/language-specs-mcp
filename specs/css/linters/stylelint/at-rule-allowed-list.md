On this page

# at-rule-allowed-list

Specify a list of allowed at-rules.

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
  "at-rule-allowed-list": ["extend", "keyframes"]
}
```

The following patterns are considered problems:

```
@import "path/to/file.css";
```

```
@media screen and (max-width: 1024px) {
  a { display: none; }
}
```

The following patterns are not considered problems:

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
@KEYFRAMES name {
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

[Previousannotation-no-unknown](/user-guide/rules/annotation-no-unknown)[Nextat-rule-descriptor-no-unknown](/user-guide/rules/at-rule-descriptor-no-unknown)

- [Options](#options)

  - [Array<string>](#arraystring)
