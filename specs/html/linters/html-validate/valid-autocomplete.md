## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require autocomplete attribute to be valid

Rule ID:valid-autocompleteCategory:HTML syntax and conceptsStandards:

- HTML5

The HTML5 `autocomplete` attribute can be used in different ways:

- On a `<form>` element it can take the `on` or `off` values to set the default for all nested controls.
- On form controls it can either take `on` or `off` to enable and disable or it can take a number of space-separated tokens describing what type of autocompletion to use.
- With the exception that `<input type="hidden">` cannot use `on` or `off`.

Further the space-separated tokens must appear in the following order:

- An optional section name (`section-` prefix).
- An optional `shipping` or `billing` token.
- An optional `home`, `work`, `mobile`, `fax` or `pager` token (for field names supporting it).
- A required field name.
- An optional `webauthn` token.

Typical field names would be:

- `name`
- `username`
- `current-password`
- `address-line1`
- `country-name`
- etc

For a full list of valid field names refer to the HTML5 standard [Autofill](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) section.

Some field names can only be used on specific input controls, for instance:

- A `new-password` field cannot be used on `<input type="number">`
- A `cc-exp-month` field cannot be used on `<input type="date">`
- etc

Again, refer to the Autofill section in the standard for a full table of allowed controls.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input type="text" autocomplete="foo">
<input type="text" autocomplete="name billing">
<input type="text" autocomplete="street-address">
```

```
error: "foo" is not a valid autocomplete token or field name (valid-autocomplete) at inline:1:34:
> 1 | <input type="text" autocomplete="foo">
    |                                  ^^^
  2 | <input type="text" autocomplete="name billing">
  3 | <input type="text" autocomplete="street-address">

error: "billing" must appear before "name" (valid-autocomplete) at inline:2:39:
  1 | <input type="text" autocomplete="foo">
> 2 | <input type="text" autocomplete="name billing">
    |                                       ^^^^^^^
  3 | <input type="text" autocomplete="street-address">

error: "street-address" cannot be used on <input type="text"> (valid-autocomplete) at inline:3:34:
  1 | <input type="text" autocomplete="foo">
  2 | <input type="text" autocomplete="name billing">
> 3 | <input type="text" autocomplete="street-address">
    |                                  ^^^^^^^^^^^^^^

3 errors found.
```

Examples of correct code for this rule:

```
<input type="text" autocomplete="name">
<input type="text" autocomplete="billing name">
<textarea autocomplete="street-address"></textarea>
```

## [References](#references)

- [HTML5 section 4.10.18.7: Autofill](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill)

## [Version history](#version-history)

- 8.15.0 - Rule added.
