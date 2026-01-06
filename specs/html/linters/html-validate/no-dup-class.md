## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallows duplicated classes on same element

Rule ID:no-dup-classCategory:HTML syntax and conceptsStandards:-

Prevents unnecessary duplication of class names.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div class="foo bar foo"></div>
```

```
error: Class "foo" duplicated (no-dup-class) at inline:1:21:
> 1 | <div class="foo bar foo"></div>
    |                     ^^^

1 error found.
```

Examples of correct code for this rule:

```
<div class="foo bar"></div>
```
