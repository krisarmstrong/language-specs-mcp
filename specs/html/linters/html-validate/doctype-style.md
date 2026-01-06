## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require a specific case for DOCTYPE

Rule ID:doctype-styleCategory:StyleStandards:-

While DOCTYPE is case-insensitive in the standard this rule requires it to be a specific style. The standard consistently uses uppercase which is the default style for this rule.

Mixed case it not supported.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!Doctype html>
```

```
error: DOCTYPE should be uppercase (doctype-style) at inline:1:1:
> 1 | <!Doctype html>
    | ^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<!DOCTYPE html>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "uppercase"
}
```

### [style](#style)

- `uppercase` requires DOCTYPE to be uppercase.
- `lowercase` requires DOCTYPE to be lowercase.
