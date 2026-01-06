On this page

# function-calc-no-unspaced-operator

Disallow invalid unspaced operator within [math functions](https://www.w3.org/TR/css-values-4/#calc-syntax), such as `calc()` or `min()`.

```
a { top: calc(1px + 2px); }
/**               ↑
 * The space around this operator */
```

This rule checks that there is a single whitespace or a newline plus indentation before the `+` or `-` operator, and a single whitespace or a newline after that operator.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `true`[​](#true)

```
{
  "function-calc-no-unspaced-operator": true
}
```

The following patterns are considered problems:

```
a { top: calc(1px+2px); }
```

```
a { top: calc(1px+ 2px); }
```

```
a { transform: rotate(atan(-2+1)); }
```

The following patterns are not considered problems:

```
a { top: calc(1px + 2px); }
```

```
a { top: calc(calc(1em * 2) / 3); }
```

```
a { top: calc(calc(1em*2)/3); }
```

```
a {
  top: calc(var(--foo) +
    var(--bar));
}
```

```
a {
  top: calc(var(--foo)
    + var(--bar));
}
```

[Previousfunction-allowed-list](/user-guide/rules/function-allowed-list)[Nextfunction-disallowed-list](/user-guide/rules/function-disallowed-list)

- [Options](#options)

  - [true](#true)
