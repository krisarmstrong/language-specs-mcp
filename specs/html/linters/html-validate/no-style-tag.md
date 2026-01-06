## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow usage of `<style>` tag

Rule ID:no-style-tagCategory:StyleStandards:-

The `<style>` tag can be used to write CSS directly inside the document. When using multiple documents it is preferable to put all styling in a single asset and use the `<link>` tag to reference it to lower the bandwidth required (by preventing duplicated style across all page loads).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<style>
    body {
        background-color: hotpink;
    }
</style>
```

```
error: Use external stylesheet with <link> instead of <style> tag (no-style-tag) at inline:1:1:
> 1 | <style>
    | ^^^^^^
  2 |     body {
  3 |         background-color: hotpink;
  4 |     }

1 error found.
```

Examples of correct code for this rule:

```
<link rel="stylesheet" src="my-style.css">
```
