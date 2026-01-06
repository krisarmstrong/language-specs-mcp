## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Prefer to use native HTML element over roles

Rule ID:prefer-native-elementCategory:AccessibilityStandards:

- ARIA in HTML

While WAI-ARIA describes many [roles](https://www.w3.org/TR/wai-aria-1.1/#role_definitions) which can provide semantic information about what the element represents. Support for roles is varying and since HTML5 has many native equivalent elements it is better to use the native when possible.

Table of equivalent elements:

RoleElementarticlearticlebannerheaderbuttonbuttoncelltdcheckboxinputcomplementaryasidecontentinfofooterfigurefigureformformheadingh1, h2, h3, h4, h5, h6inputinputlinkalistul, ollistboxselectlistitemlimainmainnavigationnavprogressbarprogressradioinputregionsectiontabletabletextboxtextarea

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<div role="main">
  <p>Lorem ipsum</p>
</div>
```

```
error: Prefer to use the native <main> element (prefer-native-element) at inline:1:6:
> 1 | <div role="main">
    |      ^^^^^^^^^^^
  2 |   <p>Lorem ipsum</p>
  3 | </div>

1 error found.
```

Examples of correct code for this rule:

```
<main>
  <p>Lorem ipsum</p>
</main>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "mapping": {
    /* ... */
  },
  "include": [],
  "exclude": [],
}
```

### [mapping](#mapping)

Object with roles to map to native elements. This can be used to provide a custom map with roles and their replacement.

### [include](#include)

If set only roles listed in this array generates errors.

### [exclude](#exclude)

If set roles listed in this array is ignored.
