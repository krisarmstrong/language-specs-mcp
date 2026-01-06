On this page

# no-invalid-position-declaration

Disallow invalid position declarations.

```
color: red;
/** ↑
 * This declaration */
```

Declarations can only be positioned within the `<declaration-list>`, `<declaration-rule-list>` and `<block-contents>` productions.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-invalid-position-declaration": true
}
```

The following patterns are considered problems:

```
color: red;
```

```
--foo: red;
```

```
@media all {
  color: red;
}
```

The following patterns are not considered problems:

```
a { color: red; }
```

```
a { --foo: red; }
```

```
@media all {
  a {
    color: red;
  }
}
```

```
a {
  @media all {
    color: red;
  }
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Ignore nesting at-rules within specified at-rules.

Given:

```
{
  "no-invalid-position-declaration": [
    true,
    { "ignoreAtRules": ["--foo", "/^--bar-/"] }
  ]
}
```

The following patterns are not considered problems:

```
@--foo {
  @media all {
    color: red;
  }
}
```

```
@--bar-baz qux {
  @layer foo {
    color: red;
  }
}
```

[Previousno-invalid-position-at-import-rule](/user-guide/rules/no-invalid-position-at-import-rule)[Nextno-irregular-whitespace](/user-guide/rules/no-irregular-whitespace)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreAtRules](#ignoreatrules)
