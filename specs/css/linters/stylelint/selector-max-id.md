On this page

# selector-max-id

Limit the number of ID selectors in a selector.

```
    #foo {}
/** ↑
 * This type of selector */
```

This rule resolves nested selectors before counting the number of ID selectors. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

The `:not()` pseudo-class is also evaluated separately. The rule processes the argument as if it were an independent selector, and the result does not count toward the total for the entire selector.

## Options[​](#options)

### `number`[​](#number)

Specify a maximum universal selectors allowed.

Given:

```
{
  "selector-max-id": 2
}
```

The following patterns are considered problems:

```
#foo #bar #baz {}
```

```
#foo #bar {
  & #baz {}
}
```

```
#foo #bar {
  & > #bar {}
}
```

The following patterns are not considered problems:

```
#foo {}
```

```
#foo #bar {}
```

```
.foo #foo {}
```

```
#foo.foo #bar {}
```

```
/* each selector in a selector list is evaluated separately */
#foo,
#baz #quux {}
```

```
/* `#bar` is inside `:not()`, so it is evaluated separately */
#foo #bar:not(#baz) {}
```

## Optional secondary options[​](#optional-secondary-options)

### `checkContextFunctionalPseudoClasses`[​](#checkcontextfunctionalpseudoclasses)

```
{
  "checkContextFunctionalPseudoClasses": [
    "array",
    "of",
    "pseudo-classes",
    "/regex/"
  ]
}
```

Check selectors inside of the specified custom [functional pseudo-classes](https://drafts.csswg.org/selectors-4/#pseudo-classes) that provide [evaluation contexts](https://drafts.csswg.org/selectors-4/#specificity-rules).

This option has a higher precedence than `ignoreContextFunctionalPseudoClasses`.

Given:

```
{
  "selector-max-id": [2, { "checkContextFunctionalPseudoClasses": [":--foo"] }]
}
```

The following pattern is considered a problem:

```
:--foo(#foo #bar #baz) {}
```

The following pattern is not considered a problem:

```
:--foo() {}
```

### `ignoreContextFunctionalPseudoClasses`[​](#ignorecontextfunctionalpseudoclasses)

```
{
  "ignoreContextFunctionalPseudoClasses": [
    "array",
    "of",
    "pseudo-classes",
    "/regex/"
  ]
}
```

Ignore selectors inside of the specified [functional pseudo-classes](https://drafts.csswg.org/selectors-4/#pseudo-classes) that provide [evaluation contexts](https://drafts.csswg.org/selectors-4/#specificity-rules).

Given:

```
{
  "selector-max-id": [
    0,
    { "ignoreContextFunctionalPseudoClasses": [":not", "/^:(h|H)as$/"] }
  ]
}
```

The following patterns are considered problems:

```
a:is(#foo) {}
```

The following patterns are not considered problems:

```
a:not(#foo) {}
```

```
a:has(#foo) {}
```

[Previousselector-max-compound-selectors](/user-guide/rules/selector-max-compound-selectors)[Nextselector-max-pseudo-class](/user-guide/rules/selector-max-pseudo-class)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [checkContextFunctionalPseudoClasses](#checkcontextfunctionalpseudoclasses)
  - [ignoreContextFunctionalPseudoClasses](#ignorecontextfunctionalpseudoclasses)
