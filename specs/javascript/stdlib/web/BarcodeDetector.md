# BarcodeDetector

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarcodeDetector&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `BarcodeDetector` interface of the [Barcode Detection API](/en-US/docs/Web/API/Barcode_Detection_API) allows detection of linear and two dimensional barcodes in images.

## In this article

- [Constructors](#constructors)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[BarcodeDetector.BarcodeDetector()](/en-US/docs/Web/API/BarcodeDetector/BarcodeDetector)Experimental

Creates and returns a `BarcodeDetector` object, with optional `BarcodeDetectorOptions`.

## [Static methods](#static_methods)

[getSupportedFormats()](/en-US/docs/Web/API/BarcodeDetector/getSupportedFormats_static)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which fulfills with an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of supported [barcode format types](/en-US/docs/Web/API/Barcode_Detection_API#supported_barcode_formats).

## [Instance methods](#instance_methods)

[detect()](/en-US/docs/Web/API/BarcodeDetector/detect)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which fulfills with an array of `DetectedBarcode` objects with the following properties:

- `boundingBox`: A [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly), which returns the dimensions of a rectangle representing the extent of a detected barcode, aligned with the image.
- `cornerPoints`: The x and y co-ordinates of the four corner points of the detected barcode relative to the image, starting with the top left and working clockwise. This may not be square due to perspective distortions within the image.
- `format`: The detected barcode format. (For a full list of formats, consult the [supported barcode format](/en-US/docs/Web/API/Barcode_Detection_API#supported_barcode_formats)) list.
- `rawValue`: A string decoded from the barcode data.

## [Examples](#examples)

### [Creating A Detector](#creating_a_detector)

This example creates a new barcode detector object, with specified supported formats and tests for browser compatibility.

js

```
// check compatibility
if (!("BarcodeDetector" in globalThis)) {
  console.log("Barcode Detector is not supported by this browser.");
} else {
  console.log("Barcode Detector supported!");

  // create new detector
  const barcodeDetector = new BarcodeDetector({
    formats: ["code_39", "codabar", "ean_13"],
  });
}
```

### [Getting Supported Formats](#getting_supported_formats)

The following example calls the `getSupportFormat()` static method and logs the results to the console.

js

```
// check supported types
BarcodeDetector.getSupportedFormats().then((supportedFormats) => {
  supportedFormats.forEach((format) => console.log(format));
});
```

### [Detect Barcodes](#detect_barcodes)

This example uses the `detect()` method to detect the barcodes within the given image. These are iterated over and the barcode data is logged to the console.

js

```
barcodeDetector
  .detect(imageEl)
  .then((barcodes) => {
    barcodes.forEach((barcode) => console.log(barcode.rawValue));
  })
  .catch((err) => {
    console.log(err);
  });
```

## [Specifications](#specifications)

Specification
[Accelerated Shape Detection in Images# barcode-detection-api](https://wicg.github.io/shape-detection-api/#barcode-detection-api)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [barcodefaq.com: A website with information about different barcodes and examples of the different types.](https://www.barcodefaq.com/)
- [Accelerated Shape Detection in Images](https://developer.chrome.com/docs/capabilities/shape-detection#barcodedetector)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/BarcodeDetector/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/barcodedetector/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarcodeDetector&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbarcodedetector%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarcodeDetector%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbarcodedetector%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
