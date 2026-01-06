## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require meta refresh to have 0 second delay

Rule ID:meta-refreshCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

The `<meta http-equiv="refresh" content="..">` directive can be used to refresh or redirect the page. For users with assistive technology a forced refresh or redirect after a fixed duration can render the user unable to read and understand the content in time.

Generally the directive should be avoided all together but under some situations it is unavoidable (e.g. a static page generator hosted on git-based hosting solutions don't provide an alternative for server-based redirection are forced to use client-side redirection).

[WCAG H76](https://www.w3.org/WAI/WCAG22/Techniques/html/H76) requires the interval to be set to exactly 0 as to do theredirection before any content is rendered to the client.

This rule prevents non-zero time intervals and using the directive to refresh the page as it would be stuck in an infinite loop refreshing the same page over and over again.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<meta http-equiv="refresh" content="5;url=target.html">
```

```
error: Meta refresh must be instant (0 second delay) (meta-refresh) at inline:1:37:
> 1 | <meta http-equiv="refresh" content="5;url=target.html">
    |                                     ^^^^^^^^^^^^^^^^^

1 error found.
```

```
<meta http-equiv="refresh" content="0">
```

```
error: Don't use instant meta refresh to reload the page (meta-refresh) at inline:1:37:
> 1 | <meta http-equiv="refresh" content="0">
    |                                     ^

1 error found.
```

Examples of correct code for this rule:

```
<meta http-equiv="refresh" content="0;url=target.html">
```

## [Options](#options)

This rule takes an optional object:

```
{
  "allowLongDelay": false
}
```

### [allowLongDelay](#allowlongdelay)

- type: `boolean`
- default: `false`

Delays longer than 20 hours is exempt from [WCAG Success Criterion 2.2.1 Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html). By enabling this option the refresh delay can be set to a value greater than `72000`.

With this option disabled:

```
<meta http-equiv="refresh" content="72001">
```

```
error: Meta refresh must be instant (0 second delay) (meta-refresh) at inline:1:37:
> 1 | <meta http-equiv="refresh" content="72001">
    |                                     ^^^^^

1 error found.
```

With this option enabled:

```
<meta http-equiv="refresh" content="72001">
```

## [References](#references)

- [WCAG Success Criterion 2.2.1: Timing Adjustable (A)](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html)
- [WCAG Success Criterion 2.2.4: Interruptions (Level AAA)](https://www.w3.org/WAI/WCAG21/Understanding/interruptions.html)
- [WCAG Success Criterion 3.2.5: Change on Request (Level AAA)](https://www.w3.org/WAI/WCAG21/Understanding/change-on-request)
- [WCAG H76: Using meta refresh to create an instant client-side redirect](https://www.w3.org/WAI/WCAG22/Techniques/html/H76)
- [WCAG G110: Using an instant client-side redirect](https://www.w3.org/WAI/WCAG22/Techniques/general/G110)

## [Version history](#version-history)

- 8.14.0 - `allowLongDelay` option added.
