## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require SRI for resources

Rule ID:require-sriCategory:SecurityStandards:

- Subresource Integrity

Subresource Integrity (SRI) is a security feature that enables browsers to verify that resources they fetch are delivered without unexpected manipulation.

Commonly needed when using Content Delivery Networks (CDN).

This rules requires the usage of the `integrity` attribute to provide the cryptographic hash for SRI to function.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<script src="//cdn.example.net/jquery.min.js"></script>
```

```
error: SRI "integrity" attribute is required on <script> element (require-sri) at inline:1:2:
> 1 | <script src="//cdn.example.net/jquery.min.js"></script>
    |  ^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<script src="//cdn.example.net/jquery.min.js" integrity="sha384-..."></script>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "target": "all",
  "include": null,
  "exclude": null
}
```

### [target](#target)

- `all` require integrity for all resources, even on same origin.
- `crossorigin` requires integrity for all crossdomain resources.

With `target` set to `crossorigin` only requests to other domains need SRI. Note that the logic for determining crossdomain is a bit naïve, resources with a full url (`protocol://`) or implicit protocol (`//`) counts as crossorigin even if it technically would point to the same origin.

```
<!--- local resource -->
<link rel="stylesheet" href="local.css">

<!-- resource loaded over CDN -->
<link rel="stylesheet" href="//cdn.example.net/remote.css">
```

```
error: SRI "integrity" attribute is required on <link> element (require-sri) at inline:5:2:
  3 |
  4 | <!-- resource loaded over CDN -->
> 5 | <link rel="stylesheet" href="//cdn.example.net/remote.css">
    |  ^^^^

1 error found.
```

### [include](#include)

- type: `string[] | null`

If set only URLs matching one or more patterns in this array yields errors. Patterns are matched as substrings.

For instance, with the following configuration only the first URL yields an error:

```
{
  "include": ["//cdn.example.net/"]
}
```

```
<!-- matches included pattern, yields error -->
<link rel="stylesheet" href="//cdn.example.net/remote.css" />
<!-- doesn't match, no error -->
<link rel="stylesheet" href="//static-assets.example.org/remote.css" />
```

```
error: SRI "integrity" attribute is required on <link> element (require-sri) at inline:2:2:
  1 | <!-- matches included pattern, yields error -->
> 2 | <link rel="stylesheet" href="//cdn.example.net/remote.css" />
    |  ^^^^
  3 | <!-- doesn't match, no error -->
  4 | <link rel="stylesheet" href="//static-assets.example.org/remote.css" />

1 error found.
```

### [exclude](#exclude)

- type: `string[] | null`

If set URLs matching one or more pattern in this array is ignored. Patterns are matched as substrings.

For instance, with the following configuration only the second URL yields an error:

```
{
  "exclude": ["//cdn.example.net/"]
}
```

```
<!-- doesn't match excluded pattern, yields error -->
<link rel="stylesheet" href="//cdn.example.net/remote.css">
<!-- matches excluded pattern, no error -->
<link rel="stylesheet" href="//static-assets.example.org/remote.css">
```

```
error: SRI "integrity" attribute is required on <link> element (require-sri) at inline:4:2:
  2 | <link rel="stylesheet" href="//cdn.example.net/remote.css">
  3 | <!-- matches excluded pattern, no error -->
> 4 | <link rel="stylesheet" href="//static-assets.example.org/remote.css">
    |  ^^^^

1 error found.
```

## [Version history](#version-history)

- 9.2.1 - only tests `<link>` with `rel` set to one of `stylesheet`, `preload` or `modulepreload`.
- 7.1.0 - `include` and `exclude` options added
