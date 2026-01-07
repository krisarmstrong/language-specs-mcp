HTML-validate - Require name and id to match on <map> elements (map-id-name)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require name and id to match on `<map>` elements

Rule ID:map-id-nameCategory:HTML syntax and conceptsStandards:

- HTML5

HTML5 requires that when the `id` attribute is present on a `<map>` element it must have the same value as the required `name` attribute.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<map name="foo" id="bar"></map>
```

```
error: "id" and "name" attribute must be the same on <map> elements (map-id-name) at inline:1:21:
> 1 | <map name="foo" id="bar"></map>
    |                     ^^^

1 error found.
```

Examples of correct code for this rule:

```
<map name="foo" id="foo"></map>
```

## [Version history](#version-history)

- 7.12.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/map-id-name.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/map-id-name.ts)
