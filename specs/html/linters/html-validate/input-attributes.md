## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Validates usage of input attributes

Rule ID:input-attributesCategory:Content modelStandards:

- HTML5

The `<input>` element uses the `type` attribute to set what type of input field it is. Depending on what type of input field it is many other attributes is allowed or disallowed.

For instance, the `step` attribute can be used with numerical fields but not with textual input.

This rule validates the usage of these attributes, ensuring the attributes are used only in the proper context.

See [HTML5 specification](https://html.spec.whatwg.org/multipage/input.html#concept-input-apply) for a table of attributes and types.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input type="text" step="5">
```

```
error: Attribute "step" is not allowed on <input type="text"> (input-attributes) at inline:1:20:
> 1 | <input type="text" step="5">
    |                    ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input type="number" step="5">
```

## [Version history](#version-history)

- 8.15.0 - This rule no longer checks the `autocomplete` attribute, use [valid-autocomplete](valid-autocomplete.html) instead.
- v4.14.0 - Rule added.
