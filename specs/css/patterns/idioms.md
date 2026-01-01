# CSS Idioms

## Prefer modern layout

- Use Flexbox and Grid over floats.

## Use custom properties for theming

```css
:root { --brand-color: #0b5fff; }
.button { color: var(--brand-color); }
```

## Avoid overly specific selectors

Keep selectors short and maintainable.
