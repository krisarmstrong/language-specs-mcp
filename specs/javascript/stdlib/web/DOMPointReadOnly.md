# DOMPointReadOnly

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMPointReadOnly&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `DOMPointReadOnly` interface specifies the coordinate and perspective fields used by [DOMPoint](/en-US/docs/Web/API/DOMPoint) to define a 2D or 3D point in a coordinate system.

There are two ways to create a new `DOMPointReadOnly` instance. First, you can use its constructor, passing in the values of the parameters for each dimension and, optionally, the perspective:

js

```
/* 2D */
const point2D = new DOMPointReadOnly(50, 50);

/* 3D */
const point3D = new DOMPointReadOnly(50, 50, 25);

/* 3D with perspective */
const point3DPerspective = new DOMPointReadOnly(100, 100, 100, 1.0);
```

The other option is to use the static [DOMPointReadOnly.fromPoint()](/en-US/docs/Web/API/DOMPointReadOnly/fromPoint_static) method:

js

```
const point = DOMPointReadOnly.fromPoint({ x: 100, y: 100, z: 50, w: 1.0 });
```

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMPointReadOnly()](/en-US/docs/Web/API/DOMPointReadOnly/DOMPointReadOnly)

Creates a new `DOMPointReadOnly` object given the values of its coordinates and perspective. To create a point using an object, you can instead use [DOMPointReadOnly.fromPoint()](/en-US/docs/Web/API/DOMPointReadOnly/fromPoint_static).

## [Instance properties](#instance_properties)

[DOMPointReadOnly.x](/en-US/docs/Web/API/DOMPointReadOnly/x)Read only

The point's horizontal coordinate, `x`.

[DOMPointReadOnly.y](/en-US/docs/Web/API/DOMPointReadOnly/y)Read only

The point's vertical coordinate, `y`.

[DOMPointReadOnly.z](/en-US/docs/Web/API/DOMPointReadOnly/z)Read only

The point's depth coordinate, `z`.

[DOMPointReadOnly.w](/en-US/docs/Web/API/DOMPointReadOnly/w)Read only

The point's perspective value, `w`.

## [Static methods](#static_methods)

[DOMPointReadOnly.fromPoint()](/en-US/docs/Web/API/DOMPointReadOnly/fromPoint_static)

A static method that creates a new `DOMPointReadOnly` object given the coordinates provided in the specified object.

## [Instance methods](#instance_methods)

[matrixTransform()](/en-US/docs/Web/API/DOMPointReadOnly/matrixTransform)

Applies a matrix transform specified as an object to the `DOMPointReadOnly` object.

[toJSON()](/en-US/docs/Web/API/DOMPointReadOnly/toJSON)

Returns a JSON representation of the `DOMPointReadOnly` object.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMPoint](https://drafts.fxtf.org/geometry/#DOMPoint)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMPoint](/en-US/docs/Web/API/DOMPoint)
- [DOMRect](/en-US/docs/Web/API/DOMRect)
- [DOMMatrix](/en-US/docs/Web/API/DOMMatrix)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMPointReadOnly/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dompointreadonly/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMPointReadOnly&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdompointreadonly%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMPointReadOnly%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdompointreadonly%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3652cfa9c036cf3ceebb1384bdc7edfd549251f3%0A*+Document+last+modified%3A+2024-10-08T19%3A28%3A25.000Z%0A%0A%3C%2Fdetails%3E)
