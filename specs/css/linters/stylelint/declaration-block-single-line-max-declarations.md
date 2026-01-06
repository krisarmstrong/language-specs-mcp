On this page

# declaration-block-single-line-max-declarations

Limit the number of declarations within a single-line declaration block.

```
a { color: pink; top: 0; }
/** ↑            ↑
 * The number of these declarations */
```

## Options[​](#options)

### `number`[​](#number)

Specify a maximum number of declarations allowed.

Given:

```
{
  "declaration-block-single-line-max-declarations": 1
}
```

The following patterns are considered problems:

```
a { color: pink; top: 3px; }
```

```
a,
b { color: pink; top: 3px; }
```

The following patterns are not considered problems:

```
a { color: pink; }
```

```
a,
b { color: pink; }
```

```
a {
  color: pink;
  top: 3px;
}
```

[Previousdeclaration-block-no-shorthand-property-overrides](/user-guide/rules/declaration-block-no-shorthand-property-overrides)[Nextdeclaration-empty-line-before](/user-guide/rules/declaration-empty-line-before)

- [Options](#options)

  - [number](#number)
