On this page

# declaration-block-no-shorthand-property-overrides

Disallow shorthand properties that override related longhand properties.

```
a { background-repeat: repeat; background: green; }
/**                            ↑
 * This overrides the longhand property before it */
```

In almost every case, this is just an authorial oversight. For more about this behavior, see [MDN's documentation of shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties).

## Options[​](#options)

### `true`[​](#true)

```
{
  "declaration-block-no-shorthand-property-overrides": true
}
```

The following patterns are considered problems:

```
a {
  padding-left: 10px;
  padding: 20px;
}
```

```
a {
  transition-property: opacity;
  transition: opacity 1s linear;
}
```

```
a {
  -webkit-transition-property: opacity;
  -webkit-transition: opacity 1s linear;
}
```

```
a {
  border-top-width: 1px;
  top: 0;
  bottom: 3px;
  border: 2px solid blue;
}
```

The following patterns are not considered problems:

```
a { padding: 10px; padding-left: 20px; }
```

```
a { transition-property: opacity; } a { transition: opacity 1s linear; }
```

```
a { transition-property: opacity; -webkit-transition: opacity 1s linear; }
```

[Previousdeclaration-block-no-redundant-longhand-properties](/user-guide/rules/declaration-block-no-redundant-longhand-properties)[Nextdeclaration-block-single-line-max-declarations](/user-guide/rules/declaration-block-single-line-max-declarations)

- [Options](#options)

  - [true](#true)
