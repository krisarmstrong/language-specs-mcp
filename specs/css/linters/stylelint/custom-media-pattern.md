On this page

# custom-media-pattern

Specify a pattern for custom media query names.

```
@custom-media --foo (max-width: 30em);
/**             ↑
 * The pattern of this */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

Given:

```
{
  "custom-media-pattern": "foo-.+"
}
```

The following patterns are considered problems:

```
@custom-media --bar (min-width: 30em);
```

The following patterns are not considered problems:

```
@custom-media --foo-bar (min-width: 30em);
```

[Previouscontainer-name-pattern](/user-guide/rules/container-name-pattern)[Nextcustom-property-empty-line-before](/user-guide/rules/custom-property-empty-line-before)

- [Options](#options)

  - [string](#string)
