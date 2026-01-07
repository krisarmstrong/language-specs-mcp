HTML-validate - Disallow link types (allowed-links)Toggle navigation[HTML-validate v10.5.0](/)

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

# Disallows link types

Rule ID:allowed-linksCategory:DocumentStandards:-

This rules checks the link destination and disallows certain categories of links:

- External links
- Relative paths
- Relative to document base url

The rule checks links from:

- `<a href=""></a>`
- `<img src="..">`
- `<link src="..">`
- `<script src=".."></script>`

Anchor links are ignored by this rule.

## [Rule details](#rule-details)

This rules requires additional configuration to yield errors. By default all links are allowed even when this rule is enabled.

## [Options](#options)

This rule takes an optional object:

```
{
  "allowExternal": true,
  "allowRelative": true,
  "allowAbsolute": true,
  "allowBase": true
}
```

### [allowExternal](#allowexternal)

By setting `allowExternal` to `false` any link to a external resource will be disallowed. This can also be set to an object (see below regarding `include` and `exclude` lists).

```
<a href="http://example.net/foo">
```

```
error: Link destination must not be external url (allowed-links) at inline:1:10:
> 1 | <a href="http://example.net/foo">
    |          ^^^^^^^^^^^^^^^^^^^^^^

1 error found.
```

```
<a href="./foo">
```

### [allowRelative](#allowrelative)

By setting `allowRelative` to `false` any link with a relative url will be disallowed. This can also be set to an object (see below regarding `include` and `exclude` lists).

```
<a href="../foo">
```

```
error: Link destination must not be relative url (allowed-links) at inline:1:10:
> 1 | <a href="../foo">
    |          ^^^^^^

1 error found.
```

```
<a href="/foo">
```

### [allowAbsolute](#allowabsolute)

By setting `allowAbsolute` to `false` any link with a absolute url will be disallowed. This can also be set to an object (see below regarding `include` and `exclude` lists).

```
<a href="/foo">
```

```
error: Link destination must not be absolute url (allowed-links) at inline:1:10:
> 1 | <a href="/foo">
    |          ^^^^

1 error found.
```

```
<a href="../foo">
```

### [allowBase](#allowbase)

By setting `allowBase` to `false` relative urls can be used only if using an explicit path but not when relative to document base url. This is useful when wanting to use relative urls but not rely on `<base href="..">` being set correctly.

Effectively this also means that links to files in the same folder must use `./target` even if `target` is valid.

```
<a href="foo">
```

```
error: Relative links must be relative to current folder (allowed-links) at inline:1:10:
> 1 | <a href="foo">
    |          ^^^

1 error found.
```

```
<a href="./foo">
```

### [Using include and exclude](#using-include-and-exclude)

In addition to a boolean value `allowExternal`, `allowRelative` and `allowAbsolute` can also be set to an object with the `include` and `exclude` properties for a more fine-grained control of what link destinations should be considered valid. Each property is a list of regular expressions matched against the link destination.

- When `include` is set each link must match at least one entry to be valid.
- When `exclude` is set each link must not match any entries to be valid.
- The two properties are not mutually exclusive, both can be enabled at the same time.

For instance, `allowExternal.include` can be used to set a whitelist of valid external links while disallowing all others. In this case external links to `foo.example.net` is valid but any other would yield an error:

```
{
  "allowExternal": {
    "include": ["^//foo.example.net"]
  }
}
```

```
<!-- allowed -->
<a href="//foo.example.net">

<!-- not allowed -->
<a href="//bar.example.net">
```

```
error: External link to this destination is not allowed by current configuration (allowed-links) at inline:5:10:
  3 |
  4 | <!-- not allowed -->
> 5 | <a href="//bar.example.net">
    |          ^^^^^^^^^^^^^^^^^

1 error found.
```

## [Version history](#version-history)

- 6.1.0 - Added support for `include` and `exclude`.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/allowed-links.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/allowed-links.ts)
