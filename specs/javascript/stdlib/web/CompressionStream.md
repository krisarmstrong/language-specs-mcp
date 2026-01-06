# CompressionStream

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompressionStream&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `CompressionStream` interface of the [Compression Streams API](/en-US/docs/Web/API/Compression_Streams_API) compresses a stream of data. It implements the same shape as a [TransformStream](/en-US/docs/Web/API/TransformStream), allowing it to be used in [ReadableStream.pipeThrough()](/en-US/docs/Web/API/ReadableStream/pipeThrough) and similar methods.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CompressionStream()](/en-US/docs/Web/API/CompressionStream/CompressionStream)

Creates a new `CompressionStream`.

## [Instance properties](#instance_properties)

[CompressionStream.readable](/en-US/docs/Web/API/CompressionStream/readable)

Returns the [ReadableStream](/en-US/docs/Web/API/ReadableStream) instance controlled by this object.

[CompressionStream.writable](/en-US/docs/Web/API/CompressionStream/writable)

Returns the [WritableStream](/en-US/docs/Web/API/WritableStream) instance controlled by this object.

## [Examples](#examples)

In this example a stream is compressed using gzip compression.

js

```
const compressedReadableStream = inputReadableStream.pipeThrough(
  new CompressionStream("gzip"),
);
```

## [Specifications](#specifications)

Specification
[Compression# compression-stream](https://compression.spec.whatwg.org/#compression-stream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DecompressionStream](/en-US/docs/Web/API/DecompressionStream)
- [TransformStream](/en-US/docs/Web/API/TransformStream)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CompressionStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/compressionstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompressionStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcompressionstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompressionStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcompressionstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fae6626ec9a5729a51f202b77586f37958088ed77%0A*+Document+last+modified%3A+2025-11-26T01%3A57%3A30.000Z%0A%0A%3C%2Fdetails%3E)
