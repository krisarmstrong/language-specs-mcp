# Geometry interfaces

Geometry interfaces is a CSS module that provides interfaces for working with 3D and 2D graphics — in particular, for working with points, rectangles, quadrilaterals and [transformation matrices](/en-US/docs/Web/API/WebGL_API/Matrix_math_for_the_web#transformation_matrices) (for operations that translate/move, scale, rotate, skew/shear/slant, and flip graphics, as well as for multiplying/chaining and inverting/undoing those operations).

As a web developer, you don't always use the geometry interfaces directly, but instead use other features that rely on them behind the scenes: parts of [CSS Transforms](/en-US/docs/Web/CSS/Guides/Transforms), the [Canvas API](/en-US/docs/Web/API/Canvas_API), the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API), and (more directly) [VideoFrame.visibleRect](/en-US/docs/Web/API/VideoFrame/visibleRect), [Element.getClientRects()](/en-US/docs/Web/API/Element/getClientRects), and [Element.getBoundingClientRect()](/en-US/docs/Web/API/Element/getBoundingClientRect).

## In this article

- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[DOMMatrix](/en-US/docs/Web/API/DOMMatrix)

Represents a [transformation matrix](/en-US/docs/Web/API/WebGL_API/Matrix_math_for_the_web#transformation_matrices), for operations that translate/move, scale, rotate, skew/shear/slant, and flip graphics, as well as for multiplying/chaining and inverting/undoing those operations.

[DOMMatrixReadOnly](/en-US/docs/Web/API/DOMMatrixReadOnly)

Read-only version of [DOMMatrix](/en-US/docs/Web/API/DOMMatrix).

[DOMPoint](/en-US/docs/Web/API/DOMPoint)

Represents a 2D or 3D point in a coordinate system; it includes values for the coordinates in up to three dimensions, as well as an optional perspective value.

[DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly)

Read-only version of [DOMPoint](/en-US/docs/Web/API/DOMPoint).

[DOMQuad](/en-US/docs/Web/API/DOMQuad)

Represents a collection of four [DOMPoint](/en-US/docs/Web/API/DOMPoint) objects defining the corners of a [quadrilateral](https://en.wikipedia.org/wiki/Quadrilateral).

[DOMRect](/en-US/docs/Web/API/DOMRect)

Represents the size and position of a rectangle.

[DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly)

Read-only version of [DOMRect](/en-US/docs/Web/API/DOMRect).

## [Examples](#examples)

The [Path2D.addPath()](/en-US/docs/Web/API/Path2D/addPath) and [CanvasPattern.setTransform()](/en-US/docs/Web/API/CanvasPattern/setTransform) articles have examples that use some of the geometry interfaces.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMMatrix](https://drafts.fxtf.org/geometry/#DOMMatrix)
[Geometry Interfaces Module Level 1# DOMPoint](https://drafts.fxtf.org/geometry/#DOMPoint)
[Geometry Interfaces Module Level 1# DOMQuad](https://drafts.fxtf.org/geometry/#DOMQuad)
[Geometry Interfaces Module Level 1# DOMRect](https://drafts.fxtf.org/geometry/#DOMRect)

## [Browser compatibility](#browser_compatibility)

### [api.DOMMatrix](#api.DOMMatrix)

### [api.DOMMatrixReadOnly](#api.DOMMatrixReadOnly)

### [api.DOMPoint](#api.DOMPoint)

### [api.DOMPointReadOnly](#api.DOMPointReadOnly)

### [api.DOMQuad](#api.DOMQuad)

### [api.DOMRect](#api.DOMRect)

### [api.DOMRectReadOnly](#api.DOMRectReadOnly)

## [See also](#see_also)

- [Path2D.addPath()](/en-US/docs/Web/API/Path2D/addPath)
- [CanvasPattern.setTransform()](/en-US/docs/Web/API/CanvasPattern/setTransform)
- [CanvasRenderingContext2D.getTransform()](/en-US/docs/Web/API/CanvasRenderingContext2D/getTransform)
- [CanvasRenderingContext2D.setTransform()](/en-US/docs/Web/API/CanvasRenderingContext2D/setTransform)
- [CSSTransformValue.toMatrix()](/en-US/docs/Web/API/CSSTransformValue/toMatrix)
- [CSSTransformComponent.toMatrix()](/en-US/docs/Web/API/CSSTransformComponent/toMatrix)
- [Element.getBoundingClientRect()](/en-US/docs/Web/API/Element/getBoundingClientRect)
- [Element.getClientRects()](/en-US/docs/Web/API/Element/getClientRects)
- [VideoFrame.visibleRect](/en-US/docs/Web/API/VideoFrame/visibleRect)
- [XRLightEstimate](/en-US/docs/Web/API/XRLightEstimate)
- [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Geometry_interfaces/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/geometry_interfaces/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeometry_interfaces&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgeometry_interfaces%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeometry_interfaces%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgeometry_interfaces%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
