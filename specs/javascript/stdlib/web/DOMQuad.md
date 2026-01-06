# DOMQuad

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMQuad&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

A `DOMQuad` is a collection of four `DOMPoint`s defining the corners of an arbitrary quadrilateral. Returning `DOMQuad`s lets `getBoxQuads()` return accurate information even when arbitrary 2D or 3D transforms are present. It has a handy `bounds` attribute returning a `DOMRectReadOnly` for those cases where you just want an axis-aligned bounding rectangle.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static methods](#static_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[DOMQuad()](/en-US/docs/Web/API/DOMQuad/DOMQuad)

Creates a new `DOMQuad` object.

## [Instance properties](#instance_properties)

[DOMQuad.p1](/en-US/docs/Web/API/DOMQuad/p1)Read only

A [DOMPoint](/en-US/docs/Web/API/DOMPoint) representing one corner of the `DOMQuad`.

[DOMQuad.p2](/en-US/docs/Web/API/DOMQuad/p2)Read only

A [DOMPoint](/en-US/docs/Web/API/DOMPoint) representing one corner of the `DOMQuad`.

[DOMQuad.p3](/en-US/docs/Web/API/DOMQuad/p3)Read only

A [DOMPoint](/en-US/docs/Web/API/DOMPoint) representing one corner of the `DOMQuad`.

[DOMQuad.p4](/en-US/docs/Web/API/DOMQuad/p4)Read only

A [DOMPoint](/en-US/docs/Web/API/DOMPoint) representing one corner of the `DOMQuad`.

## [Instance methods](#instance_methods)

[DOMQuad.getBounds()](/en-US/docs/Web/API/DOMQuad/getBounds)

Returns a [DOMRect](/en-US/docs/Web/API/DOMRect) object with the coordinates and dimensions of the `DOMQuad` object.

[DOMQuad.toJSON()](/en-US/docs/Web/API/DOMQuad/toJSON)

Returns a JSON representation of the `DOMQuad` object.

## [Static methods](#static_methods)

[DOMQuad.fromQuad()](/en-US/docs/Web/API/DOMQuad/fromQuad_static)

Returns a new `DOMQuad` object based on the provided set of coordinates in the shape of another `DOMQuad` object.

[DOMQuad.fromRect()](/en-US/docs/Web/API/DOMQuad/fromRect_static)

Returns a new `DOMQuad` object based on the provided set of coordinates in the shape of a [DOMRect](/en-US/docs/Web/API/DOMRect) object.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMQuad](https://drafts.fxtf.org/geometry/#DOMQuad)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMQuad/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domquad/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMQuad&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomquad%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMQuad%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomquad%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fad44886809ba4fac0cda32fd0c83a3dfbae14e57%0A*+Document+last+modified%3A+2025-10-27T13%3A48%3A00.000Z%0A%0A%3C%2Fdetails%3E)
