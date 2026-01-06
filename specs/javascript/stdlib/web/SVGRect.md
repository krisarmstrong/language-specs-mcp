# SVGRect

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGRect&level=high)

The `SVGRect`, an alias for [DOMRect](/en-US/docs/Web/API/DOMRect), represents a rectangle. Rectangles consist of an `x` and `y` coordinate pair identifying a minimum `x` value, a minimum `y` value, and a `width` and `height`, which are constrained to be non-negative.

An `SVGRect` object can be designated as read only, which means that attempts to modify the object will result in an exception being thrown.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[SVGRect.x](/en-US/docs/Web/API/SVGRect/x)

The exact effect of this coordinate depends on each element. If the attribute is not specified, the effect is as if a value of `0` were specified.

[SVGRect.y](/en-US/docs/Web/API/SVGRect/y)

The exact effect of this coordinate depends on each element. If the attribute is not specified, the effect is as if a value of `0` were specified.

[SVGRect.width](/en-US/docs/Web/API/SVGRect/width)

This represents the width of the rectangle. A value that is negative results to an error. A value of `0` disables rendering of the element

[SVGRect.height](/en-US/docs/Web/API/SVGRect/height)

This represents the height of the rectangle. A value that is negative results to an error. A value of `0` disables rendering of the element.

## [Instance methods](#instance_methods)

None.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMRect](https://drafts.fxtf.org/geometry/#DOMRect)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMRect](/en-US/docs/Web/API/DOMRect)
- [DOMPoint](/en-US/docs/Web/API/DOMPoint) alias [SVGPoint](/en-US/docs/Web/API/SVGPoint)
- [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) alias [SVGMatrix](/en-US/docs/Web/API/DOMMatrix)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGRect/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgrect/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGRect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgrect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGRect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgrect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3ae7f380c04096191376ffc2b455471e5d5fd8a8%0A*+Document+last+modified%3A+2025-01-07T09%3A38%3A48.000Z%0A%0A%3C%2Fdetails%3E)
