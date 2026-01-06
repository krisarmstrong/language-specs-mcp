## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow usage of abstract WAI-ARIA roles

Rule ID:no-abstract-roleCategory:AccessibilityStandards:

- WAI ARIA

WAI-ARIA defines a list of [abstract roles](https://www.w3.org/TR/wai-aria-1.2/#abstract_roles) which cannot be used by authors:

- `command`
- `composite`
- `input`
- `landmark`
- `range`
- `roletype`
- `section`
- `sectionhead`
- `select`
- `structure`
- `widget`
- `window`

Typically one of the role subclasses should be used instead.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div role="landmark"></div>
```

```
error: Role "landmark" is abstract and must not be used (no-abstract-role) at inline:1:12:
> 1 | <div role="landmark"></div>
    |            ^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<div role="navigation"></div>
```

## [Version history](#version-history)

- 8.12.0 - Rule added.
