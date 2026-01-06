On this page

# at-rule-prelude-no-invalid

Disallow invalid preludes for at-rules.

```
@property --foo {}
/**       ↑
 * Preludes like this */
```

This rule considers preludes for at-rules defined within the CSS specifications, up to and including Editor's Drafts, to be valid.

You can filter the [CSSTree Syntax Reference](https://csstree.github.io/docs/syntax/) to find out what preludes are valid for an at-rule.

This rule is only appropriate for CSS. You should not turn it on for CSS-like languages, such as SCSS or Less.

This rule overlaps with:

- [media-query-no-invalid](/user-guide/rules/media-query-no-invalid)
- [string-no-newline](/user-guide/rules/string-no-newline)
- [unit-no-unknown](/user-guide/rules/unit-no-unknown)

You can either turn off the rules or configure them to ignore the overlaps.

For customizing syntax, see the [languageOptions](/user-guide/configure#languageoptions) section.

Prior art:

- [stylelint-csstree-validator](https://www.npmjs.com/package/stylelint-csstree-validator)

## Options[​](#options)

### `true`[​](#true)

```
{
  "at-rule-prelude-no-invalid": true
}
```

The following patterns are considered problems:

```
@property foo {}
```

```
@font-palette-values foo {}
```

The following patterns are not considered problems:

```
@property --foo {}
```

```
@font-palette-values --foo {}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Given:

```
{
  "at-rule-prelude-no-invalid": [
    true,
    { "ignoreAtRules": ["property", "/^font-/"] }
  ]
}
```

The following patterns are not considered problems:

```
@property foo;
```

```
@font-palette-values foo {}
```

[Previousat-rule-no-vendor-prefix](/user-guide/rules/at-rule-no-vendor-prefix)[Nextat-rule-property-required-list](/user-guide/rules/at-rule-property-required-list)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAtRules](#ignoreatrules)
