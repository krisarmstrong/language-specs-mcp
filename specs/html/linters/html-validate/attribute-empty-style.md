## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Empty attribute style

Rule ID:attribute-empty-styleCategory:StyleStandards:

- HTML5

Attributes without a value is implied to be an empty string by the [HTML5 standard](https://html.spec.whatwg.org/multipage/syntax.html#attributes-2), e.g. `<a download>` and `<a download="">` are equal. This rule requires a specific style when writing empty attributes. Default is to omit the empty string `""`.

This rule does not have an effect on boolean attributes, see [attribute-boolean-style](attribute-boolean-style.html) instead.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<a download=""></a>
```

```
error: Attribute "download" should omit value (attribute-empty-style) at inline:1:4:
> 1 | <a download=""></a>
    |    ^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<a download></a>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "omit"
}
```

### [Style](#style)

- `omit` require empty attributes to omit value, e.g. `<a download></a>`
- `empty` require empty attributes to be empty string, e.g. `<a download=""></a>`
