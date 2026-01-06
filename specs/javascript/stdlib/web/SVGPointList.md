# SVGPointList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGPointList&level=high)

The `SVGPointList` interface represents a list of [DOMPoint](/en-US/docs/Web/API/DOMPoint) objects.

An `SVGPointList` can be designated as read-only, which means that attempts to modify the object will result in an exception being thrown.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[SVGPointList.length](/en-US/docs/Web/API/SVGPointList/length)Read only

Returns the number of points in the list.

[SVGPointList.numberOfItems](/en-US/docs/Web/API/SVGPointList/numberOfItems)Read only

Returns the number of points in the list.

## [Instance methods](#instance_methods)

[SVGPointList.clear()](/en-US/docs/Web/API/SVGPointList/clear)

Removes all items in the list.

[SVGPointList.initialize()](/en-US/docs/Web/API/SVGPointList/initialize)

First removes all items in the list, then adds a single value to the list.

[SVGPointList.getItem()](/en-US/docs/Web/API/SVGPointList/getItem)

Gets an item from the list at a specified position.

[SVGPointList.insertItemBefore()](/en-US/docs/Web/API/SVGPointList/insertItemBefore)

Inserts an element into the list at a specified position.

[SVGPointList.replaceItem()](/en-US/docs/Web/API/SVGPointList/replaceItem)

Replaces an item in the list with a new item.

[SVGPointList.removeItem()](/en-US/docs/Web/API/SVGPointList/removeItem)

Removes an item from the list.

[SVGPointList.appendItem()](/en-US/docs/Web/API/SVGPointList/appendItem)

Adds an item to the end of the list.

## [Examples](#examples)

The following example shows an SVG which contains a [<polyline>](/en-US/docs/Web/SVG/Reference/Element/polyline) with five coordinate pairs. The `points` property returns an `SVGPointList`.

html

```
<svg viewBox="-10 -10 120 120" xmlns="http://www.w3.org/2000/svg">
  <polyline
    id="example"
    stroke="black"
    fill="none"
    points="50,0 21,90 98,35 2,35 79,90" />
</svg>
```

js

```
const example = document.getElementById("example");
console.log(example.points); // An SVGPointList
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGPointList](https://svgwg.org/svg2-draft/shapes.html#InterfaceSVGPointList)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGPointList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgpointlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGPointList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgpointlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGPointList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgpointlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F43a8839abdfb01d4388f11a028582bec4e7ead18%0A*+Document+last+modified%3A+2025-06-08T10%3A11%3A23.000Z%0A%0A%3C%2Fdetails%3E)
