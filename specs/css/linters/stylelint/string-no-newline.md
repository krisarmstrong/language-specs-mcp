On this page

# string-no-newline

Disallow invalid newlines within strings.

```
a {
  content: "foo
    bar"; }/*  ↑
 *             ↑
 * The newline here */
```

[The spec](https://www.w3.org/TR/CSS2/syndata.html#strings) says this: "A string cannot directly contain a newline. To include a newline in a string, use an escape representing the line feed character in ISO-10646 (U+000A), such as '\A' or '\00000a'." And also: "It is possible to break strings over several lines, for aesthetic or other reasons, but in such a case the newline itself has to be escaped with a backslash (\)."

This rule overlaps with:

- [at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)
- [at-rule-prelude-no-invalid](/user-guide/rules/at-rule-prelude-no-invalid)
- [declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)
- [media-query-no-invalid](/user-guide/rules/media-query-no-invalid)

We recommend configuring this rule so that it doesn't overlap.

## Options[​](#options)

### `true`[​](#true)

```
{
  "string-no-newline": true
}
```

The following patterns are considered problems:

```
a {
  content: "foo
    bar";
}
```

```
[title="something
is probably wrong"] {}
```

```
a {
  font-family: "Times
    New
    Roman";
}
```

The following patterns are not considered problems:

```
a {
  content: "foo\Abar";
}
```

```
a {
  content: "foo\\nbar";
}
```

```
[title="nothing\
  is wrong"] {}
```

```
a {
  font-family: "Times New Roman";
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"at-rule-preludes"`[​](#at-rule-preludes)

Ignore strings in at-rule preludes.

```
{
  "string-no-newline": [true, { "ignore": ["at-rule-preludes"] }]
}
```

The following patterns are not considered problems:

```
@import url('foo
.css');
```

#### `"declaration-values"`[​](#declaration-values)

Ignore strings in declaration values.

The following patterns are not considered problems:

```
a {
  content: "foo
    bar";
}
```

[Previousshorthand-property-no-redundant-values](/user-guide/rules/shorthand-property-no-redundant-values)[Nextsyntax-string-no-invalid](/user-guide/rules/syntax-string-no-invalid)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
