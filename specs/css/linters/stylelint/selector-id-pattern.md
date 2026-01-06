On this page

# selector-id-pattern

Specify a pattern for ID selectors.

```
.foo, #bar.baz a, #hoo[disabled] { color: pink; }
/**   ↑           ↑
 * These ID selectors */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

The selector value after `#` will be checked. No need to include `#` in your pattern.

Given:

```
{
  "selector-id-pattern": "foo-[a-z]+"
}
```

The following patterns are considered problems:

```
#foop {}
```

```
#foo-BAR {}
```

```
div > .zing + #foo-BAR {}
```

The following patterns are not considered problems:

```
#foo-bar {}
```

```
div > .zing + #foo-bar {}
```

```
.foop {}
```

```
[foo='bar'] {}
```

[Previousselector-disallowed-list](/user-guide/rules/selector-disallowed-list)[Nextselector-max-attribute](/user-guide/rules/selector-max-attribute)

- [Options](#options)

  - [string](#string)
