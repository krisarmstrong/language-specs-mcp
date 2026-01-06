## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow inline style

Rule ID:no-inline-styleCategory:StyleStandards:-

Inline style is a sign of unstructured CSS. Use class or ID with a separate stylesheet.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p style="color: red"></p>
```

```
error: Inline style is not allowed (no-inline-style) at inline:1:4:
> 1 | <p style="color: red"></p>
    |    ^^^^^^^^^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<p class="error"></p>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "include": [],
  "exclude": [],
  "allowedProperties": ["display"]
}
```

Both `include` and `exclude` are only useful when using a framework with dynamic attributes such as `ng-style` or `:style` to allow/disallow one or more specific variant of the attribute. For instance:

```
<p :style="style></p>
```

would normally trigger the rule when using [html-validate-vue](../frameworks/vue.html) but by adding `:style` to `exclude` it can be allowed.

### [include](#include)

If set only attributes listed in this array generates errors.

### [exclude](#exclude)

If set attributes listed in this array is ignored.

### [allowedProperties](#allowedproperties)

List of CSS properties to ignore. If the `style` attribute contains only the properties listed no error will be yielded.

By default `display` is allowed.

```
<p style="display: none"></p>
```
