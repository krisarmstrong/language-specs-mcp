On this page

# selector-disallowed-list

Specify a list of disallowed selectors.

```
    .foo > .bar {}
/** ↑
 * This is selector */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "selectors", "/regex/"]
```

Given:

```
{
  "selector-disallowed-list": ["a > .foo", "/\\[data-.+]/"]
}
```

The following patterns are considered problems:

```
a > .foo {}
```

```
a[data-auto="1"] {}
```

```
.foo, [data-auto="1"] {}
```

The following patterns are not considered problems:

```
.foo {}
```

```
a
>
.foo {}
```

```
.bar > a > .foo {}
```

```
.data-auto {}
```

```
a[href] {}
```

## Optional secondary options[​](#optional-secondary-options)

### `splitList`[​](#splitlist)

Split selector lists into individual selectors. Defaults to `false`.

Given:

```
{
  "selector-disallowed-list": [".foo", { "splitList": true }]
}
```

The following pattern is considered a problem:

```
.bar, .foo {}
```

The following pattern is not considered a problem:

```
.bar .foo {}
```

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"inside-block"`[​](#inside-block)

Ignore selectors that are inside a block.

Given:

```
{
  "selector-disallowed-list": [".foo", { "ignore": ["inside-block"] }]
}
```

The following pattern is not considered a problem:

```
.bar {
  .foo {}
}
```

#### `"keyframe-selectors"`[​](#keyframe-selectors)

Ignore keyframe selectors.

Given:

```
{
  "selector-disallowed-list": ["/from/", { "ignore": ["keyframe-selectors"] }]
}
```

The following pattern is not considered a problem:

```
@keyframes fade-in {
  from {}
}
```

[Previousselector-combinator-disallowed-list](/user-guide/rules/selector-combinator-disallowed-list)[Nextselector-id-pattern](/user-guide/rules/selector-id-pattern)

- [Options](#options)

  - [Array<string>](#arraystring)

- [Optional secondary options](#optional-secondary-options)

  - [splitList](#splitlist)
  - [ignore](#ignore)
