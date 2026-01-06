On this page

# function-url-no-scheme-relative

Disallow scheme-relative urls.

```
a { background-image: url('//www.example.org/file.jpg'); }
/**                        ↑
 *  This scheme-relative url */
```

A [scheme-relative url](https://url.spec.whatwg.org/#syntax-url-scheme-relative) is a url that begins with `//` followed by a host.

This rule ignores url arguments that are variables (`$sass`, `@less`, `--custom-property`).

## Options[​](#options)

### `true`[​](#true)

```
{
  "function-url-no-scheme-relative": true
}
```

The following patterns are considered problems:

```
a {
  background: url("//www.example.org/file.jpg");
}
```

```
@import url("//www.example.org/foo.css");
```

The following patterns are not considered problems:

```
a {
  background: url("../file.jpg");
}
```

```
a {
  background: url("http://www.example.org/file.jpg");
}
```

```
a {
  background: url("/path/to/file.jpg");
}
```

```
@import url("http://www.example.org/foo.css");
```

```
@import url("/path/to/foo.css");
```

[Previousfunction-no-unknown](/user-guide/rules/function-no-unknown)[Nextfunction-url-quotes](/user-guide/rules/function-url-quotes)

- [Options](#options)

  - [true](#true)
