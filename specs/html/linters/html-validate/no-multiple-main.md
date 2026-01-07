HTML-validate - Disallow multiple `<main>` (no-multiple-main)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows multiple `<main>` elements in the same document

Rule ID:no-multiple-mainCategory:Content modelStandards:

- HTML5

HTML5 [disallows](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) multiple visible `<main>` element in the same document. Multiple `<main>` can be present but at most one can be visible and the others must be hidden using the `hidden` attribute.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<main>foo</main>
<main>bar</main>
```

```
error: Multiple <main> elements present in document (no-multiple-main) at inline:2:2:
  1 | <main>foo</main>
> 2 | <main>bar</main>
    |  ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<main>foo</main>
<main hidden>bar</main>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-multiple-main.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-multiple-main.ts)
