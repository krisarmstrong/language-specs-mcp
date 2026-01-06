## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require CSP nonce for resources

Rule ID:require-csp-nonceCategory:SecurityStandards:

- Content Security Policy

Requires that a [Content-Security-Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) nonce is present on elements required by the policy.

The CSP nonce is a cryptography secure random token and must match the `Content-Security-Policy` header for the given resource. The token should be unique per request and should not be guessable by an attacker. It is used to prevent cross site scripting (XSS) by preventing malicious actors from injecting scripts into the page.

`Content-Security-Policy: script-src 'nonce-r4nd0m'`

Given the above header all inline `<script>` elements must contain the `nonce="r4nd0m"` attribute (see examples below).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<script>
	doFancyStuff();
</script>
```

```
error: required CSP nonce is missing (require-csp-nonce) at inline:1:2:
> 1 | <script>
    |  ^^^^^^
  2 | 	doFancyStuff();
  3 | </script>

1 error found.
```

Examples of correct code for this rule:

```
<script nonce="r4nd0m">
	doFancyStuff();
</script>
```

## [When to use](#when-to-use)

If you use nonces in your CSP policies you should use this rule to ensure nonces are present on the elements.

If you dont use nonces or CSP you should not use this rule.

## [Options](#options)

This rule takes an optional object:

```
{
  "tags": ["script", "style"]
}
```

### [tags](#tags)

List of elements to check for the `nonce` attribute.

Limited to:

- `script` (when `src` attribute is not present)
- `style`

## [Version history](#version-history)

- 7.1.0 - rule added
