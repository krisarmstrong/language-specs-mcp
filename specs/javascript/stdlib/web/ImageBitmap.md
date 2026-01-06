# ImageBitmap

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageBitmap&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ImageBitmap` interface represents a bitmap image which can be drawn to a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) without undue latency. It can be created from a variety of source objects using the [Window.createImageBitmap()](/en-US/docs/Web/API/Window/createImageBitmap) or [WorkerGlobalScope.createImageBitmap()](/en-US/docs/Web/API/WorkerGlobalScope/createImageBitmap) factory method. `ImageBitmap` provides an asynchronous and resource efficient pathway to prepare textures for rendering in WebGL.

`ImageBitmap` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[ImageBitmap.height](/en-US/docs/Web/API/ImageBitmap/height)Read only

An `unsigned long` representing the height, in CSS pixels, of the `ImageBitmap`.

[ImageBitmap.width](/en-US/docs/Web/API/ImageBitmap/width)Read only

An `unsigned long` representing the width, in CSS pixels, of the `ImageBitmap`.

## [Instance methods](#instance_methods)

[ImageBitmap.close()](/en-US/docs/Web/API/ImageBitmap/close)

Disposes of all graphical resources associated with an `ImageBitmap`.

## [Specifications](#specifications)

Specification
[HTML# imagebitmap](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#imagebitmap)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Window.createImageBitmap](/en-US/docs/Web/API/Window/createImageBitmap)
- [WorkerGlobalScope.createImageBitmap](/en-US/docs/Web/API/WorkerGlobalScope/createImageBitmap)
- [CanvasRenderingContext2D.drawImage()](/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage)
- [WebGLRenderingContext.texImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/texImage2D)
- [OffscreenCanvas.transferToImageBitmap()](/en-US/docs/Web/API/OffscreenCanvas/transferToImageBitmap)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ImageBitmap/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/imagebitmap/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageBitmap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fimagebitmap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageBitmap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fimagebitmap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd030ae03d26d003beea8069d29cce1d3cbeaaadc%0A*+Document+last+modified%3A+2025-05-16T00%3A03%3A27.000Z%0A%0A%3C%2Fdetails%3E)
