# Biome Security Rules

Rules that prevent security vulnerabilities.

## noDangerouslySetInnerHtml

Prevent XSS via dangerouslySetInnerHTML.

```tsx
// BAD
<div dangerouslySetInnerHTML={{ __html: userContent }} />

// GOOD - sanitize first
import DOMPurify from "dompurify";
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userContent) }} />

// BETTER - avoid when possible
<div>{userContent}</div>
```

## noDangerouslySetInnerHtmlWithChildren

Don't combine dangerouslySetInnerHTML with children.

```tsx
// BAD - children are ignored
<div dangerouslySetInnerHTML={{ __html: html }}>
  <span>Child</span>
</div>

// GOOD - use one or the other
<div dangerouslySetInnerHTML={{ __html: html }} />
// or
<div><span>Child</span></div>
```

## noGlobalEval

Don't use eval().

```typescript
// BAD
eval(userInput);
new Function(userInput);
setTimeout(userInput, 1000);
setInterval(userInput, 1000);

// GOOD
JSON.parse(userInput);  // for data
// Use proper parsing for code
```

## Configuration

```json
{
  "linter": {
    "rules": {
      "security": {
        "noDangerouslySetInnerHtml": "error",
        "noDangerouslySetInnerHtmlWithChildren": "error",
        "noGlobalEval": "error"
      }
    }
  }
}
```
