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
