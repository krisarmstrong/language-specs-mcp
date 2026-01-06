On this page

# value-keyword-case

Specify lowercase or uppercase for keywords values.

```
    a { display: block; }
/**              ↑
 *    These values */
```

This rule ignores [<custom-idents>](https://developer.mozilla.org/en/docs/Web/CSS/custom-ident) of known properties. Keyword values which are paired with non-properties (e.g. `$vars` and custom properties), and do not conform to the primary option, can be ignored using the `ignoreKeywords: []` secondary option.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"lower"`[​](#lower)

```
{
  "value-keyword-case": "lower"
}
```

The following patterns are considered problems:

```
a {
  display: Block;
}
```

```
a {
  display: bLoCk;
}
```

```
a {
  display: BLOCK;
}
```

```
a {
  transition: -WEBKIT-TRANSFORM 2s;
}
```

The following patterns are not considered problems:

```
a {
  display: block;
}
```

```
a {
  transition: -webkit-transform 2s;
}
```

### `"upper"`[​](#upper)

```
{
  "value-keyword-case": "upper"
}
```

The following patterns are considered problems:

```
a {
  display: Block;
}
```

```
a {
  display: bLoCk;
}
```

```
a {
  display: block;
}
```

```
a {
  transition: -webkit-transform 2s;
}
```

The following patterns are not considered problems:

```
a {
  display: BLOCK;
}
```

```
a {
  transition: -WEBKIT-TRANSFORM 2s;
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreKeywords`[​](#ignorekeywords)

```
{ "ignoreKeywords": ["array", "of", "keywords", "/regex/"] }
```

Ignore case of keywords values.

Given:

```
{
  "value-keyword-case": [
    "lower",
    { "ignoreKeywords": ["Block", "/^(f|F)lex$/"] }
  ]
}
```

The following patterns are considered problems:

```
a {
  display: bLoCk;
}
```

```
a {
  display: BLOCK;
}
```

```
a {
  display: fLeX;
}
```

```
a {
  display: FLEX;
}
```

The following patterns are not considered problems:

```
a {
  display: block;
}
```

```
a {
  display: Block;
}
```

```
a {
  display: flex;
}
```

```
a {
  display: Flex;
}
```

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Ignore case of the values of the listed properties.

Given:

```
{
  "value-keyword-case": [
    "lower",
    { "ignoreProperties": ["/^(b|B)ackground$/", "display"] }
  ]
}
```

The following patterns are considered problems:

```
a {
  text-align: LEFT;
}
```

```
a {
  text-align: Left;
}
```

The following patterns are not considered problems:

```
a {
  display: bloCk;
}
```

```
a {
  display: BloCk;
}
```

```
a {
  display: BLOCK;
}
```

```
a {
  display: block;
}
```

```
a {
  background: Red;
}
```

```
a {
  Background: deepPink;
}
```

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Ignore case of the values inside the listed functions.

Given:

```
{
  "value-keyword-case": ["upper", { "ignoreFunctions": ["/^(f|F)oo$/", "t"] }]
}
```

The following patterns are considered problems:

```
a {
  display: b(inline);
}
```

```
a {
  color: bar(--camelCase);
}
```

The following patterns are not considered problems:

```
a {
  display: t(flex);
}
```

```
a {
  display: t(fLeX);
}
```

```
a {
  color: t(--camelCase);
}
```

```
a {
  color: foo(--camelCase);
}
```

```
a {
  color: Foo(--camelCase);
}
```

### `camelCaseSvgKeywords`[​](#camelcasesvgkeywords)

If `true`, this rule expects SVG keywords to be camel case when the primary option is `"lower"`. Defaults to `false`.

Given:

```
{
  "value-keyword-case": ["lower", { "camelCaseSvgKeywords": true }]
}
```

The following pattern is not considered a problem:

```
a {
  color: currentColor;
}
```

The following pattern is considered a problem:

```
a {
  color: currentcolor;
}
```

[Previousunit-no-unknown](/user-guide/rules/unit-no-unknown)[Nextvalue-no-vendor-prefix](/user-guide/rules/value-no-vendor-prefix)

- [Options](#options)

  - ["lower"](#lower)
  - ["upper"](#upper)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreKeywords](#ignorekeywords)
  - [ignoreProperties](#ignoreproperties)
  - [ignoreFunctions](#ignorefunctions)
  - [camelCaseSvgKeywords](#camelcasesvgkeywords)
