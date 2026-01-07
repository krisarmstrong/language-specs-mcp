HTML-validate - Disallow usage of deprecated elements (deprecated)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow usage of deprecated elements

Rule ID:deprecatedCategory:DeprecatedStandards:

- HTML5

HTML5 deprecated many old elements.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<center>...</center>
<big>...</big>
```

```
error: <center> is deprecated: use CSS instead (deprecated) at inline:1:2:
> 1 | <center>...</center>
    |  ^^^^^^
  2 | <big>...</big>

error: <big> is deprecated: use CSS instead (deprecated) at inline:2:2:
  1 | <center>...</center>
> 2 | <big>...</big>
    |  ^^^

2 errors found.
```

Examples of correct code for this rule:

```
<main>...</main>
```

## [Elements](#elements)

When using custom elements metadata you can optionally specify a message:

```
import { defineMetadata } from "html-validate";

export default defineMetadata({
  "my-element": {
    deprecated: "replaced with <other-element>",
  },
});
```

The message will be shown alongside the regular message:

```
<my-element>...</my-element>
```

```
error: <my-element> is deprecated: replaced with <other-element> (deprecated) at inline:1:2:
> 1 | <my-element>...</my-element>
    |  ^^^^^^^^^^

1 error found.
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

If set only elements listed in this array generates errors.

### [exclude](#exclude)

If set elements listed in this array is ignored.

## [Version history](#version-history)

- v4.11.0 - `include` and `exclude` options added.
- v1.13.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/deprecated.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/deprecated.ts)
