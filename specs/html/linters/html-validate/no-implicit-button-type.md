HTML-validate - Disallow implicit button type (no-implicit-button-type)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow implicit button type

Rule ID:no-implicit-button-typeCategory:AccessibilityStandards:-

When the `type` attribute is omitted it defaults to `submit`. Submit buttons are triggered when a keyboard user presses Enter.

As this may or may not be inteded this rule enforces that the `type` attribute be explicitly set to one of the valid types:

- `button` - a generic button.
- `submit` - a submit button.
- `reset`- a button to reset form fields.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<button>My Awesome Button</button>
```

```
error: <button> is missing recommended "type" attribute (no-implicit-button-type) at inline:1:2:
> 1 | <button>My Awesome Button</button>
    |  ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<button type="button">My Awesome Button</button>
```

## [Version history](#version-history)

- 10.3.0 - Rule ignores omitted `type` attribute on `<button>` when used as first child of `<select>`.
- 8.3.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-implicit-button-type.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-implicit-button-type.ts)
