## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Attribute name case

Rule ID:attr-caseCategory:StyleStandards:

- HTML5

Requires a specific case for attribute names. This rule matches case for letters only, for restricting allowed characters use [attr-pattern](attr-pattern.html).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p ID="foo"></p>
```

```
error: Attribute "ID" should be lowercase (attr-case) at inline:1:4:
> 1 | <p ID="foo"></p>
    |    ^^

1 error found.
```

Examples of correct code for this rule:

```
<p id="foo"></p>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "lowercase",
  "ignoreForeign": true
}
```

### [style](#style)

- `camelcase` requires all attribute names to be camelCase.
- `lowercase` requires all attribute names to be lowercase.
- `pascalcase` requires all attribute names to be PascalCase.
- `uppercase` requires all attribute names to be UPPERCASE.

Multiple styles can be set as an array of strings. With multiple styles the attribute must match at least one pattern to be considered valid.

For instance, when configured with `{"style": ["lowercase", "uppercase"]}` attributes can be either lowercase or uppercase:

```
<p foobar></p>
<p FOOBAR></p>
<p fooBar></p>
```

```
error: Attribute "fooBar" should be lowercase or uppercase (attr-case) at inline:3:4:
  1 | <p foobar></p>
  2 | <p FOOBAR></p>
> 3 | <p fooBar></p>
    |    ^^^^^^

1 error found.
```

### [ignoreForeign](#ignoreforeign)

By default attributes on foreign elements (such as `<svg>` and `<math>`) are ignored as they follow their own specifications. For instance, the SVG specifications uses camelcase for many attributes.

With this option enabled the following is valid despite camelcase attribute:

```
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" />
```

Disable this option if you want to validate attributes on foreign elements as well.
