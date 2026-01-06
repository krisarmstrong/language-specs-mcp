# ImageBitmapRenderingContext

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageBitmapRenderingContext&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ImageBitmapRenderingContext` interface is a canvas rendering context that provides the functionality to replace the canvas's contents with the given [ImageBitmap](/en-US/docs/Web/API/ImageBitmap). Its context id (the first argument to [HTMLCanvasElement.getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext) or [OffscreenCanvas.getContext()](/en-US/docs/Web/API/OffscreenCanvas/getContext)) is `"bitmaprenderer"`.

This interface is available in both the window and the [worker](/en-US/docs/Web/API/Web_Workers_API) context.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[ImageBitmapRenderingContext.canvas](/en-US/docs/Web/API/ImageBitmapRenderingContext/canvas)Read only

A read-only reference to the [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement) or [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas) object that is associated with the given context.

## [Instance methods](#instance_methods)

[ImageBitmapRenderingContext.transferFromImageBitmap()](/en-US/docs/Web/API/ImageBitmapRenderingContext/transferFromImageBitmap)

Displays the given `ImageBitmap` in the canvas associated with this rendering context. Ownership of the `ImageBitmap` is transferred to the canvas. This was previously named `transferImageBitmap()`, but was renamed in a spec change. The old name is being kept as an alias to avoid code breakage.

## [Specifications](#specifications)

Specification
[HTML# the-imagebitmaprenderingcontext-interface](https://html.spec.whatwg.org/multipage/canvas.html#the-imagebitmaprenderingcontext-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 23, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ImageBitmapRenderingContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/imagebitmaprenderingcontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageBitmapRenderingContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fimagebitmaprenderingcontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageBitmapRenderingContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fimagebitmaprenderingcontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3610b480fe28dcab6de41edb95300ad9be9b5777%0A*+Document+last+modified%3A+2024-08-23T04%3A57%3A34.000Z%0A%0A%3C%2Fdetails%3E)
