HTML-validate - Disallows `aria-hidden` on focusable elements (hidden-focusable)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows `aria-hidden` on focusable elements

Rule ID:hidden-focusableCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

When focusable elements are hidden with `aria-hidden` they are still reachable using conventional means such as a mouse or keyboard but won't be exposed to assistive technology (AT). This is often confusing for users of AT such as screenreaders.

This applies to the element itself and any ancestors as `aria-hidden` applies to all child elements.

To fix this either:

- Remove `aria-hidden`.
- Remove the element from the DOM instead.
- Use `tabindex="-1"` to remove the element from tab order.
- Use `hidden`, `inert` or similar means to hide or disable the element.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<a href="#" aria-hidden="true">
	lorem ipsum
</a>
```

```
error: aria-hidden cannot be used on focusable elements (hidden-focusable) at inline:1:13:
> 1 | <a href="#" aria-hidden="true">
    |             ^^^^^^^^^^^
  2 | 	lorem ipsum
  3 | </a>

1 error found.
```

Examples of correct code for this rule:

```
<a href="#">
	lorem ipsum
</a>
```

## [Version history](#version-history)

- 8.16.0 - Rule handles `inert`, `tabindex="-1"` and `disabled`.
- 8.9.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/hidden-focusable.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/hidden-focusable.ts)
