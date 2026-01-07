HTML-validate - Disallow usage of deprecated attributes (no-deprecated-attr)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows usage of deprecated attributes

Rule ID:no-deprecated-attrCategory:DeprecatedStandards:

- HTML5

HTML5 deprecated many old attributes.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<body bgcolor="red"></body>
```

```
error: Attribute "bgcolor" is deprecated on <body> element (no-deprecated-attr) at inline:1:7:
> 1 | <body bgcolor="red"></body>
    |       ^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<body style="background: red;"></body>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-deprecated-attr.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-deprecated-attr.ts)
