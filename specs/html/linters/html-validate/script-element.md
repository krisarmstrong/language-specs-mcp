HTML-validate - Require end tag for `<script>` (script-element)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require end tag for `<script>` element

Rule ID:script-elementCategory:Content modelStandards:

- HTML5

For legacy reasons the `<script>` element must include a `</script>` end tag even when using the `src` attribute.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<script src="myscript.js"/>
```

```
error: End tag for <script> must not be omitted (script-element) at inline:1:26:
> 1 | <script src="myscript.js"/>
    |                          ^^

1 error found.
```

Examples of correct code for this rule:

```
<script src="myscript.js"></script>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/script-element.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/script-element.ts)
