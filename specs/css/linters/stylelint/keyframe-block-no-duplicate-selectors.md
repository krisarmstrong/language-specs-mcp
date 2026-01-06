On this page

# keyframe-block-no-duplicate-selectors

Disallow duplicate selectors within keyframe blocks.

```
@keyframes foo { 0% {} 0% {} }
/**                    ↑
 *                     This duplicate selector */
```

This rule is case-insensitive.

## Options[​](#options)

### `true`[​](#true)

```
{
  "keyframe-block-no-duplicate-selectors": true
}
```

The following patterns are considered problems:

```
@keyframes foo { 0% {} 0% {} }
```

```
@keyframes foo { from {} from {} }
```

```
@keyframes foo { from {} FROM {} }
```

The following patterns are not considered problems:

```
@keyframes foo { 0% {} 100% {} }
```

```
@keyframes foo { from {} to {} }
```

[Previousimport-notation](/user-guide/rules/import-notation)[Nextkeyframe-declaration-no-important](/user-guide/rules/keyframe-declaration-no-important)

- [Options](#options)

  - [true](#true)
