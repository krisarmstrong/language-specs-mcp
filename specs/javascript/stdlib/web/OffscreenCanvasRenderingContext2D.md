# OffscreenCanvasRenderingContext2D

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOffscreenCanvasRenderingContext2D&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `OffscreenCanvasRenderingContext2D` interface is a [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D) rendering context for drawing to the bitmap of an `OffscreenCanvas` object. It is similar to the `CanvasRenderingContext2D` object, with the following differences:

- there is no support for user-interface features (`drawFocusIfNeeded`)
- its `canvas` attribute refers to an `OffscreenCanvas` object rather than a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element
- the bitmap for the placeholder [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element belonging to the `OffscreenCanvas` object is updated during the rendering update of the `Window` or `Worker` that owns the `OffscreenCanvas`

## In this article

- [Example](#example)
- [Additional methods](#additional_methods)
- [Unsupported features](#unsupported_features)
- [Inherited properties and methods](#inherited_properties_and_methods)
- [Unsupported properties and methods](#unsupported_properties_and_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Example](#example)

The following code snippet creates a [Worker](/en-US/docs/Web/API/Worker) object using the [Worker()](/en-US/docs/Web/API/Worker/Worker) constructor. The `transferControlToOffscreen()` method is used to get an `OffscreenCanvas` object from the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element so it can be transferred to the worker:

js

```
const canvas = document.getElementById("canvas");
const offscreen = canvas.transferControlToOffscreen();
const worker = new Worker("worker.js");
worker.postMessage({ canvas: offscreen }, [offscreen]);
```

In the worker thread, we can use the `OffscreenCanvasRenderingContext2D` to draw to the bitmap of the `OffscreenCanvas` object:

js

```
onmessage = (event) => {
  const canvas = event.data.canvas;
  const offCtx = canvas.getContext("2d");
  // draw to the offscreen canvas context
  offCtx.fillStyle = "red";
  offCtx.fillRect(0, 0, 100, 100);
};
```

For a full example, see our [OffscreenCanvas worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/offscreen-canvas-worker) ([run OffscreenCanvas worker](https://mdn.github.io/dom-examples/web-workers/offscreen-canvas-worker/)).

## [Additional methods](#additional_methods)

The following method is new to the `OffscreenCanvasRenderingContext2D` interface and does not exist in the `CanvasRenderingContext2D` interface:

[commit()](/en-US/docs/Web/API/OffscreenCanvasRenderingContext2D/commit)DeprecatedNon-standard

Pushes the rendered image to the context's `OffscreenCanvas` object's placeholder [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element.

## [Unsupported features](#unsupported_features)

The following user interface method is not supported by the `OffscreenCanvasRenderingContext2D` interface:

[CanvasRenderingContext2D.drawFocusIfNeeded()](/en-US/docs/Web/API/CanvasRenderingContext2D/drawFocusIfNeeded)

If a given element is focused, this method draws a focus ring around the current path.

## [Inherited properties and methods](#inherited_properties_and_methods)

The following properties and methods are inherited from [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D). They have the same usage as in `CanvasRenderingContext2D`

### [Context](#context)

[CanvasRenderingContext2D.getContextAttributes()](/en-US/docs/Web/API/CanvasRenderingContext2D/getContextAttributes)Experimental

Returns an object containing the actual context attributes. Context attributes can be requested with [OffscreenCanvas.getContext()](/en-US/docs/Web/API/OffscreenCanvas/getContext).

[CanvasRenderingContext2D.isContextLost()](/en-US/docs/Web/API/CanvasRenderingContext2D/isContextLost)

Returns `true` if the rendering context was lost.

### [Drawing rectangles](#drawing_rectangles)

[CanvasRenderingContext2D.clearRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/clearRect)

Sets all pixels in the rectangle defined by starting point (x, y) and size (width, height) to transparent black, erasing any previously drawn content.

[CanvasRenderingContext2D.fillRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/fillRect)

Draws a filled rectangle at (x, y) position whose size is determined by width and height.

[CanvasRenderingContext2D.strokeRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/strokeRect)

Paints a rectangle which has a starting point at (x, y) and has a w width and an h height onto the canvas, using the current stroke style.

### [Drawing text](#drawing_text)

The following methods and properties control drawing text. See also the [TextMetrics](/en-US/docs/Web/API/TextMetrics) object for text properties.

[CanvasRenderingContext2D.fillText()](/en-US/docs/Web/API/CanvasRenderingContext2D/fillText)

Draws (fills) a given text at the given (x, y) position.

[CanvasRenderingContext2D.strokeText()](/en-US/docs/Web/API/CanvasRenderingContext2D/strokeText)

Draws (strokes) a given text at the given (x, y) position.

[CanvasRenderingContext2D.measureText()](/en-US/docs/Web/API/CanvasRenderingContext2D/measureText)

Returns a [TextMetrics](/en-US/docs/Web/API/TextMetrics) object.

[CanvasRenderingContext2D.textRendering](/en-US/docs/Web/API/CanvasRenderingContext2D/textRendering)

Text rendering. Possible values: `auto` (default), `optimizeSpeed`, `optimizeLegibility`,

### [Line styles](#line_styles)

The following methods and properties control how lines are drawn.

[CanvasRenderingContext2D.lineWidth](/en-US/docs/Web/API/CanvasRenderingContext2D/lineWidth)

Width of lines. Default `1.0`.

[CanvasRenderingContext2D.lineCap](/en-US/docs/Web/API/CanvasRenderingContext2D/lineCap)

Type of endings on the end of lines. Possible values: `butt` (default), `round`, `square`.

[CanvasRenderingContext2D.lineJoin](/en-US/docs/Web/API/CanvasRenderingContext2D/lineJoin)

Defines the type of corners where two lines meet. Possible values: `round`, `bevel`, `miter` (default).

[CanvasRenderingContext2D.miterLimit](/en-US/docs/Web/API/CanvasRenderingContext2D/miterLimit)

Miter limit ratio. Default `10`.

[CanvasRenderingContext2D.getLineDash()](/en-US/docs/Web/API/CanvasRenderingContext2D/getLineDash)

Returns the current line dash pattern array containing an even number of non-negative numbers.

[CanvasRenderingContext2D.setLineDash()](/en-US/docs/Web/API/CanvasRenderingContext2D/setLineDash)

Sets the current line dash pattern.

[CanvasRenderingContext2D.lineDashOffset](/en-US/docs/Web/API/CanvasRenderingContext2D/lineDashOffset)

Specifies where to start a dash array on a line.

### [Text styles](#text_styles)

The following properties control how text is laid out.

[CanvasRenderingContext2D.font](/en-US/docs/Web/API/CanvasRenderingContext2D/font)

Font setting. Default value `10px sans-serif`.

[CanvasRenderingContext2D.textAlign](/en-US/docs/Web/API/CanvasRenderingContext2D/textAlign)

Text alignment setting. Possible values: `start` (default), `end`, `left`, `right`, `center`.

[CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline)

Baseline alignment setting. Possible values: `top`, `hanging`, `middle`, `alphabetic` (default), `ideographic`, `bottom`.

[CanvasRenderingContext2D.direction](/en-US/docs/Web/API/CanvasRenderingContext2D/direction)

Directionality. Possible values: `ltr`, `rtl`, `inherit` (default).

[CanvasRenderingContext2D.letterSpacing](/en-US/docs/Web/API/CanvasRenderingContext2D/letterSpacing)

Letter spacing. Default: `0px`.

[CanvasRenderingContext2D.fontKerning](/en-US/docs/Web/API/CanvasRenderingContext2D/fontKerning)

Font kerning. Possible values: `auto` (default), `normal`, `none`.

[CanvasRenderingContext2D.fontStretch](/en-US/docs/Web/API/CanvasRenderingContext2D/fontStretch)

Font stretch. Possible values: `ultra-condensed`, `extra-condensed`, `condensed`, `semi-condensed`, `normal` (default), `semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`.

[CanvasRenderingContext2D.fontVariantCaps](/en-US/docs/Web/API/CanvasRenderingContext2D/fontVariantCaps)

Font variant caps. Possible values: `normal` (default), `small-caps`, `all-small-caps`, `petite-caps`, `all-petite-caps`, `unicase`, `titling-caps`.

[CanvasRenderingContext2D.textRendering](/en-US/docs/Web/API/CanvasRenderingContext2D/textRendering)Experimental

Text rendering. Possible values: `auto` (default), `optimizeSpeed`, `optimizeLegibility`, `geometricPrecision`.

[CanvasRenderingContext2D.wordSpacing](/en-US/docs/Web/API/CanvasRenderingContext2D/wordSpacing)

Word spacing. Default value: `0px`

[CanvasRenderingContext2D.lang](/en-US/docs/Web/API/CanvasRenderingContext2D/lang)Experimental

Gets or sets the language of the canvas drawing context.

### [Fill and stroke styles](#fill_and_stroke_styles)

Fill styling is used for colors and styles inside shapes and stroke styling is used for the lines around shapes.

[CanvasRenderingContext2D.fillStyle](/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle)

Color or style to use inside shapes. Default to `black`.

[CanvasRenderingContext2D.strokeStyle](/en-US/docs/Web/API/CanvasRenderingContext2D/strokeStyle)

Color or style to use for the lines around shapes. Default to `black`.

### [Gradients and patterns](#gradients_and_patterns)

[CanvasRenderingContext2D.createConicGradient()](/en-US/docs/Web/API/CanvasRenderingContext2D/createConicGradient)

Creates a conic gradient around a point given by coordinates represented by the parameters.

[CanvasRenderingContext2D.createLinearGradient()](/en-US/docs/Web/API/CanvasRenderingContext2D/createLinearGradient)

Creates a linear gradient along the line given by the coordinates represented by the parameters.

[CanvasRenderingContext2D.createRadialGradient()](/en-US/docs/Web/API/CanvasRenderingContext2D/createRadialGradient)

Creates a radial gradient given by the coordinates of the two circles represented by the parameters.

[CanvasRenderingContext2D.createPattern()](/en-US/docs/Web/API/CanvasRenderingContext2D/createPattern)

Creates a pattern using the specified image. It repeats the source in the directions specified by the repetition argument. This method returns a [CanvasPattern](/en-US/docs/Web/API/CanvasPattern).

### [Shadows](#shadows)

[CanvasRenderingContext2D.shadowBlur](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowBlur)

Specifies the blurring effect. Default: `0`.

[CanvasRenderingContext2D.shadowColor](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowColor)

Color of the shadow. Default: fully-transparent black.

[CanvasRenderingContext2D.shadowOffsetX](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowOffsetX)

Horizontal distance the shadow will be offset. Default: `0`.

[CanvasRenderingContext2D.shadowOffsetY](/en-US/docs/Web/API/CanvasRenderingContext2D/shadowOffsetY)

Vertical distance the shadow will be offset. Default: `0`.

### [Paths](#paths)

The following methods can be used to manipulate paths of objects.

[CanvasRenderingContext2D.beginPath()](/en-US/docs/Web/API/CanvasRenderingContext2D/beginPath)

Starts a new path by emptying the list of sub-paths. Call this method when you want to create a new path.

[CanvasRenderingContext2D.closePath()](/en-US/docs/Web/API/CanvasRenderingContext2D/closePath)

Causes the point of the pen to move back to the start of the current sub-path. It tries to draw a straight line from the current point to the start. If the shape has already been closed or has only one point, this function does nothing.

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

### [Drawing paths](#drawing_paths)

[CanvasRenderingContext2D.fill()](/en-US/docs/Web/API/CanvasRenderingContext2D/fill)

Fills the current sub-paths with the current fill style.

[CanvasRenderingContext2D.stroke()](/en-US/docs/Web/API/CanvasRenderingContext2D/stroke)

Strokes the current sub-paths with the current stroke style.

[CanvasRenderingContext2D.clip()](/en-US/docs/Web/API/CanvasRenderingContext2D/clip)

Creates a clipping path from the current sub-paths. Everything drawn after `clip()` is called appears inside the clipping path only. For an example, see [Clipping paths](/en-US/docs/Web/API/Canvas_API/Tutorial/Compositing) in the Canvas tutorial.

[CanvasRenderingContext2D.isPointInPath()](/en-US/docs/Web/API/CanvasRenderingContext2D/isPointInPath)

Reports whether or not the specified point is contained in the current path.

[CanvasRenderingContext2D.isPointInStroke()](/en-US/docs/Web/API/CanvasRenderingContext2D/isPointInStroke)

Reports whether or not the specified point is inside the area contained by the stroking of a path.

### [Transformations](#transformations)

Objects in the `CanvasRenderingContext2D` rendering context have a current transformation matrix and methods to manipulate it. The transformation matrix is applied when creating the current default path, painting text, shapes and [Path2D](/en-US/docs/Web/API/Path2D) objects. The methods listed below remain for historical and compatibility reasons as [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) objects are used in most parts of the API nowadays and will be used in the future instead.

[CanvasRenderingContext2D.getTransform()](/en-US/docs/Web/API/CanvasRenderingContext2D/getTransform)

Retrieves the current transformation matrix being applied to the context.

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

Alpha value that is applied to shapes and images before they are composited onto the canvas. Default `1.0` (opaque).

[CanvasRenderingContext2D.globalCompositeOperation](/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation)

With `globalAlpha` applied this sets how shapes and images are drawn onto the existing bitmap.

### [Drawing images](#drawing_images)

[CanvasRenderingContext2D.drawImage()](/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage)

Draws the specified image. This method is available in multiple formats, providing a great deal of flexibility in its use.

### [Pixel manipulation](#pixel_manipulation)

See also the [ImageData](/en-US/docs/Web/API/ImageData) object.

[CanvasRenderingContext2D.createImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/createImageData)

Creates a new, blank [ImageData](/en-US/docs/Web/API/ImageData) object with the specified dimensions. All of the pixels in the new object are transparent black.

[CanvasRenderingContext2D.getImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData)

Returns an [ImageData](/en-US/docs/Web/API/ImageData) object representing the underlying pixel data for the area of the canvas denoted by the rectangle which starts at (sx, sy) and has an sw width and sh height.

[CanvasRenderingContext2D.putImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/putImageData)

Paints data from the given [ImageData](/en-US/docs/Web/API/ImageData) object onto the bitmap. If a dirty rectangle is provided, only the pixels from that rectangle are painted.

### [Image smoothing](#image_smoothing)

[CanvasRenderingContext2D.imageSmoothingEnabled](/en-US/docs/Web/API/CanvasRenderingContext2D/imageSmoothingEnabled)

Image smoothing mode; if disabled, images will not be smoothed if scaled.

[CanvasRenderingContext2D.imageSmoothingQuality](/en-US/docs/Web/API/CanvasRenderingContext2D/imageSmoothingQuality)

Allows you to set the quality of image smoothing.

### [The canvas state](#the_canvas_state)

The `CanvasRenderingContext2D` rendering context contains a variety of drawing style states (attributes for line styles, fill styles, shadow styles, text styles). The following methods help you to work with that state:

[CanvasRenderingContext2D.save()](/en-US/docs/Web/API/CanvasRenderingContext2D/save)

Saves the current drawing style state using a stack so you can revert any change you make to it using `restore()`.

[CanvasRenderingContext2D.restore()](/en-US/docs/Web/API/CanvasRenderingContext2D/restore)

Restores the drawing style state to the last element on the 'state stack' saved by `save()`.

[CanvasRenderingContext2D.canvas](/en-US/docs/Web/API/CanvasRenderingContext2D/canvas)

A read-only reference to an `OffscreenCanvas` object.

[CanvasRenderingContext2D.getContextAttributes()](/en-US/docs/Web/API/CanvasRenderingContext2D/getContextAttributes)Experimental

Returns an object containing the actual context attributes. Context attributes can be requested with [HTMLCanvasElement.getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext).

[CanvasRenderingContext2D.reset()](/en-US/docs/Web/API/CanvasRenderingContext2D/reset)

Resets the current drawing style state to the default values.

### [Filters](#filters)

[CanvasRenderingContext2D.filter](/en-US/docs/Web/API/CanvasRenderingContext2D/filter)

Applies a CSS or SVG filter to the canvas; e.g., to change its brightness or blurriness.

## [Unsupported properties and methods](#unsupported_properties_and_methods)

The following method is not supported in the `OffscreenCanvasRenderingContext2D` interface:

[CanvasRenderingContext2D.drawFocusIfNeeded()](/en-US/docs/Web/API/CanvasRenderingContext2D/drawFocusIfNeeded)

If a given element is focused, this method draws a focus ring around the current path.

## [Specifications](#specifications)

Specification
[HTML# the-offscreen-2d-rendering-context](https://html.spec.whatwg.org/multipage/canvas.html#the-offscreen-2d-rendering-context)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement)
- [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/OffscreenCanvasRenderingContext2D/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/offscreencanvasrenderingcontext2d/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOffscreenCanvasRenderingContext2D&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Foffscreencanvasrenderingcontext2d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOffscreenCanvasRenderingContext2D%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Foffscreencanvasrenderingcontext2d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbc9f7bec1ab48f29d241e38a9f1598f783f6b60a%0A*+Document+last+modified%3A+2025-08-12T01%3A00%3A18.000Z%0A%0A%3C%2Fdetails%3E)
