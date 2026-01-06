## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require a specific ID format

Rule ID:id-patternCategory:StyleStandards:-

Requires all IDs to match a given pattern.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div id="fooBar"></foobar>
```

```
error: id "fooBar" does not match the configured pattern "kebabcase" (id-pattern) at inline:1:10:
> 1 | <div id="fooBar"></foobar>
    |          ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<div id="foo-bar"></div>
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
