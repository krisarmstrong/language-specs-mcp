# HTML Generation Checklist

**Read this BEFORE writing HTML. Semantic markup matters for accessibility and SEO.**

## Critical: You Must Do These

### 1. Use Semantic Elements
```html
<!-- BAD - div soup -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">
  <div class="article">...</div>
  <div class="sidebar">...</div>
</div>
<div class="footer">...</div>

<!-- GOOD - semantic elements -->
<header>
  <nav>...</nav>
</header>
<main>
  <article>...</article>
  <aside>...</aside>
</main>
<footer>...</footer>
```

### 2. Always Include Alt Text for Images
```html
<!-- BAD - missing alt -->
<img src="photo.jpg">

<!-- GOOD - descriptive alt -->
<img src="team-photo.jpg" alt="Our development team at the 2024 conference">

<!-- GOOD - decorative image (empty alt) -->
<img src="decorative-border.png" alt="">

<!-- GOOD - complex image with longer description -->
<figure>
  <img src="chart.png" alt="Sales increased 50% in Q4">
  <figcaption>Quarterly sales data showing significant Q4 growth</figcaption>
</figure>
```

### 3. Use Proper Heading Hierarchy
```html
<!-- BAD - skipped levels, style-based choices -->
<h1>Company Name</h1>
<h3>Products</h3>  <!-- Skipped h2! -->
<h5>Product One</h5>  <!-- Why h5? -->

<!-- GOOD - sequential hierarchy -->
<h1>Company Name</h1>
<h2>Products</h2>
<h3>Product One</h3>
<h3>Product Two</h3>
<h2>Services</h2>
<h3>Service One</h3>
```

### 4. Label All Form Inputs
```html
<!-- BAD - no label -->
<input type="email" placeholder="Email">

<!-- GOOD - explicit label -->
<label for="email">Email Address</label>
<input type="email" id="email" name="email">

<!-- GOOD - implicit label -->
<label>
  Email Address
  <input type="email" name="email">
</label>

<!-- GOOD - with aria-label when visual label not possible -->
<input type="search" aria-label="Search products">
```

### 5. Use Button for Clickable Actions
```html
<!-- BAD - link for action -->
<a href="#" onclick="submit()">Submit</a>
<div onclick="toggle()">Toggle</div>

<!-- GOOD - button for actions -->
<button type="submit">Submit</button>
<button type="button" onclick="toggle()">Toggle</button>

<!-- Links are for navigation -->
<a href="/products">View Products</a>
```

## Important: Strong Recommendations

### 6. Include Essential Meta Tags
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Brief description of page content">
  <title>Page Title - Site Name</title>

  <!-- Open Graph for social sharing -->
  <meta property="og:title" content="Page Title">
  <meta property="og:description" content="Description">
  <meta property="og:image" content="https://example.com/image.jpg">
</head>
```

### 7. Use Lists for Related Items
```html
<!-- BAD - divs for list content -->
<div class="features">
  <div>Fast</div>
  <div>Secure</div>
  <div>Reliable</div>
</div>

<!-- GOOD - semantic lists -->
<ul class="features">
  <li>Fast</li>
  <li>Secure</li>
  <li>Reliable</li>
</ul>

<!-- GOOD - definition list for key-value pairs -->
<dl>
  <dt>Name</dt>
  <dd>Alice Smith</dd>
  <dt>Email</dt>
  <dd>alice@example.com</dd>
</dl>
```

### 8. Use Tables for Tabular Data Only
```html
<!-- BAD - table for layout -->
<table>
  <tr><td>Logo</td><td>Navigation</td></tr>
  <tr><td colspan="2">Content</td></tr>
</table>

<!-- GOOD - table for data with headers -->
<table>
  <caption>Monthly Sales Report</caption>
  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Sales</th>
      <th scope="col">Growth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">January</th>
      <td>$10,000</td>
      <td>+5%</td>
    </tr>
  </tbody>
</table>
```

### 9. Use Appropriate Input Types
```html
<!-- BAD - generic text for everything -->
<input type="text" name="email">
<input type="text" name="phone">
<input type="text" name="date">

<!-- GOOD - semantic input types -->
<input type="email" name="email" autocomplete="email">
<input type="tel" name="phone" autocomplete="tel">
<input type="date" name="date">
<input type="url" name="website">
<input type="number" name="quantity" min="1" max="100">
<input type="password" name="password" autocomplete="current-password">
```

### 10. Use `<time>` for Dates and Times
```html
<!-- BAD - unstructured date -->
<span>January 15, 2024</span>

<!-- GOOD - machine-readable time -->
<time datetime="2024-01-15">January 15, 2024</time>
<time datetime="2024-01-15T14:30">January 15, 2024 at 2:30 PM</time>
<time datetime="PT2H30M">2 hours 30 minutes</time>
```

## Accessibility

### 11. Use ARIA Only When Necessary
```html
<!-- BAD - redundant ARIA -->
<button role="button">Click me</button>
<nav role="navigation">...</nav>

<!-- GOOD - no ARIA needed for semantic elements -->
<button>Click me</button>
<nav>...</nav>

<!-- GOOD - ARIA for custom components -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>
<div role="tabpanel" id="panel1">Content 1</div>
<div role="tabpanel" id="panel2" hidden>Content 2</div>
```

### 12. Provide Skip Links
```html
<!-- GOOD - skip to main content -->
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  <header>...</header>
  <nav>...</nav>
  <main id="main">
    <!-- Main content -->
  </main>
</body>
```

### 13. Use `aria-live` for Dynamic Content
```html
<!-- GOOD - announce dynamic updates -->
<div aria-live="polite" aria-atomic="true">
  <!-- Content updated by JavaScript will be announced -->
</div>

<!-- For urgent announcements -->
<div role="alert">Error: Please fix the highlighted fields</div>

<!-- For status messages -->
<div role="status">Form submitted successfully</div>
```

## Performance

### 14. Lazy Load Below-the-Fold Images
```html
<!-- GOOD - native lazy loading -->
<img src="photo.jpg" alt="Description" loading="lazy">

<!-- Above the fold - load eagerly -->
<img src="hero.jpg" alt="Hero image" loading="eager">

<!-- GOOD - with dimensions to prevent layout shift -->
<img src="photo.jpg" alt="Description"
     width="800" height="600" loading="lazy">
```

### 15. Preload Critical Resources
```html
<head>
  <!-- Preload critical assets -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/css/critical.css" as="style">

  <!-- Preconnect to required origins -->
  <link rel="preconnect" href="https://api.example.com">

  <!-- Prefetch likely next pages -->
  <link rel="prefetch" href="/products">
</head>
```

---

**Quick Reference - Copy This Mental Model:**
- Semantic elements (header, nav, main, article, aside, footer)
- Alt text for all images
- Sequential heading hierarchy (h1 > h2 > h3)
- Labels for all form inputs
- Button for actions, links for navigation
- Essential meta tags (charset, viewport, description)
- Lists for related items
- Tables only for tabular data
- Semantic input types
- `<time>` for dates
- ARIA only when necessary
- Skip links for keyboard users
- Lazy load images below fold
- Preload critical resources
