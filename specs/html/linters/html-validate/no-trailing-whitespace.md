HTML-validate - Disallow trailing whitespace (no-trailing-whitespace)Toggle navigation[HTML-validate v10.5.0](/)

- [User guide](../usage/index.html)
- [Elements](../guide/metadata/simple-component.html)
- [Rules](index.html)
- [Developers guide](../dev/using-api.html)
- [Changelog](../changelog/index.html)
- [About](../about/index.html)

html-validate-10.5.0

## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallows trailing whitespace at the end of lines

Rule ID:no-trailing-whitespaceCategory:StyleStandards:-

Lines with trailing whitespace cause unnecessary diff when using version control and usually serve no special purpose in HTML.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p>lorem ipsum</p>  
<p>dolor sit amet</p>
```

```
error: Trailing whitespace (no-trailing-whitespace) at inline:1:19:
> 1 | <p>lorem ipsum</p>  
    |                   ^^
> 2 | <p>dolor sit amet</p>
    | ^

1 error found.
```

Examples of correct code for this rule:

```
<p>lorem ipsum</p>
<p>dolor sit amet</p>
```

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-trailing-whitespace.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-trailing-whitespace.ts)
