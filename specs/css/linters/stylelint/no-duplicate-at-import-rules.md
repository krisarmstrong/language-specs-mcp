On this page

# no-duplicate-at-import-rules

Disallow duplicate `@import` rules.

```
    @import "a.css";
    @import "a.css";
/** ↑
 * These are duplicates */
```

## Options[​](#options)

### `true`[​](#true)

```
{
  "no-duplicate-at-import-rules": true
}
```

The following patterns are considered problems:

```
@import 'a.css';
@import 'a.css';
```

```
@import url("a.css");
@import url("a.css");
```

```
@import "a.css";
@import 'a.css';
```

```
@import "a.css";
@import 'b.css';
@import url(a.css);
```

The following patterns are not considered problems:

```
@import "a.css";
@import "b.css";
```

```
@import url('a.css') projection;
@import url('a.css') tv;
```

[Previousno-descending-specificity](/user-guide/rules/no-descending-specificity)[Nextno-duplicate-selectors](/user-guide/rules/no-duplicate-selectors)

- [Options](#options)

  - [true](#true)
