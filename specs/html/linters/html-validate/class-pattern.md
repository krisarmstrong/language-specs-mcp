HTML-validate - Require classes to match a specific pattern (class-pattern)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require a specific class format

Rule ID:class-patternCategory:StyleStandards:-

Requires all classes to match a given pattern.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div class="fooBar"></foobar>
```

```
error: class "fooBar" does not match the configured pattern "kebabcase" (class-pattern) at inline:1:13:
> 1 | <div class="fooBar"></foobar>
    |             ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<div class="foo-bar"></div>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "pattern": "kebabcase"
}
```

### [Pattern](#pattern)

- type: `string | string[]`
- default: `"kebabcase"`

Either one of the presets or a custom regular expression.

- `"kebabcase"` matches lowercase letters, digits and hyphen (e.g. `kebab-case`)) (default)
- `"camelcase"` matches lowercase letter followed by letters and digits (e.g. `camelCase`)
- `"snakecase"` matches lowercase letters, digits and underscore (e.g. `snake_case`)
- `"bem"` matches [BEM naming convention](https://getbem.com/naming/) (e.g. `block__elem--modifier`)

Read more about [details and examples of predefined patterns](../pattern.html).

Multiple patterns can be set as an array. If value matches either of the patterns it is considered valid.

## [Version history](#version-history)

- 8.18.0 - Support `snakecase` (previously `underscore`) and `bem`.
- 8.17.0 - Support multiple patterns.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/class-pattern.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/class-pattern.ts)
