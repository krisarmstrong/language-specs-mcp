On this page

# function-url-scheme-disallowed-list

Specify a list of disallowed URL schemes.

```
a { background-image: url('http://www.example.com/file.jpg'); }
/**                        ↑
 *           This URL scheme */
```

A [URL scheme](https://url.spec.whatwg.org/#syntax-url-scheme) consists of alphanumeric, `+`, `-`, and `.` characters. It can appear at the start of a URL and is followed by `:`.

This rule ignores:

- URL arguments without an existing URL scheme
- URL arguments with variables or variable interpolation (`$sass`, `@less`, `--custom-property`, `#{$var}`, `@{var}`, `$(var)`)

## Options[​](#options)

### `Array<string>`[​](#arraystring)

```
["array", "of", "schemes", "/regex/"]
```

Given:

```
{
  "function-url-scheme-disallowed-list": ["ftp", "/^http/"]
}
```

The following patterns are considered problems:

```
a { background-image: url('ftp://www.example.com/file.jpg'); }
```

```
a { background-image: url('http://www.example.com/file.jpg'); }
```

```
a { background-image: url('https://www.example.com/file.jpg'); }
```

The following patterns are not considered problems:

```
a { background-image: url('data:image/gif;base64,R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs='); }
```

```
a { background-image: url('example.com/file.jpg'); }
```

```
a { background-image: url('/example.com/file.jpg'); }
```

```
a { background-image: url('//example.com/file.jpg'); }
```

```
a { background-image: url('./path/to/file.jpg'); }
```

[Previousfunction-url-scheme-allowed-list](/user-guide/rules/function-url-scheme-allowed-list)[Nexthue-degree-notation](/user-guide/rules/hue-degree-notation)

- [Options](#options)

  - [Array<string>](#arraystring)
