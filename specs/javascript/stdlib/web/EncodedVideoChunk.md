# EncodedVideoChunk

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncodedVideoChunk&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `EncodedVideoChunk` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) represents a chunk of encoded video data.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[EncodedVideoChunk()](/en-US/docs/Web/API/EncodedVideoChunk/EncodedVideoChunk)

Creates a new `EncodedVideoChunk` object.

## [Instance properties](#instance_properties)

[EncodedVideoChunk.type](/en-US/docs/Web/API/EncodedVideoChunk/type)Read only

Returns a string indicating whether this chunk of data is a key chunk.

[EncodedVideoChunk.timestamp](/en-US/docs/Web/API/EncodedVideoChunk/timestamp)Read only

Returns an integer representing the timestamp of the video in microseconds.

[EncodedVideoChunk.duration](/en-US/docs/Web/API/EncodedVideoChunk/duration)Read only

Returns an integer representing the duration of the video in microseconds.

[EncodedVideoChunk.byteLength](/en-US/docs/Web/API/EncodedVideoChunk/byteLength)Read only

Returns an integer representing the length of the video in bytes.

## [Instance methods](#instance_methods)

[EncodedVideoChunk.copyTo()](/en-US/docs/Web/API/EncodedVideoChunk/copyTo)

Copies the encoded video data.

## [Specifications](#specifications)

Specification
[WebCodecs# encodedvideochunk-interface](https://w3c.github.io/webcodecs/#encodedvideochunk-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/EncodedVideoChunk/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/encodedvideochunk/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncodedVideoChunk&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fencodedvideochunk%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncodedVideoChunk%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fencodedvideochunk%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3789de65bd11453c4cb24625723f81a7e8fcdd56%0A*+Document+last+modified%3A+2024-05-08T04%3A36%3A35.000Z%0A%0A%3C%2Fdetails%3E)
