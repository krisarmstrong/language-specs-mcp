On this page

# at-rule-descriptor-no-unknown

Disallow unknown descriptors for at-rules.

```
@counter-style foo {
  unknown-descriptor: cyclic;
/**                ↑
 * Descriptors like this */
}
```

This rule considers descriptors defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

You can filter the [CSSTree Syntax Reference](https://csstree.github.io/docs/syntax/) to find out what descriptors are known for an at-rule.

This rule is only appropriate for CSS. You should not turn it on for CSS-like languages, such as SCSS or Less.

This rule checks descriptors within at-rules. To check properties, you can use the [property-no-unknown](/user-guide/rules/property-no-unknown) rule.

For customizing syntax, see the [languageOptions](/user-guide/configure#languageoptions) section.

Prior art:

- [stylelint-csstree-validator](https://www.npmjs.com/package/stylelint-csstree-validator)

## Options[​](#options)

### `true`[​](#true)

```
{
  "at-rule-descriptor-no-unknown": true
}
```

The following patterns are considered problems:

```
@counter-style foo {
  unknown-descriptor: cyclic;
}
```

```
@property --foo {
  unknown-descriptor: "<color>";
}
```

The following patterns are not considered problems:

```
@counter-style foo {
  system: cyclic;
}
```

```
@property --foo {
  syntax: "<color>";
}
```

[Previousat-rule-allowed-list](/user-guide/rules/at-rule-allowed-list)[Nextat-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)

- [Options](#options)

  - [true](#true)
