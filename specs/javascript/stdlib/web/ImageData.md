# ImageData

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageData&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ImageData` interface represents the underlying pixel data of an area of a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element.

It is created using the [ImageData()](/en-US/docs/Web/API/ImageData/ImageData) constructor or creator methods on the [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D) object associated with a canvas: [createImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/createImageData) and [getImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData). It can also be used to set a part of the canvas by using [putImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/putImageData).

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[ImageData()](/en-US/docs/Web/API/ImageData/ImageData)

Creates an `ImageData` object from a given [Uint8ClampedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) or [Float16Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float16Array) and the size of the image it contains. If no array is given, it creates an image of a transparent black rectangle. Note that this is the most common way to create such an object in workers as [createImageData()](/en-US/docs/Web/API/CanvasRenderingContext2D/createImageData) is not available there.

## [Instance properties](#instance_properties)

[ImageData.data](/en-US/docs/Web/API/ImageData/data)Read only

A [Uint8ClampedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) or [Float16Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float16Array) representing a one-dimensional array containing the data in the RGBA order. The order goes by rows from the top-left pixel to the bottom-right.

[ImageData.colorSpace](/en-US/docs/Web/API/ImageData/colorSpace)Read only

A string indicating the color space of the image data.

[ImageData.height](/en-US/docs/Web/API/ImageData/height)Read only

An `unsigned long` representing the actual height, in pixels, of the `ImageData`.

[ImageData.width](/en-US/docs/Web/API/ImageData/width)Read only

An `unsigned long` representing the actual width, in pixels, of the `ImageData`.

[ImageData.pixelFormat](/en-US/docs/Web/API/ImageData/pixelFormat)Read onlyExperimental

A string indicating the format to use for the `ImageData`.

## [Specifications](#specifications)

Specification
[HTML# imagedata](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#imagedata)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D)
- The [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element and its associated interface, [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ImageData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/imagedata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fimagedata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fimagedata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Feba7ce08cf50c5d9e344652748f6bcfb19f3a396%0A*+Document+last+modified%3A+2025-08-19T18%3A45%3A18.000Z%0A%0A%3C%2Fdetails%3E)
