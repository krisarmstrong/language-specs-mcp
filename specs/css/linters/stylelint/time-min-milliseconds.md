On this page

# time-min-milliseconds

Limit the minimum number of milliseconds for time values.

```
a { animation: slip-n-slide 150ms linear; }
/**                         ↑
 *                  This time */
```

This rule checks positive numbers in `transition-duration`, `transition-delay`, `animation-duration`, `animation-delay`, and those times as they manifest in the `transition` and `animation` shorthands.

## Options[​](#options)

### `number`[​](#number)

Specify a minimum number of milliseconds for time values.

Given:

```
{
  "time-min-milliseconds": 100
}
```

The following patterns are considered problems:

```
a { animation: 80ms; }
```

```
a { transition-duration: 0.08s; }
```

```
a { transition: background-color 6ms linear; }
```

```
a { animation-delay: 0.01s; }
```

The following patterns are not considered problems:

```
a { animation: 8s; }
```

```
a { transition-duration: 0.8s; }
```

```
a { transition: background-color 600ms linear; }
```

```
a { animation-delay: 1s; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"delay"`[​](#delay)

Ignore time values for an animation or transition delay.

Given:

```
{
  "time-min-milliseconds": [200, { "ignore": ["delay"] }]
}
```

The following pattern is not considered a problem:

```
a { animation-delay: 100ms; }
```

[Previoussyntax-string-no-invalid](/user-guide/rules/syntax-string-no-invalid)[Nextunit-allowed-list](/user-guide/rules/unit-allowed-list)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
