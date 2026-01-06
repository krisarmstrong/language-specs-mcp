## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow implicit input type

Rule ID:no-implicit-input-typeCategory:StyleStandards:-

When the `type` attribute is omitted it defaults to `text`. Being explicit about the intended type better conveys the purpose of the input field.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input>
```

```
error: <input> is missing recommended "type" attribute (no-implicit-input-type) at inline:1:2:
> 1 | <input>
    |  ^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input type="text">
```

## [Version history](#version-history)

- 8.10.0 - Rule added.
