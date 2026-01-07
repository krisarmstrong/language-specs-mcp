HTML-validate - Disallow whitespace between attribute key and value (attr-delimiter)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow whitespace between attribute key and value

Rule ID:attr-delimiterCategory:HTML syntax and conceptsStandards:

- HTML5

While technically allowed by the HTML5 specification this rule disallows the usage of whitespace separating the attribute key and value, i.e. before or after the `=` character.

Usage of whitespace in this context is typically a sign of typo or unintended behaviour. For instance, consider the following markup:

```
<input name= disabled>
```

As the HTML5 specification allows whitespace after `=` this is to be interpreted as `<input name="disabled">` which is has a completely different meaning than the developer probably intended. This could have been generated from a templating langage where the value supposted to be bound to `name` was not set:

```
<input name=<%= fieldName %> disabled>
```

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<input name= "my-field">
<input name ="my-field">
```

```
error: Attribute value must not be delimited by whitespace (attr-delimiter) at inline:1:12:
> 1 | <input name= "my-field">
    |            ^^
  2 | <input name ="my-field">

error: Attribute value must not be delimited by whitespace (attr-delimiter) at inline:2:12:
  1 | <input name= "my-field">
> 2 | <input name ="my-field">
    |            ^^

2 errors found.
```

Examples of correct code for this rule:

```
<input name="my-field">
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/attr-delimiter.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/attr-delimiter.ts)
