# Markdown Generation Checklist

**Read this BEFORE writing Markdown. Consistency and accessibility matter.**

## Critical: You Must Do These

### 1. Use Proper Heading Hierarchy
```markdown
<!-- BAD - skipped levels -->
# Main Title
### Subsection  <!-- Skipped h2! -->
##### Detail    <!-- Skipped h4! -->

<!-- GOOD - sequential hierarchy -->
# Main Title
## Section
### Subsection
#### Detail
```

### 2. Always Include Alt Text for Images
```markdown
<!-- BAD - no alt text -->
![](screenshot.png)
![][image]

<!-- GOOD - descriptive alt text -->
![Dashboard showing user analytics](screenshot.png)

<!-- GOOD - for decorative images -->
![](decorative-divider.png)
<!-- Note: Empty alt is OK for purely decorative images -->
```

### 3. Use Reference-Style Links for Readability
```markdown
<!-- BAD - inline links in dense text -->
Check the [documentation](https://docs.example.com/guide) and [API reference](https://docs.example.com/api) for more information about [configuration](https://docs.example.com/config).

<!-- GOOD - reference-style links -->
Check the [documentation][docs] and [API reference][api] for more
information about [configuration][config].

[docs]: https://docs.example.com/guide
[api]: https://docs.example.com/api
[config]: https://docs.example.com/config
```

### 4. Use Fenced Code Blocks with Language
```markdown
<!-- BAD - no language specified -->
```
function hello() {
  return "world";
}
```

<!-- GOOD - language specified for syntax highlighting -->
```javascript
function hello() {
  return "world";
}
```

<!-- GOOD - use appropriate language identifiers -->
```python
```typescript
```bash
```json
```yaml
```

### 5. Use Consistent List Formatting
```markdown
<!-- BAD - mixed markers -->
- Item 1
* Item 2
+ Item 3

<!-- GOOD - consistent markers -->
- Item 1
- Item 2
- Item 3

<!-- GOOD - numbered lists for ordered items -->
1. First step
2. Second step
3. Third step

<!-- Note: Numbers don't have to be sequential -->
1. First
1. Second (still renders as 2)
1. Third (still renders as 3)
```

## Important: Strong Recommendations

### 6. Add Blank Lines Around Block Elements
```markdown
<!-- BAD - cramped, may not render correctly -->
Some text.
- List item 1
- List item 2
More text.

<!-- GOOD - proper spacing -->
Some text.

- List item 1
- List item 2

More text.
```

### 7. Use Tables Appropriately
```markdown
<!-- GOOD - aligned table -->
| Name  | Role       | Department |
|-------|------------|------------|
| Alice | Developer  | Engineering|
| Bob   | Designer   | UX         |

<!-- GOOD - with alignment specifiers -->
| Left | Center | Right |
|:-----|:------:|------:|
| a    |   b    |     c |

<!-- For complex data, consider linking to a spreadsheet -->
```

### 8. Use Blockquotes for Quotations
```markdown
<!-- GOOD - blockquote for actual quotes -->
> The only way to do great work is to love what you do.
> — Steve Jobs

<!-- GOOD - for callouts/notes (common convention) -->
> **Note**: This feature requires version 2.0 or higher.

> **Warning**: This action cannot be undone.
```

### 9. Escape Special Characters When Needed
```markdown
<!-- Characters that may need escaping: \ ` * _ { } [ ] ( ) # + - . ! -->

<!-- BAD - renders as emphasis -->
Use the * character for wildcards.

<!-- GOOD - escaped -->
Use the \* character for wildcards.

<!-- GOOD - code span (preferred for code elements) -->
Use the `*` character for wildcards.
```

### 10. Use HTML Sparingly
```markdown
<!-- Avoid HTML when Markdown suffices -->

<!-- BAD - unnecessary HTML -->
<b>Bold text</b>
<i>Italic text</i>
<a href="url">Link</a>

<!-- GOOD - use Markdown -->
**Bold text**
*Italic text*
[Link](url)

<!-- OK - when Markdown can't do it -->
<details>
<summary>Click to expand</summary>

Hidden content here.

</details>

<!-- OK - for specific formatting needs -->
<kbd>Ctrl</kbd> + <kbd>C</kbd>
```

## Document Structure

### 11. Start with a Clear Title and Summary
```markdown
# Project Name

Brief one-line description of what this is.

## Overview

Slightly longer explanation of the project's purpose.

## Installation

...
```

### 12. Use Table of Contents for Long Documents
```markdown
# Project Documentation

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)

## Installation

...
```

### 13. Include Metadata When Appropriate
```markdown
---
title: API Documentation
author: Development Team
date: 2024-01-15
version: 2.0
---

# API Documentation

...
```

## Accessibility and Clarity

### 14. Write Descriptive Link Text
```markdown
<!-- BAD - unclear link text -->
Click [here](url) for more information.
[Link](url)
Read more [>>>](url)

<!-- GOOD - descriptive link text -->
Read the [installation guide](url) for setup instructions.
See the [API documentation](url) for endpoint details.
```

### 15. Use Emphasis Meaningfully
```markdown
<!-- BAD - overuse diminishes impact -->
This is **really** *very* **important** *information*.

<!-- GOOD - emphasis for actual emphasis -->
This action **cannot be undone**.
The file *must* be in UTF-8 encoding.
```

### 16. Keep Lines Reasonably Short
```markdown
<!-- BAD - very long lines are hard to read and diff -->
This is a very long line that goes on and on and contains a lot of information that would be better split across multiple lines for readability and version control purposes.

<!-- GOOD - wrapped at ~80-100 characters -->
This is a long line that has been wrapped at a reasonable point
for better readability and cleaner diffs in version control.

<!-- Or use semantic line breaks -->
This is a sentence.
This is another sentence that relates to the first.
This is a third sentence starting a new thought.
```

---

**Quick Reference - Copy This Mental Model:**
- Sequential heading hierarchy (h1 > h2 > h3)
- Alt text for all images
- Reference-style links for dense text
- Fenced code blocks with language
- Consistent list markers (all `-` or all `*`)
- Blank lines around block elements
- Escape special characters or use code spans
- Minimal HTML (only when necessary)
- Descriptive link text (not "click here")
- Meaningful emphasis (not decoration)
- Wrap long lines for readability
