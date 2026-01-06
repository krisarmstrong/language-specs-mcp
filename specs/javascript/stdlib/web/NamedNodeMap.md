# NamedNodeMap

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNamedNodeMap&level=high)

The `NamedNodeMap` interface represents a collection of [Attr](/en-US/docs/Web/API/Attr) objects. Objects inside a `NamedNodeMap` are not in any particular order, unlike [NodeList](/en-US/docs/Web/API/NodeList), although they may be accessed by an index as in an array.

A `NamedNodeMap` object is live and will thus be auto-updated if changes are made to its contents internally or elsewhere.

Note: Although called `NamedNodeMap`, this interface doesn't deal with [Node](/en-US/docs/Web/API/Node) objects but with [Attr](/en-US/docs/Web/API/Attr) objects, which are a specialized class of [Node](/en-US/docs/Web/API/Node) objects.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface doesn't inherit any property.

[NamedNodeMap.length](/en-US/docs/Web/API/NamedNodeMap/length)Read only

Returns the amount of objects in the map.

## [Instance methods](#instance_methods)

This interface doesn't inherit any method.

[NamedNodeMap.getNamedItem()](/en-US/docs/Web/API/NamedNodeMap/getNamedItem)

Returns an [Attr](/en-US/docs/Web/API/Attr), corresponding to the given name.

[NamedNodeMap.setNamedItem()](/en-US/docs/Web/API/NamedNodeMap/setNamedItem)

Replaces, or adds, the [Attr](/en-US/docs/Web/API/Attr) identified in the map by the given name.

[NamedNodeMap.removeNamedItem()](/en-US/docs/Web/API/NamedNodeMap/removeNamedItem)

Removes the [Attr](/en-US/docs/Web/API/Attr) identified by the given map.

[NamedNodeMap.item()](/en-US/docs/Web/API/NamedNodeMap/item)

Returns the [Attr](/en-US/docs/Web/API/Attr) at the given index, or `null` if the index is higher or equal to the number of nodes.

[NamedNodeMap.getNamedItemNS()](/en-US/docs/Web/API/NamedNodeMap/getNamedItemNS)

Returns an [Attr](/en-US/docs/Web/API/Attr) identified by a namespace and related local name.

[NamedNodeMap.setNamedItemNS()](/en-US/docs/Web/API/NamedNodeMap/setNamedItemNS)

Replaces, or adds, the [Attr](/en-US/docs/Web/API/Attr) identified in the map by the given namespace and related local name.

[NamedNodeMap.removeNamedItemNS()](/en-US/docs/Web/API/NamedNodeMap/removeNamedItemNS)

Removes the [Attr](/en-US/docs/Web/API/Attr) identified by the given namespace and related local name.

## [Specifications](#specifications)

Specification
[DOM# interface-namednodemap](https://dom.spec.whatwg.org/#interface-namednodemap)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Element.attributes](/en-US/docs/Web/API/Element/attributes)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/NamedNodeMap/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/namednodemap/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNamedNodeMap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnamednodemap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNamedNodeMap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnamednodemap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfb7587e3e3122630ad6cbd94d834ecadbe0a746%0A*+Document+last+modified%3A+2024-07-26T03%3A44%3A38.000Z%0A%0A%3C%2Fdetails%3E)
