On this page

# selector-pseudo-element-colon-notation

Specify single or double colon notation for applicable pseudo-element selectors.

```
    a::before {}
/**  ↑
 * This notation */
```

The `::` notation was chosen for pseudo-elements to establish a discrimination between pseudo-classes (which subclass existing elements) and pseudo-elements (which are elements not represented in the document tree).

However, for compatibility with existing style sheets, user agents also accept the previous one-colon notation for pseudo-elements introduced in CSS levels 1 and 2 (namely, `:first-line`, `:first-letter`, `:before` and `:after`).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"single"`[​](#single)

Applicable pseudo-elements must always use the single colon notation.

```
{
  "selector-pseudo-element-colon-notation": "single"
}
```

The following patterns are considered problems:

```
a::before { color: pink; }
```

```
a::after { color: pink; }
```

```
a::first-letter { color: pink; }
```

```
a::first-line { color: pink; }
```

The following patterns are not considered problems:

```
a:before { color: pink; }
```

```
a:after { color: pink; }
```

```
a:first-letter { color: pink; }
```

```
a:first-line { color: pink; }
```

```
input::placeholder { color: pink; }
```

```
li::marker { font-variant-numeric: tabular-nums; }
```

### `"double"`[​](#double)

Applicable pseudo-elements must always use the double colon notation.

```
{
  "selector-pseudo-element-colon-notation": "double"
}
```

The following patterns are considered problems:

```
a:before { color: pink; }
```

```
a:after { color: pink; }
```

```
a:first-letter { color: pink; }
```

```
a:first-line { color: pink; }
```

The following patterns are not considered problems:

```
a::before { color: pink; }
```

```
a::after { color: pink; }
```

```
a::first-letter { color: pink; }
```

```
a::first-line { color: pink; }
```

```
input::placeholder { color: pink; }
```

```
li::marker { font-variant-numeric: tabular-nums; }
```

[Previousselector-pseudo-element-allowed-list](/user-guide/rules/selector-pseudo-element-allowed-list)[Nextselector-pseudo-element-disallowed-list](/user-guide/rules/selector-pseudo-element-disallowed-list)

- [Options](#options)

  - ["single"](#single)
  - ["double"](#double)
