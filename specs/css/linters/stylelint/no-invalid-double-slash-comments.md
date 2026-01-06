On this page

# no-invalid-double-slash-comments

Disallow invalid double-slash comments.

```
a {
  //color: pink;
}
/** ↑
 *  This comment */
```

Disallow double-slash comments (`//...`) are not supported by CSS and [could lead to unexpected results](https://stackoverflow.com/a/20192639/130652).

If you are using a preprocessor that allows `//` single-line comments (e.g. Sass, Less, Stylus), this rule will not complain about those. They are compiled into standard CSS comments by your preprocessor, so Stylelint will consider them valid. This rule only complains about the lesser-known method of using `//` to "comment out" a single-line of code in regular CSS. (If you didn't know this was possible, have a look at ["Single Line Comments (//) in CSS"](http://www.xanthir.com/b4U10)).

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-invalid-double-slash-comments": true
}
```

The following patterns are considered problems:

```
a {
  //color: pink;
}
```

```
//a { color: pink; }
```

```
// Comment {}
a {
  color: pink;
}
```

The following patterns are not considered problems:

```
a {
  /* color: pink; */
}
```

```
/* a { color: pink;  } */
```

[Previousno-empty-source](/user-guide/rules/no-empty-source)[Nextno-invalid-position-at-import-rule](/user-guide/rules/no-invalid-position-at-import-rule)

- [Options](#options)

  - [true](#true)
