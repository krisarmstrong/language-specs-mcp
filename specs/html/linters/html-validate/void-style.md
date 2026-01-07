HTML-validate - Require a specific style for closing void elements (void-style)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require a specific style for closing void elements

Rule ID:void-styleCategory:StyleStandards:-

HTML [void elements](https://www.w3.org/TR/html5/syntax.html#void-elements) are elements which cannot have content. Void elements are implicitly closed (`<img>`) but may optionally be XML-style self-closed (`<img/>`).

This rules enforces usage of one of the two styles. Default is to omit self-closing tag.

This rule has no effect on non-void elements, see the related rule [no-self-closing](no-self-closing.html).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input/>
```

```
error: Expected omitted end tag <input> instead of self-closing element <input/> (void-style) at inline:1:7:
> 1 | <input/>
    |       ^^

1 error found.
```

Examples of correct code for this rule:

```
<input>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "omit"
}
```

### [Style](#style)

- `omit` requires end tag to be omitted and disallows self-closing elements (default).
- `selfclosing` requests self-closing all void element.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/void-style.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/void-style.ts)
