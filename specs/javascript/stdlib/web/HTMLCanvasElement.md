# HTMLCanvasElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLCanvasElement&level=high)

The `HTMLCanvasElement` interface provides properties and methods for manipulating the layout and presentation of [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) elements. The `HTMLCanvasElement` interface also inherits the properties and methods of the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLCanvasElement.height](/en-US/docs/Web/API/HTMLCanvasElement/height)

The [height](/en-US/docs/Web/HTML/Reference/Elements/canvas#height) HTML attribute of the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element is a non-negative `integer` reflecting the number of logical pixels (or RGBA values) going down one column of the canvas. When the attribute is not specified, or if it is set to an invalid value, like a negative, the default value of `150` is used. If no [separate] CSS height is assigned to the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas), then this value will also be used as the height of the canvas in the length-unit CSS Pixel.

[HTMLCanvasElement.width](/en-US/docs/Web/API/HTMLCanvasElement/width)

The [width](/en-US/docs/Web/HTML/Reference/Elements/canvas#width) HTML attribute of the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element is a non-negative `integer` reflecting the number of logical pixels (or RGBA values) going across one row of the canvas. When the attribute is not specified, or if it is set to an invalid value, like a negative, the default value of `300` is used. If no [separate] CSS width is assigned to the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas), then this value will also be used as the width of the canvas in the length-unit CSS Pixel.

[HTMLCanvasElement.mozOpaque](/en-US/docs/Web/API/HTMLCanvasElement/mozOpaque)Non-standardDeprecated

A boolean value reflecting the [moz-opaque](/en-US/docs/Web/HTML/Reference/Elements/canvas#moz-opaque) HTML attribute of the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element. It lets the canvas know whether or not translucency will be a factor. If the canvas knows there's no translucency, painting performance can be optimized. This is only supported in Mozilla-based browsers; use the standardized [canvas.getContext('2d', { alpha: false })](/en-US/docs/Web/API/HTMLCanvasElement/getContext) instead.

`HTMLCanvasElement.mozPrintCallback`Non-standard

A `function` that is Initially null. Web content can set this to a JavaScript function that will be called when the canvas is to be redrawn while the page is being printed. When called, the callback is passed a "printState" object that implements the [MozCanvasPrintState](https://searchfox.org/firefox-main/search?q=interface%20MozCanvasPrintState&path=HTMLCanvasElement.webidl) interface. The callback can get the context to draw to from the printState object and must then call done() on it when finished. The purpose of `mozPrintCallback` is to obtain a higher resolution rendering of the canvas at the resolution of the printer being used. [See this blog post.](https://blog.mozilla.org/labs/2012/09/a-new-way-to-control-printing-output/)

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLCanvasElement.captureStream()](/en-US/docs/Web/API/HTMLCanvasElement/captureStream)

Returns a [CanvasCaptureMediaStreamTrack](/en-US/docs/Web/API/CanvasCaptureMediaStreamTrack) that is a real-time video capture of the surface of the canvas.

[HTMLCanvasElement.getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext)

Returns a drawing context on the canvas, or [null](/en-US/docs/Web/JavaScript/Reference/Operators/null) if the context identifier is not supported, or the canvas has already been set to a different context mode.

[HTMLCanvasElement.toDataURL()](/en-US/docs/Web/API/HTMLCanvasElement/toDataURL)

Returns a data-URL containing a representation of the image in the format specified by the `type` parameter (defaults to `png`). The returned image is in a resolution of 96dpi.

[HTMLCanvasElement.toBlob()](/en-US/docs/Web/API/HTMLCanvasElement/toBlob)

Creates a [Blob](/en-US/docs/Web/API/Blob) object representing the image contained in the canvas; this file may be cached on the disk or stored in memory at the discretion of the user agent.

[HTMLCanvasElement.transferControlToOffscreen()](/en-US/docs/Web/API/HTMLCanvasElement/transferControlToOffscreen)

Transfers control to an [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas) object, either on the main thread or on a worker.

## [Events](#events)

Inherits events from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[contextlost](/en-US/docs/Web/API/HTMLCanvasElement/contextlost_event)

Fired if the browser detects that the `CanvasRenderingContext2D` context has been lost.

[contextrestored](/en-US/docs/Web/API/HTMLCanvasElement/contextrestored_event)

Fired if the browser successfully restores a `CanvasRenderingContext2D` context

[webglcontextcreationerror](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextcreationerror_event)

Fired if the user agent is unable to create a `WebGLRenderingContext` or `WebGL2RenderingContext` context.

[webglcontextlost](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event)

Fired if the user agent detects that the drawing buffer associated with a `WebGLRenderingContext` or `WebGL2RenderingContext` object has been lost.

[webglcontextrestored](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event)

Fired if the user agent restores the drawing buffer for a `WebGLRenderingContext` or `WebGL2RenderingContext` object.

## [Specifications](#specifications)

Specification
[HTML# htmlcanvaselement](https://html.spec.whatwg.org/multipage/canvas.html#htmlcanvaselement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLCanvasElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlcanvaselement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLCanvasElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlcanvaselement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLCanvasElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlcanvaselement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F886f2641ae90a70858c5e7d0d20959c70ee44d9d%0A*+Document+last+modified%3A+2025-08-20T01%3A23%3A27.000Z%0A%0A%3C%2Fdetails%3E)
