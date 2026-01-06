On this page

# function-linear-gradient-no-nonstandard-direction

Disallow non-standard direction values for linear gradient functions.

```
.foo { background: linear-gradient(to top, #fff, #000); }
/**                                ↑
 * This (optional) first argument is the "direction" */
```

A valid and standard direction value is one of the following:

- an angle
- `to` plus a side-or-corner (`to top`, `to bottom`, `to left`, `to right`; `to top right`, `to right top`, `to bottom left`, etc.)

A common mistake (matching outdated non-standard syntax) is to use just a side-or-corner without the preceding `to`.

This rule overlaps with:

- [at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)
- [declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)

We recommend using these rules for CSS and this rule for CSS-like languages, such as SCSS and Less.

## Options[​](#options)

### `true`[​](#true)

```
{
  "function-linear-gradient-no-nonstandard-direction": true
}
```

The following patterns are considered problems:

```
.foo { background: linear-gradient(top, #fff, #000); }
```

```
.foo { background: linear-gradient(bottom, #fff, #000); }
```

```
.foo { background: linear-gradient(left, #fff, #000); }
```

```
.foo { background: linear-gradient(45, #fff, #000); }
```

```
.foo { background: linear-gradient(to top top, #fff, #000); }
```

The following patterns are not considered problems:

```
.foo { background: linear-gradient(to top, #fff, #000); }
```

```
.foo { background: linear-gradient(to bottom right, #fff, #000); }
```

```
.foo { background: linear-gradient(45deg, #fff, #000); }
```

```
.foo { background: linear-gradient(1.57rad, #fff, #000); }
```

```
/* Direction defaults to "to bottom" */
.foo { background: linear-gradient(#fff, #000); }
```

[Previousfunction-disallowed-list](/user-guide/rules/function-disallowed-list)[Nextfunction-name-case](/user-guide/rules/function-name-case)

- [Options](#options)

  - [true](#true)
