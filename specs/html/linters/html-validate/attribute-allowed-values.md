HTML-validate - Validate permitted attribute values (attribute-allowed-values)Toggle navigation[HTML-validate v10.5.0](/)

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

# Allowed attribute values

Rule ID:attribute-allowed-valuesCategory:Content modelStandards:

- HTML5

Validates attributes for allowed values. Enumerated string values are matched case insensitive while regular expressions are matched case sensitive unless `/i` is used.

Use [element-required-attributes](/rules/element-required-attributes.html) to validate presence of attributes.

The requirements comes from the [element metadata](/usage/elements.html):

```
{
  "input": {
    "attributes": {
      "type": {
        "enum": ["text", "email", "..."]
      }
    }
  }
}
```

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<a href>...</a>
<input type="foobar">
```

```
error: Attribute "href" is missing value (attribute-allowed-values) at inline:1:4:
> 1 | <a href>...</a>
    |    ^^^^
  2 | <input type="foobar">

error: Attribute "type" has invalid value "foobar" (attribute-allowed-values) at inline:2:14:
  1 | <a href>...</a>
> 2 | <input type="foobar">
    |              ^^^^^^

2 errors found.
```

Examples of correct code for this rule:

```
<a href="page.html">...</a>
<input type="text">
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/attribute-allowed-values.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/attribute-allowed-values.ts)
