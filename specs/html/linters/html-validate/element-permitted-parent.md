## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Validate permitted element parent

Rule ID:element-permitted-parentCategory:Content modelStandards:

- HTML5

Some elements have restrictions for what parent element they can have. For instance, the parent of `<body>` element must the `<html>` element.

This rule does not validate the document root element, e.g. while the `<body>` element can only have `<html>` as parent if there is no parent at all it is assumed to be valid usage.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div>
    <title>Lorem ipsum</title>
</div>
```

```
error: <title> element requires a <head> element as parent (element-permitted-parent) at inline:2:6:
  1 | <div>
> 2 |     <title>Lorem ipsum</title>
    |      ^^^^^
  3 | </div>

1 error found.
```

Examples of correct code for this rule:

```
<head>
    <title>Lorem ipsum</title>
</head>
```

## [Version history](#version-history)

- 7.4.0 - Rule added.
