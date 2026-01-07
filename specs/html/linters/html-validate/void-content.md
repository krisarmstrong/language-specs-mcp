HTML-validate - Disallow void element with content (void-content)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows void element with content

Rule ID:void-contentCategory:Content modelStandards:

- HTML5

HTML [void elements](https://www.w3.org/TR/html5/syntax.html#void-contents) cannot have any content and must not have an end tag.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<img></img>
```

```
error: End tag for <img> must be omitted (void-content) at inline:1:7:
> 1 | <img></img>
    |       ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<img>
<img/>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/void-content.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/void-content.ts)
