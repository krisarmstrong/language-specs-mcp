HTML-validate - Require elements with optional end tags to be explicitly closed (no-implicit-close)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require elements with optional end tags to be explicitly closed

Rule ID:no-implicit-closeCategory:StyleStandards:

- HTML5

Some elements in HTML has optional end tags. When an optional tag is omitted a browser must handle it as if the end tag was present.

Omitted end tags can be ambiguous for humans to read and many editors have trouble formatting the markup.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<ul>
    <li>foo
    <li>bar
    <li>baz
</ul>
```

```
error: Element <li> is implicitly closed by sibling (no-implicit-close) at inline:2:6:
  1 | <ul>
> 2 |     <li>foo
    |      ^^
  3 |     <li>bar
  4 |     <li>baz
  5 | </ul>

error: Element <li> is implicitly closed by sibling (no-implicit-close) at inline:3:6:
  1 | <ul>
  2 |     <li>foo
> 3 |     <li>bar
    |      ^^
  4 |     <li>baz
  5 | </ul>

error: Element <li> is implicitly closed by parent </ul> (no-implicit-close) at inline:4:6:
  2 |     <li>foo
  3 |     <li>bar
> 4 |     <li>baz
    |      ^^
  5 | </ul>

3 errors found.
```

```
<p>lorem ipsum
<p>dolor sit amet
```

```
error: Element <p> is implicitly closed by sibling (no-implicit-close) at inline:1:2:
> 1 | <p>lorem ipsum
    |  ^
  2 | <p>dolor sit amet

error: Element <p> is implicitly closed by document ending (no-implicit-close) at inline:2:2:
  1 | <p>lorem ipsum
> 2 | <p>dolor sit amet
    |  ^

2 errors found.
```

```
<p>
    <div>lorem ipsum</div>
</p>
```

```
error: Element <p> is implicitly closed by adjacent <div> (no-implicit-close) at inline:1:2:
> 1 | <p>
    |  ^
  2 |     <div>lorem ipsum</div>
  3 | </p>

1 error found.
```

Examples of correct code for this rule:

```
<ul>
     <li>foo</li>
     <li>bar</li>
     <li>baz</li>
</ul>
```

```
<p>lorem ipsum</p>
<p>dolor sit amet</p>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-implicit-close.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-implicit-close.ts)
