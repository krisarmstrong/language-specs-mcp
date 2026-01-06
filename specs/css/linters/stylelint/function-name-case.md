On this page

# function-name-case

Specify lowercase or uppercase for function names.

```
a { width: calc(5% - 10em); }
/**        ↑
 * This function */
```

Camel case function names, e.g. `translateX`, are accounted for when the `lower` option is used.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"lower"`[​](#lower)

```
{
  "function-name-case": "lower"
}
```

The following patterns are considered problems:

```
a {
  width: Calc(5% - 10em);
}
```

```
a {
  width: cAlC(5% - 10em);
}
```

```
a {
  width: CALC(5% - 10em);
}
```

```
a {
  background: -WEBKIT-RADIAL-GRADIENT(red, green, blue);
}
```

The following patterns are not considered problems:

```
a {
  width: calc(5% - 10em);
}
```

```
a {
  background: -webkit-radial-gradient(red, green, blue);
}
```

### `"upper"`[​](#upper)

```
{
  "function-name-case": "upper"
}
```

The following patterns are considered problems:

```
a {
  width: Calc(5% - 10em);
}
```

```
a {
  width: cAlC(5% - 10em);
}
```

```
a {
  width: calc(5% - 10em);
}
```

```
a {
  background: -webkit-radial-gradient(red, green, blue);
}
```

The following patterns are not considered problems:

```
a {
  width: CALC(5% - 10em);
}
```

```
a {
  background: -WEBKIT-RADIAL-GRADIENT(red, green, blue);
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignoreFunctions`[​](#ignorefunctions)

```
{ "ignoreFunctions": ["array", "of", "functions", "/regex/"] }
```

Ignore case of function names.

Given:

```
{
  "function-name-case": [
    "lower",
    { "ignoreFunctions": ["--some-function", "/^--get.*$/"] }
  ]
}
```

The following patterns are considered problems:

```
a {
  color: --sOmE-FuNcTiOn();
}
```

```
a {
  color: --GetColor();
}
```

```
a {
  color: --GET_COLOR();
}
```

The following patterns are not considered problems:

```
a {
  display: --some-function();
}
```

```
a {
  display: --getColor();
}
```

```
a {
  display: --get_color();
}
```

[Previousfunction-linear-gradient-no-nonstandard-direction](/user-guide/rules/function-linear-gradient-no-nonstandard-direction)[Nextfunction-no-unknown](/user-guide/rules/function-no-unknown)

- [Options](#options)

  - ["lower"](#lower)
  - ["upper"](#upper)

- [Optional secondary options](#optional-secondary-options)

  - [ignoreFunctions](#ignorefunctions)
