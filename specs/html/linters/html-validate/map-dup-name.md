## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require `<map name>` to be unique

Rule ID:map-dup-nameCategory:HTML syntax and conceptsStandards:

- HTML5

In HTML5 the `<map name>` attribute is required to be a unique name within the document.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<map name="foo"></map>
<map name="foo"></map>
```

```
error: <map> name must be unique (map-dup-name) at inline:2:6:
  1 | <map name="foo"></map>
> 2 | <map name="foo"></map>
    |      ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<map name="foo"></map>
<map name="bar"></map>
```

## [Version history](#version-history)

- 7.9.0 - Rule added.
