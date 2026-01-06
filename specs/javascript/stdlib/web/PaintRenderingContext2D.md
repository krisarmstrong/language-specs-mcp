# PaintRenderingContext2D

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaintRenderingContext2D&level=not)

The `PaintRenderingContext2D` interface of the [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API) is the API's rendering context for drawing to the bitmap. It implements a subset of the [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D) API, with the following exceptions:

- It doesn't implement the [CanvasImageData pixel manipulation](/en-US/docs/Web/API/CanvasRenderingContext2D#pixel_manipulation), [CanvasUserInterface focus](/en-US/docs/Web/API/CanvasRenderingContext2D/drawFocusIfNeeded), [CanvasText text drawing](/en-US/docs/Web/API/CanvasRenderingContext2D), or [CanvasTextDrawingStyles text style](/en-US/docs/Web/API/CanvasRenderingContext2D#text_styles) interface methods.
- The output bitmap is the size of the object it is rendering to.
- The value `currentColor`, when used as a color, is treated as opaque black.

The interface is only available in [PaintWorkletGlobalScope](/en-US/docs/Web/API/PaintWorkletGlobalScope).

## In this article

- [Instance properties and methods](#instance_properties_and_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties and methods](#instance_properties_and_methods)

The `PaintRenderingContext2D` implements a subset of the [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D) API, with all properties and methods having the same usage as in `CanvasRenderingContext2D`

### [Context](#context)

[CanvasRenderingContext2D.isContextLost()](/en-US/docs/Web/API/CanvasRenderingContext2D/isContextLost)

Returns `true` if the rendering context was lost.

### [State](#state)

[CanvasRenderingContext2D.save()](/en-US/docs/Web/API/CanvasRenderingContext2D/save)

Saves the current drawing style state using a stack so you can revert any change you make to it using `restore()`.

[CanvasRenderingContext2D.restore()](/en-US/docs/Web/API/CanvasRenderingContext2D/restore)

Restores the drawing style state to the last element on the 'state stack' saved by `save()`.

[CanvasRenderingContext2D.reset()](/en-US/docs/Web/API/CanvasRenderingContext2D/reset)

Resets the current drawing style state to the default values.

### [Transformations](#transformations)

[CanvasRenderingContext2D.getTransform()](/en-US/docs/Web/API/CanvasRenderingContext2D/getTransform)

Retrieves the current transformation matrix being applied to the context as a [DOMMatrix](/en-US/docs/Web/API/DOMMatrix).

[CanvasRenderingContext2D.rotate()](/en-US/docs/Web/API/CanvasRenderingContext2D/rotate)

Adds a rotation to the transformation matrix. The angle argument represents a clockwise rotation angle and is expressed in radians.

[CanvasRenderingContext2D.scale()](/en-US/docs/Web/API/CanvasRenderingContext2D/scale)

Adds a scaling transformation to the canvas units by x horizontally and by y vertically.

[CanvasRenderingContext2D.translate()](/en-US/docs/Web/API/CanvasRenderingContext2D/translate)

Adds a translation transformation by moving the canvas and its origin x horizontally and y vertically on the grid.

[CanvasRenderingContext2D.transform()](/en-US/docs/Web/API/CanvasRenderingContext2D/transform)

Multiplies the current transformation matrix with the matrix described by its arguments.

[CanvasRenderingContext2D.setTransform()](/en-US/docs/Web/API/CanvasRenderingContext2D/setTransform)

Resets the current transform to the identity matrix, and then invokes the `transform()` method with the same arguments.

[CanvasRenderingContext2D.resetTransform()](/en-US/docs/Web/API/CanvasRenderingContext2D/resetTransform)

Resets the current transform by the identity matrix.

### [Compositing](#compositing)

[CanvasRenderingContext2D.globalAlpha](/en-US/docs/Web/API/CanvasRenderingContext2D/globalAlpha)

Alpha value that is applied to shapes and images before they are composited onto the canvas.

[CanvasRenderingContext2D.globalCompositeOperation](/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation)

With `globalAlpha` applied, this sets how shapes and images are drawn onto the existing bitmap.

### [Image smoothing](#image_smoothing)

[CanvasRenderingContext2D.imageSmoothingEnabled](/en-US/docs/Web/API/CanvasRenderingContext2D/imageSmoothingEnabled)

Image smoothing mode; if disabled, images will not be smoothed if scaled.

[CanvasRenderingContext2D.imageSmoothingQuality](/en-US/docs/Web/API/CanvasRenderingContext2D/imageSmoothingQuality)

Allows you to set the quality of image smoothing.

### [Fill and stroke styles](#fill_and_stroke_styles)

[CanvasRenderingContext2D.fillStyle](/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle)

Color or style to use inside shapes.

[CanvasRenderingContext2D.strokeStyle](/en-US/docs/Web/API/CanvasRenderingContext2D/strokeStyle)

Color or style to use for the lines around shapes.

### [Gradients and patterns](#gradients_and_patterns)

[CanvasRenderingContext2D.createConicGradient()](/en-US/docs/Web/API/CanvasRenderingContext2D/createConicGradient)

Creates a conic gradient around a point given by coordinates represented by the parameters.

[CanvasRenderingContext2D.createLinearGradient()](/en-US/docs/Web/API/CanvasRenderingContext2D/createLinearGradient)

Creates a linear gradient along the line given by the coordinates represented by the parameters.

[CanvasRenderingContext2D.createRadialGradient()](/en-US/docs/Web/API/CanvasRenderingContext2D/createRadialGradient)

Creates a radial gradient given by the coordinates of the two circles represented by the parameters.

[CanvasRenderingContext2D.createPattern()](/en-US/docs/Web/API/CanvasRenderingContext2D/createPattern)

Creates a [CanvasPattern](/en-US/docs/Web/API/CanvasPattern) pattern of the specified image repeated in the directions specified by the repetition argument.

### [Shadows](#shadows)

[CanvasRenderingContext2D.shadowBlur](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowBlur)

Specifies the amount of blur as a number.

[CanvasRenderingContext2D.shadowColor](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowColor)

Specifies the color of the shadow as a CSS [<color>](/en-US/docs/Web/CSS/Reference/Values/color_value).

[CanvasRenderingContext2D.shadowOffsetX](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowOffsetX)

Specifies the horizontal distance the shadow will be offset as a number.

[CanvasRenderingContext2D.shadowOffsetY](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowOffsetY)

Specifies the vertical distance the shadow will be offset as a number.

### [Drawing rectangles](#drawing_rectangles)

[CanvasRenderingContext2D.clearRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/clearRect)

Erases the pixels in the given rectangle, setting them to transparent black.

[CanvasRenderingContext2D.fillRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/fillRect)

Paints the pixels of the given rectangle, filling it with the current fill style.

[CanvasRenderingContext2D.strokeRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/strokeRect)

Paints the outline of the given rectangle using the current stroke style.

### [Drawing paths](#drawing_paths)

[CanvasRenderingContext2D.beginPath()](/en-US/docs/Web/API/CanvasRenderingContext2D/beginPath)

Starts a new path, emptying the list of sub-paths. Call this method when you want to create a new path.

[CanvasRenderingContext2D.fill()](/en-US/docs/Web/API/CanvasRenderingContext2D/fill)

Fills the sub-paths of the current path with the current fill style.

[CanvasRenderingContext2D.stroke()](/en-US/docs/Web/API/CanvasRenderingContext2D/stroke)

Strokes the sub-paths of the current path with the current stroke style.

[CanvasRenderingContext2D.clip()](/en-US/docs/Web/API/CanvasRenderingContext2D/clip)

Turns the current or given path into the current clipping region, using the given fill rule to determine which points are in the path. Subsequent path modifications will appear inside the clipping path only.

[CanvasRenderingContext2D.isPointInPath()](/en-US/docs/Web/API/CanvasRenderingContext2D/isPointInPath)

A boolean whose value is `true` if the specified point is contained in the current or specified path.

[CanvasRenderingContext2D.isPointInStroke()](/en-US/docs/Web/API/CanvasRenderingContext2D/isPointInStroke)

A boolean whose value is `true` if the point is inside the area contained by the stroking of a path

### [Drawing images](#drawing_images)

[CanvasRenderingContext2D.drawImage()](/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage)

Draws the given image or specified portion thereof, optionally at a specified size and position.

### [Line styles](#line_styles)

[CanvasRenderingContext2D.lineWidth](/en-US/docs/Web/API/CanvasRenderingContext2D/lineWidth)

A number specifying the line width, in coordinate space units.

[CanvasRenderingContext2D.lineCap](/en-US/docs/Web/API/CanvasRenderingContext2D/lineCap)

Type of endings on the end of lines. Possible values: `butt` (default), `round`, `square`.

[CanvasRenderingContext2D.lineJoin](/en-US/docs/Web/API/CanvasRenderingContext2D/lineJoin)

Defines the type of corners where two lines meet. Possible values: `round`, `bevel`, `miter` (default).

[CanvasRenderingContext2D.miterLimit](/en-US/docs/Web/API/CanvasRenderingContext2D/miterLimit)

A number specifying the miter limit ratio, in coordinate space units.

[CanvasRenderingContext2D.getLineDash()](/en-US/docs/Web/API/CanvasRenderingContext2D/getLineDash)

Returns the current line dash pattern as an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of numbers that specify the lengths of the alternative lines and gaps in coordinate space units.

[CanvasRenderingContext2D.setLineDash()](/en-US/docs/Web/API/CanvasRenderingContext2D/setLineDash)

Sets the list of line and dash distances as the current line dash pattern (as used when stroking).

[CanvasRenderingContext2D.lineDashOffset](/en-US/docs/Web/API/CanvasRenderingContext2D/lineDashOffset)

Specifies where to start a dash array on a line.

### [Paths](#paths)

[CanvasRenderingContext2D.closePath()](/en-US/docs/Web/API/CanvasRenderingContext2D/closePath)

Marks the current subpath as closed, drawing a straight line from the current point to the start, and starts a new subpath with a point the same as the start and end of the newly closed subpath. If the shape has already been closed or has only one point, this function does nothing.

[CanvasRenderingContext2D.moveTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/moveTo)

Moves the starting point of a new sub-path to the (x, y) coordinates.

[CanvasRenderingContext2D.lineTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/lineTo)

Connects the last point in the current sub-path to the specified (x, y) coordinates with a straight line.

[CanvasRenderingContext2D.bezierCurveTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/bezierCurveTo)

Adds a cubic Bézier curve to the current path.

[CanvasRenderingContext2D.quadraticCurveTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/quadraticCurveTo)

Adds a quadratic Bézier curve to the current path.

[CanvasRenderingContext2D.arc()](/en-US/docs/Web/API/CanvasRenderingContext2D/arc)

Adds a circular arc to the current path.

[CanvasRenderingContext2D.arcTo()](/en-US/docs/Web/API/CanvasRenderingContext2D/arcTo)

Adds an arc to the current path with the given control points and radius, connected to the previous point by a straight line.

[CanvasRenderingContext2D.ellipse()](/en-US/docs/Web/API/CanvasRenderingContext2D/ellipse)

Adds an elliptical arc to the current path.

[CanvasRenderingContext2D.rect()](/en-US/docs/Web/API/CanvasRenderingContext2D/rect)

Creates a path for a rectangle at position (x, y) with a size that is determined by width and height.

[CanvasRenderingContext2D.roundRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/roundRect)

Creates a path for a rectangle with rounded corners at position (x, y) with a size that is determined by width and height and radii determined by radii.

### [Filters](#filters)

[CanvasRenderingContext2D.filter](/en-US/docs/Web/API/CanvasRenderingContext2D/filter)Non-standard

Applies a CSS or SVG filter to the canvas, e.g., to change its brightness or blurriness.

## [Examples](#examples)

See full examples at [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API).

## [Specifications](#specifications)

Specification
[CSS Painting API Level 1# 2d-rendering-context](https://drafts.css-houdini.org/css-paint-api/#2d-rendering-context)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API/Guide)
- [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API)
- [Houdini APIs](/en-US/docs/Web/API/Houdini_APIs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 6, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PaintRenderingContext2D/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/paintrenderingcontext2d/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaintRenderingContext2D&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpaintrenderingcontext2d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaintRenderingContext2D%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpaintrenderingcontext2d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F315d781abffb349cbfb730b83ffeccdea980ddeb%0A*+Document+last+modified%3A+2025-02-06T06%3A00%3A53.000Z%0A%0A%3C%2Fdetails%3E)
