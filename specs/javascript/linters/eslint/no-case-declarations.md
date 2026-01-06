# no-case-declarations

Disallow lexical declarations in case clauses

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

This rule disallows lexical declarations (`let`, `const`, `function` and `class`) in `case`/`default` clauses. The reason is that the lexical declaration is visible in the entire `switch` block but it only gets initialized when it is assigned, which will only happen if the `case` where it is defined is reached.

To ensure that the lexical declaration only applies to the current `case` clause wrap your clauses in blocks.

## Rule Details

This rule aims to prevent access to uninitialized lexical bindings as well as accessing hoisted functions across `case` clauses.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2FzZS1kZWNsYXJhdGlvbnM6IFwiZXJyb3JcIiovXG5cbnN3aXRjaCAoZm9vKSB7XG4gICAgY2FzZSAxOlxuICAgICAgICBsZXQgeCA9IDE7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgMjpcbiAgICAgICAgY29uc3QgeSA9IDI7XG4gICAgICAgIGJyZWFrO1xuICAgIGNhc2UgMzpcbiAgICAgICAgZnVuY3Rpb24gZigpIHt9XG4gICAgICAgIGJyZWFrO1xuICAgIGRlZmF1bHQ6XG4gICAgICAgIGNsYXNzIEMge31cbn0ifQ==)

```
/*eslint no-case-declarations: "error"*/

switch (foo) {
    case 1:
        let x = 1;
        break;
    case 2:
        const y = 2;
        break;
    case 3:
        function f() {}
        break;
    default:
        class C {}
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY2FzZS1kZWNsYXJhdGlvbnM6IFwiZXJyb3JcIiovXG5cbi8vIERlY2xhcmF0aW9ucyBvdXRzaWRlIHN3aXRjaC1zdGF0ZW1lbnRzIGFyZSB2YWxpZFxuY29uc3QgYSA9IDA7XG5cbnN3aXRjaCAoZm9vKSB7XG4gICAgLy8gVGhlIGZvbGxvd2luZyBjYXNlIGNsYXVzZXMgYXJlIHdyYXBwZWQgaW50byBibG9ja3MgdXNpbmcgYnJhY2tldHNcbiAgICBjYXNlIDE6IHtcbiAgICAgICAgbGV0IHggPSAxO1xuICAgICAgICBicmVhaztcbiAgICB9XG4gICAgY2FzZSAyOiB7XG4gICAgICAgIGNvbnN0IHkgPSAyO1xuICAgICAgICBicmVhaztcbiAgICB9XG4gICAgY2FzZSAzOiB7XG4gICAgICAgIGZ1bmN0aW9uIGYoKSB7fVxuICAgICAgICBicmVhaztcbiAgICB9XG4gICAgY2FzZSA0OlxuICAgICAgICAvLyBEZWNsYXJhdGlvbnMgdXNpbmcgdmFyIHdpdGhvdXQgYnJhY2tldHMgYXJlIHZhbGlkIGR1ZSB0byBmdW5jdGlvbi1zY29wZSBob2lzdGluZ1xuICAgICAgICB2YXIgeiA9IDQ7XG4gICAgICAgIGJyZWFrO1xuICAgIGRlZmF1bHQ6IHtcbiAgICAgICAgY2xhc3MgQyB7fVxuICAgIH1cbn0ifQ==)

```
/*eslint no-case-declarations: "error"*/

// Declarations outside switch-statements are valid
const a = 0;

switch (foo) {
    // The following case clauses are wrapped into blocks using brackets
    case 1: {
        let x = 1;
        break;
    }
    case 2: {
        const y = 2;
        break;
    }
    case 3: {
        function f() {}
        break;
    }
    case 4:
        // Declarations using var without brackets are valid due to function-scope hoisting
        var z = 4;
        break;
    default: {
        class C {}
    }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

## When Not To Use It

If you depend on fall through behavior and want access to bindings introduced in the `case` block.

## Related Rules

- [no-fallthrough](/docs/latest/rules/no-fallthrough)

## Version

This rule was introduced in ESLint v1.9.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-case-declarations.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-case-declarations.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-case-declarations.md
                    
                
                )
