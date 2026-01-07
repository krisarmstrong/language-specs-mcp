HTML-validate - Disallow usage of unknown elements (no-unknown-elements)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow usage of unknown elements

Rule ID:no-unknown-elementsCategory:-Standards:-

This rule requires all elements to have a corresponding metadata element describing its content model.

All HTML5 elements are bundled and enabled by default. For custom elements (and framework components) you need supply your [own metadata](../usage/elements.html):

```
{
  "elements": ["html5", "./my-awesome-elements.js"]
}
```

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<custom-element></custom-element>
```

```
error: Unknown element <custom-element> (no-unknown-elements) at inline:1:1:
> 1 | <custom-element></custom-element>
    | ^^^^^^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<div></div>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "include": [],
  "exclude": []
}
```

### [include](#include)

If set only elements listed in this array generates errors. Supports wildcard with `*` (e.g. `custom-*`) and regexp with `/../` (e.g. `custom-(foo|bar)`).

### [exclude](#exclude)

If set elements listed in this array is ignored. Supports wildcard with `*` (e.g. `custom-*`) and regexp with `/../` (e.g. `custom-(foo|bar)`).

## [Version history](#version-history)

- 7.11.0 - Added support for `include` and `exclude`.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-unknown-elements.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-unknown-elements.ts)
