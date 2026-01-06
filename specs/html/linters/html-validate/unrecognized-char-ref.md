## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow unrecognized character references

Rule ID:unrecognized-char-refCategory:HTML syntax and conceptsStandards:

- HTML5

HTML5 defines a set of [named character references](https://html.spec.whatwg.org/multipage/named-characters.html) (sometimes called HTML entities) which can be used as `&name;` where `name` is the entity name, e.g. `'` (`'`) or `&` (`&`). Only entities from the list can be used. Each entity is case sensitive but some entities is defined in multiple casing variants, e.g. both `©` and `©` are acceptable.

This rule ignores numerical entities such as `—` or `—`.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p>&foobar;</p>
```

```
error: Unrecognized character reference "&foobar;" (unrecognized-char-ref) at inline:1:4:
> 1 | <p>&foobar;</p>
    |    ^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<p>&amp;</p>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "ignoreCase": false,
  "requireSemicolon": true
}
```

### [ignoreCase](#ignorecase)

If set to `true` this rule ignores the casing of the entity.

With this option disabled the following is incorrect:

```
<p>&Amp;</p>
```

```
error: Unrecognized character reference "&Amp;" (unrecognized-char-ref) at inline:1:4:
> 1 | <p>&Amp;</p>
    |    ^^^^^

1 error found.
```

With this option enabled the following is correct:

```
<p>&Amp;</p>
```

### [requireSemicolon](#requiresemicolon)

By default named character references are terminated by a semicolon (`;`) but for legacy compatibility some are listed without.

If set to `false` legacy variants without semicolon are allowed.

With this option enabled the following is incorrect:

```
<p>&copy</p>
```

```
error: Character reference "&copy" must be terminated by a semicolon (unrecognized-char-ref) at inline:1:4:
> 1 | <p>&copy</p>
    |    ^^^^^

1 error found.
```

With this option disabled the following is correct:

```
<p>&copy</p>
```

Attribute values with a `?` is treated as a querystring and unless terminated with a `;` is considered to be a parameter and not a character reference, e.g. the following is always valid even if `&bar` looks like a reference without semicolon to terminate it:

```
<a href="foo.php?foo=1&bar=2">...</a>
```

## [Version history](#version-history)

- 7.9.0 - Rule was made case sensitive and the `ignoreCase` and `requireSemicolon` options was added.
