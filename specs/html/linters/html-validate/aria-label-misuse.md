HTML-validate - Disallow `aria-label` and `aria-labelledby` misuse (aria-label-misuse)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow `aria-label` and `aria-labelledby` misuse

Rule ID:aria-label-misuseCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

`aria-label` and `aria-labelledby` are used to set the label of an element when no native text is present or is non-descriptive. The attribute can only be used on the following elements:

- Interactive elements
- Labelable elements
- Landmark elements
- Elements with roles inheriting from widget
- `<area>`
- `<dialog>`
- `<form>` and `<fieldset>`
- `<iframe>`
- `<img>` and `<figure>`
- `<summary>`
- `<table>`, `<td>` and `<th>`

Additionally, this rule ignores custom elements that explicitly declare `aria-label` in metadata. See the section on [custom components](#custom-components) below.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input type="hidden" aria-label="foobar">
```

```
error: "aria-label" cannot be used on this element (aria-label-misuse) at inline:1:22:
> 1 | <input type="hidden" aria-label="foobar">
    |                      ^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input type="text" aria-label="foobar">
```

## [Other namable elements](#other-namable-elements)

While some other elements (such as `<h1>`) allow naming with `aria-label` or `aria-labelledby`, it is generally recommended to avoid it:

- It can hide other textual child content of the element from assistive technologies.
- Risk of conflicting information for assistive technologies and what is rendered visually.

The [ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/) strongly recommends to avoid such usage.

To allow `aria-label` or `aria-labelledby` on any element that allows naming, see the [allowAnyNamable](#allowanynamable) option below.￼

## [Custom components](#custom-components)

When using custom components, if you expect consumers to set `aria-label` or `aria-labelledby` on your component, explicitly declare the `aria-label` attribute:

```
import { defineMetadata } from "html-validate";

export default defineMetadata({
  "awesome-component": {
    attributes: {
      "aria-label": {},
    },
  },
});
```

The mere presence of an `aria-label` declaration ensures this rule allows both `aria-label` and `aria-labelledby` on the component. You do not need to declare `aria-labelledby` explicitly.

## [Options](#options)

This rule takes an optional object:

```
{
  "allowAnyNamable": false
}
```

### [allowAnyNamable](#allowanynamable)

By default this rule disallows `aria-label` or `aria-labelledby` on elements that allow naming but where it is not recommended to do so.

With this option enabled, the following is valid despite not being recommended:

```
<h1 aria-label="Lorem ipsum">dolor sit amet</h1>
```

This option is disabled by default and `html-validate:recommended` but enabled by `html-validate:standard`.

## [Version history](#version-history)

- 10.2.0 - validates `aria-labelledby` in addition to `aria-label`.
- 8.11.0 - `allowAnyNamable` option added.
- 7.17.0 - Allow usage on custom elements.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/aria-label-misuse.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/aria-label-misuse.ts)
