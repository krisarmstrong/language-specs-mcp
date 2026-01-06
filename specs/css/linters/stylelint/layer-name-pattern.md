On this page

# layer-name-pattern

Specify a pattern for layer names.

```
@layer foo {}
/**    ↑
 * This layer name */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

Given:

```
{
  "layer-name-pattern": "^[a-z][a-z0-9.-]*$"
}
```

The following patterns are considered problems:

```
@layer Foo;
```

```
@layer foo.Bar {}
```

```
@layer foo, Bar {}
```

```
@import "foo.css" layer(Bar);
```

The following patterns are not considered problems:

```
@layer foo;
```

```
@layer foo.bar {}
```

```
@layer foo, bar {}
```

```
@import "foo.css" layer(bar);
```

[Previouskeyframes-name-pattern](/user-guide/rules/keyframes-name-pattern)[Nextlength-zero-no-unit](/user-guide/rules/length-zero-no-unit)

- [Options](#options)

  - [string](#string)
