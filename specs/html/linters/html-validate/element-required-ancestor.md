HTML-validate - Validate required element ancestors (element-required-ancestor)Toggle navigation[HTML-validate v10.5.0](/)

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

# Validate required element ancestors

Rule ID:element-required-ancestorCategory:Content modelStandards:

- HTML5

HTML defines requirements for required ancestors on certain elements.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<area>
```

```
error: <area> element requires a <map> or <template> ancestor (element-required-ancestor) at inline:1:2:
> 1 | <area>
    |  ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<map>
    <area>
</map>
```

## [Version history](#version-history)

- 7.2.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-required-ancestor.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-required-ancestor.ts)
