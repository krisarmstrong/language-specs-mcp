On this page

# color-function-notation

Specify modern or legacy notation for color-functions.

```
    a { color: rgb(0 0 0 / 0.2) }
/**            ↑
 *             This notation */
```

Modern color-functions use a comma-free syntax because functions in CSS are used to group/name a syntax chunk. They should work by the same rules that CSS grammar does in general: values are optional and re-orderable when possible, space-separated, and commas are used to separate repetitions only.

For legacy reasons, `rgb()` and `hsl()` also supports an alternate syntax that separates all of its arguments with commas. Also for legacy reasons, the `rgba()` and `hsla()` functions exist using the same comma-based syntax.

The [fix option](/user-guide/options#fix) can automatically fix some of the problems reported by this rule when the primary option is `"modern"`.

## Options[​](#options)

### `"modern"`[​](#modern)

Applicable color-functions must always use modern notation.

```
{
  "color-function-notation": "modern"
}
```

The following patterns are considered problems:

```
a { color: rgb(0, 0, 0) }
```

```
a { color: rgba(12, 122, 231, 0.2) }
```

```
a { color: hsla(270, 60%, 50%, 15%) }
```

```
a { color: hsl(.75turn, 60%, 70%) }
```

The following patterns are not considered problems:

```
a { color: rgb(0 0 0) }
```

```
a { color: rgb(12 122 231 / 0.2) }
```

```
a { color: hsl(270 60% 50% / 15%) }
```

```
a { color: hsl(.75turn 60% 70%) }
```

### `"legacy"`[​](#legacy)

Applicable color-functions must always use the legacy notation.

```
{
  "color-function-notation": "legacy"
}
```

The following patterns are considered problems:

```
a { color: rgb(0 0 0) }
```

```
a { color: rgb(12 122 231 / 0.2) }
```

```
a { color: hsl(270 60% 50% / 15%) }
```

```
a { color: hsl(.75turn 60% 70%) }
```

The following patterns are not considered problems:

```
a { color: rgb(0, 0, 0) }
```

```
a { color: rgba(12, 122, 231, 0.2) }
```

```
a { color: hsla(270, 60%, 50%, 15%) }
```

```
a { color: hsl(.75turn, 60%, 70%) }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"with-var-inside"`[​](#with-var-inside)

Ignore color functions containing variables.

Given:

```
{
  "color-function-notation": ["modern", { "ignore": ["with-var-inside"] }]
}
```

The following patterns are not considered problems:

```
a {
  color: rgba(var(--foo), 0.5);
}
```

Given:

```
{
  "color-function-notation": ["legacy", { "ignore": ["with-var-inside"] }]
}
```

The following patterns are not considered problems:

```
a {
  color: rgba(var(--foo) / 0.5);
}
```

[Previouscolor-function-alias-notation](/user-guide/rules/color-function-alias-notation)[Nextcolor-hex-alpha](/user-guide/rules/color-hex-alpha)

- [Options](#options)

  - ["modern"](#modern)
  - ["legacy"](#legacy)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
