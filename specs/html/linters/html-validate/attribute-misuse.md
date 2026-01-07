HTML-validate - Require attribute to be used in correct context (attribute-misuse)Toggle navigation[HTML-validate v10.5.0](/)

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

# Require attribute to be used in correct context

Rule ID:attribute-misuseCategory:Content modelStandards:

- HTML5

Some attributes have usage requirements, for instance:

- `<a target>` requires the `href` attribute.
- `<button formaction>` requires `type="submit"`.
- `<meta content>` requires one of the `name`, `http-equiv` or `itemprop` attributes.
- `<meta>` can only contain one of the `name`, `http-equiv` or `itemprop` attributes.
- `<meta name>` requires the `content` attribute.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<a target="_blank">
<button type="button" formaction="post">
<meta name=".." http-equiv="..">
```

```
error: "target" attribute cannot be used on <a> in this context: requires "href" attribute to be present (attribute-misuse) at inline:1:4:
> 1 | <a target="_blank">
    |    ^^^^^^
  2 | <button type="button" formaction="post">
  3 | <meta name=".." http-equiv="..">

error: "formaction" attribute cannot be used on <button> in this context: "type" attribute must be "submit" (attribute-misuse) at inline:2:23:
  1 | <a target="_blank">
> 2 | <button type="button" formaction="post">
    |                       ^^^^^^^^^^
  3 | <meta name=".." http-equiv="..">

error: "name" attribute cannot be used on <meta> in this context: cannot be used at the same time as "http-equiv" (attribute-misuse) at inline:3:7:
  1 | <a target="_blank">
  2 | <button type="button" formaction="post">
> 3 | <meta name=".." http-equiv="..">
    |       ^^^^

error: "http-equiv" attribute cannot be used on <meta> in this context: cannot be used at the same time as "name" (attribute-misuse) at inline:3:17:
  1 | <a target="_blank">
  2 | <button type="button" formaction="post">
> 3 | <meta name=".." http-equiv="..">
    |                 ^^^^^^^^^^

4 errors found.
```

Examples of correct code for this rule:

```
<a href=".." target="_blank">
<button type="submit" formaction="post">
<meta name=".." content="..">
<meta http-equiv=".." content="..">
```

## [Version history](#version-history)

- 7.7.0 - Rule added.

[Edit this page](https://gitlab.com/html-validate/html-validate/edit/master/docs/rules/attribute-misuse.md)[View rule source](https://gitlab.com/html-validate/html-validate/blob/master/src/rules/attribute-misuse.ts)
