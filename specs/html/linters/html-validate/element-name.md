HTML-validate - Disallow invalid element names (element-name)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallow invalid element names

Rule ID:element-nameCategory:HTML syntax and conceptsStandards:

- HTML5

HTML defines what content is considered a valid (custom) [element
name](https://www.w3.org/TR/custom-elements/#valid-custom-element-name), essentially:

- Must start with `a-z`.
- Must contain a dash `-`.

Elements with xml namespaces is ignored by this rule.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<foobar></foobar>
```

```
error: <foobar> is not a valid element name (element-name) at inline:1:2:
> 1 | <foobar></foobar>
    |  ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<div></div>
<foo-bar></foo-bar>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "pattern": "[a-z][a-z0-9\\-._]*-[a-z0-9\\-._]*$",
  "whitelist": [],
  "blacklist": []
}
```

### [Pattern](#pattern)

A regular expression for matching valid names. If changed you should ensure it still fulfills the original HTML specification, in particular requiring a `-`.

### [Whitelist](#whitelist)

Elements in the whitelist will never trigger this rule even if it would not match the pattern.

### [Blacklist](#blacklist)

Elements in the blacklist will always trigger this rule.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/element-name.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/element-name.ts)
