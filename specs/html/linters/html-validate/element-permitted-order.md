HTML-validate - Validate required element order (element-permitted-order)Toggle navigation[HTML-validate v10.5.0](/)

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

# Validate required element order

Rule ID:element-permitted-orderCategory:Content modelStandards:

- HTML5

Some elements has a specific order the children must use.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!-- table caption must be used before thead -->
<table>
    <thead></thead>
    <caption></caption>
</div>
```

```
error: Element <caption> must be used before <thead> in this context (element-permitted-order) at inline:4:6:
  2 | <table>
  3 |     <thead></thead>
> 4 |     <caption></caption>
    |      ^^^^^^^
  5 | </div>

1 error found.
```

Examples of correct code for this rule:

```
<table>
    <caption></caption>
    <thead></thead>
</table>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-permitted-order.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-permitted-order.ts)
