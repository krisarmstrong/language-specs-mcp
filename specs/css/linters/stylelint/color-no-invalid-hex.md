On this page

# color-no-invalid-hex

Disallow invalid hex colors.

```
a { color: #y3 }
/**        ↑
 * This hex color */
```

Longhand hex colors can be either 6 or 8 (with alpha channel) hexadecimal characters. And their shorthand variants are 3 and 4 characters respectively.

This rule overlaps with:

- [at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)
- [declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)

We recommend using these rules for CSS and this rule for CSS-like languages, such as SCSS and Less.

## Options[​](#options)

### `true`[​](#true)

```
{
  "color-no-invalid-hex": true
}
```

The following patterns are considered problems:

```
a { color: #00; }
```

```
a { color: #fff1az; }
```

```
a { color: #12345aa; }
```

The following patterns are not considered problems:

```
a { color: #000; }
```

```
a { color: #000f; }
```

```
a { color: #fff1a0; }
```

```
a { color: #123450aa; }
```

[Previouscolor-no-hex](/user-guide/rules/color-no-hex)[Nextcomment-empty-line-before](/user-guide/rules/comment-empty-line-before)

- [Options](#options)

  - [true](#true)
