HTML-validate - Require title to have textual content (empty-title)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require title to have textual content

Rule ID:empty-titleCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

The `<title>` element is used to describe the document and is shown in the browser tab and titlebar. The content cannot be whitespace only.

WCAG ([H25](https://www.w3.org/WAI/WCAG22/Techniques/html/H25)) and SEO requires a descriptive title and preferably unique within the site. For SEO a maximum of around 60-70 characters is recommended.

Each title should make sense on its own and properly describe the document. Avoid keyword stuffing.

See also [WCAG G88: Providing descriptive titles](https://www.w3.org/WAI/WCAG22/Techniques/general/G88).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<head>
    <title></title>
</head>
```

```
error: <title> cannot be empty, must have text content (empty-title) at inline:2:6:
  1 | <head>
> 2 |     <title></title>
    |      ^^^^^
  3 | </head>

1 error found.
```

Examples of correct code for this rule:

```
<head>
    <title>Lorem ipsum</title>
</head>
```

## [Whitespace](#whitespace)

Text with only whitespace is also considered empty.

```
<head>
    <title> </title>
</head>
```

```
error: <title> cannot be empty, must have text content (empty-title) at inline:2:6:
  1 | <head>
> 2 |     <title> </title>
    |      ^^^^^
  3 | </head>

1 error found.
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/empty-title.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/empty-title.ts)
