HTML-validate - Require a specific style for boolean attributes (attribute-boolean-style)Toggle navigation[HTML-validate v10.5.0](/)

- [User guide](../usage/index.html)
- [Elements](../guide/metadata/simple-component.html)
- [Rules](index.html)
- [Developers guide](../dev/using-api.html)
- [Changelog](../changelog/index.html)
- [About](../about/index.html)

html-validate-10.5.0

## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Boolean attribute style

Rule ID:attribute-boolean-styleCategory:StyleStandards:

- HTML5

Boolean attributes are attributes without a value and the presence of the attribute is considered a boolean `true` and absence a boolean `false`. The [HTML5 standard](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attributes) allows three styles to write boolean attributes:

- `<input required>` (omitting the value)
- `<input required="">` (empty string)
- `<input required="required">` (attribute name)

This rule requires a specific style when writing boolean attributes. Default is to omit the value.

This rule does not have an effect on regular attributes with empty values, see [attribute-empty-style](attribute-empty-style.html) instead.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input required="">
<input required="required">
```

```
error: Attribute "required" should omit value (attribute-boolean-style) at inline:1:8:
> 1 | <input required="">
    |        ^^^^^^^^
  2 | <input required="required">

error: Attribute "required" should omit value (attribute-boolean-style) at inline:2:8:
  1 | <input required="">
> 2 | <input required="required">
    |        ^^^^^^^^

2 errors found.
```

Examples of correct code for this rule:

```
<input required>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "omit"
}
```

### [Style](#style)

- `omit` require boolean attributes to omit value, e.g. `<input required>`
- `empty` require boolean attributes to be empty string, e.g. `<input required="">`
- `name` require boolean attributes to be the attributes name, e.g. `<input required="required">`

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/attribute-boolean-style.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/attribute-boolean-style.ts)
