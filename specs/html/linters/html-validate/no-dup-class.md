HTML-validate - Disallow duplicated classes (no-dup-class)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows duplicated classes on same element

Rule ID:no-dup-classCategory:HTML syntax and conceptsStandards:-

Prevents unnecessary duplication of class names.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div class="foo bar foo"></div>
```

```
error: Class "foo" duplicated (no-dup-class) at inline:1:21:
> 1 | <div class="foo bar foo"></div>
    |                     ^^^

1 error found.
```

Examples of correct code for this rule:

```
<div class="foo bar"></div>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-dup-class.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-dup-class.ts)
