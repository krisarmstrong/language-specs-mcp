HTML-validate - Require non-breaking characters in telephone numbers (tel-non-breaking)Toggle navigation[HTML-validate v10.5.0](/)

- [User guide](../usage/index.html)
- [Elements](../guide/metadata/simple-component.html)
- [Rules](index.html)
- [Developers guide](../dev/using-api.html)
- [Changelog](../changelog/index.html)
- [About](../about/index.html)

html-validate-10.5.0

## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require non-breaking characters in telephone numbers

Rule ID:tel-non-breakingCategory:AccessibilityStandards:-

When telephone numbers are written out they are expected to be all on one line with no line breaks. If line break are added it gets harder to read and comprehend. Line breaks are typically added if the text is placed near the end of a line and the containing element gets too small.

Consider the following two:

- `+4670 174 06 35`
- 
`+4670 17406 35`

When written on a single line it is quickly recognizable and readable but when the line break is inserted the natural flow is broken and is not as easy to read.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<a href="tel:555123456">
    <span>555-123 456</span>
</a>
```

```
error: "-" should be replaced with "&#8209;" (non-breaking hyphen) in telephone number (tel-non-breaking) at inline:2:14:
  1 | <a href="tel:555123456">
> 2 |     <span>555-123 456</span>
    |              ^
  3 | </a>

error: " " should be replaced with "&nbsp;" (non-breaking space) in telephone number (tel-non-breaking) at inline:2:18:
  1 | <a href="tel:555123456">
> 2 |     <span>555-123 456</span>
    |                  ^
  3 | </a>

2 errors found.
```

Examples of correct code for this rule:

```
<a href="tel:555123456">
    <span>555&#8209;123&nbsp;456</span>
</a>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "characters": [
    { "pattern": " ", "replacement": "&nbsp;", "description": "non-breaking space" },
    { "pattern": "-", "replacement": "&#8209;", "description": "non-breaking hyphen" }
  ],
  "ignoreClasses": [],
  "ignoreStyle": true
}
```

### [characters](#characters)

List of disallowed characters and their replacements.

### [ignoreClasses](#ignoreclasses)

If the `<a>` element has one of the listed classes it is ignored by this rule. Use when applying styling to prevent line breaks.

For instance, when configured with `["nobreak"]` the following is valid:

```
<a class="nobreak" href="tel:555123456">
    <span>555-123 456</span>
</a>
```

### [ignoreStyle](#ignorestyle)

When set to `true` the `<a>` element is checked for inline styling forcing it to preserve whitespace and prevent line breaks.

Currently the following styles is checked:

- `white-space: nowrap`
- `white-space: pre`

With this option the following is valid:

```
<a style="white-space: nowrap" href="tel:555123456">
    555-123 456
</a>
```

## [Version history](#version-history)

- 6.8.0 - `ignoreStyle` added
- 6.7.0 - Rule added

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/tel-non-breaking.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/tel-non-breaking.ts)
