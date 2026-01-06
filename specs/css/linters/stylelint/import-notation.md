On this page

# import-notation

Specify string or URL notation for `@import` rules.

```
@import url("x.jpg");
/**     ↑
 *      This notation */
```

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"string"`[​](#string)

`@import` rules must always use string notation.

```
{
  "import-notation": "string"
}
```

The following patterns are considered problems:

```
@import url(foo.css);
```

```
@import url('foo.css');
```

```
@import url("foo.css");
```

The following patterns are not considered problems:

```
@import 'foo.css';
```

```
@import "foo.css";
```

### `"url"`[​](#url)

`@import` rules must always use URL notation.

```
{
  "import-notation": "url"
}
```

The following patterns are considered problems:

```
@import 'foo.css';
```

```
@import "foo.css";
```

The following patterns are not considered problems:

```
@import url(foo.css);
```

```
@import url('foo.css');
```

```
@import url("foo.css");
```

[Previoushue-degree-notation](/user-guide/rules/hue-degree-notation)[Nextkeyframe-block-no-duplicate-selectors](/user-guide/rules/keyframe-block-no-duplicate-selectors)

- [Options](#options)

  - ["string"](#string)
  - ["url"](#url)
