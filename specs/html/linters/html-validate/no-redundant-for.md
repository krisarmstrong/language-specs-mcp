## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow usage of redundant label for attributes

Rule ID:no-redundant-forCategory:HTML syntax and conceptsStandards:

- HTML5

`<label>` can either use the `for` attribute to reference the labelable control or wrap it. Doing both is redundant as the label already references the control.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<label for="foo">
  <input type="checkbox" id="foo">
  My fancy checkbox
</label>
```

```
error: Redundant "for" attribute (no-redundant-for) at inline:1:8:
> 1 | <label for="foo">
    |        ^^^
  2 |   <input type="checkbox" id="foo">
  3 |   My fancy checkbox
  4 | </label>

1 error found.
```

Examples of correct code for this rule:

```
<!-- without for attribute -->
<label>
  <input type="checkbox">
  My fancy checkbox
</label>

<!-- without wrapping -->
<input type="checkbox" id="foo">
<label for="foo">
  My fancy checkbox
</label>
```
