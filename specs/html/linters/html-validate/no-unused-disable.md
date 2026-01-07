HTML-validate - Disallow unused disable directives (no-unused-disable)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow unused disable directives

Rule ID:no-unused-disableCategory:-Standards:-

Rules can be disabled using [directives](../usage/index.html#inline-configuration) such as `<!-- [html-validate-disable-next my-rule] -->`. This rules disallows unneccesary disabled rules, i.e. rules that would not have generated any error even if enabled.

This is usually a case of refactoring or changing environment.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!-- [html-validate-disable-next attribute-allowed-values -- no error, disable is invalid] -->
<button type="submit"></button>
```

```
error: "attribute-allowed-values" rule is disabled but no error was reported (no-unused-disable) at inline:1:34:
> 1 | <!-- [html-validate-disable-next attribute-allowed-values -- no error, disable is invalid] -->
    |                                  ^^^^^^^^^^^^^^^^^^^^^^^^
  2 | <button type="submit"></button>

1 error found.
```

Examples of correct code for this rule:

```
<!-- disable removed, no error -->
<button type="submit"></button>
```

```
<!-- [html-validate-disable-next attribute-allowed-values -- element has error, disable is valid] -->
<button type="foobar"></button>
```

This rule can also disable itself:

```
<!-- [html-validate-disable-next attribute-allowed-values, no-unused-disable -- no error as no-unused-disable is also disabled] -->
<button type="submit"></button>
```

## [Version history](#version-history)

- 7.13.1 - Rule is allowed to disable itself with directive.
- 7.13.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-unused-disable.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-unused-disable.ts)
