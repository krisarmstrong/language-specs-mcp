# Range

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRange&level=high)

The `Range` interface represents a fragment of a document that can contain nodes and parts of text nodes.

A range can be created by using the [Document.createRange()](/en-US/docs/Web/API/Document/createRange) method. Range objects can also be retrieved by using the [getRangeAt()](/en-US/docs/Web/API/Selection/getRangeAt) method of the [Selection](/en-US/docs/Web/API/Selection) object or the [caretRangeFromPoint()](/en-US/docs/Web/API/Document/caretRangeFromPoint) method of the [Document](/en-US/docs/Web/API/Document) object.

There also is the [Range()](/en-US/docs/Web/API/Range/Range) constructor available.

## In this article

- [Instance properties](#instance_properties)
- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

There are no inherited properties.

[Range.collapsed](/en-US/docs/Web/API/Range/collapsed)Read only

Returns a boolean value indicating whether the range's start and end points are at the same position.

[Range.commonAncestorContainer](/en-US/docs/Web/API/Range/commonAncestorContainer)Read only

Returns the deepest [Node](/en-US/docs/Web/API/Node) that contains the `startContainer` and `endContainer` nodes.

[Range.endContainer](/en-US/docs/Web/API/Range/endContainer)Read only

Returns the [Node](/en-US/docs/Web/API/Node) within which the `Range` ends.

[Range.endOffset](/en-US/docs/Web/API/Range/endOffset)Read only

Returns a number representing where in the `endContainer` the `Range` ends.

[Range.startContainer](/en-US/docs/Web/API/Range/startContainer)Read only

Returns the [Node](/en-US/docs/Web/API/Node) within which the `Range` starts.

[Range.startOffset](/en-US/docs/Web/API/Range/startOffset)Read only

Returns a number representing where in the `startContainer` the `Range` starts.

## [Constructor](#constructor)

[Range()](/en-US/docs/Web/API/Range/Range)

Returns a `Range` object with the global [Document](/en-US/docs/Web/API/Document) as its start and end.

## [Instance methods](#instance_methods)

There are no inherited methods.

[Range.collapse()](/en-US/docs/Web/API/Range/collapse)

Collapses the `Range` to one of its boundary points.

[Range.compareBoundaryPoints()](/en-US/docs/Web/API/Range/compareBoundaryPoints)

Compares the boundary points of the `Range` with another `Range`.

[Range.compareNode()](/en-US/docs/Web/API/Range/compareNode)DeprecatedNon-standard

Returns a constant representing whether the [Node](/en-US/docs/Web/API/Node) is before, after, inside, or surrounding the range.

[Range.comparePoint()](/en-US/docs/Web/API/Range/comparePoint)

Returns -1, 0, or 1 indicating whether the point occurs before, inside, or after the `Range`.

[Range.cloneContents()](/en-US/docs/Web/API/Range/cloneContents)

Returns a [DocumentFragment](/en-US/docs/Web/API/DocumentFragment) copying the nodes of a `Range`.

[Range.cloneRange()](/en-US/docs/Web/API/Range/cloneRange)

Returns a `Range` object with boundary points identical to the cloned `Range`.

[Range.createContextualFragment()](/en-US/docs/Web/API/Range/createContextualFragment)

Returns a [DocumentFragment](/en-US/docs/Web/API/DocumentFragment) created from a given string of code.

[Range.deleteContents()](/en-US/docs/Web/API/Range/deleteContents)

Removes the contents of a `Range` from the [Document](/en-US/docs/Web/API/Document).

[Range.detach()](/en-US/docs/Web/API/Range/detach)

Does nothing. Kept for compatibility.

[Range.extractContents()](/en-US/docs/Web/API/Range/extractContents)

Moves contents of a `Range` from the document tree into a [DocumentFragment](/en-US/docs/Web/API/DocumentFragment).

[Range.getBoundingClientRect()](/en-US/docs/Web/API/Range/getBoundingClientRect)

Returns a [DOMRect](/en-US/docs/Web/API/DOMRect) object which bounds the entire contents of the `Range`; this would be the union of all the rectangles returned by [range.getClientRects()](/en-US/docs/Web/API/Range/getClientRects).

[Range.getClientRects()](/en-US/docs/Web/API/Range/getClientRects)

Returns a list of [DOMRect](/en-US/docs/Web/API/DOMRect) objects that aggregates the results of [Element.getClientRects()](/en-US/docs/Web/API/Element/getClientRects) for all the elements in the `Range`.

[Range.isPointInRange()](/en-US/docs/Web/API/Range/isPointInRange)

Returns a `boolean` indicating whether the given point is in the `Range`.

[Range.insertNode()](/en-US/docs/Web/API/Range/insertNode)

Insert a [Node](/en-US/docs/Web/API/Node) at the start of a `Range`.

[Range.intersectsNode()](/en-US/docs/Web/API/Range/intersectsNode)

Returns a `boolean` indicating whether the given node intersects the `Range`.

[Range.selectNode()](/en-US/docs/Web/API/Range/selectNode)

Sets the `Range` to contain the [Node](/en-US/docs/Web/API/Node) and its contents.

[Range.selectNodeContents()](/en-US/docs/Web/API/Range/selectNodeContents)

Sets the `Range` to contain the contents of a [Node](/en-US/docs/Web/API/Node).

[Range.setEnd()](/en-US/docs/Web/API/Range/setEnd)

Sets the end position of a `Range`.

[Range.setStart()](/en-US/docs/Web/API/Range/setStart)

Sets the start position of a `Range`.

[Range.setEndAfter()](/en-US/docs/Web/API/Range/setEndAfter)

Sets the end position of a `Range` relative to another [Node](/en-US/docs/Web/API/Node).

[Range.setEndBefore()](/en-US/docs/Web/API/Range/setEndBefore)

Sets the end position of a `Range` relative to another [Node](/en-US/docs/Web/API/Node).

[Range.setStartAfter()](/en-US/docs/Web/API/Range/setStartAfter)

Sets the start position of a `Range` relative to another [Node](/en-US/docs/Web/API/Node).

[Range.setStartBefore()](/en-US/docs/Web/API/Range/setStartBefore)

Sets the start position of a `Range` relative to another [Node](/en-US/docs/Web/API/Node).

[Range.surroundContents()](/en-US/docs/Web/API/Range/surroundContents)

Moves content of a `Range` into a new [Node](/en-US/docs/Web/API/Node).

[Range.toString()](/en-US/docs/Web/API/Range/toString)

Returns the text of the `Range`.

## [Specifications](#specifications)

Specification
[DOM# interface-range](https://dom.spec.whatwg.org/#interface-range)
[DOM Parsing and Serialization# extensions-to-the-range-interface](https://w3c.github.io/DOM-Parsing/#extensions-to-the-range-interface)
[CSSOM View Module# extensions-to-the-range-interface](https://drafts.csswg.org/cssom-view/#extensions-to-the-range-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The DOM interfaces index](/en-US/docs/Web/API/Document_Object_Model)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/Range/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/range/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRange&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frange%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRange%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frange%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2937558d5ed1e03d7f60b2de71dd9c17f490166e%0A*+Document+last+modified%3A+2023-02-19T10%3A03%3A58.000Z%0A%0A%3C%2Fdetails%3E)
