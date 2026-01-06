On this page

# rule-nesting-at-rule-required-list

Require rules to be nested in specific at-rules.

```
a { color: red; }
/** ↑
 * This rule */
```

## Options[​](#options)

### `Array<string | RegExp>`[​](#arraystring--regexp)

Given:

```
{
  "rule-nesting-at-rule-required-list": ["layer", "/^--foo-/"]
}
```

The following patterns are considered problems:

```
a { color: red; }
```

```
@media all {
  a { color: red; }
}
```

```
a {
  @layer {
    color: red;
  }
}
```

The following patterns are not considered problems:

```
@layer {
  a { color: red; }
}
```

```
@--foo-bar {
  a { color: red; }
}
```

```
@--foo-baz {
  a { color: red; }
}
```

```
@font-face {
  font-family: "foo";
}
```

[Previousrule-empty-line-before](/user-guide/rules/rule-empty-line-before)[Nextrule-selector-property-disallowed-list](/user-guide/rules/rule-selector-property-disallowed-list)

- [Options](#options)

  - [Array<string | RegExp>](#arraystring--regexp)
