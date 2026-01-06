## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require headings to have textual content

Rule ID:empty-headingCategory:AccessibilityStandards:

- WCAG 2.2 (AA)
- WCAG 2.1 (AA)
- WCAG 2.0 (AA)

Assistive technology such as screen readers require textual content in headings. The content cannot be whitespace only.

Each heading should make sense on its own and properly describe the related section. Assistive tools may build a list of headings to help the user navigate between headings, a feature which can be confusing when headings are empty or non-descriptive.

See also [WCAG G130: Providing descriptive headings](https://www.w3.org/WAI/WCAG22/Techniques/general/G130).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<h1></h1>
<h2><span></span></h2>
```

```
error: <h1> cannot be empty, must have text content (empty-heading) at inline:1:2:
> 1 | <h1></h1>
    |  ^^
  2 | <h2><span></span></h2>

error: <h2> cannot be empty, must have text content (empty-heading) at inline:2:2:
  1 | <h1></h1>
> 2 | <h2><span></span></h2>
    |  ^^

2 errors found.
```

Examples of correct code for this rule:

```
<h1>Lorem ipsum</h1>
<h2><span>Dolor sit amet</span></h2>
```

### [Whitespace](#whitespace)

Text with only whitespace is also considered empty.

```
<h1> </h1>
```

```
error: <h1> cannot be empty, must have text content (empty-heading) at inline:1:2:
> 1 | <h1> </h1>
    |  ^^

1 error found.
```

### [Images](#images)

Images can be used if they have alternative text:

```
<h1>
    <img src="awesome-logo.png" alt="Our awesome logo!">
</h1>
```

### [Hidden](#hidden)

Even if the heading or one of its parents are `hidden` this rule tests if the heading is empty.

```
<h1 hidden></h1>
<div hidden>
    <h2></h1>
</div>
```

```
error: <h1> cannot be empty, must have text content (empty-heading) at inline:1:2:
> 1 | <h1 hidden></h1>
    |  ^^
  2 | <div hidden>
  3 |     <h2></h1>
  4 | </div>

error: <h2> cannot be empty, must have text content (empty-heading) at inline:3:6:
  1 | <h1 hidden></h1>
  2 | <div hidden>
> 3 |     <h2></h1>
    |      ^^
  4 | </div>

2 errors found.
```

Non-empty headings are valid:

```
<h1 hidden>Lorem ipsum</h1>
<div hidden>
    <h2>dolor sit amet</h2>
</div>
```

## [Version history](#version-history)

- 7.10.0 - Handles when heading (or a parent) is `hidden`.
- 7.6.0 - Handles `<img alt="..">` and `<svg>` with title.
