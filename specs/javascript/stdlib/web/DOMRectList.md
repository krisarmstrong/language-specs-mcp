# DOMRectList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRectList&level=high)

The `DOMRectList` interface represents a collection of [DOMRect](/en-US/docs/Web/API/DOMRect) objects, typically used to hold the rectangles associated with a particular element, like bounding boxes returned by methods such as [getClientRects()](/en-US/docs/Web/API/Element/getClientRects). It provides access to each rectangle in the list via its index, along with a `length` property that indicates the total number of rectangles in the list.

Note:`DOMRectList` exists for compatibility with legacy Web content and is not recommended to be used when creating new APIs.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[DOMRectList.length](/en-US/docs/Web/API/DOMRectList/length)Read only

A read-only property that returns the total number of [DOMRect](/en-US/docs/Web/API/DOMRect) objects in the `DOMRectList`.

## [Instance methods](#instance_methods)

[DOMRectList.item](/en-US/docs/Web/API/DOMRectList/item)

Returns the [DOMRect](/en-US/docs/Web/API/DOMRect) object at the specified index. If the `index` is out of range, it returns `null`.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMRectList](https://drafts.fxtf.org/geometry/#DOMRectList)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMRect](/en-US/docs/Web/API/DOMRect)
- [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMRectList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domrectlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRectList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomrectlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRectList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomrectlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd0ed4906719465102739e604bdb35213fb19f251%0A*+Document+last+modified%3A+2025-06-26T01%3A52%3A11.000Z%0A%0A%3C%2Fdetails%3E)
