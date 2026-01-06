# DOMRectReadOnly

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRectReadOnly&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `DOMRectReadOnly` interface specifies the standard properties (also used by [DOMRect](/en-US/docs/Web/API/DOMRect)) to define a rectangle whose properties are immutable.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMRectReadOnly()](/en-US/docs/Web/API/DOMRectReadOnly/DOMRectReadOnly)

Defined to create a new `DOMRectReadOnly` object.

## [Instance properties](#instance_properties)

[DOMRectReadOnly.x](/en-US/docs/Web/API/DOMRectReadOnly/x)Read only

Returns the x coordinate of the `DOMRectReadOnly`'s origin.

[DOMRectReadOnly.y](/en-US/docs/Web/API/DOMRectReadOnly/y)Read only

Returns the y coordinate of the `DOMRectReadOnly`'s origin.

[DOMRectReadOnly.width](/en-US/docs/Web/API/DOMRectReadOnly/width)Read only

Returns the width of the `DOMRectReadOnly`.

[DOMRectReadOnly.height](/en-US/docs/Web/API/DOMRectReadOnly/height)Read only

Returns the height of the `DOMRectReadOnly`.

[DOMRectReadOnly.top](/en-US/docs/Web/API/DOMRectReadOnly/top)Read only

Returns the top coordinate value of the `DOMRectReadOnly` (usually the same as `y`).

[DOMRectReadOnly.right](/en-US/docs/Web/API/DOMRectReadOnly/right)Read only

Returns the right coordinate value of the `DOMRectReadOnly` (usually the same as `x + width`).

[DOMRectReadOnly.bottom](/en-US/docs/Web/API/DOMRectReadOnly/bottom)Read only

Returns the bottom coordinate value of the `DOMRectReadOnly` (usually the same as `y + height`).

[DOMRectReadOnly.left](/en-US/docs/Web/API/DOMRectReadOnly/left)Read only

Returns the left coordinate value of the `DOMRectReadOnly` (usually the same as `x`).

## [Static methods](#static_methods)

[DOMRectReadOnly.fromRect()](/en-US/docs/Web/API/DOMRectReadOnly/fromRect_static)

Creates a new `DOMRectReadOnly` object with a given location and dimensions.

## [Instance methods](#instance_methods)

[DOMRectReadOnly.toJSON()](/en-US/docs/Web/API/DOMRectReadOnly/toJSON)

Returns a JSON representation of the `DOMRectReadOnly` object.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMRect](https://drafts.fxtf.org/geometry/#DOMRect)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMPoint](/en-US/docs/Web/API/DOMPoint)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 16, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMRectReadOnly/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domrectreadonly/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRectReadOnly&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomrectreadonly%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRectReadOnly%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomrectreadonly%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9f09d944bca13b61293b4cc93cb52011c6134b0d%0A*+Document+last+modified%3A+2024-11-16T01%3A07%3A04.000Z%0A%0A%3C%2Fdetails%3E)
