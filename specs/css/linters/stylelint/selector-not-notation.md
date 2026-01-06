On this page

# selector-not-notation

Specify simple or complex notation for `:not()` pseudo-class selectors.

```
    a:not(.foo, .bar) {}
/**  ↑
 * This notation */
```

In Selectors Level 3, only a single simple selector was allowed as the argument to `:not()`, whereas Selectors Level 4 allows a selector list.

Use:

- `"complex"` to author modern Selectors Level 4 CSS
- `"simple"` for backwards compatibility with older browsers

note

The notations can have different specificities. For example:

```
/* this complex notation has a specificity of 0,1,1 */
a:not(.foo, .bar) {}

/* this simple notation has a specificity of 0,2,1 */
a:not(.foo):not(.bar) {}
```

The [fix option](/user-guide/options#fix) option can automatically fix most of the problems reported by this rule.

## Options[​](#options)

### `"simple"`[​](#simple)

```
{
  "selector-not-notation": "simple"
}
```

The following patterns are considered problems:

```
:not(a, div) {}
```

```
:not(a.foo) {}
```

The following patterns are not considered problems:

```
:not(a):not(div) {}
```

```
:not(a) {}
```

### `"complex"`[​](#complex)

```
{
  "selector-not-notation": "complex"
}
```

The following pattern is considered a problem:

```
:not(a):not(div) {}
```

The following patterns are not considered problems:

```
:not(a, div) {}
```

```
:not(a.foo) {}
```

```
:not(a).foo:not(:empty) {}
```

[Previousselector-no-vendor-prefix](/user-guide/rules/selector-no-vendor-prefix)[Nextselector-pseudo-class-allowed-list](/user-guide/rules/selector-pseudo-class-allowed-list)

- [Options](#options)

  - ["simple"](#simple)
  - ["complex"](#complex)
