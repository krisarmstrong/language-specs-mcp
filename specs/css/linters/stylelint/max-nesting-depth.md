On this page

# max-nesting-depth

Limit the depth of nesting.

```
a { & > b { top: 0; } }
/** ↑
 * This nesting */
```

This rule works by checking rules' and at-rules' actual "nesting depth" against your specified max. Here's how nesting depths works:

```
a {
  & b { /* nesting depth 1 */
    & .foo { /* nesting depth 2 */
      @media print { /* nesting depth 3 */
        & .baz { /* nesting depth 4 */
          color: pink;
        }
      }
    }
  }
}
```

note

root-level at-rules will not be included in the nesting depth calculation, because most users would take for granted that root-level at-rules are "free" (because necessary). So both of the following `.foo` rules have a nesting depth of 2, and will therefore pass if your `max` is less than or equal to 2:

```
a {
  b { /* 1 */
    .foo {} /* 2 */
  }
}

@media print { /* ignored */
  a {
    b { /* 1 */
      .foo {} /* 2 */
    }
  }
}
```

This rule integrates into Stylelint's core the functionality of the (now deprecated) plugin [stylelint-statement-max-nesting-depth](https://github.com/davidtheclark/stylelint-statement-max-nesting-depth).

## Options[​](#options)

### `number`[​](#number)

Specify a maximum nesting depth allowed.

Given:

```
{
  "max-nesting-depth": 2
}
```

The following patterns are considered problems:

```
a {
  & .foo { /* 1 */
    &__foo { /* 2 */
      & > .bar {} /* 3 */
    }
  }
}
```

```
a {
  @media print { /* 1 */
    & .foo { /* 2 */
      & .bar {} /* 3 */
    }
  }
}
```

The following patterns are not considered problems:

```
a {
  & .foo { /* 1 */
    &__foo {} /* 2 */
  }
}

a .foo__foo .bar .baz {}
```

