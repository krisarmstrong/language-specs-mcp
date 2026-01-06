On this page

# color-named

Require (where possible) or disallow named colors.

```
a { color: black }
/**        ↑
 * This named color */
```

This rule ignores `$sass` and `@less` variable syntaxes.

## Options[​](#options)

### `"always-where-possible"`[​](#always-where-possible)

Colors must always, where possible, be named.

```
{
  "color-named": "always-where-possible"
}
```

This will complain if a hex (3, 4, 6 and 8 digit), `rgb()`, `rgba()`, `hsl()`, `hsla()`, `hwb()` or `gray()` color can be represented as a named color.

The following patterns are considered problems:

```
a { color: #000; }
```

```
a { color: #f000; }
```

```
a { color: #ff000000; }
```

```
a { color: rgb(0, 0, 0); }
```

```
a { color: rgb(0%, 0%, 0%); }
```

```
a { color: rgba(0, 0, 0, 0); }
```

```
a { color: hsl(0, 0%, 0%); }
```

```
a { color: hwb(0, 0%, 100%); }
```

```
a { color: gray(0); }
```

The following patterns are not considered problems:

```
a { color: black; }
```

```
a { color: rgb(10, 0, 0); }
```

```
a { color: rgb(0, 0, 0, 0.5); }
```

### `"never"`[​](#never)

Colors must never be named.

```
{
  "color-named": "never"
}
```

The following patterns are considered problems:

```
a { color: black; }
```

```
a { color: white; }
```

The following patterns are not considered problems:

```
a { color: #000; }
```

```
a { color: rgb(0, 0, 0); }
```

```
a { color: var(--white); }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"inside-function"`[​](#inside-function)

Ignore colors that are inside a function.

Given:

```
{
  "color-named": ["never", { "ignore": ["inside-function"] }]
}
```

The following patterns are not considered problems:

```
a {
  color: map-get($color, blue);
}
```

```
a {
  background-image: url(red);
}
```

### `ignoreProperties`[​](#ignoreproperties)

```
{ "ignoreProperties": ["array", "of", "properties", "/regex/"] }
```

Given:

```
{
  "color-named": ["never", { "ignoreProperties": ["/^my-/", "composes"] }]
}
```

The following patterns are not considered problems:

```
a {
  my-property: red;
}
```

```
a {
  my-other-property: red;
}
```

```
a {
  composes: red from './index.css';
}
```

[Previouscolor-hex-length](/user-guide/rules/color-hex-length)[Nextcolor-no-hex](/user-guide/rules/color-no-hex)

- [Options](#options)

  - ["always-where-possible"](#always-where-possible)
  - ["never"](#never)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
  - [ignoreProperties](#ignoreproperties)
