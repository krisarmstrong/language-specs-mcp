On this page

# keyframe-selector-notation

Specify keyword or percentage notation for keyframe selectors.

```
@keyframes foo { from {} to {} }
/**              ↑       ↑
 *               These notations */
```

The keyword `from` is equivalent to the value `0%`. The keyword `to` is equivalent to the value `100%`.

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule.

## Options[​](#options)

### `"keyword"`[​](#keyword)

Keyframe selectors must always use the keyword notation.

```
{
  "keyframe-selector-notation": "keyword"
}
```

The following pattern is considered a problem:

```
@keyframes foo { 0% {} 100% {} }
```

The following pattern is not considered a problem:

```
@keyframes foo { from {} to {} }
```

### `"percentage"`[​](#percentage)

Keyframe selectors must always use the percentage notation.

```
{
  "keyframe-selector-notation": "percentage"
}
```

The following pattern is considered a problem:

```
@keyframes foo { from {} to {} }
```

The following pattern is not considered a problem:

```
@keyframes foo { 0% {} 100% {} }
```

### `"percentage-unless-within-keyword-only-block"`[​](#percentage-unless-within-keyword-only-block)

Keyframe selectors must use the percentage notation unless within a keyword-only block.

```
{
  "keyframe-selector-notation": "percentage-unless-within-keyword-only-block"
}
```

The following pattern is considered a problem:

```
@keyframes foo { from {} 100% {} }
```

The following patterns are not considered problems:

```
@keyframes foo { 0% {} 100% {} }
```

```
@keyframes foo { from {} to {} }
```

[Previouskeyframe-declaration-no-important](/user-guide/rules/keyframe-declaration-no-important)[Nextkeyframes-name-pattern](/user-guide/rules/keyframes-name-pattern)

- [Options](#options)

  - ["keyword"](#keyword)
  - ["percentage"](#percentage)
  - ["percentage-unless-within-keyword-only-block"](#percentage-unless-within-keyword-only-block)
