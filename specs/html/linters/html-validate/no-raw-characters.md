## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow the use of unescaped special characters

Rule ID:no-raw-charactersCategory:HTML syntax and conceptsStandards:

- HTML5

Some characters hold special meaning in HTML and must be escaped using character references (html entities) to be used as plain text:

- `<` (U+003C) must be escaped using `<`
- `>` (U+003E) must be escaped using `>`
- `&` (U+0026) must be escaped using `&`

Additionally, unquoted attribute values further restricts the allowed characters:

- `"` (U+0022) must be escaped using `"`
- `'` (U+0027) must be escaped using `'`
- `=` (U+003D) must be escaped using `&quals;`
- ``` (U+0060) must be escaped using ```

Quotes attributes must escape only the following characters:

- `"` (U+0022) must be escaped using `"` if attribute is quoted using `"`
- `'` (U+0027) must be escaped using `'` if attribute is quoted using `'`

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p>Fred & Barney</p>
<p class=foo's></p>
```

```
error: Raw "&" must be encoded as "&amp;" (no-raw-characters) at inline:1:9:
> 1 | <p>Fred & Barney</p>
    |         ^
  2 | <p class=foo's></p>

error: Raw "'" must be encoded as "&apos;" (no-raw-characters) at inline:2:13:
  1 | <p>Fred & Barney</p>
> 2 | <p class=foo's></p>
    |             ^

2 errors found.
```

Examples of correct code for this rule:

```
<p>Fred &amp; Barney</p>
<p class=foo&apos;s></p>
<p class="'foo'"></p>
```

## [Parser](#parser)

Note that documents using unescaped `<` might not parse properly due to the strict parsing of HTML-validate. This is intentional.

For instance, in the following case `<3` is misinterpreted as a tag `<3>` followed by a boolean attribute `Barney`.

```
<p>Fred <3 Barney</p>
```

```
error: failed to tokenize "</p>", expected attribute, ">" or "/>" (parser-error) at inline:1:18:
> 1 | <p>Fred <3 Barney</p>
    |                  ^

1 error found.
```

## [Options](#options)

This rule takes an optional object:

```
{
  "relaxed": false
}
```

### [relaxed](#relaxed)

HTML5 introduces the concept of [ambiguous ampersands](https://html.spec.whatwg.org/multipage/syntax.html#syntax-ambiguous-ampersand) and relaxes the rules slightly. Using this options ampersands (`&`) only needs to be escaped if the context is ambiguous (applies to both text nodes and attribute values).

This is disabled by default as explicit encoding is easier for readers than implicitly having to figure out if encoding is needed or not.

Examples of correct code with this option:

```
<!-- Not ambiguous: & is followed by whitespace -->
<p>Fred & Barney</p>

<!-- Not ambiguous: &Barney is not terminated by ; -->
<p>Fred&Barney</p>

<!-- Not ambiguous: = and " both stops the character reference -->
<a href="?foo&bar=1&baz"></p>

<!-- Not ambiguous: even unquoted & is understood to be stopped by > -->
<a href=?foo&bar></p>
```
