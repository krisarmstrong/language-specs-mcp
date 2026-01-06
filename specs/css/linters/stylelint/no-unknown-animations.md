On this page

# no-unknown-animations

Disallow unknown animations.

```
a { animation-name: fancy-slide; }
/**                    ↑
 *   This animation name */

a { animation: fancy-slide 2s linear; }
/**                    ↑
 *           And this one */
```

This rule considers the identifiers of `@keyframes` rules defined within the same source to be known.

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-unknown-animations": true
}
```

The following patterns are considered problems:

```
a { animation-name: fancy-slide; }
```

```
a { animation: fancy-slide 2s linear; }
```

```
a { animation-name: fancccy-slide; }
@keyframes fancy-slide {}
```

```
a { animation: linear 100ms fancccy-slide; }
@keyframes fancy-slide {}
```

```
a { animation-name: jump; }
@keyframes fancy-slide {}
```

The following patterns are not considered problems:

```
a { animation-name: fancy-slide; }
@keyframes fancy-slide {}
```

```
@keyframes fancy-slide {}
a { animation-name: fancy-slide; }
```

```
@keyframes fancy-slide {}
a { animation: fancy-slide 2s linear; }
```

```
a { animation: 100ms steps(12, end) fancy-slide; }
@keyframes fancy-slide {}
```

[Previousno-irregular-whitespace](/user-guide/rules/no-irregular-whitespace)[Nextno-unknown-custom-media](/user-guide/rules/no-unknown-custom-media)

- [Options](#options)

  - [true](#true)
