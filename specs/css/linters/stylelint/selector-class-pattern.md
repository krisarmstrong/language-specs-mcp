On this page

# selector-class-pattern

Specify a pattern for class selectors.

```
    .foo, #bar.baz span, #hoo[disabled] { color: pink; }
/** ↑         ↑
 * These class selectors */
```

This rule ignores non-outputting Less mixin definitions and called Less mixins.

Escaped selectors (e.g. `.u-size-11\/12\@sm`) are parsed as escaped twice (e.g. `.u-size-11\\/12\\@sm`). Your RegExp should account for that.

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

The selector value after `.` will be checked. No need to include `.` in your pattern.

Given:

```
{
  "selector-class-pattern": "foo-[a-z]+"
}
```

The following patterns are considered problems:

```
.foop {}
```

```
.foo-BAR {}
```

```
div > #zing + .foo-BAR {}
```

The following patterns are not considered problems:

```
.foo-bar {}
```

```
div > #zing + .foo-bar {}
```

```
#foop {}
```

```
[foo='bar'] {}
```

## Optional secondary options[​](#optional-secondary-options)

### `resolveNestedSelectors`[​](#resolvenestedselectors)

This option will resolve nested selectors with `&` interpolation. Defaults to `false`.

Given the string:

```
{
  "selector-class-pattern": ["^[A-Z]+$", { "resolveNestedSelectors": true }]
}
```

The following patterns are considered problems:

```
.A {
  &__B {} /* resolved to ".A__B" */
}
```

The following patterns are not considered problems:

```
.A {
  &B {} /* resolved to ".AB" */
}
```

[Previousselector-attribute-quotes](/user-guide/rules/selector-attribute-quotes)[Nextselector-combinator-allowed-list](/user-guide/rules/selector-combinator-allowed-list)

- [Options](#options)

  - [string](#string)

- [Optional secondary options](#optional-secondary-options)

  - [resolveNestedSelectors](#resolvenestedselectors)
