HTML-validate - Require a specific case for element names (element-case)Toggle navigation[HTML-validate v10.5.0](/)

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

# Element name case

Rule ID:element-caseCategory:StyleStandards:-

Requires a specific case for element names.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<DIV>...</DIV>
```

```
error: Element "DIV" should be lowercase (element-case) at inline:1:2:
> 1 | <DIV>...</DIV>
    |  ^^^

1 error found.
```

Examples of correct code for this rule:

```
<div>...</div>
```

### [Matching case](#matching-case)

When using styles such as `pascalcase` the start and end tag must have matching case:

```
<FooBar>...</Foobar>
```

```
error: Start and end tag must not differ in casing (element-case) at inline:1:13:
> 1 | <FooBar>...</Foobar>
    |             ^^^^^^^

1 error found.
```

## [Options](#options)

This rule takes an optional object:

```
{
  "style": "lowercase"
}
```

### [Style](#style)

- `camelcase` requires all element names to be camelCase.
- `lowercase` requires all element names to be lowercase.
- `pascalcase` requires all element names to be PascalCase.
- `uppercase` requires all element names to be UPPERCASE.

Multiple styles can be set as an array of strings. With multiple styles the element name must match at least one pattern to be considered valid.

For instance, when configured with `{"style": ["lowercase", "pascalcase"]}` element names can be either lowercase or PascalCase:

```
<foo-bar></foo-bar>
<FooBar></FooBar>
<fooBar></fooBar>
```

```
error: Element "fooBar" should be lowercase or PascalCase (element-case) at inline:3:2:
  1 | <foo-bar></foo-bar>
  2 | <FooBar></FooBar>
> 3 | <fooBar></fooBar>
    |  ^^^^^^

1 error found.
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-case.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-case.ts)
