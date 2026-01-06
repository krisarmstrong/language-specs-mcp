## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require usage of "html" doctype

Rule ID:doctype-htmlCategory:DocumentStandards:

- HTML5

HTML5 requires the usage of the `<!DOCTYPE html>` doctype to prevent browsers from guessing and/or using "quirks mode".

HTML5 also supports legacy strings for document generators but this rule disallows legacy strings as well.

This rule only validates the doctype itself not the presence of the declaration. Use [missing-doctype](missing-doctype.html) to validate presence.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

```
error: doctype should be "html" (doctype-html) at inline:1:11:
> 1 | <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 error found.
```

```
<!DOCTYPE html SYSTEM "about:legacy-compat">
```

```
error: doctype should be "html" (doctype-html) at inline:1:11:
> 1 | <!DOCTYPE html SYSTEM "about:legacy-compat">
    |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 error found.
```

Examples of correct code for this rule:

```
<!DOCTYPE html>
```
