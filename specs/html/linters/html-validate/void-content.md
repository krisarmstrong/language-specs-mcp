## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallows void element with content

Rule ID:void-contentCategory:Content modelStandards:

- HTML5

HTML [void elements](https://www.w3.org/TR/html5/syntax.html#void-contents) cannot have any content and must not have an end tag.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<img></img>
```

```
error: End tag for <img> must be omitted (void-content) at inline:1:7:
> 1 | <img></img>
    |       ^^^^

1 error found.
```

Examples of correct code for this rule:

```
<img>
<img/>
```
