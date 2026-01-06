On this page

# selector-attribute-quotes

Require or disallow quotes for attribute values.

```
[target="_blank"] {}
/**     ↑      ↑
 * These quotes */
```

The [fix option](/user-guide/options#fix) can automatically fix most of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

Attribute values must always be quoted.

```
{
  "selector-attribute-quotes": "always"
}
```

The following patterns are considered problems:

```
[title=flower] {}
```

```
[class^=top] {}
```

The following patterns are not considered problems:

```
[title] {}
```

```
[target="_blank"] {}
```

```
[class|="top"] {}
```

```
[title~='text'] {}
```

```
[data-attribute='component'] {}
```

### `"never"`[​](#never)

Attribute values must never be quoted.

```
{
  "selector-attribute-quotes": "never"
}
```

The following patterns are considered problems:

```
[target="_blank"] {}
```

```
[class|="top"] {}
```

```
[title~='text'] {}
```

```
[data-attribute='component'] {}
```

The following patterns are not considered problems:

```
[title] {}
```

```
[title=flower] {}
```

```
[class^=top] {}
```

[Previousselector-attribute-operator-disallowed-list](/user-guide/rules/selector-attribute-operator-disallowed-list)[Nextselector-class-pattern](/user-guide/rules/selector-class-pattern)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)
