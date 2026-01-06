On this page

# at-rule-no-unknown

Disallow unknown at-rules.

```
    @unknown (max-width: 960px) {}
/** ↑
 * At-rules like this */
```

This rule considers at-rules defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

For customizing syntax, see the [languageOptions](/user-guide/configure#languageoptions) section.

## Options[​](#options)

### `true`[​](#true)

```
{
  "at-rule-no-unknown": true
}
```

The following patterns are considered problems:

```
@unknown {}
```

The following patterns are not considered problems:

```
@media (max-width: 960px) {}
```

```
@font-feature-values Font One {
  @styleset {}
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Given:

```
{
  "at-rule-no-unknown": [true, { "ignoreAtRules": ["/^--my-/", "--custom"] }]
}
```

The following patterns are not considered problems:

```
@--my-at-rule "x.css";
```

```
@--my-other-at-rule {}
```

```
@--custom {}
```

[Previousat-rule-no-deprecated](/user-guide/rules/at-rule-no-deprecated)[Nextat-rule-no-vendor-prefix](/user-guide/rules/at-rule-no-vendor-prefix)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAtRules](#ignoreatrules)
