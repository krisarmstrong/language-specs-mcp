On this page

# at-rule-no-vendor-prefix

Disallow vendor prefixes for at-rules.

```
    @-webkit-keyframes { 0% { top: 0; } }
/**   ↑
 * This prefix */
```

This rule ignores non-standard vendor-prefixed at-rules that aren't handled by [Autoprefixer](https://github.com/postcss/autoprefixer).

The [fix option](/user-guide/options#fix) can automatically fix all of the problems reported by this rule. However, it will not remove duplicate at-rules produced when the prefixes are removed. You can use [Autoprefixer](https://github.com/postcss/autoprefixer) itself, with the [add option off and the remove option on](https://github.com/postcss/autoprefixer#options), in these situations.

## Options[​](#options)

### `true`[​](#true)

```
{
  "at-rule-no-vendor-prefix": true
}
```

The following patterns are considered problems:

```
@-webkit-keyframes { 0% { top: 0; } }
```

```
@-ms-viewport { orientation: landscape; }
```

The following patterns are not considered problems:

```
@keyframes { 0% { top: 0; } }
```

```
@viewport { orientation: landscape; }
```

[Previousat-rule-no-unknown](/user-guide/rules/at-rule-no-unknown)[Nextat-rule-prelude-no-invalid](/user-guide/rules/at-rule-prelude-no-invalid)

- [Options](#options)

  - [true](#true)
