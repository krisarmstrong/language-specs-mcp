## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Ensure required elements are present

Rule ID:element-required-contentCategory:Content modelStandards:

- HTML5

Some elements has requirements where certain child elements has to be present.

The requirements comes from the [element metadata](/usage/elements.html):

```
{
  "my-element": {
    "requiredContent": ["my-other-element"]
  }
}
```

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<html>
    <head>
    </head>
</html>
```

```
error: <html> element must have <body> as content (element-required-content) at inline:1:2:
> 1 | <html>
    |  ^^^^
  2 |     <head>
  3 |     </head>
  4 | </html>

error: <head> element must have <title> as content (element-required-content) at inline:2:6:
  1 | <html>
> 2 |     <head>
    |      ^^^^
  3 |     </head>
  4 | </html>

2 errors found.
```

Examples of correct code for this rule:

```
<html>
    <head>
        <title>foo</title>
    </head>
    <body></body>
</html>
```
