## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require alternative text on `<area>` elements

Rule ID:area-altCategory:AccessibilityStandards:

- WCAG 2.2 (A)
- WCAG 2.1 (A)
- WCAG 2.0 (A)

The `alt` attribute is used to provide an alternative text describing the area in the image map. It is used both by the browser when the `<img>` source is missing but most of all it is used by screen readers and is a required technique for [WCAG H24](https://www.w3.org/WAI/WCAG22/Techniques/html/H24).

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<img src="image.png" usemap="#imagemap" alt="An awesome image">
<map name="imagemap">
	<area href="target1.html">
	<area alt="Link purpose">
</map>
```

```
error: "alt" attribute must be set and non-empty when the "href" attribute is present (area-alt) at inline:3:8:
  1 | <img src="image.png" usemap="#imagemap" alt="An awesome image">
  2 | <map name="imagemap">
> 3 | 	<area href="target1.html">
    | 	      ^^^^
  4 | 	<area alt="Link purpose">
  5 | </map>

error: "alt" attribute cannot be used unless the "href" attribute is present (area-alt) at inline:4:8:
  2 | <map name="imagemap">
  3 | 	<area href="target1.html">
> 4 | 	<area alt="Link purpose">
    | 	      ^^^
  5 | </map>

2 errors found.
```

Examples of correct code for this rule:

```
<img src="image.png" usemap="#imagemap" alt="An awesome image">
<map name="imagemap">
	<area href="target1.html" alt="Link purpose">
	<area href="target2.html" alt="Link purpose">
</map>
```

## [Options](#options)

This rule takes an optional object:

```
{
  "accessible": true
}
```

### [accessible](#accessible)

The HTML5 standard allows only a single `<area>` element to contain alternative text when a group of `<area>` references the same resource. WCAG requires all of them to be labeled even if referencing the same resource. This is because HTML only considers the case when the image is missing and uses an algorithm to remove duplicated links pointing to the same resource, thus only requiring a single `<area>` for each resource to contain the `alt` text. As for screen readers and accessibility each of the `<area>` elements could be read by the user and thus each of them must be adequate labeled.

This option is enabled by default by the `html-validate:recommended` and `html-validate:a11y` presets but disabled by the `html-validate:standard` preset.

With this option enabled the following is incorrect:

```
<img src="image.png" usemap="#imagemap" alt="An awesome image">
<map name="imagemap">
	<area href="target.html" alt="">
	<area href="target.html" alt="Link purpose">
</map>
```

```
error: "alt" attribute must be set and non-empty when the "href" attribute is present (area-alt) at inline:3:27:
  1 | <img src="image.png" usemap="#imagemap" alt="An awesome image">
  2 | <map name="imagemap">
> 3 | 	<area href="target.html" alt="">
    | 	                         ^^^
  4 | 	<area href="target.html" alt="Link purpose">
  5 | </map>

1 error found.
```

With this option disabled the following is correct:

```
<img src="image.png" usemap="#imagemap" alt="An awesome image">
<map name="imagemap">
	<area href="target.html" alt="">
	<area href="target.html" alt="Link purpose">
</map>
```

## [Version history](#version-history)

- 7.7.0 - Rule added.
