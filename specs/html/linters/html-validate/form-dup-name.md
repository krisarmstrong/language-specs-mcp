HTML-validate - Require form controls to have a unique name (form-dup-name)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require form controls to have a unique name

Rule ID:form-dup-nameCategory:HTML syntax and conceptsStandards:-

While not strictly required by the HTML standard using the same name on multiple form controls can be confusing to read and is often an oversight by the developer. Submitting form with duplicate names are converted to arrays and some javascript frameworks assume the name is unique when serializing form data.

The form control name also plays a role in the autocomplete heurestics so using good names is important to get accurate results.

By default, radiobuttons (`<input type="radio">`) is generally ignored by this rule as they are typically using the same name on purpose but they cannot share the same name as other controls.

Each `<form>` and `<template>` element tracks the names separately, i.e. you can have two forms with colliding names. Disabled inputs are ignored by this rule.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<form>
    <input name="foo">
    <input name="foo">
</form>
```

```
error: Duplicate form control name "foo" (form-dup-name) at inline:3:18:
  1 | <form>
  2 |     <input name="foo">
> 3 |     <input name="foo">
    |                  ^^^
  4 | </form>

1 error found.
```

Examples of correct code for this rule:

```
<form>
    <input name="foo">
    <input name="bar">
</form>
```

## [Radiobuttons](#radiobuttons)

By default, radiobuttons may share the same name:

```
<form>
    <input name="foo" type="radio">
    <input name="foo" type="radio">
</form>
```

They cannot share the same name as other controls:

```
<form>
    <input name="foo" type="text">
    <input name="foo" type="radio">
</form>
```

```
error: Duplicate form control name "foo" (form-dup-name) at inline:3:18:
  1 | <form>
  2 |     <input name="foo" type="text">
> 3 |     <input name="foo" type="radio">
    |                  ^^^
  4 | </form>

1 error found.
```

See the [shared](#shared) option to add this behaviour for other controls.

## [Options](#options)

This rule takes an optional object:

```
{
  "allowArrayBrackets": true,
  "allowCheckboxDefault": true,
  "shared": ["radio"]
}
```

### [allowArrayBrackets](#allowarraybrackets)

- type: `boolean`
- default: `true`

Form control names ending with `[]` is typically used to signify arrays. With this option names ending with `[]` may be shared between controls.

With this option disabled the following is incorrect:

```
<form>
    <input name="foo[]">
    <input name="foo[]">
</form>
```

```
error: Duplicate form control name "foo[]" (form-dup-name) at inline:3:18:
  1 | <form>
  2 |     <input name="foo[]">
> 3 |     <input name="foo[]">
    |                  ^^^^^
  4 | </form>

1 error found.
```

With this option enabled the following is correct:

```
<form>
    <input name="foo[]">
    <input name="foo[]">
</form>
```

### [allowCheckboxDefault](#allowcheckboxdefault)

- type: `boolean`
- default: `true`

When serializing form data (e.g. using `FormData` or form submission) unchecked checkboxes are omitted from the entry list. A common pattern with server-side frameworks is to include an `<input type="hidden" value="0">` or similar as a default value, i.e. if the checkbox is unchecked the default value is used.

With this option disabled the following is incorrect:

```
<form>
    <input name="foo" value="0" type="hidden">
    <input name="foo" value="1" type="checkbox">
</form>
```

```
error: Duplicate form control name "foo" (form-dup-name) at inline:3:18:
  1 | <form>
  2 |     <input name="foo" value="0" type="hidden">
> 3 |     <input name="foo" value="1" type="checkbox">
    |                  ^^^
  4 | </form>

1 error found.
```

With this option enabled the following is correct:

```
<form>
    <input name="foo" value="0" type="hidden">
    <input name="foo" value="1" type="checkbox">
</form>
```

Note that even with this option enabled at most one checkbox may share the same name as a single hidden control. Use two or more hidden or two or more checkboxes with the same name is still an error.

### [shared](#shared)

- type: `Array<"radio" | "checkbox" | "submit" | "button" | "reset">`
- default: `["radio", "submit", "button", "reset"]`

By default only `<input type="radio">` can have a shared common name. This options lets you specify additional controls that may have a shared common name.

- `"radio"` - applies to `<input type="radio">`.
- `"checkbox"` - applies to `<input type="checkbox">`.
- `"submit"` - applies to `<button type="submit">` and `<input type="submit">`.
- `"button"` - applies to `<button type="button">` and `<input type="button">`.
- `"reset"` - applies to `<button type="reset">` and `<input type="reset">`.

With this option set to `["radio"]` the following is incorrect:

```
<form>
    <input name="foo" type="checkbox">
    <input name="foo" type="checkbox">
</form>
```

```
error: Duplicate form control name "foo" (form-dup-name) at inline:3:18:
  1 | <form>
  2 |     <input name="foo" type="checkbox">
> 3 |     <input name="foo" type="checkbox">
    |                  ^^^
  4 | </form>

1 error found.
```

With this option set to `["radio", "checkbox"]` the following is correct:

```
<form>
    <input name="foo" type="checkbox">
    <input name="foo" type="checkbox">
</form>
```

The name cannot be shared between different types of controls:

```
<form>
    <input name="foo" type="checkbox">
    <input name="foo" type="radio">
</form>
```

```
error: Duplicate form control name "foo" (form-dup-name) at inline:3:18:
  1 | <form>
  2 |     <input name="foo" type="checkbox">
> 3 |     <input name="foo" type="radio">
    |                  ^^^
  4 | </form>

1 error found.
```

## [Metadata](#metadata)

This rule check all elements marked as `formAssociated` with the `listed` property.

To use with custom elements set the `listed` property to `true`:

```
import { defineMetadata } from "html-validate";

export default defineMetadata({
  "custom-element": {
    formAssociated: {
      listed: true,
    },
  },
});
```

## [Version history](#version-history)

- 10.1.2 - Rule ignores disabled inputs.
- 8.19.0 - `allowCheckboxDefault` option added.
- 8.18.1 - Track `<template>` elements separately.
- 7.15.2 - `<button type="submit">` included as `shared` by default.
- 7.12.2 - `allowArrayBrackets` and `shared` options added.
- 7.12.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/form-dup-name.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/form-dup-name.ts)
