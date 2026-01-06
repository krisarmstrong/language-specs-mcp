On this page

# at-rule-descriptor-value-no-unknown

Disallow unknown values for descriptors within at-rules.

```
@counter-style foo {
  system: unknown;
/**       ↑
 * Values like this */
}
```

This rule considers descriptors and values defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

You can filter the [CSSTree Syntax Reference](https://csstree.github.io/docs/syntax/) to find out what values are valid for a descriptor of an at-rule.

This rule is only appropriate for CSS. You should not turn it on for CSS-like languages, such as SCSS or Less.

This rule checks descriptor values within at-rules. You can use [declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown) to disallow unknown values for properties within declarations, and [at-rule-descriptor-no-unknown](/user-guide/rules/at-rule-descriptor-no-unknown) to disallow unknown descriptors for at-rules.

This rule overlaps with:

- [color-no-invalid-hex](/user-guide/rules/color-no-invalid-hex)
- [function-linear-gradient-no-nonstandard-direction](/user-guide/rules/function-linear-gradient-no-nonstandard-direction)
- [function-no-unknown](/user-guide/rules/function-no-unknown)
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
  "at-rule-descriptor-value-no-unknown": true
}
```

The following patterns are considered problems:

```
@counter-style foo {
  system: unknown;
}
```

```
@property --foo {
  syntax: unknown;
}
```

The following patterns are not considered problems:

```
@counter-style foo {
  system: numeric;
}
```

```
@property --foo {
  syntax: "<color>";
}
```

[Previousat-rule-descriptor-no-unknown](/user-guide/rules/at-rule-descriptor-no-unknown)[Nextat-rule-disallowed-list](/user-guide/rules/at-rule-disallowed-list)

- [Options](#options)

  - [true](#true)
