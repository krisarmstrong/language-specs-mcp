On this page

# container-name-pattern

Specify a pattern for container names.

```
@container foo (width > 400px) {}
/**        ↑
 * The pattern of this */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

Given:

```
{
  "container-name-pattern": "foo-.+"
}
```

The following patterns are considered problems:

```
@container foo {}
```

```
a { container-name: bar; }
```

```
a { container: baz / inline-size; }
```

The following patterns are not considered problems:

```
@container foo-bar {}
```

```
a { container-name: foo-bar; }
```

```
a { container: foo-baz / inline-size; }
```

[Previouscomment-word-disallowed-list](/user-guide/rules/comment-word-disallowed-list)[Nextcustom-media-pattern](/user-guide/rules/custom-media-pattern)

- [Options](#options)

  - [string](#string)
