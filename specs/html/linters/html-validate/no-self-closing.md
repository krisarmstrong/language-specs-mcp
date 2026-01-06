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
