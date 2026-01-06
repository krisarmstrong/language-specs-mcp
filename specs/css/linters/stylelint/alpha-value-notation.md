On this page

# alpha-value-notation

Specify percentage or number notation for alpha-values.

```
    a { color: rgb(0 0 0 / 0.5) }
/**                        ↑
 *                         This notation */
```

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"number"`[​](#number)

Alpha-values must always use the number notation.

```
{
  "alpha-value-notation": "number"
}
```

The following patterns are considered problems:

```
a { opacity: 50% }
```

```
a { color: rgb(0 0 0 / 50%) }
```

The following patterns are not considered problems:

```
a { opacity: 0.5 }
```

```
a { color: rgb(0 0 0 / 0.5) }
```

### `"percentage"`[​](#percentage)

Alpha-values must always use percentage notation.

```
{
  "alpha-value-notation": "percentage"
}
```

The following patterns are considered problems:

```
a { opacity: 0.5 }
```

```
a { color: rgb(0 0 0 / 0.5) }
```

The following patterns are not considered problems:

```
a { opacity: 50% }
```

```
a { color: rgb(0 0 0 / 50%) }
```

## Optional secondary options[​](#optional-secondary-options)

### `exceptProperties`[​](#exceptproperties)

```
{ "exceptProperties": ["array", "of", "properties", "/regex/"] }
```

Reverse the primary option for matching properties.

Given:

```
{
  "alpha-value-notation": ["percentage", { "exceptProperties": ["opacity"] }]
}
```

The following patterns are considered problems:

```
a { opacity: 50% }
```

```
a { color: rgb(0 0 0 / 0.5) }
```

The following patterns are not considered problems:

```
a { opacity: 0.5 }
```

```
a { color: rgb(0 0 0 / 50%) }
```

[PreviousRules](/user-guide/rules)[Nextannotation-no-unknown](/user-guide/rules/annotation-no-unknown)

- [Options](#options)

  - ["number"](#number)
  - ["percentage"](#percentage)

- [Optional secondary options](#optional-secondary-options)

  - [exceptProperties](#exceptproperties)
