HTML-validate - Disallow end tags from having attributes (close-attr)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow end tags from having attributes

Rule ID:close-attrCategory:HTML syntax and conceptsStandards:

- HTML5

HTML disallows end tags to have attributes.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div></div id="foo">
```

```
error: Close tags cannot have attributes (close-attr) at inline:1:12:
> 1 | <div></div id="foo">
    |            ^^

1 error found.
```

Examples of correct code for this rule:

```
<div id="foo"></div>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/close-attr.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/close-attr.ts)
