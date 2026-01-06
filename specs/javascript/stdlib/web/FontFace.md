# FontFace

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFace&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FontFace` interface of the [CSS Font Loading API](/en-US/docs/Web/API/CSS_Font_Loading_API) represents a single usable font face.

This interface defines the source of a font face, either a URL to an external resource or a buffer, and font properties such as `style`, `weight`, and so on. For URL font sources it allows authors to trigger when the remote font is fetched and loaded, and to track loading status.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FontFace()](/en-US/docs/Web/API/FontFace/FontFace)

Constructs and returns a new `FontFace` object, built from an external resource described by a URL or from an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer).

## [Instance properties](#instance_properties)

[FontFace.ascentOverride](/en-US/docs/Web/API/FontFace/ascentOverride)

A string that retrieves or sets the ascent metric of the font. It is equivalent to the [ascent-override](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override) descriptor.

[FontFace.descentOverride](/en-US/docs/Web/API/FontFace/descentOverride)

A string that retrieves or sets the descent metric of the font. It is equivalent to the [descent-override](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/descent-override) descriptor.

[FontFace.display](/en-US/docs/Web/API/FontFace/display)

A string that determines how a font face is displayed based on whether and when it is downloaded and ready to use.

[FontFace.family](/en-US/docs/Web/API/FontFace/family)

A string that retrieves or sets the family of the font. It is equivalent to the [font-family](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family) descriptor.

[FontFace.featureSettings](/en-US/docs/Web/API/FontFace/featureSettings)

A string that retrieves or sets infrequently used font features that are not available from a font's variant properties. It is equivalent to the CSS [font-feature-settings](/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings) property.

[FontFace.lineGapOverride](/en-US/docs/Web/API/FontFace/lineGapOverride)

A string that retrieves or sets the line-gap metric of the font. It is equivalent to the [line-gap-override](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/line-gap-override) descriptor.

[FontFace.loaded](/en-US/docs/Web/API/FontFace/loaded)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the current `FontFace` object when the font specified in the object's constructor is done loading or rejects with a `SyntaxError`[DOMException](/en-US/docs/Web/API/DOMException).

[FontFace.status](/en-US/docs/Web/API/FontFace/status)Read only

Returns an enumerated value indicating the status of the font, one of `"unloaded"`, `"loading"`, `"loaded"`, or `"error"`.

[FontFace.stretch](/en-US/docs/Web/API/FontFace/stretch)

A string that retrieves or sets how the font stretches. It is equivalent to the [font-stretch](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch) descriptor.

[FontFace.style](/en-US/docs/Web/API/FontFace/style)

A string that retrieves or sets the style of the font. It is equivalent to the [font-style](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style) descriptor.

[FontFace.unicodeRange](/en-US/docs/Web/API/FontFace/unicodeRange)

A string that retrieves or sets the range of unicode code points encompassing the font. It is equivalent to the [unicode-range](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range) descriptor.

[FontFace.variant](/en-US/docs/Web/API/FontFace/variant)Non-standard

A string that retrieves or sets the variant of the font.

[FontFace.variationSettings](/en-US/docs/Web/API/FontFace/variationSettings)

A string that retrieves or sets the variation settings of the font. It is equivalent to the [font-variation-settings](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings) descriptor.

[FontFace.weight](/en-US/docs/Web/API/FontFace/weight)

A string that contains the weight of the font. It is equivalent to the [font-weight](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight) descriptor.

[FontFace.load()](/en-US/docs/Web/API/FontFace/load)

Loads a font based on current object's constructor-passed requirements, including a location or source buffer, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the current FontFace object.

## [Examples](#examples)

The code below defines a font face using data at the URL "my-font.woff" with a few font descriptors. Just to show how it works, we then define the `stretch` descriptor using a property.

js

```
// Define a FontFace
const font = new FontFace("my-font", 'url("my-font.woff")', {
  style: "italic",
  weight: "400",
});

font.stretch = "condensed";
```

Next we load the font using [FontFace.load()](/en-US/docs/Web/API/FontFace/load) and use the returned promise to track completion or report an error.

js

```
// Load the font
font.load().then(
  () => {
    // Resolved - add font to document.fonts
  },
  (err) => {
    console.error(err);
  },
);
```

To actually use the font we will need to add it to a [FontFaceSet](/en-US/docs/Web/API/FontFaceSet). We could do that before or after loading the font.

For additional examples see [CSS Font Loading API > Examples](/en-US/docs/Web/API/CSS_Font_Loading_API#examples).

## [Specifications](#specifications)

Specification
[CSS Font Loading Module Level 3# fontface-interface](https://drafts.csswg.org/css-font-loading/#fontface-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@font-face](/en-US/docs/Web/CSS/Reference/At-rules/@font-face)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FontFace/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fontface/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffontface%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffontface%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
