HTML-validate - Require input to have label (input-missing-label)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require input elements to have a label

Rule ID:input-missing-labelCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

All input elements must have an associated label or accessible name.

It is required for accessibility tools to identify the purpose of the field.

For browsers it helps the user when clicking on the label to focus the field, especially important for checkboxes and radiobuttons where many users expect to be able to click in the label.

The recommended way is using a `<label>` element either explicitly associated using the `for` attribute or by nesting the `<input>` element inside the `<label>`. For regular input fields the former is recommended and for checkboxes and radiobuttons the latter is recommended.

An accessible name may also be provided using `aria-label` or `aria-labelledby`. This ensures accessibility tools can pick up the label but does not ensure a visual text is present so use with caution.

This rule ignores:

- `<input type="hidden">`
- `<input type="submit">` - but you should ensure `value` contains non-empty text.
- `<input type="reset">` - but you should ensure `value` contains non-empty text.
- `<input type="button">` - but you should ensure `value` contains non-empty text.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!-- no label element at all -->
<div>
    <strong>My input field</strong>
    <input type="text">

    <textarea></textarea>

    <select>
        <option>Option</option>
    </select>
</div>

<!-- unassociated label -->
<div>
    <label>My input field</label>
    <input type="text">
</div>
```

```
error: <input> element does not have a <label> (input-missing-label) at inline:4:6:
  2 | <div>
  3 |     <strong>My input field</strong>
> 4 |     <input type="text">
    |      ^^^^^
  5 |
  6 |     <textarea></textarea>
  7 |

error: <textarea> element does not have a <label> (input-missing-label) at inline:6:6:
  4 |     <input type="text">
  5 |
> 6 |     <textarea></textarea>
    |      ^^^^^^^^
  7 |
  8 |     <select>
  9 |         <option>Option</option>

error: <select> element does not have a <label> (input-missing-label) at inline:8:6:
   6 |     <textarea></textarea>
   7 |
>  8 |     <select>
     |      ^^^^^^
   9 |         <option>Option</option>
  10 |     </select>
  11 | </div>

error: <input> element does not have a <label> (input-missing-label) at inline:16:6:
  14 | <div>
  15 |     <label>My input field</label>
> 16 |     <input type="text">
     |      ^^^^^
  17 | </div>

4 errors found.
```

Examples of correct code for this rule:

```
<!-- label with descendant -->
<div>
    <label>My field <input type="text"></label>
</div>

<!-- associated label -->
<div>
    <label for="my-field">My field</label>
    <input id="my-field" type="text">
</div>
```

### [Hidden labels](#hidden-labels)

This rule requires labels to be accessible, i.e. the label must not be `hidden`, `inert`, `aria-hidden` or hidden with CSS. If multiple labels are associated at least one of them must be accessible.

```
<label for="my-input" aria-hidden="true">My field</label>
<input id="my-input" type="text">
```

```
error: <input> element has <label> but <label> element is hidden (input-missing-label) at inline:2:2:
  1 | <label for="my-input" aria-hidden="true">My field</label>
> 2 | <input id="my-input" type="text">
    |  ^^^^^

1 error found.
```

### [Using aria-label or aria-labelledby](#using-aria-label-or-aria-labelledby)

A accessible name can be provided using `aria-label` or `aria-labelledby`.

If a visual indication is already provided elsewhere (such as an icon) you can use `aria-label` to convey the same information to screen readers:

```
<div>
    <input id="my-input" type="text" aria-label="My field">
    <svg><use xlink:href="#search-icon"></svg>
</div>
```

If the label is provided by another element elsewhere `aria-labelledby` can be used to reference the element:

```
<h2 id="my-heading">Enter your name</h2>
<input type="text" aria-labelledby="my-heading">
```

## [Version history](#version-history)

- 8.17.0 - Ignores `<input>` hidden by CSS and handles `inert` attribute.
- 7.6.0 - Checks for presence of non-empty accessible text not just presence of `<label>` element.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/input-missing-label.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/input-missing-label.ts)
