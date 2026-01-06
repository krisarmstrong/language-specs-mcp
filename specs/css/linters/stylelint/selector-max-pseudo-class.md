On this page

# selector-max-pseudo-class

Limit the number of pseudo-classes in a selector.

```
.foo .bar:first-child:hover {}
/*       ↑           ↑
         ↑           ↑
         1           2 -- this selector contains two pseudo-classes */
```

This rule resolves nested selectors before counting the number of pseudo-classes in a selector. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

The content of the `:not()` pseudo-class is also evaluated separately. The rule processes the argument as if it were an independent selector, and the result does not count toward the total for the entire selector.

## Options[​](#options)

### `number`[​](#number)

Specify a maximum pseudo-classes allowed.

Given:

```
{
  "selector-max-pseudo-class": 1
}
```

The following patterns are considered problems:

```
a:first-child:focus {}
```

```
.foo .bar:first-child:hover {}
```

The following patterns are not considered problems:

```
a {}
```

```
a:first-child {}
```

```
.foo .bar:first-child {}
```

[Previousselector-max-id](/user-guide/rules/selector-max-id)[Nextselector-max-specificity](/user-guide/rules/selector-max-specificity)

- [Options](#options)

  - [number](#number)
