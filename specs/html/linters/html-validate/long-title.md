## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require title not to have too long text

Rule ID:long-titleCategory:SEOStandards:-

Search engines truncates titles with too long text, typically only displaying the first 60-70 characters. Possibly down-ranking the page in the process as it raises the suspicion of keyword stuffing.

See [MDN recommendation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title#Page_titles_and_SEO) and [WCAG G88: Providing descriptive
titles](https://www.w3.org/WAI/WCAG21/Techniques/general/G88).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<head>
    <title>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</title>
</head>
```

```
error: title text cannot be longer than 70 characters (long-title) at inline:2:142:
  1 | <head>
> 2 |     <title>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</title>
    |                                                                                                                                              ^
  3 | </head>

1 error found.
```

Examples of correct code for this rule:

```
<head>
    <title>Lorem ipsum</title>
</head>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "maxlength": 120
}
```

### [maxlength](#maxlength)

Set a custom max length (inclusive).
