On this page

# keyframe-declaration-no-important

Disallow invalid `!important` within keyframe declarations.

```
@keyframes foo {
  from { opacity: 0 }
  to { opacity: 1 !important }
}              /* ↑ */
/**               ↑
*   This !important */
```

Using `!important` within keyframes declarations is [completely ignored in some browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes#!important_in_a_keyframe).

## Options[​](#options)

### `true`[​](#true)

```
{
  "keyframe-declaration-no-important": true
}
```

The following pattern is considered a problem:

```
@keyframes foo {
  from {
    opacity: 0;
  }
  to {
    opacity: 1 !important;
  }
}
```

The following patterns are not considered problems:

```
@keyframes foo {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
```

```
a { color: pink !important; }
```

[Previouskeyframe-block-no-duplicate-selectors](/user-guide/rules/keyframe-block-no-duplicate-selectors)[Nextkeyframe-selector-notation](/user-guide/rules/keyframe-selector-notation)

- [Options](#options)

  - [true](#true)
