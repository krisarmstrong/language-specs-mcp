HTML-validate - Require all element references to exist (no-missing-references)Toggle navigation[HTML-validate v10.5.0](/)

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

# No missing references

Rule ID:no-missing-referencesCategory:DocumentStandards:

- HTML5

Require all elements referenced by attributes such as `for` to exist in the current document.

Checked attributes:

- `label[for]`
- `input[list]`
- `*[aria-activedescendant]`
- `*[aria-controls]`
- `*[aria-describedby]`
- `*[aria-details]`
- `*[aria-errormessage]`
- `*[aria-flowto]`
- `*[aria-labelledby]`
- `*[aria-owns]`

A current limitation is that only the `<title>` and `<desc>` elements from an SVG can be referenced.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<label for="missing-input"></label>
<div aria-labelledby="missing-text"></div>
<div aria-describedby="missing-text another-missing"></div>
```

```
error: Element references missing id "missing-input" (no-missing-references) at inline:1:13:
> 1 | <label for="missing-input"></label>
    |             ^^^^^^^^^^^^^
  2 | <div aria-labelledby="missing-text"></div>
  3 | <div aria-describedby="missing-text another-missing"></div>

error: Element references missing id "missing-text" (no-missing-references) at inline:2:23:
  1 | <label for="missing-input"></label>
> 2 | <div aria-labelledby="missing-text"></div>
    |                       ^^^^^^^^^^^^
  3 | <div aria-describedby="missing-text another-missing"></div>

error: Element references missing id "missing-text" (no-missing-references) at inline:3:24:
  1 | <label for="missing-input"></label>
  2 | <div aria-labelledby="missing-text"></div>
> 3 | <div aria-describedby="missing-text another-missing"></div>
    |                        ^^^^^^^^^^^^

error: Element references missing id "another-missing" (no-missing-references) at inline:3:37:
  1 | <label for="missing-input"></label>
  2 | <div aria-labelledby="missing-text"></div>
> 3 | <div aria-describedby="missing-text another-missing"></div>
    |                                     ^^^^^^^^^^^^^^^

4 errors found.
```

Examples of correct code for this rule:

```
<label for="my-input"></label>
<div id="verbose-text"></div>
<div id="another-text"></div>
<div aria-labelledby="verbose-text"></div>
<div aria-describedby="verbose-text another-text"></div>
<input id="my-input">
```

## [Version history](#version-history)

- 6.6.0 - Handle SVG `<title>` and `<desc>`
- 5.5.0 - Extended list of checked aria attributes.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-missing-references.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-missing-references.ts)
