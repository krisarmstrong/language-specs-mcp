# Highlight

 Baseline  2025 Newly available

 Since ⁨June 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHighlight&level=low)

The `Highlight` interface of the [CSS Custom Highlight API](/en-US/docs/Web/API/CSS_Custom_Highlight_API) is used to represent a collection of [Range](/en-US/docs/Web/API/Range) instances to be styled using the API.

To style arbitrary ranges in a page, instantiate a new `Highlight` object, add one or more `Range` objects to it, and register it using the [HighlightRegistry](/en-US/docs/Web/API/HighlightRegistry).

A `Highlight` instance is a [Set-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) that can hold one or more `Range` objects.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Highlight()](/en-US/docs/Web/API/Highlight/Highlight)

Returns a newly created `Highlight` object.

## [Instance properties](#instance_properties)

The `Highlight` interface doesn't inherit any properties.

[Highlight.priority](/en-US/docs/Web/API/Highlight/priority)

A number that indicates the priority of this `Highlight` object. When multiple highlights overlap, the browser uses this priority to decide how to style the overlapping parts.

[Highlight.size](/en-US/docs/Web/API/Highlight/size)Read only

Returns the number of ranges in the `Highlight` object.

[Highlight.type](/en-US/docs/Web/API/Highlight/type)

An enumerated [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) used to specify the semantic meaning of the highlight. This allows assistive technologies to include this meaning when exposing the highlight to users.

## [Instance methods](#instance_methods)

The `Highlight` interface doesn't inherit any methods.

[Highlight.add()](/en-US/docs/Web/API/Highlight/add)

Add a new range to this highlight.

[Highlight.clear()](/en-US/docs/Web/API/Highlight/clear)

Remove all ranges from this highlight.

[Highlight.delete()](/en-US/docs/Web/API/Highlight/delete)

Remove a range from this highlight.

[Highlight.entries()](/en-US/docs/Web/API/Highlight/entries)

Returns a new iterator object that contains each range in the highlight object, in insertion order.

[Highlight.forEach()](/en-US/docs/Web/API/Highlight/forEach)

Calls the given callback once for each range in the highlight object, in insertion order.

[Highlight.has()](/en-US/docs/Web/API/Highlight/has)

Returns a boolean asserting whether a range is present the highlight object or not.

[Highlight.keys()](/en-US/docs/Web/API/Highlight/keys)

An alias for [Highlight.values()](/en-US/docs/Web/API/Highlight/values).

[Highlight.values()](/en-US/docs/Web/API/Highlight/values)

Returns a new iterator object that yields the ranges in the highlight object in insertion order.

## [Examples](#examples)

The following example demonstrates how specific parts of a block of text can be highlighted.

html

```
<p class="foo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem
  sapiente non eum facere? Nam rem hic culpa, ipsa rerum ab itaque consectetur
  molestiae dolores vitae! Quo ex explicabo tempore? Tenetur.</p>
```

This JavaScript code creates [ranges](/en-US/docs/Web/API/Range), instantiates a new `Highlight` object for them, and [registers it](/en-US/docs/Web/API/HighlightRegistry/set) to be styled on the page:

js

```
const parentNode = document.querySelector(".foo");
const textNode = parentNode.firstChild;

// Create a couple of ranges.
const range1 = new Range();
range1.setStart(textNode, 6);
range1.setEnd(textNode, 21);

const range2 = new Range();
range2.setStart(textNode, 57);
range2.setEnd(textNode, 71);

// Create a custom highlight for these ranges.
const highlight = new Highlight(range1, range2);

// Register the ranges in the HighlightRegistry.
CSS.highlights.set("my-custom-highlight", highlight);
```

The following CSS code snippet demonstrates how to style the registered custom highlight by using the [::highlight](/en-US/docs/Web/CSS/Reference/Selectors/::highlight) pseudo-element:

css

```
::highlight(my-custom-highlight) {
  background-color: peachpuff;
}
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[CSS Custom Highlight API Module Level 1# highlight](https://drafts.csswg.org/css-highlight-api/#highlight)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The CSS Custom Highlight API](/en-US/docs/Web/API/CSS_Custom_Highlight_API)
- [CSS custom highlight API](/en-US/docs/Web/CSS/Guides/Custom_highlight_API) module
- [CSS Custom Highlight API: The Future of Highlighting Text Ranges on the Web](https://css-tricks.com/css-custom-highlight-api-early-look/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Highlight/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/highlight/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHighlight&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhighlight%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHighlight%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhighlight%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
