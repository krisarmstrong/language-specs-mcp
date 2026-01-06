# Path2D

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨August 2016⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPath2D&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Path2D` interface of the Canvas 2D API is used to declare a path that can then be used on a [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D) object. The [path methods](/en-US/docs/Web/API/CanvasRenderingContext2D#paths) of the `CanvasRenderingContext2D` interface are also present on this interface, which gives you the convenience of being able to retain and replay your path whenever desired.

## In this article

- [Constructors](#constructors)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[Path2D()](/en-US/docs/Web/API/Path2D/Path2D)

`Path2D` constructor. Creates a new `Path2D` object.

## [Instance methods](#instance_methods)

[Path2D.addPath()](/en-US/docs/Web/API/Path2D/addPath)

Adds a path to the current path.

[Path2D.closePath()](/en-US/docs/Web/API/CanvasRenderingContext2D/closePath)

Causes the point of the pen to move back to the start of the current sub-path. It tries to draw a straight line from the current point to the start. If the shape has already been closed or has only one point, this function does nothing.

[Path2D.moveTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/moveTo)

Moves the starting point of a new sub-path to the (`x, y`) coordinates.

[Path2D.lineTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/lineTo)

Connects the last point in the subpath to the (`x, y`) coordinates with a straight line.

[Path2D.bezierCurveTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/bezierCurveTo)

Adds a cubic Bézier curve to the path. It requires three points. The first two points are control points and the third one is the end point. The starting point is the last point in the current path, which can be changed using `moveTo()` before creating the Bézier curve.

[Path2D.quadraticCurveTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/quadraticCurveTo)

Adds a quadratic Bézier curve to the current path.

[Path2D.arc()](/en-US/docs/Web/API/CanvasRenderingContext2D/arc)

Adds an arc to the path which is centered at (`x, y`) position with radius `r` starting at `startAngle` and ending at `endAngle` going in the given direction by `counterclockwise` (defaulting to clockwise).

[Path2D.arcTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/arcTo)

Adds a circular arc to the path with the given control points and radius, connected to the previous point by a straight line.

[Path2D.ellipse()](/en-US/docs/Web/API/CanvasRenderingContext2D/ellipse)

Adds an elliptical arc to the path which is centered at (`x, y`) position with the radii `radiusX` and `radiusY` starting at `startAngle` and ending at `endAngle` going in the given direction by `counterclockwise` (defaulting to clockwise).

[Path2D.rect()](/en-US/docs/Web/API/CanvasRenderingContext2D/rect)

Creates a path for a rectangle at position (`x, y`) with a size that is determined by `width` and `height`.

[Path2D.roundRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/roundRect)

Creates a path for a rounded rectangle at position (`x, y`) with a size that is determined by `width` and `height` and the radii of the circular arc to be used for the corners of the rectangle is determined by `radii`.

## [Specifications](#specifications)

Specification
[HTML# path2d-objects](https://html.spec.whatwg.org/multipage/canvas.html#path2d-objects)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Path2D/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/path2d/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPath2D&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpath2d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPath2D%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpath2d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdaeff1a2efaae366bcc8b6d911d86985646e665e%0A*+Document+last+modified%3A+2024-04-22T04%3A54%3A38.000Z%0A%0A%3C%2Fdetails%3E)
