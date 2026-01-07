HTML-validate - Require a specific case for DOCTYPE (doctype-style)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require a specific case for DOCTYPE

Rule ID:doctype-styleCategory:StyleStandards:-

While DOCTYPE is case-insensitive in the standard this rule requires it to be a specific style. The standard consistently uses uppercase which is the default style for this rule.

Mixed case it not supported.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!Doctype html>
```

```
error: DOCTYPE should be uppercase (doctype-style) at inline:1:1:
> 1 | <!Doctype html>
    | ^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<!DOCTYPE html>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "uppercase"
}
```

### [style](#style)

- `uppercase` requires DOCTYPE to be uppercase.
- `lowercase` requires DOCTYPE to be lowercase.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/doctype-style.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/doctype-style.ts)
