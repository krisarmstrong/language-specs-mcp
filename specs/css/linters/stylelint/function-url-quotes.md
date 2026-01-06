On this page

# function-url-quotes

Require or disallow quotes for urls.

```
a { background: url("x.jpg") }
/**                 ↑     ↑
 *             These quotes */
```

The [fix option](/user-guide/options#fix) can automatically fix most of the problems reported by this rule.

## Options[​](#options)

### `"always"`[​](#always)

Urls must always be quoted.

```
{
  "function-url-quotes": "always"
}
```

The following patterns are considered problems:

```
@import url(foo.css);
```

```
@font-face { font-family: 'foo'; src: url(foo.ttf); }
```

The following patterns are not considered problems:

```
a { background: url('x.jpg'); }
```

```
@import url("foo.css");
```

```
@font-face { font-family: "foo"; src: url("foo.ttf"); }
```

### `"never"`[​](#never)

Urls must never be quoted.

```
{
  "function-url-quotes": "never"
}
```

The following patterns are considered problems:

```
a { background: url('x.jpg'); }
```

```
@import url("foo.css");
```

```
@font-face { font-family: "foo"; src: url('foo.ttf'); }
```

The following patterns are not considered problems:

```
a { background: url(x.jpg); }
```

```
@import url(foo.css);
```

```
@font-face { font-family: 'foo'; src: url(foo.ttf); }
```

## Optional secondary options[​](#optional-secondary-options)

### `except`[​](#except)

```
{ "except": ["array", "of", "options"] }
```

#### `"empty"`[​](#empty)

Reverse the primary option for functions that have no arguments.

Given:

```
{
  "function-url-quotes": ["always", { "except": ["empty"] }]
}
```

The following patterns are not considered problems:

```
@-moz-document url-prefix() {}
```

[Previousfunction-url-no-scheme-relative](/user-guide/rules/function-url-no-scheme-relative)[Nextfunction-url-scheme-allowed-list](/user-guide/rules/function-url-scheme-allowed-list)

- [Options](#options)

  - ["always"](#always)
  - ["never"](#never)

- [Optional secondary options](#optional-secondary-options)

  - [except](#except)
