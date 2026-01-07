HTML-validate - Disallow implicit input type (no-implicit-input-type)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow implicit input type

Rule ID:no-implicit-input-typeCategory:StyleStandards:-

When the `type` attribute is omitted it defaults to `text`. Being explicit about the intended type better conveys the purpose of the input field.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input>
```

```
error: <input> is missing recommended "type" attribute (no-implicit-input-type) at inline:1:2:
> 1 | <input>
    |  ^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input type="text">
```

## [Version history](#version-history)

- 8.10.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-implicit-input-type.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-implicit-input-type.ts)
