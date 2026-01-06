On this page

# function-no-unknown

Disallow unknown functions.

```
a { transform: unknown(1); }
/**            ↑
 * Functions like this */
```

This rule considers functions defined in the CSS Specifications to be known.

This rule ignores double-dashed custom functions, e.g. `--custom-function()`.

This rule overlaps with:

- [at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)
- [declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)

We recommend using these rules for CSS and this rule for CSS-like languages, such as SCSS and Less.

## Options[​](#options)

### `true`[​](#true)

```
{
  "function-no-unknown": true
}
```

The following patterns are considered problems:

```
a { transform: unknown(1); }
```

The following patterns are not considered problems:

```
a { transform: scale(1); }
```

```
a { transform: --custom-function(1); }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Ignore the specified functions.

Given:

```
{
  "function-no-unknown": [true, { "ignoreFunctions": ["theme", "/^foo-/"] }]
}
```

The following patterns are not considered problems:

```
a { transform: theme(1); }
```

```
a { transform: foo-func(1); }
```

[Previousfunction-name-case](/user-guide/rules/function-name-case)[Nextfunction-url-no-scheme-relative](/user-guide/rules/function-url-no-scheme-relative)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreFunctions](#ignorefunctions)
