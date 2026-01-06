## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require attributes to be separated by whitespace

Rule ID:attr-spacingCategory:HTML syntax and conceptsStandards:

- HTML5

In HTML attributes must be separated by whitespace (commonly a regular space).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input type="submit"class="foo">
```

```
error: No space between attributes (attr-spacing) at inline:1:21:
> 1 | <input type="submit"class="foo">
    |                     ^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input type="submit" class="foo">
```
