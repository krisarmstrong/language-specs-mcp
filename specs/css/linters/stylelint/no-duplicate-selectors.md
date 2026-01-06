On this page

# no-duplicate-selectors

Disallow duplicate selectors.

```
    .foo {} .bar {} .foo {}
/** ↑               ↑
 * These duplicates */
```

This rule checks for two types of duplication:

- Duplication of a single selector with a rule's selector list, e.g. `a, b, a {}`.
- Duplication of a selector list within a stylesheet, e.g. `a, b {} a, b {}`. Duplicates are found even if the selectors come in different orders or have different spacing, e.g. `a d, b > c {} b>c, a d {}`.

The same selector is allowed to repeat in the following circumstances:

- It is used in different selector lists, e.g. `a {} a, b {}`.
- The duplicates are determined to originate in different stylesheets, e.g. you have concatenated or compiled files in a way that produces sourcemaps for PostCSS to read, e.g. postcss-import.
- The duplicates are in rules with different parent nodes, e.g. inside and outside of a media query.

This rule resolves nested selectors. So `a b {} a { & b {} }` counts as a problem, because the resolved selectors end up with a duplicate.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-duplicate-selectors": true
}
```

The following patterns are considered problems:

```
.foo,
.bar,
.foo {}
```

```
.foo {}
.bar {}
.foo {}
```

```
.foo .bar {}
.bar {}
.foo .bar {}
```

```
@media (min-width: 10px) {
  .foo {}
  .foo {}
}
```

```
.foo, .bar {}
.bar, .foo {}
```

```
a .foo, b + .bar {}
b+.bar,
a
  .foo {}
```

```
a b {}
a {
  & b {}
}
```

The following patterns are not considered problems:

```
.foo {}
@media (min-width: 10px) {
  .foo {}
}
```

```
.foo {
  .foo {}
}
```

```
.foo {}
.bar {}
.foo .bar {}
.bar .foo {}
```

```
a b {}
a {
  & b,
  & c {}
}
```

## Optional secondary options[​](#optional-secondary-options)

### `disallowInList`[​](#disallowinlist)

This option will also disallow duplicate selectors within selector lists. Defaults to `false`.

Given:

```
{
  "no-duplicate-selectors": [true, { "disallowInList": true }]
}
```

The following patterns are considered problems:

```
input, textarea {
  border: 2px;
}
textarea {
  border: 1px;
}
```

[Previousno-duplicate-at-import-rules](/user-guide/rules/no-duplicate-at-import-rules)[Nextno-empty-source](/user-guide/rules/no-empty-source)

- [Options](#options)

  - [true](#true)

- [Optional secondary options](#optional-secondary-options)

  - [disallowInList](#disallowinlist)
