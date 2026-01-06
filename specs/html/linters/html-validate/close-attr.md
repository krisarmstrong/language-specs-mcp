## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow end tags from having attributes

Rule ID:close-attrCategory:HTML syntax and conceptsStandards:

- HTML5

HTML disallows end tags to have attributes.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div></div id="foo">
```

```
error: Close tags cannot have attributes (close-attr) at inline:1:12:
> 1 | <div></div id="foo">
    |            ^^

1 error found.
```

Examples of correct code for this rule:

```
<div id="foo"></div>
```
