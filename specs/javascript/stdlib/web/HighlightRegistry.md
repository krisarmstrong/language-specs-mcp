# HighlightRegistry

 Baseline  2025  * Newly available

 Since ⁨June 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHighlightRegistry&level=low)

The `HighlightRegistry` interface of the [CSS Custom Highlight API](/en-US/docs/Web/API/CSS_Custom_Highlight_API) is used to register [Highlight](/en-US/docs/Web/API/Highlight) objects to be styled using the API. It is accessed via [CSS.highlights](/en-US/docs/Web/API/CSS/highlights_static).

A `HighlightRegistry` instance is a [Map-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis), in which each key is the name string for a custom highlight, and the corresponding value is the associated [Highlight](/en-US/docs/Web/API/Highlight) object.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `HighlightRegistry` interface doesn't inherit any properties.

[HighlightRegistry.size](/en-US/docs/Web/API/HighlightRegistry/size)Read only

Returns the number of `Highlight` objects currently registered.

## [Instance methods](#instance_methods)

The `HighlightRegistry` interface doesn't inherit any methods.

[HighlightRegistry.clear()](/en-US/docs/Web/API/HighlightRegistry/clear)

Remove all `Highlight` objects from the registry.

[HighlightRegistry.delete()](/en-US/docs/Web/API/HighlightRegistry/delete)

Remove the named `Highlight` object from the registry.

[HighlightRegistry.entries()](/en-US/docs/Web/API/HighlightRegistry/entries)

Returns a new iterator object that contains each `Highlight` object in the registry, in insertion order.

[HighlightRegistry.forEach()](/en-US/docs/Web/API/HighlightRegistry/forEach)

Calls the given callback once for each `Highlight` object in the registry, in insertion order.

[HighlightRegistry.get()](/en-US/docs/Web/API/HighlightRegistry/get)

Gets the named `Highlight` object from the registry.

[HighlightRegistry.has()](/en-US/docs/Web/API/HighlightRegistry/has)

Returns a boolean asserting whether a `Highlight` object is present the registry or not.

[HighlightRegistry.highlightsFromPoint()](/en-US/docs/Web/API/HighlightRegistry/highlightsFromPoint)Experimental

Returns an array of objects representing the custom highlights applied at a specific point within the viewport.

[HighlightRegistry.keys()](/en-US/docs/Web/API/HighlightRegistry/keys)

An alias for [HighlightRegistry.values()](/en-US/docs/Web/API/HighlightRegistry/values).

[HighlightRegistry.set()](/en-US/docs/Web/API/HighlightRegistry/set)

Adds the given `Highlight` object to the registry with the given name, or updates the named `Highlight` object, if it already exists in the registry.

[HighlightRegistry.values()](/en-US/docs/Web/API/HighlightRegistry/values)

Returns a new iterator object that yields the `Highlight` objects in the registry, in insertion order.

## [Examples](#examples)

### [Registering a highlight](#registering_a_highlight)

The following example demonstrates how to create ranges, instantiate a new `Highlight` object for them, and register the highlight using the `HighlightRegistry`, to style it on the page:

#### HTML

html

```
<p id="foo">CSS Custom Highlight API</p>
```

#### CSS

css

```
::highlight(my-custom-highlight) {
  background-color: peachpuff;
}
```

#### JavaScript

js

```
const text = document.getElementById("foo").firstChild;

if (!CSS.highlights) {
  text.textContent =
    "The CSS Custom Highlight API is not supported in this browser!";
}

// Create a couple of ranges.
const range1 = new Range();
range1.setStart(text, 0);
range1.setEnd(text, 3);

const range2 = new Range();
range2.setStart(text, 21);
range2.setEnd(text, 24);

// Create a custom highlight for these ranges.
const highlight = new Highlight(range1, range2);

// Register the ranges in the HighlightRegistry.
CSS.highlights.set("my-custom-highlight", highlight);
```

#### Result

## [Specifications](#specifications)

Specification
[CSS Custom Highlight API Module Level 1# highlight-registry](https://drafts.csswg.org/css-highlight-api/#highlight-registry)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The CSS Custom Highlight API](/en-US/docs/Web/API/CSS_Custom_Highlight_API)
- [CSS custom highlight API](/en-US/docs/Web/CSS/Guides/Custom_highlight_API) module
- [CSS Custom Highlight API: The Future of Highlighting Text Ranges on the Web](https://css-tricks.com/css-custom-highlight-api-early-look/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HighlightRegistry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/highlightregistry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHighlightRegistry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhighlightregistry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHighlightRegistry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhighlightregistry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
