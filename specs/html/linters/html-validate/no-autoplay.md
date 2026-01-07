HTML-validate - Disallow autoplaying media elements (no-autoplay)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow autoplaying media elements

Rule ID:no-autoplayCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

Autoplaying content can be disruptive for users and has accessibility issues. This rule disallows `<audio>` and `<video>` with autoplay enabled.

Unless the user is expecting media to play automatically it is better to let the user control playback. The media might be too loud or the user might be in a location where audio is discouraged.

Users with assistive technology might find it hard to pause as they must first navigate to the controls. Media can be distracting for users with cognitive or concentration issues and if the video contains flashing or blinking sequences it can cause epilepsy.

There are also issues where some browsers use heuristics to prevent autoplaying so results may vary when used.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<video autoplay></video>
```

```
error: The autoplay attribute is not allowed on <video> (no-autoplay) at inline:1:8:
> 1 | <video autoplay></video>
    |        ^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<video></video>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "include": ["audio", "video"],
  "exclude": []
}
```

### [include](#include)

If set only elements listed in this array generates errors.

### [exclude](#exclude)

If set elements listed in this array is ignored.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/no-autoplay.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/no-autoplay.ts)
