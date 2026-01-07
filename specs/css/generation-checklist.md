# CSS Generation Checklist

**Read this BEFORE writing CSS. Modern CSS is powerful—use it properly.**

## Critical: You Must Do These

### 1. Use CSS Custom Properties (Variables)
```css
/* BAD - hardcoded values everywhere */
.button { background: #007bff; }
.link { color: #007bff; }
.header { border-bottom: 1px solid #007bff; }

/* GOOD - CSS custom properties */
:root {
  --color-primary: #007bff;
  --color-text: #333;
  --spacing-md: 1rem;
  --border-radius: 4px;
}

.button { background: var(--color-primary); }
.link { color: var(--color-primary); }
```

### 2. Use Relative Units, Not Pixels for Typography
```css
/* BAD - fixed pixels don't respect user preferences */
body { font-size: 16px; }
h1 { font-size: 32px; }

/* GOOD - relative units */
:root { font-size: 100%; }  /* Respects browser settings */
body { font-size: 1rem; }
h1 { font-size: 2rem; }
p { line-height: 1.5; }     /* Unitless for inheritance */
```

### 3. Use Modern Layout: Flexbox and Grid
```css
/* BAD - float-based layouts */
.container { overflow: hidden; }
.sidebar { float: left; width: 200px; }
.main { margin-left: 200px; }

/* GOOD - Flexbox for 1D layouts */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

/* GOOD - Grid for 2D layouts */
.page {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
}
```

### 4. Mobile-First Responsive Design
```css
/* BAD - desktop-first requires overriding */
.container { width: 1200px; }
@media (max-width: 768px) {
  .container { width: 100%; }
}

/* GOOD - mobile-first, enhance upward */
.container { width: 100%; }
@media (min-width: 768px) {
  .container { max-width: 750px; }
}
@media (min-width: 1200px) {
  .container { max-width: 1140px; }
}
```

### 5. Use Logical Properties for Internationalization
```css
/* BAD - assumes LTR text direction */
.card {
  margin-left: 1rem;
  padding-right: 2rem;
  text-align: left;
}

/* GOOD - logical properties work with RTL */
.card {
  margin-inline-start: 1rem;
  padding-inline-end: 2rem;
  text-align: start;
}
```

## Important: Strong Recommendations

### 6. Use BEM or Consistent Naming Convention
```css
/* BAD - unclear, conflicts likely */
.header { }
.title { }
.active { }

/* GOOD - BEM naming */
.header { }
.header__title { }
.header__nav { }
.header--sticky { }  /* Modifier */

.card { }
.card__image { }
.card__title { }
.card--featured { }
```

### 7. Prefer Classes Over IDs and Element Selectors
```css
/* BAD - high specificity, hard to override */
#main-header { }
div.container > ul li a { }

/* GOOD - low, consistent specificity */
.main-header { }
.nav-link { }
```

### 8. Use `min()`, `max()`, `clamp()` for Responsive Values
```css
/* BAD - media queries for every breakpoint */
.title { font-size: 1.5rem; }
@media (min-width: 768px) { .title { font-size: 2rem; } }
@media (min-width: 1200px) { .title { font-size: 2.5rem; } }

/* GOOD - fluid typography */
.title {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
}

/* GOOD - constrained width */
.container {
  width: min(90%, 1200px);
}
```

### 9. Use `aspect-ratio` for Consistent Proportions
```css
/* BAD - padding hack */
.video-container {
  position: relative;
  padding-bottom: 56.25%;  /* 16:9 */
}

/* GOOD - aspect-ratio property */
.video-container {
  aspect-ratio: 16 / 9;
}

.square-image {
  aspect-ratio: 1;
  object-fit: cover;
}
```

### 10. Use `:is()` and `:where()` for Selector Lists
```css
/* BAD - repetitive */
article h1,
article h2,
article h3,
section h1,
section h2,
section h3 {
  color: navy;
}

/* GOOD - :is() selector */
:is(article, section) :is(h1, h2, h3) {
  color: navy;
}

/* :where() has zero specificity */
:where(article, section) h1 {
  margin-top: 0;
}
```

## Accessibility

### 11. Ensure Sufficient Color Contrast
```css
/* BAD - low contrast */
.text { color: #999; background: #fff; }  /* Fails WCAG */

/* GOOD - sufficient contrast (4.5:1 minimum for body text) */
.text { color: #595959; background: #fff; }

/* Use tools to check:
   - WebAIM Contrast Checker
   - Chrome DevTools */
```

### 12. Don't Disable Focus Indicators
```css
/* BAD - removes accessibility feature */
*:focus { outline: none; }

/* GOOD - customize, don't remove */
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Hide outline for mouse, show for keyboard */
:focus:not(:focus-visible) {
  outline: none;
}
```

### 13. Use `prefers-reduced-motion`
```css
/* GOOD - respect user preferences */
@media (prefers-reduced-motion: no-preference) {
  .animated {
    transition: transform 0.3s ease;
  }
}

/* Alternative: reduce, don't remove */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Performance

### 14. Prefer `transform` and `opacity` for Animations
```css
/* BAD - triggers layout/paint */
.animate {
  transition: left 0.3s, width 0.3s;
}

/* GOOD - only compositor properties */
.animate {
  transition: transform 0.3s, opacity 0.3s;
  will-change: transform;  /* Use sparingly */
}
```

### 15. Use `contain` for Isolation
```css
/* GOOD - contains layout recalculations */
.card {
  contain: content;  /* or layout, paint, style */
}

/* For virtualized lists */
.list-item {
  contain: strict;
  content-visibility: auto;
}
```

### 16. Avoid Universal Selectors in Key Positions
```css
/* BAD - expensive selectors */
* { }
[class*="icon-"] { }
div * { }

/* GOOD - specific selectors */
.icon { }
.card > .icon { }
```

---

**Quick Reference - Copy This Mental Model:**
- CSS custom properties for theming
- Relative units (rem, em) for typography
- Flexbox for 1D, Grid for 2D layouts
- Mobile-first media queries
- Logical properties for i18n
- BEM naming convention
- Classes over IDs
- `clamp()` for fluid sizing
- `aspect-ratio` for proportions
- Check color contrast (4.5:1+)
- Customize focus, don't remove
- `prefers-reduced-motion` support
- Transform/opacity for animations
