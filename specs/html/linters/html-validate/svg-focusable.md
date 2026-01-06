## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require `<svg>` elements to have focusable attribute

Rule ID:svg-focusableCategory:AccessibilityStandards:-

Inline SVG elements in IE are focusable by default which may cause issues with tab-ordering. For instance, if a link or button has an SVG icon inside the user would need to press tab twice to move focus to the next element as pressing tab would move focus to the `<svg>` element instead. Edge and other browsers implements proper support for `tabindex` and are unaffected by this bug.

If support for IE is required the `focusable` attribute should explicitly be set to `true` or `false` to avoid unintended behavior. Otherwise this rule can safely be disabled.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<a href="#">
	<svg></svg>
</a>
```

```
error: <svg> is missing required "focusable" attribute (svg-focusable) at inline:2:3:
  1 | <a href="#">
> 2 | 	<svg></svg>
    | 	 ^^^
  3 | </a>

1 error found.
```

Examples of correct code for this rule:

```
<a href="#">
	<svg focusable="false"></svg>
</a>
```
