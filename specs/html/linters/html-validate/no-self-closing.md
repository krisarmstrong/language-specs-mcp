HTML-validate - Disallow self-closing elements (no-self-closing)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow self-closing elements

Rule ID:no-self-closingCategory:StyleStandards:

- HTML5

Require regular end tags for elements even if the element has no content, e.g. require `<div></div>` instead of `<div/>`.

This rule has no effect on void elements, see the related rule [void-style](void-style.html).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div/>
```

```
error: <div> must not be self-closed (no-self-closing) at inline:1:5:
> 1 | <div/>
    |     ^^

1 error found.
```

Examples of correct code for this rule:

```
<div></div>

<!-- foreign elements are ignored -->
<svg/>

<!-- elements with XML namespace are ignored -->
<xi:include/>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "ignoreForeign": true,
  "ignoreXML": true
}
```

### [ignoreForeign](#ignoreforeign)

By default foreign elements are ignored by this rule. By setting `ignoreForeign` to `false` foreign elements must not be self-closed either.

```
<svg/>
```

```
error: <svg> must not be self-closed (no-self-closing) at inline:1:5:
> 1 | <svg/>
    |     ^^

1 error found.
```

### [ignoreXML](#ignorexml)

By default elements in XML namespaces are ignored by this rule. By setting `ignoreXML` to `false` elements in XML namespaces must not be self-closed either.

```
<xi:include/>
```

```
error: <xi:include> must not be self-closed (no-self-closing) at inline:1:12:
> 1 | <xi:include/>
    |            ^^

1 error found.
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-self-closing.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-self-closing.ts)
