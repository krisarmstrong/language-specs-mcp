## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require a doctype for the document

Rule ID:missing-doctypeCategory:DocumentStandards:

- HTML5

Requires that the document contains a doctype.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<html>
    <body>...</body>
</html>
```

```
error: Document is missing doctype (missing-doctype) at inline:1:1:
> 1 | <html>
    | ^
  2 |     <body>...</body>
  3 | </html>

1 error found.
```

Examples of correct code for this rule:

```
<!doctype html>
<html>
    <body>...</body>
</html>
```
