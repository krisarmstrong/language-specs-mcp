# JavaScript Generation Checklist

**Most JavaScript rules are shared with TypeScript. See the full checklist:**
→ [TypeScript Generation Checklist](../typescript/generation-checklist.md)

## JavaScript-Specific Additions

### Use JSDoc for Type Documentation (When Not Using TS)
```javascript
/**
 * Process user data
 * @param {Object} user - The user object
 * @param {string} user.name - User's name
 * @param {number} user.age - User's age
 * @returns {boolean} Success status
 */
function processUser(user) {
    // ...
}
```

### Consider TypeScript for New Projects
For any non-trivial project, TypeScript provides:
- Compile-time error checking
- Better IDE support
- Self-documenting code
- Easier refactoring

---

**Quick Reference (Same as TypeScript):**
- `const` > `let` > never `var`
- `===` always, never `==`
- Handle all Promise rejections
- `?.` and `??` for null safety
- Array methods > loops
- async/await > .then chains
- Never insert user input as HTML
