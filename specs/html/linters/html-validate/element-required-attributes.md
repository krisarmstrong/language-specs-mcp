HTML-validate - Ensure required attributes are set (element-required-attributes)Toggle navigation[HTML-validate v10.5.0](/)

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

# Ensure required attributes are set

Rule ID:element-required-attributesCategory:Content modelStandards:

- HTML5

Ensures required attributes are present but may be empty. Use [attribute-allowed-values](attribute-allowed-values.html) rule to disallow certain values.

The requirements comes from the [element metadata](../usage/elements.html):

```
{
  "img": {
    "attributes": {
      "src": {
        "required": true
      }
    }
  }
}
```

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<img>
```

```
error: <img> is missing required "src" attribute (element-required-attributes) at inline:1:2:
> 1 | <img>
    |  ^^^

1 error found.
```

Examples of correct code for this rule:

```
<img src="cat.gif">
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-required-attributes.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-required-attributes.ts)
