## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow labels associated with multiple controls

Rule ID:multiple-labeled-controlsCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

`<label>` can only be associated with a single control at once. It should either wrap a single [labelable](https://html.spec.whatwg.org/multipage/forms.html#category-label) control or use the `for` attribute to reference the control.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<label>
  <input type="text">
  <input type="text">
</label>
```

```
error: <label> is associated with multiple controls (multiple-labeled-controls) at inline:1:2:
> 1 | <label>
    |  ^^^^^
  2 |   <input type="text">
  3 |   <input type="text">
  4 | </label>

1 error found.
```

```
<label for="bar">
  <input type="text" id="foo">
</label>
<input type="text" id="bar">
```

```
error: <label> is associated with multiple controls (multiple-labeled-controls) at inline:1:2:
> 1 | <label for="bar">
    |  ^^^^^
  2 |   <input type="text" id="foo">
  3 | </label>
  4 | <input type="text" id="bar">

1 error found.
```

Examples of correct code for this rule:

```
<label>
  <input type="text">
</label>
```

## [Version history](#version-history)

- 8.19.0 - Rule ignores properly ignores `<input type="hidden">`.
