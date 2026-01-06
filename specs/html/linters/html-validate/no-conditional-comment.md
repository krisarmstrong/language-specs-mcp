## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow usage of conditional comments

Rule ID:no-conditional-commentCategory:DeprecatedStandards:-

Microsoft Internet Explorer previously supported using special HTML comments ([conditional comments](https://msdn.microsoft.com/en-us/library/ms537512(v=vs.85).aspx)) for targeting specific versions of IE but since IE 10 it is deprecated and not supported in standards mode.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!--[if IE]>
<p>You are using Internet Explorer.</p>
<![endif]-->

<![if !IE]>
<p>You are not using Internet Explorer.</p>
<![endif]>
```

```
error: Use of conditional comments are deprecated (no-conditional-comment) at inline:1:1:
> 1 | <!--[if IE]>
    | ^^^^^^^^^^^^
  2 | <p>You are using Internet Explorer.</p>
  3 | <![endif]-->
  4 |

error: Use of conditional comments are deprecated (no-conditional-comment) at inline:3:1:
  1 | <!--[if IE]>
  2 | <p>You are using Internet Explorer.</p>
> 3 | <![endif]-->
    | ^^^^^^^^^^^^
  4 |
  5 | <![if !IE]>
  6 | <p>You are not using Internet Explorer.</p>

error: Use of conditional comments are deprecated (no-conditional-comment) at inline:5:1:
  3 | <![endif]-->
  4 |
> 5 | <![if !IE]>
    | ^^^^^^^^^^^
  6 | <p>You are not using Internet Explorer.</p>
  7 | <![endif]>

error: Use of conditional comments are deprecated (no-conditional-comment) at inline:7:1:
  5 | <![if !IE]>
  6 | <p>You are not using Internet Explorer.</p>
> 7 | <![endif]>
    | ^^^^^^^^^^

4 errors found.
```
