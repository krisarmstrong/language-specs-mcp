On this page

# keyframes-name-pattern

Specify a pattern for keyframe names.

```
@keyframes slide-right {}
/**             ↑
 * The pattern of this */
```

## Options[​](#options)

### `string`[​](#string)

Specify a regex string not surrounded with `"/"`.

Given:

```
{
  "keyframes-name-pattern": "foo-.+"
}
```

The following patterns are considered problems:

```
@keyframes foo {}
```

```
@keyframes bar {}
```

```
@keyframes FOO-bar {}
```

The following patterns are not considered problems:

```
@keyframes foo-bar {}
```

[Previouskeyframe-selector-notation](/user-guide/rules/keyframe-selector-notation)[Nextlayer-name-pattern](/user-guide/rules/layer-name-pattern)

- [Options](#options)

  - [string](#string)
