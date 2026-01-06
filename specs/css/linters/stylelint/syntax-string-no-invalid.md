On this page

# syntax-string-no-invalid

Disallow invalid syntax strings.

```
@property --foo {
  syntax: "<color>";
/**       ↑
 * Syntax strings like this */
}
```

Syntax strings are used for the `syntax` descriptor value of the `@property` at-rule. This rule checks their grammar and flags unsupported type names.

You can check [§5.1 “Supported Names” of the CSS Properties & Values API](https://drafts.css-houdini.org/css-properties-values-api/#supported-names) for a list of valid syntax component names.

## Options[​](#options)

### `true`[​](#true)

```
{
  "syntax-string-no-invalid": true
}
```

The following patterns are considered problems:

```
@property --foo {
  syntax: "<bar>";
}
```

```
@property --foo {
  syntax: "<alpha-value>";
}
```

The following patterns are not considered problems:

```
@property --foo {
  syntax: "<color>";
}
```

```
@property --foo {
  syntax: "<length> | <color>";
}
```

[Previousstring-no-newline](/user-guide/rules/string-no-newline)[Nexttime-min-milliseconds](/user-guide/rules/time-min-milliseconds)

- [Options](#options)

  - [true](#true)
