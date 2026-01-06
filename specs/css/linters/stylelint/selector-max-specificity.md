On this page

# selector-max-specificity

Limit the specificity of selectors.

```
    .foo, #bar.baz span, #hoo { color: pink; }
/** ↑     ↑              ↑
 * Each of these selectors */
```

Visit the [Specificity Calculator](https://specificity.keegan.st) for visual representation of selector specificity.

This rule ignores selectors with variable interpolation (`#{$var}`, `@{var}`, `$(var)`).

This rule resolves nested selectors before counting the specificity of a selector. Each selector in a [selector list](https://www.w3.org/TR/selectors4/#selector-list) is evaluated separately.

## Options[​](#options)

### `string`[​](#string)

Specify a maximum specificity allowed.

The format is `"id,class,type"`, as laid out in the [W3C selector spec](https://drafts.csswg.org/selectors/#specificity-rules).

Given:

```
{
  "selector-max-specificity": "0,2,0"
}
```

The following patterns are considered problems:

```
#foo {}
```

```
.foo .baz .bar {}
```

```
.foo .baz {
  & .bar {}
}
```

```
.foo {
  color: red;
  @nest .baz .bar & {
    color: blue;
  }
}
```

The following patterns are not considered problems:

```
div {}
```

```
.foo div {}
```

```
.foo div {
  & div a {}
}
```

```
.foo {
  & .baz {}
}
```

```
.foo {
  color: red;
  @nest .baz & {
    color: blue;
  }
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreSelectors`[​](#ignoreselectors)

```
{ "ignoreSelectors": ["array", "of", "selectors", "/regex/"] }
```

Given:

```
{
  "selector-max-specificity": [
    "0,2,0",
    {
      "ignoreSelectors": [":host", ":host-context", "/^my-/"]
    }
  ]
}
```

The following patterns are not considered problems:

```
:host(.foo) .bar {}
```

```
:host-context(.foo.bar) {}
```

```
:host-context(.foo, :host(.bar).baz) {}
```

```
my-element.foo.bar {}
```

The following patterns are considered problems:

```
:host(.foo) .bar.baz {}
```

```
:host-context(.foo.bar.baz) {}
```

```
:host-context(.foo, :host(.bar), .foo.bar.baz) {}
```

```
my-element.foo.bar.baz {}
```

[Previousselector-max-pseudo-class](/user-guide/rules/selector-max-pseudo-class)[Nextselector-max-type](/user-guide/rules/selector-max-type)

- [Options](#options)

  - [string](#string)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreSelectors](#ignoreselectors)
