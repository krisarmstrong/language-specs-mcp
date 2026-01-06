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
