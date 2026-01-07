HTML-validate - Disallow aria-label and label with same text content (no-redundant-aria-label)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow `aria-label` and `<label>` with same text content

Rule ID:no-redundant-aria-labelCategory:AccessibilityStandards:-

Reports error when an input element (`<input>`, `<textarea>` and `<select>`) contains both the `aria-label` attribute and an associated `<label>` element and both have the same text content.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<label for="foo"> lorem ipsum </label>
<input id="foo" aria-label="lorem ipsum" />
```

```
error: aria-label is redundant when label containing same text exists (no-redundant-aria-label) at inline:2:17:
  1 | <label for="foo"> lorem ipsum </label>
> 2 | <input id="foo" aria-label="lorem ipsum" />
    |                 ^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<!-- different texts -->
<label for="foo"> lorem ipsum </label>
<input id="foo" aria-label="screenreader text" />

<!-- only label -->
<label for="foo"> lorem ipsum </label>
<input id="foo" />
```

## [Version history](#version-history)

- 8.1.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-redundant-aria-label.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-redundant-aria-label.ts)
