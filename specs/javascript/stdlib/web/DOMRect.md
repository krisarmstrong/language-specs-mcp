# DOMRect

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRect&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

A `DOMRect` describes the size and position of a rectangle.

The type of box represented by the `DOMRect` is specified by the method or property that returned it. For example, [Range.getBoundingClientRect()](/en-US/docs/Web/API/Range/getBoundingClientRect) specifies the rectangle that bounds the content of the range using such objects.

It inherits from its parent, [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMRect()](/en-US/docs/Web/API/DOMRect/DOMRect)

Creates a new `DOMRect` object.

## [Instance properties](#instance_properties)

`DOMRect` inherits properties from its parent, [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly). The difference is that they are not read-only anymore.

[DOMRect.x](/en-US/docs/Web/API/DOMRect/x)

The x coordinate of the `DOMRect`'s origin (typically the top-left corner of the rectangle).

[DOMRect.y](/en-US/docs/Web/API/DOMRect/y)

The y coordinate of the `DOMRect`'s origin (typically the top-left corner of the rectangle).

[DOMRect.width](/en-US/docs/Web/API/DOMRect/width)

The width of the `DOMRect`.

[DOMRect.height](/en-US/docs/Web/API/DOMRect/height)

The height of the `DOMRect`.

[DOMRectReadOnly.top](/en-US/docs/Web/API/DOMRectReadOnly/top)

Returns the top coordinate value of the `DOMRect` (has the same value as `y`, or `y + height` if `height` is negative).

[DOMRectReadOnly.right](/en-US/docs/Web/API/DOMRectReadOnly/right)

Returns the right coordinate value of the `DOMRect` (has the same value as `x + width`, or `x` if `width` is negative).

[DOMRectReadOnly.bottom](/en-US/docs/Web/API/DOMRectReadOnly/bottom)

Returns the bottom coordinate value of the `DOMRect` (has the same value as `y + height`, or `y` if `height` is negative).

[DOMRectReadOnly.left](/en-US/docs/Web/API/DOMRectReadOnly/left)

Returns the left coordinate value of the `DOMRect` (has the same value as `x`, or `x + width` if `width` is negative).

## [Static methods](#static_methods)

`DOMRect` may also inherit static methods from its parent, [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly).

[DOMRect.fromRect()](/en-US/docs/Web/API/DOMRect/fromRect_static)

Creates a new `DOMRect` object with a given location and dimensions.

## [Instance methods](#instance_methods)

`DOMRect` may inherit methods from its parent, [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly).

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMRect](https://drafts.fxtf.org/geometry/#DOMRect)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMPoint](/en-US/docs/Web/API/DOMPoint)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMRect/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domrect/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomrect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMRect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomrect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdc82e604c805cd2eae887a371111e902c8c52241%0A*+Document+last+modified%3A+2024-11-17T20%3A35%3A49.000Z%0A%0A%3C%2Fdetails%3E)
