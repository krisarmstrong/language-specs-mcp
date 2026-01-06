On this page

# unit-no-unknown

Disallow unknown units.

```
a { width: 100pixels; }
/**           ↑
 *  These units */
```

This rule considers units defined in the CSS Specifications, up to and including Editor's Drafts, to be known.

This rule overlaps with:

- [at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)
- [at-rule-prelude-no-invalid](/user-guide/rules/at-rule-prelude-no-invalid)
- [declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)
- [media-feature-name-value-no-unknown](/user-guide/rules/media-feature-name-value-no-unknown)
- [media-query-no-invalid](/user-guide/rules/media-query-no-invalid)

We recommend using these rules for CSS and this rule for CSS-like languages, such as SCSS and Less.

## Options[​](#options)

### `true`[​](#true)

```
{
  "unit-no-unknown": true
}
```

The following patterns are considered problems:

```
a {
  width: 10pixels;
}
```

```
a {
  width: calc(10px + 10pixels);
}
```

The following patterns are not considered problems:

```
a {
  width: 10px;
}
```

```
a {
  width: 10Px;
}
```

```
a {
  width: 10pX;
}
```

```
a {
  width: calc(10px + 10px);
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreUnits`[​](#ignoreunits)

```
{ "ignoreUnits": ["array", "of", "units", "/regex/"] }
```

Given:

```
{
  "unit-no-unknown": [true, { "ignoreUnits": ["/^--foo-/", "--bar"] }]
}
```

The following patterns are not considered problems:

```
a {
  width: 10--foo--baz;
}
```

```
a {
  width: 10--bar;
}
```

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Given:

```
{
  "unit-no-unknown": [
    true,
    { "ignoreFunctions": ["foo", "/^my-/", "/^YOUR-/i"] }
  ]
}
```

The following patterns are not considered problems:

```
a {
  width: foo(1x);
}
```

```
a {
  width: my-func(1x);
}
```

```
a {
  width: YoUr-func(1x);
}
```

[Previousunit-disallowed-list](/user-guide/rules/unit-disallowed-list)[Nextvalue-keyword-case](/user-guide/rules/value-keyword-case)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreUnits](#ignoreunits)
  - [ignoreFunctions](#ignorefunctions)
