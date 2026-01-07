HTML-validate - Require elements to have valid text content (text-content)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require elements to have valid text

Rule ID:text-contentCategory:AccessibilityStandards:

- WCAG 2.2 (AA)
- WCAG 2.1 (AA)
- WCAG 2.0 (AA)

Requires presence or absence of textual content on an element (or one of its children). Whitespace is ignored.

It comes in three variants:

- Text must be absent.
- Text must be present.
- Text must be accessible (regular text or aria attributes).

Bundled HTML5 elements only specify accessible text but custom elements can specify others.

By default this rules validates:

- `<button>`

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<button type="button"></button>
```

```
error: <button> must have accessible text (text-content) at inline:1:2:
> 1 | <button type="button"></button>
    |  ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<!-- regular static text -->
<button type="button">Add item</button>

<!-- text from aria-label -->
<button type="button" aria-label="Add item">
  <i class="fa-solid fa-plus" aria-hidden="true"></i>
</button>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/text-content.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/text-content.ts)
