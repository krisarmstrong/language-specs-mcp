HTML-validate - Disallow duplicated attributes (no-dup-attr)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows duplicated attributes on same element

Rule ID:no-dup-attrCategory:HTML syntax and conceptsStandards:

- HTML5

HTML [disallows](https://www.w3.org/TR/html5/syntax.html#attributes-0) two or more attributes with the same (case-insensitive) name.

Browsers handles duplication differently and thus this is a source for bugs.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div class="foo" class="bar"></div>
```

```
error: Attribute "class" duplicated (no-dup-attr) at inline:1:18:
> 1 | <div class="foo" class="bar"></div>
    |                  ^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<div class="foo bar"></div>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-dup-attr.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-dup-attr.ts)
