HTML-validate - Require attributes to be separated by whitespace (attr-spacing)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require attributes to be separated by whitespace

Rule ID:attr-spacingCategory:HTML syntax and conceptsStandards:

- HTML5

In HTML attributes must be separated by whitespace (commonly a regular space).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input type="submit"class="foo">
```

```
error: No space between attributes (attr-spacing) at inline:1:21:
> 1 | <input type="submit"class="foo">
    |                     ^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input type="submit" class="foo">
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/attr-spacing.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/attr-spacing.ts)
