HTML-validate - Require form control names to match a specific pattern (name-pattern)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require form control names to match a specific pattern

Rule ID:name-patternCategory:StyleStandards:-

Requires all names on form controls to match a given pattern.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input name="foo-bar">
```

```
error: name "foo-bar" does not match the configured pattern "camelcase" (name-pattern) at inline:1:14:
> 1 | <input name="foo-bar">
    |              ^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<input name="fooBar">
```

Array brackets are ignored by this rule:

```
<input name="fooBar[]">
```

## [Options](#options)

This rule takes an optional object:

```
{
  "pattern": "camelcase"
}
```

### [Pattern](#pattern)

- type: `string | string[]`
- default: `"camelcase"`

Either one of the presets or a custom regular expression.

- `"kebabcase"` matches lowercase letters, digits and hyphen (e.g. `kebab-case`)) (default)
- `"camelcase"` matches lowercase letter followed by letters and digits (e.g. `camelCase`)
- `"snakecase"` matches lowercase letters, digits and underscore (e.g. `snake_case`)
- `"bem"` matches [BEM naming convention](https://getbem.com/naming/) (e.g. `block__elem--modifier`)

Read more about [details and examples of predefined patterns](../pattern.html).

Multiple patterns can be set as an array. If value matches either of the patterns it is considered valid.

## [Version history](#version-history)

- 8.18.0 - Support `snakecase` (previously `underscore`) and `bem`.
- 8.17.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/name-pattern.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/name-pattern.ts)
