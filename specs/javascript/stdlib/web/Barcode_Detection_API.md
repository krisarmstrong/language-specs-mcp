# Barcode Detection API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarcode_Detection_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Barcode Detection API detects linear and two-dimensional barcodes in images.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Support for barcode recognition within web apps unlocks a variety of use cases through supported barcode formats. QR codes can be used for online payments, web navigation or establishing social media connections, Aztec codes can be used to scan boarding passes and shopping apps can use EAN or UPC barcodes to compare prices of physical items.

Detection is achieved through the [detect()](/en-US/docs/Web/API/BarcodeDetector/detect) method, which takes an image object; it can be one of these objects: a [HTMLImageElement](/en-US/docs/Web/API/HTMLImageElement), a [SVGImageElement](/en-US/docs/Web/API/SVGImageElement), a [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement), a [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement), an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap), an [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas), a [VideoFrame](/en-US/docs/Web/API/VideoFrame), a [Blob](/en-US/docs/Web/API/Blob), or an [ImageData](/en-US/docs/Web/API/ImageData). Optional parameters can be passed to the [BarcodeDetector](/en-US/docs/Web/API/BarcodeDetector) constructor to provide hints on which barcode formats to detect.

### [Supported barcode formats](#supported_barcode_formats)

The Barcode Detection API supports the following barcode formats:

FormatDescriptionImageaztec A square two-dimensional matrix following iso24778 and with a square bullseye pattern at their center, thus resembling an Aztec pyramid. Does not require a surrounding blank zone. code_128 A linear (one-dimensional), bidirectionally-decodable, self-checking barcode following iso15417 and able to encode all 128 characters of [ASCII](/en-US/docs/Glossary/ASCII) (hence the naming). code_39 A linear (one-dimensional), self-checking barcode following iso16388. It is a discrete and variable-length barcode type. code_93 A linear, continuous symbology with a variable length following bc5. It offers a larger information density than Code 128 and the visually similar Code 39. Code 93 is used primarily by Canada Post to encode supplementary delivery information. codabar A linear barcode representing characters 0-9, A-D and symbols - . $ / + data_matrix An orientation-independent two-dimensional barcode composed of black and white modules arranged in either a square or rectangular pattern following iso16022. ean_13 A linear barcode based on the UPC-A standard and defined in iso15420. ean_8A linear barcode defined in iso15420 and derived from EAN-13.itf A continuous, self-checking, bidirectionally decodable barcode. It will always encode 14 digits. pdf417 A continuous two-dimensional barcode symbology format with multiple rows and columns. It's bi-directionally decodable and uses the iso15438 standard. qr_code A two-dimensional barcode that uses the iso18004 standard. The information encoded can be text, URL or other data. upc_a One of the most common linear barcode types and is widely applied to retail in the United States. Defined in iso15420, it represents digits by strips of bars and spaces, each digit being associated to a unique pattern of 2 bars and 2 spaces, both of variable width. UPC-A can encode 12 digits that are uniquely assigned to each trade item, and it's technically a subset of EAN-13 (UPC-A codes are represented in EAN-13 with the first character set to 0). upc_e A variation of UPC-A defined in iso15420, compressing out unnecessary zeros for a more compact barcode. unknown This value is used by the platform to signify that it does not know or specify which barcode format is being detected or supported. 

You can check for formats supported by the user agent via the [getSupportedFormats()](/en-US/docs/Web/API/BarcodeDetector/getSupportedFormats_static) method.

## [Interfaces](#interfaces)

[BarcodeDetector](/en-US/docs/Web/API/BarcodeDetector)Experimental

The `BarcodeDetector` interface of the Barcode Detection API allows detection of linear and two dimensional barcodes in images.

## [Examples](#examples)

### [Creating A Detector](#creating_a_detector)

This example tests for browser compatibility and creates a new barcode detector object, with specified supported formats.

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

The following example calls the `getSupportedFormats()` method and logs the results to the console.

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
- [The Shape Detection API: a picture is worth a thousand words, faces, and barcodes](https://developer.chrome.com/docs/capabilities/shape-detection#barcodedetector)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/Barcode_Detection_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/barcode_detection_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarcode_Detection_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbarcode_detection_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarcode_Detection_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbarcode_detection_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F41d343d684f9f6e7199d408b209bcd0e077eb023%0A*+Document+last+modified%3A+2023-12-13T09%3A03%3A37.000Z%0A%0A%3C%2Fdetails%3E)
