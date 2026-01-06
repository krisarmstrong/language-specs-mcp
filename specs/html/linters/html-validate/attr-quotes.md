## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Requires a specific style of attribute quoting

Rule ID:attr-quotesCategory:StyleStandards:-

HTML allows different styles for quoting attributes:

- Single-quote `'`:
`<div id='foo'>`
- Double-quote `"`:
`<div id="foo">`
- Unquoted:
`<div id=foo>` (with limitations on allowed content)

This rule unifies which styles are allowed.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p class='foo'></p>
```

```
error: Attribute "class" used ' instead of expected " (attr-quotes) at inline:1:4:
> 1 | <p class='foo'></p>
    |    ^^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<p class="foo"></p>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "auto",
  "unquoted": false
}
```

### [Style](#style)

- `auto` requires usage of double quotes `"` unless the attribute value contains `"` (default).
- `single` requires usage of single quotes `'` for all attributes.
- `double` requires usage of double quotes `"` for all attributes.
- `any` requires usage of either single quotes `'` or double quotes `"` for all attributes.

### [Unquoted](#unquoted)

If `false` unquoted attributes is disallowed (default).

## [Version history](#version-history)

- 7.1.0 - `any` added to `style` option
