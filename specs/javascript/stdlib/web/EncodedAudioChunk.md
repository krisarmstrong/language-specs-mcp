# EncodedAudioChunk

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncodedAudioChunk&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `EncodedAudioChunk` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) represents a chunk of encoded audio data.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[EncodedAudioChunk()](/en-US/docs/Web/API/EncodedAudioChunk/EncodedAudioChunk)

Creates a new `EncodedAudioChunk` object.

## [Instance properties](#instance_properties)

[EncodedAudioChunk.type](/en-US/docs/Web/API/EncodedAudioChunk/type)Read only

Returns a string indicating whether this chunk of data is a key chunk.

[EncodedAudioChunk.timestamp](/en-US/docs/Web/API/EncodedAudioChunk/timestamp)Read only

Returns an integer representing the timestamp of the audio in microseconds.

[EncodedAudioChunk.duration](/en-US/docs/Web/API/EncodedAudioChunk/duration)Read only

Returns an integer representing the duration of the audio in microseconds.

[EncodedAudioChunk.byteLength](/en-US/docs/Web/API/EncodedAudioChunk/byteLength)Read only

Returns an integer representing the length of the audio in bytes.

## [Instance methods](#instance_methods)

[EncodedAudioChunk.copyTo()](/en-US/docs/Web/API/EncodedAudioChunk/copyTo)

Copies the encoded audio data.

## [Specifications](#specifications)

Specification
[WebCodecs# encodedaudiochunk-interface](https://w3c.github.io/webcodecs/#encodedaudiochunk-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/EncodedAudioChunk/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/encodedaudiochunk/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncodedAudioChunk&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fencodedaudiochunk%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncodedAudioChunk%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fencodedaudiochunk%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06b418a190b8e4a46682ab706d14984e7db34862%0A*+Document+last+modified%3A+2024-09-11T03%3A36%3A25.000Z%0A%0A%3C%2Fdetails%3E)
