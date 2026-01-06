# VideoColorSpace

 Baseline  2024 Newly available

 Since ⁨September 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoColorSpace&level=low)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `VideoColorSpace` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) represents the color space of a video.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[VideoColorSpace()](/en-US/docs/Web/API/VideoColorSpace/VideoColorSpace)

Creates a new `VideoColorSpace` object.

## [Instance properties](#instance_properties)

[VideoColorSpace.primaries](/en-US/docs/Web/API/VideoColorSpace/primaries)Read only

A string containing the color primary describing the color [gamut](/en-US/docs/Glossary/Gamut) of a video sample.

[VideoColorSpace.transfer](/en-US/docs/Web/API/VideoColorSpace/transfer)

A string containing the transfer characteristics of video samples.

[VideoColorSpace.matrix](/en-US/docs/Web/API/VideoColorSpace/matrix)

A string containing the matrix coefficients describing the relationship between sample component values and color coordinates.

[VideoColorSpace.fullRange](/en-US/docs/Web/API/VideoColorSpace/fullRange)

A [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean). If `true` indicates that full-range color values are used.

## [Instance methods](#instance_methods)

[VideoColorSpace.toJSON()](/en-US/docs/Web/API/VideoColorSpace/toJSON)

Returns a JSON representation of the `VideoColorSpace` object.

## [Examples](#examples)

In the following example, `colorSpace` is a `VideoColorSpace` object returned from [VideoFrame](/en-US/docs/Web/API/VideoFrame). The object is then printed to the console.

js

```
let colorSpace = VideoFrame.colorSpace;
console.log(colorSpace);
```

## [Specifications](#specifications)

Specification
[WebCodecs# videocolorspace](https://w3c.github.io/webcodecs/#videocolorspace)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VideoColorSpace/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videocolorspace/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoColorSpace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideocolorspace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoColorSpace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideocolorspace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3789de65bd11453c4cb24625723f81a7e8fcdd56%0A*+Document+last+modified%3A+2024-05-08T04%3A36%3A35.000Z%0A%0A%3C%2Fdetails%3E)
