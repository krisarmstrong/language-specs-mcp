HTML-validate - Validate permitted content (element-permitted-content)Toggle navigation[HTML-validate v10.5.0](/)

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

# Validate element content

Rule ID:element-permitted-contentCategory:Content modelStandards:

- HTML5

HTML defines what content is allowed under each type of element.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!-- <li> is only allowed with <ul> or <ol> as parent -->
<div>
    <li>foo</li>
</div>

<!-- interactive elements cannot be nested -->
<button>
    <a href="#">Lorem ipsum</a>
</button>
```

```
error: <li> element is not permitted as content under <div> (element-permitted-content) at inline:3:6:
  1 | <!-- <li> is only allowed with <ul> or <ol> as parent -->
  2 | <div>
> 3 |     <li>foo</li>
    |      ^^
  4 | </div>
  5 |
  6 | <!-- interactive elements cannot be nested -->

error: <a> element is not permitted as a descendant of <button> (element-permitted-content) at inline:8:6:
  6 | <!-- interactive elements cannot be nested -->
  7 | <button>
> 8 |     <a href="#">Lorem ipsum</a>
    |      ^
  9 | </button>

2 errors found.
```

Examples of correct code for this rule:

```
<ul>
    <li>foo</li>
</ul>

<button>
    Lorem ipsum
</button>
```

## [Version history](#version-history)

- 7.2.0 - Required ancestors moved to new rule [element-required-ancestor](element-required-ancestor.html).

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-permitted-content.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-permitted-content.ts)
