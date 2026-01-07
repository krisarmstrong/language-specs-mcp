HTML-validate - Require `id` to be a valid identifier (valid-id)Toggle navigation[HTML-validate v10.5.0](/)

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

# Valid ID

Rule ID:valid-idCategory:HTML syntax and conceptsStandards:

- HTML5

Requires the `id` attribute to be a valid identifier.

Strictly the HTML5 standard defines valid IDs as non-empty and without any whitespace but many other characters can be troublesome when used to create selectors as they require intricate escaping (e.g. `id="123"` becomes `#\\31 23`).

By default, this rule enforces that ID begins with a letter and that only letters, numbers, underscores and dashes are used but this can be disabled with the "relaxed" option to only validate the strict definition from the standard.

See also the related [id-pattern](id-pattern.html) rule which can be used for applying a consistent style to the codebase (by for instance requiring only dashes instead of underscores as separators)

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<p id=""></p>
<p id="foo bar"></p>
<p id="123"></p>
```

```
error: element id "" must not be empty (valid-id) at inline:1:4:
> 1 | <p id=""></p>
    |    ^^^^^
  2 | <p id="foo bar"></p>
  3 | <p id="123"></p>

error: element id "foo bar" must not contain whitespace (valid-id) at inline:2:8:
  1 | <p id=""></p>
> 2 | <p id="foo bar"></p>
    |        ^^^^^^^
  3 | <p id="123"></p>

error: element id "123" must begin with a letter (valid-id) at inline:3:8:
  1 | <p id=""></p>
  2 | <p id="foo bar"></p>
> 3 | <p id="123"></p>
    |        ^^^

3 errors found.
```

Examples of correct code for this rule:

```
<p id="foo-123"></p>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "relaxed": false
}
```

### [relaxed](#relaxed)

When set to `true` this rule only validates the ID is non-empty and contains no whitespace.

```
<p id="123"></p>
<p id="#foo[bar]"></p>
```

## [Version history](#version-history)

- 8.19.0 - Handles unicode letters.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/valid-id.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/valid-id.ts)
