On this page

# selector-max-combinators

Limit the number of combinators in a selector.

```
  a > b + c ~ d e { color: pink; }
/** ↑   ↑   ↑  ↑
 * These are combinators */
```

This rule resolves nested selectors before counting the number of combinators selectors. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

## Options[​](#options)

### `number`[​](#number)

Specify a maximum combinators selectors allowed.

Given:

```
{
  "selector-max-combinators": 2
}
```

The following patterns are considered problems:

```
a b ~ c + d {}
```

```
a b ~ c {
  & > d {}
}
```

```
a b {
  & ~ c {
    & + d {}
  }
}
```

The following patterns are not considered problems:

```
a {}
```

```
a b {}
```

```
a b ~ c {}
```

```
a b {
  & ~ c {}
}
```

```
/* each selector in a selector list is evaluated separately */
a b,
c > d {}
```

[Previousselector-max-class](/user-guide/rules/selector-max-class)[Nextselector-max-compound-selectors](/user-guide/rules/selector-max-compound-selectors)

- [Options](#options)

  - [number](#number)
