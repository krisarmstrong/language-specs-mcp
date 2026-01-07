HTML-validate - Validate permitted number of element occurrences (element-permitted-occurrences)Toggle navigation[HTML-validate v10.5.0](/)

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

# Validate permitted number of element occurrences

Rule ID:element-permitted-occurrencesCategory:Content modelStandards:

- HTML5

Some elements may only be used a fixed amount of times in given context.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!-- table footer can only be used once -->
<table>
    <tfoot></tfoot>
    <tfoot></tfoot>
</div>
```

```
error: Element <tfoot> can only appear once under <table> (element-permitted-occurrences) at inline:4:6:
  2 | <table>
  3 |     <tfoot></tfoot>
> 4 |     <tfoot></tfoot>
    |      ^^^^^
  5 | </div>

1 error found.
```

Examples of correct code for this rule:

```
<table>
    <tfoot></tfoot>
</table>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-permitted-occurrences.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-permitted-occurrences.ts)
