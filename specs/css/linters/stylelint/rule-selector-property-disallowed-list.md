On this page

# rule-selector-property-disallowed-list

Specify a list of disallowed properties for selectors within rules.

```
    a { color: red; }
/** ↑   ↑
 * Selector and property name */
```

## Options[​](#options)

### `Object<string, Array<string>>`[​](#objectstring-arraystring)

```
{ "selector": ["array", "of", "properties", "/regex/"] }
```

You can specify a regex for a selector, such as `{ "/foo-/": [] }`.

Given:

```
{
  "rule-selector-property-disallowed-list": {
    "a": ["color", "/margin/"],
    "/foo/": ["/size/"]
  }
}
```

The following patterns are considered problems:

```
a { color: red; }
```

```
a { margin-top: 0px; }
```

```
html[data-foo] { font-size: 1px; }
```

The following patterns are not considered problems:

```
a { background: red; }
```

```
a { padding-top: 0px; }
```

```
html[data-foo] { color: red; }
```

## Optional secondary options[​](#optional-secondary-options)

### `ignore`[​](#ignore)

```
{ "ignore": ["array", "of", "options"] }
```

#### `"keyframe-selectors"`[​](#keyframe-selectors)

Ignore keyframe selectors.

Given:

```
{
  "rule-selector-property-disallowed-list": [
    { "/^[a-z]+$/": ["opacity"] },
    { "ignore": ["keyframe-selectors"] }
  ]
}
```

The following pattern is not considered a problem:

```
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

[Previousrule-nesting-at-rule-required-list](/user-guide/rules/rule-nesting-at-rule-required-list)[Nextselector-anb-no-unmatchable](/user-guide/rules/selector-anb-no-unmatchable)

- [Options](#options)

  - [Object<string, Array<string>>](#objectstring-arraystring)

- [Optional secondary options](#optional-secondary-options)

  - [ignore](#ignore)
