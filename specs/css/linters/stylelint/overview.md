# Stylelint Overview

CSS/SCSS/Less linter.

**Source:** https://stylelint.io/

## Running

```bash
# Lint
stylelint "**/*.css"
stylelint "src/**/*.scss"

# Fix
stylelint --fix "**/*.css"

# Specific config
stylelint --config .stylelintrc.json "**/*.css"

# Output formats
stylelint "**/*.css" --formatter verbose
stylelint "**/*.css" --formatter json
```

## Configuration

`.stylelintrc.json`:

```json
{
  "extends": [
    "stylelint-config-standard",
    "stylelint-config-recommended-scss"
  ],
  "plugins": [
    "stylelint-scss",
    "stylelint-order"
  ],
  "rules": {
    "color-hex-length": "long",
    "color-named": "never",
    "declaration-block-no-redundant-longhand-properties": true,
    "declaration-no-important": true,
    "font-family-name-quotes": "always-where-recommended",
    "function-url-quotes": "always",
    "max-nesting-depth": 3,
    "no-descending-specificity": true,
    "no-duplicate-selectors": true,
    "property-no-vendor-prefix": true,
    "selector-class-pattern": "^[a-z][a-z0-9]*(-[a-z0-9]+)*$",
    "selector-max-compound-selectors": 3,
    "selector-max-id": 0,
    "selector-no-qualifying-type": true,
    "selector-pseudo-element-colon-notation": "double",
    "shorthand-property-no-redundant-values": true,
    "value-no-vendor-prefix": true,
    "order/properties-alphabetical-order": true
  },
  "ignoreFiles": [
    "node_modules/**",
    "dist/**"
  ]
}
```

## Rule Categories

| Category | Description |
|----------|-------------|
| Possible errors | Catch likely mistakes |
| Limit language features | Restrict usage |
| Stylistic issues | Formatting/style |
| SCSS/Sass rules | Preprocessor specific |

## Key Rules

### Possible Errors

**color-no-invalid-hex**

```css
/* BAD */
.example { color: #00; }
.example { color: #fff1az; }

/* GOOD */
.example { color: #000000; }
.example { color: #fff1a0; }
```

**declaration-block-no-duplicate-properties**

```css
/* BAD */
.example {
  color: red;
  font-size: 16px;
  color: blue;
}

/* GOOD */
.example {
  color: blue;
  font-size: 16px;
}
```

**no-duplicate-selectors**

```css
/* BAD */
.foo { color: red; }
.bar { color: blue; }
.foo { font-size: 16px; }

/* GOOD */
.foo {
  color: red;
  font-size: 16px;
}
.bar { color: blue; }
```

**no-descending-specificity**

```css
/* BAD */
.container .item { color: red; }
.item { color: blue; }  /* Less specific comes after more specific */

/* GOOD */
.item { color: blue; }
.container .item { color: red; }
```

### Limit Language Features

**declaration-no-important**

```css
/* BAD */
.example { color: red !important; }

/* GOOD */
.example { color: red; }
.specific.selector { color: red; }
```

**selector-max-id**

```css
/* BAD (if max is 0) */
#header { color: red; }
#nav #link { color: blue; }

/* GOOD */
.header { color: red; }
.nav .link { color: blue; }
```

**max-nesting-depth**

```scss
/* BAD (if max is 3) */
.a {
  .b {
    .c {
      .d {
        color: red;  /* 4 levels deep */
      }
    }
  }
}

/* GOOD */
.a .b .c .d { color: red; }
```

**color-named**

```css
/* BAD (if "never") */
.example { color: red; }
.example { background: white; }

/* GOOD */
.example { color: #ff0000; }
.example { background: #ffffff; }
```

**selector-class-pattern**

```css
/* BAD (if BEM pattern) */
.myComponent { }
.my_component { }

/* GOOD */
.my-component { }
.my-component__element { }
.my-component--modifier { }
```

### Stylistic Issues

**color-hex-length**

```css
/* BAD (if "long") */
.example { color: #fff; }

/* GOOD */
.example { color: #ffffff; }
```

**indentation**

```css
/* BAD */
.example {
color: red;
  font-size: 16px;
}

/* GOOD */
.example {
  color: red;
  font-size: 16px;
}
```

**declaration-colon-space-after**

```css
/* BAD */
.example { color:red; }
.example { color :red; }

/* GOOD */
.example { color: red; }
```

**selector-pseudo-element-colon-notation**

```css
/* BAD (if "double") */
.example:before { }
.example:after { }

/* GOOD */
.example::before { }
.example::after { }
```

**length-zero-no-unit**

```css
/* BAD */
.example { margin: 0px; }
.example { padding: 0em; }

/* GOOD */
.example { margin: 0; }
.example { padding: 0; }
```

**shorthand-property-no-redundant-values**

```css
/* BAD */
.example { margin: 1px 1px 1px 1px; }
.example { padding: 10px 20px 10px 20px; }

/* GOOD */
.example { margin: 1px; }
.example { padding: 10px 20px; }
```

**declaration-block-no-redundant-longhand-properties**

```css
/* BAD */
.example {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 10px;
  margin-left: 20px;
}

/* GOOD */
.example {
  margin: 10px 20px;
}
```

### Property Order

With `stylelint-order` plugin:

```json
{
  "plugins": ["stylelint-order"],
  "rules": {
    "order/properties-alphabetical-order": true
  }
}
```

Or grouped:

```json
{
  "rules": {
    "order/properties-order": [
      "display",
      "position",
      "top", "right", "bottom", "left",
      "width", "height",
      "margin", "padding",
      "font", "color",
      "background"
    ]
  }
}
```

### SCSS Rules

With `stylelint-scss`:

```json
{
  "plugins": ["stylelint-scss"],
  "rules": {
    "scss/at-rule-no-unknown": true,
    "scss/dollar-variable-pattern": "^[a-z][a-z0-9]*(-[a-z0-9]+)*$",
    "scss/selector-no-redundant-nesting-selector": true,
    "scss/no-duplicate-mixins": true
  }
}
```

**scss/selector-no-redundant-nesting-selector**

```scss
/* BAD */
.parent {
  & .child { }  /* & is redundant */
}

/* GOOD */
.parent {
  .child { }
}
```

## Inline Ignores

```css
/* stylelint-disable */
.ignored { color: red !important; }
/* stylelint-enable */

/* stylelint-disable declaration-no-important */
.specific { color: red !important; }
/* stylelint-enable declaration-no-important */

.example {
  color: red !important; /* stylelint-disable-line declaration-no-important */
}

/* stylelint-disable-next-line declaration-no-important */
.example { color: red !important; }
```

## Common Config Presets

```bash
# Standard CSS
npm install stylelint-config-standard

# Recommended (fewer rules)
npm install stylelint-config-recommended

# Standard SCSS
npm install stylelint-config-standard-scss

# Prettier compatibility
npm install stylelint-config-prettier
```

```json
{
  "extends": [
    "stylelint-config-standard",
    "stylelint-config-prettier"
  ]
}
```
