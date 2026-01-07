HTML-validate - Require attributes to match configured patterns (attr-pattern)Toggle navigation[HTML-validate v10.5.0](/)

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

# Attribute name pattern

Rule ID:attr-patternCategory:StyleStandards:-

Require attributes to match configured patterns. This rule is case-insensitive, for matching case use [attr-case](attr-case.html).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p foo_bar="baz"></p>
```

```
error: Attribute "foo_bar" should match /[a-z0-9-:]+/ (attr-pattern) at inline:1:4:
> 1 | <p foo_bar="baz"></p>
    |    ^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<p foo-bar="baz"></p>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "pattern": "[a-z0-9-:]+",
  "ignoreForeign": true
}
```

### [pattern](#pattern)

- type: `string | string[]`
- default: `[a-z0-9-:]+`

Pattern to match.

Multiple patterns can be set as an array of strings. With multiple patterns the attribute must match at least one pattern to be considered valid.

For instance, when configured with `{"pattern": ["[a-z0-9-]+", "myprefix-.+"]}` attributes can be either letters and digits or anything with the `myprefix-` prefix:

```
<p foo-bar-123></p>
<p myprefix-foo_123!></p>
```

### [ignoreForeign](#ignoreforeign)

By default attributes on foreign elements (such as `<svg>` and `<math>`) are ignored as they follow their own specifications.

Disable this option if you want to validate attributes on foreign elements as well.

## [Version history](#version-history)

- v4.14.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/attr-pattern.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/attr-pattern.ts)
