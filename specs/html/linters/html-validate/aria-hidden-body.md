HTML-validate - disallow `aria-hidden` from being set on `<body>` (aria-hidden-body)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow `aria-hidden` from being set on `<body>`

Rule ID:aria-hidden-bodyCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

Requires `aria-hidden` is not used on the `<body>` element.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<body aria-hidden="true"></body>
```

```
error: aria-hidden must not be used on <body> (aria-hidden-body) at inline:1:7:
> 1 | <body aria-hidden="true"></body>
    |       ^^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<body></body>
```

## [Options](#options)

This rule takes no options.

## [Version history](#version-history)

-- 6.3.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/aria-hidden-body.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/aria-hidden-body.ts)