```
@media print {
  a {
    & .foo { /* 1 */
      &__foo {} /* 2 */
    }
  }
}
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"blockless-at-rules"`[​](#blockless-at-rules)

Ignore at-rules that only wrap other rules, and do not themselves have declaration blocks.

Given:

```
{
  "max-nesting-depth": [1, { "ignore": ["blockless-at-rules"] }]
}
```

The following patterns are considered problems:

As the at-rules have a declarations blocks.

```
a {
  &:hover { /* 1 */
    @media (min-width: 500px) { color: pink; } /* 2 */
  }
}
```

```
a {
  @nest > b { /* 1 */
    .foo { color: pink; } /* 2 */
  }
}
```

The following patterns are not considered problems:

As all of the following `.foo` rules would have a nesting depth of just 1.

```
a {
  .foo { color: pink; } /* 1 */
}
```

```
@media print { /* ignored regardless of options */
  a {
    .foo { color: pink; } /* 1 */
  }
}
```

```
a {
  @media print { /* ignored because it's an at-rule without a declaration block of its own */
    .foo { color: pink; } /* 1 */
  }
}
```

#### `"pseudo-classes"`[​](#pseudo-classes)

Ignore rules where the first selector in each selector list item is a pseudo-class

Given:

```
{
  "max-nesting-depth": [1, { "ignore": ["pseudo-classes"] }]
}
```

The following patterns are considered problems:

```
a {
  b { /* 1 */
    .c { /* 2 */
      top: 0;
    }
  }
}
```

```
a {
  &:hover { /* ignored */
    b { /* 1 */
      .c { /* 2 */
        top: 0;
      }
    }
  }
}
```

```
a {
  b { /* 1 */
    &::selection { /* 2 */
      color: #64FFDA;
    }
  }
}
```

```
a {
  b { /* 1 */
    &:hover, .c { /* 2 */
      top: 0;
    }
  }
}
```

The following patterns are not considered problems:

As all of the following pseudo-classes rules would have a nesting depth of just 1.

```
a {
  b { /* 1 */
    &:hover { /* ignored */
      top: 0;
    }
  }
}
```

```
a {
  b { /* 1 */
    &:nest {
      &:nest-lvl2 {  /* ignored */
        top: 0;
      }
    }
  }
}
```

```
a {
  &:hover {  /* ignored */
    b { /* 1 */
      top: 0;
    }
  }
}
```

```
a {
  &:nest {  /* ignored */
    &:nest-lvl2 {  /* ignored */
      top: 0;
      b { /* 1 */
        bottom: 0;
      }
    }
  }
}
```

```
a {
  b { /* 1 */
    &:hover, &:focus {  /* ignored */
      top: 0;
    }
  }
}
```

### `ignoreAtRules`[​](#ignoreatrules)

```
{ "ignoreAtRules": ["array", "of", "at-rules", "/regex/"] }
```

Ignore the specified at-rules.

Given:

```
{
  "max-nesting-depth": [1, { "ignoreAtRules": ["/^--my-/", "media"] }]
}
```

The following patterns are not considered problems:

```
a {
  @media print {      /* 1 */
    b {               /* 2 */
      c { top: 0; }   /* 3 */
    }
  }
}
```

```
a {
  b {                 /* 1 */
    @media print {    /* 2 */
      c { top: 0; }   /* 3 */
    }
  }
}
```

```
a {
  @--my-at-rule print {  /* 1 */
    b {                /* 2 */
      c { top: 0; }    /* 3 */
    }
  }
}
```

```
a {
  @--my-other-at-rule print {  /* 1 */
    b {                      /* 2 */
      c { top: 0; }          /* 3 */
    }
  }
}
```

The following patterns are considered problems:

```
a {
  @import print {       /* 1 */
    b { top: 0; }       /* 2 */
  }
}
```

```
a {
  @--not-my-at-rule print {   /* 1 */
    b { top: 0; }       /* 2 */
  }
}
```

### `ignorePseudoClasses`[​](#ignorepseudoclasses)

```
{ "ignorePseudoClasses": ["array", "of", "pseudo-classes", "/regex/"] }
```

Ignore the specified pseudo-classes.

Given:

```
{
  "max-nesting-depth": [1, { "ignorePseudoClasses": ["hover", "^focus-"] }]
}
```

The following patterns are not considered problems:

```
a {
  &:hover {   /* ignored */
    b {      /* 1 */
      top: 0;
    }
  }
}
```

```
a {
  &:hover, &:active { /* ignored */
    b {              /* 1 */
      top: 0;
    }
  }
}
```

The following patterns are considered problems:

```
a {
  &:visited { /* 1 */
    b {      /* 2 */
      top: 0;
    }
  }
}
```

```
a {
  &:hover, &:visited { /* 1 */
    b {               /* 2 */
      top: 0;
    }
  }
}
```

### `ignoreRules`[​](#ignorerules)

```
{ "ignoreRules": ["array", "of", "selectors", "/regex/"] }
```

Ignore rules matching with the specified selectors.

Given:

```
{
  "max-nesting-depth": [
    1,
    { "ignoreRules": [".my-selector", "/^.ignored-sel/"] }
  ]
}
```

The following patterns are not considered problems:

```
a {
  .my-selector {   /* ignored */
    b {      /* 1 */
      top: 0;
    }
  }
}
```

```
a {
  .my-selector, .ignored-selector { /* ignored */
    b {              /* 1 */
      top: 0;
    }
  }
}
```

The following patterns are considered problems:

```
a {
  .not-ignored-selector { /* 1 */
    b {      /* 2 */
      top: 0;
    }
  }
}
```

```
a {
  .my-selector, .not-ignored-selector { /* 1 */
    b {               /* 2 */
      top: 0;
    }
  }
}
```

[Previouslightness-notation](/user-guide/rules/lightness-notation)[Nextmedia-feature-name-allowed-list](/user-guide/rules/media-feature-name-allowed-list)

- [Options](#options)

  - [number](#number)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
  - [ignoreAtRules](#ignoreatrules)
  - [ignorePseudoClasses](#ignorepseudoclasses)
  - [ignoreRules](#ignorerules)
