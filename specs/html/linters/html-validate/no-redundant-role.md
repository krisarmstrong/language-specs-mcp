## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow usage of redundant roles

Rule ID:no-redundant-roleCategory:AccessibilityStandards:

- ARIA in HTML

Some HTML5 elements have implicit [WAI-ARIA roles](https://www.w3.org/TR/wai-aria-1.1/#role_definitions) defined by [ARIA in HTML](https://www.w3.org/TR/html-aria/#docconformance). This rule disallows using the `role` attribute to set the role to same as the implied role.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<main role="main">
  <ul>
    <li role="listitem">Lorem ipsum</li>
  </ul>
</main>
```

```
error: Redundant role "main" on <main> (no-redundant-role) at inline:1:13:
> 1 | <main role="main">
    |             ^^^^
  2 |   <ul>
  3 |     <li role="listitem">Lorem ipsum</li>
  4 |   </ul>

error: Redundant role "listitem" on <li> (no-redundant-role) at inline:3:15:
  1 | <main role="main">
  2 |   <ul>
> 3 |     <li role="listitem">Lorem ipsum</li>
    |               ^^^^^^^^
  4 |   </ul>
  5 | </main>

2 errors found.
```

Examples of correct code for this rule:

```
<ul>
  <li role="presentation">Lorem ipsum</li>
</ul>
```
