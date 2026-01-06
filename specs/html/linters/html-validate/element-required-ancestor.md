## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Validate required element ancestors

Rule ID:element-required-ancestorCategory:Content modelStandards:

- HTML5

HTML defines requirements for required ancestors on certain elements.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<area>
```

```
error: <area> element requires a <map> or <template> ancestor (element-required-ancestor) at inline:1:2:
> 1 | <area>
    |  ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<map>
    <area>
</map>
```

## [Version history](#version-history)

- 7.2.0 - Rule added.
