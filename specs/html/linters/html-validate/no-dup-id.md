## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallows elements with duplicated ID

Rule ID:no-dup-idCategory:DocumentStandards:

- HTML5

The ID of an element [must be unique](https://www.w3.org/TR/html5/dom.html#the-id-attribute) within the document. When `<template>` is used the `id` within the template must be unique but can otherwise contain duplicates as it isn't attached to the document yet.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div id="foo"></div>
<div id="foo"></div>
```

```
error: Duplicate ID "foo" (no-dup-id) at inline:2:10:
  1 | <div id="foo"></div>
> 2 | <div id="foo"></div>
    |          ^^^

1 error found.
```

Examples of correct code for this rule:

```
<div id="foo"></div>
<div id="bar"></div>
```
