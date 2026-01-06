On this page

# declaration-property-value-no-unknown

Disallow unknown values for properties within declarations.

```
a { top: unknown; }
/** ↑    ↑
 * property and value pairs like these */
```

This rule considers values for properties defined within the CSS specifications to be known. You can use the `propertiesSyntax` and `typesSyntax` secondary options to extend the syntax.

You can filter the [CSSTree Syntax Reference](https://csstree.github.io/docs/syntax/) to find out what value syntax is known for a property.

This rule is only appropriate for CSS. You should not turn it on for CSS-like languages, such as SCSS or Less.

This rule checks property values. You can use [at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown) to disallow unknown values for descriptors within at-rules.

This rule overlaps with:

- [color-no-invalid-hex](/user-guide/rules/color-no-invalid-hex)
- [function-linear-gradient-no-nonstandard-direction](/user-guide/rules/function-linear-gradient-no-nonstandard-direction)
- [function-no-unknown](/user-guide/rules/function-no-unknown)
- [string-no-newline](/user-guide/rules/string-no-newline)
- [unit-no-unknown](/user-guide/rules/unit-no-unknown)

You can either turn off the rules or configure them to ignore the overlaps.

Prior art:

- [stylelint-csstree-validator](https://www.npmjs.com/package/stylelint-csstree-validator)

## Options[​](#options)

### `true`[​](#true)

```
{
  "declaration-property-value-no-unknown": true
}
```

The following patterns are considered problems:

```
a { top: red; }
```

```
a { top: unknown; }
```

The following patterns are not considered problems:

```
a { top: 0; }
```

```
a { top: var(--foo); }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreProperties`[​](#ignoreproperties)

```
{
  "ignoreProperties": { "property-name": ["array", "of", "values", "/regex/"] }
}
```

Ignore the specified property and value pairs. Keys in the object indicate property names.

You can specify a regex for a property name, such as `{ "/^margin/": [] }`.

Given:

```
{
  "declaration-property-value-no-unknown": [
    true,
    {
      "ignoreProperties": {
        "top": ["unknown"],
        "/^margin-/": ["/^--foo/"],
        "padding": ["/.+/"],
        "/.+/": ["--unknown-value"]
      }
    }
  ]
}
```

The following patterns are not considered problems:

```
a { top: unknown; }
```

```
a { margin-top: --foo-bar; }
```

```
a { padding: invalid; }
```

```
a { width: --unknown-value; }
```

### `propertiesSyntax`[​](#propertiessyntax)

```
{ "propertiesSyntax": { "property": "syntax" } }
```

Extend or alter the properties syntax dictionary. [CSS Value Definition Syntax](https://github.com/csstree/csstree/blob/master/docs/definition-syntax.md) is used to define a value's syntax. If a definition starts with `|` it is added to the [existing definition value](https://csstree.github.io/docs/syntax/) if any.

Given:

```
{
  "declaration-property-value-no-unknown": [
    true,
    { "propertiesSyntax": { "size": "<length-percentage>" } }
  ]
}
```

The following patterns are not considered problems:

```
a { size: 0; }
```

```
a { size: 10px }
```

### `typesSyntax`[​](#typessyntax)

```
{ "typesSyntax": { "type": "syntax" } }
```

Extend or alter the types syntax dictionary. [CSS Value Definition Syntax](https://github.com/csstree/csstree/blob/master/docs/definition-syntax.md) is used to define a value's syntax. If a definition starts with `|` it is added to the [existing definition value](https://csstree.github.io/docs/syntax/) if any.

Types are something like a preset which allows you to reuse a definition across other definitions. So, you'll likely want to also use the `propertiesSyntax` option when using this option.

Given:

```
{
  "declaration-property-value-no-unknown": [
    true,
    {
      "propertiesSyntax": { "top": "| <--foo()>" },
      "typesSyntax": { "--foo()": "--foo( <length-percentage> )" }
    }
  ]
}
```

The following patterns are not considered problems:

```
a { top: --foo(0); }
```

```
a { top: --foo(10px); }
```

[Previousdeclaration-property-value-keyword-no-deprecated](/user-guide/rules/declaration-property-value-keyword-no-deprecated)[Nextfont-family-name-quotes](/user-guide/rules/font-family-name-quotes)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreProperties](#ignoreproperties)
  - [propertiesSyntax](#propertiessyntax)
  - [typesSyntax](#typessyntax)
