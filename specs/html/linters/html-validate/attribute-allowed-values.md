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
