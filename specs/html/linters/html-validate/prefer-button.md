## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Prefer to use `<button>` instead of `<input>` for buttons

Rule ID:prefer-buttonCategory:StyleStandards:-

HTML5 introduces the generic `<button>` element which replaces `<input type="button">` and similar constructs.

The `<button>` elements has some advantages:

- It can contain markup as content compared to the `value` attribute of `<input>` which can only hold text. Especially useful to add `<svg>` icons.
- The button text is a regular text node, no need to quote characters in the `value` attribute.
- Styling is easier, compare the selector `button` to `input[type="submit"], input[type="button"], ...`.

This rule will target the following input types:

- `<input type="button">`
- `<input type="submit">`
- `<input type="reset">`
- `<input type="image">`

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input type="button">
```

```
error: Prefer to use <button> instead of <input type="button"> when adding buttons (prefer-button) at inline:1:14:
> 1 | <input type="button">
    |              ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<button type="button"></button>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "include": [],
  "exclude": []
}
```

### [include](#include)

If set only types listed in this array generates errors.

### [exclude](#exclude)

If set types listed in this array is ignored.
