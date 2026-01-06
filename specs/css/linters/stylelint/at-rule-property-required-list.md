On this page

# at-rule-property-required-list

Specify a list of required properties (or descriptors) for an at-rule.

```
    @font-face { font-display: swap; font-family: 'foo'; }
/**  ↑           ↑                   ↑
 *  At-rule and required descriptor names */
```

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
{ "at-rule-name": ["array", "of", "properties", "or", "descriptors"] }
```

Given:

```
{
  "at-rule-property-required-list": {
    "font-face": ["font-display", "font-family", "font-style"]
  }
}
```

The following patterns are considered problems:

```
@font-face {
    font-family: 'foo';
    src: url('./fonts/foo.woff2') format('woff2');
}
```

```
@font-face {
    font-family: 'foo';
    font-style: normal;
    src: url('./fonts/foo.woff2') format('woff2');
}
```

The following patterns are not considered problems:

```
@font-face {
    font-display: swap;
    font-family: 'foo';
    font-style: normal;
    src: url('./fonts/foo.woff2') format('woff2');
}
```

[Previousat-rule-prelude-no-invalid](/user-guide/rules/at-rule-prelude-no-invalid)[Nextblock-no-empty](/user-guide/rules/block-no-empty)

- [Options](#options)

  - [Array<string>](#arraystring)
