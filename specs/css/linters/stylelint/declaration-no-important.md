On this page

# declaration-no-important

Disallow `!important` within declarations.

```
a { color: pink !important; }
/**             ↑
 * This !important */
```

If you always want `!important` in your declarations, e.g. if you're writing [user styles](https://userstyles.org/), you can safely add them using [postcss-safe-important](https://github.com/crimx/postcss-safe-important).

## Options[​](#options)

### `true`[​](#true)

```
{
  "declaration-no-important": true
}
```

The following patterns are considered problems:

```
a { color: pink !important; }
```

```
a { color: pink ! important; }
```

```
a { color: pink!important; }
```

The following patterns are not considered problems:

```
a { color: pink; }
```

[Previousdeclaration-empty-line-before](/user-guide/rules/declaration-empty-line-before)[Nextdeclaration-property-max-values](/user-guide/rules/declaration-property-max-values)

- [Options](#options)

  - [true](#true)
