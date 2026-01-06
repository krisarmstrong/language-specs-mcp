# no-empty-static-block

Disallow empty static blocks

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Empty static blocks, while not technically errors, usually occur due to refactoring that wasn’t completed. They can cause confusion when reading code.

## Rule Details

This rule disallows empty static blocks. This rule ignores static blocks which contain a comment.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktc3RhdGljLWJsb2NrOiBcImVycm9yXCIqL1xuXG5jbGFzcyBGb28ge1xuICAgIHN0YXRpYyB7fVxufSJ9)

```
/*eslint no-empty-static-block: "error"*/

class Foo {
    static {}
}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktc3RhdGljLWJsb2NrOiBcImVycm9yXCIqL1xuXG5jbGFzcyBGb28ge1xuICAgIHN0YXRpYyB7XG4gICAgICAgIGJhcigpO1xuICAgIH1cbn1cblxuY2xhc3MgQmFyIHtcbiAgICBzdGF0aWMge1xuICAgICAgICAvLyBjb21tZW50XG4gICAgfVxufSJ9)

```
/*eslint no-empty-static-block: "error"*/

class Foo {
    static {
        bar();
    }
}

class Bar {
    static {
        // comment
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
```

## When Not To Use It

This rule should not be used in environments prior to ES2022.

## Related Rules

- [no-empty](/docs/latest/rules/no-empty)
- [no-empty-function](/docs/latest/rules/no-empty-function)

## Version

This rule was introduced in ESLint v8.27.0.

## Further Reading

[GitHub - tc39/proposal-class-static-block: ECMAScript class static initialization blocks](https://github.com/tc39/proposal-class-static-block)
 github.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-empty-static-block.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-empty-static-block.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-empty-static-block.md
                    
                
                )
